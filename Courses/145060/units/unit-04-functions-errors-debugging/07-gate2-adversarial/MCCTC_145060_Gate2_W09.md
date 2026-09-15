# Gate 2: Adversarial Review · Week 9
## 145060 Programming · Unit 4 · Friday, November 6

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether it is correct, because the model is
what is being reviewed.

The files are in [`gate2-w09-files/`](gate2-w09-files/): `prize_counter.py` and `prizes.txt`. Put them in the same folder and run the
program from that folder. In PowerShell, type your input at the prompts, or put it in a text file and run
`cmd /c "python prize_counter.py < my_input.txt"`.

**This program uses Units 0 through 4 only:** functions, `try` and `except`, loops, and reading a file. No lists or dictionaries.

---

## What you are looking at

Somebody gave an AI assistant the requirements in Part A and got the program in Part B. It runs, it has functions with docstrings, it
validates input, and it has error handling.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It trusts something it should not, so someone can get something they should not |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

---

## PART A: The requirements

> The arcade at a family fun center lets kids trade prize tickets at a self-serve kiosk. Staff update the prize list by hand in a text
> file whenever the prize wall changes. Write `prize_counter.py`.
>
> 1. Read prizes from **`prizes.txt`**. It is fixed width: prize code in positions 0-2, prize name in positions 4-23, cost in tickets in
>    positions 24-28.
> 2. Ask how many tickets are on the player's card. It must be a whole number, 0 or more.
> 3. Repeat until the player types `done`: ask for a prize code, in any capitalization, then ask how many, **from 1 to 5**. If the player has
>    enough tickets, subtract the cost and say how many are left. **If not, say how many more tickets they need.**
> 4. A code that is not on the list gets a message naming the code. Anything that is not a whole number gets a message asking for a whole
>    number. **The kiosk must never crash, and never give a player a wrong message, on anything a player types.**
> 5. When the player types `done`, print how many prizes they traded for and the tickets left on the card.

The prize file, exactly as staff left it:

```
A01 Glow bracelet          15
A02 Sticker sheet          20
B03 Mini basketball       150
B04 Slime kit             175
C05 Plush dragon          400
C06 LED desk lamp         750
C07 Bluetooth speaker   1,200
D08 Gaming headset       2500
```

The fun center and its kiosk are a composite scenario written for this exercise.

---

## PART B: What the AI produced

Count line numbers from `# prize_counter.py` as line 1. Blank lines count.

```python
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
```

### A real run

Typing `480`, then `a01` and `2`, then `B03` and `1`, then `done`:

```
PRIZE COUNTER
=============
Tickets on your card: 480
Prize code, or done: a01
How many Glow bracelet? 2
Enjoy your Glow bracelet. Tickets left: 450
Prize code, or done: B03
How many Mini basketball? 1
Enjoy your Mini basketball. Tickets left: 300
Prize code, or done: done

Prizes traded for: 3
Tickets left on your card: 300
```

**Before you read the code line by line, check that run against Part A.** Two glow bracelets at 15 is 30. A mini basketball is 150. 480 minus 180 is 300.
It is right. That is what makes this hard.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real player or the staff**, **the input that shows it**, and **the fix**. Then one
final entry: **what I was unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 10:** you are a kid at the kiosk with not quite enough tickets for the prize you want. Play it that way. Then read requirement 3 again and look at what
  the kiosk told you. Then try quantities nobody sensible would type.
- **Next 10:** read every `try` block, and ask what its `except` is really catching. Requirement 4 says the kiosk must never give a player a wrong message.
- **Next 10:** read each function's name and docstring, then its `return` line. Does the function hand back what its name promises? Then count how many lines of
  `prizes.txt` each lookup reads to find prize `A01`.
- **Rest:** the unsure-about entry. Name something specific.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the security weighting before you start. **Four of five is a strong
score.**
