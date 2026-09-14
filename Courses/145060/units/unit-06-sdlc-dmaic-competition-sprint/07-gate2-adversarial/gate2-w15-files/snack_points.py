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
