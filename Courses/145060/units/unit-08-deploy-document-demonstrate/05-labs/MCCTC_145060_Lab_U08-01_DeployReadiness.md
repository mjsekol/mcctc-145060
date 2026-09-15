# Lab U8-01: Deploy Readiness
## 145060 Programming · Unit 8 · Week 18, Monday

**Gate:** 3 (open tooling). **Duration:** Monday Build 1, 35 minutes, plus the first 10
minutes of Build 2 if you need them. **Competencies:** 5.6.16 (deploy the application),
5.5.3 (operating system calls: environment variables), 5.3.10 (error handling), 9.3.3
(secure coding: error handling and input validation), 1.2.11 (a README that names the start
command).

**Files:** `05-labs/lab-u08-01-files/` holds `playlist_namer.py` and `check_ready.py`. Copy
both into a new folder in your repository.

---

## The scenario

Your study group made a small web app that names study playlists, and it works perfectly on the
laptop that built it. The group wants the link in their group chat by tonight, so it has to run on
Render, where nobody can sit at the keyboard and there is no language model. Right now it would
fail there in at least four different ways, and none of them show up on the laptop.

## What you will build

The same app, changed so it starts, answers, and stays useful on a host you cannot touch, proved
by a checker that runs it the way Render does.

---

## Starter code

`lab-u08-01-files/playlist_namer.py`. It runs. It works on your machine when a model is running.
It is not ready to deploy, and the five TODOs say where.

```python
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
```

**The checker.** `check_ready.py` starts your app as a separate program with `PORT` set to a port
it chooses, points the model at an address where nothing listens, makes real requests, and stops
your app when it finishes. It never edits your files. Run it on the starter first:

```
python check_ready.py
```

```
Starting playlist_namer.py with PORT=59503 and no model...

FAIL  1. listens on the port in the PORT variable
      nothing answered on port 59503 within 10 seconds
SKIP  2. accepts connections from other machines
      check 1 has to pass first
SKIP  3. /health answers 200 in under 2 seconds
      check 1 has to pass first
SKIP  4. the home page loads
      check 1 has to pass first
SKIP  5. a name page still works with no model, labelled as a saved name
      check 1 has to pass first
SKIP  6. a mood with symbols in it is refused with 400
      check 1 has to pass first
FAIL  7. PORT=not-a-port stops the app with a message that names PORT
      the app kept running, so it is not reading PORT at all
FAIL  8. requirements.txt exists
      It tells anyone deploying the app what to install. Add one, even if it only has a comment.
FAIL  9. README.md names the start command
      README.md must contain: python playlist_namer.py

0 passed, 4 failed, 5 skipped
```

Your port number will be different, because the checker picks a free one each run.

---

## Steps

### Step 1. Copy, run, commit
Copy both files into a new folder. Run `python playlist_namer.py` and open
http://127.0.0.1:8000. Stop it with Ctrl+C. Commit.

**Observable result:** the home page loads. A new commit in `git log --oneline`.

### Step 2. Run the checker on the starter
Run `python check_ready.py`.

**Observable result:** `0 passed, 4 failed, 5 skipped`. Copy that line into a file called
`readiness.md`. This is your before picture.

### Step 3. TODO 1: read the port from the environment
Replace `PORT = 8000` so the port comes from the `PORT` environment variable, as a whole number,
with 8000 when `PORT` is not set.

**Observable result:** check 1 passes. **Before you move on,** set `$env:PORT = "10000"` in
PowerShell, run the app yourself, and see it listen on 10000. Then `Remove-Item Env:PORT`.

### Step 4. Make a bad PORT stop with a message, not a crash
If `PORT` is set to something that is not a whole number between 1 and 65535, print a message that
names `PORT` and exit with a nonzero code. No traceback.

**Observable result:** check 7 passes. Try `$env:PORT = "abc"` yourself and read your message.

### Step 5. TODO 2: listen on every connection
Change the host.

**Observable result:** check 2 passes. Prove it by hand: run the app, find your IPv4 address with
`ipconfig`, and run `curl.exe -s http://YOUR-IPV4-ADDRESS:8000`.

### Step 6. TODO 3: add `/health`
Answer `GET /health` with status 200 and a short JSON body. Do not call the model.

**Observable result:** check 3 passes, and `curl.exe -s http://127.0.0.1:8000/health` prints your
JSON.

### Step 7. TODO 4: survive a missing model
Catch the failure when the model is not there. Return one of `BACKUP_NAMES`, and put the words
`saved name` on the page so the user knows the model did not write it. Shorten the model timeout
so a missing model does not freeze the page.

**Observable result:** check 5 passes. With nothing listening on port 11434, your own browser
shows a name and the words `saved name`.

### Step 8. Check the reply before trusting it
A model server can answer with status 200 and still send something useless. Before returning the
name, confirm the reply says `"done": true` and has a non-empty `"response"` string. Treat
anything else as a failure, which step 7 already handles.

**Observable result:** check 5 still passes. Reading your code, a reply of `{"done": false}` goes
to the saved name.

### Step 9. TODO 5: requirements and README
Create `requirements.txt` with a comment saying the app uses only the standard library. Create
`README.md` that says what the app is and how to run it, with a line like
`Start command: python playlist_namer.py`. The checker looks for `python playlist_namer.py`.

**Observable result:** checks 8 and 9 pass.

### Step 10. Run the checker, record, commit
Run `python check_ready.py` one final time.

**Observable result:** `9 passed, 0 failed, 0 skipped` and `Ready to deploy.` Paste the final line
under your before picture in `readiness.md`. Commit and push.

---

## Acceptance criteria

- [ ] `check_ready.py` reports 9 passed, 0 failed, 0 skipped
- [ ] `PORT` is converted to a whole number at the moment it is read
- [ ] A bad `PORT` prints a message naming `PORT` and exits nonzero, with no traceback
- [ ] The host is `0.0.0.0`
- [ ] `/health` answers 200 and never calls the model
- [ ] A missing, slow, or broken model gives a saved name labelled `saved name`
- [ ] The model reply is checked for `"done": true` and a non-empty `"response"`
- [ ] The reason the model failed is printed for whoever runs the server, never on the page
- [ ] `requirements.txt` and `README.md` exist and the README names the start command
- [ ] `readiness.md` shows the before and after checker results
- [ ] Committed and pushed

---

## If it breaks

### 1. The app crashes the moment `PORT` is set

```
TypeError: 'str' object cannot be interpreted as an integer
```

**Cause:** you read `PORT` with `os.environ.get("PORT", 8000)` and handed it straight to
`HTTPServer`. Environment variables are always text. On your laptop, `PORT` is not set, so you get
the number 8000 and it works. When `PORT` is set, you get the text `"10000"`. Convert with `int()`
at the moment you read it.

### 2. Check 2 fails with "refused"

```
FAIL  2. accepts connections from other machines
      http://10.200.57.157:55346/ was refused ([WinError 10061] No connection could be made because the target machine actively refused it)
```

**Cause:** the host is still `127.0.0.1`. Your address and port numbers will differ from these.

### 3. Check 5 fails with "Remote end closed connection"

```
FAIL  5. a name page still works with no model, labelled as a saved name
      no page came back (Remote end closed connection without response)
```

and the terminal running your app ends with:

```
urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>
```

**Cause:** the model call failed, nothing caught the error, and the server closed the connection
without sending a page. In a browser the page never arrives. `URLError` is a kind of `OSError`, so
an `except OSError` around the model call catches it, along with timeouts.

### 4. Check 7 fails: "crashed with a traceback"

```
FAIL  7. PORT=not-a-port stops the app with a message that names PORT
      the app crashed with a traceback instead of printing a message
```

and running it yourself shows:

```
ValueError: invalid literal for int() with base 10: 'not-a-port'
```

**Cause:** you convert with `int()`, which is right, but nothing catches the `ValueError`. A deploy
log full of traceback is harder to read than one sentence that says `PORT must be a whole number`.

### Not an error message: your change does not show up

You edited the app, restarted it, and the browser still shows the old behaviour. **Look for another
terminal still running the old version.** On Windows, `HTTPServer` lets a second copy start on the
same port without any error, and in testing the old copy kept answering every request. Close every
terminal running the app, then start one.

---

## Stretch goal

Your app asks the model on every single request, even after it has failed ten times in a row. With
no model on Render, every visitor pays for a failed attempt. Make the app stop asking for 60 seconds
after two failures in a row, then try again. Explain in your README why this matters more on a web
server than it did in the Unit 7 terminal program.

---

## Submission checklist

- [ ] Final checker output pasted in `readiness.md`
- [ ] Tested by hand with `$env:PORT` set, with `PORT` unset, and with no model running
- [ ] `git status` clean, pushed
- [ ] AI usage log updated if a model helped at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still on step 3 at the 15-minute mark, or asking what an environment variable is | SCAFFOLDED |
| Working through the checks one at a time, reading the FAIL lines | STANDARD |
| At 9 passed before 25 minutes, or asking why the app asks the model every time | EXTENDED |
| Says nobody would ever use a playlist namer, or has an app of their own they care about more | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** TODO 1 and TODO 2 arrive done: `read_port()` is written for you and the host is
  `0.0.0.0`. Your teacher gives you that version of the file.
- **Steps:** skip steps 3 through 5. Start at step 6. Step 8, checking the reply, is optional.
- **Checkpoints:** show your teacher the checker output after step 6 and after step 7.
- **Before you start,** read `read_port()` out loud to a partner, one line at a time, and say why
  the default is `"8000"` in quotes.

**Acceptance criteria:** checker reports 9 passed; `/health` never calls the model; the saved name
is labelled; you can explain every line of `read_port()`, including the ones you did not write.

**Grading:** same 100-point scale. Requirements Fit is judged against this list. Being able to
explain `read_port()` is required, because the one way to fail outright is submitting work you
cannot explain.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus the stretch goal as a requirement, plus one addition that needs
something not taught.

**Added requirement 1.** The stretch goal: stop asking the model for 60 seconds after two failures
in a row.

**Added requirement 2.** Some health checkers send a `HEAD` request instead of `GET`. Make
`/health` answer `HEAD` with status 200 and no body.

**Hint, not the answer.** Read the documentation for `BaseHTTPRequestHandler` in the `http.server`
module at `https://docs.python.org/3/library/http.server.html`. Look for how the handler decides
which of your methods to call based on the request's command, and what happens when that method
does not exist.

**Added requirement 3.** Prove requirement 2 without a browser, because typing an address into a
browser sends `GET`, not `HEAD`. `curl.exe` has an option for it.

**The honest warning.** The clock you use for the 60 seconds matters. A clock that follows the
computer's date and time can jump when that time is corrected. The `time` module has a clock meant
for measuring intervals. Find it, and say in your README why you chose it.

**Acceptance criteria:** all STANDARD criteria, plus a recorded run showing the model is not asked
during the rest period, plus a `HEAD /health` result of 200 with an empty body.

---

## APPLIED

**For the student who says this does not apply to them.** Same skills, your own app.

**Changed scenario.** Take any program you built this semester that takes input, such as your Unit
7 API app or your CLI Toolsmith, and put it behind a one-form web page with the same five readiness
changes.

**What you build.** A web page with one form, the logic from your old program behind it, and the
same readiness properties: `PORT` read and converted, `0.0.0.0`, `/health`, a labelled fallback when
anything outside your program is missing, `requirements.txt`, and a README with the start command.

**The extra requirement that makes it the same lab.** `check_ready.py` only knows the Playlist
Namer's addresses, so it cannot check your app. Write `readiness.md` by hand as a table with the
same nine checks, the exact command you used to test each one, and what you saw.

**Acceptance criteria:** all nine checks demonstrated by recorded commands and output, plus the
README.

**Grading:** same scale. Requirements Fit is judged on whether the recorded commands actually prove
each check, which is harder than running a checker somebody else wrote.
