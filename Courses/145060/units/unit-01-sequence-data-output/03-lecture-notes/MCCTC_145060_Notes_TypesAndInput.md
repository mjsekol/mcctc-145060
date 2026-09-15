# Lecture Notes: Types and Input
## 145060 Programming · Unit 1 · Week 2 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W02_TypesAndInput.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W02_TypesAndInput.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example, especially the one that does not crash.

**This is the most important file in Unit 1.** Every program you write from here to
the end of the course takes input from somebody. The bug this file describes does not produce an
error message, which means nothing will tell you when you have made it.

---

## Why this exists

Wednesday's programs had the numbers typed into the file. That means the program
answers exactly one question forever. Changing the answer means editing the code,
and only you can do that.

A program becomes useful when somebody else can run it with their own numbers.
That requires asking them, and asking them requires understanding one thing about
what comes back.

---

## The concept in plain language

**Every value in Python has a type.** The type is what kind of thing it is, and it
decides what operations mean.

| Type | What it is | Examples |
|---|---|---|
| `int` | A whole number | `12`, `0`, `-40` |
| `float` | A number with a decimal part | `11.5`, `3.0`, `-0.25` |
| `str` | Text, written in quotes | `"Ava"`, `"12"`, `""` |
| `bool` | True or false | `True`, `False` |

You can ask Python what something is:

```python
print(type(12))        # <class 'int'>
print(type(11.5))      # <class 'float'>
print(type("12"))      # <class 'str'>
```

Look at the last two rows of that table. `12` and `"12"` look almost the same on
the page and are completely different things. One is a quantity. One is two
characters of text that happen to be digits.

### The rule that matters

> **`input()` always hands back a `str`.**
>
> Always. No exceptions. It does not matter what the person typed.

If someone types `12`, you do not have the number 12. You have the text `"12"`.

Converting it is a **separate step that you have to ask for**, and it can fail.

---

## Worked example 1: proving it to yourself

```python
hours = input("How many hours did you work? ")
print("You typed:", hours)
print("Python thinks that is a:", type(hours).__name__)
```

Typing `12`:

```
How many hours did you work? 12
You typed: 12
Python thinks that is a: str
```

`str`. The person typed digits and nothing else, and Python is still holding text.
Run this yourself, because most people do not believe it until they see it.

---

## Worked example 2: converting on purpose

```python
people = int(input("How many people are going? "))
cost_each = 14
total = people * cost_each
print("Total cost:", total, "dollars")
```

Typing `5`:

```
How many people are going? 5
Total cost: 70 dollars
```

`int(...)` wrapped around `input(...)` converts the text to a whole number before
anything is tied to `people`. Read it from the inside out: ask the question, take
the text that comes back, convert it, then attach the name.

For values that can have a decimal part, use `float`:

```python
hours = float(input("Hours worked (decimals allowed): "))
rate = 11.50
print("Pay before taxes:", hours * rate)
```

Typing `7.5`:

```
Hours worked (decimals allowed): 7.5
Pay before taxes: 86.25
```

**Choosing between `int` and `float` is a real decision.** Ask yourself: could this
value reasonably be a half of something? Hours worked, yes. Number of people, no.

---

## Worked example 3: the same value, three operations

```python
count = "3"
print(count * 2)
print(int(count) * 2)
print(count + "2")
```

Output:

```
33
6
32
```

One starting value. Three different answers, and only the middle one is
arithmetic.

- `count * 2` repeats the text twice, giving `"33"`.
- `int(count) * 2` converts to the number 3 and doubles it, giving `6`.
- `count + "2"` glues two pieces of text together, giving `"32"`.

**The type decides what the operator means.** `*` on text is repetition. `*` on
numbers is multiplication. Same symbol, different jobs, and Python picks based on
what it is holding.

---

## The wrong version, and what it does instead of an error

Here is the bug. Read it carefully, because it is going to happen to you.

```python
hours = input("How many hours did you work? ")
print("Three weeks of that is:", hours * 3)
```

Type `12`. Output:

```
How many hours did you work? 12
Three weeks of that is: 121212
```

**No error. No traceback. No red text. A confidently wrong answer.**

Python did exactly what it was told. `hours` is the text `"12"`, and repeating text
three times is a real Python feature that works correctly. You asked for it by
accident.

Now the version that does crash:

```python
hours = "12"
print(hours + 3)
```

```
    print(hours + 3)
          ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

`+` between text and a number is not defined, because there is no single sensible
meaning. It could mean gluing or adding, so Python refuses to guess and stops.

### Write this down

> **The dangerous bugs are the ones that do not crash.**

The `+` version is the better outcome. It failed loudly, at the exact line, and you
fixed it in ten seconds. The `*` version succeeded, handed you garbage, and said
nothing. You find that one weeks later when somebody reports a weird number in your
text adventure, and by then you have no idea which line did it.

An error message is a gift. Something that quietly does the wrong thing is not.

---

## Converting can fail too

Fixing one problem introduces another. `int()` refuses text that does not spell a
whole number.

```python
print(int("abc"))
```

```
ValueError: invalid literal for int() with base 10: 'abc'
```

That one is unsurprising. This one is not:

```python
print(int("11.5"))
```

```
ValueError: invalid literal for int() with base 10: '11.5'
```

`11.5` is a number to you. It is not a **whole** number, and `int()` converts text
that spells a whole number. Use `float("11.5")`, which gives `11.5`.

**What happens when a user types a word into your program and it crashes?** Right
now, nothing good. Handling that properly is Unit 4, and it has a name: error
handling. For now, know that the crash is possible and know which line causes it.

---

## Why the wrong version is tempting

Three reasons, stacked.

**It looks finished.** `hours = input("How many hours did you work? ")` reads like a
complete thought in English. You asked for hours, you got hours. The word "hours"
appears three times and every one of them suggests a quantity.

**Nothing warns you.** Every other mistake you have made so far turned red. This
one produces output that scrolls by and looks approximately like output should look.
If the number is long, you may not even read it.

**The feature is genuinely useful.** String repetition is not a design flaw. It is
how you write `print("-" * 20)` to draw a separator line. Python cannot tell the
difference between you wanting that and you forgetting to convert, because from the
inside those two things are identical.

The defense is a habit, not attention: **convert at the moment you ask.** Wrap
`int()` or `float()` around `input()` on the same line, every time, so there is
never a window where an unconverted value exists.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Type** | What kind of thing a value is. Decides what operations mean. |
| **`int`** | A whole number. |
| **`float`** | A number with a decimal part. |
| **`str`** | Text. Written between quotes. |
| **`bool`** | `True` or `False`. |
| **`input()`** | Asks the user a question. Always returns a `str`. |
| **Prompt** | The text inside `input()` that the user sees. |
| **Type conversion** | Turning a value of one type into another, with `int()` or `float()`. |
| **`int()`** | Converts to a whole number. Fails on text that does not spell one. |
| **`float()`** | Converts to a decimal number. |
| **`str()`** | Converts a value to text. |
| **Concatenation** | Joining two strings with `+`. |
| **String repetition** | Repeating a string with `*` and a whole number. |
| **`TypeError`** | The operation is not defined for those types. |
| **`ValueError`** | The type is right but the value is not usable. |

---

## Self-check

**Question 1.** A user types `25`. Write the exact output, and say whether an error
appears.

```python
amount = input("Amount: ")
print("Tripled:", amount * 3)
```

**Question 2.** Two lines, one crashes and one does not. Say which, quote the error
message, and explain in one sentence why Python treats them differently.

```python
print("12" + 3)
print("12" * 3)
```

**Question 3.** For each value below, say whether you would use `int()`, `float()`,
or no conversion at all, and why.

- The number of people splitting a bill
- Hours worked on a timesheet
- A jersey number
- A student's first name
- The price of a sandwich

---

### Answers

**1.**

```
Amount: 25
Tripled: 252525
```

**No error appears.** `amount` is the text `"25"`, and repeating it three times
gives `"252525"`. This is the bug from the middle of this file. If you expected 75,
the fix is `int(input("Amount: "))`.

**2.** Line 1 crashes:

```
TypeError: can only concatenate str (not "int") to str
```

Line 2 runs and prints `121212`. Python defines `*` between text and a whole number
as repetition, which has one obvious meaning. It does not define `+` between text
and a number, because that could mean gluing or adding, and rather than guess,
Python stops.

**3.**

| Value | Conversion | Why |
|---|---|---|
| People splitting a bill | `int()` | There is no such thing as 2.5 people. |
| Hours worked | `float()` | 7.5 hours is a real timesheet entry. |
| Jersey number | none | It is a label, not a quantity. You never do arithmetic on it, and `07` should keep its zero. |
| First name | none | It is text and there is nothing to convert it to. |
| Price of a sandwich | `float()` | `4.99` needs the decimal part. |

The jersey number is the one worth arguing about, and it is the most useful item in
the table. It is written with digits, so converting it feels natural. Ask the test
question: **would I ever add two of these together?** If adding two jersey numbers
is meaningless, it is not a quantity, and it stays text. The same reasoning applies
to phone numbers, zip codes, and student ID numbers.
