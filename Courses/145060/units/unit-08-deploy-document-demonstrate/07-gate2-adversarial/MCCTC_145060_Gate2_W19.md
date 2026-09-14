# Gate 2: Adversarial Review · Week 19
## 145060 Programming · Unit 8 · Tuesday, January 26, Build 2

**40 minutes.** Individual. You may and should run the code. You may not ask a model whether it
is correct, because the model is what is being reviewed.

**The last Gate 2 of the semester.** Everything the course has taught you to look for is in play,
plus the thing this week is about: code that works on your laptop and fails where it is deployed.

**Files:** `07-gate2-adversarial/gate2-w19-files/` holds `caption_app.py` and
`saved_captions.json`. Copy both into one folder.

---

## What you are looking at

The photography club handed an AI assistant the requirements in Part A and got the program in
Part B. It runs. It is tidy, and its comments sound like they know what Render does.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says, somewhere you might not be testing |
| **Security** | Something public that should not be, or trust that was not earned |
| **Readability** | A comment or name that would mislead the next person to touch it |
| **Performance** | Work done over and over that only needed doing once |
| **Requirements Fit** | Something the spec asked for that is missing |

**One of these defects cannot be seen on your laptop no matter how long you test it the way you
normally test.** You have to run the program the way Render runs it.

---

## PART A: The requirements

> Write `caption_app.py`, a web app the photography club will deploy on Render so members can get a
> caption idea for a post. The repository is public.
>
> 1. Render starts it with `python caption_app.py`. It must listen on all network interfaces, on the
>    port Render provides in the `PORT` environment variable. With no `PORT` set, it uses 8000.
> 2. The home page `/` shows a form with one field, `topic`: what the photo shows.
> 3. `/caption?topic=...` accepts a topic of 1 to 40 letters, digits, and spaces, in any case.
>    Anything else gets a 400 page with a friendly message.
> 4. The caption comes from a local Ollama-compatible model at `CAPTION_MODEL_URL`, model
>    `CAPTION_MODEL`, with a 4-second timeout. A reply only counts if it says `"done": true` and has
>    a `"response"` string.
> 5. If the model fails for any reason, show a random caption from `saved_captions.json`, **and label
>    it on the page with the words "Saved caption"** so members know the model did not write it.
> 6. `/health` returns status 200 and JSON at all times, and never contacts the model.
> 7. `/stats` shows how many captions came from the model and how many were saved ones. Officers
>    only. The officer key is set in the Render dashboard as `OFFICER_KEY`, **and the key must never
>    appear in the repository.**
> 8. Every piece of text shown on a page is escaped.

---

## PART B: What the AI produced

Count line numbers from `# caption_app.py` as line 1. Blank lines count.

```python
# caption_app.py
#
# Caption Helper for the photography club. Members describe a photo and get a
# caption idea for the club's post. A local language model writes the caption.
# When no model is reachable, the app picks a saved caption instead.
#
# Deployment: Render starts this file with `python caption_app.py`.
# Local testing: run the same command and open http://127.0.0.1:8000

import hmac
import html
import json
import os
import random
import sys
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
SAVED_CAPTIONS_FILE = HERE / "saved_captions.json"

MODEL_URL = os.environ.get("CAPTION_MODEL_URL", "http://127.0.0.1:11434")
MODEL_NAME = os.environ.get("CAPTION_MODEL", "llama3.2")
MODEL_TIMEOUT_SECONDS = 4

# Officers use this key to open /stats. Read from the environment so it can be
# set in the Render dashboard. Falls back to the key the officers already use.
OFFICER_KEY = os.environ.get("OFFICER_KEY", "shutter-club-2027")

HOST = "0.0.0.0"
PORT = os.environ.get("PORT", 8000)

MAX_TOPIC_LENGTH = 40
ALLOWED_TOPIC_CHARACTERS = set("abcdefghijklmnopqrstuvwxyz0123456789 ")

stats = {"model": 0, "saved": 0}
stats_lock = threading.Lock()

HOME_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Caption Helper</title></head>
<body>
<h1>Caption Helper</h1>
<form action="/caption" method="get">
<label for="topic">What does the photo show?</label>
<input id="topic" name="topic" maxlength="40">
<button type="submit">Suggest a caption</button>
</form>
</body></html>
"""


def clean_topic(text):
    """Return the topic in lowercase, or None if it is empty, too long, or has symbols."""
    topic = text.strip().lower()
    if topic == "" or len(topic) > MAX_TOPIC_LENGTH:
        return None
    if any(character not in ALLOWED_TOPIC_CHARACTERS for character in topic):
        return None
    return topic


def load_saved_captions():
    """Read the saved captions, one list of strings, from saved_captions.json."""
    with open(SAVED_CAPTIONS_FILE, encoding="utf-8") as caption_file:
        return json.load(caption_file)


def ask_model(topic):
    """Ask the local model for one caption. Raises an error if there is no usable reply."""
    prompt = (f"Write one short, friendly caption for a school photography club post. "
              f"The photo shows: {topic}. No hashtags. Reply with the caption only.")
    payload = json.dumps({"model": MODEL_NAME, "prompt": prompt, "stream": False}).encode("utf-8")
    request = urllib.request.Request(MODEL_URL + "/api/generate", data=payload,
                                     headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=MODEL_TIMEOUT_SECONDS) as response:
        reply = json.loads(response.read().decode("utf-8"))
    if not isinstance(reply, dict) or reply.get("done") is not True or not isinstance(reply.get("response"), str):
        raise ValueError("unusable model reply")
    return reply["response"].strip()


def suggest_caption(topic):
    """Return a caption from the model, or a saved caption if the model fails."""
    saved_captions = load_saved_captions()
    try:
        caption = ask_model(topic)
        source = "model"
    except (OSError, ValueError) as error:
        print(f"model unavailable: {error}", file=sys.stderr, flush=True)
        caption = random.choice(saved_captions)
        source = "saved"
    with stats_lock:
        stats[source] += 1
    return caption


class CaptionHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        address = urlparse(self.path)
        query = parse_qs(address.query)
        if address.path == "/":
            self.send_page(200, HOME_PAGE)
        elif address.path == "/health":
            # Render polls this. Returns 503 while the model is unreachable,
            # so Render knows to restart the app until the model comes back.
            self.send_body(200, b'{"status": "ok"}', "application/json")
        elif address.path == "/caption":
            topic = clean_topic(query.get("topic", [""])[0])
            if topic is None:
                self.send_page(400, "<p>Describe the photo in 40 characters or fewer, letters and numbers only.</p>")
                return
            caption = suggest_caption(topic)
            self.send_page(200, f"<h1>{html.escape(caption)}</h1><p><a href=\"/\">Try another</a></p>")
        elif address.path == "/stats":
            key = query.get("key", [""])[0]
            if not hmac.compare_digest(key.encode("utf-8"), OFFICER_KEY.encode("utf-8")):
                self.send_page(403, "<p>Officers only.</p>")
                return
            with stats_lock:
                body = json.dumps(stats).encode("utf-8")
            self.send_body(200, body, "application/json")
        else:
            self.send_page(404, "<p>Nothing here.</p>")

    def send_page(self, status, page):
        self.send_body(status, page.encode("utf-8"), "text/html; charset=utf-8")

    def send_body(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = ThreadingHTTPServer((HOST, PORT), CaptionHandler)
    print(f"Caption Helper listening on {HOST}:{PORT}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
```

### A real run, for reference

On a lab machine with no model server running. The app in one terminal, requests in another:

```
python caption_app.py
Caption Helper listening on 0.0.0.0:8000
```

```
> curl.exe -s http://127.0.0.1:8000/health
{"status": "ok"}
> curl.exe -s "http://127.0.0.1:8000/caption?topic=team+photo"
<h1>Caught in the moment.</h1><p><a href="/">Try another</a></p>
> curl.exe -s "http://127.0.0.1:8000/caption?topic=%3Cb%3E"
<p>Describe the photo in 40 characters or fewer, letters and numbers only.</p>
> curl.exe -s "http://127.0.0.1:8000/stats"
<p>Officers only.</p>
```

The caption is chosen at random, so yours may differ.

**Read that output against requirements 3, 5, and 7 before you read the code.** One defect is
sitting in it in plain sight.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**, **the
command you ran that proves it**, and **the fix**. Then one final entry: **what I was unsure
about**, naming something specific. That entry is scored, and a blank costs more than a wrong
guess.

### How to spend 40 minutes

- **First 5:** run it as shown above. Compare every line of output to Part A.
- **Next 10:** run it the way Render runs it. In PowerShell, `$env:PORT = "10000"`, then start it.
  Afterward, `Remove-Item Env:PORT`.
- **Next 10:** go through Part A one requirement at a time and point at the line that satisfies it.
  If you cannot point, you found one.
- **Rest:** read every comment against the code beneath it, and ask what happens on the second,
  third, and hundredth request.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your teacher states the security
weighting before you start.

**Four of five is a strong score.**
