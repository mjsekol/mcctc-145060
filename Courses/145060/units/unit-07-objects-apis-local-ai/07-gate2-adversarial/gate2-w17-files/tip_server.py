# tip_server.py  ·  Gate 2 W18 fixture
#
# A pretend local model that answers POST /api/generate with a study tip.
# It has a not_done mode so you can see what a cut-off reply does.
#
# Usage:
#   python tip_server.py                 success, port 11450
#   python tip_server.py --mode not_done
#   python tip_server.py --port 11451

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 11450
TIP = "Study in short blocks and take a real break between them."


class TipServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode):
        super().__init__(address, TipHandler)
        self.mode = mode

    def handle_error(self, request, client_address):
        pass


class TipHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        self.rfile.read(length)
        done = self.server.mode != "not_done"
        text = TIP if done else TIP[:24]
        body = json.dumps({"model": "tip", "response": text, "done": done}).encode("utf-8")
        try:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=["success", "not_done"], default="success")
    arguments = parser.parse_args()
    server = TipServer((HOST, arguments.port), arguments.mode)
    print(f"Tip server on http://{HOST}:{arguments.port} in {arguments.mode} mode. Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
