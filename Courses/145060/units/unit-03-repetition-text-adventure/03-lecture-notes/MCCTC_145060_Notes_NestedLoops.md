# Lecture Notes: Nested Loops and Nested Structures
## 145060 Programming · Unit 3 · Week 7, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W07_NestedLoops.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W07_NestedLoops.pptx)

If you missed class, you can learn this concept from this file alone. Before you run each example,
predict how many lines it prints. Then count. Today's bug prints fewer lines than it should and says
nothing.

---

## Why this exists

A lot of real information comes in two directions at once. A theater has rows **and** seats. A
season has weeks **and** days. A school day has periods, and a week has school days. A tournament has
players, and each player gets several attempts.

One loop walks one direction. To walk both, you put a loop **inside** a loop. And your text adventure
already puts decisions inside decisions inside a loop: which room, then which direction, every turn.
The WebXam names this directly in outcome 5.3.8: **write code that uses nested structures.**

---

## The concept in plain language

A **nested loop** is a loop inside the body of another loop.

```python
for outer in range(3):
    # this part runs 3 times
    for inner in range(4):
        # this part runs 4 times for EACH outer pass: 12 times total
    # this part runs 3 times, after each inner loop finishes
```

The rule that explains every nested loop:

> **The inner loop runs all the way through, from start to finish, on every single pass of the outer
> loop.**

So the inner body runs **outer count times inner count** times. Three outer passes of four inner passes
is 12.

A **nested structure** is any control structure inside another: an `if` inside a loop, a loop inside an
`if`, an `if` inside an `if` inside a `while`. **Indentation is the only thing that says what is inside
what.** Move a line four spaces left and it changes which structure owns it.

---

## Worked example 1: weeks and practices

```python
# Three weeks of practice, four practices a week.
for week in range(1, 4):
    print(f"Week {week}:")
    for practice in range(1, 5):
        print(f"  Practice {practice}")
```

```
Week 1:
  Practice 1
  Practice 2
  Practice 3
  Practice 4
Week 2:
  Practice 1
  Practice 2
  Practice 3
  Practice 4
Week 3:
  Practice 1
  Practice 2
  Practice 3
  Practice 4
```

Fifteen lines: 3 week headings plus 3 times 4 practices. Notice that `practice` starts over at 1 for every
week. The inner `for` begins fresh each time the outer loop reaches it.

---

## Worked example 2: counting the passes

```python
# The inner loop finishes completely for every outer pass.
passes = 0
for outer in range(1, 4):
    for inner in range(1, 3):
        passes = passes + 1
        print(f"outer {outer}, inner {inner}")
print(f"Inner body ran {passes} times")
```

```
outer 1, inner 1
outer 1, inner 2
outer 2, inner 1
outer 2, inner 2
outer 3, inner 1
outer 3, inner 2
Inner body ran 6 times
```

Read the left column top to bottom: the outer value holds still while the inner value runs through all of
its values. It works like a clock. The minute hand goes all the way around before the hour hand moves one
step.

---

## Worked example 3: building a seat map

```python
# Seat labels for a small theater: rows A to C, seats 1 to 5.
ROWS = 3
SEATS_PER_ROW = 5
for row in range(ROWS):
    row_letter = chr(ord("A") + row)
    row_text = ""
    for seat in range(1, SEATS_PER_ROW + 1):
        row_text = row_text + f"{row_letter}{seat} "
    print(row_text.strip())
print(f"Total seats: {ROWS * SEATS_PER_ROW}")
```

```
A1 A2 A3 A4 A5
B1 B2 B3 B4 B5
C1 C2 C3 C4 C5
Total seats: 15
```

Three things worth noticing:

- `chr(ord("A") + row)` is Week 4 coming back. Row 0 is `A`, row 1 is `B`, because letters are numbers.
- `row_text = ""` sits **inside the outer loop, above the inner loop.** It resets once per row. That
  placement is the whole trick. Move it above the outer loop and every row carries the previous rows with it.
- `print(row_text.strip())` is in the outer loop, after the inner loop, so it prints once per row, when the
  row is complete.

---

## Worked example 4: decisions nested inside a game loop

Your game already has nesting. Last week's decision tree said the destination depends on the room first
and the direction second. As code, inside the loop:

```python
    if command == "north" or command == "south" or command == "east" or command == "west":
        destination = ""
        if room == "lobby":
            if command == "north":
                destination = "hallway"
        elif room == "hallway":
            if command == "south":
                destination = "lobby"
            elif command == "west":
                destination = "studio"
        elif room == "studio":
            if command == "east":
                destination = "hallway"

        if destination == "":
            print(f"You cannot go {command} from here.")
        else:
            room = destination
            moves = moves + 1
```

That is an `if` inside an `if` inside an `if` inside a `while`. Four levels. It is correct nesting, because
each question really does depend on the answer before it, which is exactly Unit 2's rule for when to keep
nesting and when to flatten.

**The detail that saves you a bug:** `destination = ""` is set before the room check. If the direction has
no exit, `destination` stays empty, and one place handles "you cannot go that way." A blocked move costs no
moves, because only the `else` adds one.

---

## Worked example 5: break only leaves the loop it is in

```python
# Nested structures: an if inside an if inside a loop.
# Each of three friends gets up to three tries to guess the locker combo digit.
SECRET_DIGIT = "7"
for friend in range(1, 4):
    print(f"Friend {friend}")
    tries = 0
    while tries < 3:
        tries = tries + 1
        guess = input("  Guess a digit: ").strip()
        if guess == SECRET_DIGIT:
            print("  Correct")
            break
        else:
            if tries == 3:
                print("  Out of tries")
            else:
                print("  Nope")
```

Typing `3`, `7` for friend 1, then `1`, `2`, `4` for friend 2, then `9`, `7` for friend 3:

```
Friend 1
  Guess a digit: 3
  Nope
  Guess a digit: 7
  Correct
Friend 2
  Guess a digit: 1
  Nope
  Guess a digit: 2
  Nope
  Guess a digit: 4
  Out of tries
Friend 3
  Guess a digit: 9
  Nope
  Guess a digit: 7
  Correct
```

**Friend 1 guessed correctly, and the program still went on to friend 2.** The `break` ended the inner
`while` only. The outer `for` did not notice and moved to the next friend. That is Wednesday's rule, "the
loop it is directly inside," doing real work. If you want a correct guess to end everything, you need a
flag that the outer loop checks too.

`tries = 0` is inside the `for`, above the `while`. Every friend gets a fresh three tries. Hold that thought.

---

## The wrong version: the seating chart with one row

```python
row = 1
seat = 1
while row <= 3:
    while seat <= 4:
        print(f"Row {row}, seat {seat}")
        seat = seat + 1
    row = row + 1
print("Seating chart done")
```

```
Row 1, seat 1
Row 1, seat 2
Row 1, seat 3
Row 1, seat 4
Seating chart done
```

**No error. Four seats instead of twelve. "Seating chart done."**

Trace it. Row 1: `seat` goes 1, 2, 3, 4, then 5, and the inner loop ends. `row` becomes 2. The outer loop
reaches the inner `while` again and checks `seat <= 4`. **`seat` is still 5.** Nothing reset it. The inner
loop runs zero times for row 2, zero times for row 3, and the program announces it is done.

The fix is one line in a different place. The inner counter must be set **inside the outer loop**, right
before the inner loop, so it starts over for every row:

```python
row = 1
while row <= 3:
    seat = 1
    while seat <= 4:
        print(f"Row {row}, seat {seat}")
        seat = seat + 1
    row = row + 1
print("Seating chart done")
```

This prints all twelve seats, `Row 1, seat 1` through `Row 3, seat 4`, then `Seating chart done`.

**This bug cannot happen with `for`.** `for seat in range(1, 5):` starts `range` over every time the outer loop
reaches it. That is one more reason to prefer `for` when the count is known.

It is the same family as every silent bug this course has shown you, and it hides especially well, because
the first row is perfect. **When you test a nested loop, check the second pass of the outer loop, not the first.**

---

## Why the wrong version is tempting

**"Set it up before the loop" is a good habit that goes one level too far.** Accumulators and counters go above
the loop. With nesting, the question is **which** loop, and the inner counter belongs above the inner loop.

**The first pass is correct.** Most people read the first few lines of output, see them working, and stop reading.

**The ending message lies.** "Seating chart done" prints no matter how many seats were printed. Output that
announces success is not evidence of success.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Nested loop** | A loop inside the body of another loop. |
| **Outer loop** | The loop that contains the other loop. |
| **Inner loop** | The loop inside. It runs completely on every outer pass. |
| **Nested structure** | Any control structure inside another, such as an `if` inside a `while`. |
| **Indentation level** | How far a line is indented, which decides which structure it belongs to. |
| **Reset** | Setting a counter or accumulator back to its starting value at the right point in a loop. |
| **Outcome 5.3.8** | The WebXam competency for nested structures and recursion. |

---

## Self-check

**Question 1.** How many lines does this print? Do not run it first.

```python
for day in range(5):
    print("Day")
    for period in range(1, 8):
        print("Period")
print("Week over")
```

**Question 2.** Write the exact output.

```python
for row in range(1, 4):
    line = ""
    for star in range(row):
        line = line + "*"
    print(line)
```

**Question 3.** This should print every player's three attempts. It prints only player 1's. Find the line that is in the
wrong place and say where it belongs.

```python
player = 1
attempt = 1
while player <= 3:
    while attempt <= 3:
        print(f"Player {player}, attempt {attempt}")
        attempt = attempt + 1
    player = player + 1
```

---

### Answers

**1.** 41 lines. The outer loop runs 5 times and prints `Day` each time: 5 lines. The inner loop runs 7 times per day:
35 lines. Then `Week over` once. 5 + 35 + 1 = 41.

**2.**

```
*
**
***
```

The inner `range(row)` depends on the outer value. On row 1 it runs once, on row 2 twice, on row 3 three times. The inner
loop's count can change on every outer pass.

**3.** `attempt = 1` is above the outer loop, so it is set once and never reset. After player 1, `attempt` is 4, and the inner
loop runs zero times for players 2 and 3. Move `attempt = 1` inside the outer loop, directly above `while attempt <= 3:`.
Better still, write the inner loop as `for attempt in range(1, 4):` and the bug cannot happen.
