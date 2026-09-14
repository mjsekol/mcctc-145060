# Lab U6-01: Tests for Code You Did Not Write
## 145060 Programming · Unit 6 · Week 13

**Gate:** 3 (open tooling). **Duration:** Build 1, Thursday, December 3, 35 minutes. Individual.
**Competencies:** 5.6.14 (ensure code quality by testing), 5.4.4 and 5.4.5 (define test cases and test
against them), 5.6.2 (processing requirements).

**Files:** `05-labs/lab-u06-01-files/concessions.py` and `test_concessions.py`. Copy both into one folder
in your repository.

---

## The scenario

The Boosters run the concession stand at home basketball games, and last year's team wrote a program that
totals orders. This year's volunteers say the totals "seem off sometimes," and nobody can say when. Before
anybody touches the code, somebody has to find out exactly which promises it breaks.

## What you will build

An acceptance test file, written from the Boosters' acceptance criteria, that shows precisely which criteria
`concessions.py` meets and which it breaks, and a short defect report.

**You are not fixing the program today.** In real teams, the person who finds a defect and the person who fixes
it are often different people. Your job is evidence.

---

## The one rule for this lab

> **Do not open `concessions.py` until step 9.**

If you read the code first, your tests will quietly agree with whatever it does. You will look at `return
min(hot_dogs, drinks)` and write a check that expects exactly that. Tests written from the criteria can catch
the code breaking a promise. Tests written from the code cannot.

---

## The stakeholder's acceptance criteria

The Boosters signed these. They are your only source of expected values.

**Prices**

| Item | Price |
|---|---|
| hot dog | $3.00 |
| nachos | $4.00 |
| pretzel | $3.50 |
| water | $1.50 |
| sports drink | $2.50 |
| candy | $2.00 |

- **AC-1.** Every item costs its listed price. `line_total(item, quantity)` returns price times quantity.
- **AC-2.** A line may have **1 to 20** of one item. A quantity of 0, or 21 or more, is refused with `ValueError`.
  Bigger orders go through the Boosters office.
- **AC-3.** An item the stand does not sell is refused with `ValueError`.
- **AC-4.** Every hot dog paired with **any** drink, water or sports drink, is one combo and saves $0.50.
  Extra hot dogs or extra drinks are not combos.
- **AC-5.** Booster members get 10% off, applied **after** combo savings.
  Example: 2 hot dogs and 2 waters is $9.00. Two combos save $1.00, leaving $8.00. A member pays $7.20.
- **AC-6.** `order_total(order, is_member)` returns the total rounded to cents. An order is a dictionary from
  item name to quantity, such as `{"hot dog": 2, "water": 2}`.
- **AC-7.** An empty order, `{}`, costs nothing.

---

## Starter code

`test_concessions.py` runs right now and checks one thing.

```python
# test_concessions.py
#
# Acceptance tests for concessions.py. You write these from the stakeholder's
# acceptance criteria in the lab handout, NOT from reading the code. If you
# read the code first, your tests will agree with whatever it does.
#
# Run:  python test_concessions.py
#
# This file runs right now. It checks one thing.

import concessions

# One True or False per check, so the summary can count them.
results = []


def check(label, actual, expected):
    """Print PASS or FAIL for one check and remember the result."""
    if actual == expected:
        results.append(True)
        print(f"PASS  {label}")
    else:
        results.append(False)
        print(f"FAIL  {label}")
        print(f"        expected: {expected!r}")
        print(f"        actual:   {actual!r}")


def refused(item, quantity):
    """Return 'ValueError' if line_total refuses this line, or the total if it does not."""
    try:
        return concessions.line_total(item, quantity)
    except ValueError:
        return "ValueError"


# AC-1: every item costs its listed price.
check("AC-1 three pretzels", concessions.line_total("pretzel", 3), 10.5)

# TODO AC-2: quantities 1 through 20 are allowed. Test both edges and one step past each.

# TODO AC-3: an item the stand does not sell is refused.

# TODO AC-4: every hot dog paired with ANY drink is a combo.

# TODO AC-5: members get 10 percent off AFTER combo savings.

# TODO AC-6: totals are rounded to cents.

# TODO AC-7: an empty order costs nothing.

print()
print(f"{results.count(True)} passed, {results.count(False)} failed")
```

Running it:

```
PASS  AC-1 three pretzels

1 passed, 0 failed
```

---

## Steps

### Step 1. Run the starter and commit
Put both files in one folder. Run `python test_concessions.py`.
**Observable result:** `1 passed, 0 failed`. Commit.

### Step 2. Read the criteria, not the code
Read AC-1 through AC-7 above. For each one, write on paper or in a comment one input you will test and the exact
value you expect, **worked out by hand**.
**Observable result:** seven expected values, each with the arithmetic that produced it.

### Step 3. AC-1
Add one more AC-1 check for a different item and quantity.
**Observable result:** one more line of output.

### Step 4. AC-2, both edges
Use `refused()` so a refusal becomes the text `"ValueError"` instead of crashing the file. Write four checks: 0, 1,
20, and 21 of one item.
**Observable result:** four new lines. **If any of them says FAIL, do not change the expected value.** The criterion
is the truth. Write it down for step 8.

### Step 5. AC-3
Check that an item the stand does not sell is refused.
**Observable result:** one new line.

### Step 6. AC-4, combos
`concessions.combo_count(order)` returns how many combos an order has. Check at least: hot dogs with waters, hot dogs
with sports drinks, hot dogs with one of each drink, and more hot dogs than drinks. Then check one full
`order_total` that includes sports drinks. Work out every expected value by hand.
**Observable result:** at least five new lines.

### Step 7. AC-5, AC-6, AC-7
Check the AC-5 example exactly as written. Check one member order where the 10% leaves a fraction of a cent. Check the
empty order.
**Observable result:** at least three new lines, and a summary line with more than one number above zero.

### Step 8. Write the defect report
Create `defects.md`. For every FAIL, one row:

```markdown
| Criterion | Input | Expected | Actual | What a volunteer at the stand would see |
|---|---|---|---|---|
```

**Observable result:** a table with one row per failing check. Commit.

### Step 9. Now open the code
Open `concessions.py` for the first time. For each row in your defect report, find the line that causes it and add
its line number to the row. **Do not edit `concessions.py`.**
**Observable result:** every row has a line number. Commit and push.

---

## Acceptance criteria

1. `python test_concessions.py` runs to the end and prints a summary line
2. Every criterion AC-1 through AC-7 has at least one check, labeled with its criterion, and AC-2 has checks at 0, 1,
   20, and 21
3. Every expected value has a comment or a step 2 note showing where it came from, and none came from running the program
4. `defects.md` lists every failing check with input, expected, actual, and a line number, and `concessions.py` is unchanged

---

## If it breaks

### 1. The test file stops partway with a traceback

```
ValueError: we do not sell pizza
```

**Cause:** you called `concessions.line_total("pizza", 1)` directly. A refusal raises `ValueError`, which ends the whole
file. Use `refused("pizza", 1)` so the refusal becomes a value `check` can compare.

### 2. A misspelled helper

```
NameError: name 'chek' is not defined. Did you mean: 'check'?
```

**Cause:** a typo in the function name. Python's suggestion is right.

### 3. A missing argument

```
TypeError: order_total() missing 1 required positional argument: 'is_member'
```

**Cause:** AC-6 says `order_total(order, is_member)`. Pass `True` or `False` as the second argument.

### 4. A refusal you did not expect

```
ValueError: we do not sell Hot Dog
```

**Cause:** item names are lowercase in the price table. `"Hot Dog"` is a different string from `"hot dog"`. Is refusing it a
defect? The criteria do not say, so it is a question for the stakeholder, not a FAIL. Put it in the notes section of your
defect report.

### Not an error: several checks say FAIL

That is the lab working. The volunteers said the totals "seem off sometimes." Your failures are the "sometimes."

---

## Stretch goal

For each FAIL, write the smallest order a volunteer could ring up at a real game that would show the problem, and what the
customer would pay versus what they should pay. One sentence each, in `defects.md`.

---

## Submission checklist

- [ ] Test file runs to the end
- [ ] All seven criteria covered, boundaries on both sides
- [ ] Every expected value has a source
- [ ] `defects.md` complete with line numbers
- [ ] `concessions.py` unchanged
- [ ] Committed and pushed
- [ ] AI usage log updated if a model was used

---

# Extended Lab Options

All four assess 5.6.14 on the same 100-point five-dimension scale, applied to the test file and defect report.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 10 minutes, still has only the starter check, or has opened `concessions.py` "to see what to test" | SCAFFOLDED |
| Writing checks steadily, asking about the criteria rather than the syntax | STANDARD |
| Finished step 7 in under 20 minutes, or asks why `7.2` compares equal to a calculated float | EXTENDED |
| Says "why test somebody else's code" or "I would fix it myself" | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** checks for AC-1, AC-3, and AC-7 are already written. The AC-2 section has the four inputs (0, 1, 20, 21)
  written as comments with the expected results blank.
- **Steps:** step 6 needs only three combo checks: water, sports drink, and more hot dogs than drinks. Step 9 is optional.
- **Checkpoints:** show your instructor the output after step 4 and after step 7.
- **The one rule stays.** Do not open the code before your tests are written.

**Acceptance criteria:** the file runs; AC-2, AC-4, and AC-5 each have checks you wrote; `defects.md` lists every FAIL with
input, expected, and actual.

**Grading:** same scale, Requirements Fit judged against this list. Full completion earns what full STANDARD completion earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition that needs something not taught.

**Added requirement.** Money in this program is a float, and `check` compares with `==`. That works today by luck. Prove it is
fragile, then make your money checks robust.

1. Show in a comment that `0.1 + 0.2 == 0.3` is `False`.
2. Write a `check_money(label, actual, expected)` helper that treats two amounts as equal when they differ by less than half a
   cent, and use it for every dollar amount.

**Hint, not the answer.** The standard library's `math` module has a function whose documentation says it determines whether two
values are close to each other. Read `https://docs.python.org/3/library/math.html` and look for the parameter that sets an
**absolute** tolerance. The default relative tolerance alone is the wrong choice for comparing money near zero, and knowing why is
part of the task.

**Acceptance criteria:** all STANDARD criteria, plus `check_money` used for every dollar comparison, plus one sentence in
`defects.md` explaining why the absolute tolerance matters for a $0.00 empty order.

---

## APPLIED

**For the student who says this does not apply to them.** Every program you will ever depend on was written by somebody else.

**Changed scenario.** Pick a function from any earlier program of yours this semester that you have not touched in at least two
weeks, and pretend someone else wrote it. Before reading its code, write three to five acceptance criteria for it from its README,
its name, and what you remember it was supposed to do. Then test those criteria.

**What you build.** `test_<function>.py` using `check`, with both sides of at least one boundary, and a `defects.md`.

**The extra requirement that makes it the same lab.** Your criteria must be committed **before** you open the function's code. Your
commit history is the proof.

**Acceptance criteria:** all STANDARD criteria applied to your function, plus the commit order showing criteria before code.

**Grading:** same scale. A student who finds a real defect in their own old code has done the lab's hardest version.
