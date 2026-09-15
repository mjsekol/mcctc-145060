# Lecture Notes: Test Cases, and Testing a Program Against Them
## 145060 Programming · Unit 4 · Week 9 · Thursday, November 5

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W09_TestCases.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W09_TestCases.pptx)

If you missed class, you can learn this concept from this file alone. You need functions that return
values (October 29) and `try` and `except` (November 3).

**Today is one concept: a test case is an input and the output you expect, decided before you run
anything, and a test is code that checks it for you.** You need two small pieces of plumbing to make that
work, `import` and one `if` line, and both are explained below.

---

## Why this exists

How did you know your text adventure version 1 worked? You played it. Then you changed something and played
it again. And again.

This week you are rebuilding that game out of functions. Every change can break something that used to work,
somewhere you are not looking. That kind of bug has a name: a **regression**, a feature that worked and then
stopped. Playing the whole game after every change does not scale, and you will skip it on the day it matters.

A **test** checks one thing the program must do, by running the code and comparing what it produces to what it
should produce. Once written, it costs one command to run all of them, every time.

Outcomes: 5.4.4, **define test cases**, and 5.4.5, **test the program using defined test cases**. Importing your own
file to reuse its functions touches 5.5.2, **develop programs that use reuse libraries**.

---

## The concept in plain language

A **test case** has four parts:

| Part | Example |
|---|---|
| **ID** | TC-3 |
| **Input** | `order_total(35)` |
| **Expected output** | `35` |
| **Why this case** | Exactly the free shipping amount. The boundary. |

**The expected output never comes from running your program.** It comes from the requirement, worked out by hand. If you run the code and copy
what it prints, the test agrees with the code whether the code is right or not, and it proves nothing. That mistake is the deliberate error
today.

**Which cases?** You met the answer in Unit 2, when you wrote six boundary tests for an eligibility rule. Pick cases from four groups:

| Group | What it catches |
|---|---|
| **Normal** | A value in the middle. It catches code that is completely wrong. |
| **Boundary** | The exact edge, and one step on each side. It catches `>` where `>=` belongs. |
| **Invalid** | Input the function must refuse. It catches missing validation. |
| **A bug you already fixed** | The reproduction from your troubleshooting log. It catches the same bug coming back. |

Middle values alone pass almost any code. **Boundaries are where bugs live.**

---

## The program under test

```python
# spirit_store.py
# Order total for the school spirit store's online shop.
# Orders of $35 or more ship free. Smaller orders pay $6 shipping.

FREE_SHIPPING_AT = 35
SHIPPING = 6


def order_total(subtotal):
    """Return the subtotal plus shipping, in whole dollars. Raise ValueError if subtotal is not positive."""
    if subtotal < 1:
        raise ValueError("An order must cost at least $1.")
    if subtotal >= FREE_SHIPPING_AT:
        return subtotal
    return subtotal + SHIPPING


def main():
    subtotal = int(input("Order subtotal in dollars: "))
    print(f"Total with shipping: ${order_total(subtotal)}")


# Run main() only when this file is run directly, not when a test imports it.
if __name__ == "__main__":
    main()
```

The rule is "$35 **or more** ships free." Here are its test cases, worked out from the rule before any code runs:

| ID | Input | Expected | Why this case |
|---|---|---|---|
| TC-1 | `order_total(20)` | `26` | Normal: pays $6 shipping |
| TC-2 | `order_total(34)` | `40` | One dollar below the boundary: still pays shipping |
| TC-3 | `order_total(35)` | `35` | The boundary: "or more" means 35 ships free |
| TC-4 | `order_total(36)` | `36` | One dollar above the boundary |
| TC-5 | `order_total(0)` | `ValueError` | Invalid: an order of nothing |
| TC-6 | `order_total(-5)` | `ValueError` | Invalid: a negative subtotal |

---

## The two pieces of plumbing

**`import spirit_store`** lets a second file, the test file, use every function in `spirit_store.py`. You call them as
`spirit_store.order_total(20)`. Both files must be in the same folder, and you write the file name without `.py`. You met
`import` once before, `import sys`, in the recursion notes. This is the same statement, pointed at your own file. Your file is
now a small library that other code can reuse.

**`if __name__ == "__main__":`** protects `main()`. When you run a file directly, Python sets the special name `__name__` to
`"__main__"`. When another file imports it, `__name__` is the file's own name instead, so the `if` is False and `main()` does not run.
Without that line, importing the store starts the store. Here is the real output of the test file when `spirit_store.py` ends with a bare
`main()` and there is no input to give it:

```
Order subtotal in dollars: Traceback (most recent call last):
  File "...\test_spirit_store.py", line 7, in <module>
    import spirit_store
  File "...\spirit_store.py", line 23, in <module>
    main()
    ~~~~^^
  File "...\spirit_store.py", line 19, in main
    subtotal = int(input("Order subtotal in dollars: "))
                   ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EOFError: EOF when reading a line
```

In a terminal you would see the prompt and the test file would sit there waiting. The traceback's first location is the `import` line,
which is how you recognize this bug.

---

## Worked example 1: assert

`assert` is a Python statement that checks a condition and crashes with `AssertionError` if it is False.

```python
import spirit_store

assert spirit_store.order_total(20) == 26
assert spirit_store.order_total(35) == 35
assert spirit_store.order_total(36) == 36
print("All asserts passed")
```

With the correct `spirit_store.py`, this prints `All asserts passed`. Now suppose somebody changed `>=` to `>` in `order_total`:

```
Traceback (most recent call last):
  File "...", line 4, in <module>
    assert spirit_store.order_total(35) == 35
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

`assert` is the shortest possible test. It has two weaknesses: it stops at the **first** failure, so you never learn whether line 5 passes, and it does not
say what the actual value was. The next example fixes both.

---

## Worked example 2: a check function and a test file

```python
# test_spirit_store.py
# Test cases for order_total. Every expected value was worked out by hand
# from the store's rule, before running anything.
#
# Run:  python test_spirit_store.py

import spirit_store


def check(label, actual, expected):
    """Print PASS or FAIL for one check. Return 1 if it failed, 0 if it passed."""
    if actual == expected:
        print(f"PASS  {label}")
        return 0
    print(f"FAIL  {label}")
    print(f"        expected: {repr(expected)}")
    print(f"        actual:   {repr(actual)}")
    return 1


def outcome(subtotal):
    """Return the total, or the text "ValueError" if order_total refuses the subtotal."""
    try:
        return spirit_store.order_total(subtotal)
    except ValueError:
        return "ValueError"


failures = 0
failures = failures + check("TC-1 normal order pays shipping", spirit_store.order_total(20), 26)
failures = failures + check("TC-2 one dollar below free shipping", spirit_store.order_total(34), 40)
failures = failures + check("TC-3 exactly the free shipping amount", spirit_store.order_total(35), 35)
failures = failures + check("TC-4 one dollar above free shipping", spirit_store.order_total(36), 36)
failures = failures + check("TC-5 zero is refused", outcome(0), "ValueError")
failures = failures + check("TC-6 negative is refused", outcome(-5), "ValueError")

print()
print(f"{failures} failed")
```

Run from the folder holding both files:

```
PASS  TC-1 normal order pays shipping
PASS  TC-2 one dollar below free shipping
PASS  TC-3 exactly the free shipping amount
PASS  TC-4 one dollar above free shipping
PASS  TC-5 zero is refused
PASS  TC-6 negative is refused

0 failed
```

Now the same test file against the version with `>`:

```
PASS  TC-1 normal order pays shipping
PASS  TC-2 one dollar below free shipping
FAIL  TC-3 exactly the free shipping amount
        expected: 35
        actual:   41
PASS  TC-4 one dollar above free shipping
PASS  TC-5 zero is refused
PASS  TC-6 negative is refused

1 failed
```

Every check runs. The failure names the test case, the expected value, and the actual value. Five of six passed, and **only the boundary caught the bug.**

Three details to notice:

- **`check` returns 1 or 0, and the caller adds it up.** That is the `moves = take_step(moves)` pattern from October 29: pass the value in, get the new value back,
  store it. In Unit 6, once you have lists, the same helper keeps a list of results instead.
- **`outcome` turns a raised `ValueError` into a value `check` can compare.** Testing that bad input is refused is as important as testing that good input works.
- **Labels start with the test case ID.** When a check fails in three weeks, the ID takes you straight back to the table and the reason the case exists.

---

## Worked example 3: testing a whole program with a script

Functions that print or ask for input are harder to test by importing them. Your text adventure's game loop is one of those. For those, the test case is a **script of
input** and the expected output is the **output of a version you trust.**

You already have test scripts from version 1. Before you change anything, save what version 1 prints:

```
cmd /c "python adventure.py < test-scripts\win.txt > test-scripts\win_v1_output.txt"
```

After refactoring, run the same script into a second file and compare the two with `fc`, the Windows file compare command:

```
cmd /c "python adventure.py < test-scripts\win.txt > win_v2_output.txt"
cmd /c "fc test-scripts\win_v1_output.txt win_v2_output.txt"
```

If nothing changed, `fc` says so:

```
Comparing files TEST-SCRIPTS\win_v1_output.txt and WIN_V2_OUTPUT.TXT
FC: no differences encountered
```

If something changed, it prints the lines that differ from each file. Some differences are ones you meant, such as a new `inventory` message. Every other difference is
a regression. Use `cmd /c` in PowerShell, because piping with `Get-Content` can put an invisible character in front of the first command.

---

## The wrong version: a test that proves nothing

A student writes tests for the version with `>`. For the boundary case, they are not sure what to expect, so they run it, see `41`, and type that in:

```python
failures = 0
failures = failures + check("normal order", spirit_store.order_total(20), 26)
failures = failures + check("big order", spirit_store.order_total(50), 50)
failures = failures + check("exactly 35", spirit_store.order_total(35), 41)
print(f"{failures} failed")
```

```
PASS  normal order
PASS  big order
PASS  exactly 35
0 failed
```

**No error, and every test passes.** The customer who orders exactly $35 still pays $6 of shipping they were promised they would not pay. The test suite now **defends**
the bug: when somebody fixes `order_total` correctly, this test will fail and tell them to put the bug back.

The first two tests have a different problem. `20` and `50` are middle values. They pass the buggy code and the correct code equally, so they could never catch a boundary
bug.

---

## Why the wrong version is tempting

**The program is faster than arithmetic.** Running the code gives an exact number instantly. Working it out from the rule takes thought. That thought is the test.

**It feels like the code knows.** It was written to follow the rule, so its output feels authoritative. The whole reason you are testing is that you do not yet know
whether it follows the rule.

**All green feels like done.** A suite where everything passes looks like success. A suite that has never failed has never proven that it can.

**The habit that prevents it:** fill in the Expected column of the table before you write the test file, and before you run the program.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Test case** | An ID, an input, the expected output, and the reason for the case. |
| **Expected output** | What the requirement says should happen, worked out without running the code. |
| **Actual output** | What the code really produced. |
| **Boundary case** | A test at the exact edge of a rule, or one step either side of it. |
| **Regression** | Something that used to work and stopped working after a change. |
| **`assert`** | A statement that crashes with `AssertionError` if its condition is False. |
| **`check`** | The course's helper: prints PASS or FAIL with a label, shows expected and actual, and returns 1 for a failure. |
| **`import`** | Loads another Python file so its functions can be used, as `file_name.function_name()`. |
| **`if __name__ == "__main__":`** | Runs the code under it only when the file is run directly, not when it is imported. |
| **`fc`** | The Windows command that compares two text files and prints their differences. |
| **Outcomes 5.4.4 and 5.4.5** | The WebXam competencies for defining test cases and testing a program with them. |

You may see Python's `unittest` module in real projects, including the text adventure's reference build. It does the same job and is organized with classes, which arrive in
Unit 7. You will be able to read it fully then. Nothing in Unit 4 asks you to write it.

---

## Self-check

**Question 1.** A function `data_charge(gb_used)` follows this rule: the first 10 GB are included, and every whole GB over 10 costs $5. Negative usage is refused with
`ValueError`. Write a test case table with at least six cases, including both sides of the boundary and one invalid input. Do not write any code.

**Question 2.** What does this print, and what does it tell you about the test file, not the function?

```python
def check(label, actual, expected):
    if actual == expected:
        print(f"PASS  {label}")
        return 0
    print(f"FAIL  {label}")
    return 1


failures = 0
failures = failures + check("seven days", 7 * 24, 168)
failures = failures + check("half", 9 // 2, 4.5)
failures = failures + check("tag", "SkaterAva".lower(), "skaterava")
print(failures, "failed")
```

**Question 3.** A test file prints `Order subtotal in dollars:` and then waits, before a single PASS or FAIL appears. What is missing, and from which file?

---

### Answers

**1.** One full-credit table, with every expected value worked out from the rule:

| ID | Input | Expected | Why this case |
|---|---|---|---|
| TC-1 | `data_charge(4)` | `0` | Normal, well under the included amount |
| TC-2 | `data_charge(10)` | `0` | The boundary: 10 GB are included |
| TC-3 | `data_charge(11)` | `5` | One GB over the boundary |
| TC-4 | `data_charge(9)` | `0` | One GB under the boundary |
| TC-5 | `data_charge(25)` | `75` | Normal overage: 15 GB at $5 |
| TC-6 | `data_charge(-1)` | `ValueError` | Invalid |

`data_charge(0)` returning `0` is also a good case. Credit needs both 10 and 11, because `>` against `>=` is invisible from either side alone.

**2.**

```
PASS  seven days
FAIL  half
PASS  tag
1 failed
```

Verified by running. `9 // 2` is `4`, floor division, so the check expecting `4.5` fails. **The failing test is wrong, not the arithmetic.** Whoever wrote it expected `/`
behavior from `//`. A failing test means the code and the expected value disagree, and either one can be the mistake. Checking the expected value against the rule is part of
reading every FAIL.

**3.** `spirit_store.py`, the file being tested, is missing `if __name__ == "__main__":` above its call to `main()`. The `import` line in the test file runs the whole store
file, which calls `main()`, which asks for input. Indent `main()` under that `if`.
