# Gate 2: Adversarial Review · Week 3
## 145060 Programming · Unit 1 · Week 3, Friday

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got the program in
Part B. It runs. It is formatted well and the comments sound sure of themselves.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

**One of these is visible in the normal output and almost nobody notices it**, because
it looks like a plausible value. Read the sample run against the spec before you read
the code.

---

## PART A: The requirements

> Write `roster_entry.py` that builds a clean roster line for a club member.
>
> Club codes have the shape `CLUB-YEAR-NUMBER`, for example `ROBO-2026-114`.
>
> The program must:
>
> 1. Ask for the member's name as they type it, and clean it: no stray spaces at the
>    ends, and consistent capitalisation.
> 2. Ask for the club code.
> 3. Pull three things out of the code: the club letters, the **full four-digit
>    season year**, and the **member number**.
> 4. Print a boxed roster line showing the cleaned name, the club, the season year,
>    and the member number, each labelled.
> 5. Print a greeting using the member's **first name only**.

---

## PART B: What the AI produced

Count line numbers from `# roster_entry.py` as line 1. Blank lines count.

```python
# roster_entry.py
#
# Builds a clean roster line from a name a member typed and their club code.
# Codes have the shape CLUB-YEAR-NUMBER, for example ROBO-2026-114.

print("ROSTER ENTRY")
print("------------")

raw_name = input("Member name: ")
club_code = input("Club code (CLUB-YEAR-NUMBER): ")

# Pull the club letters off the front of the code.
club = club_code[0:4]

# The season year sits between the two dashes.
year = club_code[5:8]

# The member's first name, used for the greeting below.
first_name = raw_name.strip().title()

print()
print(f"| {raw_name.strip().title():<24} |")
print(f"| {'Club: ' + club:<24} |")
print(f"| {'Season: ' + year:<24} |")
print()
print(f"Welcome back, {first_name}.")
print(f"Roster line built for {raw_name.strip().title()}.")
```

### A real run, for reference

Typing `  ava RUIZ  ` and then `ROBO-2026-114`:

```
ROSTER ENTRY
------------
Member name:   ava RUIZ
Club code (CLUB-YEAR-NUMBER): ROBO-2026-114

| Ava Ruiz                 |
| Club: ROBO               |
| Season: 202              |

Welcome back, Ava Ruiz.
Roster line built for Ava Ruiz.
```

**Read those seven lines against the five requirements before you read the code.**
Two defects are sitting in that output in plain sight.

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real
person**, and **the fix**. Then one final entry: **what I was unsure about**, naming
something specific. That entry is scored and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** run it with the sample inputs. Compare every output line to the spec.
- **Next 10:** run it with inputs nobody would choose. An empty name. A code with a
  three-letter club. A code with no dashes.
- **Next 10:** read Part A one requirement at a time and point at the line that
  satisfies it. If you cannot point, you found one.
- **Rest:** read each comment against the code underneath it. Ask whether it is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor
states the security weighting before you start.

**Four of five is a strong score.**
