# Gate 2: Adversarial Review · Week 17
## 145060 Programming · Unit 7 · Thursday, January 14

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed. Gate 2 runs Thursday
this week so Friday can hold Problem Drop #4.

The program is `gate2-w17-files/high_scores.py`. It talks to a fixture,
`score_server.py`, in the same folder. Copy both and run them.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got `high_scores.py`. It
runs and shows scores. Your job is to find what is wrong.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**One of these makes a failure look like success.** When the server is slow or down, the
program says something that is not true. Run it against a slow server and read carefully.

---

## PART A: The requirements

> Write `high_scores.py` that shows the arcade high scores for one game from the score
> API. It must:
>
> 1. Fetch the scores for the game named on the command line.
> 2. Print the **top three** scores, highest first.
> 3. Handle a **404, a timeout, and a rate limit (429) distinctly**, each with its own
>    message that tells the user what happened.
> 4. Keep the API key **out of the code file**, reading it from the environment.
> 5. If the game exists but has no scores yet, say so.

---

## PART B: What the AI produced

The code is in `gate2-w17-files/high_scores.py`. Start the fixture, then run the client:

```
python score_server.py
python high_scores.py pixel-racer
```

A real run against the normal server:

```
pixel-racer: 4 scores on record
Top three:
  NovaFox      48210
  PixelMoth    47990
```

**Read those lines against the five requirements before you read the code.** Two things
are already wrong in that output.

The fixture has modes so you can trigger the failures:

```
python score_server.py --mode slow      every request takes 10 seconds
python score_server.py --mode rate      every request is rate limited (429)
python score_server.py --mode empty     the game exists but has no scores
```

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real user**,
and **the fix**. Then one final entry: **what I was unsure about**, naming something
specific. That entry is scored and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** run it against the normal server. Count the scores printed.
- **Next 10:** run it against the slow server and the rate server. Read what it says.
- **Next 10:** read Part A one requirement at a time and point at the line that meets it.
- **Rest:** read each comment and name against the code. Ask whether it is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states
the security weighting before you start.

**Four of five is a strong score.**
