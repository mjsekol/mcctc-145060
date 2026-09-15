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
