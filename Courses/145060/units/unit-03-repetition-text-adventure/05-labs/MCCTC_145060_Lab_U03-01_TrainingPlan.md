# Lab U3-01: Training Plan
## 145060 Programming · Unit 3 · Week 7

**Gate:** 3 (open tooling). **Duration:** two Build 1 blocks, 35 minutes each. Part 1 on
Monday, October 19. Part 2 on Thursday, October 22. **Competencies:** 5.3.6 (repetition
control structures), 5.3.8 (nested structures), 5.5.5 (naming and comments), 5.4.7 (debug
logic errors).

---

## The scenario

Tryouts are in six weeks and you are nowhere near ready. The coach says to start slow and add
a few minutes to every run each week, and to run five days a week with Wednesdays and Sundays
off. Working out the whole plan on your phone's calculator takes twenty minutes and you got week
four wrong twice.

## What you will build

A program that asks three questions and prints your full week-by-week running plan, first as a
list and then as a grid, with the total minutes worked out two different ways.

---

## Starter code

Create `training_plan.py` and type this in. It runs. It does nothing useful.

```python
# training_plan.py
# Prints a running plan that builds week by week up to tryouts.
#
# This file runs right now. It does not do anything useful yet.

RUNS_PER_WEEK = 5          # you run five days and rest two
DAY_NAMES = "MonTueWedThuFriSatSun"
REST_DAYS = "Wed Sun"

print("TRAINING PLAN")
print("-------------")

# TODO 1 (Monday): Ask for the minutes per run in week 1, the minutes to add
#                  each week, and the number of weeks until tryouts.

# TODO 2 (Monday): Loop once per week. Work out that week's minutes per run,
#                  print one line for the week, and add the week to a total.

# TODO 3 (Monday): After the loop, print the season total.

# TODO 4 (Thursday): Print the same plan as a grid. One row per week,
#                    one column per day, with rest days marked.

print("No plan yet.")
```

Running it produces:

```
TRAINING PLAN
-------------
No plan yet.
```

**Use your own sport or activity if it fits better.** Swim laps, practice minutes, a skate park
session. The loops are the same. Keep the numbers realistic, and keep five active days and two rest
days so your output can be checked against the examples below.

---

## Part 1: Monday, steps 1 through 6

### Step 1. Starter running and committed
Create the file, run it, commit it.
**Observable result:** three lines of output and a new commit in `git log --oneline`.

### Step 2. Ask the three questions
Replace TODO 1. Convert each answer to a whole number **on the same line you ask**.
**Observable result:** the program asks all three questions and still prints `No plan yet.`

### Step 3. Write the week loop
Replace TODO 2 with a `for` loop over `range` that gives `week` the values 1, 2, 3, and so on, up to
and including the number of weeks. Inside it, print only `Week 1`, `Week 2`, and so on for now.
**Observable result:** with `6` weeks, exactly six lines, `Week 1` through `Week 6`. **Count them.**

### Step 4. Work out each week's minutes
Week 1 uses the starting minutes. Every later week adds one more increase. Work out `minutes_per_run`
for the week, and `week_minutes` for five runs. Print both on the week's line.
**Observable result:** with `20`, `5`, `6`, week 1 shows 20 minutes per run and week 6 shows 45.

### Step 5. Break it on purpose
Change your `range` so it stops one number too early. Run it with `20`, `5`, `6`. Write down how many weeks
printed, what the program said, and whether any error appeared. Put that in a comment at the top of your file,
then fix the `range`.
**Observable result:** a comment recording that tryout week vanished with no error message.

### Step 6. The season total, then commit
Replace TODO 3 with an accumulator: set it before the loop, add each `week_minutes` inside the loop, print it
after. Remove the `No plan yet.` line.
**Observable result:** with `20`, `5`, `6`, the season total is **975 minutes**. Commit.

### Acceptance criteria, Part 1
1. `python training_plan.py` runs with no traceback
2. With `20`, `5`, `6`, it prints six week lines and `Season total: 975 minutes`
3. The step 5 comment records the silent missing week

---

## Part 2: Thursday, steps 7 through 11

### Step 7. Print the header row
Below the Part 1 output, print a header: the word `Week`, then the seven day names. Use a `for` loop over
`range(7)` and take each three-letter day name out of `DAY_NAMES` with a slice.
**Observable result:** `Week   Mon  Tue  Wed  Thu  Fri  Sat  Sun`, with the names lined up in columns five
characters wide.

### Step 8. One row per week
Add a second week loop. For each week, build a string that starts with the week number. Print it.
**Observable result:** six lines, each showing only its week number.

### Step 9. The inner loop
Inside the week loop, add a loop over the seven days. For each day, add either `rest` or that week's minutes to
the row string, five characters wide. Use `in` to check whether the day name is in `REST_DAYS`.
**Observable result:** every row has seven columns, with `rest` under Wed and Sun.

### Step 10. Add up the grid, and check it against Part 1
Count minutes inside the inner loop as you build the row. Print the grid total after both loops.
**Observable result:** `Grid total: 975 minutes`, which matches Part 1. **If the two totals disagree, one of your
loops is wrong.** That is a test you built into your own program.

### Step 11. Break it on purpose, then commit
Move the line that starts each row string so it sits **above the week loop** instead of inside it. Run it. Write what
happened to the rows in a comment. Put the line back. Commit.
**Observable result:** a comment describing rows that grow longer and longer, and a clean grid after the fix.

### Acceptance criteria, Part 2
4. The grid has one row per week and seven aligned columns with rest days marked
5. The grid total equals the Part 1 season total for at least two different sets of answers
6. The step 11 comment records what a misplaced reset does

---

## Acceptance criteria, full lab

- [ ] Runs with no traceback on reasonable whole-number answers
- [ ] Part 1 prints every week, including the last one, and a correct season total
- [ ] Part 2 prints the grid with rest days and a grid total that matches Part 1
- [ ] Every loop's `range` is correct, and you counted the output lines to prove it
- [ ] Steps 5 and 11 are recorded in comments
- [ ] Names say what they hold. No `x`, `i2`, or `temp`
- [ ] At least three commits with messages saying why

---

## If it breaks

### 1. The last week is missing and there is no error

```
Week 5: 5 runs x 40 min = 200 min
Season total: 750 minutes
```

**Cause:** `range(1, weeks)` stops **before** `weeks`. To include the last week, the stop is `weeks + 1`. This is step 5,
and it is the most common mistake in the lab.

### 2. There is a Week 0

```
Week 0: 5 runs x 15 min = 75 min
```

**Cause:** `range(weeks)` starts at 0. Nobody runs in week zero. Use `range(1, weeks + 1)`.

### 3. `TypeError: can only concatenate str (not "int") to str`

```
    for week in range(1, weeks + 1):
                         ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

**Cause:** `weeks` is still the text from `input()`. Wrap the `input()` in `int()` on the same line.

### 4. `ValueError: invalid literal for int() with base 10: 'six'`

**Cause:** somebody typed a word. Handling that without crashing is a validation loop, which is Wednesday's lesson.
For this lab, type whole numbers. Record it under stretch goals if you want to fix it later.

### 5. Every row is longer than the last

```
   20   20 rest   20   20   20 rest
   20   20 rest   20   20   20 rest   25   25 rest   25   25   25 rest
```

**Cause:** the row string is set **above** the week loop, so it never starts over. It must be set inside the week loop,
above the day loop. This is step 11.

### 6. The season total prints after every week

**Cause:** the `print` for the total is indented inside the loop. Move it left so it runs once, after the loop.

---

## Stretch goal

Add a validation loop so that typing a word, a negative number, or zero weeks is refused and asked again instead of crashing
or printing an empty plan. Wednesday's notes show the pattern.

---

## Submission checklist

- [ ] Runs with no traceback
- [ ] Tested with `20`, `5`, `6` and with one set of your own numbers
- [ ] Output line count checked by hand for both parts
- [ ] Steps 5 and 11 comments present
- [ ] Pushed, `git status` clean
- [ ] AI usage log updated if a model was used at any point

---

# Extended Lab Options

All four assess the same competencies, 5.3.6 and 5.3.8, on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 15 minutes into Part 1, the week loop still prints the wrong count, or they are copying the lecture notes line by line without changing names | SCAFFOLDED |
| Working steadily, asking about formatting rather than about loops | STANDARD |
| Part 1 done in under 20 minutes with the step 5 comment written, or they ask how to make the last week different | EXTENDED |
| Says they do not play a sport, or asks when anyone would ever need a grid | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the three `input` lines are already written and converted. The week loop header for Part 1 is given, with an
  empty body: `for week in range(1, weeks + 1):`.
- **Part 1:** steps 2 and 3 are done for you. Step 5 stays. Do not cut the deliberate break.
- **Part 2:** the header row is given as a single `print` line. The student writes only the week loop, the inner day loop,
  and the grid total.
- **Checkpoints:** show your terminal after step 4 and after step 9.

**Acceptance criteria:** runs; with `20`, `5`, `6` prints six weeks and 975; grid rows have seven columns with rest days; grid
total matches; step 5 comment present.

**Grading:** same 100-point scale, Requirements Fit judged against this list. A complete SCAFFOLDED submission earns what a
complete STANDARD submission earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a requirement that needs something not taught yet.

**Added requirement.** Coaches cut training back right before a big race. Make the **final week** a taper week: half that
week's normal minutes per run, rounded to a whole minute. It must work for any number of weeks, and both the list and the grid
must show the taper.

**Hint, not the answer.** Python has a built-in function that rounds a number to a whole number. Find it in the built-in
functions page of the official documentation, `https://docs.python.org/3/library/functions.html`, and read its description
carefully, especially the sentence about values exactly halfway between two whole numbers.

**Second added requirement.** In a comment, report what your taper gives for a normal week of 45 minutes and for a normal week of
43 minutes, and whether either surprised you.

**The honest warning:** half of 45 is 22.5, and the answer Python gives may not be the one you learned in math class. It will not
crash. It will quietly do something you did not expect. Documenting that earns more than working around it.

**Acceptance criteria:** all STANDARD criteria, plus a taper in the final week of both the list and the grid, plus the comment with
both results.

---

## APPLIED

**For the student who says this does not apply to them.** Same loops, and running was never the point.

**Changed scenario.** Pick any real plan that grows by a fixed amount on a schedule and repeats across days, and build it. Real options:
saving part of a paycheck every week toward a phone, adding practice minutes on an instrument, a reading plan that adds pages per week,
a streak in a language app, reps for a lift that go up each week.

**What you build.** The same two outputs: a line per week with a running total, and a grid of weeks down and days across, with at least
one kind of day that is skipped.

**The extra requirement that makes it the same lab.** Your file starts with a comment block called `The plan` that states the starting
amount, the weekly increase, and which days are skipped, and then states by hand what the final total should be for one set of numbers.
Your program's two totals must both match that hand calculation.

**Acceptance criteria:** all STANDARD criteria applied to your plan, plus `The plan` comment with a hand-calculated total that the program
matches.

**Grading:** same scale. Requirements Fit is judged on whether both totals match the student's own hand calculation.
