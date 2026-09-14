# Gate 2: Adversarial Review · Week 13
## 145060 Programming · Unit 6 · Friday, December 4

**40 minutes.** Individual. You may and should run the code. You may not ask a model whether it is
correct, because the model is what is being reviewed.

**Files:** `07-gate2-adversarial/gate2-w13-files/ticket_order.py` and `prices.json`. Keep both in the
same folder and run from that folder.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got the program in Part B. It runs. It
even comes with its own acceptance tests, and **every one of them passes.**

That last sentence is the point of this week. Yesterday you learned that a test is only as good as the
place its expected value came from.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what the requirements say |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name, comment, or docstring that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the requirements asked for that is missing, or something nobody asked for |

**One of these defects hides behind a passing test.** Do the arithmetic for every expected value yourself,
from Part A, before you trust any PASS line.

---

## PART A: The requirements

> Write `ticket_order.py` for the winter concert ticket table.
>
> 1. Student tickets cost $6 and adult tickets cost $10. Prices live in `prices.json`, so the office can
>    change a price without editing code.
> 2. One order is 1 to 8 tickets in total. Any other order is refused with a clear message.
> 3. An order of **6 or more** tickets gets $1 off every ticket in the order.
> 4. `order_total(students, adults)` returns the order's total in whole dollars.
> 5. The file includes acceptance tests covering every requirement, **including both edges of the 1-to-8
>    rule and the edge of the group rate**, and prints how many passed and failed.

---

## PART B: What the AI produced

Count line numbers from `# ticket_order.py` as line 1. Blank lines count.

```python
# ticket_order.py
#
# Winter concert ticket pricing for the front table, with the acceptance
# tests built in so anyone can confirm the rules before the doors open.
#
# Run the tests:   python ticket_order.py

import json

PRICES_FILE = "prices.json"
MIN_TICKETS = 1
MAX_TICKETS = 8
GROUP_SIZE = 6          # orders of this many tickets or more get the group rate
GROUP_DISCOUNT = 1      # dollars off each ticket in a group order


def price_for(kind):
    """Look up the current price for one ticket type from prices.json.

    Reading the file here means the office can change a price without
    anyone editing the code.
    """
    with open(PRICES_FILE, encoding="utf-8") as file:
        prices = json.load(file)
    return prices[kind]


def order_total(students, adults):
    """Return the total for one order, in cents.

    Raises ValueError when the order is smaller or larger than the table
    is allowed to sell in one transaction.
    """
    ticket_count = students + adults
    if ticket_count < MIN_TICKETS or ticket_count > MAX_TICKETS:
        raise ValueError(f"orders must be {MIN_TICKETS} to {MAX_TICKETS} tickets")

    total = 0
    for _ in range(students):
        total += price_for("student")
    for _ in range(adults):
        total += price_for("adult")

    # Group rate: $1 off every ticket for groups of six or more.
    if ticket_count > GROUP_SIZE:
        total -= GROUP_DISCOUNT * ticket_count

    return total


def receipt_line(students, adults):
    """Build the one-line receipt the table reads back to the buyer."""
    total = order_total(students, adults)
    return f"{students} student, {adults} adult: ${total}"


# Acceptance tests. Each check compares the program to the spec.
results = []


def check(label, actual, expected):
    """Record and print one PASS or FAIL."""
    if actual == expected:
        results.append(True)
        print(f"PASS  {label}")
    else:
        results.append(False)
        print(f"FAIL  {label}: expected {expected}, got {actual}")


def run_acceptance_tests():
    """Run every acceptance test from the spec and print a summary."""
    check("one student ticket", order_total(1, 0), 6)
    check("one adult ticket", order_total(0, 1), 10)
    check("mixed order of four", order_total(2, 2), 32)
    check("group of six adults", order_total(0, 6), 60)
    check("group of seven gets the group rate", order_total(3, 4), 51)

    try:
        order_total(0, 0)
        check("empty order is refused", "accepted", "refused")
    except ValueError:
        check("empty order is refused", "refused", "refused")

    check("receipt wording", receipt_line(2, 1), "2 student, 1 adult: $22")

    print()
    print(f"{results.count(True)} passed, {results.count(False)} failed")


if __name__ == "__main__":
    run_acceptance_tests()
```

`prices.json`:

```json
{
  "student": 6,
  "adult": 10
}
```

### A real run, for reference

```
$ python ticket_order.py
PASS  one student ticket
PASS  one adult ticket
PASS  mixed order of four
PASS  group of six adults
PASS  group of seven gets the group rate
PASS  empty order is refused
PASS  receipt wording

7 passed, 0 failed
```

**Seven for seven.** Before you believe it, work out by hand what six adult tickets should cost under
requirement 3.

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real person**, and **the fix**.
Then one final entry: **what I was unsure about**, naming something specific. That entry is scored and a
blank costs more than a wrong guess.

You can test any single order without editing the file:

```
python -c "import ticket_order; print(ticket_order.order_total(1, 2))"
```

### How to spend 40 minutes

- **First 5:** run it. Then compute every expected value in `run_acceptance_tests` yourself from Part A.
- **Next 10:** call `order_total` with orders nobody would choose: 0 and 0, 8 tickets, 9 tickets, and
  counts that should never be possible at a ticket table.
- **Next 10:** read Part A one requirement at a time and point at the line that satisfies it. Requirement 5
  names specific edges. Find the check for each one.
- **Rest:** read every comment and docstring against the code underneath it, and count how many times the
  program reads `prices.json` for one order.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the security
weighting before you start.

**Four of five is a strong score.**
