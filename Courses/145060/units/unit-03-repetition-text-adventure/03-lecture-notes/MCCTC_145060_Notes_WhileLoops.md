# Lecture Notes: The while Loop
## 145060 Programming · Unit 3 · Week 6 · Thursday, October 15

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W06_WhileLoops.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W06_WhileLoops.pptx)

If you missed class, you can learn this concept from this file alone. Before you run the
infinite loop example, know how to stop a running program: click in the terminal and press
**Ctrl+C**. Practice that once on purpose before you need it.

---

## Why this exists

Every program you have written runs top to bottom once and ends. A game cannot work that way.
It has to show the room, read a command, react, and then **do it again**, over and over, until
the player wins, loses, or quits.

Yesterday you wrote this line of pseudocode:

```
WHILE playing
```

Today it becomes Python. A **loop** repeats a block of code. This course has two kinds, and today
is the first: `while`. The WebXam calls loops **repetition control structures**, outcome 5.3.6.

---

## The concept in plain language

```python
while condition:
    # this indented block repeats
    # as long as condition is True
# the first unindented line runs after the loop ends
```

A `while` loop works like an `if` that keeps coming back:

1. Check the condition.
2. If it is False, skip the block and continue after it. The loop is over.
3. If it is True, run the whole block.
4. **Go back to step 1.**

The condition is checked **at the top, before each pass**. Not in the middle. A value that becomes
False halfway through the block does not stop the block. It stops the **next** pass from starting.

Two words you will use:

- **Iteration:** one pass through the block.
- **Loop variable:** the value the condition depends on. **Something inside the loop must change it**,
  or the loop never ends.

There are two common shapes.

| Shape | You know in advance how many times? | Stops when |
|---|---|---|
| **Count-controlled** | Yes | A counter reaches a limit |
| **Sentinel-controlled** | No | A special value shows up, such as the player typing `quit` |

---

## Worked example 1: count-controlled, the storm countdown

```python
moves_left = 3

while moves_left > 0:
    print(f"Thunder rolls. Moves until the storm: {moves_left}")
    moves_left = moves_left - 1

print("The storm has reached the ridge.")
```

Output:

```
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 2
Thunder rolls. Moves until the storm: 1
The storm has reached the ridge.
```

Trace it. `moves_left` is 3, which is more than 0, so the block runs, prints 3, and `moves_left` becomes 2.
Back to the top: 2 is more than 0. Prints 2, becomes 1. Back to the top: prints 1, becomes 0. Back to the
top: **0 is not more than 0**, so the loop ends and the last line prints.

**Three parts make every count-controlled loop work.** Set the counter before the loop. Check it in the
condition. Change it inside the block. Miss any one of the three and the loop breaks, and the worst of
the three is the change.

What if the counter starts at 0?

```python
moves_left = 0

while moves_left > 0:
    print(f"Thunder rolls. Moves until the storm: {moves_left}")
    moves_left = moves_left - 1

print("The storm has reached the ridge.")
```

```
The storm has reached the ridge.
```

The condition was False the first time it was checked, so the block ran **zero times**. A `while` loop
might not run at all, and that is correct behavior.

---

## Worked example 2: sentinel-controlled, the game loop

The player decides when the game ends. You cannot count that in advance.

```python
playing = True

while playing:
    command = input("> ").strip().lower()
    if command == "look":
        print("Rain streaks the glass doors behind you.")
    elif command == "quit":
        print("You leave the station to the storm.")
        playing = False
    else:
        print(f"'{command}' is not a command. Try look or quit.")

print("GAME OVER")
```

Typing `look`, then `dance`, then `QUIT`:

```
> look
Rain streaks the glass doors behind you.
> dance
'dance' is not a command. Try look or quit.
> QUIT
You leave the station to the storm.
GAME OVER
```

`quit` is the **sentinel**: the value that signals the end. The loop variable is `playing`, a `bool`, and
the only line that changes it is inside the `quit` branch. That is exactly yesterday's pseudocode, and it
is the same shape the class adventure, Storm Relay, uses for its whole game.

**Everything from Unit 2 lives inside the loop.** The `if`/`elif`/`else` runs once per command. A loop
does not replace decisions. It repeats them.

There is a second way to write a sentinel loop, by checking the typed value directly:

```python
command = ""

while command != "quit":
    command = input("> ").strip().lower()
    print(f"You typed {command}.")

print("GAME OVER")
```

Typing `look`, then `quit`:

```
> look
You typed look.
> quit
You typed quit.
GAME OVER
```

**Look at the fourth line of output.** The program printed `You typed quit.` before stopping. The check
happens at the top of each pass, so the pass that read `quit` finished its block first. Sometimes that is
harmless. In a game, it might mean the player moves one more room after quitting. The `playing` flag
version above avoids it by deciding inside the block what to do with `quit`.

`command = ""` before the loop matters too. The condition reads `command` on the very first check, so it
must already exist.

---

## Worked example 3: a loop that refuses bad input

Unit 2's club sign-up refused a bad grade once and then ended. A loop can keep asking.

```python
grade = int(input("Grade level (9-12): "))

while grade < 9 or grade > 12:
    print("Sign-ups are for grades 9 through 12.")
    grade = int(input("Grade level (9-12): "))

print(f"Grade {grade} accepted.")
```

Typing `7`, then `13`, then `10`:

```
Grade level (9-12): 7
Sign-ups are for grades 9 through 12.
Grade level (9-12): 13
Sign-ups are for grades 9 through 12.
Grade level (9-12): 10
Grade 10 accepted.
```

The condition is the **refusal** condition from Unit 2, unchanged. The loop repeats while the input is bad.
The `input` line inside the block is the change that lets it end. Typing a word instead of a number still
crashes with a `ValueError`, and handling that is Unit 4.

---

## The wrong versions

### Wrong 1: the loop that never ends

Delete one line from worked example 1: the line that changes the counter.

```python
moves_left = 3

while moves_left > 0:
    print(f"Thunder rolls. Moves until the storm: {moves_left}")

print("The storm has reached the ridge.")
```

Output:

```
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 3
...
```

It never stops. `moves_left` is 3 forever, so `moves_left > 0` is True forever. This is an **infinite loop**.
When these notes were tested, the program printed more than 370,000 lines in the fifth of a second before it was
interrupted. Your terminal will scroll faster than you can read.

**Press Ctrl+C.** Python stops the program and ends the traceback with:

```
KeyboardInterrupt
```

That is not a bug in Python. It is Python telling you that you stopped it by hand. The traceback above it shows
which line was running when you did, which is useful: it is almost always inside the loop that forgot to change
its variable.

**The checklist when a loop will not stop:** what is the condition, what value does it depend on, and which line
inside the block changes that value? If you cannot point at the line, that is the bug.

### Wrong 2: the loop that runs one time too few, and does not crash

Practice is three laps.

```python
laps_required = 3
lap = 1

while lap < laps_required:
    print(f"Lap {lap} done.")
    lap = lap + 1

print("Practice complete.")
```

```
Lap 1 done.
Lap 2 done.
Practice complete.
```

**No error. Two laps.** Your coach would notice. Python did not.

`lap` starts at 1. When `lap` is 3, `3 < 3` is False, so the third lap never runs. Starting at 1 and using `<`
disagree about what the limit means. Either start at 0, or use `<=`:

```python
while lap <= laps_required:
```

```
Lap 1 done.
Lap 2 done.
Lap 3 done.
Practice complete.
```

This is the same bug as Week 3's `code[5:8]` giving `202`, and Week 4's `battery < 20` at exactly 20: a boundary
decided with the wrong comparison. It is the eleventh appearance of the shape this course keeps showing you. **The
dangerous bugs are the ones that do not crash**, and a loop that runs one time too few is one of the most common
in all of programming. Always count the iterations of a new loop by hand at least once.

### Wrong 3: the mistakes that do crash

```python
moves_left = 3
while moves_left > 0
    moves_left = moves_left - 1
```

```
    while moves_left > 0
                        ^
SyntaxError: expected ':'
```

```python
moves_left = 3
while moves_left > 0:
print(moves_left)
```

```
    print(moves_left)
    ^^^^^
IndentationError: expected an indented block after 'while' statement on line 2
```

Same rules as `if`: a colon, then an indented block.

---

## Why the wrong versions are tempting

**The update line feels like housekeeping.** The interesting line is the `print`. The `moves_left = moves_left - 1`
line looks like bookkeeping, and it is the line in the loop you are most likely to forget, move outside the block, or indent
wrong.

**Off by one looks right.** `while lap < laps_required` reads as "while we have not reached the required laps,"
which sounds exactly correct in English. Whether "reached" includes the last lap is the whole question, and the
sentence hides it.

**Small tests hide it.** If you test with one lap required, starting at 0, most off-by-one mistakes still print
something plausible. Test the loop with the real number and count the output lines.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Loop** | A structure that repeats a block of code. |
| **Repetition control structure** | The WebXam's term for a loop. |
| **`while`** | Repeats its block as long as its condition is True, checked at the top of each pass. |
| **Iteration** | One pass through the loop's block. |
| **Loop variable** | The value the loop condition depends on. Something inside the loop must change it. |
| **Count-controlled loop** | A loop that runs a known number of times, using a counter. |
| **Sentinel-controlled loop** | A loop that runs until a special value appears, such as `quit`. |
| **Sentinel** | The special value that ends a sentinel-controlled loop. |
| **Flag** | A `bool` such as `playing` that a loop checks, set to False to end it. |
| **Infinite loop** | A loop whose condition never becomes False. |
| **Off-by-one error** | A loop, slice, or boundary that is wrong by exactly one. |
| **`KeyboardInterrupt`** | What Python reports when you stop a running program with Ctrl+C. |

---

## Self-check

**Question 1.** Write the exact output.

```python
tickets_left = 5
while tickets_left > 1:
    tickets_left = tickets_left - 2
    print(f"Sold two. Left: {tickets_left}")
print("Window closed.")
```

**Question 2.** This program is supposed to print a countdown from 10 to 1 before a race. It prints nothing but the
last line, and there is no error. Explain why and fix it.

```python
seconds = 10
while seconds < 1:
    print(seconds)
    seconds = seconds - 1
print("Go.")
```

**Question 3.** A student's game loop never ends, even when they type `quit`. Find the bug.

```python
playing = True
while playing:
    command = input("> ").strip().lower()
    if command == "quit":
        print("Goodbye.")
        playing == False
```

---

### Answers

**1.**

```
Sold two. Left: 3
Sold two. Left: 1
Window closed.
```

5 is more than 1, so it becomes 3 and prints. 3 is more than 1, so it becomes 1 and prints. 1 is not more than 1, so
the loop ends. The value printed is the value **after** the subtraction, because the `print` comes second in the block.

**2.** The condition is backwards. `seconds` starts at 10, and `10 < 1` is False on the very first check, so the block
runs zero times. The loop should continue while there are seconds left: `while seconds >= 1:` or `while seconds > 0:`.
Either prints 10 down to 1, then `Go.`

**3.** `playing == False` **compares** `playing` to False and throws the answer away. It never changes `playing`. Unit 2's
rule: one equals assigns, two equals asks. The line must be `playing = False`. No error appears, because a comparison on
a line by itself is legal Python that does nothing.
