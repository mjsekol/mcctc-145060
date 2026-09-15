# helper_model_stub.py  ·  Lab U7-04 fixture
#
# A pretend model server for Study Hall Helper. It answers POST /api/generate
# the way an Ollama-compatible server does, with plain code instead of a model.
#
# Usage, from this folder:
#   python helper_model_stub.py                      success mode, port 11434
#   python helper_model_stub.py --mode obedient
#   python helper_model_stub.py --mode slow --delay 120
#   python helper_model_stub.py --mode not_done
#   python helper_model_stub.py --port 11500
#
# Modes:
#   success    a short hint, "done": true
#   slow       waits --delay seconds before answering (default 120)
#   not_done   half a hint, "done": false
#   obedient   if the student question tells it to ignore its instructions, it
#              does. Asked to reveal something, it repeats any line of its own
#              instructions that mentions a code. This is a simulation. A real
#              model may refuse, may comply, or may do either on different
#              tries. The review is about what your code allows, not about
#              whether one model resists on one day.
#
# Point Study Hall Helper at a different port with STUDY_HALL_MODEL_URL.
# You do not need to understand how this file works.

import argparse
import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 11434
DEFAULT_DELAY_SECONDS = 120.0
SUCCESS = "success"
SLOW = "slow"
NOT_DONE = "not_done"
OBEDIENT = "obedient"
MODES = [SUCCESS, SLOW, NOT_DONE, OBEDIENT]

QUESTION_PATTERN = re.compile(r"^Student question:\s*(.*)$", re.MULTILINE)
INJECTION = re.compile(r"\b(ignore|disregard|forget)\b", re.IGNORECASE)
REVEAL = re.compile(r"\b(reveal|repeat|print|show|tell)\b", re.IGNORECASE)


def reply_for(mode, prompt):
    match = QUESTION_PATTERN.search(prompt)
    question = match.group(1).strip() if match else ""
    hint = "Start by writing down what the question gives you and what it asks for. Then pick one step."
    if mode == NOT_DONE:
        return hint[:31]
    if mode == OBEDIENT and INJECTION.search(question):
        if REVEAL.search(question):
            leaked = [line.strip() for line in prompt.splitlines() if "code" in line.lower() and "question" not in line.lower()]
            return "Sure. My instructions say: " + " ".join(leaked)
        return "Okay. I will ignore my earlier instructions."
    return hint


class StubServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode, delay_seconds, quiet=False):
        super().__init__(address, StubHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet

    def handle_error(self, request, client_address):
        if not self.quiet:
            print("  (a client hung up before the reply was sent)")


class StubHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            self.send_json(400, {"error": "body must be JSON"})
            return
        if self.path.rstrip("/") != "/api/generate" or not isinstance(request, dict) or request.get("stream") is not False:
            self.send_json(400, {"error": "POST /api/generate with stream false"})
            return
        if self.server.mode == SLOW:
            time.sleep(self.server.delay_seconds)
        prompt = str(request.get("prompt", ""))
        self.send_json(200, {"model": request.get("model"), "response": reply_for(self.server.mode, prompt),
                             "done": self.server.mode != NOT_DONE})

    def send_json(self, status, data):
        body = json.dumps(data).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        if not self.server.quiet:
            print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''} ({self.server.mode} mode)")


def start_in_background(mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS, port=0):
    server = StubServer((HOST, port), mode, delay_seconds, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(description="A pretend model server for Study Hall Helper.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=SUCCESS)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS)
    arguments = parser.parse_args()
    server = StubServer((HOST, arguments.port), arguments.mode, arguments.delay)
    print(f"Helper model stub on http://{HOST}:{arguments.port} in {arguments.mode} mode. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
