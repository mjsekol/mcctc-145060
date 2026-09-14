# concessions.py
#
# Order totals for the Boosters concession stand at home basketball games.
# Written by last year's team. You did not write this, and you are not
# allowed to change it today. Your job is to test it against the spec.
#
# Spec: see Lab U06-01, "The stakeholder's acceptance criteria".

PRICES = {
    "hot dog": 3.00,
    "nachos": 4.00,
    "pretzel": 3.50,
    "water": 1.50,
    "sports drink": 2.50,
    "candy": 2.00,
}

DRINKS = ["water", "sports drink"]
COMBO_SAVINGS = 0.50
MEMBER_DISCOUNT = 0.10
MAX_PER_ITEM = 20


def line_total(item, quantity):
    """Return the price for one line of an order, such as 3 pretzels.

    Raises ValueError for an item the stand does not sell, or a quantity
    outside 1 to 20. Bigger orders go through the Boosters office.
    """
    if item not in PRICES:
        raise ValueError(f"we do not sell {item}")
    if quantity < 1 or quantity >= MAX_PER_ITEM:
        raise ValueError(f"quantity must be 1 to {MAX_PER_ITEM}")
    return PRICES[item] * quantity


def combo_count(order):
    """Return how many hot dog and drink combos are in the order.

    Every hot dog paired with any drink is one combo.
    """
    hot_dogs = order.get("hot dog", 0)
    drinks = order.get("water", 0)
    return min(hot_dogs, drinks)


def order_total(order, is_member):
    """Return the total for a whole order, rounded to cents.

    order is a dictionary from item name to quantity.
    Combo savings come off first. The member discount applies to what is left.
    """
    subtotal = 0
    for item in order:
        subtotal = subtotal + line_total(item, order[item])

    if is_member:
        subtotal = subtotal * (1 - MEMBER_DISCOUNT)

    total = subtotal - combo_count(order) * COMBO_SAVINGS
    return round(total, 2)


if __name__ == "__main__":
    sample = {"hot dog": 2, "water": 2}
    print("Sample order:", sample)
    print("Non-member total:", order_total(sample, False))
    print("Member total:", order_total(sample, True))
