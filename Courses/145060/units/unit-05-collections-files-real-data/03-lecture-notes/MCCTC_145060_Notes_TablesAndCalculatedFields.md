# Lecture Notes: Tables in Code and Calculated Fields
## 145060 Programming · Unit 5 · Week 10, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W10_TablesAndCalculatedFields.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W10_TablesAndCalculatedFields.pptx)

If you missed class, you can learn this concept from this file alone. The bug in the
middle of this file produces a report that looks complete. Type it and see it for
yourself before you read the explanation.

**Every program below was run on Python 3.13.7.** The output shown is the real output.

---

## Why this exists

A coach has a season of stats: games played, total points, rebounds. What the coach
wants to see is **points per game** for every player, and how the guards compare with
the forwards. Nobody typed those numbers anywhere.

Every real report works like this. The data you are given has some columns. The report
needs columns that are **calculated** from them: a price times a quantity, a total
divided by a count, a percent of a whole. This lesson puts Monday's lists and Tuesday's
dictionaries together into the shape that holds that kind of data, and shows you how to
add the columns nobody typed.

---

## The concept in plain language

**A list of dictionaries is a table.**

- Each **dictionary** is one row. Its keys are the column names.
- The **list** holds the rows, in order.
- `players[1]["name"]` reads row 1, column `name`.

This is exactly the shape a spreadsheet, a CSV file, and a table on a website turn into
when a program reads them. You will read all three into this shape next week.

**A calculated field is a value your program computes from other values in the same
row, or across rows.** Points per game is a calculated field. So is a team total, a
percent, or a price after a discount.

**Grouping** means sorting rows into buckets by one column, such as position. The result
is a **dictionary of lists**: each key is a group, and each value is the list of rows in
that group.

---

## Worked example 1: a calculated field and a running total

```python
players = [
    {"name": "Jaylen", "position": "Guard", "games": 12, "points": 138},
    {"name": "Sofia", "position": "Forward", "games": 12, "points": 101},
    {"name": "Dev", "position": "Center", "games": 11, "points": 92},
    {"name": "Hannah", "position": "Guard", "games": 12, "points": 77},
]

print(players[1]["name"])

total_points = 0
for player in players:
    player["ppg"] = player["points"] / player["games"]
    total_points += player["points"]
    print(f"{player['name']:<8} {player['ppg']:.1f} points per game")
print("Team points:", total_points)
```

Output:

```
Sofia
Jaylen   11.5 points per game
Sofia    8.4 points per game
Dev      8.4 points per game
Hannah   6.4 points per game
Team points: 408
```

One loop does two jobs:

1. `player["ppg"] = ...` adds a new key to each row. That is the calculated field.
2. `total_points += ...` adds each row to a running total. That is the accumulator you
   have written since Unit 3.

**Check one by hand before you trust any of them.** 138 points over 12 games is 11.5.
The four point totals add to 408. A report you have never checked by hand is a guess
with nice formatting.

---

## Worked example 2: grouping into a dictionary of lists

```python
by_position = {}
for player in players:
    if player["position"] not in by_position:
        by_position[player["position"]] = []
    by_position[player["position"]].append(player["name"])
print(by_position)
```

Output:

```
{'Guard': ['Jaylen', 'Hannah'], 'Forward': ['Sofia'], 'Center': ['Dev']}
```

This is Tuesday's counting pattern with a list in place of a number. If the group has no
list yet, start an empty one. Then append to it. Version 3 of the text adventure stores
the items left in each room exactly this way: a dictionary from room id to a list of item
names.

---

## Worked example 3: calculated fields that depend on the whole table

Some calculated fields need a total first. A percent of the whole is the common case.

```python
orders = [
    {"item": "hoodie", "quantity": 3, "price": 32.00},
    {"item": "beanie", "quantity": 5, "price": 12.50},
    {"item": "sticker pack", "quantity": 10, "price": 4.00},
]

grand_total = 0
for order in orders:
    order["line_total"] = order["quantity"] * order["price"]
    grand_total += order["line_total"]

for order in orders:
    share = order["line_total"] / grand_total * 100
    print(f"{order['item']:<14}{order['line_total']:>8.2f}{share:>7.1f}%")
print(f"{'Total':<14}{grand_total:>8.2f}")
```

Output:

```
hoodie           96.00   48.4%
beanie           62.50   31.5%
sticker pack     40.00   20.2%
Total           198.50
```

**Two loops, on purpose.** You cannot work out a share of the total until you know the
total. The first loop builds each line total and the grand total. The second loop uses
them. Trying to do both in one loop gives you shares of a total that is not finished yet,
and the percents come out wrong without any error.

`:>8.2f` means right-aligned, 8 characters wide, 2 decimal places. Right-aligning numbers
lines up the decimal points, which is what makes a report readable.

---

## A failure to name before you hit it: dividing by zero

```python
players = [
    {"name": "Grace", "games": 12, "points": 58},
    {"name": "Noah", "games": 0, "points": 0},
]
for player in players:
    print(player["name"], player["points"] / player["games"])
```

Output:

```
Grace 4.833333333333333
Traceback (most recent call last):
  ...
    print(player["name"], player["points"] / player["games"])
                          ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

One injured player with zero games, and the whole report stops. Put the check inside a
function that does the dividing, and decide on purpose what the report should show:

```python
def per_game(total, games):
    """Return total divided by games, or None for a player who has not played."""
    if games == 0:
        return None
    return total / games


players = [
    {"name": "Grace", "games": 12, "points": 58},
    {"name": "Noah", "games": 0, "points": 0},
]
for player in players:
    ppg = per_game(player["points"], player["games"])
    if ppg is None:
        print(f"{player['name']:<6} not played")
    else:
        print(f"{player['name']:<6} {ppg:.1f}")
```

Output:

```
Grace  4.8
Noah   not played
```

Returning `None` instead of `0` keeps "has not played" different from "played and scored
nothing." Those are different facts, and a report should not blur them.

---

## The wrong version, and what it does instead of an error

You want a separate report list holding each player's name and points per game.

```python
players = [
    {"name": "Jaylen", "games": 12, "points": 138},
    {"name": "Sofia", "games": 12, "points": 101},
    {"name": "Dev", "games": 11, "points": 92},
]

report = []
row = {}
for player in players:
    row["name"] = player["name"]
    row["ppg"] = round(player["points"] / player["games"], 1)
    report.append(row)

for line in report:
    print(line)
```

Output:

```
{'name': 'Dev', 'ppg': 8.4}
{'name': 'Dev', 'ppg': 8.4}
{'name': 'Dev', 'ppg': 8.4}
```

**No error. Three rows, and every one of them is Dev.**

There was only ever **one** dictionary. `row = {}` ran once, above the loop. Each
`report.append(row)` did not copy it. It added another reference to that same
dictionary. Every pass through the loop overwrote the same two keys, so by the end, all
three entries in the list point at one dictionary holding the last player.

This is the name tag model from Unit 1 arriving with real consequences. Two names, or
three list slots, can point at the same thing.

### The fix: a new dictionary on every pass

```python
report = []

for player in players:
    row = {}
    row["name"] = player["name"]
    row["ppg"] = round(player["points"] / player["games"], 1)
    report.append(row)
```

Output:

```
{'name': 'Jaylen', 'ppg': 11.5}
{'name': 'Sofia', 'ppg': 8.4}
{'name': 'Dev', 'ppg': 8.4}
```

Moving one line inside the loop makes a brand new dictionary each time.

### Copying a row on purpose

If you want a new row that starts with everything the old row had, `dict()` makes a copy:

```python
player = {"name": "Dev", "games": 11, "points": 92}
row = dict(player)
row["ppg"] = round(row["points"] / row["games"], 1)
print(player)
print(row)
```

Output:

```
{'name': 'Dev', 'games': 11, 'points': 92}
{'name': 'Dev', 'games': 11, 'points': 92, 'ppg': 8.4}
```

The original is untouched. The copy has the new field.

---

## Why the wrong version is tempting

**It looks tidy.** Setting up your variables before the loop is a habit you were
rewarded for with counters and totals. `total = 0` above the loop is correct. `row = {}`
above the loop is not, and they look almost identical.

**It works with one player.** Test it with a single row and it is perfect.

**The output looks complete.** Three rows, correct keys, reasonable numbers. You have to
read the names to see that anything is wrong. That is what makes it a bug that does not
crash.

The rule that separates the two cases: **a number is replaced when you add to it. A
dictionary is changed in place.** Anything you mean to append as a separate row must be
created inside the loop.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Table** | Rows and columns. In Python, a list of dictionaries. |
| **Row** | One dictionary in the list. One player, one order, one sign-up. |
| **Column** | A key that every row has. |
| **Calculated field** | A value computed from other values, such as points per game. |
| **Accumulator** | A variable that builds up a total across a loop. |
| **Grouping** | Sorting rows into buckets by one column. |
| **Dictionary of lists** | Each key is a group and each value is a list of that group's rows. |
| **Reference** | A name or list slot that points at a value. Several can point at one value. |
| **`dict(d)`** | A new dictionary copying every pair from `d`. |
| **`ZeroDivisionError`** | You divided by zero. Guard the division, not the whole report. |

---

## Self-check

**Question 1.** Write the exact output.

```python
cart = [
    {"item": "fries", "price": 3.00, "quantity": 2},
    {"item": "shake", "price": 4.50, "quantity": 1},
]
total = 0
for line in cart:
    line["cost"] = line["price"] * line["quantity"]
    total += line["cost"]
print(cart[0]["cost"], total)
print(len(cart[1]))
```

**Question 2.** A student's report prints the same student on every row, and there is no
error. Name the most likely cause in one sentence and the one-line fix.

**Question 3.** You are building a report of how many hoodies each grade ordered. Should
the result be a list, a dictionary, or a dictionary of lists? What if the report also has
to name who in each grade ordered one?

---

### Answers

**1.**

```
6.0 10.5
4
```

Fries cost 3.00 times 2, which is 6.0. The total is 6.0 plus 4.50, which is 10.5. The
shake row started with three keys and gained `cost`, so it has four.

**2.** The row dictionary was created once, above the loop, so every append added the same
dictionary and each pass overwrote it. Move `row = {}` inside the loop.

**3.** For a count per grade, a **dictionary** from grade to a number. If the report also
names who ordered, a **dictionary of lists** from grade to the list of names, and the
count for each grade is the `len()` of its list, so you do not need to store the count
separately.
