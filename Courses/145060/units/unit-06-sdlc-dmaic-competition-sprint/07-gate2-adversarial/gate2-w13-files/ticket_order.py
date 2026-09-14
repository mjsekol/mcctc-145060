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
