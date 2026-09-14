# Gate 2: Adversarial Review · Week 4
## 145060 Programming · Unit 1 · Friday, October 2

**35 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

---

## What you are looking at

Somebody gave an AI assistant the requirements in Part A and got the program in Part B.
It runs, the output is lined up, and it looks finished.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It reads, exposes, or trusts something it should not |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

**The three repeated blocks are not a defect.** You do not have loops yet. Do not spend a
finding on them.

---

## PART A: The requirements

> Write `member_report.py` for the club board.
>
> 1. Read the club roster from **`roster.txt`**. Fixed width: name in positions 0-19,
>    member code in positions 20-32. Codes look like `ROBO-2026-114`.
> 2. For each of the three members, print their name, their **season year**, and their
>    **member number**, lined up in columns.
> 3. At the end, print how many **members** are in the roster.

The roster file:

```
Ava Ruiz            ROBO-2026-114
Marcus Delgado      BAND-2027-009
Priya Patel         ROBO-2026-207
```

---

## PART B: What the AI produced

Count line numbers from `# member_report.py` as line 1. Blank lines count.

```python
# member_report.py
#
# Prints a formatted member report from the club roster file.
# The roster is fixed width: name in positions 0-19, code in positions 20-32.
# Codes look like ROBO-2026-114.

print("MEMBER REPORT")
print("=============")

roster_name = input("Roster file to report on: ")

# Count the members in the roster.
roster_file = open(roster_name)
contents = roster_file.read()
roster_file.close()
member_count = len(contents)

roster_file = open(roster_name)

line = roster_file.readline()
name = line[0:20].strip()
number = line[30:32]
print(f"{name:<18} member #{number}")

line = roster_file.readline()
name = line[0:20].strip()
number = line[30:32]
print(f"{name:<18} member #{number}")

line = roster_file.readline()
name = line[0:20].strip()
number = line[30:32]
print(f"{name:<18} member #{number}")

roster_file.close()

print("-------------")
print(f"Members: {member_count}")
```

### A real run

Typing `roster.txt` at the prompt:

```
MEMBER REPORT
=============
Roster file to report on: Ava Ruiz           member #11
Marcus Delgado     member #00
Priya Patel        member #20
-------------
Members: 102
```

**Compare every line of that output to the roster file and to Part A before you read
the code.** At least two defects are visible without reading a single line of Python.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**,
and **the fix**. Then one final entry: **what I was unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 5:** run it with `roster.txt`. Check each output value against the file.
- **Next 10:** run it again and type something other than `roster.txt` at the prompt.
  Think about what files exist on a shared lab machine.
- **Next 10:** read Part A one requirement at a time and point at the line that satisfies
  it.
- **Rest:** read each comment and variable name against what the code actually does.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states
the security weighting before you start. **Four of five is a strong score.**
