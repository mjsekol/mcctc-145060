# Lecture Notes: Code Review by Peer Walkthrough and Static Analysis
## 145060 Programming · Unit 6 · Week 14, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W14_CodeReview.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W14_CodeReview.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 5.6.13 (perform code reviews: peer walkthrough, static analysis), 5.6.9
(review the design: peer walkthrough), 5.5.2 (reuse libraries, here Python's `ast` module).

---

## Why this exists

Your tests check what somebody thought to check. Nobody thinks to check everything. That
is not a character flaw. It is how being the author works: your eyes slide over your own
assumptions because they are yours.

A **code review** puts other eyes on the code before it is trusted. There are two kinds,
and they catch different defects.

- A **peer walkthrough** is people reading the code together while the author explains it.
  People are slow, get tired, and understand what the code is **for**.
- **Static analysis** is a program reading the code without running it. Programs are fast,
  never tired, and have no idea what the code is for.

Neither one is enough alone. Today you see exactly what each one misses, using a checker
you can read line by line.

---

## The concept in plain language

### Static analysis

**Static** means the code is not running. The analyzer reads the file, turns it into a
structure it can search, and looks for **patterns** that are often mistakes: an `except`
that swallows every error, a password typed into the code, a file opened inside a loop.

It can find patterns. It cannot find **intent.** It has no idea that the stakeholder said
"1 to 24 laptops," so it cannot notice that the code refuses laptop 24.

Python ships with two static tools you can run right now, with nothing installed:

| Tool | Command | What it checks |
|---|---|---|
| `py_compile` | `python -m py_compile file.py` | Can Python read this file at all? Syntax only. |
| `ast` | used inside your own checker | Gives you the whole program as a tree of pieces you can search |

**Optional, not required and not installed on the lab machines:** professional teams use
installable linters such as `pylint`, `flake8`, and `ruff`, which check hundreds of
patterns. They work on the same idea as the checker in this note, at a much larger scale.
You do not need them for this unit.

### Peer walkthrough

The author walks reviewers through the code **in the order of the requirements**, not the
order of the file. For each requirement, the author points at the lines that satisfy it and
the reviewers ask what input would break them. A recorder writes down every finding.

Every finding has four parts: **where** (function and line), **dimension** (Correctness,
Security, Readability, Performance, Requirements Fit), **consequence**, and **fix**. The full
procedure is in `09-project/MCCTC_145060_PeerReview_Protocol.md`.

**The one rule: review the code, never the coder.**

---

## Worked example 1: what `py_compile` can and cannot tell you

Two broken files. Save them and check both.

`door.py`:

```python
print("Checking the door")
if door_open
    print("Close it")
```

`greet.py`:

```python
def greet(hour):
    """Greet the player based on the hour."""
    if hour < 12:
        return "Good morning"
    return "Good " + tiem_of_day


print(greet(9))
```

Run the checker on both:

```
$ python -m py_compile door.py
  File "door.py", line 2
    if door_open
                ^
SyntaxError: expected ':'

$ python -m py_compile greet.py

```

`door.py` fails, exit code 1. `greet.py` produces **no output at all**, exit code 0. It passed.

Now run `greet.py`:

```
$ python greet.py
Good morning
```

Still no error, because 9 is before noon and the broken line never ran. Call `greet(15)` and
it finally fails:

```
NameError: name 'tiem_of_day' is not defined
```

**`py_compile` only answers "can Python read this file."** A misspelled name in a branch that
has not run yet passes the check and passes the first test run. This is the bug that waits.

---

## Worked example 2: build the smallest useful checker

An `except` block that only says `pass` makes failures disappear. Here is a checker that finds
every one, in eight lines of real code.

`tiny_checker.py`:

```python
# tiny_checker.py
# The smallest useful static check: find every except block that only says pass.
import ast
import sys

with open(sys.argv[1], encoding="utf-8") as file:
    tree = ast.parse(file.read())

for node in ast.walk(tree):
    if isinstance(node, ast.ExceptHandler):
        if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            print(f"line {node.lineno}: this except block hides the failure")
```

`save.py`, the file being checked:

```python
import json


def save_scores(scores, path):
    """Write the high score table to disk."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(scores, file)
    except OSError:
        pass


save_scores({"level 1": 4200}, "scores.json")
```

```
$ python tiny_checker.py save.py
line 9: this except block hides the failure
```

**Read it line by line.** `ast.parse` reads the file the way Python does before running it and
hands back a **tree**: the whole program as nested pieces. `ast.walk` visits every piece.
`isinstance(node, ast.ExceptHandler)` asks "is this piece an except block?" The next line asks
whether its body is exactly one `pass`. The checker never runs `save.py`. It only reads it.

---

## Worked example 3: the full checker on a peer's code

`05-labs/lab-u06-03-files/review_check.py` is the same idea with six checks, each mapped to a
review dimension. Here it is on `cart_checkout.py`, the practice code for Lab U06-03.

```
$ python review_check.py cart_checkout.py
Static review of cart_checkout.py
------------------------------------------------------------
line 19   Security     'RESET_PIN' looks like a secret written into the code
line 44   Correctness  bare except catches every error, including your own typos
line 44   Correctness  except block only says pass, so the failure disappears silently
line 48   Readability  function 'chk' has no docstring
line 48   Readability  one-letter name 'c'
line 48   Readability  one-letter name 'n'
line 82   Performance  open() inside a loop reads or writes the file on every pass
------------------------------------------------------------
7 finding(s)
Not checked by this tool: Requirements Fit, and whether the logic is right.
```

Seven findings in under a second. Four dimensions covered. **Look at what is missing from the
list: Requirements Fit.** No static tool can check it, because the requirements are not in the
file. Lab U06-03 has you find what the checker could not.

### Static tools are wrong in both directions

**A false alarm.** Here is `shopping.py`:

```python
def shopping_total(prices):
    """Add up a list of prices."""
    total = 0
    for price in prices:
        total = total + price
    return total


shopping_list = "milk, eggs, bread"
print(shopping_total([2.5, 3.0, 1.25]))
```

```
$ python review_check.py shopping.py
Static review of shopping.py
------------------------------------------------------------
line 9    Security     'shopping_list' looks like a secret written into the code
------------------------------------------------------------
1 finding(s)
Not checked by this tool: Requirements Fit, and whether the logic is right.
```

"Shop**pin**g" contains the letters `pin`. A person looks at it for two seconds and dismisses it.

**A silent miss.** Run the same checker on `concessions.py` from Lab U06-01, which has three real
defects your tests found last week:

```
$ python review_check.py concessions.py
Static review of concessions.py
------------------------------------------------------------
------------------------------------------------------------
0 finding(s)
Not checked by this tool: Requirements Fit, and whether the logic is right.
```

---

## The wrong version, and what it does instead of an error

The wrong version is not a line of code. It is a conclusion:

> "The checker found 0 findings, so the code is clean."

`concessions.py` got 0 findings. It also refuses a legal order of 20 hot dogs, ignores sports
drinks in combos, and applies the member discount in the wrong order. All three defects are
about **what the code is supposed to do**, and the checker cannot see purpose.

**No error. No warning. A clean report on broken code.** It is the same shape as a test that
agrees with the bug: a tool that says "fine" and a person who stops looking.

---

## Why the wrong version is tempting

**Zero is a satisfying number.** It feels like a grade, and 0 findings feels like 100 percent.

**The tool looks authoritative.** It prints line numbers and dimension names, the same words the
rubric uses. It reads like a reviewer.

**People are slower and it is Monday.** A walkthrough takes twenty minutes and a checker takes
one second, so the temptation is to let the fast one stand in for the slow one.

The defense is the order in the protocol: **run the tools first, then do the walkthrough
anyway.** The tools clear the pattern-shaped defects in a minute, which leaves the people's
twenty minutes for the defects only people can find.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Code review** | Other people examining code before it is trusted. |
| **Peer walkthrough** | The author walks reviewers through the code, requirement by requirement. |
| **Static analysis** | Examining code without running it, usually with a tool. |
| **Dynamic testing** | Running the code to see what it does. Your acceptance tests are dynamic. |
| **Linter** | A static analysis tool that flags suspicious patterns. |
| **`py_compile`** | A standard library tool that checks whether Python can read a file. |
| **Abstract syntax tree** | The program represented as nested pieces. `ast.parse` builds it. |
| **False positive** | A tool flags something that is not a problem. |
| **False negative** | A tool misses something that is a problem. |
| **Finding** | One reviewed problem: where, dimension, consequence, fix. |

---

## Self-check

**Question 1.** A file passes `python -m py_compile` with no output. List two kinds of defect it
could still contain, with a one-line example of each.

**Question 2.** Name one defect a peer walkthrough can find that `review_check.py` never can, and
one defect `review_check.py` finds faster than any person.

**Question 3.** Predict the exact output of `python tiny_checker.py backup.py`, where `backup.py`
is:

```python
def backup(path):
    """Copy the save file."""
    try:
        data = open(path).read()
    except FileNotFoundError:
        print("No save file yet")
    try:
        open(path + ".bak", "w").write(data)
    except:
        pass
```

---

### Answers

**1.** Any defect that is not a syntax error. A misspelled name in a branch that has not run, such
as `return "Good " + tiem_of_day`. A logic error, such as `if quantity >= 20` when 20 is allowed.
A missing requirement. A swallowed error, such as `except: pass`.

**2.** Walkthrough only: anything about purpose, such as refusing laptop 24 when the requirement
says 1 to 24, or a report that is missing a requirement entirely. Faster by tool: a secret
written into the code, an `except` that only says `pass`, a missing docstring, or a file opened
inside a loop.

**3.** Output:

```
line 9: this except block hides the failure
```

Line 5's `except FileNotFoundError:` has a `print` in its body, not `pass`, so it is not flagged.
Line 9's bare `except:` contains only `pass`. Notice the checker does not notice that `data` is
never defined if the first `try` fails. That is a person's finding.
