# Lecture Notes: Acceptance Tests Agreed with Stakeholders
## 145060 Programming · Unit 6 · Week 13 · Thursday, December 3

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W13_AcceptanceTests.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W13_AcceptanceTests.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 5.6.14 (ensure code quality by testing and debugging the application),
5.6.10 (present the system design to stakeholders), with 5.4.4 and 5.4.5 from Unit 4
applied. Latent 145130: 2.15.2 (research with the end user in mind, such as beta testing).

---

## Why this exists

In Unit 4 you wrote test cases to check your own functions. Those tests answered one
question: does my code do what I think it does?

That is not the question the stakeholder asks on December 18. The stakeholder asks: **does
it do what I need?** Those are different questions, and a program can pass the first and
fail the second completely.

An acceptance test answers the stakeholder's question. It is written from the acceptance
criteria they signed, it is agreed with them **before** the code exists, and on demo day it
is the thing that decides whether the project passed. Not your opinion. Not theirs. The
test they agreed to.

---

## The concept in plain language

An **acceptance test** is a check that one acceptance criterion is met, runnable by anyone,
with an expected value that came from the stakeholder.

Three rules make acceptance tests worth having.

1. **The expected value comes from the stakeholder or from arithmetic you did by hand.**
   Never from running your own program and copying what it printed.
2. **Tests are written before the code, and they fail at first.** A failing test on
   December 3 is correct. It is a promise waiting to be kept.
3. **Every criterion has at least one check, and boundaries get a check on both sides.**

### The `check` pattern used in this unit

Classes are Unit 7, so this unit does not use Python's `unittest` module, which needs them.
Every test file uses a small helper instead:

```python
results = []


def check(label, actual, expected):
    """Print PASS or FAIL for one check and remember the result."""
    if actual == expected:
        results.append(True)
        print(f"PASS  {label}")
    else:
        results.append(False)
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")
```

The label always starts with the criterion it checks, such as `AC-2 uneven split rounds up`.
When something fails, the label tells you which promise was broken.

### Agreed means shown to the stakeholder

On Friday your stakeholder reads your criteria and the list of check labels, and signs both.
That meeting is a small version of competency 5.6.10, presenting your design to a
stakeholder. It is also the moment to catch misunderstandings, because changing a check on
December 4 costs one line and changing it on December 17 costs the demo.

When the stakeholder later runs the program on their own data to see whether it works for
them, that is **user acceptance testing**. In industry it is closely related to beta
testing: real users, real data, before the software is declared finished.

---

## The program being tested

All three examples test this function. Save it as `split.py`.

```python
# split.py
# Splits a pizza bill so the group always collects enough to pay it.

def split_bill(total_cents, people):
    """Return what each person pays, in cents, rounded UP so the bill is covered.

    Raises ValueError unless people is 1 to 12.
    """
    if people < 1 or people > 12:
        raise ValueError("people must be 1 to 12")
    return (total_cents + people - 1) // people
```

Money is in **cents** on purpose. Whole numbers of cents avoid the floating point surprises
from Unit 1, such as `0.1 + 0.2` printing `0.30000000000000004`.

---

## Worked example 1: criteria become checks

```python
# Acceptance criteria, agreed with the group before any code was written:
# AC-1  Given a $30.00 bill and 3 people, each pays $10.00.
# AC-2  Given a $10.00 bill and 3 people, each pays $3.34, so $10.02 is collected.
# AC-3  Whatever the bill, people times the share is never less than the bill.

import split

results = []


def check(label, actual, expected):
    """Print PASS or FAIL for one check and remember the result."""
    if actual == expected:
        results.append(True)
        print(f"PASS  {label}")
    else:
        results.append(False)
        print(f"FAIL  {label}: expected {expected!r}, got {actual!r}")


check("AC-1 even split", split.split_bill(3000, 3), 1000)
check("AC-2 uneven split rounds up", split.split_bill(1000, 3), 334)
check("AC-3 bill is covered", split.split_bill(1999, 4) * 4 >= 1999, True)
print(f"{results.count(True)} passed, {results.count(False)} failed")
```

Output:

```
PASS  AC-1 even split
PASS  AC-2 uneven split rounds up
PASS  AC-3 bill is covered
3 passed, 0 failed
```

Where did `334` come from? From AC-2, which the group agreed to: ten dollars split three
ways is $3.333, and rounding **up** makes $3.34. Somebody did that by hand before the code
existed.

---

## Worked example 2: both sides of every boundary

The rule is "1 to 12 people." A boundary has two edges, and each edge needs a check on the
allowed side and the refused side.

```python
# Boundary tests: both edges of "1 to 12 people," and one step past each edge.
import split


def outcome(total_cents, people):
    """Return the share, or 'refused' if split_bill raises ValueError."""
    try:
        return split.split_bill(total_cents, people)
    except ValueError:
        return "refused"


for people, expected in [(0, "refused"), (1, 2400), (12, 200), (13, "refused")]:
    actual = outcome(2400, people)
    if actual == expected:
        print(f"PASS  {people} people -> {actual}")
    else:
        print(f"FAIL  {people} people -> expected {expected}, got {actual}")
```

Output:

```
PASS  0 people -> refused
PASS  1 people -> 2400
PASS  12 people -> 200
PASS  13 people -> refused
```

**`outcome()` is how you test a refusal.** It turns "this raised `ValueError`" into a plain
value, `"refused"`, that `check` can compare. Without it, a refusal would crash the test file
instead of being checked by it.

---

## Worked example 3: which criteria have no test?

A test plan maps every criterion to its checks. Sets from Unit 5 find the gaps.

```python
# A test plan maps every acceptance criterion to at least one check.
criteria = {"AC-1", "AC-2", "AC-3", "AC-4", "AC-5"}
checks = {
    "even split": "AC-1",
    "uneven split rounds up": "AC-2",
    "bill is covered": "AC-3",
    "zero people refused": "AC-4",
}

tested = set()
for label in checks:
    tested.add(checks[label])

print("Criteria with no test:", sorted(criteria - tested))
```

Output:

```
Criteria with no test: ['AC-5']
```

A criterion with no check is a promise nobody will verify. **The gap list must be empty
before the stakeholder signs.**

---

## The wrong version, and what it does instead of an error

Here `split_bill` has a real defect. It rounds to the **nearest** cent, so the group comes
up short. Watch two tests of the same value.

```python
# A broken split_bill: it rounds to the NEAREST cent, so the group comes up short.
def split_bill(total_cents, people):
    """Return what each person pays, in cents."""
    return round(total_cents / people)


share = split_bill(1000, 3)

# The test that cannot fail: its expected value comes from the code under test.
expected = split_bill(1000, 3)
if share == expected:
    print("PASS  uneven split:", share)
else:
    print("FAIL  uneven split:", share)

# The real test: its expected value comes from the stakeholder's AC-2.
if share == 334:
    print("PASS  AC-2 uneven split rounds up")
else:
    print("FAIL  AC-2 uneven split rounds up: expected 334, got", share)
print("Collected:", share * 3, "cents for a 1000 cent bill")
```

Output:

```
PASS  uneven split: 333
FAIL  AC-2 uneven split rounds up: expected 334, got 333
Collected: 999 cents for a 1000 cent bill
```

**The first test passed on broken code.** It compared the function's answer to the
function's answer. It would pass if `split_bill` returned 7, or -40, or 333. It cannot fail,
so it proves nothing.

The second test failed, correctly, because its 334 came from the criterion. The group is one
cent short and somebody at the pizza place is annoyed.

The subtle version of this bug is not calling the function twice. It is running the program,
seeing `333`, and typing `333` into the check as the expected value. **The result is the same:
a test that agrees with the bug.**

---

## Why the wrong version is tempting

**It is fast.** Running the program and pasting its output is quicker than doing arithmetic by
hand.

**It turns red to green.** A failing test feels like a problem. Changing the expected value
makes it pass, and a passing test feels like progress.

**The output looks plausible.** `333` is almost right, and "almost right" is exactly what a
silent bug looks like. Every silent bug this semester looked plausible: `121212`, `202`, a
three-digit season, a sprint plan that started with the chart.

The defense is rule 1, applied every time: **write down where each expected value came from.**
The test plan template has a section for exactly that.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Acceptance test** | A check that an acceptance criterion is met, with an expected value from the stakeholder. |
| **Unit test** | A check that one function works as its author intended. |
| **Expected value** | What the check compares against. Must come from the criterion or hand arithmetic. |
| **Boundary test** | Checks at an edge of an allowed range, on both sides. |
| **Test plan** | A table mapping every acceptance criterion to the checks that prove it. |
| **Test-first** | Writing the tests before the code, so they fail until the code is right. |
| **User acceptance testing** | The stakeholder running the software to confirm it meets their need. |
| **Beta testing** | Real users trying software on real work before it is declared finished. |
| **A test that cannot fail** | A check whose expected value comes from the code it tests. It proves nothing. |

---

## Self-check

**Question 1.** A teammate writes this check. Explain why it proves nothing, and rewrite it.

```python
check("AC-4 group of five", split.split_bill(2500, 5), split.split_bill(2500, 5))
```

**Question 2.** The criterion says "a locker can be reserved for 1 to 5 days." List the four
day values your boundary checks should use, and what each should expect.

**Question 3.** Predict the exact output.

```python
results = []


def check(label, actual, expected):
    if actual == expected:
        results.append(True)
    else:
        results.append(False)
        print("FAIL", label)


check("AC-1", 7 * 3, 21)
check("AC-2", 10 // 4, 2.5)
check("AC-3", len("pizza"), 5)
print(results.count(True), "passed,", results.count(False), "failed")
```

---

### Answers

**1.** The expected value is computed by the same function being tested, so the check compares
the function's answer to itself and passes no matter what it returns. Rewrite it with a value
worked out by hand from the criterion: $25.00 split between 5 people is exactly $5.00.

```python
check("AC-4 group of five", split.split_bill(2500, 5), 500)
```

**2.** `0` should be refused, `1` allowed, `5` allowed, `6` refused. Both edges, and one step past
each edge.

**3.** Output:

```
FAIL AC-2
2 passed, 1 failed
```

`10 // 4` is floor division and gives `2`, not `2.5`. The helper only prints on failure, so the
two passing checks print nothing.
