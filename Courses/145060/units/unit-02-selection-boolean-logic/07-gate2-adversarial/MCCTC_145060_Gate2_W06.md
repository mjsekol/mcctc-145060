# Gate 2: Adversarial Review · Week 6
## 145060 Programming · Unit 2 review · Thursday, October 15 · Build 2

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

This review closes Unit 2. The program uses only Unit 2 tools: `if`/`elif`/`else`, `and`,
`or`, `not`, nesting, and `match`. There are no loops in it.

---

## What you are looking at

A teacher asked an AI assistant to turn a late-work policy into a calculator. The policy is in
Part A. The program is in Part B. It runs, it uses `match` the way Monday's lesson did, and the
sample run is correct.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It gives the wrong answer for some input |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work or structure that is not needed |
| **Requirements Fit** | Something the policy asked for that is missing or different |

**At least two of these are bugs from this unit's lecture notes, wearing different clothes.**

---

## PART A: The late-work policy

> Write `late_work.py` to apply the late-work policy to one assignment.
>
> 1. Ask for the assignment type, the score earned, and the number of days late.
> 2. The score must be 0 through 100, and days late cannot be negative. Otherwise, refuse
>    with a message and apply no policy.
> 3. The only assignment types are `lab`, `project`, and `quiz`, typed in any capitalization.
>    Any other type is refused with a message naming the three types.
> 4. A quiz that is late at all is not accepted.
> 5. Projects get **one** grace day: subtract one day before applying the schedule.
> 6. The schedule, by counted days late:
>
>    | Counted days late | Penalty |
>    |---|---|
>    | 0 or fewer | none |
>    | 1 to 2 | 10 points |
>    | 3 to 5 | 25 points |
>    | 6 or more | not accepted, final score 0 |
>
> 7. The final score is never below 0.
> 8. Print the type, the original score, the penalty with its reason, and the final score.

---

## PART B: What the AI produced

Count line numbers from `# late_work.py` as line 1. Blank lines count.

```python
# late_work.py
#
# Applies the late-work policy to one assignment and prints the final score.
# Handles labs, projects, and quizzes, with the grace rules built in.

print("LATE WORK CALCULATOR")
print("-" * 20)

assignment_type = input("Assignment type (lab, project, quiz): ").strip().lower()
score = int(input("Score earned (0-100): "))
days_late = int(input("Days late (0 if on time): "))

NOT_ACCEPTED_DAYS = 6
SMALL_PENALTY = 10
LARGE_PENALTY = 25

# Refuse values that cannot be real before applying any policy.
if score < 0 or score > 100 or days_late < 0:
    print("Score must be 0-100 and days late cannot be negative.")
else:
    # Work out how many days count against the student.
    match assignment_type:
        case "quiz":
            # Quizzes are never accepted late.
            if days_late > 0:
                counted_days = NOT_ACCEPTED_DAYS
            else:
                counted_days = 0
        case "project":
            # Projects get two grace days.
            counted_days = days_late - 1
        case standard_type:
            # Labs and other standard work follow the normal schedule.
            counted_days = days_late

    # Apply the penalty for the counted days.
    if counted_days >= NOT_ACCEPTED_DAYS:
        penalty = score
        note = "not accepted"
    elif counted_days >= 1:
        if counted_days < NOT_ACCEPTED_DAYS:
            penalty = SMALL_PENALTY
            note = "1-2 days late"
    elif counted_days >= 3:
        penalty = LARGE_PENALTY
        note = "3-5 days late"
    else:
        penalty = 0
        note = "on time"

    final_score = score - penalty

    print(f"Type: {assignment_type}")
    print(f"Original score: {score}")
    print(f"Penalty: {penalty} ({note})")
    print(f"Final score: {final_score}")
```

### A real run, for reference

Typing `project`, `92`, `1`:

```
LATE WORK CALCULATOR
--------------------
Assignment type (lab, project, quiz): project
Score earned (0-100): 92
Days late (0 if on time): 1
Type: project
Original score: 92
Penalty: 0 (on time)
Final score: 92
```

**That output is correct.** The project was one day late and the grace day covered it.

---

## What to submit

For each defect: **line number**, **dimension**, **the exact inputs you typed to prove it**
(or, for a defect you can prove by reading, the lines that prove it), **what goes wrong for a real
student**, and **the fix**. Then one final entry: **what I was unsure about**, naming something
specific. That entry is scored, and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** run the sample. Then run a lab that is 2 days late and check it by hand.
- **Next 10:** build a test table from Part A. One row for **every band** of the schedule, one row
  at each band's boundary, one quiz row, one project row, and one row for a type that is not on the
  list. Write the correct answer for every row **before** you run anything.
- **Next 15:** run your table. Every disagreement is a defect.
- **Rest:** read each comment against its code. Then read the penalty chain top to bottom and ask,
  for each branch, which values can actually reach it.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start.

**Four of five is a strong score.**
