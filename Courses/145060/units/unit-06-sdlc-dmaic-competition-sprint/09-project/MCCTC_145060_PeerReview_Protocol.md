# Peer Code Review Protocol
## 145060 Programming · Unit 6 · Reviews 1 and 2

**Review 1:** Monday, December 14, Build 2, 40 minutes. You review another team's
Sprint 1 code. **Review 2:** Thursday, December 17, Build 1, 30 minutes plus 5 minutes
to merge and tag. You review another team's change branch before it merges into their
baseline.

**Both teams in a pair review at the same time.** Each team leaves one member at its own
screen as the author. Its other members go to the partner team's screen as reader and
recorder.

**Competencies:** 5.6.9 (review by peer walkthrough), 5.6.13 (code reviews by peer
walkthrough and static analysis), 1.2.3 (verbal, nonverbal, and active listening).

---

## Why reviews exist

Every Gate 2 this semester, you reviewed code a model wrote. The model could not
argue back and did not have feelings about your findings. A peer review is the same
five dimensions with two differences that make it harder.

**The author is in the room.** They know things about the code you do not, and you
know things about it they cannot see, because they wrote it and their eyes slide over
their own assumptions. A review combines the two.

**You will be reviewed next.** How you give a finding is how you will receive one.

Reviews catch different defects than tests do. A test only checks what somebody
thought to check. A reviewer asks what nobody thought to check.

---

## The one rule

> **Review the code, never the coder.**

"This function hides errors" is a finding. "You always hide errors" is an attack, and
it is also useless, because it names no line and no fix. If a sentence in your review
would still make sense with the author's name in it, rewrite it.

---

## Roles during the review

A review has three roles. On a team of three, the recorder also reads.

| Role | Who | Job |
|---|---|---|
| **Author** | One member of the team being reviewed | Walks the reviewers through the code. Answers questions. Does not defend, argue, or fix during the review. |
| **Reader** | One reviewer | Keeps the walkthrough moving through the checklist, one requirement at a time. |
| **Recorder** | One reviewer | Writes every finding on the scoring form as it is found, with a line number. |

**The author's job is the hardest.** You will want to explain why the code is the way
it is. Say "noted" and let the recorder write it down. You respond in writing later,
in `docs/review_1.md`, where you can accept, reject, or defer each finding with a
reason. Arguing during the review costs everyone the time to find the next defect.

---

## The procedure, 40 minutes

### 1. Static analysis first · 5 minutes

Before any person reads the code, run the machine checks. They are fast and they do
not get tired.

```
python -m py_compile yourprogram.py
python review_check.py yourprogram.py
```

`py_compile` confirms Python can read the file at all. `review_check.py` is the
checker from Monday's lesson, in `05-labs/lab-u06-03-files/`. Paste both outputs onto
the scoring form.

**Treat every static finding as a question, not a verdict.** A checker flags
`shopping_list` as a possible secret because it contains the letters "pin." A person
decides whether a finding is real.

### 2. Run the acceptance tests · 3 minutes

```
python test_yourprogram.py
```

Record the pass and fail counts. If anything fails, that is a Correctness finding and
it goes on the form first.

### 3. The walkthrough · 20 minutes

The author shares their screen and walks through the program **in the order the
requirements are written**, not the order of the file. For each requirement:

1. The reader reads the requirement and its acceptance criteria aloud.
2. The author points at the lines that satisfy it.
3. The reviewers ask: what input would break this? Then one of them runs it.
4. The recorder writes down anything found.

If the author cannot point at the lines for a requirement, that is a Requirements Fit
finding. Keep going.

### 4. The five-dimension pass · 7 minutes

The reader goes through the checklist below out loud. Anything new goes on the form.

### 5. Score and hand over · 5 minutes

Reviewers score each dimension out of 20 on the form, agree the totals, and hand the
form to the authors. Authors say one thing: "thank you." Responses happen in writing.

**Review 2 is 30 minutes, then 5 minutes to merge and tag.** Static analysis 3 minutes,
tests 2, walkthrough 15, five-dimension pass 5, score and hand over 5. Review only the
change: compare the branch against the `v1.0` tag, and ask the change review questions
at the bottom.

---

## The checklist

### Correctness
- Do all acceptance checks pass?
- Try both sides of every boundary. Is anything off by one?
- Does any `except` block hide a failure instead of reporting it?
- Does any `.get()` with a default quietly cover a misspelled key?
- Is anything compared as text that should be compared as a number?

### Security
- Is every input checked before it is used: typed input, file contents, file names?
- Can a value that should be refused get through, such as a negative count or a blank?
- Is anything that should be secret written into the code?
- Could the program overwrite or damage a file it should only read?

### Readability
- Does every function have a docstring that matches what it does?
- Does every name say what the value is? Does any comment disagree with its code?
- Could a new team member find where a requirement is handled in under a minute?

### Performance
- Is any file opened, or any total recomputed, inside a loop when once would do?
- Is a list searched repeatedly where a set or dictionary would answer directly?

At this size, runtime is rarely the problem. This row scores **work done more times
than it needs to be**, because that work is also code somebody has to maintain.

### Requirements Fit
- Does every requirement have code the author can point at?
- Does every acceptance criterion have a check in the test file?
- Is there anything built that nobody asked for?

---

## How to write a finding

Every finding has four parts. A finding missing one of them does not count.

| Part | Weak | Strong |
|---|---|---|
| **Where** | "the report part" | "`report()`, line 82" |
| **Dimension** | (none) | Performance |
| **Consequence** | "inefficient" | "Reopens `cart.json` once per laptop, 24 times per report, so a corrupt file fails 24 ways" |
| **Fix** | "make it better" | "Load the cart once before the loop and pass it in" |

**Severity.** Mark each finding **must fix** (a requirement fails, data can be damaged,
or a secret is exposed), **should fix** (it works but will cause a real problem), or
**consider** (a genuine improvement that can wait).

---

## Giving and receiving findings

These are the listening and communication skills in competency 1.2.3, used for a
real purpose.

**When you give a finding:**
- Point at the line on the screen. Nonverbal matters: pointing at code keeps attention
  on the code.
- Say the consequence as a question first: "What happens here if the seat code is
  blank?" Let the author see it.
- Say one thing the code does well before the end of the review. Not as a cushion. As
  information, because it tells them what to keep.

**When you receive a finding:**
- Restate it before responding: "So you are saying a blank seat marks the laptop as
  returned." If you cannot restate it, ask a question until you can.
- Watch your own face and posture. Crossed arms and a sigh say "I am not listening"
  louder than any word.
- "Noted" is a complete answer during the review.

---

## Change review questions, Review 2 only

A change review asks a different question from a first review. **Not "is this code
good," but "did this change do only what was requested, and did it break anything
that was already accepted?"**

1. Read the change request. What exactly was asked for?
2. Which functions did the branch change? Compare against `v1.0`.
3. For every changed function, what else calls it? Did any of those behaviors change?
4. Do all the checks that passed at `v1.0` still pass? Were checks added for the change?
5. Did the change remove any validation, any check, or any error message that existed
   before?
6. Is anything in the branch that the change request did not ask for?

Question 5 is where change reviews earn their time. Code that is deleted leaves no
line to point at, so nobody reviews it unless somebody asks.

---

## What you submit

- The completed scoring form, handed to the authors and committed to **their**
  repository as `docs/review_1.md` or `docs/review_2.md`, with their response below it
- A copy committed to **your own** repository as `docs/reviews_given.md`

A review counts as complete when every section of the scoring form is filled in, the
static analysis output is pasted, and every finding has all four parts.
