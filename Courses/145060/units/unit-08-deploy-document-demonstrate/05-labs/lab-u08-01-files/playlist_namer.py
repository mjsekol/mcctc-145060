# playlist_namer.py
# A small web app. You type the mood of your study session and it suggests a
# name for the playlist. A language model on this machine writes the name.
#
# Run it:
#   python playlist_namer.py
# Then open http://127.0.0.1:8000 in a browser.
#
# This file WORKS on your machine when a model is running. It is NOT ready to
# deploy. Your job in Lab U8-01 is the five TODOs below.

import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

# The model settings already come from environment variables, like Unit 7.
MODEL_URL = os.environ.get("PLAYLIST_MODEL_URL", "http://127.0.0.1:11434")
MODEL_NAME = os.environ.get("PLAYLIST_MODEL", "llama3.2")

# TODO 1: The port is typed into the code. Render tells your app which port
#         to use through the PORT environment variable. Read it from there.
PORT = 8000

# TODO 2: 127.0.0.1 only accepts connections from this same machine.
#         Render's router is not on this machine.
HOST = "127.0.0.1"

MAX_MOOD_LENGTH = 30
ALLOWED_MOOD_CHARACTERS = set("abcdefghijklmnopqrstuvwxyz ")

BACKUP_NAMES = [
    "Focus Mode, Volume One",
    "Homework Headphones",
    "Quiet Hours",
    "Last Chapter Energy",
]

HOME_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Playlist Namer</title></head>
<body>
<h1>Playlist Namer</h1>
<form action="/name" method="get">
<label for="mood">What is the mood of this study session?</label>
<input id="mood" name="mood" maxlength="30">
<button type="submit">Name my playlist</button>
</form>
</body></html>
"""


def clean_mood(text):
    """Return the mood in lowercase, or None if it is not a short phrase of plain letters."""
    mood = text.strip().lower()
    if mood == "" or len(mood) > MAX_MOOD_LENGTH:
        return None
    for character in mood:
        if character not in ALLOWED_MOOD_CHARACTERS:
            return None
    return mood


def ask_model(mood):
    """Ask the local model for a playlist name and return its text."""
    prompt = f"Suggest one short, clean name for a study playlist with this mood: {mood}. Reply with the name only."
    payload = json.dumps({"model": MODEL_NAME, "prompt": prompt, "stream": False}).encode("utf-8")
    request = urllib.request.Request(MODEL_URL + "/api/generate", data=payload,
                                     headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=20) as response:
        reply = json.loads(response.read().decode("utf-8"))
    return reply["response"].strip()


# TODO 3: Render needs a quick way to ask "is this app alive?"
#         Add a /health route that answers 200 without calling the model.

# TODO 4: When no model is reachable, ask_model raises an error and the page
#         never loads. Catch it, use a backup name, and label it "saved name".

# TODO 5: Add requirements.txt and a README that names the start command.


class PlaylistHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        address = urlparse(self.path)
        if address.path == "/":
            self.send_page(200, HOME_PAGE)
        elif address.path == "/name":
            query = parse_qs(address.query)
            mood = clean_mood(query.get("mood", [""])[0])
            if mood is None:
                self.send_page(400, "<p>Type a mood using letters and spaces, 30 characters at most.</p>")
                return
            name = ask_model(mood)
            # The mood was checked above, and the model's reply is escaped here,
            # because model output is untrusted text too.
            safe_name = name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            self.send_page(200, f"<h1>{safe_name}</h1><p><a href=\"/\">Name another</a></p>")
        else:
            self.send_page(404, "<p>Nothing here.</p>")

    def send_page(self, status, page):
        body = page.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = HTTPServer((HOST, PORT), PlaylistHandler)
    print(f"Playlist Namer running at http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()
