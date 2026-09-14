# Lecture Notes: elif Chains and the Order of Conditions
## 145060 Programming · Unit 2 · Week 5 · Monday, October 5

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W05_ElifChains.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W05_ElifChains.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example and run each one with the exact boundary numbers listed. The bug in this file
does not crash, so running it once with a normal number proves nothing.

---

## Why this exists

Thursday gave you a fork with two paths: `if` and `else`. Most real decisions have
more than two outcomes.

A test score is an A, B, C, D, or F. A movie ticket is free, child, adult, or senior.
Your phone's screen time report is under an hour, one to three hours, or "please go
outside." You could build those out of a stack of separate `if` statements, and by
the end of this file you will see why that goes wrong.

`elif` gives you **one decision with many possible outcomes, where exactly one
outcome happens.**

---

## The concept in plain language

`elif` is short for "else if." It adds another condition to the same decision.

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 was False and condition_2 is True
elif condition_3:
    # runs if both earlier ones were False and condition_3 is True
else:
    # runs if every condition above was False
```

Python checks the conditions **from the top down** and stops at the **first one that
is True**. It runs that block, then skips everything else in the chain. It never goes
back and never checks the rest.

Three rules:

1. **Exactly one block in an `if`/`elif`/`else` chain runs.** Never two.
2. **`else` is optional, and if you have one it goes last.** It catches everything the
   conditions above did not.
3. **Order matters whenever two conditions could both be True for the same value.**
   The first one wins.

Rule 3 is the whole lesson. The rest is syntax.

---

## Worked example 1: grade bands, in the right order

```python
score = int(input("Test score: "))

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Score {score}: letter grade {letter}")
```

Four runs, chosen on purpose:

```
Test score: 95
Score 95: letter grade A
```

```
Test score: 90
Score 90: letter grade A
```

```
Test score: 89
Score 89: letter grade B
```

```
Test score: 59
Score 59: letter grade F
```

**Trace 89 by hand.** Is 89 at least 90? No, move on. Is 89 at least 80? Yes. Set
`letter` to `"B"` and skip the rest of the chain. Python never asks whether 89 is at
least 70, even though it is.

That is why this works. **A score of 95 is also at least 80, 70, and 60.** Four of the
five conditions are True for 95. Only the first True one counts, so the order has to
put the hardest-to-reach band first.

Notice 90 and 89. Those are the two sides of the A boundary, and they are the two
runs that prove `>=` was the right choice.

---

## Worked example 2: the same idea counting up

The chain does not have to go from high to low. It has to be **consistent**.

```python
minutes = int(input("Minutes on your phone today: "))

if minutes < 60:
    print("Under an hour. Nice.")
elif minutes < 180:
    print("One to three hours. Pretty normal.")
elif minutes < 300:
    print("Three to five hours. That is a part-time job.")
else:
    print("Five hours or more. Your thumbs need a day off.")
```

Runs at the boundaries:

```
Minutes on your phone today: 60
One to three hours. Pretty normal.
```

```
Minutes on your phone today: 179
One to three hours. Pretty normal.
```

```
Minutes on your phone today: 180
Three to five hours. That is a part-time job.
```

With `<`, the chain starts at the **smallest** cutoff. With `>=`, it starts at the
**largest**. Either way, the first condition is the narrowest band, the one the fewest
values can reach from that direction.

---

## Worked example 3: what to wear

```python
temp = int(input("Temperature outside: "))

if temp >= 80:
    print("Shorts.")
elif temp >= 60:
    print("Hoodie optional.")
elif temp >= 40:
    print("Hoodie.")
else:
    print("Real coat. Do not argue.")
```

```
Temperature outside: 60
Hoodie optional.
```

```
Temperature outside: 12
Real coat. Do not argue.
```

The `else` has no condition. It does not need one. By the time Python reaches it,
every condition above has already been False, so the temperature must be under 40.

---

## The wrong version: right conditions, wrong order

**This is the bug of the week.** Every condition below is correct. Only the order
changed.

```python
score = int(input("Test score: "))

if score >= 60:
    letter = "D"
elif score >= 70:
    letter = "C"
elif score >= 80:
    letter = "B"
elif score >= 90:
    letter = "A"
else:
    letter = "F"

print(f"Score {score}: letter grade {letter}")
```

```
Test score: 95
Score 95: letter grade D
```

```
Test score: 72
Score 72: letter grade D
```

**No error. A 95 is a D.**

Python asked whether 95 is at least 60. It is. So `letter` became `"D"` and the rest
of the chain was skipped. The `A` line can never run for any score, because any score
that reaches 90 already passed 60 first. The code for an A is in the file and it is
unreachable.

Notice what testing would have found. **A student who tested this with 45 and 65 saw
`F` and `D` and called it done.** Both answers were correct. The bug only appears for
scores of 70 and up. That is why you test every band, not one or two.

> **The dangerous bugs are the ones that do not crash.**

Fifth time this course has shown you the shape: `121212`, 2.5 people, `202`, `"9"`
beating `"10"`, and now a 95 that earns a D. Every one of them ran cleanly and printed
something that looked like an answer.

---

## The other wrong version: separate `if`s instead of a chain

```python
score = int(input("Test score: "))

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
if score >= 60:
    print("D")
else:
    print("F")
```

```
Test score: 95
A
B
C
D
```

Four separate `if` statements are four separate decisions, and each one checks its own
condition no matter what happened above. A 95 passes all four. **`elif` is what ties
the conditions into one decision.** If you only want one outcome, you need one chain.

The `else` here belongs only to the last `if`. That is why a score of 42 prints only
`F`, and a score of 95 prints no `F`. It looks almost right, which is what makes it
dangerous.

---

## The mistakes that do crash

### `elif` after `else`

```python
score = 85
if score >= 90:
    print("A")
else:
    print("Not an A")
elif score >= 80:
    print("B")
```

```
    elif score >= 80:
    ^^^^
SyntaxError: invalid syntax
```

`else` ends the chain. Nothing can be added after it.

### A condition on `else`

```python
score = 85
if score >= 90:
    print("A")
else score >= 80:
    print("B")
```

```
    else score >= 80:
         ^^^^^
SyntaxError: expected ':'
```

`else` never takes a condition. If you need a condition, you need `elif`.

### Spelling it the way another language does

`else if` and `elseif` both fail. Python spells it `elif`.

```
    else if score >= 80:
         ^^
SyntaxError: expected ':'
```

```
    elseif score >= 80:
           ^^^^^
SyntaxError: invalid syntax
```

---

## Why the wrong order is tempting

**You write the bands in the order you think of them.** Most people think of grades
from the bottom up, or read a grading scale from a syllabus that lists F first.
Typing the chain in that order feels natural and produces the bug.

**Every line looks correct on its own.** `score >= 60` really is the rule for a D, if
you read it alone. The bug is not in any line. It is in the relationship between
lines, and that is much harder to see by reading.

**The low scores test correctly.** A 45 and a 65 both give the right answer. If those
are the numbers you tried, the program passed your testing.

**The defense is a habit.** For every chain, ask one question before you run it:
**could a value make two of these conditions True?** If yes, the most specific one
must come first. Then test one value from **every** band, plus the exact boundary
numbers.

---

## Vocabulary

| Term | What it means |
|---|---|
| **`elif`** | "Else if." Adds another condition to the same decision. |
| **Chain** | One `if`, any number of `elif`s, and an optional `else`, working as one decision. |
| **First True wins** | Python runs the block of the first True condition in a chain and skips the rest. |
| **Overlapping conditions** | Two conditions that can both be True for the same value, like `score >= 60` and `score >= 90`. |
| **Unreachable code** | Code that can never run for any input, such as the `A` line in the wrong-order chain. |
| **Band** | A range of values that share an outcome, such as 80 to 89 for a B. |
| **Boundary test** | Running a program with the exact cutoff value and the value on either side of it. |
| **Catch-all** | The `else` at the end of a chain, which handles everything the conditions did not. |

---

## Self-check

**Question 1.** Write the exact output for a height of `54` and for a height of `48`.

```python
height = int(input("Height in inches: "))

if height >= 54:
    print("You can ride everything.")
elif height >= 48:
    print("You can ride everything except the Drop Tower.")
elif height >= 42:
    print("Kiddie rides and the carousel.")
else:
    print("Carousel with a grown-up.")
```

**Question 2.** A shipping program charges by package weight in pounds. It gives the
wrong price for a 12-pound package, and there is no error. Find the problem, write the
corrected chain, and name the weight you would test to prove the fix.

```python
weight = float(input("Weight in pounds: "))

if weight > 2:
    price = 9.00
elif weight > 10:
    price = 15.00
else:
    price = 5.00

print(f"Shipping: ${price:.2f}")
```

**Question 3.** Explain in two sentences why this program prints two lines for a score
of 95, and what single word change makes it print one.

```python
score = 95
if score >= 90:
    print("Honor roll")
if score >= 80:
    print("Good standing")
```

---

### Answers

**1.** For `54`:

```
Height in inches: 54
You can ride everything.
```

For `48`:

```
Height in inches: 48
You can ride everything except the Drop Tower.
```

54 is exactly the first cutoff and `>=` includes it. 48 fails the first condition and
passes the second.

**2.** The chain checks `weight > 2` before `weight > 10`. A 12-pound package is more
than 2, so it takes the first branch and pays `$9.00`. The `$15.00` branch can never
run, because anything over 10 is also over 2. Put the more specific condition first:

```python
weight = float(input("Weight in pounds: "))

if weight > 10:
    price = 15.00
elif weight > 2:
    price = 9.00
else:
    price = 5.00

print(f"Shipping: ${price:.2f}")
```

```
Weight in pounds: 12
Shipping: $15.00
```

Test with `12` to prove the fix, then with `10` and `10.5` to prove the boundary. `10`
should cost `$9.00` because 10 is not more than 10, and `10.5` should cost `$15.00`.

**3.** The two `if` statements are separate decisions, and 95 is at least 90 and also
at least 80, so both run no matter what the other one did. Changing the second `if` to
`elif` joins them into one chain, and 95 then prints only `Honor roll`, because the
first True condition wins and the rest of the chain is skipped.
