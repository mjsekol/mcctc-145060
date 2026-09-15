# Lab U7-02: Practice Check
## 145060 Programming · Unit 7 · Week 16

**Gate:** 3 (open tooling). **Duration:** three Build blocks, Monday through Wednesday.
**Competencies:** 5.5.7 (read inputs from APIs), 5.3.10 (error handling), 3.2.1 and
9.3.4 (secure configuration).

**Files for this lab are in** `lab-u07-02-files/`: `practice_check.py` (the starter),
`weather_station_server.py` (the fixture you run), and `test_practice_check.py` (the
acceptance tests). Copy all three into your repository.

---

## The scenario

Before a team walks outside, a coach has to decide: is practice on, or does it move
inside? The district runs a weather station feed for the practice fields. Your program
asks that feed for the last hour of readings and for lightning, and applies the coach's
rule. The stations and the feed are invented for this lab.

## What you will build

A command-line tool. `python practice_check.py` lists the stations.
`python practice_check.py north-field` reports the readings for one station and says
whether practice is on. The coach's rule: practice moves inside if any gust in the last
hour reached 30 mph, or if any lightning struck in the last 30 minutes.

---

## Before you start

The feed runs on your own computer. Start it in one terminal and leave it open:

```
python weather_station_server.py
```

It prints a feed key. You need that key for the lightning readings, in Part 3. Run the
client in a second terminal. Run the tests any time; they start their own copy of the
feed:

```
python -m unittest test_practice_check.Part1Tests
```

---

## Part 1: Monday, one request, one JSON reply

### Step 1. Write get_json
Replace TODO 1. Build a `Request` for `settings["base_url"] + path`, open it with
`DIRECT.open(request, timeout=settings["timeout"])`, read the bytes, decode as UTF-8, and
return `json.loads` of the text.
**Observable result:** `Part1Tests` `test_get_json_returns_the_station_list_as_a_dictionary`
passes.

### Step 2. Write decide for real readings
Replace TODO 2. Find the strongest gust in the readings, then return the lines: a header,
a summary, and the decision. Move inside if the strongest gust is 30 or more, or if
lightning struck.
**Observable result:** a calm reading says practice is on; a 30 mph gust says move inside.

### Acceptance criteria, Part 1
1. All four `Part1Tests` pass
2. `decide` moves inside at exactly 30 mph, not only above it

---

## Part 2: Tuesday, every failure gets its own message

### Step 3. Write fetch with a branch per failure
Replace TODO 3. Wrap `get_json` in a `try`. Catch `HTTPError` first (it is a kind of
`URLError`). Give a 404, a feed error, a timeout, an unreachable server, and a
non-JSON reply each its own message. Return `(data, None)` on success or
`(None, message)` on failure.
**Observable result:** the 404, feed-error, not-JSON, timeout, and unreachable tests pass.

### Step 4. Decide what empty readings mean
Finish TODO 5 inside `decide`. An empty list of readings is not calm weather. It means
the station is not reporting. Return a NO DECISION message, not "practice is on."
**Observable result:** `test_empty_readings_are_not_calm_weather` passes.

### Acceptance criteria, Part 2
3. All of `Part2Tests` pass
4. An empty readings list never produces "PRACTICE IS ON"

---

## Part 3: Wednesday, settings and the key from the environment

### Step 5. Rewrite load_settings
Read the base URL, the timeout, and the key from the `environment` dictionary, with
defaults. Refuse a timeout that is not a number by raising `ValueError`.
**Observable result:** `Part3Tests` settings tests pass.

### Step 6. Send the key in a header, and add the 429 retry
In `get_json`, if the key is set, send it in the `X-Feed-Key` header. In `fetch`, on a
429, read `Retry-After` and, if the wait is short, wait and try once more.
**Observable result:** `test_wrong_key_is_refused_with_its_own_message` and
`test_lightning_moves_practice_inside` pass. Set the key in your terminal:

```
$env:PRACTICE_FEED_KEY = "the key the feed printed"
python practice_check.py track
```

### Step 7. README and push
Three sections: what it is and how to run it, a real run of each of the four station
kinds, and one thing you learned about handling failures. Confirm no key is in any file.
**Observable result:** README renders, all 17 tests pass, pushed.

### Acceptance criteria, Part 3
5. All 17 tests pass together
6. No key is written in any file; the program reads it from the environment

---

## Acceptance criteria, full lab

- [ ] `python -m unittest test_practice_check` reports 17 passed
- [ ] A 404, a timeout, and a rate limit each print a different message
- [ ] An empty readings list never says "practice is on"
- [ ] The key is read from the environment, never written in a file
- [ ] README has all three sections with a real run of each station kind
- [ ] Three or more commits, pushed

---

## If it breaks

### 1. HTTPError caught as a connection failure

```
CANNOT CONNECT ...   (when you expected NOT FOUND)
```

**Cause:** your `except urllib.error.URLError` comes before `except HTTPError`. Since
`HTTPError` is a kind of `URLError`, the general one catches the 404 first. Put the
specific `HTTPError` clause first.

### 2. JSONDecodeError on a real reply

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Cause:** you asked an address that returns an HTML page, not JSON, or you did not
handle the non-JSON case in `fetch`. Catch `json.JSONDecodeError` and return a NOT JSON
message.

### 3. The lightning reading is refused

```
REFUSED. The feed key is missing or wrong ...
```

**Cause:** `PRACTICE_FEED_KEY` is not set in this terminal, or does not match the key the
feed printed. Set it with `$env:PRACTICE_FEED_KEY`. This is expected until you do.

### 4. The program prints "practice is on" for an offline station

**Cause:** you did not handle the empty readings list. No readings is not calm weather.
Check `len(observations) == 0` before looking at gusts. **No error appears**, which is
why the test exists.

---

## Stretch goal

Add a `--all` option that checks every station in one run and prints a one-line verdict
for each. Then answer in your README: if two stations disagree, which one does the coach
trust, and how would your program help them decide? There is no single right answer; a
good one names a rule, like trusting the station closest to the field.

---

## Submission checklist

- [ ] `python -m unittest test_practice_check` reports 17 passed
- [ ] Ran it against a live, a stale, an offline station, and a bad id
- [ ] Grepped your files: no key anywhere
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still fighting the three-step request at 20 minutes into Part 1 | SCAFFOLDED |
| Working steadily, asking about wording rather than mechanics | STANDARD |
| Finished Part 2 early, or asked about retrying automatically | EXTENDED |
| Says weather is boring, or does not do a sport | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `get_json` is written for you. You write `decide` and `fetch`.
- **Steps:** Part 2 handles only three failures: 404, timeout, and a bad reply. The
  429 retry and the wrong-key branch are dropped.
- **Step 4 stays.** Do not cut the empty-readings case. It is the point of the day.
- **Checkpoints:** show you the terminal after Part 1 and after each `fetch` branch.

**Acceptance criteria:** `Part1Tests` pass, plus the 404, timeout, and not-JSON tests,
plus the empty-readings test. Full completion earns what a STANDARD student earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not taught.

**Added requirement.** A single timeout is blunt. Make `fetch` try a slow request up to
three times with a growing wait between attempts, one second, then two, then four, before
it gives up. This is called backoff.

**Hint, not the answer.** Look up "exponential backoff" and read one short explanation.
The pattern is a loop with a wait that doubles each time, capped at a maximum. Do not
retry a 404, because it will never succeed. Only retry a timeout or a 500.

**The honest warning:** it is tempting to write a retry loop that waits on a 404 too, which
only makes a permanent failure take twelve seconds instead of one. Retry only the
failures that could succeed later. Say in your README which failures you retry and why.

**Acceptance criteria:** all STANDARD criteria, plus backoff on retryable failures only,
plus the README note on what you retry and why.

---

## APPLIED

**For the student who does not do a sport.** Same skills, different feed.

**Changed scenario.** Pick a real decision someone makes from live-ish data: is the lake
warm enough to swim, is the trail open, is the parking lot full, is the pool lane free.
Use the same weather fixture, or ask your instructor to point the fixture at a different
set of readings.

**What you build.** A tool that reads the feed, applies a rule you define, and gives a
clear verdict, with a different message for each way the feed can fail.

**The extra requirement that makes it the same lab.** Your README must include a section
called `The rule and its edges` stating the exact threshold and what happens at the
boundary, plus what your tool says when the feed has no data, which must not be the same
as a confident verdict.

**Acceptance criteria:** all STANDARD criteria applied to your chosen decision, plus
`The rule and its edges`, plus distinct handling of an empty feed.

**Grading:** same scale. Requirements Fit is judged on whether every failure is handled
distinctly and an empty feed never reads as a confident answer.
