# valley_data_server.py  ·  API Application project fixture
#
# Millbrook Valley Open Data: a pretend public data service for an invented
# town. It serves three feeds, bus arrivals, weather stations, and park court
# status, and it behaves the way real public APIs behave, including the ways
# they fail. Every stop, station, park, and reading is invented.
#
# Usage, from this folder:
#   python valley_data_server.py                     normal mode, port 8090
#   python valley_data_server.py --mode slow         every data request takes 15 seconds
#   python valley_data_server.py --mode error        every data request fails with HTTP 500
#   python valley_data_server.py --port 8091
#   python valley_data_server.py --key NOT-A-REAL-KEY-myapp
#   python valley_data_server.py --limit 3 --window 10
#
# Leave this terminal open while your app runs in a second terminal.
# Press Ctrl+C here to stop it. Full documentation is in README.md next to this file.
#
# You do not need to understand how this file works. It uses classes that
# build on classes from the standard library, which is 145065 material.

import argparse
import json
import math
import secrets
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"
DEFAULT_PORT = 8090
DEFAULT_DELAY_SECONDS = 15.0
DEFAULT_LIMIT = 10
DEFAULT_WINDOW_SECONDS = 10.0
KEY_HEADER = "X-Valley-Key"

NORMAL = "normal"
SLOW = "slow"
ERROR = "error"
MODES = [NORMAL, SLOW, ERROR]

STOPS = {
    "MR-104": {
        "name": "Maple Run High School, Front Loop",
        "routes": ["7", "12"],
        "feed_status": "live",
        "updated_at": "2027-01-19T07:12:30",
        "arrivals": [
            {"route": "7", "headsign": "Downtown Transit Center", "minutes_away": 4, "scheduled": "07:17"},
            {"route": "12", "headsign": "Millbrook Mall", "minutes_away": 11, "scheduled": "07:21"},
            {"route": "7", "headsign": "Downtown Transit Center", "minutes_away": 34, "scheduled": "07:47"},
        ],
    },
    "LIB-220": {
        "name": "Millbrook Public Library",
        "routes": ["12"],
        "feed_status": "live",
        "updated_at": "2027-01-19T07:12:10",
        "arrivals": [
            {"route": "12", "headsign": "Maple Run High School", "minutes_away": 0, "scheduled": "07:12"},
        ],
    },
    "PARK-310": {
        "name": "Riverside Park and Ride",
        "routes": ["3", "7"],
        "feed_status": "stale",
        "updated_at": "2027-01-19T06:41:02",
        "arrivals": [],
    },
    "DEPOT-001": {
        "name": "North Depot",
        "routes": ["3"],
        "feed_status": "no_service",
        "updated_at": "2027-01-19T07:12:40",
        "arrivals": [],
    },
}

WEATHER_STATIONS = {
    "maple-run": {"name": "Maple Run High School Roof", "updated_at": "2027-01-19T07:10:00",
                  "temperature_f": 18, "feels_like_f": 7, "wind_mph": 12, "conditions": "light snow"},
    "riverside": {"name": "Riverside Park", "updated_at": "2027-01-19T07:05:00",
                  "temperature_f": 21, "feels_like_f": 13, "wind_mph": 6, "conditions": "cloudy"},
}

PARKS = {
    "oak-hollow": {"name": "Oak Hollow Park", "updated_at": "2027-01-19T07:00:00",
                   "courts": [
                       {"court": "Court 1", "sport": "basketball", "status": "open", "lights_until": "21:00"},
                       {"court": "Court 2", "sport": "basketball", "status": "closed", "lights_until": None},
                       {"court": "Court 3", "sport": "pickleball", "status": "open", "lights_until": "20:00"},
                   ]},
    "millbrook": {"name": "Millbrook Community Center", "updated_at": "2027-01-18T22:15:00",
                  "courts": [
                      {"court": "Gym A", "sport": "volleyball", "status": "reserved", "lights_until": "22:00"},
                  ]},
}

NOT_FOUND_PAGE = """<!doctype html>
<html><head><title>404 Not Found</title></head>
<body><h1>Not Found</h1><p>Millbrook Valley Open Data has no page at this address.</p></body></html>
"""


class ValleyDataServer(ThreadingHTTPServer):
    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS, key=None,
                 limit=DEFAULT_LIMIT, window_seconds=DEFAULT_WINDOW_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, ValleyDataHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.key = key or "NOT-A-REAL-KEY-" + secrets.token_hex(3)
        self.limit = limit
        self.window_seconds = window_seconds
        self.quiet = quiet
        self.recent_requests = []
        self.data_requests = 0
        self.lock = threading.Lock()

    @property
    def base_url(self):
        return f"http://{self.server_address[0]}:{self.server_address[1]}"

    def seconds_until_allowed(self):
        now = time.monotonic()
        with self.lock:
            self.data_requests += 1
            self.recent_requests = [t for t in self.recent_requests if now - t < self.window_seconds]
            if len(self.recent_requests) >= self.limit:
                return max(1, math.ceil(self.window_seconds - (now - self.recent_requests[0])))
            self.recent_requests.append(now)
            return 0

    def handle_error(self, request, client_address):
        if not self.quiet:
            print("  (a client hung up before the reply was sent)")


class ValleyDataHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        if path == "":
            self.send_text(200, "Millbrook Valley Open Data is running. Every data path starts with /v1/\n")
            return
        if not path.startswith("/v1/"):
            self.send_body(404, NOT_FOUND_PAGE.encode("utf-8"), "text/html; charset=utf-8")
            return

        # Checked in the same order a real service usually checks: who you
        # are, then how fast you are going, then what you asked for.
        if self.headers.get(KEY_HEADER) != self.server.key:
            self.send_json(401, {"error": f"missing or invalid {KEY_HEADER} header"})
            return
        wait = self.server.seconds_until_allowed()
        if wait:
            self.send_json(429, {"error": "rate limit exceeded", "retry_after_seconds": wait},
                           {"Retry-After": str(wait)})
            return
        if self.server.mode == SLOW:
            time.sleep(self.server.delay_seconds)
        if self.server.mode == ERROR:
            self.send_json(500, {"error": "internal error"})
            return

        parts = path.split("/")[2:]      # after '', 'v1'
        route = self.route(parts)
        if route is None:
            self.send_json(404, {"error": f"nothing found at {path}"})
            return
        self.send_json(200, route)

    def route(self, parts):
        """The JSON for a path, or None when the path or the id does not exist."""
        if parts == ["transit", "stops"]:
            return {"stops": [{"id": stop_id, "name": s["name"], "routes": s["routes"]}
                              for stop_id, s in STOPS.items()]}
        if len(parts) == 4 and parts[:2] == ["transit", "stops"] and parts[3] == "arrivals":
            stop = STOPS.get(parts[2])
            if stop is None:
                return None
            return {"stop_id": parts[2], "stop_name": stop["name"], "feed_status": stop["feed_status"],
                    "updated_at": stop["updated_at"], "arrivals": stop["arrivals"]}
        if parts == ["weather", "stations"]:
            return {"stations": [{"id": station_id, "name": s["name"]} for station_id, s in WEATHER_STATIONS.items()]}
        if len(parts) == 4 and parts[:2] == ["weather", "stations"] and parts[3] == "current":
            station = WEATHER_STATIONS.get(parts[2])
            if station is None:
                return None
            return dict(station, station_id=parts[2])
        if parts == ["courts", "parks"]:
            return {"parks": [{"id": park_id, "name": p["name"]} for park_id, p in PARKS.items()]}
        if len(parts) == 4 and parts[:2] == ["courts", "parks"] and parts[3] == "status":
            park = PARKS.get(parts[2])
            if park is None:
                return None
            return dict(park, park_id=parts[2])
        return None

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
            pass

    def log_message(self, format, *args):
        if not self.server.quiet:
            print(f"  {self.command} {self.path} -> {args[1] if len(args) > 1 else ''}")


def start_in_background(mode=NORMAL, delay_seconds=DEFAULT_DELAY_SECONDS, key=None,
                        limit=DEFAULT_LIMIT, window_seconds=DEFAULT_WINDOW_SECONDS, port=0):
    """Start a quiet server on its own thread and return it. Port 0 picks a free port."""
    server = ValleyDataServer((HOST, port), mode=mode, delay_seconds=delay_seconds, key=key,
                              limit=limit, window_seconds=window_seconds, quiet=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def main():
    parser = argparse.ArgumentParser(description="Millbrook Valley Open Data, a pretend public API.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=NORMAL)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS)
    parser.add_argument("--key", default=None)
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="requests allowed per window")
    parser.add_argument("--window", type=float, default=DEFAULT_WINDOW_SECONDS, help="window length in seconds")
    arguments = parser.parse_args()
    server = ValleyDataServer((HOST, arguments.port), mode=arguments.mode, delay_seconds=arguments.delay,
                              key=arguments.key, limit=arguments.limit, window_seconds=arguments.window)
    print(f"Millbrook Valley Open Data on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    print(f"App key for this run: {server.key}")
    print(f"Rate limit: {server.limit} requests every {server.window_seconds:g} seconds.")
    print("Put the key in an environment variable in your terminal. Never type it into your code.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
