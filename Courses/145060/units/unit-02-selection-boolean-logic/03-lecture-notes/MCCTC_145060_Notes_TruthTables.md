# Lecture Notes: Truth Tables
## 145060 Programming · Unit 2 · Week 5 · Wednesday, October 7

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W05_TruthTables.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W05_TruthTables.pptx)

If you missed class, you can learn this concept from this file alone. You need paper for
this one. Build every table by hand first, then check it with Python. The skill being
tested on the WebXam is building the table, not running the code.

---

## Why this exists

Yesterday you joined conditions with `and`, `or`, and `not`. A condition with two or three
parts can be True or False in several different situations, and you cannot hold all of
them in your head at once.

A **truth table** is a list of every possible situation and the answer in each one. It
does three jobs:

1. It shows you exactly when a compound condition is True. No guessing.
2. It tells you whether two conditions that look different actually mean the same thing.
3. **It is a complete test plan.** Every row is one test case. If your program gives the
   right answer on every row, you have tested every combination there is.

That third job is why a working programmer cares. It is also why outcome 5.3.2 on the
WebXam is literally "solve a truth table."

---

## The concept in plain language

A truth table has one column for each input, one column for each result you care about,
and one row for every combination of True and False the inputs can take.

### How many rows

Each input has two possible values. Every input you add doubles the number of rows.

| Inputs | Rows |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |

You have seen this before. Week 4's bell ringer asked how many arrangements eight light
switches can make, and the answer was 256, because each switch doubles the count. A truth
table is that same counting problem.

### How to fill in the input columns without missing a row

Count in binary, with True as 1 and False as 0. For two inputs: 11, 10, 01, 00. That gives
the order TT, TF, FT, FF, and it guarantees you did not skip or repeat a row.

For three inputs, the first column changes every four rows, the second every two rows, and
the third every row.

### The three basic tables

**and**

| A | B | A and B |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**or**

| A | B | A or B |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**not**

| A | not A |
|---|---|
| True | False |
| False | True |

The shortcut worth memorizing: **`and` is True in exactly one row. `or` is False in exactly
one row.**

---

## Worked example 1: a two-input table, by hand

Build the table for `A and not B`.

Add a helper column for the part inside, `not B`, then combine.

| A | B | not B | A and not B |
|---|---|---|---|
| True | True | False | False |
| True | False | True | True |
| False | True | False | False |
| False | False | True | False |

Check it with Python. Each line below is one row, with the values typed in:

```python
print(True and not True)
print(True and not False)
print(False and not True)
print(False and not False)
```

Output:

```
False
True
False
False
```

The four lines match the last column. **Helper columns are not optional on hard tables.**
They are where your mistakes become visible.

---

## Worked example 2: three inputs, a real rule

You can go to the party if your homework is done **and** your parents said yes, **or** if it
is a holiday.

```python
homework_done = True
parents_said_yes = False
is_holiday = True

can_go = (homework_done and parents_said_yes) or is_holiday
print("Can go to the party:", can_go)
```

Output:

```
Can go to the party: True
```

That run is one row. Here is the whole table. `H` is homework done, `P` is parents said yes,
`V` is holiday.

| H | P | V | H and P | (H and P) or V |
|---|---|---|---|---|
| True | True | True | True | True |
| True | True | False | True | True |
| True | False | True | False | True |
| True | False | False | False | False |
| False | True | True | False | True |
| False | True | False | False | False |
| False | False | True | False | True |
| False | False | False | False | False |

Eight rows, because three inputs. Read the answer column and a pattern appears: **every
holiday row is True.** That is what the `or V` means.

Now move the parentheses: `H and (P or V)`. The rows change. With homework **not** done on a
holiday, the first version says you can go and the second says you cannot. Same three
words, same order, different meaning. Build the second table yourself and you find exactly
two rows where they disagree, `False True True` and `False False True`. Both are a holiday
with homework not done, and in both the program would give somebody the wrong answer.

---

## Worked example 3: are these two conditions the same

Outdoor practice happens when it is warm **and** dry. Your coach wants a program that says
when practice is cancelled. The honest version is "not warm-and-dry":

```python
is_warm = True
is_dry = False

cancel_practice = not (is_warm and is_dry)
print("Cancel practice:", cancel_practice)
```

```
Cancel practice: True
```

Warm and raining, so cancelled. Correct.

Here is a table comparing it with two ways people try to "simplify" it by pushing the `not`
inside. `W` is warm, `D` is dry.

| W | D | not (W and D) | not W and not D | not W or not D |
|---|---|---|---|---|
| True | True | False | False | False |
| True | False | True | **False** | True |
| False | True | True | **False** | True |
| False | False | True | True | True |

The third column matches the first in every row. The second column does not.

**The rule, called De Morgan's law:** when you push `not` inside parentheses, **`and` becomes
`or`, and `or` becomes `and`.**

- `not (W and D)` is the same as `not W or not D`
- `not (W or D)` is the same as `not W and not D`

You do not need to memorize the name. You need to know that the operator flips, and you
need to know how to prove it: build the table.

---

## The wrong version: a simplification that does not crash

```python
is_warm = True
is_dry = False

cancel_practice = not is_warm and not is_dry
print("Cancel practice:", cancel_practice)
```

```
Cancel practice: False
```

**No error. The team practices outside in the rain.**

This is the second column of the table above. It only cancels practice when it is cold
**and** wet. On a warm rainy day, and on a cold dry day, it says practice is on. Two of the
four rows are wrong, and the row you probably tested, a cold rainy day, is right.

Seventh appearance of the shape this course keeps showing you. The code ran. It printed
something that looks like an answer. It was wrong, and a table with four rows would have
found it in two minutes.

The correct simplification flips the operator:

```python
cancel_practice = not is_warm or not is_dry
```

```
Cancel practice: True
```

### The mistake that does crash

```python
print(true and false)
```

```
    print(true and false)
          ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
```

`True` and `False` are capitalized in Python. Lowercase `true` is a name nobody
defined. On paper you may write T and F. In code you write `True` and `False`.

---

## Why the wrong version is tempting

**It looks like algebra.** In math, a minus sign distributes: `-(a + b)` is `-a - b`, and the
plus stays a plus. People expect `not` to distribute the same way and leave `and` alone. It
does not. The operator flips.

**It sounds right out loud.** "Not warm and not dry" sounds like a reasonable description of
bad weather. It describes one specific kind of bad weather.

**It passes the obvious test.** The first situation anyone tries for "cancel practice" is a
cold rainy day, and the wrong version gets that row right.

**The defense is a habit.** Any time you rewrite a condition to make it "simpler," build a
table for the old version and the new version side by side. If a single row differs, they
are not the same condition, and the rewrite is a bug.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Truth table** | A table listing every combination of inputs and the result of a condition for each. |
| **Row** | One combination of input values. One row is one test case. |
| **Helper column** | A column for part of a condition, filled in before the whole condition. |
| **Boolean logic** | Reasoning with values that are only True or False, using and, or, and not. |
| **Equivalent conditions** | Two conditions whose truth tables match in every row. |
| **De Morgan's law** | Pushing `not` into parentheses flips `and` to `or` and `or` to `and`. |
| **2 to the n** | The number of rows for n inputs. Three inputs, 2 times 2 times 2, is 8 rows. |

---

## Self-check

**Question 1.** Build the full truth table for `has_id and (is_member or not is_banned)`.
Use helper columns. How many rows are True?

**Question 2.** A student says `not (is_tired or is_sick)` means the same thing as
`not is_tired or not is_sick`. Prove whether they are right with a truth table, and if they
are wrong, give the correct equivalent.

**Question 3.** A condition has four inputs. How many rows does its truth table have, and
what is the fastest way to be sure you did not skip one?

---

### Answers

**1.** Eight rows, because three inputs. `I` is has_id, `M` is is_member, `B` is is_banned.

| I | M | B | not B | M or not B | I and (M or not B) |
|---|---|---|---|---|---|
| True | True | True | False | True | True |
| True | True | False | True | True | True |
| True | False | True | False | False | False |
| True | False | False | True | True | True |
| False | True | True | False | True | False |
| False | True | False | True | True | False |
| False | False | True | False | False | False |
| False | False | False | True | True | False |

**Three rows are True**, all of them with `has_id` True. Every row without an ID is False,
because `and` needs both sides. Verified by evaluating all eight rows in Python.

**2.** The student is wrong.

| T | S | not (T or S) | not T or not S |
|---|---|---|---|
| True | True | False | False |
| True | False | False | **True** |
| False | True | False | **True** |
| False | False | True | True |

Two rows differ. When pushing `not` inside, `or` must flip to `and`. The correct equivalent is
`not is_tired and not is_sick`, which is True only in the last row, matching the first column.

**3.** Sixteen rows, because 2 times 2 times 2 times 2 is 16. The fastest way to be sure is to
count in binary from 1111 down to 0000, writing 1 as True and 0 as False. The first column
switches every eight rows, the second every four, the third every two, and the last every row.
