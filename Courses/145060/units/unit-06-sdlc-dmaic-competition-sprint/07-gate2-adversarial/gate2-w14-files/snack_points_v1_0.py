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
