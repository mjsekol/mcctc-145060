# announcement_writer.py  ·  Lab U7-03 starter
#
# Club officers hand the front office one line of facts for the morning
# announcements. This program asks a language model running on lab hardware
# to turn those facts into one friendly sentence. By the end of the lab it
# refuses to trust the reply until the reply has passed every check, and it
# falls back to a plain template when anything goes wrong.
#
# What goes into the prompt: a club name, a day, a time, a room, and one detail.
# What never goes into the prompt: any student's name, grade, schedule, or
# anything else about a real person.
#
# Start the stub first, in a second terminal in this folder:
#   python stub_model_server.py
#
# This file runs right now. It does not do anything useful yet.

import json
import os
import sys
import urllib.error
import urllib.request

URL_VARIABLE = "ANNOUNCE_MODEL_URL"
MODEL_VARIABLE = "ANNOUNCE_MODEL"
TIMEOUT_VARIABLE = "ANNOUNCE_MODEL_TIMEOUT"
DEFAULT_URL = "http://127.0.0.1:11434"
DEFAULT_MODEL = "llama3.2"
DEFAULT_TIMEOUT_SECONDS = 20.0
GENERATE_PATH = "/api/generate"
MAX_REPLY_CHARACTERS = 300
FACTS_TO_KEEP = ["time", "room"]

PROMPT_TEMPLATE = """Write one short, friendly school morning announcement from these facts.
Keep the time and the room exactly as written. Do not add facts. No exclamation points.
Reply with the announcement only.

Club: {club}
Day: {day}
Time: {time}
Room: {room}
Detail: {detail}"""

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))

SAMPLE_FACTS = [
    {"club": "Robotics Club", "day": "Thursday", "time": "3:15", "room": "Room 118",
     "detail": "Bring safety glasses."},
    {"club": "Esports Club", "day": "Friday", "time": "2:50", "room": "the Media Center",
     "detail": "Tryouts for the spring roster start this week."},
]


# ----- Already written for you -----

def load_settings(environment):
    base_url = environment.get(URL_VARIABLE, DEFAULT_URL).rstrip("/")
    if not base_url.startswith(("http://", "https://")):
        raise ValueError(f"{URL_VARIABLE} must start with http:// or https://")
    timeout_text = environment.get(TIMEOUT_VARIABLE, "")
    timeout = DEFAULT_TIMEOUT_SECONDS
    if timeout_text:
        try:
            timeout = float(timeout_text)
        except ValueError:
            raise ValueError(f"{TIMEOUT_VARIABLE} must be a number of seconds") from None
    return {"base_url": base_url, "model": environment.get(MODEL_VARIABLE, DEFAULT_MODEL), "timeout": timeout}


def build_prompt(facts):
    return PROMPT_TEMPLATE.format(**facts)


def template_announcement(facts):
    """The announcement with no model at all. Plain, and always correct."""
    return f"{facts['club']} meets {facts['day']} at {facts['time']} in {facts['room']}. {facts['detail']}"


def ask_model(settings, prompt):
    """Send the prompt. Return (body_bytes, None), or (None, reason) for each kind of failure."""
    payload = json.dumps({"model": settings["model"], "prompt": prompt, "stream": False})
    request = urllib.request.Request(settings["base_url"] + GENERATE_PATH, data=payload.encode("utf-8"),
                                     headers={"Content-Type": "application/json"}, method="POST")
    try:
        with DIRECT.open(request, timeout=settings["timeout"]) as response:
            return response.read(), None
    except urllib.error.HTTPError as error:
        error.close()
        return None, f"the model server answered HTTP {error.code}"
    except urllib.error.URLError as error:
        return None, f"could not reach the model server ({error.reason})"
    except TimeoutError:
        return None, f"no answer within {settings['timeout']:g} seconds"


# ----- Yours to write -----

def parse_reply(body):
    """Pull the announcement out of a /api/generate reply. Return (text, None) or (None, reason)."""
    # TODO 1: turn the bytes into a dictionary and return its "response".
    # TODO 2: refuse a reply that does not say "done": true.
    # TODO 3: refuse a reply whose "response" is missing or is not a string.
    # TODO 4: refuse broken JSON, blank text, and text over MAX_REPLY_CHARACTERS.
    return None, "parse_reply is not written yet"


def remove_control_characters(text):
    """TODO 5: keep only the characters where character.isprintable() is True."""
    return text


def missing_facts(text, facts):
    """TODO 6: the names in FACTS_TO_KEEP whose value does not appear in the text."""
    return []


def write_announcement(settings, facts):
    """TODO 7: return (announcement, where_it_came_from). Use the template on any problem."""
    return template_announcement(facts), "template, because write_announcement is not written yet"


def main(environment):
    settings = load_settings(environment)
    for facts in SAMPLE_FACTS:
        body, problem = ask_model(settings, build_prompt(facts))
        print("Raw reply:", body if problem is None else problem)
    print("Nothing is parsed yet. Start with TODO 1.")
    return 0


if __name__ == "__main__":
    sys.exit(main(os.environ))
