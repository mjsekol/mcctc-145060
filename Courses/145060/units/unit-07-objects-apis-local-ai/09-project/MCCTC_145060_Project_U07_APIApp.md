# Project: API-Consuming Application
## 145060 Programming · Unit 7 · Consume a Real-Shaped API

**Mode:** solo. **Gate:** 3, full tooling. **Periods:** Week 16, alongside the API labs.

**Competencies:** 5.5.7 (read inputs from an API), 5.5.4 (call other programs), 5.3.10
(error handling), 3.2.1 and 9.3.4 (secure configuration), 5.3.12 (classes to model the
data).

---

## The brief

Read this as though a person said it to you, because a person did.

> There is a data feed I check all the time, and I want a small program that reads it and
> tells me the one thing I actually care about, laid out so I can read it in a second. It
> has to work when the feed is having a bad day. If the feed is down, or slow, or I ask
> for something that does not exist, or I have been hitting it too much, I want to know
> which of those happened and what to do about it. I do not want a wall of red text, and I
> do not want it to lie to me and say there is no data when really it only could not
> reach the feed.

**That is the whole brief.** The program's value is not the happy path. It is that every
way the feed can fail gets an honest, distinct answer.

## Where the project comes from

**A feed you would actually check.** The provided fixture is the Millbrook Valley Open
Data service, an invented town's public feed with bus arrivals, weather stations, and park
courts. Build against it. You may instead point your program at a real public API that
needs no key, but the fixture must still be your fallback for the demo, because the network
is not reliable in the lab.

---

## Requirements

### Technical

1. **Read a real-shaped JSON API** over HTTP, standard library only.
2. **Handle a 404, a timeout, and a rate limit (429) distinctly.** Each gets its own
   message that says what happened and what to do. Also handle a server error and an
   unreachable server.
3. **An empty result is not a failure and a failure is not an empty result.** If the feed
   returns nothing, say so honestly; if it could not be reached, say that instead. Never
   report a failure as "no data."
4. **All configuration from the environment:** the base URL, the timeout, and the key.
   **No key or changeable address written in the code.**
5. **Validate any input that becomes part of a request** before it is sent.
6. **Model the reply with a class** so a bad reply fails with a clear reason instead of
   printing nonsense later.
7. **A test suite** that starts the fixture itself and needs no live network.

### Repository

```
api-app/
  <yourapp>.py          the program
  <fixture>.py          the fixture server, so the demo always works
  test_<yourapp>.py     the test suite
  README.md
```

### README, four sections

1. **What it is and how to run it**, including starting the fixture and setting the key.
2. **Every failure it handles**, with the message for each.
3. **A real run** of a success and at least two different failures.
4. **Configuration**, which environment variables it reads and their defaults.

---

## Constraints, and why each exists

| You may not | Why |
|---|---|
| Use a package outside the standard library | The lab machines have only the standard library, and `urllib` plus `json` is enough. |
| Write a key or a changeable address in the code | A committed key is public, and a baked-in address breaks on another machine. |
| Use one `except` for every failure | The brief demands distinct handling. One message for all failures is the thing it forbids. |
| Report a failure as an empty result | The brief names this exactly: do not say "no data" when you could not reach the feed. |
| Require a live internet API for the demo | The lab network is unreliable. Your fixture must carry the demo. |

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 16 Mon, end of Build 2 | The one thing your program tells the user, in one sentence |
| **Measure** | Week 16 Mon, end of Build 2 | Every endpoint you call, and every way each can fail |
| **Analyze** | Week 16 Tue, end of Build 2 | On paper: the message for each failure, and how you tell an empty result from a failure |
| **Improve** | Tue to Thu Week 16 | Build it: the request, the failure branches, the class, the config |
| **Control** | Week 16 Thu, end of Build 2 | Tests pass, README complete, a success and two failures recorded |

**Analyze is the checkpoint that saves this project.** Write the message for each failure
on paper before you code. A student who has not decided what a timeout should say will
write one catch-all and lose the whole point.

---

## Milestone schedule, against actual class days

| Day | Goal |
|---|---|
| Week 16 Mon | Fixture running, one successful request parsed and displayed |
| Week 16 Tue | Every failure branch, each with its own message |
| Week 16 Wed | Config from the environment, the reply class, input validation |
| Week 16 Thu | Tests, README, recorded runs. Submit |

---

## Three worked scope examples

These calibrate you. Do not build any of these three; they are occupied.

### Too small
> Fetch the bus stops and print the raw JSON.

One request, no failure handling, no formatting, no config. It meets almost none of the
requirements and does not do what the brief asked.

### About right
> **Next Bus.** Reads the transit feed for one stop, prints a clean departure board, and
> handles a 404, a timeout, a 429, a server error, and an unreachable feed with five
> different messages. Tells a stale feed apart from a stop with no buses. Key and URL from
> the environment. A `StopBoard` class checks the reply. Tests pass.

Every requirement, at a size one person finishes and explains. This is the bar.

### Too big
> A dashboard that polls all three feeds every ten seconds, caches results, draws graphs,
> and sends a text when a bus is late.

Polling, caching, graphs, and notifications are each a project. This is a good capstone
idea. It is far too big for one week.

**The calibration question:** can you name, right now, the five different messages your
program prints for the five different failures? If not, the core of the project is not
designed yet.

---

## The five-minute demo

1. **What it tells you, in one sentence.** (30s)
2. **A successful run.** The one thing, laid out cleanly. (60s)
3. **Two failures, live.** Stop the fixture, or run it in slow or rate mode. Show two
   different honest messages. (120s)
4. **One decision you made and why.** A message you chose, the empty-versus-failure split,
   the config choice. (60s)
5. **Questions.** (30s)

**Item 3 is the graded part.** The failures are the project. Show two of them behaving
differently and honestly.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Reads the feed. Five failures handled distinctly. Empty result and failure are never confused. |
| **Code Quality** | 20 | Config from the environment, no key in code. `HTTPError` before `URLError`. A reply class. Readable. |
| **Documentation** | 20 | Four README sections. Every failure's message listed. A success and two failures recorded. |
| **Process** | 15 | DMAIC checkpoints on time. Commits spread across the week. |
| **Demonstration** | 10 | Can explain any line. Shows two failures behaving differently. |
| **Polish** | 10 | The output reads at a glance. Messages tell the user what to do, not only what broke. |

**The fastest way to lose Functionality points** is a catch-all `except` that turns every
failure into one message. That is the exact thing the brief forbids.

---

## If you are stuck

**"I do not know what message a timeout should say."** Say what happened and what to do:
"The feed did not answer in time. Try again in a minute." Different from a 404, which will
never succeed on retry, so its message says check the id.

**"My program says no data when the feed is down."** That is the bug the brief names.
Separate a failure (return a message) from an empty-but-successful reply (say "none this
hour"). They are different and must read differently.

**"Where does the key go."** The environment, read with `os.environ.get`. Refuse to run if
it is not set. Never in a file.

**"I want to add a second feed."** Finish one feed with all five failures first. A second
feed with sloppy handling is worth less than one feed done right.

---

## The reference implementation

A complete, verified reference is in `09-project/reference-implementation/api-app/`, with
its own README. It reads the transit feed, handles five failures distinctly, keeps a stale
feed apart from a stop with no buses, takes all config from the environment, uses a
`StopBoard` class to check the reply, and passes 26 tests. Do not copy it. Build your own.
It is there for the instructor to compare behaviour.
