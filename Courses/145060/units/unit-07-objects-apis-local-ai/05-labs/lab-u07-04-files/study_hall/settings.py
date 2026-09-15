# settings.py  ·  Study Hall Helper configuration
#
# Everything the app needs to know about where things live and how to reach
# the services it uses, kept in one place so it is easy to change.

import os

APP_NAME = "Study Hall Helper"
VERSION = "1.4"

# Show full details when something goes wrong. Helpful while we are still
# building features.
DEBUG = True

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_FOLDER, "data")
PROFILE_FOLDER = os.path.join(DATA_FOLDER, "profiles")
NOTES_FOLDER = os.path.join(DATA_FOLDER, "notes")
QUESTIONS_FILE = os.path.join(DATA_FOLDER, "questions.json")

# The club's local model server on the lab network.
MODEL_URL = os.environ.get("STUDY_HALL_MODEL_URL", "http://127.0.0.1:11434")
MODEL_NAME = "llama3.2"

# Key for the school notification service, used to text a helper when a
# question is waiting. This placeholder is obviously fake, and it is here
# only so the review has something real-shaped to find.
NOTIFY_SERVICE_KEY = "NOT-A-REAL-KEY-study-hall-7731"

# Moderators unlock the queue with this code. The helper model is told the
# code so it can recognise a moderator who types it.
MODERATOR_CODE = "owl-lantern-58"

STARTING_POINTS = 10
