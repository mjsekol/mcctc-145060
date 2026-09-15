# Lecture Notes: match and case
## 145060 Programming · Unit 2 · Week 6, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W06_MatchCase.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W06_MatchCase.pptx)

If you missed class, you can learn this concept from this file alone. `match` needs Python
3.10 or newer. The lab machines run 3.14, so you are fine. If you try this on an old
computer at home and every `match` line is a `SyntaxError`, check `python --version` first.

---

## Why this exists

Look at this kind of chain:

```python
if club == "robotics":
    ...
elif club == "band":
    ...
elif club == "esports" or club == "gaming":
    ...
else:
    ...
```

Every condition asks the same question about the same variable: **which one of these exact
values is it?** You type `club ==` over and over, and every repetition is another place to
make Tuesday's `or "gaming"` mistake.

Most programming languages have a structure built for exactly this situation. In Java,
JavaScript, and C#, it is called `switch`. In Python, since version 3.10, it is `match`. The
WebXam calls the idea a **selection control structure**, and it lists "case" and "switch" by
name.

---

## The concept in plain language

```python
match value:
    case "first option":
        # runs when value is "first option"
    case "second option" | "another spelling":
        # runs when value is either of these
    case _:
        # runs when nothing above matched
```

- `match` names the value you are checking, once.
- Each `case` gives a pattern. Python checks them **top to bottom** and runs the **first**
  one that matches, then skips the rest. Same rule as an `elif` chain.
- `|` inside a case means "or this one." It only works between patterns, not between
  full conditions.
- `case _:` is the catch-all. The underscore matches anything. It works like `else`, and it
  goes last.

**Unlike `switch` in some other languages, there is no "fall through."** Python never runs a
second case after the first match. You do not write `break`.

---

## Worked example 1: which club room

```python
club = input("Which club? ").strip().lower()

match club:
    case "robotics":
        print("Room B114, Tuesdays after school.")
    case "band":
        print("Band room, every morning at 7:15.")
    case "esports" | "gaming":
        print("Lab C, Thursdays. Bring your own headset.")
    case _:
        print("That club is not on the list. Check the spelling.")
```

```
Which club? Robotics
Room B114, Tuesdays after school.
```

```
Which club? gaming
Lab C, Thursdays. Bring your own headset.
```

```
Which club? chess
That club is not on the list. Check the spelling.
```

**Clean first, match second.** `Robotics` matched `"robotics"` only because of `.lower()`.
A `case` compares exactly, character for character, the same way `==` does.

Here is the `elif` version of the same program. It was run with the same three inputs and
printed the same three results.

```python
club = input("Which club? ").strip().lower()

if club == "robotics":
    print("Room B114, Tuesdays after school.")
elif club == "band":
    print("Band room, every morning at 7:15.")
elif club == "esports" or club == "gaming":
    print("Lab C, Thursdays. Bring your own headset.")
else:
    print("That club is not on the list. Check the spelling.")
```

Both are correct. The `match` version names `club` once and lists the options as a menu.

---

## Worked example 2: setting a value, then using it

A `case` block can hold any code, including assignments.

```python
order = input("What do you want from the snack bar? ").strip().lower()

match order:
    case "pretzel":
        price = 3.00
    case "nachos" | "nacho":
        price = 4.50
    case "water":
        price = 1.00
    case _:
        price = 0.00

if price > 0:
    print(f"That will be ${price:.2f}.")
else:
    print("We do not sell that here.")
```

```
What do you want from the snack bar? Nachos
That will be $4.50.
```

```
What do you want from the snack bar? pizza
We do not sell that here.
```

Every case sets `price`, including the catch-all. If one did not, the `if` below could hit a
`NameError`, exactly like the ticket lab's If it breaks item 3.

---

## Worked example 3: match is the wrong tool for ranges

`match` is built for **exact values.** It can handle a range, with a `case` that has an `if`
attached, called a guard:

```python
score = int(input("Score: "))
match score:
    case 100:
        print("Perfect.")
    case s if s >= 90:
        print("A")
    case s if s >= 80:
        print("B")
    case _:
        print("Below a B")
```

Scores `100`, `93`, `85`, and `40` print `Perfect.`, `A`, `B`, and `Below a B`.

It works. It is also harder to read than the `elif` chain from last Monday, and it introduces a
new name `s` for no benefit. **Be honest about the choice:**

| Use `match` when | Use `if`/`elif` when |
|---|---|
| One variable is compared to a list of exact values | Conditions use `<`, `>`, `<=`, `>=` |
| The options read like a menu | Conditions involve more than one variable |
| You would otherwise type `x ==` many times | Conditions combine with `and` and `or` |

Grade bands, ticket ages, and GPA cutoffs are `elif`. Menu choices, commands, and club names are
`match`.

---

## The wrong versions

### Wrong 1: a name in a case captures instead of compares

**This is the bug of the day, and in its worst form it does not crash.**

You have a variable holding today's special, and you want a case for it:

```python
TODAYS_SPECIAL = "tacos"
order = input("What do you want? ").strip().lower()

match order:
    case "pizza":
        print("Pizza slice, $3.00")
    case TODAYS_SPECIAL:
        print("Today's special, $2.50")
```

```
What do you want? sushi
Today's special, $2.50
```

**No error. Sushi is today's special.** The snack bar does not even sell sushi.

Here is why. In a `case`, a **quoted value** like `"pizza"` is compared. A **bare name** like
`TODAYS_SPECIAL` is not compared to anything. It is a **capture**: it matches whatever the value
is, and it stores that value in the name. After this program runs, `TODAYS_SPECIAL` holds
`"sushi"`. The case matched every order that was not pizza, and it overwrote your variable while
it was at it.

Add a catch-all after it, and Python notices:

```python
    case TODAYS_SPECIAL:
        print("Today's special, $2.50")
    case _:
        print("Not on the menu.")
```

```
    case TODAYS_SPECIAL:
         ^^^^^^^^^^^^^^
SyntaxError: name capture 'TODAYS_SPECIAL' makes remaining patterns unreachable
```

That message is Python saying: this case catches everything, so the one below it can never run.
Monday of Week 5 had unreachable code with no warning. `match` warns you, **but only if there is
a case below the capture.**

The fix is to write the value in quotes in the case, `case "tacos":`, or to use an `if` when
the value you are comparing to lives in a variable.

Ninth appearance of the shape: a program that runs, prints something confident, and is wrong.

### Wrong 2: no catch-all

```python
club = input("Which club? ").strip().lower()
match club:
    case "robotics":
        print("Room B114")
    case "band":
        print("Band room")
print("Done.")
```

```
Which club? chess
Done.
```

No case matched, so nothing in the `match` ran, and the program moved on. Sometimes that is what
you want. Usually it means somebody typed something and got silence. **Include `case _:` unless
you have decided on purpose that silence is correct.**

### Wrong 3: another language's words

```python
club = "band"
switch club:
    case "band":
        print("Band room")
```

```
    switch club:
           ^^^^
SyntaxError: invalid syntax
```

```python
club = "band"
match club:
    case "band":
        print("Band room")
    default:
        print("Unknown")
```

```
    default:
    ^^^^^^^
SyntaxError: invalid syntax
```

Python says `match`, not `switch`, and `case _:`, not `default:`.

---

## Why the wrong versions are tempting

**Every other place in Python, a name means its value.** `print(TODAYS_SPECIAL)` prints `tacos`.
`if order == TODAYS_SPECIAL:` compares to `tacos`. A `case` is the one place where a bare name
means "grab whatever is here." Nothing about the syntax warns you that the rules changed.

**It passes the obvious test.** Order `tacos` and you get today's special. Correct. Order `pizza`
and you get pizza. Correct. The bug appears only for an order that should match nothing, and that
is the test people skip.

**Other languages trained your fingers.** If you have written any Java, JavaScript, or C#, `switch`
and `default` feel right. Python chose different words.

**The defense.** In a `case`, write literal values in quotes. Always test one input that should
reach the catch-all, and confirm that it does.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Selection control structure** | A structure that chooses one path among many. `if`/`elif`/`else` and `match`/`case` are both selection structures. |
| **`match`** | Python's structure for comparing one value against a list of patterns. Python 3.10 and newer. |
| **`case`** | One pattern inside a `match`, with the code to run if it matches. |
| **Pattern** | What a `case` checks against. A quoted value is compared exactly. |
| **Or-pattern** | `case "esports" \| "gaming":`, matches either value. |
| **Wildcard** | `case _:`, matches anything. Python's version of `default`. |
| **Capture pattern** | A bare name in a `case`. Matches anything and stores the value in that name. |
| **Guard** | An `if` attached to a `case`, such as `case s if s >= 90:`. |
| **`switch`** | The equivalent structure in Java, JavaScript, and C#. Not a Python word. |

---

## Self-check

**Question 1.** Write the exact output for the input `  SKIP ` and for the input `pause`.

```python
command = input("Command: ").strip().lower()

match command:
    case "play" | "resume":
        print("Playing.")
    case "skip" | "next":
        print("Next song.")
    case "stop":
        print("Stopped.")
    case _:
        print("Unknown command.")
```

**Question 2.** Rewrite this `elif` chain as a `match`. It must behave identically, including
for inputs that match nothing.

```python
size = input("Drink size: ").strip().lower()
if size == "small":
    price = 1.50
elif size == "medium" or size == "regular":
    price = 2.00
elif size == "large":
    price = 2.50
else:
    price = 0.00
print(f"${price:.2f}")
```

**Question 3.** A classmate says they should convert their grade-band `elif` chain to `match`
because `match` is newer and cleaner. Give the strongest argument against that in two sentences.

---

### Answers

**1.** For `  SKIP `:

```
Command:   SKIP 
Next song.
```

For `pause`:

```
Command: pause
Unknown command.
```

`.strip().lower()` turns `  SKIP ` into `skip`, which matches the second case. `pause` matches
nothing and reaches `case _:`.

**2.**

```python
size = input("Drink size: ").strip().lower()
match size:
    case "small":
        price = 1.50
    case "medium" | "regular":
        price = 2.00
    case "large":
        price = 2.50
    case _:
        price = 0.00
print(f"${price:.2f}")
```

Executed with `Regular`, `large`, and `huge`: prints `$2.00`, `$2.50`, and `$0.00`, the same as
the `elif` version.

**3.** Grade bands are ranges checked with `>=`, and `match` compares exact values, so every band
would need a guard like `case s if s >= 90:`, which is longer and harder to read than the chain it
replaces. Newer is not a reason to change working code, and the right tool depends on whether you
are comparing to exact values or to ranges.
