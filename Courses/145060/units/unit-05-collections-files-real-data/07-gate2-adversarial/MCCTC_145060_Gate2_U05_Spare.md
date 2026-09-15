# Gate 2: Adversarial Review · Unit 5 Spare
## 145060 Programming · Unit 5 · Spare Gate 2 for any extra day · One build block

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether
it is correct, because the model is what is being reviewed.

This spare Gate 2 uses the whole unit: CSV, cleaning, dictionaries, sets, calculated fields,
JSON, and files and folders.

The program is `gate2-u05-spare-files/resale_report.py`, with two sheets in
`gate2-u05-spare-files/sheets/`. **Copy the whole `gate2-u05-spare-files` folder somewhere in your own
workspace before you run it**, because it creates a `reports` folder next to itself, and you
may want to add test sheets.

---

## What you are looking at

A group of friends who resell sneakers asked an AI assistant for a profit report and got the
program in Part B. It reads every sheet in a folder, cleans dollar signs, skips duplicates,
calculates profit and margin, and writes a JSON report per friend. It runs, and the reports
look professional.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It reads, exposes, or trusts something it should not |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be, or the wrong structure for the job |
| **Requirements Fit** | Something the spec asked for that is missing, or something nobody asked for |

---

## PART A: The requirements

> Write `resale_report.py` for our sneaker resale group.
>
> 1. Every friend keeps a sheet in the `sheets` folder, one CSV per friend, with the columns
>    Shoe, Size, Paid, Sold For, Platform, Seller. Process every `.csv` file in that folder.
> 2. Money may be typed with or without a dollar sign. A blank Sold For means the pair has not
>    sold yet.
> 3. The same pair typed twice, with every column identical, counts once.
> 4. For each sold pair, calculate profit (Sold For minus Paid) and margin (profit as a percent
>    of what was **paid**).
> 5. For each friend, write a JSON report into the `reports` folder, named after the seller:
>    pairs sold, total profit, average margin, profit by platform, and the pairs still unsold.
> 6. A row that cannot be read, for example a price that is not a number, must be **listed in
>    that friend's report with its line number**, not dropped.
> 7. Sheets are shared from friends' own drives, so **treat everything inside a sheet as
>    untrusted**.
> 8. Sheets can grow to thousands of rows, so the duplicate check must stay fast.

---

## PART B: What the AI produced

Count line numbers from `# resale_report.py` as line 1. Blank lines count.

```python
# resale_report.py
#
# Builds a profit report for every friend in the sneaker resale group.
# Reads each friend's sheet from the sheets folder and writes one JSON
# report per seller into the reports folder.

import csv
import json
import os

SHEETS_FOLDER = "sheets"
REPORT_FOLDER = "reports"


def parse_money(text):
    """Turn '$145' or '145.00' into 145.0. Raises ValueError if it is not money."""
    return float(text.strip().lstrip("$"))


def read_sheet(path):
    """Read one friend's sheet. Return a list of clean rows, duplicates removed."""
    rows = []
    seen = []
    with open(path, newline="", encoding="utf-8") as sheet:
        for raw in csv.DictReader(sheet):
            key = ",".join(raw.values())
            if key in seen:
                continue
            seen.append(key)
            try:
                paid = parse_money(raw["Paid"])
                sold_for = None
                if raw["Sold For"].strip() != "":
                    sold_for = parse_money(raw["Sold For"])
            except ValueError:
                continue
            rows.append({
                "shoe": raw["Shoe"].strip(),
                "size": raw["Size"].strip(),
                "paid": paid,
                "sold_for": sold_for,
                "platform": raw["Platform"].strip().lower(),
                "seller": raw["Seller"].strip(),
            })
    return rows


def add_profit(row):
    """Add profit and margin to a sold pair."""
    row["profit"] = row["sold_for"] - row["paid"]
    # Margin is the profit as a percent of the sale price.
    row["margin_pct"] = row["profit"] / row["paid"] * 100


def profit_by_platform(sold_rows, totals={}):
    """Return a dictionary of platform name to total profit."""
    for row in sold_rows:
        if row["platform"] not in totals:
            totals[row["platform"]] = 0.0
        totals[row["platform"]] += row["profit"]
    return totals


def build_report(rows):
    sold = []
    unsold = []
    for row in rows:
        if row["sold_for"] is None:
            unsold.append(f"{row['shoe']} (size {row['size']})")
        else:
            add_profit(row)
            sold.append(row)
    total_profit = 0.0
    margin_total = 0.0
    for row in sold:
        total_profit += row["profit"]
        margin_total += row["margin_pct"]
    average_margin = None
    if sold:
        average_margin = round(margin_total / len(sold), 1)
    return {
        "pairs_sold": len(sold),
        "total_profit": round(total_profit, 2),
        "average_margin_pct": average_margin,
        "profit_by_platform": profit_by_platform(sold),
        "still_unsold": unsold,
    }


def main():
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    for filename in sorted(os.listdir(SHEETS_FOLDER)):
        if not filename.endswith(".csv"):
            continue
        rows = read_sheet(os.path.join(SHEETS_FOLDER, filename))
        if not rows:
            continue
        report = build_report(rows)
        seller = rows[0]["seller"]
        report_path = os.path.join(REPORT_FOLDER, seller + ".json")
        with open(report_path, "w", encoding="utf-8") as out:
            json.dump(report, out, indent=2)
        print(f"{seller}: {report['pairs_sold']} sold, ${report['total_profit']:.2f} profit -> {report_path}")


main()
```

### The two sheets

`sheets/maya.csv`:

```
Shoe,Size,Paid,Sold For,Platform,Seller
Court Classic Low,10,$110,$145,LaceSwap,maya
Trail Runner X,9.5,$85,$92,local pickup,maya
Retro High 89,11,$160,,LaceSwap,maya
Cloud Step 2,8,$70,$64,StockBox,maya
Court Classic Low,10,$110,$145,LaceSwap,maya
Skyline Mid,10.5,$125,$180,StockBox,maya
```

`sheets/theo.csv`:

```
Shoe,Size,Paid,Sold For,Platform,Seller
Retro High 89,9,$150,$210,StockBox,theo
Harbor Slide,11,$40,$55,local pickup,theo
Trail Runner X,10,$85,ninety,LaceSwap,theo
Skyline Mid,12,$125,,StockBox,theo
```

The shoe models and platforms are invented.

### A real run

```
maya: 4 sold, $91.00 profit -> reports\maya.json
theo: 2 sold, $75.00 profit -> reports\theo.json
```

`reports/maya.json`:

```
{
  "pairs_sold": 4,
  "total_profit": 91.0,
  "average_margin_pct": 18.9,
  "profit_by_platform": {
    "laceswap": 35.0,
    "local pickup": 7.0,
    "stockbox": 49.0
  },
  "still_unsold": [
    "Retro High 89 (size 11)"
  ]
}
```

`reports/theo.json`:

```
{
  "pairs_sold": 2,
  "total_profit": 75.0,
  "average_margin_pct": 38.8,
  "profit_by_platform": {
    "laceswap": 35.0,
    "local pickup": 22.0,
    "stockbox": 109.0
  },
  "still_unsold": [
    "Skyline Mid (size 12)"
  ]
}
```

**Before you read any code, work out Theo's report by hand from his sheet.** Four rows. Compare
every number and every row to his JSON.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**, and **the
fix**. Then one final entry: **what I was unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 10:** calculate Maya's and Theo's reports by hand and compare them to the JSON. Every
  number, and every row accounted for.
- **Next 10:** requirement 7 says the sheets are untrusted. Make a third sheet for a friend and
  think about what each column could contain. Look closely at how the report's file name is built.
- **Next 5:** read Part A one requirement at a time and point at the line that satisfies it.
- **Rest:** read every comment against the line under it, and think about requirement 8 with a
  sheet of five thousand rows.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start. **Four of five is a strong score.**
