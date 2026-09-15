# Lecture Notes: HTTP Requests and JSON Responses
## 145060 Programming · Unit 7 · Week 16 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_HTTPAndJSON.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_HTTPAndJSON.pptx)

If you missed class, you can learn this concept from this file alone. You need the lab's
fixture server running to try the examples. Start it in a second terminal first.

---

## Why this exists

Every program you have written so far worked with data it already had: typed in, read
from a file, computed. Real programs get data from other programs over the network. A
bus app asks a transit server. A weather widget asks a weather service. This week your
program becomes a customer of another program.

The reply comes back in a format called JSON, which you already met in Unit 5 for save
files. The new part is asking for it over HTTP and turning the reply into Python data.

---

## The concept in plain language

**Your program sends a request to a URL and gets a response back.** The response body
arrives as bytes. You decode the bytes to text. You parse the text as JSON, which gives
you a Python dictionary or list. Three steps, and each one has a job:

1. `opener.open(url)` sends the request and gives you a response.
2. `response.read()` gives the body as bytes.
3. `json.loads(text)` turns JSON text into Python data.

You will use the standard library only: `urllib.request` and `json`. No packages to
install.

---

## Worked example 1: the three steps, spelled out

```python
import json
import urllib.request

# Skip proxies. A school proxy cannot reach 127.0.0.1, and routing a local
# request through one fails in confusing ways.
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

with opener.open("http://127.0.0.1:8070/api/v1/stations", timeout=5) as response:
    raw_bytes = response.read()

print(type(raw_bytes))                  # <class 'bytes'>
text = raw_bytes.decode("utf-8")
print(type(text))                       # <class 'str'>
data = json.loads(text)
print(type(data))                       # <class 'dict'>
print(len(data["stations"]))            # 4
```

Output:

```
<class 'bytes'>
<class 'str'>
<class 'dict'>
4
```

Watch the type change at each step: bytes, then text, then a dictionary. Skip a step and
you get an error, which the wrong version below shows.

---

## Worked example 2: reaching into the parsed data

Once it is a dictionary, it is ordinary Python.

```python
with opener.open("http://127.0.0.1:8070/api/v1/stations/north-field/observations",
                 timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))

print(data["name"])                          # North Practice Field
print(len(data["observations"]))             # 4
print(data["observations"][0]["gust_mph"])   # 19
```

Output:

```
North Practice Field
4
19
```

A JSON object becomes a dictionary. A JSON array becomes a list. You navigate it with
the keys and indexes you already know.

---

## Worked example 3: always set a timeout

```python
# timeout=5 means give up after 5 seconds. Without it, a slow or dead server
# can freeze your program with no way out.
with opener.open("http://127.0.0.1:8070/api/v1/stations", timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))
print("Got", len(data["stations"]), "stations")
```

Output:

```
Got 4 stations
```

The `timeout` is not optional in real code. A request with no timeout can hang forever,
which is an availability problem you will name in Week 17. Set it every time.

---

## The wrong version, and the error it produces

The classic mistake is to parse a page that is not JSON. The fixture has an old address,
`/api/stations`, that returns an HTML page for old bookmarks:

```python
with opener.open("http://127.0.0.1:8070/api/stations", timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))
```

Output:

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

The reply was `<!doctype html>...`, and `json.loads` cannot read that. The error points
at column 1, character 0, because the very first character, `<`, is not valid JSON.

### Write this down

> Getting a reply is not the same as getting the data you asked for.

This is the running thread on the network. The crash here is the friendly case. The
dangerous case is a server that returns valid JSON containing an error message, which no
exception catches. You handle that next week.

---

## Why the wrong version is tempting

The URL looks right, the request succeeds, and `response.read()` returns something. It
feels like it worked. But "the server answered" and "the server answered with the data I
wanted" are two different claims. A wrong address, a redirect to a login page, or an old
endpoint can all return a real response that is not your data.

The habit that prevents it: check what you got, do not assume. Next week you wrap the
whole thing in error handling so a bad reply becomes a clear message instead of a crash.

---

## Vocabulary

| Term | What it means |
|---|---|
| **HTTP** | The rules programs use to ask servers for things over the web. |
| **Request** | Your program asking a server for something. |
| **Response** | What the server sends back. |
| **URL** | The address of the thing you are asking for. |
| **JSON** | A text format for data. Objects become dicts, arrays become lists. |
| **`urllib.request`** | The standard-library module for making requests. |
| **`json.loads`** | Turns JSON text into Python data. |
| **timeout** | How long to wait before giving up on a request. |

---

## Self-check

**Question 1.** Name the three steps between sending a request and having a Python
dictionary, and say what each one produces.

**Question 2.** A program does `data = json.loads(response)` and gets a `TypeError`
saying the JSON object must be str, bytes, or bytearray. What step was skipped, and what
is the fix?

**Question 3.** Why should every request have a timeout, and what kind of problem does a
missing timeout cause?

---

### Answers

**1.** Step one, `opener.open(url)`, sends the request and gives a response. Step two,
`response.read()`, gives the body as bytes. Step three, `json.loads(text)`, turns JSON
text into a Python dictionary or list. Bytes, then text, then data.

**2.** The `.read()` step was skipped. `json.loads` was handed the response object
itself, not its body. `json.loads` accepts text or bytes, but not a response object. The
fix is `json.loads(response.read().decode("utf-8"))`, which reads the body to bytes and
decodes it to text first.

**3.** So a slow or dead server cannot freeze the program forever. A missing timeout
causes an availability problem: the program hangs with no answer and no way out, and a
person waiting on it is stuck.
