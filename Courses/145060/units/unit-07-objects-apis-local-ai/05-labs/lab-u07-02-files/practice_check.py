# practice_check.py  ·  Lab U7-02 starter
#
# Answers one question before the team walks outside: is practice on, or does
# it move inside? By Wednesday it asks the district weather station feed for
# the last hour of readings, and for lightning, and applies the coach's rule:
#
#   Practice moves inside if any gust in the last hour reached 30 mph,
#   or if any lightning struck within the last 30 minutes.
#
# The rule and the feed are invented for this lab.
#
# Start the feed first, in a second terminal in this folder:
#   python weather_station_server.py
#
# This file runs right now. It does not do anything useful yet.

import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_URL = "http://127.0.0.1:8070"
DEFAULT_TIMEOUT_SECONDS = 5.0
KEY_HEADER = "X-Feed-Key"
GUST_LIMIT_MPH = 30

# Talk to the feed directly, never through a proxy. A school proxy cannot
# reach 127.0.0.1, and a request that detours through one fails in confusing ways.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def load_settings(environment):
    """Part 3 rewrites this. For now it ignores the environment and uses the defaults."""
    return {"base_url": DEFAULT_URL, "timeout": DEFAULT_TIMEOUT_SECONDS, "key": ""}


def get_json(settings, path):
    """GET one path from the feed and return the parsed JSON."""
    # TODO 1 (Part 1): build a urllib.request.Request for settings["base_url"] + path,
    #   open it with DIRECT.open(request, timeout=settings["timeout"]),
    #   read the bytes, decode them as UTF-8, and return json.loads of the text.
    # TODO 6 (Part 3): if settings["key"] is not empty, send it in the KEY_HEADER header.
    return {}


def decide(name, observations, strikes):
    """Apply the coach's rule to a list of readings. Returns a list of lines to print."""
    # TODO 2 (Part 1): find the strongest gust, then return the lines.
    # TODO 5 (Part 2): decide what an EMPTY list of readings should mean.
    return ["No decision made yet."]


def fetch(settings, path, sleep=time.sleep):
    """Return (data, None) on success, or (None, message) saying exactly what went wrong."""
    # TODO 3 (Part 2): catch each failure separately. 404, 429, timeout,
    #   could not connect, a reply that is not JSON, and any other HTTP error.
    # TODO 4 (Part 2): on a 429, wait the Retry-After seconds and try once more.
    return get_json(settings, path), None


def check_station(settings, station_id, sleep=time.sleep):
    """Everything needed to answer for one station, as text. Already written for you."""
    readings, problem = fetch(settings, f"/api/v1/stations/{station_id}/observations", sleep)
    if problem is not None:
        return problem
    lightning, problem = fetch(settings, f"/api/v1/stations/{station_id}/lightning", sleep)
    if problem is not None:
        return problem
    return "\n".join(decide(readings["name"], readings["observations"], lightning["strikes_last_30_min"]))


def main(arguments, environment):
    settings = load_settings(environment)
    print(f"Practice Check will ask the feed at {settings['base_url']}.")
    print("Nothing is checked yet. Start with TODO 1.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], os.environ))
