# weather_station_server.py  ·  Lab U7-02 fixture
#
# A pretend weather station feed for the district's practice fields. It runs
# on your own computer, so you can practise talking to an API, and practise
# watching it fail, without touching a real service. The stations and every
# reading are invented.
#
# Usage, from this folder:
#   python weather_station_server.py                    normal mode, port 8070
#   python weather_station_server.py --mode slow        every data request takes 15 seconds
#   python weather_station_server.py --mode slow --delay 40
#   python weather_station_server.py --mode error       every data request fails with HTTP 500
#   python weather_station_server.py --port 8071        a different port
#   python weather_station_server.py --key NOT-A-REAL-KEY-practice
#
# Leave this terminal open while your program runs in a second terminal.
# Press Ctrl+C here to stop the server.
#
# You do not need to understand how this file works. It uses a class that
# builds on a class from the standard library, which is 145065 material.
# What you need to know is how it behaves, because it behaves like a real feed:
#
#   GET /api/v1/stations                          the list of stations
#   GET /api/v1/stations/<id>/observations        readings from the last hour, newest first
#   GET /api/v1/stations/<id>/lightning           needs the header X-Feed-Key
#
#   - A station id that does not exist gets 404 Not Found.
#   - A path that does not exist gets a 404 web page, not JSON.
#   - More than 5 requests in 10 seconds gets 429 Too Many Requests, with a
#     Retry-After header saying how many seconds to wait.
#   - The lightning endpoint without the right key gets 401 Unauthorized.
#   - The feed key changes every time the server starts, unless you give one
#     with --key. That is on purpose. A key typed into your code would break
#     tomorrow, and it would be sitting in your repository forever.
#   - It only answers requests from this computer.

import argparse
import json
import math
import secrets
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 8070
DEFAULT_DELAY_SECONDS = 15.0
DEFAULT_LIMIT = 5              # requests allowed ...
DEFAULT_WINDOW_SECONDS = 10.0  # ... in this many seconds
KEY_HEADER = "X-Feed-Key"

NORMAL = "normal"
SLOW = "slow"
ERROR = "error"
MODES = [NORMAL, SLOW, ERROR]

STATIONS = {
    "north-field": {
        "name": "North Practice Field",
        "status": "online",
        "lightning_strikes_last_30_min": 0,
        "observations": [
            {"observed_at": "2027-01-11T15:45:00", "temperature_f": 38, "wind_mph": 11, "gust_mph": 19},
            {"observed_at": "2027-01-11T15:30:00", "temperature_f": 38, "wind_mph": 13, "gust_mph": 22},
            {"observed_at": "2027-01-11T15:15:00", "temperature_f": 39, "wind_mph": 9, "gust_mph": 16},
            {"observed_at": "2027-01-11T15:00:00", "temperature_f": 39, "wind_mph": 10, "gust_mph": 18},
        ],
    },
    "stadium": {
        "name": "Stadium Press Box",
        "status": "online",
        "lightning_strikes_last_30_min": 0,
        "observations": [
            {"observed_at": "2027-01-11T15:45:00", "temperature_f": 36, "wind_mph": 21, "gust_mph": 28},
            {"observed_at": "2027-01-11T15:30:00", "temperature_f": 36, "wind_mph": 24, "gust_mph": 34},
            {"observed_at": "2027-01-11T15:15:00", "temperature_f": 37, "wind_mph": 19, "gust_mph": 27},
        ],
    },
    "track": {
        "name": "Track and Long Jump Pit",
        "status": "online",
        "lightning_strikes_last_30_min": 3,
        "observations": [
            {"observed_at": "2027-01-11T15:45:00", "temperature_f": 41, "wind_mph": 6, "gust_mph": 12},
            {"observed_at": "2027-01-11T15:30:00", "temperature_f": 41, "wind_mph": 7, "gust_mph": 11},
        ],
    },
    "tennis-courts": {
        "name": "Tennis Courts",
        "status": "offline",
        "lightning_strikes_last_30_min": None,
        "observations": [],
    },
}

NOT_FOUND_PAGE = """<!doctype html>
<html><head><title>404 Not Found</title></head>
<body><h1>Not Found</h1><p>The page you asked for is not part of the station feed.</p></body></html>
"""

MOVED_PAGE = """<!doctype html>
<html><head><title>Station Feed</title></head>
<body><h1>The station feed has moved</h1>
<p>Data now lives under /api/v1/. This page is here for old bookmarks.</p></body></html>
"""


class StationFeedServer(ThreadingHTTPServer):
    """The HTTP server, plus the settings and request history the handler needs."""

    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS,
                 key=None, limit=DEFAULT_LIMIT, window_seconds=DEFAULT_WINDOW_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, StationFeedHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.key = key or "NOT-A-REAL-KEY-" + secrets.token_hex(3)
        self.limit = limit
        self.window_seconds = window_seconds
        self.quiet = quiet
        self.recent_requests = []
        self.request_count = 0
        self.lock = threading.Lock()

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def seconds_until_allowed(self):
        """0 if this request is allowed now, or how long to wait before the next one is."""
        now = time.monotonic()
        with self.lock:
            self.request_count += 1
            self.recent_requests = [t for t in self.recent_requests if now - t < self.window_seconds]
            if len(self.recent_requests) >= self.limit:
                oldest = self.recent_requests[0]
                return max(1, math.ceil(self.window_seconds - (now - oldest)))
            self.recent_requests.append(now)
            return 0

    def handle_error(self, request, client_address):
        # A program that gives up on a slow reply closes the connection early.
        # The standard server prints a traceback for that. It is expected here.
        if not self.quiet:
            print(f"  (a client at {client_address[0]} hung up before the reply was sent)")


class StationFeedHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        if path == "":
            self.send_text(200, "Station feed is running. Data is under /api/v1/stations\n")
            return
        if path in ("/api", "/api/stations"):
            self.send_body(200, MOVED_PAGE.encode("utf-8"), "text/html; charset=utf-8")
            return
        if not path.startswith("/api/v1/stations"):
            self.send_body(404, NOT_FOUND_PAGE.encode("utf-8"), "text/html; charset=utf-8")
            return

        wait = self.server.seconds_until_allowed()
        if wait:
            self.send_json(429, {"error": "too many requests", "retry_after_seconds": wait},
                           extra_headers={"Retry-After": str(wait)})
            return
        if self.server.mode == SLOW:
            time.sleep(self.server.delay_seconds)
        if self.server.mode == ERROR:
            self.send_json(500, {"error": "the station feed failed on purpose"})
            return

        parts = path.split("/")          # ['', 'api', 'v1', 'stations', '<id>', '<what>']
        if len(parts) == 4:
            listing = [{"id": station_id, "name": s["name"], "status": s["status"]}
                       for station_id, s in STATIONS.items()]
            self.send_json(200, {"stations": listing})
            return
        if len(parts) != 6 or parts[4] not in STATIONS:
            self.send_json(404, {"error": f"no station matches '{'/'.join(parts[4:])}'"})
            return

        station_id, what = parts[4], parts[5]
        station = STATIONS[station_id]
        if what == "observations":
            self.send_json(200, {"station_id": station_id, "name": station["name"],
                                 "status": station["status"], "observations": station["observations"]})
        elif what == "lightning":
            if self.headers.get(KEY_HEADER) != self.server.key:
                self.send_json(401, {"error": f"send a valid {KEY_HEADER} header"})
                return
            self.send_json(200, {"station_id": station_id,
                                 "strikes_last_30_min": station["lightning_strikes_last_30_min"]})
        else:
            self.send_json(404, {"error": f"stations have no '{what}' data"})

    def send_json(self, status, data, extra_headers=None):
        self.send_body(status, json.dumps(data, indent=2).encode("utf-8"), "application/json", extra_headers)

    def send_text(self, status, text):
        self.send_body(status, text.encode("utf-8"), "text/plain; charset=utf-8")

    def send_body(self, status, body, content_type, extra_headers=None):
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            for name, value in (extra_headers or {}).items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass   # the client gave up waiting; nothing to send it

    def log_message(self, format, *args):
        if not self.server.quiet:
            print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''}")


def start_in_background(mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS, key=None,
                        limit=DEFAULT_LIMIT, window_seconds=DEFAULT_WINDOW_SECONDS, port=0):
    """Start a quiet server on its own thread and return it. Port 0 picks a free port.

    Stop it with server.shutdown() and then server.server_close().
    """
    server = StationFeedServer((HOST, port), mode=mode, delay_seconds=delay_seconds, key=key,
                               limit=limit, window_seconds=window_seconds, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(description="A pretend weather station feed for Lab U7-02.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=NORMAL)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS,
                        help="seconds each data request takes in slow mode")
    parser.add_argument("--key", default=None, help="use this feed key instead of a new random one")
    arguments = parser.parse_args()

    server = StationFeedServer((HOST, arguments.port), mode=arguments.mode,
                               delay_seconds=arguments.delay, key=arguments.key)
    print(f"Station feed on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    print(f"Feed key for this run: {server.key}")
    print("Put the key in an environment variable in your terminal. Never type it into your code.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
