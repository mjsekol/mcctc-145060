# Gate 2: Adversarial Review · Week 14
## 145060 Programming · Unit 6 · Week 14, Tuesday · A change review

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether it is
correct, because the model is what is being reviewed.

**Files:** `07-gate2-adversarial/gate2-w14-files/`. Run everything from that folder. The programs read
`points.json` and `orders.csv` and write `points_after.json`, so running them repeatedly is safe.

---

## What you are looking at

This Gate 2 is different. You are not reviewing a whole program. You are reviewing **a change.**

The snack bar's loyalty points program, version 1.0, was accepted by the stakeholder and tagged as the
baseline. Then the stakeholder sent change request CR-2. Somebody gave an AI assistant the change request and
the baseline, and it produced version 1.1.

A change review asks two questions:

1. Did the change do what the change request asked?
2. **Did the change break, remove, or alter anything that was already accepted?**

**Five defects in version 1.1, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | Behavior that is now wrong, including behavior the change request never mentioned |
| **Security** | Input the program now accepts that it should refuse |
| **Readability** | A name, comment, or docstring that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the change request asked for that is missing |

**One defect is genuinely hard to see.** Most reviewers will look for it in the wrong place.

---

## PART A: The change request

> **CR-2 · Double points on home game days**
>
> On home game days, every purchase earns double points. Game days are listed in `game_days.txt`, one date per
> line. **Nothing else about how points are earned may change.** The receipt line must end with `DOUBLE POINTS`
> when an order earned double.

---

## PART B: The baseline, version 1.0 (accepted, do not review)

`snack_points_v1_0.py`. Read it so you know what was accepted.

```python
# snack_points_v1_0.py
#
# Snack bar loyalty points, version 1.0. This is the BASELINE: the version
# the stakeholder accepted and the team tagged. Do not review this file.
# Compare against it.
#
# Usage:  python snack_points_v1_0.py

import csv
import json

POINTS_FILE = "points.json"
ORDERS_FILE = "orders.csv"
AFTER_FILE = "points_after.json"


def points_for(total):
    """One point per whole dollar spent. $4.99 earns 4 points."""
    return int(total)


def read_orders(path):
    """Return (orders, skipped). A total must be a number above zero, or the order is skipped."""
    orders = []
    skipped = 0
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                total = float(row["total"])
            except ValueError:
                skipped += 1
                continue
            if total <= 0:
                skipped += 1
                continue
            orders.append({"date": row["date"].strip(), "card": row["card"].strip(), "total": total})
    return orders, skipped


def receipt(order, earned, balance):
    """One receipt line for the register screen."""
    return f"{order['date']}  {order['card']}  ${order['total']:>6.2f}  +{earned:<3} balance {balance}"


def main():
    """Apply one batch of orders to the points balances."""
    with open(POINTS_FILE, encoding="utf-8") as file:
        points = json.load(file)
    orders, skipped = read_orders(ORDERS_FILE)
    for order in orders:
        earned = points_for(order["total"])
        points[order["card"]] = points.get(order["card"], 0) + earned
        print(receipt(order, earned, points[order["card"]]))
    print(f"Skipped {skipped} orders.")
    with open(AFTER_FILE, "w", encoding="utf-8") as file:
        json.dump(points, file, indent=2)


if __name__ == "__main__":
    main()
```

---

## PART C: What the AI produced, version 1.1 (review this)

`snack_points.py`. Count line numbers from `# snack_points.py` as line 1. Blank lines count.

```python
# snack_points.py
#
# Snack bar loyalty points, version 1.1.
# Change request CR-2: double points on home game days.
#
# Usage:  python snack_points.py

import csv
import json

POINTS_FILE = "points.json"
ORDERS_FILE = "orders.csv"
AFTER_FILE = "points_after.json"
GAME_DAYS_FILE = "game_days.txt"

# Game-day orders earn triple points so the promotion stands out.
GAME_DAY_MULTIPLIER = 2


def points_for(total, multiplier=1):
    """Points for one order: one per dollar, times the day's multiplier."""
    return round(total) * multiplier


def is_game_day(date):
    """True when the date is listed in game_days.txt."""
    with open(GAME_DAYS_FILE, encoding="utf-8") as file:
        for line in file:
            if line.strip() == date:
                return True
    return False


def read_orders(path):
    """Return (orders, skipped). Orders with a total that is not a number are skipped."""
    orders = []
    skipped = 0
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                total = float(row["total"])
            except ValueError:
                skipped += 1
                continue
            orders.append({"date": row["date"].strip(), "card": row["card"].strip(), "total": total})
    return orders, skipped


def receipt(order, earned, balance):
    """One receipt line for the register screen."""
    return f"{order['date']}  {order['card']}  ${order['total']:>6.2f}  +{earned:<3} balance {balance}"


def main():
    """Apply one batch of orders to the points balances."""
    with open(POINTS_FILE, encoding="utf-8") as file:
        points = json.load(file)
    orders, skipped = read_orders(ORDERS_FILE)
    for order in orders:
        multiplier = 1
        if is_game_day(order["date"]):
            multiplier = GAME_DAY_MULTIPLIER
        earned = points_for(order["total"], multiplier)
        points[order["card"]] = points.get(order["card"], 0) + earned
        print(receipt(order, earned, points[order["card"]]))
    print(f"Skipped {skipped} orders.")
    with open(AFTER_FILE, "w", encoding="utf-8") as file:
        json.dump(points, file, indent=2)


if __name__ == "__main__":
    main()
```

### The data

`orders.csv`:

```
date,card,total
2026-12-14,C1001,4.99
2026-12-14,C1002,5.50
2026-12-14,C1003,12.00
2026-12-15,C1001,3.75
2026-12-15,C1004,-25.00
2026-12-16,C1002,4.50
2026-12-16,C1003,8.25
2026-12-17,C1001,6.49
2026-12-17,C1004,two dollars
```

`game_days.txt` lists `2026-12-16` and `2026-12-18`. `points.json` starts every card with a balance.

### Real runs, for reference

```
$ python snack_points_v1_0.py
2026-12-14  C1001  $  4.99  +4   balance 44
2026-12-14  C1002  $  5.50  +5   balance 17
2026-12-14  C1003  $ 12.00  +12  balance 87
2026-12-15  C1001  $  3.75  +3   balance 47
2026-12-16  C1002  $  4.50  +4   balance 21
2026-12-16  C1003  $  8.25  +8   balance 95
2026-12-17  C1001  $  6.49  +6   balance 53
Skipped 2 orders.

$ python snack_points.py
2026-12-14  C1001  $  4.99  +5   balance 45
2026-12-14  C1002  $  5.50  +6   balance 18
2026-12-14  C1003  $ 12.00  +12  balance 87
2026-12-15  C1001  $  3.75  +4   balance 49
2026-12-15  C1004  $-25.00  +-25 balance -5
2026-12-16  C1002  $  4.50  +8   balance 26
2026-12-16  C1003  $  8.25  +16  balance 103
2026-12-17  C1001  $  6.49  +6   balance 55
Skipped 1 orders.
```

**Compare the two runs line by line before you read the new code.**

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real person**, and **the fix**. Then:
**what I was unsure about**, naming something specific. That entry is scored.

You can test one function without editing anything:

```
python -c "import snack_points as new; print(new.points_for(4.99))"
python -c "import snack_points_v1_0 as old; print(old.points_for(4.99))"
```

### How to spend 35 minutes

- **First 5:** run both versions. Put the outputs side by side and mark every line that differs.
- **Next 10:** for every difference, ask whether CR-2 asked for it. Then ask what version 1.1 **removed** from
  version 1.0, not only what it added.
- **Next 10:** read CR-2 one sentence at a time and point at the line that satisfies it.
- **Rest:** read every comment against the code under it, and count how many times `game_days.txt` is opened in one
  run.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **Missing the security defect costs two points.**

**Four of five is a strong score.**
