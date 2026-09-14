# Lecture Notes: Comparisons, Booleans, and if/else
## 145060 Programming · Unit 2 · Week 4 · Thursday, October 1

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W04_BooleansAndIf.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W04_BooleansAndIf.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example. Run each one with at least two different inputs, because a program with a
fork in it has more than one path, and you have only tested the paths you ran.

---

## Why this exists

Every program you have written so far is a straight line. Line 1 runs, then line 2,
then line 3, every time, for everybody.

That is why your CLI Toolsmith prints a sentence like "a number above 100 means the
target is out of reach." The program cannot tell whether the number is above 100. It
hands that job to the person reading the output.

Real programs make decisions. Your phone warns you at low battery and stays quiet at
80 percent. A game says "new high score" only when you beat the old one. A ticket
site charges one price for a child and another for an adult. All of those are the
same idea: **ask a question, then do one thing or another based on the answer.**

---

## The concept in plain language

### Part 1: a comparison is a question with a True or False answer

Python has six comparison operators. Each one asks a yes-or-no question about two
values.

| Operator | Question it asks | Example | Result |
|---|---|---|---|
| `==` | Are these equal? | `7 == 7` | `True` |
| `!=` | Are these different? | `7 != 10` | `True` |
| `<` | Is the left smaller? | `7 < 5` | `False` |
| `>` | Is the left bigger? | `7 > 5` | `True` |
| `<=` | Is the left smaller or equal? | `7 <= 7` | `True` |
| `>=` | Is the left bigger or equal? | `7 >= 8` | `False` |

The answer is a value, and that value has a type. You met the type in Week 2 and
have not needed it until now: `bool`. A `bool` holds exactly one of two values,
`True` or `False`, with capital letters and no quotes.

```python
score = 7
print(score > 5)
print(score == 10)
print(score != 10)
print(score <= 7)
print(type(score > 5))
```

Output:

```
True
False
True
True
<class 'bool'>
```

`score > 5` is not a statement. It is a question, and Python answers it.

### Part 2: `if` runs a block only when the answer is True

```python
if battery < 20:
    print("Plug in your phone before practice.")
```

Read it out loud as English: **if** battery is less than 20, **then** do the indented
part. The colon at the end of the `if` line says "the block starts here." The
indentation says what is inside the block.

`else` gives the other path. It has no condition of its own. It runs when the `if`
condition was False.

### Part 3: indentation is not decoration

In most of what you have typed so far, spacing was about looks. Here it is meaning.
**The indented lines are inside the `if`. The first line that is not indented is
outside it, and runs no matter what.**

VS Code indents with four spaces when you press Tab. Use that. Do not mix tabs and
spaces by hand.

### The rule to write down

> **One equals assigns. Two equals asks.**
>
> `score = 7` puts 7 into `score`. `score == 7` asks whether `score` is 7.

---

## Worked example 1: the battery warning

```python
battery = int(input("Battery percent: "))

if battery < 20:
    print("Plug in your phone before practice.")
    print("It will not survive the bus ride home.")
else:
    print("You are fine for now.")

print("Battery check done.")
```

Typing `12`:

```
Battery percent: 12
Plug in your phone before practice.
It will not survive the bus ride home.
Battery check done.
```

Typing `64`:

```
Battery percent: 64
You are fine for now.
Battery check done.
```

Typing `20`:

```
Battery percent: 20
You are fine for now.
Battery check done.
```

**Look at the third run.** Exactly 20 percent took the `else` path, because 20 is
not less than 20. Whether the boundary value belongs on one side or the other is a
decision you make with `<` or `<=`. Nobody makes it for you. Always test the exact
boundary number, not only a number far from it.

The last line, `Battery check done.`, printed in every run. It is not indented, so it
is not inside either block.

---

## Worked example 2: comparing text

Comparisons work on strings too. `==` asks whether two strings are exactly the same,
character for character.

```python
answer = input("Are you coming to the game? ")

if answer == "yes":
    print("See you at 7.")
else:
    print("Okay, maybe next time.")
```

Typing `yes`:

```
Are you coming to the game? yes
See you at 7.
```

Typing `Yes`:

```
Are you coming to the game? Yes
Okay, maybe next time.
```

**Your friend said yes and the program heard no.** `"Yes"` and `"yes"` are different
strings, because `Y` and `y` are different characters. Nothing crashed.

You already own the fix from Week 3. Clean the text before you compare it:

```python
answer = input("Are you coming to the game? ").strip().lower()

if answer == "yes":
    print("See you at 7.")
else:
    print("Okay, maybe next time.")
```

Typing `  Yes ` with stray spaces:

```
Are you coming to the game?   Yes 
See you at 7.
```

**Clean first, compare second.** You will write that pattern for the rest of the year.

---

## Worked example 3: making your CLI Toolsmith smarter

Your final-grade style tool prints a number and leaves the reader to judge it. Now
the program can judge it.

```python
needed = 104.5
if needed > 100:
    print("That target is out of reach this semester.")
else:
    print(f"You need {needed:.1f}% on the final.")
```

Output:

```
That target is out of reach this semester.
```

Change `needed` to `91.25` and run it again. You get `You need 91.2% on the final.`
This is exactly the kind of condition your CLI Toolsmith Build 2 asks you to add
today: replace a sentence that tells a human to check something with a condition that
checks it.

---

## The wrong versions, and the exact errors

### Wrong 1: one equals where you meant two

```python
score = 7
if score = 7:
    print("yes")
```

```
    if score = 7:
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Python names the fix. `=` is an instruction to store something, and an `if` needs a
question. Ignore the `:=` in the message. That operator exists and it is not part of
this course.

### Wrong 2: forgetting the colon

```python
score = 7
if score == 7
    print("yes")
```

```
    if score == 7
                 ^
SyntaxError: expected ':'
```

### Wrong 3: forgetting to indent

```python
score = 7
if score == 7:
print("yes")
```

```
    print("yes")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

### Wrong 4: comparing text to a number

```python
age = input("How old are you? ")
if age >= 16:
    print("You can take the driving test.")
```

Typing `17`:

```
    if age >= 16:
       ^^^^^^^^^
TypeError: '>=' not supported between instances of 'str' and 'int'
```

`input()` always hands back a `str`. That was Week 2's rule and it did not stop being
true. Python refuses to decide whether the text `"17"` is bigger than the number 16.
The fix is the same habit: `age = int(input("How old are you? "))`.

### Wrong 5: the one that does not crash

**This is the most important example in the file.**

```python
my_score = input("Your score: ")
best_score = input("Best score so far: ")

if my_score > best_score:
    print("New high score.")
else:
    print("Not this time.")
```

Typing `9`, then `10`:

```
Your score: 9
Best score so far: 10
New high score.
```

**No error. Nine beat ten.**

Both values are strings, so Python is allowed to compare them, and it compares text
the way a dictionary sorts words: one character at a time, from the left. The first
character of `"9"` is `9`. The first character of `"10"` is `1`. The character `9`
comes after `1`, so `"9"` counts as bigger, and Python never looks further.

Wrong 4 crashed because a string and a number cannot be compared. Wrong 5 did not
crash because two strings can. **The one that crashed was the lucky one.**

This is the fourth time this course has shown you this shape. `"12" * 3` gave
`121212`. A headcount of 2.5 people was accepted. `code[5:8]` gave `202`. Now `"9"`
beats `"10"`. None of them produced an error.

> **The dangerous bugs are the ones that do not crash.**

The fix is to convert both values with `int()` at the moment you ask for them.

### Wrong 6: an indentation mistake that also does not crash

```python
battery = int(input("Battery percent: "))

if battery < 20:
    print("Plug in your phone before practice.")
    print("It will not survive the bus ride home.")
else:
    print("You are fine for now.")
    print("Battery check done.")
```

Typing `12`:

```
Battery percent: 12
Plug in your phone before practice.
It will not survive the bus ride home.
```

The last line got four extra spaces, so it moved inside the `else`. Now the check
only says it is done when the battery is fine. Python did exactly what the spaces
told it to do.

---

## Why the wrong versions are tempting

**`=` has meant "equals" your whole life.** In math class, `x = 7` is a question you
check. In Python, it is an order. Your hands will type one equals sign for about three
weeks after your head knows better. The error message is there to catch it.

**Text that looks like a number feels like a number.** `"9"` and `"10"` on your screen
look like quantities. Python sees characters. The only defense is converting at the
moment you ask, every time, which is the Week 2 habit.

**Indentation looks like formatting.** In an essay, an indent is style. In Python, an
indent is a decision about which lines are inside the fork. Read your indentation as
carefully as your words.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Comparison operator** | `==`, `!=`, `<`, `>`, `<=`, `>=`. Asks a question about two values. |
| **Relational operator** | Another name for a comparison operator. The WebXam uses this term. |
| **Boolean** | A value that is either `True` or `False`. Named after George Boole. |
| **`bool`** | Python's type for Boolean values. |
| **Condition** | An expression whose answer is `True` or `False`, used to make a decision. |
| **`if`** | Runs its block only when its condition is `True`. |
| **`else`** | Runs its block only when the `if` condition was `False`. |
| **Block** | The indented lines that belong to an `if` or `else`. |
| **Indentation** | The spaces at the start of a line. In Python it decides what is inside a block. |
| **Selection** | The general idea of a program choosing a path. Also called a conditional. |
| **Boundary value** | The exact number where a condition flips, such as 20 in `battery < 20`. |

---

## Self-check

**Question 1.** Write the exact output. Four lines.

```python
laps = 12
print(laps >= 12)
print(laps != 12)
print(laps == "12")
print(type(laps < 3))
```

**Question 2.** A student types `8` at the first prompt and `12` at the second. Write
what the program prints, state whether an error appears, and give the one change that
fixes it.

```python
hours_this_week = input("Hours this week: ")
hours_last_week = input("Hours last week: ")
if hours_this_week > hours_last_week:
    print("You worked more this week.")
else:
    print("You worked less or the same.")
```

**Question 3.** Your phone should warn you when the battery is **at or below** 15
percent. A classmate wrote `if battery < 15:`. Which battery value proves the
classmate wrong, and what is the corrected line?

---

### Answers

**1.**

```
True
False
False
<class 'bool'>
```

The third line is the one worth a second look. `laps` is the number 12 and `"12"` is
text, so they are not equal. Python does not crash when you ask whether a number and
a string are equal. It answers `False`. Only the ordering operators such as `<` and
`>=` refuse to compare a string with a number.

**2.** It prints `You worked more this week.` and **no error appears**. Both values
are strings. `"8"` is compared to `"12"` one character at a time, and `8` comes after
`1`, so `"8"` counts as bigger. The fix is converting both at the moment you ask:
`hours_this_week = int(input("Hours this week: "))` and the same for the second line.
`float()` also works and allows half hours.

**3.** The value `15` proves it wrong. `15 < 15` is `False`, so the phone stays quiet
at exactly 15 percent, which the requirement says should warn. The corrected line is
`if battery <= 15:`. The boundary value is the only test that catches this, which is
why you always run the exact boundary number.
