# Lecture Notes: Calling a Local Model and Parsing Its Reply
## 145060 Programming · Unit 7 · Week 16 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_CallingALocalModel.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_CallingALocalModel.pptx)

If you missed class, you can learn this concept from this file alone. You need the lab's
stub model server running to try the examples.

**Be honest about what a language model is.** It generates plausible text. It can be
wrong, it can drop facts, and it does not know anything. Your program has to treat every
reply as untrusted until it has checked it. That is the whole lesson.

---

## Why this exists

A language model running on lab hardware can turn dry facts into readable prose: a room's
stored description into a narrated scene, a line of club facts into a friendly
announcement. You call it the same way you called the weather API, because it speaks
HTTP. The new part is that its reply is text a model made up, so it can be incomplete,
wrong, or missing the facts you needed. A careful program checks the reply before it
trusts it, and falls back to something it built itself when the reply is bad.

---

## The concept in plain language

You send a prompt to the model's `/api/generate` endpoint and get JSON back. The reply
carries two fields you care about: `response`, the text, and `done`, whether the model
finished. Status 200 is not enough. Before you use the text, check:

1. The reply is valid JSON and an object.
2. `done` is exactly `True`.
3. `response` is a string, and not empty.
4. Optionally, the text still contains the facts you needed.

If any check fails, you fall back. The fallback is the description or template your own
code holds, so the program always produces something correct.

---

## Worked example 1: the request and a good reply

```python
import json
import urllib.request

opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
payload = json.dumps({"model": "llama3.2", "prompt": "Say hello.", "stream": False})
request = urllib.request.Request("http://127.0.0.1:11434/api/generate",
                                 data=payload.encode("utf-8"),
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
with opener.open(request, timeout=20) as response:
    reply = json.loads(response.read().decode("utf-8"))

print(reply["done"])          # True
print(reply["response"])      # (the model's text)
```

Against the lab's announcement stub, `reply["done"]` is `True` and `reply["response"]`
is a sentence. Note `stream: False`, which asks for one whole reply instead of a stream
of pieces. This is a POST, because you are sending data, the prompt.

---

## Worked example 2: checking the reply before trusting it

```python
def usable_text(reply):
    if reply.get("done") is not True:
        return None
    text = reply.get("response")
    if not isinstance(text, str) or text.strip() == "":
        return None
    return text.strip()

print(usable_text({"response": "Meet at 3:15.", "done": True}))   # Meet at 3:15.
print(usable_text({"response": "Meet at 3:", "done": False}))     # None
print(usable_text({"done": True}))                                # None
```

Output:

```
Meet at 3:15.
None
None
```

The first reply is finished and has text, so it is used. The second was cut off, so
`done` is `False` and it is rejected. The third has no `response` at all. Each bad reply
returns `None`, which tells the caller to fall back.

---

## Worked example 3: falling back cleanly

```python
def announcement(reply, facts):
    text = usable_text(reply)
    if text is None:
        # The fallback the program built itself. Always correct.
        return f"{facts['club']} meets {facts['day']} at {facts['time']} in {facts['room']}."
    return text

facts = {"club": "Robotics Club", "day": "Thursday", "time": "3:15", "room": "Room 118"}
print(announcement({"response": "Meet at 3:", "done": False}, facts))
```

Output:

```
Robotics Club meets Thursday at 3:15 in Room 118.
```

The model reply was bad, so the program used its own template. The person reading the
morning announcements still gets a correct, complete sentence. A bad model never breaks
the feature; it only means you see the plain version.

---

## The wrong version, and the bug that does not crash

Skip the `done` check and print whatever came back:

```python
reply = {"response": "The transmitter dials glow amber. Type broadcast to", "done": False}
print(reply["response"])
```

Output:

```
The transmitter dials glow amber. Type broadcast to
```

**No error. A half-sentence printed as if it were finished.** The model was cut off, and
`done` was `False`, but nothing checked it. In the text adventure, a description that
loses "broadcast on 1470" could make the game unwinnable. The reply was valid JSON with
status 200, so no exception fires. Only your own check catches it.

### Write this down

> Check `done` before you trust the text. A 200 is not a finished answer.

Check `done` with `is not True`, not with `if not reply.get("done")`. The string
`"false"` is truthy, so a lazy truthiness check would pass a reply that is not done.

---

## Why the wrong version is tempting

The request succeeded, the JSON parsed, and `reply["response"]` has text in it. Every
sign says it worked. But a model can stop mid-sentence, reword a number, or drop a fact,
and none of that raises an error, because as far as HTTP and JSON are concerned the reply
is fine. The model's job is to produce plausible text, not correct text. Plausible and
correct are different, and only your program can tell them apart, by checking.

The habit that prevents it: never print a model reply straight through. Run it past your
checks first, and keep a fallback you control for when it fails.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Prompt** | The text you send the model, asking for what you want. |
| **`/api/generate`** | The endpoint an Ollama-compatible model server answers. |
| **`response`** | The field holding the model's generated text. |
| **`done`** | The field saying whether the model finished. Check it. |
| **`stream: False`** | Asks for one whole reply instead of a stream of pieces. |
| **Fallback** | The correct output your own code produces when the model fails. |
| **Untrusted** | Treated as possibly wrong until checked. Model replies are this. |

---

## Self-check

**Question 1.** Name the three checks a reply must pass before you use its text.

**Question 2.** Why is `if reply.get("done"):` not a safe check? Give the exact value
that defeats it.

**Question 3.** A model rewords "1470 kHz" as "fourteen seventy" in a room description.
No error appears. Why is that dangerous, and what kind of check catches it?

---

### Answers

**1.** The reply is valid JSON and an object, `done` is exactly `True`, and `response` is
a non-empty string. Only then is the text safe to use.

**2.** Because `.get("done")` can return the string `"false"`, which is truthy, so the
check passes on a reply that is not done. The value that defeats it is `"false"` (or any
non-empty string, or the number 1). Use `is not True` to require the real boolean.

**3.** In the text adventure a player needs the exact number `1470` to win, and
"fourteen seventy" would leave them unable to tune the transmitter, with no error to warn
anyone. A keep-phrase check catches it: after the reply passes the other checks, confirm
the required fact still appears in the text, and reject the reply if it does not.
