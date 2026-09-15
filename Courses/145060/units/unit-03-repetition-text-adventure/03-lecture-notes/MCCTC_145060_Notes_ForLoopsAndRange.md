# Lecture Notes: for Loops and range
## 145060 Programming · Unit 3 · Week 7, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W07_ForLoopsAndRange.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W07_ForLoopsAndRange.pptx)

If you missed class, you can learn this concept from this file alone. Type every example.
Count the lines of output on every one, because the bug in this file does not crash and the
only way to see it is to count.

---

## Why this exists

Thursday's `while` loop needs three things from you, every time:

1. Set the counter before the loop.
2. Check it in the condition.
3. Change it inside the block.

Forget the third and the loop never ends. Get the second one slightly wrong and the loop runs
one time too few, which is exactly what happened to the three-lap practice on Thursday.

A huge number of loops have the same shape: **do this a known number of times**, or **do this
once for each thing in a sequence.** Seven days of pushups. Three repeats of an emergency
broadcast. Every character in a username. For that shape, Python has a loop that does all three
counter jobs for you. It is `for`, and together with `while` it completes outcome 5.3.6:
**repetition control structures (while, for).**

---

## The concept in plain language

```python
for name in sequence:
    # this indented block runs once for each item in the sequence
    # and name holds the current item
# the first unindented line runs after the last item
```

A `for` loop walks through a sequence **one item at a time**. On each pass, the loop variable
holds the current item. When the sequence runs out, the loop ends. There is no condition to write
and no counter to update, because the sequence decides both.

The sequence you will use most is **`range`**, which produces whole numbers.

| You write | Numbers produced | How to read it |
|---|---|---|
| `range(5)` | 0, 1, 2, 3, 4 | five numbers, starting at 0 |
| `range(1, 8)` | 1, 2, 3, 4, 5, 6, 7 | from 1 up to but not including 8 |
| `range(10, 31, 5)` | 10, 15, 20, 25, 30 | from 10, counting by 5, stopping before 31 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 | from 5, counting down, stopping before 0 |

**The rule you already know.** `range` stops **before** its stop number, exactly like a slice.
`code[5:9]` gives positions 5, 6, 7, 8. `range(5, 9)` gives 5, 6, 7, 8. Say it the same way:
**from here, up to but not including there.**

A string is also a sequence, so a `for` loop can walk through its characters.

---

## Worked example 1: the same loop, written both ways

Thursday's version, with a `while`:

```python
# The while version from Thursday: three places to get right.
day = 1
while day <= 7:
    print(f"Day {day}: 20 pushups")
    day = day + 1
```

Today's version, with a `for`:

```python
# The for version: range does the counting.
for day in range(1, 8):
    print(f"Day {day}: 20 pushups")
```

Both print the same seven lines:

```
Day 1: 20 pushups
Day 2: 20 pushups
Day 3: 20 pushups
Day 4: 20 pushups
Day 5: 20 pushups
Day 6: 20 pushups
Day 7: 20 pushups
```

Count the lines of the two programs. The `for` version has no `day = 1` and no `day = day + 1`.
`range(1, 8)` supplies every value `day` will take, in order, and there is **no update line to
forget**. That is not a small thing. The most common infinite loop in this course is a `while`
with a missing update, and a `for` over a `range` cannot have one.

**Why 8 and not 7?** Up to but not including. To reach 7, stop at 8.

---

## Worked example 2: starting at zero, counting by fives, counting down

```python
for rep in range(5):
    print("Rep", rep)
```

```
Rep 0
Rep 1
Rep 2
Rep 3
Rep 4
```

**Five reps, numbered 0 to 4.** One number in `range` means "this many, starting at 0." That is
perfect when you only care about how many times something happens. It is wrong the moment a person
reads the numbers, because nobody does rep zero.

A step changes how much each number grows:

```python
# Couch-to-5K style plan: start at 10 minutes, add 5 each week, stop at 30.
for minutes in range(10, 31, 5):
    print(f"Run {minutes} minutes")

print("Countdown to the bus:")
for seconds in range(5, 0, -1):
    print(seconds)
print("Go")
```

```
Run 10 minutes
Run 15 minutes
Run 20 minutes
Run 25 minutes
Run 30 minutes
Countdown to the bus:
5
4
3
2
1
Go
```

`range(10, 31, 5)` stops before 31, so 30 is included. `range(5, 0, -1)` counts **down** and stops
before 0, so it ends at 1. A negative step is the only way `range` counts backwards.

---

## Worked example 3: repeating an action a set number of times

In the class adventure, Storm Relay, an emergency broadcast repeats so that somebody who tunes in
late still hears it. The number of repeats is a constant.

```python
BROADCAST_REPEATS = 3
EMERGENCY_FREQUENCY = 1470

for repeat in range(1, BROADCAST_REPEATS + 1):
    print(f"({repeat} of {BROADCAST_REPEATS}) This is Kestrel Ridge relay on {EMERGENCY_FREQUENCY} kHz.")
```

```
(1 of 3) This is Kestrel Ridge relay on 1470 kHz.
(2 of 3) This is Kestrel Ridge relay on 1470 kHz.
(3 of 3) This is Kestrel Ridge relay on 1470 kHz.
```

**`BROADCAST_REPEATS + 1` is the pattern to memorize.** When you count from 1 and want the last
number to be the limit itself, the stop is the limit plus one. Change the constant to 5 and the loop
prints five lines, labeled `1 of 5` through `5 of 5`, with no other edit.

---

## Worked example 4: walking through a string

```python
# A for loop walks any sequence. A string is a sequence of characters.
username = "xX_SkaterAva_Xx"
underscores = 0
for character in username:
    if character == "_":
        underscores = underscores + 1
print(f"{username} has {underscores} underscores")
```

```
xX_SkaterAva_Xx has 2 underscores
```

On each pass, `character` holds one character of the username, in order, from `x` to `x`. No index
numbers and no slicing. The `if` inside the loop runs once per character. **Everything from Unit 2
still works inside a loop.** A loop repeats decisions, it does not replace them.

`underscores` is an **accumulator**: a variable set before the loop and updated inside it, so that
after the loop it holds a result built from every pass.

---

## Worked example 5: an accumulator with input

```python
# Accumulator: add up a week of practice minutes typed in one day at a time.
total_minutes = 0
for day in range(1, 8):
    minutes = int(input(f"Minutes practiced on day {day}: "))
    total_minutes = total_minutes + minutes
print(f"Week total: {total_minutes} minutes")
```

Typing `30`, `45`, `0`, `60`, `30`, `20`, `90`:

```
Minutes practiced on day 1: 30
Minutes practiced on day 2: 45
Minutes practiced on day 3: 0
Minutes practiced on day 4: 60
Minutes practiced on day 5: 30
Minutes practiced on day 6: 20
Minutes practiced on day 7: 90
Week total: 275 minutes
```

Two placement rules that make or break an accumulator:

- **`total_minutes = 0` goes before the loop.** Put it inside and it resets to 0 every day, so the
  total is only the last day.
- **The final `print` goes after the loop, unindented.** Indent it and it prints a running total
  seven times.

---

## The wrong version: the week that has six days

```python
# Wrong: a week has seven days.
for day in range(1, 7):
    print(f"Day {day}: 20 pushups")
print("Week complete")
```

```
Day 1: 20 pushups
Day 2: 20 pushups
Day 3: 20 pushups
Day 4: 20 pushups
Day 5: 20 pushups
Day 6: 20 pushups
Week complete
```

**No error. Six days. "Week complete."** The program is confident and wrong.

`range(1, 7)` stops **before** 7. The writer was thinking "days 1 through 7," typed the 7, and
`range` did precisely what it always does. This is Thursday's three-lap practice that stopped at two
laps, and it is Week 3's `code[5:8]` giving `202`. **The dangerous bugs are the ones that do not
crash**, and a loop that runs one time too few is one of the most common of them in all of
programming.

**The defense is counting, not staring.** For every new loop, count the lines of output on one real
run. Six is not seven, and you will only notice if you count.

### The mistakes that do crash

`range` needs whole numbers. `input()` gives text:

```python
days = input("How many days? ")
for day in range(days):
    print("Day", day)
```

```
    for day in range(days):
               ~~~~~^^^^^^
TypeError: 'str' object cannot be interpreted as an integer
```

Convert on the line you ask: `days = int(input("How many days? "))`.

If you convert later and add first, you get Unit 1's error instead:

```
TypeError: can only concatenate str (not "int") to str
```

A missing colon gives `SyntaxError: expected ':'`, the same as `while` and `if`.

---

## Why the wrong version is tempting

**The number you type is the number in your head.** "Days 1 through 7" puts a 7 in your head, and
your fingers type the 7. `range` wants 8. Nothing about the line looks wrong.

**`range(7)` hides it the other way.** `range(7)` does give seven numbers, so a student who learned
"seven times means 7" gets the right count, then prints `Day 0` and never `Day 7`. Both habits are
half right.

**Short tests pass.** A loop that should run 3 times and runs 2 still prints something plausible.
Test with the real number and count.

---

## Which loop to use

| Situation | Use | Why |
|---|---|---|
| Do something a known number of times | `for` with `range` | No counter to forget |
| Do something once for each character | `for` over the string | No index arithmetic |
| Keep going until the player quits | `while` | Nobody knows the count in advance |
| Keep asking until the answer is valid | `while` | Nobody knows how many bad answers are coming |

**The test question:** before the loop starts, can the program know how many passes it will make? If
yes, `for`. If no, `while`. A text adventure's game loop is a `while` for exactly this reason, and
the repeats inside a broadcast are a `for`.

---

## Vocabulary

| Term | What it means |
|---|---|
| **`for` loop** | Runs its block once for each item in a sequence. |
| **Sequence** | An ordered series of items a `for` loop can walk through, such as a `range` or a string. |
| **`range(stop)`** | Whole numbers from 0 up to but not including `stop`. |
| **`range(start, stop)`** | Whole numbers from `start` up to but not including `stop`. |
| **`range(start, stop, step)`** | Counts by `step`. A negative step counts down. |
| **Loop variable** | The name that holds the current item on each pass. |
| **Accumulator** | A variable set before a loop and updated on every pass to build a result. |
| **Off-by-one error** | A loop or boundary that is wrong by exactly one. |
| **Repetition control structure** | The WebXam's term for a loop, outcome 5.3.6. |

---

## Self-check

**Question 1.** Write the exact output.

```python
for points in range(100, 500, 150):
    print(points)
print("done")
```

**Question 2.** A program should print `Round 1` through `Round 12` for a tournament. It prints
`Round 0` through `Round 11`. Write the line that is wrong and the fixed line.

```python
for round_number in range(12):
    print(f"Round {round_number}")
```

**Question 3.** For each task, say `for` or `while`, and give the reason in one sentence.

- Print a reminder for each of the 5 school days
- Keep asking for a PIN until the right one is typed
- Count the vowels in a song title
- Keep a game running until the player types `quit`

---

### Answers

**1.**

```
100
250
400
done
```

It starts at 100 and adds 150 each time. The next number would be 550, which is not less than 500,
so the loop stops after 400.

**2.** `range(12)` produces 0 through 11. The fix is:

```python
for round_number in range(1, 13):
    print(f"Round {round_number}")
```

Twelve numbers, starting at 1, stopping before 13. No error appeared, which is why you have to read
the output to catch it.

**3.**

| Task | Loop | Reason |
|---|---|---|
| Reminder for each of 5 school days | `for` | The count, 5, is known before the loop starts. |
| Ask for a PIN until correct | `while` | Nobody knows how many wrong tries are coming. |
| Count vowels in a song title | `for` | A `for` walks every character of a string. |
| Keep a game running until `quit` | `while` | The player decides when it ends, so there is no count. |
