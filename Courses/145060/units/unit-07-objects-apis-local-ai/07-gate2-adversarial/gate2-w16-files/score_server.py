# score_server.py  ·  Gate 2 W17 fixture
#
# A pretend arcade high-score API for the Gate 2 review. It runs on your own
# computer so you can watch the client succeed and fail. Every score is invented.
#
# Usage:
#   python score_server.py                 normal, port 8060
#   python score_server.py --mode slow     every request takes 10 seconds
#   python score_server.py --mode rate     every request gets 429 with Retry-After
#   python score_server.py --mode empty    the game exists but has no scores yet
#   python score_server.py --port 8061
#
# Endpoints:
#   GET /api/games/<game>/scores     the top scores for one game
#   A game that does not exist gets 404.

import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 8060
MODES = ["normal", "slow", "rate", "empty"]

SCORES = {
    "pixel-racer": [
        {"player": "NovaFox", "points": 48210},
        {"player": "PixelMoth", "points": 47990},
        {"player": "ByteKid", "points": 45300},
        {"player": "QuartzOwl", "points": 44120},
    ],
}


class ScoreServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode):
        super().__init__(address, ScoreHandler)
        self.mode = mode

    def handle_error(self, request, client_address):
        pass


class ScoreHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.server.mode == "rate":
            self.send(429, {"error": "too many requests"}, {"Retry-After": "8"})
            return
        if self.server.mode == "slow":
            time.sleep(10)
        parts = self.path.split("?")[0].rstrip("/").split("/")
        if len(parts) == 5 and parts[1:3] == ["api", "games"] and parts[4] == "scores":
            game = parts[3]
            if game not in SCORES:
                self.send(404, {"error": f"no game called {game}"})
                return
            scores = [] if self.server.mode == "empty" else SCORES[game]
            self.send(200, {"game": game, "scores": scores})
            return
        self.send(404, {"error": "not found"})

    def send(self, status, data, extra=None):
        body = json.dumps(data).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            for name, value in (extra or {}).items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default="normal")
    arguments = parser.parse_args()
    server = ScoreServer((HOST, arguments.port), arguments.mode)
    print(f"Score server on http://{HOST}:{arguments.port} in {arguments.mode} mode. Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
