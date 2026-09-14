# Lecture Notes: Deploying to Render
## 145060 Programming · Unit 8 · Week 19 · Monday, January 25

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W19_ShipItToRender.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W19_ShipItToRender.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example. Two of them work perfectly on your machine and fail the moment you deploy,
and you need to see that happen before it happens to your final project.

**Render screens change.** Every Render menu name, button, and setting in this file is
marked **[VERIFY]**. Your teacher confirms them on a real account before class. If a
screen does not match, trust the screen and tell your teacher.

---

## Why this exists

Every program you have written this semester runs on one computer: yours. Your text
adventure works for exactly one person, sitting at exactly one keyboard.

Deploying means putting the program on a computer somebody else runs, at a web address
anybody can open. Your cousin on her phone. A judge at a competition. A college
admissions reader. That is the difference between "I built a game" and "here is my
game."

The problem is that the other computer is not your computer. It has different settings,
it is reached in a different way, and it does not have the things you forgot you
installed. **Most deploy failures are not bugs in your game. They are assumptions about
your laptop that turned out to be false somewhere else.**

---

## The concept in plain language

**A deployed web app has to listen where the host can reach it.** Two settings decide
where your app listens: the **host** and the **port**.

| Setting | What it means | On your laptop | On Render |
|---|---|---|---|
| **Host** | Which network connections the app accepts | `127.0.0.1` works, because you are on the same machine | Must be `0.0.0.0`, because requests arrive from outside the machine |
| **Port** | Which numbered door on that machine the app answers | You pick one, like `8000` | Render picks it and tells you through the `PORT` environment variable **[VERIFY]** |

Think of a building. The host is which entrances are unlocked. `127.0.0.1` locks every
door except the one from inside the building. `0.0.0.0` unlocks all of them. The port
is the apartment number. Render's router walks up to the building and knocks on the
apartment number it gave you. If you are in a different apartment, or the front door is
locked, nobody answers.

### The environment variable rule

> **Environment variables are always text.**

Render sets `PORT` to something like `"10000"`. That is a string, the same way
`input()` always hands you a string. A socket needs the number `10000`. You have seen
this exact problem before, in Week 2, with `"12" * 3`.

---

## Worked example 1: the smallest deployable web app

This uses `http.server`, which is part of Python's standard library. Nothing to install.

```python
# on_the_air.py  ·  the smallest web app that can be deployed
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000


class OnTheAir(BaseHTTPRequestHandler):
    def do_GET(self):
        body = "Kestrel Ridge relay is on the air.".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer((HOST, PORT), OnTheAir)
print(f"Listening on {HOST}:{PORT}", flush=True)
server.serve_forever()
```

Run it with `python on_the_air.py`. The terminal shows:

```
Listening on 127.0.0.1:8000
```

In a second terminal, ask it for the page. On Windows, type `curl.exe`, not `curl`,
because PowerShell has its own command called `curl` that behaves differently.

```
curl.exe -s http://127.0.0.1:8000
```

```
Kestrel Ridge relay is on the air.
```

It works. Press Ctrl+C in the first terminal to stop it. Now watch it fail.

---

## The wrong version, part 1: it works for you and nobody else

Find your machine's own network address with `ipconfig` and look for the line that
starts `IPv4 Address`. On the machine that produced these notes it was `10.200.57.157`.
Yours is different. Start the app again and ask for the page at that address instead:

```
curl.exe -s -S http://10.200.57.157:8000
```

```
curl: (7) Failed to connect to 10.200.57.157:8000 after 2055 ms: Could not connect to server
```

**Same machine. Same app. Same port.** The only difference is how you knocked.
`127.0.0.1` means "this machine, talking to itself." An app bound to it refuses every
connection that arrives any other way, and that includes Render's router.

The fix is one line:

```python
HOST = "0.0.0.0"
```

Run it again:

```
Listening on 0.0.0.0:8000
```

```
curl.exe -s http://10.200.57.157:8000
```

```
Kestrel Ridge relay is on the air.
```

**A neighbor can try this too.** Give them your IPv4 address and have them run the same
`curl.exe` command from their machine. If the school network or the Windows firewall
blocks it, that is a lab network setting, not your code. The same-machine test above
proves the point either way.

---

## The wrong version, part 2: the one that does not crash on your laptop

Render tells you the port through `PORT`. So you read it:

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = os.environ.get("PORT", 8000)
```

Run it on your laptop:

```
Listening on 0.0.0.0:8000
```

```
Kestrel Ridge relay is on the air.
```

**It works. Every test you run on your laptop passes.** Now do what Render does and set
`PORT` before you start the app. In PowerShell:

```
$env:PORT = "10000"
python on_the_air.py
```

```
Traceback (most recent call last):
  File "...\on_the_air.py", line 19, in <module>
    server = HTTPServer((HOST, PORT), OnTheAir)
  File "C:\Python313\Lib\socketserver.py", line 457, in __init__
    self.server_bind()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Python313\Lib\http\server.py", line 136, in server_bind
    socketserver.TCPServer.server_bind(self)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Python313\Lib\socketserver.py", line 478, in server_bind
    self.socket.bind(self.server_address)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
TypeError: 'str' object cannot be interpreted as an integer
```

Here is why your laptop never showed you this. With `PORT` unset, `.get()` hands back
the default, `8000`, which you typed as a number. With `PORT` set, `.get()` hands back
what the environment holds, `"10000"`, which is text. **The same line returns two
different types depending on where it runs.** Your laptop only ever tested one of them.

**This is the bug that does not crash, promoted.** In Week 2, `"12" * 3` gave you
`121212` and no error. This one gives no error anywhere you look, and then crashes on the
one computer you cannot sit at.

The fix converts at the moment you read, exactly like `int(input(...))`:

```python
PORT = int(os.environ.get("PORT", "8000"))
```

Notice the default is now the text `"8000"`, so both paths go through `int()` and both
paths are tested every time.

To clear the variable afterward in PowerShell: `Remove-Item Env:PORT`.

---

## Worked example 2: a health route

A **health check** is a small address that answers "I am alive" quickly. Hosting
services, including Render **[VERIFY the Health Check Path setting]**, can use one to
decide whether your app started correctly.

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8000"))


class OnTheAir(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = "ok".encode("utf-8")
        else:
            body = "Kestrel Ridge relay is on the air.".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer((HOST, PORT), OnTheAir)
print(f"Listening on {HOST}:{PORT}", flush=True)
server.serve_forever()
```

With `$env:PORT = "10000"`:

```
Listening on 0.0.0.0:10000
```

```
curl.exe -s http://10.200.57.157:10000/health
```

```
ok
```

**The rule for a health route: never make it depend on something optional.** If your
health route asked the language model a question, then on Render, where there is no
model, the health check would fail forever. Your app is healthy. The model is absent.
Those are different facts.

---

## Worked example 3: there is no model on Render

Read this section twice. It decides whether your deployed text adventure works.

**Render runs your code on a server with no language model on it.** The model you called
in Unit 7 runs on lab hardware inside the school. Render cannot reach it, and you must
not try to make it reachable: opening a lab machine to the public internet is a security
decision for the district, not for a class project.

So on Render, every call to the model fails. Your app has two choices:

1. **Crash**, or hang until the request times out, so the page never loads.
2. **Fall back**: catch the failure, use the stored text, and say so on the page.

Text adventure v4 already does option 2. `Game.ask_narrator()` catches `ModelError` and
returns the stored description. That design is exactly why v4 can be deployed. Here is
the shape in a small form:

```python
def ask_model(prompt):
    raise ConnectionRefusedError("nothing is listening on that port")


def describe(room, stored_text):
    try:
        return ask_model("Describe the " + room)
    except OSError:
        return stored_text + " (stored description: the model did not answer)"


print(describe("Lobby", "Rain streaks the glass doors behind you."))
```

```
Rain streaks the glass doors behind you. (stored description: the model did not answer)
```

`ConnectionRefusedError` is a kind of `OSError`, and so are timeouts and `urllib`'s
`URLError`. One `except OSError` covers "the model server is not there."

**Say it on the page.** A user who reads a stored description while thinking a model
wrote it has been misled. Label it.

---

## What Render needs from you

Four things, and your repository has to carry all of them, because Render only sees what
you pushed.

| Render needs | You provide | Why |
|---|---|---|
| Your code | A pushed GitHub repository **[VERIFY: connecting GitHub]** | Render builds from the repository, not from your laptop |
| A build command | `pip install -r requirements.txt` **[VERIFY: the default for Python]** | Installs packages. Yours has none, so `requirements.txt` holds only a comment |
| A start command | `python app.py`, or whatever starts your app | Render runs exactly this. If it works in your terminal from the repository folder, it is the right command |
| A port and host | `int(os.environ.get("PORT", "8000"))` and `0.0.0.0` | Render tells your app the port. Your app must listen on it, from outside |

A `requirements.txt` with only comments is valid. `pip install -r requirements.txt`
finishes with exit code 0 and installs nothing.

```
# Storm Relay web uses only the Python standard library.
# There is nothing to install.
```

### The deploy log is your terminal now

On your laptop, errors appear in the terminal. On Render, they appear in the service's
logs **[VERIFY: Logs tab name]**. That is why the examples above use
`print(..., flush=True)`: a program not attached to a terminal can hold its output in a
buffer, and then the log looks empty right when you need it.

---

## Why the wrong versions are tempting

**They pass every test you can run.** `127.0.0.1` is what every tutorial and every
Unit 7 stub used, because it is the safe choice on a laptop. `os.environ.get("PORT",
8000)` reads like a complete, careful line. It even has a default.

**The failure happens somewhere you cannot see.** You cannot watch Render start your
app. You push, you wait, and then you read a log. Beginners change three things at once
at this point and lose track of which one mattered.

**The defaults hide the type.** You wrote `8000` as a number because it is a number. The
environment writes `"10000"` as text because the environment only has text. Both look
like ports.

The defense is a habit: **run your app locally the way the host runs it.** Set `PORT`
yourself. Request the page through your network address, not `127.0.0.1`. Stop the model
and reload the page. If all three work, most of the deploy surprises are already gone.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Deploy** | Put a program on a server where other people can use it |
| **Host (address)** | Which network connections an app accepts. `127.0.0.1` is this machine only. `0.0.0.0` is every connection |
| **Port** | The numbered door an app listens on |
| **Environment variable** | A named setting the operating system hands a program when it starts. Always text |
| **`PORT`** | The environment variable Render uses to tell your app which port to listen on **[VERIFY]** |
| **Build command** | What the host runs once, before starting, to install what the app needs |
| **Start command** | What the host runs to start your app |
| **Health check** | A quick address that answers when the app is running |
| **Fallback** | What the app does when something it depends on is missing |
| **Cold start** | The delay while a sleeping free-tier app wakes up for its first visitor **[VERIFY behaviour]** |
| **Deploy log** | Where a host shows your app's output and errors |

---

## Self-check

**Question 1.** Your app prints `Listening on 127.0.0.1:10000` in the Render log, and
Render reports that it cannot reach your app. The port is right. What is wrong, and what
is the one-line fix?

**Question 2.** Write the exact output of this program, including whether it crashes.

```python
render = {"PORT": "10000"}
laptop = {}
print(type(render.get("PORT", 8000)).__name__)
print(type(laptop.get("PORT", 8000)).__name__)
```

**Question 3.** A classmate's `/health` route asks the language model "are you there?"
and returns 200 only if the model answers. It works in the lab. Explain in two sentences
what happens on Render and why the design is wrong even though the code is correct.

---

### Answers

**1.** The app is bound to `127.0.0.1`, so it only accepts connections from inside the
same machine, and Render's router is not inside it. Change the host to
`HOST = "0.0.0.0"`.

**2.**

```
str
int
```

No crash. The first dictionary holds `PORT` as the text `"10000"`, so `.get()` returns
that string. The second has no `PORT`, so `.get()` returns the default you typed, the
number `8000`. Same line of code, two types. This is exactly why an app can pass every
test on a laptop and crash on Render.

**3.** On Render there is no model, so the health check fails every time and the host
treats a working app as broken. Health should report whether your app is running,
and a missing optional dependency is something the app handles with a fallback, not a
reason to call itself dead.
