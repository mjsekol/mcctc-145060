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
