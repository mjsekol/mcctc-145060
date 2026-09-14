# Gate 2: Adversarial Review · Week 5
## 145060 Programming · Unit 2 · Thursday, October 8 · Build 2

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

---

## What you are looking at

A volunteer coordinator handed an AI assistant the requirements in Part A and got the
validation program in Part B. It runs. It uses named constants, a flat `elif` chain,
and comments that sound sure of themselves. It looks like the flattened code you learned
about this morning.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It gives the wrong answer for some input |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing or different |

**One of these defects sits exactly on a boundary.** The sample run does not touch it. You
will only find it by choosing inputs the author did not.

---

## PART A: The requirements

> Write `volunteer_check.py` to validate one application for the Riverside 5K Teen
> Volunteer Crew.
>
> 1. Ask for the applicant's first name, age, t-shirt size, hours available on race
>    weekend, and whether a guardian consent form is signed (y/n).
> 2. The first name must not be empty.
> 3. Volunteers must be **14 through 18 years old, inclusive.**
> 4. Volunteers **under 16** must have a signed guardian consent form.
> 5. The t-shirt size must be S, M, L, or XL, typed in any capitalization.
> 6. Hours available must be from 2 through 12.
> 7. Print **every** problem with the application, one per line, in the order of this list.
> 8. Finish with `APPROVED` and a summary line, or `NOT APPROVED` and the number of problems.

---

## PART B: What the AI produced

Count line numbers from `# volunteer_check.py` as line 1. Blank lines count.

```python
# volunteer_check.py
#
# Validates one application for the Riverside 5K Teen Volunteer Crew.
# Applies the coordinator's rules in order and prints a clear decision,
# so no ineligible volunteer is ever placed on a race-day shift.

print("RIVERSIDE 5K TEEN VOLUNTEER CREW")
print("Application check")
print("-" * 32)

# Collect everything up front so each check below can use it.
first_name = input("First name: ").strip()
age = int(input("Age: "))
shirt_size = input("T-shirt size (S, M, L, XL): ")
hours = int(input("Hours available on race weekend: "))
consent_answer = input("Guardian consent form signed? (y/n): ").strip().lower()

# Coordinator rules, kept in one place so they are easy to update.
MIN_AGE = 14
MAX_AGE = 18
CONSENT_AGE = 16
MIN_HOURS = 2
MAX_HOURS = 12

# Consent is recorded unless the applicant answered no.
has_consent = consent_answer != "n"

# Tracks whether the application has passed every check so far.
is_eligible = 0

# Check each rule in order and report the problem clearly.
if first_name == "":
    print("Problem: first name is required.")
    is_eligible = is_eligible + 1
elif age < MIN_AGE or age >= MAX_AGE:
    print(f"Problem: volunteers must be {MIN_AGE} to {MAX_AGE} years old.")
    is_eligible = is_eligible + 1
elif age < CONSENT_AGE and not has_consent:
    print(f"Problem: volunteers under {CONSENT_AGE} need a signed consent form.")
    is_eligible = is_eligible + 1
elif shirt_size.strip().upper() != "S" and shirt_size.strip().upper() != "M" and shirt_size.strip().upper() != "L" and shirt_size.strip().upper() != "XL":
    print("Problem: t-shirt size must be S, M, L, or XL.")
    is_eligible = is_eligible + 1
elif hours < MIN_HOURS or hours > MAX_HOURS:
    print(f"Problem: volunteers must be available {MIN_HOURS} to {MAX_HOURS} hours.")
    is_eligible = is_eligible + 1

print("-" * 32)
if is_eligible == 0:
    print(f"APPROVED: {first_name}, age {age}, shirt {shirt_size.strip().upper()}, {hours} hours")
else:
    print(f"NOT APPROVED ({is_eligible} problem found)")
```

### A real run, for reference

Typing `Maya`, `15`, `m`, `6`, `y`:

```
RIVERSIDE 5K TEEN VOLUNTEER CREW
Application check
--------------------------------
First name: Maya
Age: 15
T-shirt size (S, M, L, XL): m
Hours available on race weekend: 6
Guardian consent form signed? (y/n): y
--------------------------------
APPROVED: Maya, age 15, shirt M, 6 hours
```

**That output is correct for those inputs.** Every defect is somewhere this run did not go.

---

## What to submit

For each defect: **line number**, **dimension**, **the exact inputs you typed to prove it**,
**what goes wrong for a real person**, and **the fix**. Then one final entry: **what I was
unsure about**, naming something specific. That entry is scored, and a blank costs more than
a wrong guess.

### How to spend 40 minutes

- **First 5:** run it with the sample inputs. Confirm it approves Maya.
- **Next 10:** build a test table from Part A before you read the code closely. For every
  rule with a number in it, write the boundary value and the value one past it. For every
  yes-or-no rule, write an answer that is not `y` or `n`.
- **Next 15:** run your table. Every row where the program disagrees with Part A is a defect.
- **Rest:** read each comment against the code underneath it, and each variable name against
  what it holds. Then read requirement 7 one more time, slowly.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start.

**Four of five is a strong score.** A finding only counts with the inputs that prove it.
