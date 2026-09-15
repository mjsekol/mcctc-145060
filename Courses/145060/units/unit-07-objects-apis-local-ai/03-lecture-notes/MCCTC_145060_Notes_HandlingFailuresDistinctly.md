# Lecture Notes: Handling 404, Timeout, and Rate Limit Distinctly
## 145060 Programming · Unit 7 · Week 16 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_HandlingFailures.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_HandlingFailures.pptx)

If you missed class, you can learn this concept from this file alone. You need the lab's
fixture server running to try the examples.

**This is the syllabus outcome that names three failures by name, and it is a WebXam
item.** Consume an external API and handle 404s, timeouts, and rate limits distinctly.

---

## Why this exists

Yesterday you asked a server for data on the happy path. Today you plan for the days it
does not go right, because most days it does not. Each failure means something different
to the person waiting, and a good program says which one happened and what to do:

- **404 Not Found:** the thing you asked for does not exist. Retrying will never help.
- **Timeout:** the server is there but too slow right now. Trying later might help.
- **429 Too Many Requests:** you are asking too fast. Waiting the requested time helps.

Printing "Error" for all three throws away the one thing the person needed to know.

---

## The concept in plain language

Different failures raise different exceptions, and you catch them separately. The one
rule you must get right is the order:

**`HTTPError` is a kind of `URLError`, so catch `HTTPError` first.** Python runs the
first `except` clause that matches. If `URLError` comes first, a 404 gets caught there
and reported as "cannot connect," which is wrong.

The status code lives on the `HTTPError`. A timeout arrives as a `TimeoutError`, either
on its own or inside a `URLError`. A refused connection arrives as a `URLError` whose
reason is not a timeout.

---

## Worked example 1: telling a 404 from a 429

```python
import urllib.error
import urllib.request

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def status_of(path):
    try:
        with opener.open("http://127.0.0.1:8070" + path, timeout=5) as response:
            response.read()
        return "ok"
    except urllib.error.HTTPError as error:
        error.close()
        return f"HTTP {error.code}"

print(status_of("/api/v1/stations/north-field/observations"))   # ok
print(status_of("/api/v1/stations/nope/observations"))          # HTTP 404
```

Output:

```
ok
HTTP 404
```

The status code is on `error.code`. A 404 and a 429 are both `HTTPError`, and the code
is how you tell them apart.

---

## Worked example 2: the full set, each with its own message

```python
import json
import urllib.error
import urllib.request

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def fetch(url, timeout):
    try:
        with opener.open(url, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8")), None
    except urllib.error.HTTPError as error:       # must be first
        error.close()
        if error.code == 404:
            return None, "NOT FOUND. Check the id. Retrying will not help."
        if error.code == 429:
            wait = error.headers.get("Retry-After", "a few")
            return None, f"RATE LIMITED. Wait {wait} seconds, then try again."
        return None, f"SERVER ERROR. HTTP {error.code}. Try again later."
    except urllib.error.URLError as error:
        if isinstance(error.reason, TimeoutError):
            return None, "TIMED OUT. Try again in a minute."
        return None, f"CANNOT CONNECT. Is the server running? ({error.reason})"
    except TimeoutError:
        return None, "TIMED OUT. Try again in a minute."
```

Each failure returns its own message. The caller gets either the data or a sentence that
says what to do. Run against the fixture in normal, error, and slow modes to see each
branch. A verified run of the reference solution shows exactly this:

```
NOT FOUND. The feed has nothing at that address. Check the station id...
TIMED OUT. The feed did not answer within 5 seconds...
FEED ERROR. The feed had a problem on its end (HTTP 500)...
```

---

## Worked example 3: reading Retry-After for the wait time

A 429 usually tells you how long to wait, in a header.

```python
try:
    with opener.open("http://127.0.0.1:8070/api/v1/stations", timeout=5) as r:
        r.read()
except urllib.error.HTTPError as error:
    if error.code == 429:
        seconds = error.headers.get("Retry-After", "5")
        print("The server wants us to wait", seconds, "seconds")
```

Against a rate-limited fixture, this prints something like:

```
The server wants us to wait 7 seconds
```

That number lets a program wait exactly long enough and try once more, instead of
guessing. Whether to retry automatically or tell the user is a design choice you weigh
by how long the wait is.

---

## The wrong version, and why it is worse than a crash

```python
try:
    data = fetch(url, 5)
except Exception:
    print("Error")
```

There is no traceback and no crash. There is also no information. A 404, a timeout, and
a 429 all print `Error`. The person cannot tell whether the id is wrong, the server is
slow, or they are asking too fast. Each of those has a different fix, and this code hides
all of them behind one word.

### Write this down

> One message for every failure is a bug that does not crash.

This is both a Requirements Fit failure and a Security failure. Swallowing errors hides
real problems, and hiding real problems is how small failures become big ones.

---

## Why the wrong version is tempting

`except Exception: print("Error")` makes the red text go away, and it is one line. It
feels safe, because the program no longer crashes. But not crashing is a low bar. The
job of error handling is not to silence errors. It is to turn a failure into a clear,
honest message so the person can act. A single catch-all does the opposite: it silences
the failure and loses the reason.

The habit that prevents it: name each failure you expect, and give it its own message.
Catch the general `Exception` last, if at all, and never with a message as empty as
"Error."

---

## Vocabulary

| Term | What it means |
|---|---|
| **`HTTPError`** | Raised for an HTTP status like 404, 429, or 500. Has `.code`. |
| **`URLError`** | Raised when the request cannot complete, like no connection. |
| **`TimeoutError`** | Raised when a request runs past its timeout. |
| **404 Not Found** | The thing asked for does not exist. |
| **429 Too Many Requests** | You are asking too fast. Often carries `Retry-After`. |
| **500 error** | The server failed on its own end. Not your request's fault. |
| **`Retry-After`** | A header saying how many seconds to wait before retrying. |

---

## Self-check

**Question 1.** Why must `except urllib.error.HTTPError` come before
`except urllib.error.URLError`?

**Question 2.** For each failure, say whether retrying the exact same request could ever
help: a 404, a timeout, a 429.

**Question 3.** A program prints `Error` for every failure. Name the two rubric
dimensions this violates and say what a person loses.

---

### Answers

**1.** Because `HTTPError` is a kind of `URLError`, and Python runs the first matching
`except`. If `URLError` came first, it would catch every `HTTPError` too, so a 404 would
be reported as a connection failure. The specific one has to come first.

**2.** A 404 will never succeed on retry, because the thing does not exist. A timeout
might succeed later, if the server was briefly busy. A 429 will succeed after you wait
the requested time, because the server is fine and only wants you to slow down.

**3.** Requirements Fit, because the spec asked for distinct handling and this gives one
message. Security, because swallowing errors hides real problems. The person loses the
one thing they needed: which failure happened and what to do about it.
