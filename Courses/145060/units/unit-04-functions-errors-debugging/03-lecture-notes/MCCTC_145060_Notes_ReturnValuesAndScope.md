# Lecture Notes: Return Values and Local Scope
## 145060 Programming · Unit 4 · Week 8 · Thursday, October 29

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W08_ReturnValuesAndScope.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W08_ReturnValuesAndScope.pptx)

If you missed class, you can learn this concept from this file alone. Read Wednesday's notes,
[Defining Functions with Parameters](MCCTC_145060_Notes_DefiningFunctions.md), first. Today's most
important bug prints the word `None` where a number should be, or quietly refuses every correct
answer, and does not crash.

---

## Why this exists

Every function you wrote yesterday did its job by **printing**. That works for a heading. It does not
work for a tip calculator whose answer you need to add to a bill, or for a check that decides whether a
frequency is on the dial, or for working out which room a player moves into.

Those functions need to **hand an answer back** to the line that called them, so the rest of the program
can use it. That is `return`.

And the moment functions hold their own variables, a question you have never had to ask becomes important:
**where does a variable exist?** A variable made inside a function belongs to that function and disappears
when the call ends. That is **scope**. Getting it wrong produces one error you will see constantly in text
adventure version 2, and today you learn to read it.

Outcomes: 5.3.9, **write code that creates and calls functions**, and 5.2.2, **identify the scope of data
(global versus local)**.

---

## The concept in plain language

```python
def function_name(parameters):
    # work
    return value     # hand value back to the caller, and end the call right here

result = function_name(arguments)   # the call is replaced by the returned value
```

- **`return value`** ends the call immediately and sends `value` back.
- **The call becomes its return value.** In `result = tip_amount(40, 18)`, once the call finishes, Python treats
  the right side as if you had typed the number that came back.
- **A function with no `return` still returns something.** It returns the special value **`None`**, which means
  "no value." Python does this silently.

**Scope:**

- A variable assigned **inside** a function, including every parameter, is **local**. It exists only while that call
  runs.
- A variable assigned at the top level of the file, outside every function, is **global**. A function can **read** it.
- If a function **assigns** to a name anywhere in its body, Python treats that name as local for the **whole** body.

---

## Worked example 1: return hands a value back

```python
# return hands a value back to the line that called the function.
def tip_amount(bill, tip_percent):
    return bill * tip_percent / 100

tip = tip_amount(40, 18)
print(f"Tip: ${tip:.2f}")
print(f"Total: ${40 + tip:.2f}")
print(f"Split four ways: ${(40 + tip_amount(40, 18)) / 4:.2f}")
```

```
Tip: $7.20
Total: $47.20
Split four ways: $11.80
```

The function prints nothing. The **caller** decides what to do with the answer: store it, add it, format it, or use the
call directly inside a larger expression, as the last line does. That is the whole advantage over printing. A printed
value is finished. A returned value can keep being used.

---

## Worked example 2: returning True or False

```python
# A function can return True or False, so a loop or an if can ask it a question.
LOWEST_FREQUENCY = 530
HIGHEST_FREQUENCY = 1700

def is_on_dial(text):
    if not text.isdecimal():
        return False
    frequency = int(text)
    return frequency >= LOWEST_FREQUENCY and frequency <= HIGHEST_FREQUENCY

print(is_on_dial("880"))
print(is_on_dial("2000"))
print(is_on_dial("loud"))
```

```
True
False
False
```

Now Week 7's validation guard has a name. `if is_on_dial(frequency_text):` reads like English. Notice two things:

- **`return False` on the first check ends the call.** `int(text)` never runs for `"loud"`, so it can never crash. An early
  `return` works like `break` for a function.
- **The function reads `LOWEST_FREQUENCY` and `HIGHEST_FREQUENCY`** from the top of the file. Reading a global constant inside a
  function is fine, and it is how constants are meant to be used.

---

## Worked example 3: return ends the function

```python
# return ends the function immediately. Nothing after it runs.
def grade_letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    return "not an A or B"
    print("This line never runs")

print(grade_letter(93))
print(grade_letter(85))
print(grade_letter(71))
```

```
A
B
not an A or B
```

For 93, `return "A"` ends the call, so the `score >= 80` check never happens. That is why these can be plain `if` lines instead
of `elif`: a `return` already guarantees only one runs. The last `print` is unreachable. Python allows it and never runs it.

---

## Worked example 4: a function that works out the next state

Yesterday's notes said moving between rooms could not become a function yet. Now it can.

```python
# A function can compute the next state and hand it back.
def destination_from(room, direction):
    if room == "lobby" and direction == "north":
        return "hallway"
    if room == "hallway" and direction == "south":
        return "lobby"
    if room == "hallway" and direction == "west":
        return "studio"
    if room == "studio" and direction == "east":
        return "hallway"
    return ""

room = "lobby"
next_room = destination_from(room, "north")
print(f"From the lobby, north leads to: {next_room}")
print("From the lobby, west leads to:", repr(destination_from(room, "west")))
```

```
From the lobby, north leads to: hallway
From the lobby, west leads to: ''
```

The function does not change `room`. It **answers a question** about `room`, and the game loop decides whether to use the
answer. That separation, functions that compute and a loop that stores, is the shape of text adventure version 2.

---

## Local scope: variables that live inside a call

```python
# A variable created inside a function is local. It exists only during the call.
def tip_amount(bill, tip_percent):
    tip = bill * tip_percent / 100
    return tip

result = tip_amount(40, 18)
print(result)
print(tip)
```

```
7.2
Traceback (most recent call last):
  File "...", line 8, in <module>
    print(tip)
          ^^^
NameError: name 'tip' is not defined. Did you mean: 'zip'?
```

`tip` existed while `tip_amount` was running, and disappeared when it returned. Only the **value** came back, tied to the name
`result`. Notice the suggestion, `zip`: Python matched the spelling against a built-in name and guessed wrong. A suggestion is a
spelling match, not understanding.

A local name can even match a global name without touching it:

```python
def show_total(price, quantity):
    total = price * quantity
    print(f"Inside: total is {total}")

total = 100
show_total(4, 3)
print(f"Outside: total is still {total}")
```

```
Inside: total is 12
Outside: total is still 100
```

Two different variables that happen to share a name. Parameters work the same way:

```python
# A parameter is a local variable too. Changing it does not change the caller's variable.
def add_move(moves):
    moves = moves + 1
    print(f"Inside the function: {moves}")

moves = 5
add_move(moves)
print(f"Outside the function: {moves}")
```

```
Inside the function: 6
Outside the function: 5
```

---

## The scope error you will meet in version 2

You move the move counter into a function, and the function adds to the global `moves`:

```python
# Reading a constant from outside is fine. Assigning to an outside name is not.
MAX_MOVES = 20
moves = 0

def take_step():
    moves = moves + 1
    print(f"Moves left: {MAX_MOVES - moves}")

take_step()
```

```
Traceback (most recent call last):
  File "...", line 9, in <module>
    take_step()
    ~~~~~~~~~^^
  File "...", line 6, in take_step
    moves = moves + 1
            ^^^^^
UnboundLocalError: cannot access local variable 'moves' where it is not associated with a value
```

**Read the rule from the top of this file.** The body assigns to `moves`, so Python treats `moves` as local for the whole body. On the
right side of that same line, the local `moves` has no value yet. Reading `MAX_MOVES` is fine, because the body never assigns to it.

**The fix is to pass the value in and return the new value**, and let the caller store it:

```python
# The fix: pass the value in, return the new value, and let the caller store it.
MAX_MOVES = 20

def take_step(moves):
    moves = moves + 1
    print(f"Moves left: {MAX_MOVES - moves}")
    return moves

moves = 0
moves = take_step(moves)
moves = take_step(moves)
print(f"Moves taken: {moves}")
```

```
Moves left: 19
Moves left: 18
Moves taken: 2
```

`moves = take_step(moves)` is the pattern for state in version 2: hand the current value in, get the new value back, store it.

---

## The wrong version: the function that returns None silently

This is the bug of the day. A student writes the tip function the way they wrote Wednesday's functions, by printing:

```python
def tip_amount(bill, tip_percent):
    tip = bill * tip_percent / 100
    print(f"Tip: ${tip:.2f}")

tip = tip_amount(40, 18)
print(f"Tip saved for later: {tip}")
print(f"Total: {40 + tip}")
```

```
Tip: $7.20
Tip saved for later: None
Traceback (most recent call last):
  File "...", line 7, in <module>
    print(f"Total: {40 + tip}")
                    ~~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

The first line looks perfect. The function **printed** the tip, so it looks like it worked. But it has no `return`, so the call handed
back `None`, and `None` got tied to `tip`. The second line printed the word `None` **and did not crash.** Only the third line, which
does arithmetic, finally failed. If the program had never added anything, nothing would ever have told you.

**The version that never crashes is worse.** Forget the `return` in the dial check:

```python
LOWEST_FREQUENCY = 530
HIGHEST_FREQUENCY = 1700

def is_on_dial(text):
    if not text.isdecimal():
        return False
    frequency = int(text)
    frequency >= LOWEST_FREQUENCY and frequency <= HIGHEST_FREQUENCY

typed = input("Frequency: ").strip()
if is_on_dial(typed):
    print("Tuning in.")
else:
    print("The dial does not go there.")
print("is_on_dial gave back:", is_on_dial(typed))
```

Typing `1470`, a frequency that is definitely on the dial:

```
Frequency: 1470
The dial does not go there.
is_on_dial gave back: None
```

The comparison on the last line of the function is worked out and thrown away. The function reaches its end, returns `None`, and an `if`
treats `None` like False. **Every correct frequency is refused, forever, with no error.** In a game, the player can never win and nothing
says why.

This is the same bug this course has been showing you since Week 2, in its newest form. `"12" * 3` gave `121212`. `code[5:8]` gave
`202`. A loop ran one time too few. **The dangerous bugs are the ones that do not crash**, and a function that returns `None` silently is
one of the most common of them.

**The habit that catches it:** the first time you call a new function, print what it returns, the way the last line above does. If you
see `None` and you expected a value, look for the missing `return`.

---

## Why the wrong version is tempting

**Printing looks like returning.** The value appears on the screen, so it feels like the function produced it. The screen is not the caller.

**Yesterday's functions all printed.** Every function you had written ended with a `print`, so the habit is one day old and already strong.

**`None` is quiet.** It prints as a word, it is False in an `if`, and nothing about it announces a mistake until arithmetic touches it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **`return`** | Ends a function call and sends a value back to the caller. |
| **Return value** | The value a call hands back. The call expression becomes this value. |
| **`None`** | Python's value for "no value." Returned silently by any function that ends without `return`. |
| **Scope** | The part of a program where a variable exists and can be used. |
| **Local variable** | A variable assigned inside a function, including parameters. It exists only during the call. |
| **Global variable** | A variable assigned at the top level of the file. Functions can read it. |
| **`UnboundLocalError`** | A function used a local variable on a line before that variable had a value. |
| **Outcome 5.2.2** | The WebXam competency for the scope of data, global versus local. |

---

## Self-check

**Question 1.** Write the exact output.

```python
def double(number):
    number = number * 2
    return number

value = 5
result = double(value)
print(value, result)
print(double(double(3)))
```

**Question 2.** A student's function runs, prints the right number on the screen, and the next line of their program prints `None`. What is missing
and where?

**Question 3.** Explain in two sentences why this function raises `UnboundLocalError`, then rewrite it and the call so it works.

```python
score = 0

def add_points(points):
    score = score + points

add_points(10)
```

---

### Answers

**1.**

```
5 10
12
```

`number` is local, so doubling it does not change `value`, which stays 5. The inner `double(3)` returns 6, and `double(6)` returns 12.

**2.** The function has no `return` statement. It printed its answer instead of returning it, so the call handed back `None`, which is what the next
line printed. Add `return` with the value at the end of the function, and remove the `print` inside it if the caller is the one who should display it.

**3.** The body assigns to `score`, so Python treats `score` as a local variable for the whole function. The right side of `score = score + points` reads
that local `score` before it has a value, so Python stops.

```python
def add_points(score, points):
    return score + points

score = 0
score = add_points(score, 10)
print(score)
```

This prints `10`. The current score goes in, the new score comes back, and the caller stores it.
