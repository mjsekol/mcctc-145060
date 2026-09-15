# Lab U5-02: Team Report
## 145060 Programming · Unit 5 · Week 10

**Gate:** 3 (open tooling). **Duration:** one Build 1 block, Thursday, 35 minutes, with
Friday flex time to finish. **Competencies:** 5.5.6 (format output: reports), 5.2.2 (scope
of data, including arrays), 5.1.5 (data management), 5.2.3 (arithmetic).

---

## The scenario

The JV basketball coach has a season of stats for ten players: games, points, rebounds,
shots made, and shots taken. What the coach actually needs before the end-of-season meeting
is points per game, rebounds per game, and shooting percentage for everyone, plus team
totals and how each position scored. One player has been injured all season and has played
zero games, and the report cannot crash because of him.

## What you will build

A program that takes a list of player dictionaries, adds three calculated fields to each
row, and prints a lined-up season report with team totals, a top scorer, and a
by-position summary.

---

## Starter code

Create `team_report.py` and type this in, or copy it from the lab handout file. It runs.
It does nothing useful. **The player names and numbers are invented.**

```python
# team_report.py
# Turns a season of JV basketball stats into a report the coach can read.
#
# This file runs right now. It does not do anything useful yet.
#
# Each player is a dictionary. The team is a list of those dictionaries.

PLAYERS = [
    {"name": "Jaylen Brooks", "position": "Guard", "games": 12, "points": 138, "rebounds": 30, "shots_made": 52, "shots_taken": 121},
    {"name": "Sofia Marchetti", "position": "Forward", "games": 12, "points": 101, "rebounds": 64, "shots_made": 41, "shots_taken": 88},
    {"name": "Dev Patel", "position": "Center", "games": 11, "points": 92, "rebounds": 97, "shots_made": 39, "shots_taken": 70},
    {"name": "Hannah Kowalski", "position": "Guard", "games": 12, "points": 77, "rebounds": 22, "shots_made": 28, "shots_taken": 75},
    {"name": "Marcus Greene", "position": "Forward", "games": 10, "points": 64, "rebounds": 41, "shots_made": 25, "shots_taken": 61},
    {"name": "Ana Lucia Reyes", "position": "Guard", "games": 9, "points": 45, "rebounds": 12, "shots_made": 17, "shots_taken": 49},
    {"name": "Tyler Nguyen", "position": "Center", "games": 8, "points": 30, "rebounds": 35, "shots_made": 13, "shots_taken": 24},
    {"name": "Grace Okonkwo", "position": "Forward", "games": 12, "points": 58, "rebounds": 50, "shots_made": 23, "shots_taken": 52},
    {"name": "Ethan Schultz", "position": "Guard", "games": 6, "points": 11, "rebounds": 5, "shots_made": 4, "shots_taken": 15},
    {"name": "Noah Fitzgerald", "position": "Forward", "games": 0, "points": 0, "rebounds": 0, "shots_made": 0, "shots_taken": 0},
]


def per_game(total, games):
    """Return total divided by games. TODO: decide what a player with 0 games gets."""
    return 0.0


def add_calculated_fields(players):
    """TODO: return a NEW list of player dictionaries with calculated fields added."""
    return []


print(f"Players on the roster: {len(PLAYERS)}")
rows = add_calculated_fields(PLAYERS)
print(f"Rows in the report: {len(rows)}")
```

Running it produces:

```
Players on the roster: 10
Rows in the report: 0
```

---

## Steps

### Step 1. Starter running and committed
**Observable result:** the two lines above, and a commit.

### Step 2. Divide safely
Finish `per_game`. Return the total divided by games, unless games is 0. Decide what a
player with no games should get, and write a comment saying why you chose it.
**Observable result:** `per_game(138, 12)` is `11.5`, and `per_game(0, 0)` returns your
chosen value **without** `ZeroDivisionError`.

### Step 3. Shooting percentage
Write `shooting_percent(made, taken)` that returns made divided by taken, times 100, with
the same zero guard.
**Observable result:** `shooting_percent(52, 121)` is about `42.98`.

### Step 4. Add the calculated fields
Finish `add_calculated_fields`. For each player, make a **new** dictionary that copies the
player's data (`dict(player)` does this), add `points_per_game`, `rebounds_per_game`, and
`shooting_pct`, and append it to the list you return.
**Observable result:** `Rows in the report: 10`, and `rows[0]["points_per_game"]` is
`11.5`. `PLAYERS[0]` does **not** have a `points_per_game` key, because you copied it.

### Step 5. Break it on purpose: one dictionary for every row
In a scratch copy of the function, create `row = {}` **above** the loop instead. Inside the
loop, set `row["name"]` and `row["points_per_game"]`, then append `row`. Print the first
three rows.
**Observable result:** all three rows show the **same** player, and **there is no error**.
Write which player, and why, in your README under `What I learned`. Then delete the scratch
copy.

### Step 6. Print the table
Write `print_report(rows)`. One line per player: name, position, points per game, rebounds
per game, and shooting percent, in lined-up columns with one decimal place.
**Observable result:** ten lines whose columns line up, including `Ana Lucia Reyes`, the
longest name.

### Step 7. Team totals
Write `team_totals(rows)` returning a dictionary of total points, rebounds, shots made, and
shots taken. Print total points and the **team** shooting percent, which is total made over
total taken, not the average of the ten percentages.
**Observable result:** `Team points: 616` and a team shooting percent of `43.6%`.

### Step 8. Top scorer
Write `top_scorer(rows)` returning the row with the highest points per game.
**Observable result:** `Jaylen Brooks at 11.5 points per game`.

### Step 9. Group by position
Write `group_by_position(rows)` returning a dictionary of position to a list of rows. Print
each position with its number of players and total points.
**Observable result:** Guard 4 players 271 points, Forward 4 players 223, Center 2 players
122.

### Step 10. Check one row by hand, README, push
Pick one player and calculate all three fields on paper. Put the arithmetic in your README
under `Checked by hand`. Push.

---

## Acceptance criteria

- [ ] Runs with no traceback, including Noah's zero games
- [ ] Three calculated fields on every row, and `PLAYERS` itself unchanged
- [ ] Table columns line up for every name
- [ ] Team points 616, team shooting 43.6%, top scorer Jaylen Brooks
- [ ] By-position totals match step 9
- [ ] README has `What I learned` (step 5) and `Checked by hand` (step 10)
- [ ] A comment explains your choice for a player with zero games
- [ ] Commits with messages that say why, pushed

---

## If it breaks

### 1. Dividing by zero

```
ZeroDivisionError: division by zero
```

**Cause:** Noah has 0 games or 0 shots taken, and the zero guard is missing or checks the
wrong variable.

### 2. A key typo

```
KeyError: 'point'
```

**Cause:** the key is `points`. Keys are exact. Copy them from the `PLAYERS` list rather
than retyping.

### 3. Looping over the wrong thing

```
TypeError: string indices must be integers, not 'str'
```

**Cause:** you looped over one dictionary, such as `for player in PLAYERS[0]`, which gives
you its **keys**, which are strings. Then `player["name"]` tries to use a string like an
index. Loop over `PLAYERS`, the list.

### 4. Formatting text as a number

```
ValueError: Unknown format code 'f' for object of type 'str'
```

**Cause:** `:.1f` is on a text value, such as the name. Put `.1f` only on numbers and `<18`
on text.

### Not an error: every row shows Noah Fitzgerald

**Cause:** one dictionary was created above the loop and appended ten times. That is step 5.
Create the row inside the loop.

---

## Stretch goal

The coach asks for "most improved" but the data has only one season. Write in your README
what data you would need, what calculated field would answer it, and what structure you
would store two seasons in. No code required.

---

## Submission checklist

- [ ] Runs with no traceback
- [ ] Numbers match the acceptance criteria
- [ ] Step 5 and step 10 recorded in the README from real runs
- [ ] `git status` clean, pushed
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Ten minutes in, still writing `PLAYERS[0]["points"] / PLAYERS[0]["games"]` one player at a time | SCAFFOLDED |
| Loop written, working through formatting and totals | STANDARD |
| Report finished and lined up before Build 1 ends | EXTENDED |
| "I do not play basketball" or "why would a real job need this" | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `per_game` and `shooting_percent` are provided complete.
- **Steps:** step 4 provides the loop and `row = dict(player)` line; they write the three
  field lines. Step 6 provides the header `print` and the first column's format.
- **Scope:** step 9, grouping, is removed.
- **Step 5 stays.**
- **Checkpoints:** show you after steps 4 and 7.

**Acceptance criteria:** runs with Noah included, three calculated fields, a readable table,
team points 616, top scorer found, step 5 recorded.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus:

**Added requirement.** Print a top-three leaderboard sorted by points per game, highest
first, with points per game shown to **two** decimal places.

**Hint, not the answer.** `sorted()` takes a `key` argument: a function that receives one
row and returns the value to sort by. Read the key functions section of the Sorting
Techniques how-to, `https://docs.python.org/3/howto/sorting.html`. You can pass the name of
a function you wrote with `def`.

**Added question for the README.** With one decimal place, two players look tied. With two,
they are not. Which two, and what does that tell you about rounding in a report the coach
will use to make decisions?

**Acceptance criteria:** all STANDARD criteria, a correct top three, and the README answer.

---

## APPLIED

**For the student who does not care about basketball.** The same skill runs a small
business.

**Changed scenario.** A bakery tracks how many of each item it baked and sold in a week.
Start from this data, as a list of dictionaries:

| Item | Category | Baked | Sold | Price |
|---|---|---|---|---|
| Cinnamon roll | Pastry | 140 | 131 | 3.50 |
| Blueberry muffin | Pastry | 120 | 94 | 2.75 |
| Sourdough loaf | Bread | 60 | 58 | 7.00 |
| Bagel | Bread | 200 | 151 | 1.50 |
| Chocolate chip cookie | Cookie | 180 | 180 | 1.25 |
| Oatmeal cookie | Cookie | 90 | 52 | 1.25 |
| Seasonal pie | Pastry | 0 | 0 | 18.00 |

**What you build.** Calculated fields for each item: revenue (sold times price), unsold
(baked minus sold), and waste percent (unsold over baked). Totals for the week, the item
with the highest waste percent, and revenue by category. The seasonal pie was not baked this
week and must not crash the report.

**The extra requirement that makes it the same lab.** Step 5's deliberate bug, done on this
data, recorded in the README. And a `Checked by hand` section for one item.

**Grading:** same scale and same dimensions. Requirements Fit is judged against the bakery
version of the acceptance criteria.
