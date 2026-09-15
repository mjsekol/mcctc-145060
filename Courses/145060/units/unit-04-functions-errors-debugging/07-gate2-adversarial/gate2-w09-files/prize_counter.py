# prize_counter.py
#
# Prize counter kiosk for the arcade. A player enters the tickets on their
# card, then trades them for prizes from the wall until they type done.
#
# prizes.txt is fixed width, one prize per line:
#   positions 0-2    prize code, for example A01
#   positions 4-23   prize name
#   positions 24-28  cost in tickets

PRIZE_FILE = "prizes.txt"
MAX_QUANTITY = 5          # the most of one prize a player can take at once
NOT_FOUND = ""
NO_COST = 0


def read_tickets():
    """Ask for the tickets on the card until a whole number of 0 or more is typed."""
    while True:
        text = input("Tickets on your card: ").strip()
        try:
            tickets = int(text)
        except ValueError:
            print("Type the number printed on your card, like 480.")
            continue
        if tickets < 0:
            print("A card cannot hold fewer than 0 tickets.")
        else:
            return tickets


def find_prize_name(code):
    """Return the name of the prize with this code, or NOT_FOUND."""
    prize_file = open(PRIZE_FILE)
    name = NOT_FOUND
    line = prize_file.readline()
    while line != "":
        if line[0:3] == code:
            name = line[4:24].strip()
            break
        line = prize_file.readline()
    prize_file.close()
    return name


def find_prize_cost(code):
    """Return the ticket cost of the prize with this code, or NO_COST."""
    prize_file = open(PRIZE_FILE)
    cost = NO_COST
    line = prize_file.readline()
    while line != "":
        if line[0:3] == code:
            cost = int(line[24:29])
        line = prize_file.readline()
    prize_file.close()
    return cost


def can_afford(tickets, total_cost):
    """Check whether the player has enough tickets for this trade."""
    return tickets - total_cost


def main():
    print("PRIZE COUNTER")
    print("=============")
    tickets = read_tickets()
    prizes_won = 0

    while True:
        code = input("Prize code, or done: ").strip().upper()
        if code == "DONE":
            break

        name = find_prize_name(code)
        if name == NOT_FOUND:
            print(f"No prize has the code {code}. Check the codes on the wall.")
            continue

        # Everything that can go wrong with a number is handled in one place.
        try:
            quantity = int(input(f"How many {name}? "))
            cost = find_prize_cost(code)
            if quantity > MAX_QUANTITY:
                print(f"The limit is {MAX_QUANTITY} of each prize.")
                continue
            total_cost = cost * quantity
            if can_afford(tickets, total_cost) >= 0:
                tickets = tickets - total_cost
                prizes_won = prizes_won + quantity
                print(f"Enjoy your {name}. Tickets left: {tickets}")
            else:
                print("Not enough tickets for that.")
        except ValueError:
            print("How many must be a whole number, like 2.")

    print()
    print(f"Prizes traded for: {prizes_won}")
    print(f"Tickets left on your card: {tickets}")


if __name__ == "__main__":
    main()
