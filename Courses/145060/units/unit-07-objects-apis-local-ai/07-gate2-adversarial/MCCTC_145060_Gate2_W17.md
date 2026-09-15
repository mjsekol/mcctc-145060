# Gate 2: Adversarial Review · Week 17
## 145060 Programming · Unit 7 · Week 17, Friday

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

The program is `gate2-w17-files/study_streak.py`. Its `tip` command talks to a fixture,
`tip_server.py`, in the same folder. Copy both.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got `study_streak.py`. It
runs. This is the security week, so read it as an attacker would, not only a user.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**The security defect only shows up when something goes wrong.** Run the `tip` command
with no server running, and read every line it prints. One of those lines should never be
on a student's screen.

---

## PART A: The requirements

> Write `study_streak.py` that tracks a daily study streak in `streak.json`. It must:
>
> 1. `record` today's study. **Recording twice in one day must not raise the streak
>    twice.** One day, one increment.
> 2. `status` shows the current streak.
> 3. `tip` asks the local model for a study tip and shows it, **only after checking the
>    reply is finished** and has text.
> 4. Read the reset code from the environment, not from the file.
> 5. On any error, show a friendly message that **does not reveal internal details**.

---

## PART B: What the AI produced

The code is in `gate2-w17-files/study_streak.py`. Try it:

```
python study_streak.py record
python study_streak.py status
python tip_server.py            (in another terminal)
python study_streak.py tip
```

The fixture has a `not_done` mode, for a model that gets cut off:

```
python tip_server.py --mode not_done
python study_streak.py tip
```

**To see the security defect, run `tip` with no server running**, and read every line:

```
python study_streak.py tip
```

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real student**,
and **the fix**. Then one final entry: **what I was unsure about**, naming something
specific. That entry is scored and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 10:** run `record` twice in one day and check `status`. Count carefully.
- **Next 10:** run `tip` with no server, and with the `not_done` server. Read every line.
- **Next 10:** read Part A one requirement at a time and point at the line that meets it.
- **Rest:** read each comment against the code under it. Ask whether it is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **The security defect
is double-penalized.** Your instructor states this before you start.

**Four of five is a strong score.**
