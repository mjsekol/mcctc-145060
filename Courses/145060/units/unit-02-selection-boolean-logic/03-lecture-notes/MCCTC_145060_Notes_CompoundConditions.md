# Lecture Notes: Compound Conditions and When to Flatten Nesting
## 145060 Programming · Unit 2 · Week 5, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W05_FlatteningNesting.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W05_FlatteningNesting.pptx)

If you missed class, you can learn this concept from this file alone. This is the hardest
lesson of Week 5, because it is not a new piece of syntax. It is a judgment call, and the
right answer changes with the shape of the problem. Read the section called "The decision
rule" twice.

---

## Why this exists

You can put an `if` inside another `if`. That is called **nesting**, and you have probably
already done it by accident. It works. The problem is what happens when you keep doing it.

Four rules deep, your code drifts to the right side of the screen, every `else` sits a long
way below the `if` it belongs to, and nobody reading it can tell which message goes with
which rule. That includes you, next week.

This lesson answers one question: **when should a decision be nested, and when should it be
flattened into one level?** Your Decision Engine project is graded on it.

---

## The concept in plain language

A **compound condition** combines smaller conditions with `and`, `or`, and `not` into one
condition. You met them Tuesday. Today you use them to replace nesting.

**Flattening** means rewriting nested `if` statements so the same decisions happen at one
level of indentation. It never changes what the program does. It changes how hard the
program is to read, test, and fix.

### Python lets you chain comparisons

One compound condition is so common that Python has a shortcut for it:

```python
age = 15
print(13 <= age <= 19)
print(age >= 13 and age <= 19)
age = 20
print(13 <= age <= 19)
```

Output:

```
True
True
False
```

`13 <= age <= 19` means exactly `age >= 13 and age <= 19`. It reads the way you would write it
in math class. Most other languages do not allow this, so you will see both forms in the wild.

---

## Worked example 1: the pyramid

The robotics team is going on a road trip. To get on the bus you must be on the team, have a
signed permission slip, have paid the fee or have a fee waiver, and have at least a 2.0 GPA.
Each missing requirement gets its own message.

```python
on_team = input("On the robotics team? (y/n): ").strip().lower() == "y"
has_slip = input("Permission slip signed? (y/n): ").strip().lower() == "y"
fee_paid = input("Trip fee paid? (y/n): ").strip().lower() == "y"
has_waiver = input("Fee waiver approved? (y/n): ").strip().lower() == "y"
gpa = float(input("Current GPA: "))

if on_team:
    if has_slip:
        if fee_paid or has_waiver:
            if gpa >= 2.0:
                print("You are on the bus.")
            else:
                print("You need a 2.0 GPA to travel.")
        else:
            print("Pay the fee or ask about a waiver.")
    else:
        print("Get your permission slip signed.")
else:
    print("This trip is for team members.")
```

```
On the robotics team? (y/n): y
Permission slip signed? (y/n): y
Trip fee paid? (y/n): n
Fee waiver approved? (y/n): y
Current GPA: 3.1
You are on the bus.
```

It is correct. Now try to answer this without counting spaces: **which `if` does the message
"Get your permission slip signed." belong to?** Its `else` is nine lines below its `if`. The
happy path sits in the middle, four levels deep, and each failure message is further from its
rule than the last. This shape has a nickname: the pyramid.

---

## Worked example 2: the same rules, flattened

Turn it inside out. **Check each reason to say no, one at a time, and say yes last.**

```python
on_team = input("On the robotics team? (y/n): ").strip().lower() == "y"
has_slip = input("Permission slip signed? (y/n): ").strip().lower() == "y"
fee_paid = input("Trip fee paid? (y/n): ").strip().lower() == "y"
has_waiver = input("Fee waiver approved? (y/n): ").strip().lower() == "y"
gpa = float(input("Current GPA: "))

if not on_team:
    print("This trip is for team members.")
elif not has_slip:
    print("Get your permission slip signed.")
elif not (fee_paid or has_waiver):
    print("Pay the fee or ask about a waiver.")
elif gpa < 2.0:
    print("You need a 2.0 GPA to travel.")
else:
    print("You are on the bus.")
```

Typing `y`, `y`, `n`, `n`, `3.1`:

```
Pay the fee or ask about a waiver.
```

Typing `y`, `y`, `y`, `n`, `1.9`:

```
You need a 2.0 GPA to travel.
```

**Every rule sits directly next to its message.** Adding a fifth requirement is one new
`elif`. Deleting one is two lines.

**Is it really the same program?** Both versions were run on all 48 combinations of the four
yes-or-no answers and three GPAs (1.9, 2.0, and 3.5). They printed identical output every
time. That is what "flattening never changes behavior" means, and it is the standard you hold
your own refactors to: same inputs, same outputs, every row of the truth table.

Notice `not (fee_paid or has_waiver)`. That is Wednesday's De Morgan table in real code. It
means the same thing as `not fee_paid and not has_waiver`.

---

## Worked example 3: when you only need yes or no

If the program does not need a separate message for each rule, the whole pyramid collapses
into one compound condition:

```python
can_travel = on_team and has_slip and (fee_paid or has_waiver) and gpa >= 2.0
print("Can travel:", can_travel)
```

Typing `y`, `y`, `n`, `y`, `3.1`:

```
Can travel: True
```

The parentheses around the `or` are not optional. Without them, Python groups the condition as
`(on_team and has_slip and fee_paid) or (has_waiver and gpa >= 2.0)`. Executed with
`on_team = False`, `has_slip = False`, `fee_paid = False`, `has_waiver = True`, and `gpa = 3.0`,
the version without parentheses gives `True`. Somebody who is not on the team and has no
permission slip gets on the bus because they have a fee waiver. No error.

---

## Worked example 4: nesting that is correct

Flattening is not always better. Here is a program where the nesting is the right shape.

```python
weather = input("Weather (rain or clear): ").strip().lower()

if weather == "rain":
    has_ride = input("Can someone drive you? (y/n): ").strip().lower() == "y"
    if has_ride:
        print("Movie theater.")
    else:
        print("Board games at home.")
else:
    friends_free = input("Are your friends free? (y/n): ").strip().lower() == "y"
    if friends_free:
        print("Meet at the park.")
    else:
        print("Shoot hoops in the driveway.")
```

```
Weather (rain or clear): rain
Can someone drive you? (y/n): n
Board games at home.
```

```
Weather (rain or clear): clear
Are your friends free? (y/n): y
Meet at the park.
```

**The inner questions are different in each branch.** On a rainy day, whether your friends are
free does not matter yet, and the program never asks. On a clear day, nobody asks about a ride.
The first answer decides which question comes next.

That shape is a **decision tree**: each answer leads to a different next question. A flattened
version would have to ask all three questions every time, including ones that do not matter,
and repeat `weather == "rain"` in every condition. Nesting wins here.

Your Decision Engine project classifies input using nested conditions for exactly this reason.
Next Tuesday you compare this kind of hand-built tree with how machine learning builds one.

---

## The decision rule

Ask these in order.

| Question | If yes |
|---|---|
| Does the inner `if` have **no `else`**, so it only adds another requirement? | Combine it into the outer condition with `and`. |
| Is every level a **requirement with its own failure message**? | Flatten into an `elif` chain: reasons to say no first, yes last. |
| Does the **next question depend on the answer** to this one? | Keep the nesting. That is a decision tree. |
| Is it more than **three levels deep**? | Stop and look again. It is almost always one of the first two cases. |

---

## The wrong version: an else attached to the wrong if

**This is the bug of the day, and it does not crash.**

```python
on_team = input("On the robotics team? (y/n): ").strip().lower() == "y"
has_slip = input("Permission slip signed? (y/n): ").strip().lower() == "y"

if on_team:
    if has_slip:
        print("You are on the bus.")
else:
    print("Get your permission slip signed.")
```

A team member with no slip, typing `y` then `n`:

```
On the robotics team? (y/n): y
Permission slip signed? (y/n): n
```

**Nothing.** No message at all.

Someone not on the team who has a slip, typing `n` then `y`:

```
On the robotics team? (y/n): n
Permission slip signed? (y/n): y
Get your permission slip signed.
```

**The wrong person got the message.**

The `else` is lined up under `if on_team:`, so it belongs to `on_team`, not to `has_slip`. The
author meant it for the inner `if` and was off by four spaces. Python did exactly what the
indentation said.

Eighth appearance. Nothing crashed. One person got silence and another got a message meant for
someone else. The flat `elif` version cannot have this bug, because every message sits on the
same level as its own rule.

### The mistake that does crash

```python
age = 16
if age >= 16:
    print("Old enough.")
        print("Book the test.")
```

```
    print("Book the test.")
IndentationError: unexpected indent
```

Indentation has to mean something. Four extra spaces that do not start a new block are an error.

---

## Why the pyramid is tempting

**It matches how you think through a checklist.** "Are they on the team? Okay, now do they have
a slip? Okay, now..." Each question feels like it comes after the last, so each `if` goes
inside the last.

**It works.** Worked example 1 is correct. Nothing about the pyramid is broken today. The cost
arrives when somebody changes it, and it is paid by whoever touches it next.

**Flattening feels backwards at first.** Checking reasons to say no before saying yes is a
habit, not an instinct. Once you have it, you will see pyramids everywhere, including in code
an AI hands you. Tomorrow's Gate 2 is waiting for that.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Nesting** | Putting an `if` inside another `if` block. |
| **Nesting depth** | How many levels deep a block is. Worked example 1 reaches depth 4. |
| **Compound condition** | One condition built from smaller ones with `and`, `or`, `not`. |
| **Chained comparison** | `13 <= age <= 19`, Python's shortcut for two comparisons joined by `and`. |
| **Flattening** | Rewriting nested decisions at one level without changing behavior. |
| **Guard** | A check that handles a reason to stop before the main path runs. |
| **Happy path** | The route through the code when every requirement is met. |
| **Decision tree** | A structure where each answer decides which question comes next. |
| **Refactor** | Changing how code is written without changing what it does. |

---

## Self-check

**Question 1.** Flatten this into a single `if` with no nesting. It must behave identically.

```python
if hours_slept >= 8:
    if ate_breakfast:
        print("Ready for the test.")
```

**Question 2.** Should this be flattened, and why? Answer in two sentences.

```python
if device == "phone":
    if battery < 20:
        print("Charge it before you leave.")
    else:
        print("Good to go.")
else:
    if is_plugged_in:
        print("Laptop is fine.")
    else:
        print("Bring the charger.")
```

**Question 3.** A 14-year-old with no physical on file sees no message at all, and a
10-year-old is told they need a physical. The rule is that players 12 and older need a physical
on file. Find the bug without running it, and write the fix.

```python
age = int(input("Age: "))
has_physical = input("Physical on file? (y/n): ").strip().lower() == "y"

if age >= 12:
    if has_physical:
        print("Bring a water bottle.")
else:
    print("You need a physical first.")
```

---

### Answers

**1.**

```python
if hours_slept >= 8 and ate_breakfast:
    print("Ready for the test.")
```

The inner `if` had no `else`, so it only added a second requirement. `and` expresses that
directly.

**2.** No. The inner question is different in each branch, battery level for a phone and whether
it is plugged in for a laptop, so this is a decision tree and the nesting is the honest shape of
the problem.

**3.** Both symptoms come from one misplaced `else`. It is lined up with `if age >= 12:`, so it
belongs to the age check, and the physical message goes to players **under** 12. Meanwhile the
inner `if has_physical:` has no `else` of its own, so a 14-year-old with no physical falls through
and gets nothing. The fix, flattened:

```python
age = int(input("Age: "))
has_physical = input("Physical on file? (y/n): ").strip().lower() == "y"

if age >= 12 and not has_physical:
    print("You need a physical first.")
else:
    print("Bring a water bottle.")
```

Executed: age `14` with `n` prints `You need a physical first.` Age `14` with `y` prints
`Bring a water bottle.` Age `10` with `n` prints `Bring a water bottle.`

The original printed nothing for `14` with `n`, and told `10` with `n` to get a physical, which
matches both symptoms in the question. **When code and intent disagree, the requirement wins,
and you have to know what the requirement says.** That is tomorrow's Gate 2 in one sentence.
