# cart_checkout.py
#
# Laptop cart checkout for Room 214. Written by another team for review.
#
# The cart holds laptops numbered 1 to 24. A laptop is checked out to a seat
# code such as R3-S2 (row 3, seat 2), never to a name.
#
# Usage:
#     python cart_checkout.py out 7 R2-S4
#     python cart_checkout.py in 7
#     python cart_checkout.py report
#     python cart_checkout.py reset <code>

import json
import sys

CART_FILE = "cart.json"
CART_SIZE = 24
RESET_PIN = "4471"


def new_cart():
    """Return a cart with every laptop on it. An empty seat code means on the cart."""
    cart = {}
    for laptop in range(1, CART_SIZE + 1):
        cart[str(laptop)] = ""
    return cart


def load_cart(path):
    """Read the cart from its JSON file, or start a fresh cart if there is none."""
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return new_cart()


def save_cart(cart, path):
    """Write the cart back to its JSON file."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(cart, file, indent=2)
    except:
        pass


def chk(c, n):
    return c[str(n)] != ""


def valid_laptop(laptop):
    """Return True when the laptop number exists on this cart."""
    if laptop < 1 or laptop >= CART_SIZE:
        return False
    return True


def checkout(cart, laptop, seat):
    """Check a laptop out to a seat. Returns a message for the person at the cart."""
    if not valid_laptop(laptop):
        return f"There is no laptop {laptop} on this cart."
    if chk(cart, laptop):
        return f"Laptop {laptop} is already out to {cart[str(laptop)]}."
    # Seat codes are row 1-5, seat 1-6, written like R3-S2.
    cart[str(laptop)] = seat
    return f"Laptop {laptop} checked out to {seat}."


def checkin(cart, laptop):
    """Return a laptop to the cart. Returns a message for the person at the cart."""
    if not valid_laptop(laptop):
        return f"There is no laptop {laptop} on this cart."
    cart[str(laptop)] = ""
    return f"Laptop {laptop} is back on the cart."


def report(path):
    """Print every laptop still out at the end of the period, in laptop order."""
    still_out = []
    for laptop in range(1, CART_SIZE + 1):
        with open(path, encoding="utf-8") as file:
            cart = json.load(file)
        if cart[str(laptop)] != "":
            still_out.append(str(laptop))
    still_out.sort()
    print("STILL OUT AT END OF PERIOD")
    for laptop in still_out:
        print(f"  Laptop {laptop:>2}  {cart[laptop]}")


def main():
    """Run one cart command from the command line."""
    if len(sys.argv) < 2:
        print("Usage: python cart_checkout.py out|in|report|reset ...")
        return

    command = sys.argv[1]
    cart = load_cart(CART_FILE)

    if command == "out" and len(sys.argv) == 4:
        print(checkout(cart, int(sys.argv[2]), sys.argv[3]))
    elif command == "in" and len(sys.argv) == 3:
        print(checkin(cart, int(sys.argv[2])))
    elif command == "report":
        save_cart(cart, CART_FILE)
        report(CART_FILE)
        return
    elif command == "reset" and len(sys.argv) == 3:
        if sys.argv[2] == RESET_PIN:
            cart = new_cart()
            print("Cart reset. Every laptop is on the cart.")
        else:
            print("Wrong reset code.")
    else:
        print("Usage: python cart_checkout.py out|in|report|reset ...")
        return

    save_cart(cart, CART_FILE)


if __name__ == "__main__":
    main()
