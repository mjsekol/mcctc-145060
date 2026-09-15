# Lecture Notes: Defining Functions with Parameters
## 145060 Programming · Unit 4 · Week 8 · Wednesday, October 28

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W08_DefiningFunctions.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W08_DefiningFunctions.pptx)

If you missed class, you can learn this concept from this file alone. Open your text adventure
version 1 in a second window while you read. By the end of this file you should be able to point at
three places in it that want to be functions.

**Today is one concept: defining a function and giving it parameters.** Functions that hand a value
back with `return` are tomorrow. Every function in this file does its job by printing.

---

## Why this exists

Look at your text adventure. Somewhere in it, you probably print a room heading, a line of dashes, and
an exits line, and you do it once per room. Maybe six times. Now your playtester says the headings
should be in capitals. You have six edits to make, and if you miss one, one room looks different and
nobody notices for a week.

Copy and paste creates a promise that you will change every copy together, forever. You will not keep
that promise. Nobody does.

A **function** gives a block of code a name, so it lives in **one place** and runs wherever you call it.
Change the one place and every call changes. That is outcome 5.3.9, **write code that creates and calls
functions**, and it is the first step of text adventure version 2, which is version 1 refactored into
functions.

---

## The concept in plain language

```python
def function_name(parameter_one, parameter_two):
    # the indented block is the body
    # it runs only when the function is called

function_name(argument_one, argument_two)   # the call
```

- **`def`** defines a function. Defining it does **not** run it. It teaches Python a new name.
- The **body** is the indented block under the `def` line.
- A **parameter** is a name in the parentheses of the `def`. It is a placeholder for a value the caller
  will supply.
- A **call** runs the body. You call a function by writing its name followed by parentheses.
- An **argument** is the actual value you put in the parentheses when you call it. Python ties each
  parameter to the matching argument **by position**: first to first, second to second.

You have been calling functions since Week 1. `print("hi")` calls `print` with one argument. `len(code)`
calls `len`. Today you write your own.

---

## Worked example 1: the copy-and-paste problem, fixed

Without a function:

```python
# Without a function: the same three lines, pasted three times.
print()
print("== Kitchen ==")
print("-" * 20)
print()
print("== Porch ==")
print("-" * 20)
print()
print("== Bedroom ==")
print("-" * 20)
```

With a function:

```python
# With a function: the three lines have one name and live in one place.
def show_heading(room_name):
    print()
    print(f"== {room_name} ==")
    print("-" * 20)

show_heading("Kitchen")
show_heading("Porch")
show_heading("Bedroom")
```

Both print exactly the same thing:

```

== Kitchen ==
--------------------

== Porch ==
--------------------

== Bedroom ==
--------------------
```

On the first call, `room_name` is `"Kitchen"`. On the second, `"Porch"`. The body is the same three lines every
time. Only the value tied to the parameter changes. To make every heading capitals, you now change one line.

---

## Worked example 2: two parameters, matched by position

```python
# Two parameters. Arguments are matched to parameters by position.
def print_receipt_line(item, price):
    print(f"{item:<16}${price:>6.2f}")

print_receipt_line("Nachos", 4.5)
print_receipt_line("Sports drink", 2.25)
print_receipt_line("Pretzel", 3)
```

```
Nachos          $  4.50
Sports drink    $  2.25
Pretzel         $  3.00
```

The first argument goes to `item`. The second goes to `price`. The format specifiers from Week 3 make every line
line up, and they live in one place now, so every receipt line is formatted identically without you trying.

---

## Worked example 3: a function body can hold anything you know

```python
# A function can make decisions and run loops inside it.
def warn_storm(moves_left):
    if moves_left == 1:
        print("Thunder rolls closer. The storm is 1 move away.")
    elif moves_left <= 5:
        print(f"Thunder rolls closer. The storm is {moves_left} moves away.")

def repeat_message(message, times):
    for count in range(1, times + 1):
        print(f"({count} of {times}) {message}")

warn_storm(9)
warn_storm(4)
warn_storm(1)
repeat_message("Stay on high ground.", 3)
```

```
Thunder rolls closer. The storm is 4 moves away.
Thunder rolls closer. The storm is 1 move away.
(1 of 3) Stay on high ground.
(2 of 3) Stay on high ground.
(3 of 3) Stay on high ground.
```

`warn_storm(9)` printed nothing, and that is correct: 9 matches neither condition. Everything from Units 2 and 3
works inside a function body: `if`, `elif`, `for`, `while`, `break`. The body is ordinary code that happens to have a
name.

```python
# A function that uses a loop and a parameter to draw a battery meter.
def show_battery(moves_left):
    meter = ""
    for bar in range(moves_left):
        meter = meter + "|"
    print(f"Battery [{meter:<8}] {moves_left} moves")

show_battery(8)
show_battery(3)
show_battery(0)
```

```
Battery [||||||||] 8 moves
Battery [|||     ] 3 moves
Battery [        ] 0 moves
```

---

## Worked example 4: defining is not running

```python
# Defining a function does not run it.
def celebrate():
    print("YOU WIN")

print("Game over screen loaded")
```

```
Game over screen loaded
```

**`YOU WIN` never prints.** The `def` taught Python what `celebrate` means. Nothing asked it to happen. A function with
no parameters still needs empty parentheses, both in the `def` and in the call. Writing `celebrate` on a line by itself
without the parentheses is legal, does nothing, and gives no error.

Order matters in a script, too. Python reads top to bottom, so the `def` has to run before the first call reaches it:

```python
def show_heading(room_name):
    print(f"== {room_name} ==")

print("Before the call")
show_heading("Studio")
print("After the call")
```

```
Before the call
== Studio ==
After the call
```

When the call runs, Python jumps into the body, runs it, and comes back to the line after the call. Put every `def` near
the top of your file, below your constants, and every call below them.

---

## The wrong version: calling without the argument

```python
def show_heading(room_name):
    print()
    print(f"== {room_name} ==")
    print("-" * 20)

show_heading()
```

```
Traceback (most recent call last):
  File "...", line 6, in <module>
    show_heading()
    ~~~~~~~~~~~~^^
TypeError: show_heading() missing 1 required positional argument: 'room_name'
```

The function promised to need a `room_name`, and the call did not supply one. Read the message like a sentence: the
function name, what is missing, how many, and the exact parameter name. Python names the fix.

Two relatives you will also meet:

Too many arguments:

```
TypeError: show_heading() takes 1 positional argument but 2 were given
```

Calling before the `def` has run:

```python
show_heading("Kitchen")

def show_heading(room_name):
    print(f"== {room_name} ==")
```

```
    show_heading("Kitchen")
    ^^^^^^^^^^^^
NameError: name 'show_heading' is not defined
```

### The one that does not crash: arguments in the wrong order

Swap the arguments to the receipt function:

```python
def print_receipt_line(item, price):
    print(f"{item:<16}${price:>6.2f}")

print_receipt_line(4.5, "Nachos")
```

Here it happens to crash, because a text price cannot be formatted with `.2f`:

```
    print(f"{item:<16}${price:>6.2f}")
                       ^^^^^^^^^^^^^
ValueError: Unknown format code 'f' for object of type 'str'
```

Be grateful when it does. If both parameters took text, say `show_exit(room, direction)`, swapping them would print a
sentence with the words backwards and raise nothing. **Python matches arguments by position, not by meaning.** It has no
idea that `"north"` is a direction.

---

## Why the wrong version is tempting

**The `def` line is far from the call.** When you call `show_heading` on line 140, the parameter list is on line 20, out of
sight. You remember the name, not the parameters.

**Defining feels like doing.** You wrote the function, so it feels like the work happened. Until something calls it, nothing
did.

**Order feels unimportant.** The receipt function takes "an item and a price." Which comes first seems like trivia until the
two are the same type and nothing complains.

---

## What this means for text adventure version 2

Look at version 1 for these three shapes. Each one is a function waiting to happen:

| Shape in version 1 | Function it becomes | Parameters |
|---|---|---|
| The same heading lines printed for every room | `show_heading` | the room name |
| A warning that depends on how many moves are left | `warn_storm` | moves left |
| A message repeated a set number of times | `repeat_message` | the message and the count |

What you **cannot** do yet is move a piece of the game that **changes** state into a function, such as moving to a new room.
That needs a function that hands a value back, and that is tomorrow.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Function** | A named block of code that runs when it is called. |
| **`def`** | The keyword that defines a function. Defining does not run it. |
| **Body** | The indented block of a function. |
| **Parameter** | A name in the `def` line's parentheses, a placeholder for a value. |
| **Argument** | The actual value supplied in a call. |
| **Call** | Running a function by writing its name and parentheses. |
| **Positional argument** | An argument matched to a parameter by its position in the call. |
| **Refactor** | Changing the structure of code without changing what it does. Version 2 is a refactor of version 1. |
| **Outcome 5.3.9** | The WebXam competency for creating and calling functions. |

---

## Self-check

**Question 1.** Write the exact output.

```python
def cheer(team, times):
    for count in range(times):
        print(f"Go {team}")
    print("---")

print("Start")
cheer("Eagles", 2)
cheer("Hawks", 1)
```

**Question 2.** A student defines `def show_exit(room, direction):` and calls `show_exit("north", "lobby")`. What happens, and why
is this worse than a `TypeError`?

**Question 3.** Read this error and say exactly what to change.

```
TypeError: print_score() missing 1 required positional argument: 'points'
```

---

### Answers

**1.**

```
Start
Go Eagles
Go Eagles
---
Go Hawks
---
```

`Start` prints first because the `def` does not run anything. Each call runs the whole body, including the `---`.

**2.** It runs without an error, with `room` tied to `"north"` and `direction` tied to `"lobby"`. Whatever the function prints uses the
two values in the wrong roles. If its body is `print(f"From the {room} you can go {direction}.")`, it prints
`From the north you can go lobby.` It is worse than a `TypeError` because nothing stops the
program, so the wrong output can go unnoticed. Arguments are matched by position, not by meaning.

**3.** The call to `print_score` is missing its `points` argument. Find the call and add the value for `points` in the position where the
`def` line lists it. The `def` line tells you the order.
