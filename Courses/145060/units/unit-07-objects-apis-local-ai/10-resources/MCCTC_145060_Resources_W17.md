# Additional Resources · Week 17
## 145060 Programming · January 11-15, 2027
### Topic: HTTP requests, JSON, failure handling, and calling a local model

Links marked **Confident** or **[VERIFY]**, same standard as every week.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff, the web APIs material | Mon-Tue | On-level | 30 min |
| 2 | Official docs: urllib.request | Mon | On-level | 15 min |
| 3 | Official docs: json | Mon | On-level | 10 min |
| 4 | Official docs: urllib.error and HTTP status meaning | Tue | On-level | 15 min |
| 5 | An article on HTTP status codes | Tue | On-level | 12 min |
| 6 | Ollama API generate reference | Thu | Extension | 15 min |
| 7 | SQ-10 API First Contact | Fri | Required-ish | 2 blocks |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, the material on fetching data from the web** ·
`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the exact
chapter, since the third edition reorganized the web material.

**Why this one.** It shows fetching data over HTTP in plain language, with real examples.
Our course uses the standard library `urllib` rather than the `requests` package the book
often uses, so tell students to read for the ideas, request, response, JSON, not to copy
the exact library calls.

**Skip:** anything that installs a package. We are standard library only.

---

## 2. Official documentation, urllib.request

`https://docs.python.org/3/library/urllib.request.html` · **Confident.**

**Assign a question, not the page.** It is a large page.

> Find `urlopen`. What does the `timeout` argument do, and what happens if you leave it out?

That settles Monday's rule that every request needs a timeout, from the primary source.

---

## 3. Official documentation, json

`https://docs.python.org/3/library/json.html` · **Confident.**

Read only `json.loads` and `json.dumps`. `loads` turns text into Python data; `dumps` turns
Python data into text. That is the whole week's use of it.

---

## 4. Official documentation, urllib.error

`https://docs.python.org/3/library/urllib.error.html` · **Confident.**

**The key fact to take from it:** `HTTPError` is a subclass of `URLError`. That is why you
catch `HTTPError` first. Read the two class descriptions and confirm the inheritance.

---

## 5. What the status codes mean

A reputable reference on HTTP status codes, for example the MDN page on HTTP response status
codes. · `https://developer.mozilla.org/en-US/docs/Web/HTTP/Status` · **[VERIFY]** the URL
before assigning; MDN is stable but confirm it resolves.

**Why this one.** 404, 429, and 500 are not arbitrary numbers. Reading what each class of
code means, 4xx is your side, 5xx is the server's, makes Tuesday's distinct handling make
sense rather than being memorized.

---

## 6. The local model API, for the curious

The Ollama API documentation for the `/api/generate` endpoint. · **[VERIFY]** the URL
before assigning, since vendor docs move. Search "Ollama API generate."

**Why this one.** Thursday's model call speaks this API. Reading the real request and
response fields, `model`, `prompt`, `stream`, `response`, `done`, shows that the bundled
stub matches a real server. **Do not require it.** Everything runs on the stub.

---

## 7. Side quest

**SQ-10 API First Contact** unlocks Friday. It is named in the syllabus as a Unit 7
deliverable. Consume a real no-key public API and handle a 404, a timeout, and a rate limit
distinctly. Bundle and description in
`Courses/Misc/side-quests/SQ-10-API-First-Contact/`. · **Confident**, it is in this
repository.

**Why it fits here.** It is the week's skill on a real feed instead of a fixture. A student
who handled the fixture's failures is ready to handle a real service's.

---

## For the student who is behind

1. The `Notes_HTTPAndJSON` lecture notes, typing the three steps until the types make sense
2. Python Tutor is not useful for network code; instead, run the fixture and the client
   side by side and watch the request in the fixture's log
3. Rewrite `get_json` from an empty file, then add one failure branch at a time

Do not assign all seven. A student who is behind and gets seven links reads none.
