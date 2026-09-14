# Lecture Notes: and, or, not
## 145060 Programming · Unit 2 · Week 5 · Tuesday, October 6

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W05_LogicalOperators.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W05_LogicalOperators.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example. The two most important examples in this file are the one that gives every
day of the week a weekend, and the one that avoids a crash by putting a check first.

---

## Why this exists

Real rules are rarely one question. You can go to the concert if you have a ticket
**and** a ride. You can sleep in if it is Saturday **or** Sunday. You get no video games
if your homework is **not** done.

You could build every one of those with `if` statements inside other `if` statements.
It gets ugly fast, and Thursday is about why. Python gives you three words that join
conditions into one bigger condition: `and`, `or`, and `not`. These are called
**logical operators**, and the WebXam uses that exact term.

---

## The concept in plain language

| Operator | The combined condition is True when | Example |
|---|---|---|
| `and` | **both** sides are True | `has_ticket and has_ride` |
| `or` | **at least one** side is True | `day == "saturday" or day == "sunday"` |
| `not` | the one thing after it is **False** | `not homework_done` |

`and` and `or` sit between two conditions. `not` goes in front of one.

```python
has_ticket = True
has_ride = False

print(has_ticket and has_ride)
print(has_ticket or has_ride)
print(not has_ride)

if has_ticket and has_ride:
    print("You are going to the concert.")
else:
    print("Not tonight.")
```

Output:

```
False
True
True
Not tonight.
```

A ticket with no ride means you are not going. That is `and`. It needs everything.

### Order of operations

Multiplication happens before addition, and logical operators have an order too:
**`not` first, then `and`, then `or`.** When a condition mixes `and` and `or`, use
parentheses to say what you mean. Parentheses cost nothing and they prevent the bug in
worked example 4.

### Short-circuiting

Python reads a logical condition **left to right and stops as soon as it knows the
answer.**

- For `and`: if the left side is False, the whole thing must be False. Python does not
  even look at the right side.
- For `or`: if the left side is True, the whole thing must be True. Python skips the
  right side.

That sounds like a speed detail. It is actually a safety tool, and worked example 3
shows why.

---

## Worked example 1: sleeping in

```python
day = input("What day is it? ").strip().lower()

if day == "saturday" or day == "sunday":
    print("Sleep in.")
else:
    print("Alarm is set for 6:45.")
```

```
What day is it? Sunday
Sleep in.
```

```
What day is it? monday
Alarm is set for 6:45.
```

**Each side of `or` is a complete comparison.** `day == "saturday"` is one question.
`day == "sunday"` is another. `or` joins two questions, not two words.

---

## Worked example 2: not

```python
homework_done = False
if not homework_done:
    print("No video games until it is done.")
chores_done = True
if homework_done and chores_done:
    print("Go ahead.")
if not (homework_done and chores_done):
    print("Something is still not done.")
```

Output:

```
No video games until it is done.
Something is still not done.
```

`not homework_done` reads like English. When a variable is already a `bool`, you do not
compare it to `True` or `False`. Write `if homework_done:`, not
`if homework_done == True:`.

The last `if` puts `not` in front of a whole parenthesized condition. It means "it is
not the case that both are done." Tomorrow's truth tables show exactly when that is True.

---

## Worked example 3: short-circuiting prevents a crash

You and some friends split a pizza. You want to know whether everyone pays ten dollars
or less.

```python
bill = float(input("Pizza bill: "))
people = int(input("How many people are paying? "))

if people > 0 and bill / people <= 10:
    print("Everyone pays ten dollars or less.")
else:
    print("Either nobody is paying or it costs more than ten each.")
```

```
Pizza bill: 36
How many people are paying? 4
Everyone pays ten dollars or less.
```

```
Pizza bill: 36
How many people are paying? 0
Either nobody is paying or it costs more than ten each.
```

With `0` people, `people > 0` is False. Because it is an `and`, Python already knows the
answer is False, and it **never runs** `bill / people`. That division would have been a
division by zero.

Now swap the two sides:

```python
if bill / people <= 10 and people > 0:
```

```
    if bill / people <= 10 and people > 0:
       ~~~~~^~~~~~~~
ZeroDivisionError: float division by zero
```

Same two conditions. Different order. One crashes. **Put the check that protects
something on the left.**

The same trick protects string indexing from Week 3:

```python
nickname = input("Nickname (Enter to skip): ").strip()
if nickname != "" and nickname[0] == "x":
    print("Edgy.")
else:
    print("Okay.")
```

Pressing Enter with nothing typed prints `Okay.` Swap the two sides, and the empty
nickname reaches `nickname[0]` first:

```
    if nickname[0] == "x" and nickname != "":
       ~~~~~~~~^^^
IndexError: string index out of range
```

---

## Worked example 4: mixing and with or

A store gives a discount to members or anyone with a coupon, **but only on a total over
$20.**

```python
is_member = True
has_coupon = False
total = 18.00

print(is_member or has_coupon and total > 20)
print((is_member or has_coupon) and total > 20)
```

Output:

```
True
False
```

The first line gives a member a discount on an $18.00 order. **No error.** Because `and`
happens before `or`, Python read it as `is_member or (has_coupon and total > 20)`. A
member skips the total check entirely.

The second line says what the store meant. Parentheses first, then `and`.

---

## The wrong versions

### Wrong 1: every day is the weekend, and nothing crashes

**This is the bug of the day.**

```python
day = input("What day is it? ").strip().lower()

if day == "saturday" or "sunday":
    print("Sleep in.")
else:
    print("Alarm is set for 6:45.")
```

```
What day is it? monday
Sleep in.
```

**No error. Monday is the weekend now.** You will be late to school.

Python did not read this as "day is Saturday or Sunday." It read it as two separate
things joined by `or`:

1. `day == "saturday"`, which is False on Monday
2. `"sunday"`, a string standing on its own

A string on its own is not a question. So Python asks what a string counts as when an
`if` needs True or False. The rule: **an empty string counts as False, and any other
string counts as True.**

```python
print(bool("sunday"))
print(bool(""))
```

```
True
False
```

`"sunday"` is not empty, so the right side of the `or` is always True, so the whole
condition is always True. Every day, forever.

> **The dangerous bugs are the ones that do not crash.**

Sixth appearance. `121212`, 2.5 people, `202`, `"9"` beating `"10"`, a 95 that earns a D,
and now a Monday that counts as Sunday.

### Wrong 2: or where you needed and

```python
age = 15
if age > 12 and age < 20:
    print("Teen")
if age > 12 or age < 20:
    print("This prints for every age there is")
```

```
Teen
This prints for every age there is
```

With `or`, an age of 80 passes because 80 is more than 12. An age of 3 passes because 3
is less than 20. Every number is either above 12 or below 20. **A range check is almost
always `and`.**

### Wrong 3: a half comparison

```python
age = 15
if age >= 13 and <= 19:
    print("Teen")
```

```
    if age >= 13 and <= 19:
                     ^^
SyntaxError: invalid syntax
```

In English you can say "at least 13 and at most 19." Python needs the left side
repeated: `age >= 13 and age <= 19`.

### Wrong 4: another language's symbols

```python
if has_ticket && has_ride:
```

```
    if has_ticket && has_ride:
                   ^
SyntaxError: invalid syntax
```

JavaScript, Java, and C# write `&&` and `||`. Python writes `and` and `or`. If you learned
another language first, your fingers will try this for a week.

---

## Why the wrong versions are tempting

**English lets you skip words.** "Is it Saturday or Sunday" is a complete sentence to a
person. Python needs "is it Saturday, or is it Sunday." The shortcut you use when you talk
is exactly the bug.

**Wrong 1 passes half its tests.** Type `saturday` and it says sleep in. Type `sunday` and
it says sleep in. Both correct. It only fails on the five days you did not try, and nothing
warns you. **Always test a value that should make the condition False.**

**Operator order is invisible.** `is_member or has_coupon and total > 20` reads left to
right like a sentence, and Python does not read it that way. Nothing on the screen shows
you the grouping. Parentheses make the grouping visible.

**The defense.** For every `or`, check that both sides are complete comparisons. For every
condition that mixes `and` and `or`, add parentheses. For every condition that divides or
indexes, put the guard on the left.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Logical operator** | `and`, `or`, `not`. Combines or flips conditions. |
| **`and`** | True only when both sides are True. |
| **`or`** | True when at least one side is True. |
| **`not`** | Flips True to False and False to True. |
| **Compound condition** | A condition built from smaller conditions with logical operators. |
| **Short-circuit** | Python stops evaluating as soon as the answer is known. |
| **Guard** | A check placed first so a dangerous operation on its right never runs when it would fail. |
| **Precedence** | The order operators are applied: `not`, then `and`, then `or`. |
| **Truthy / falsy** | What a non-`bool` value counts as in a condition. Empty string is falsy, other strings are truthy. |

---

## Self-check

**Question 1.** Write the exact output. Three lines.

```python
has_permission_slip = True
paid_fee = False
is_on_team = True
print(has_permission_slip and paid_fee)
print(not paid_fee or is_on_team)
print(has_permission_slip and (paid_fee or is_on_team))
```

**Question 2.** This program is supposed to allow a shift only on Friday or Saturday. A
worker types `wednesday`. Write what it prints, say whether an error appears, and write the
corrected condition.

```python
day = input("Shift day: ").strip().lower()
if day == "friday" or "saturday":
    print("Shift approved.")
else:
    print("Weekend shifts only.")
```

**Question 3.** A student writes the condition below to check whether the first character
of a username is a capital letter. It crashes when the user presses Enter without typing
anything. Rewrite it so it never crashes, and explain in one sentence why your version is
safe.

```python
if username[0] == username[0].upper() and username != "":
```

---

### Answers

**1.**

```
False
True
True
```

Line 1: `paid_fee` is False, so `and` is False. Line 2: `not paid_fee` is True, so `or` is
True without checking the right side. Line 3: the parentheses give `False or True`, which is
True, then `True and True` is True.

**2.** It prints `Shift approved.` and **no error appears**. The right side of `or` is the
string `"saturday"` on its own, which is not empty and so counts as True every time. The
corrected condition is `if day == "friday" or day == "saturday":`, which prints
`Weekend shifts only.` for `wednesday`.

**3.**

```python
if username != "" and username[0] == username[0].upper():
```

Because `and` stops as soon as its left side is False, an empty username makes
`username != ""` False and Python never reaches `username[0]`, which is the part that
would crash.
