# Gate 2: Adversarial Review · Week 13
## 145060 Programming · Unit 6 · Week 13, Thursday · Independent

**40 minutes.** Individual and silent. **Nobody will be available to explain anything.** Everything you
need is in this packet. You may and should run the code. You may not ask a model whether it is correct,
because the model is what is being reviewed. You may not work with your team.

**Files:** `07-gate2-adversarial/gate2-w13-files/fundraiser_report.py` and `sales.csv`. The code and a real
run are also printed below, so you can do this on paper if the machines are down.

---

## Before you run anything

**Make a copy of the data file first.** In the `gate2-w13-files` folder, copy `sales.csv` to a new file named
`sales_backup.csv`. You can do this in VS Code's file explorer with copy and paste, then rename.

**Why:** this program writes a file whose name you type. When you test a program that writes files, you keep a
backup of every file it could touch. That is a habit, not a hint. If anything happens to `sales.csv` while you
test, copy the backup over it and keep going. Write down exactly what happened, because that is a finding.

---

## What you are looking at

A club advisor asked an AI assistant for the program in Part B, using the requirements in Part A. It runs. It
prints a tidy table. The comments are confident.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what the requirements say |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name, comment, or docstring that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the requirements asked for that is missing, or something nobody asked for |

**One of these is the kind of bug this whole course has warned you about: it does not crash, and the numbers look
reasonable.** Check at least one team's total by hand against `sales.csv`.

---

## PART A: The requirements

> Write `fundraiser_report.py` for the winter cookie dough fundraiser.
>
> 1. Read every sale from `sales.csv`, which has the columns `team`, `item`, `qty`, and `unit_price`.
> 2. For each team, total the dollars sold: `qty` times `unit_price`, added up over that team's rows.
> 3. Print the standings, highest total first, with each team's total and its share of all sales as a percent.
> 4. Skip any row whose `qty` or `unit_price` is missing or not a number, and print how many rows were skipped.
> 5. Ask for a file name and save the standings to that file as JSON, so the activities office can post them.

---

## PART B: What the AI produced

Count line numbers from `# fundraiser_report.py` as line 1. Blank lines count.

```python
# fundraiser_report.py
#
# Leaderboard for the winter cookie dough fundraiser. Reads every sale from
# sales.csv, totals each team, prints the standings, and saves them as JSON
# so the activities office can post them.
#
# Usage:  python fundraiser_report.py

import csv
import json

SALES_FILE = "sales.csv"
PROJECTION_FACTOR = 1.35   # typical late-season lift for school fundraisers


def read_sales(path):
    """Read sales.csv and return (valid_rows, skipped_count)."""
    rows = []
    skipped = 0
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                quantity = int(row.get("quantity", 1))
                price = float(row["unit_price"])
            except (ValueError, TypeError):
                skipped += 1
                continue
            rows.append({"team": row["team"].strip(), "quantity": quantity, "price": price})
    return rows, skipped


def average_by_team(rows):
    """Group the sales by team."""
    totals = {}
    for row in rows:
        amount = row["quantity"] * row["price"]
        totals[row["team"]] = totals.get(row["team"], 0) + amount
    return totals


def total_of(entry):
    """Sort helper: the dollar total of one leaderboard entry."""
    return entry["total"]


def build_leaderboard(rows):
    """Return the standings, highest total first, with each team's share of all sales."""
    totals = average_by_team(rows)
    board = []
    for team in totals:
        grand_total = 0
        for row in rows:
            grand_total += row["quantity"] * row["price"]
        share = round(totals[team] / grand_total * 100, 1)
        board.append({
            "team": team,
            "total": round(totals[team], 2),
            "share": share,
            "projected": round(totals[team] * PROJECTION_FACTOR, 2),
        })
    board.sort(key=total_of, reverse=True)
    return board


def print_leaderboard(board, skipped):
    """Print the standings as a table the office can read aloud."""
    print("COOKIE DOUGH FUNDRAISER STANDINGS")
    print(f"{'Team':<16}{'Total':>10}{'Share':>8}{'Projected':>12}")
    for entry in board:
        print(f"{entry['team']:<16}{entry['total']:>10.2f}{entry['share']:>7.1f}%{entry['projected']:>12.2f}")
    print(f"Skipped {skipped} rows.")


def save_leaderboard(board, filename):
    """Save the standings as JSON for the activities office."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(board, file, indent=2)
    print(f"Saved standings to {filename}")


def main():
    """Read, total, print, and save."""
    rows, skipped = read_sales(SALES_FILE)
    board = build_leaderboard(rows)
    print_leaderboard(board, skipped)
    filename = input("Save standings as (for example standings.json): ").strip()
    save_leaderboard(board, filename)


if __name__ == "__main__":
    main()
```

### The data, `sales.csv`

```
team,item,qty,unit_price
Robotics,chocolate chip tub,4,12.00
Robotics,sugar cookie tub,2,12.00
Band,chocolate chip tub,6,12.00
Band,snickerdoodle tub,3,13.50
Culinary Club,sugar cookie tub,5,12.00
Robotics,snickerdoodle tub,1,13.50
Culinary Club,chocolate chip tub,ten,12.00
Band,sugar cookie tub,2,12.00
Culinary Club,snickerdoodle tub,4,
Esports,chocolate chip tub,3,12.00
```

### A real run, typing `standings.json` at the prompt

```
COOKIE DOUGH FUNDRAISER STANDINGS
Team                 Total   Share   Projected
Robotics             37.50   33.8%       50.62
Band                 37.50   33.8%       50.62
Culinary Club        24.00   21.6%       32.40
Esports              12.00   10.8%       16.20
Skipped 1 rows.
Save standings as (for example standings.json): Saved standings to standings.json
```

**Before you read the code, compute Robotics' total yourself from the three Robotics rows in `sales.csv`.** Then
count the rows that should be skipped under requirement 4.

---

## What to submit

**On paper,** in the packet's answer space, **or typed,** in a file named `gate2_w14_<your first name>.md` saved in
your own repository and pushed. Your substitute collects paper copies at minute 40.

For each defect: **file and line**, **dimension**, **what goes wrong for a real person**, and **the fix**. Then one
final entry: **what I was unsure about**, naming something specific. That entry is scored, and a blank costs more
than a wrong guess.

### How to spend 40 minutes

- **First 5:** make the backup. Run it with `standings.json`. Compute one team's total by hand and compare.
- **Next 10:** run it again and type file names nobody should type. Think about which files are in that folder.
  **Restore from your backup if anything goes wrong.**
- **Next 10:** read Part A one requirement at a time and point at the line that does it. Then look for anything the
  program prints or saves that Part A never mentions.
- **Rest:** read every name, comment, and docstring against the code under it. Then look inside
  `build_leaderboard` and count how many times the rows are added up.

### Answer space

| # | Line(s) | Dimension | What goes wrong for a real person | Fix |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**What I was unsure about:**

<br>
<br>

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **Missing the security defect costs two points,
not one**, because a review that misses a threat to the data has missed what reviews are for.

**Four of five is a strong score.**
