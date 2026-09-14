# Gate 2: Adversarial Review · Week 7
## 145060 Programming · Unit 3 · Friday, October 23

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether
it is correct, because the model is what is being reviewed.

The files are in [`gate2-w07-files/`](gate2-w07-files/): `snack_tally.py` and `goal.txt`. Put them
in the same folder and run the program from that folder.

---

## What you are looking at

Somebody gave an AI assistant the requirements in Part A and got the program in Part B. It runs,
the messages are friendly, and the summary looks finished.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It trusts input it should not, and something bad follows |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

---

## PART A: The requirements

> Write `snack_tally.py` for the robotics club's concession stand at home football games.
>
> 1. Tonight's fundraising goal is stored in **`goal.txt`** as a whole number of dollars, so the
>    treasurer can change it without touching the code.
> 2. The volunteer types each sale as a whole number of dollars. Typing **`done`**, in any
>    capitalization, ends the shift.
> 3. A sale must be a whole number **from 1 to 50**. Anything else is refused with a message and
>    the volunteer is asked for the next sale. A refused entry is never counted. **Nothing the
>    volunteer types may crash the program**, because a crash loses the whole night's tally.
> 4. At the end, print the number of sales, the total collected, and the **biggest single sale**.
> 5. Print one line for **each $50 milestone the total reached**, for example `Reached $50`.
> 6. Say whether the goal was met.

`goal.txt` contains:

```
150
```

---

## PART B: What the AI produced

Count line numbers from `# snack_tally.py` as line 1. Blank lines count.

```python
# snack_tally.py
#
# Concession stand tally for the robotics club.
# The volunteer enters each sale in whole dollars. Typing "done" ends the shift.
# Sales must be between $1 and $100. Anything else is refused and not counted.
# At the end, the program prints a shift summary, the milestones reached,
# and whether the club hit tonight's fundraising goal from goal.txt.

GOAL_FILE = "goal.txt"
MIN_SALE = 1
MAX_SALE = 50
MILESTONE_STEP = 50

print("SNACK BAR TALLY")
print("===============")
print('Enter each sale in whole dollars. Type "done" to close out the shift.')
print()

sale_count = 0
total = 0
biggest_sale = 0

while True:
    entry = input("Sale amount: ").strip().lower()

    if entry == "done":
        break

    sale = int(entry)

    # Refuse anything outside the allowed range without counting it.
    if sale < MIN_SALE or sale > MAX_SALE:
        print(f"  Refused. Sales must be from ${MIN_SALE} to ${MAX_SALE}.")
        continue

    # Load tonight's goal so the running status stays accurate.
    goal_file = open(GOAL_FILE)
    goal = int(goal_file.read())
    goal_file.close()

    sale_count = sale_count + 1
    total = total + sale
    if sale > biggest_sale:
        biggest_sale = sale

    print(f"  Recorded ${sale}. Running total: ${total} of ${goal}.")

print()
print("SHIFT SUMMARY")
print("-------------")
print(f"Sales recorded: {sale_count}")
print(f"Total collected: ${total}")

# Celebrate every $50 milestone the stand passed tonight.
for milestone in range(MILESTONE_STEP, total, MILESTONE_STEP):
    print(f"Reached ${milestone}")

goal_file = open(GOAL_FILE)
goal = int(goal_file.read())
goal_file.close()

if total >= goal:
    print(f"Goal of ${goal} met. Nice work.")
else:
    print(f"${goal - total} short of the ${goal} goal.")
```

### A real run

Typing `12`, `8`, `35`, `60`, `20`, `40`, `22`, `done`:

```
SNACK BAR TALLY
===============
Enter each sale in whole dollars. Type "done" to close out the shift.

Sale amount: 12
  Recorded $12. Running total: $12 of $150.
Sale amount: 8
  Recorded $8. Running total: $20 of $150.
Sale amount: 35
  Recorded $35. Running total: $55 of $150.
Sale amount: 60
  Refused. Sales must be from $1 to $50.
Sale amount: 20
  Recorded $20. Running total: $75 of $150.
Sale amount: 40
  Recorded $40. Running total: $115 of $150.
Sale amount: 22
  Recorded $22. Running total: $137 of $150.
Sale amount: done

SHIFT SUMMARY
-------------
Sales recorded: 6
Total collected: $137
Reached $50
Reached $100
$13 short of the $150 goal.
```

**Compare that summary with Part A, one requirement at a time, before you read the code.** One defect is
visible without reading a single line of Python.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person at the concession
stand**, **the command or input that shows it**, and **the fix**. Then one final entry: **what I was
unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 5:** run it with the inputs above. Check every summary line against Part A.
- **Next 10:** try to break it. Think about what a tired volunteer really types at 9pm: prices with cents,
  a typo, a sale that lands a total on an exact milestone. Requirement 3 says nothing may crash it.
- **Next 10:** read Part A one requirement at a time and point at the line that satisfies it.
- **Rest:** read every comment against the line below it, and ask how many times each line runs during a
  shift of 200 sales.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the security
weighting before you start. **Four of five is a strong score.**
