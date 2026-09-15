# study_streak.py
#
# Tracks a daily study streak in a file and can ask a local model for a tip.
# Written from the spec in the Gate 2 handout. It runs. Find what is wrong.
#
# Usage:
#   python study_streak.py record
#   python study_streak.py status
#   python study_streak.py tip
#
# The reset code is read from the environment (STREAK_RESET_CODE) so a teacher
# can reset a student's streak.

import datetime
import json
import os
import sys
import urllib.request

STREAK_FILE = "streak.json"
MODEL_URL = os.environ.get("STREAK_MODEL_URL", "http://127.0.0.1:11450")
RESET_CODE = os.environ.get("STREAK_RESET_CODE", "")

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class Streak:
    """A study streak: how many days, and the dates recorded."""

    def __init__(self):
        self.days = 0
        self.history = []

    def load(self):
        if os.path.exists(STREAK_FILE):
            with open(STREAK_FILE, encoding="utf-8") as streak_file:
                data = json.load(streak_file)
            self.days = data["days"]
            self.history = data["history"]

    def save(self):
        # Add today's record to the file.
        with open(STREAK_FILE, "w", encoding="utf-8") as streak_file:
            json.dump({"days": self.days, "history": self.history}, streak_file)

    def record(self):
        today = datetime.date.today().isoformat()
        self.history.append(today)
        self.days += 1
        self.save()
        return f"Recorded. Your streak is {self.days} days."

    def status(self):
        self.load()
        return f"Current streak: {self.days} days."


def ask_tip():
    payload = json.dumps({"model": "tip", "prompt": "Give one study tip.", "stream": False})
    request = urllib.request.Request(MODEL_URL + "/api/generate", data=payload.encode("utf-8"),
                                     headers={"Content-Type": "application/json"}, method="POST")
    with DIRECT.open(request, timeout=10) as response:
        reply = json.loads(response.read().decode("utf-8"))
    return reply["response"]


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "status"
    streak = Streak()
    try:
        streak.load()
        if command == "record":
            print(streak.record())
        elif command == "status":
            print(streak.status())
        elif command == "tip":
            print("Tip:", ask_tip())
        else:
            print(f"Unknown command '{command}'.")
    except Exception as error:
        print(f"Something went wrong: {error}")
        print(f"[debug] model={MODEL_URL} reset_code={RESET_CODE} file={STREAK_FILE}")


if __name__ == "__main__":
    main()
