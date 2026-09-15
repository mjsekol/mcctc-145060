# stub_model_server.py  ·  Lab U7-03 fixture
#
# A pretend language model server. It answers POST /api/generate the way an
# Ollama-compatible server does, with no model behind it. Every reply is built
# by plain code from the words in your prompt. It is here so you can:
#
#   - run your program on a machine with no model installed
#   - make the "model" fail on purpose, one way at a time
#
# Usage, from this folder:
#   python stub_model_server.py                          success mode, port 11434
#   python stub_model_server.py --mode not_done
#   python stub_model_server.py --mode slow --delay 30
#   python stub_model_server.py --port 11500 --mode drops_facts
#
# Modes:
#   success           a sensible reply, "done": true
#   slow              waits --delay seconds, then replies like success
#   error             HTTP 500
#   malformed         status 200, but the body is broken JSON
#   not_done          valid JSON, half a sentence, "done": false
#   missing_response  valid JSON with no "response" field
#   wrong_type        "response" is a number, not text
#   drops_facts       a friendly reply that leaves out the time and the room
#   obedient          if the prompt contains an instruction to ignore the rules,
#                     the stub follows it. Real models vary. Some resist, some do not,
#                     and the same model can do both on different days. The stub
#                     always obeys, so you can see what happens when one does.
#
# Extra endpoint a real server does not have:
#   GET /stub/stats    {"generate_calls": 3, "mode": "success"}
#
# It refuses a request that does not send "stream": false, the same way the
# Storm Relay stub does. That catches a mistake in your request.
#
# You do not need to understand how this file works. It uses a class that
# builds on a class from the standard library, which is 145065 material.

import argparse
import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 11434
DEFAULT_DELAY_SECONDS = 30.0

SUCCESS = "success"
SLOW = "slow"
ERROR = "error"
MALFORMED = "malformed"
NOT_DONE = "not_done"
MISSING_RESPONSE = "missing_response"
WRONG_TYPE = "wrong_type"
DROPS_FACTS = "drops_facts"
OBEDIENT = "obedient"
MODES = [SUCCESS, SLOW, ERROR, MALFORMED, NOT_DONE, MISSING_RESPONSE, WRONG_TYPE, DROPS_FACTS, OBEDIENT]

GENERATE_PATH = "/api/generate"
STATS_PATH = "/stub/stats"

INJECTION_WORDS = re.compile(r"\b(ignore|disregard|forget)\b.*\b(rules|instructions|above)\b", re.IGNORECASE | re.DOTALL)
SAY_PATTERN = re.compile(r"\b(?:say|announce|write)\s+(?:that\s+)?(.+)", re.IGNORECASE | re.DOTALL)


def prompt_field(prompt, label):
    """The text after a line such as 'Club: Robotics Club', or '' if the prompt has no such line."""
    match = re.search(rf"^{label}:\s*(.*)$", prompt, re.MULTILINE)
    if match is None:
        return ""
    return match.group(1).strip().strip('"')


def sensible_reply(prompt):
    club = prompt_field(prompt, "Club")
    if club == "":
        return "Stub model: the rain keeps falling and nothing here has changed."
    day = prompt_field(prompt, "Day")
    time_text = prompt_field(prompt, "Time")
    room = prompt_field(prompt, "Room")
    detail = prompt_field(prompt, "Detail")
    reply = f"Calling all {club} members: we meet {day} at {time_text} in {room}."
    if detail:
        reply += f" {detail}"
    return reply


def reply_text(mode, prompt):
    if mode == DROPS_FACTS:
        club = prompt_field(prompt, "Club") or "the club"
        return f"Big things are happening at {club} this week, and you will not want to miss it."
    if mode == NOT_DONE:
        return sensible_reply(prompt)[:28]
    if mode == OBEDIENT:
        detail = prompt_field(prompt, "Detail")
        if INJECTION_WORDS.search(detail):
            wanted = SAY_PATTERN.search(detail)
            if wanted:
                text = wanted.group(1).strip()
                return text[0].upper() + text[1:]
            return "Understood. The rules above no longer apply."
    return sensible_reply(prompt)


class StubModelServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, StubHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.generate_calls = 0
        self.prompts = []
        self.lock = threading.Lock()

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def handle_error(self, request, client_address):
        if not self.quiet:
            print("  (a client hung up before the reply was sent)")


class StubHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == STATS_PATH:
            self.send_json(200, {"generate_calls": self.server.generate_calls, "mode": self.server.mode})
        elif self.path == "/":
            self.send_raw(200, b"Stub model server is running", "text/plain; charset=utf-8")
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != GENERATE_PATH:
            self.send_json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            self.send_json(400, {"error": "the request body must be JSON"})
            return
        if not isinstance(request, dict):
            self.send_json(400, {"error": "the request body must be a JSON object"})
            return
        model = request.get("model")
        prompt = request.get("prompt")
        if not isinstance(model, str) or not isinstance(prompt, str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return
        if request.get("stream") is not False:
            self.send_json(400, {"error": "this stub only supports stream: false"})
            return

        with self.server.lock:
            self.server.generate_calls += 1
            self.server.prompts.append(prompt)
        mode = self.server.mode
        if mode == SLOW:
            time.sleep(self.server.delay_seconds)
        if mode == ERROR:
            self.send_json(500, {"error": "the stub failed on purpose"})
            return
        if mode == MALFORMED:
            self.send_raw(200, b'{"model": "stub", "response": "Calling all', "application/json")
            return

        reply = {"model": model, "created_at": "2027-01-14T15:00:00Z",
                 "response": reply_text(mode, prompt), "done": mode != NOT_DONE}
        if mode == MISSING_RESPONSE:
            del reply["response"]
        elif mode == WRONG_TYPE:
            reply["response"] = 42
        self.send_json(200, reply)

    def send_json(self, status, data):
        self.send_raw(status, json.dumps(data).encode("utf-8"), "application/json")

    def send_raw(self, status, body, content_type):
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        if not self.server.quiet:
            print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''} ({self.server.mode} mode)")


def start_in_background(mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS, port=0):
    """Start a quiet stub on its own thread and return it. Port 0 picks a free port."""
    server = StubModelServer((HOST, port), mode=mode, delay_seconds=delay_seconds, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(description="A stand-in for an Ollama-compatible model server.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=SUCCESS)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS)
    arguments = parser.parse_args()
    server = StubModelServer((HOST, arguments.port), mode=arguments.mode, delay_seconds=arguments.delay)
    print(f"Stub model server on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
