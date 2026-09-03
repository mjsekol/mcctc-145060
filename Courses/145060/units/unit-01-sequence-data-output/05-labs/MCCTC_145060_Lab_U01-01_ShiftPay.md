# Lab U1-01: Shift Pay
## 145060 Programming · Unit 1 · Week 2

**Gate:** 3 (open tooling). **Duration:** two 40-minute Build 2 blocks, Wednesday
and Thursday. **Competencies:** 5.2.1 (primitive numeric and nonnumeric types), 5.2.2 (scope of
data), 5.2.3 (arithmetic operations), 5.5.7 (read inputs), 5.5.5 (naming
conventions and comments), 5.4.3 (interpret a working program), 5.4.6 (correct
syntax and runtime errors).

---

## The scenario

You work, or somebody you know works, and the hours are different every week. The
paycheck is a surprise until it arrives, and by then you have already decided
whether you could afford the thing you wanted.

You want to know on Sunday night what Friday's check will look like, and how many
more weeks like this one stand between you and the thing you are saving for.

## What you will build

A program that takes your hours and pay rate, works out your pay, and tells you
how many weeks at that rate it takes to afford something specific.

**Wednesday you build it with the numbers written into the file. Thursday you make
it ask.** That order is deliberate. Getting the arithmetic right is one problem and
getting input right is a different one, and doing them at once is how you end up
unable to tell which half is broken.

---

## Starter code

Create `shift_pay.py` and type this in. It runs. It does nothing useful.

```python
# shift_pay.py
# Works out what a week of shifts pays, and how close that gets you to
# something you are saving for.
#
# This file runs right now. It does not do anything useful yet.
# Replace each TODO with real lines.

print("SHIFT PAY")
print("---------")

# TODO 1: Store the number of hours you worked this week in a variable.

# TODO 2: Store your hourly pay rate in a variable.

# TODO 3: Calculate pay before taxes, and store it in a variable.

# TODO 4: Store what you are saving for, and what it costs.

# TODO 5: Calculate how many weeks like this one it takes to afford it.

print("Nothing is calculated yet.")
```

Running it produces:

```
SHIFT PAY
---------
Nothing is calculated yet.
```

**Use real numbers.** Your actual hours, or a real job you know about. A goal you
actually want. The program is more interesting when the answer means something, and
Thursday's testing goes faster when you can tell whether an answer is plausible.

If you do not have a job, use one you could get. Ohio's minimum wage and a
15-hour week is a fine starting point.

---

## Part 1: Wednesday, steps 1 through 6

### Step 1. Get the starter running and committed

Create the file, run it, confirm three lines of output, then commit it.

**Observable result:** `python shift_pay.py` prints the three starter lines.
`git log --oneline` shows a new commit.

### Step 2. Name your hours and your rate

Replace TODO 1 and TODO 2 with two variables. Names a stranger could read.

**Observable result:** the program still runs and still prints the same three
lines, because nothing uses your new variables yet. That is expected.

### Step 3. Calculate the pay

Replace TODO 3. Build the value from the two names above it, not from typed-in
numbers.

**Observable result:** still no visible change. Add a temporary
`print(pay_before_taxes)` to confirm it worked, then decide whether to keep it.

### Step 4. Print what you have, labeled

Print hours, rate, and pay, each with a label saying what it is.

**Observable result:** six lines of output, three of them yours, and every number
has a word next to it explaining what it is.

### Step 5. Add the goal

Replace TODO 4 with two variables: what you are saving for, and what it costs. One
of these is text and one is a number. Notice which is which.

**Observable result:** the program runs with no error. A `SyntaxError` here almost
always means the goal name is missing its quotes.

### Step 6. Calculate the weeks, and commit

Replace TODO 5. Divide the cost by your weekly pay. Print it with a label.

**Observable result:** a number, probably with a long decimal tail like
`0.9006211180124224`. That is correct and it is ugly. Leave it for now. Making
numbers look right is a real topic and it is Unit 5.

Commit with a message that says what the program now does.

### Acceptance criteria, Part 1

1. Running `python shift_pay.py` produces output with no traceback
2. At least five variables, each with a name a stranger could read
3. `pay_before_taxes` and `weeks_needed` are calculated from other variables, and
   no number appears twice in the file
4. Every number printed has a label saying what it is

---

## Part 2: Thursday, steps 7 through 12

### Step 7. Make the hours a question

Replace the hours line so the program asks instead of knowing. Wrap the conversion
around the input on the same line.

**Observable result:** running the program stops and waits for you. Type a number
and press enter, and the rest of the output appears using what you typed.

### Step 8. Test it with a decimal

Run it again and type `13.5` for hours.

**Observable result:** it works, and the pay reflects the half hour. If it crashed
with a `ValueError`, you used `int()`. Hours can be 13.5, so this one needs
`float()`. Fix it and run again.

### Step 9. Make the rate a question

Same treatment.

**Observable result:** two questions, then the output.

### Step 10. Make the goal a question

Two more inputs: what you are saving for, and what it costs.

**Observable result:** four questions. **One of these four must not be converted.**
Work out which one and leave it as text.

### Step 11. Break it on purpose, and write down what happened

Run it and type a word where it wants hours. Type `twelve` instead of `12`.

**Observable result:** a crash, and a specific error message. Copy the last line of
it into your README exactly. Do not fix it. Handling this properly is Unit 4, and
knowing it exists is this week.

### Step 12. Update the README and push

Your README needs: what the program does, the exact command to run it, a real
sample run with the questions and answers shown, and a section called
`Known limitations` containing the error from step 11 and one sentence on when it
happens.

**Observable result:** GitHub shows your README, and a stranger could run this.

### Acceptance criteria, full lab

- [ ] Every value the user supplies is asked for with `input()`
- [ ] Every value used in arithmetic is converted, on the same line it is asked for
- [ ] The goal name is **not** converted, and you can say why
- [ ] `float()` is used where decimals are possible, and you can say why
- [ ] Typing `13.5` for hours works
- [ ] Every prompt says what it wants, including units
- [ ] Running it twice with different answers gives different, correct results
- [ ] README has all four sections including `Known limitations`
- [ ] Three or more commits, messages saying why
- [ ] Committed and pushed

---

## If it breaks

### 1. You typed a word where a number was wanted

```
    hours_worked = float(input("Hours worked this week: "))
ValueError: could not convert string to float: 'twelve'
```

**Cause:** `float()` got text that does not spell a number. This is step 11 and it
is expected. Note that the message differs depending on the converter. `int()`
says `invalid literal for int() with base 10: 'abc'` instead.

### 2. Your answer is repeated text instead of a number

```
Pay before taxes: 141414141414141414141414
```

**Cause:** you forgot to convert. `input()` handed back text, and multiplying text
repeats it. **No error appears**, which is why the acceptance criteria check for the
conversion rather than for the output looking right. Wrap `float()` around the
`input()`.

### 3. Decimal hours crash the program

```
ValueError: invalid literal for int() with base 10: '13.5'
```

**Cause:** you used `int()` where the value can have a decimal part. `int()`
converts text that spells a **whole** number, and `13.5` does not. Use `float()`.

### 4. A name is not defined

```
NameError: name 'pay_before_taxs' is not defined. Did you mean: 'pay_before_taxes'?
```

**Cause:** a misspelling, or the line that creates the name is below the line that
uses it. If Python offers a `Did you mean:`, it is the first. If it does not, check
the order of your lines.

### Not an error: the long decimal

`0.9006211180124224` is arithmetic working correctly. Division produces as many
decimal places as it needs. Controlling how numbers display is Unit 5.

---

## Stretch goal

Two parts, and the second is the interesting one.

**Part A.** Make the weeks number readable. Python has a built-in called `round()`
that takes the value and how many decimal places you want:
`round(weeks_needed, 1)`.

**Part B.** Answer this in your README, in three or four sentences. Your program
says you need `0.9` weeks. Is that a useful answer to the question "how many more
weeks do I have to work?" What number would actually answer it, and what would you
have to do differently to get that number?

There is a real answer to Part B and you have not been taught the tool for it. Say
what you would need, not how to do it. Naming the gap is the point.

---

## Submission checklist

- [ ] `python shift_pay.py` runs and completes with no traceback
- [ ] You have run it at least three times with different answers
- [ ] You have tested `13.5` for hours and it worked
- [ ] You have tested a word for hours and recorded the error in your README
- [ ] `git status` shows nothing uncommitted
- [ ] Pushed, and the GitHub page shows your README
- [ ] AI usage log updated if you used a model at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four versions assess the same competency and grade on the same 100-point
five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still typing the starter at 15 minutes, or every variable is one letter | SCAFFOLDED |
| Working steadily, questions are about wording rather than mechanics | STANDARD |
| Finished Part 1 in 20 minutes, or asked what happens with a decimal before you said | EXTENDED |
| Said out loud that they do not have a job or that this does not apply to them | APPLIED |

---

## SCAFFOLDED

**Changed sections:**

- **Starter code:** TODO 1, 2, and 4 are already filled in with working example
  values. The student writes only the two calculations and the print lines.
- **Steps:** Part 2 drops to two inputs, hours and rate. The goal stays hardcoded.
- **Step 11 stays.** Do not cut the deliberate break. It is the most valuable
  ninety seconds in the lab.
- **Checkpoints:** show you the terminal after step 4 and after step 8.
- **README:** two sections, what it does and how to run it.

**Acceptance criteria:** program runs; hours and rate are asked for and converted;
decimal hours work; every number is labeled; README names the program and gives the
command.

**Grading:** same 100-point scale. Requirements Fit is judged against this
version's list. A student who completes this version fully earns the same grade as
one who completes STANDARD fully.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition that needs a concept you have not been
taught.

**Added requirement.** Your program reports `0.9` weeks, which is not an answer
anybody can act on. You cannot work nine tenths of a week. Make it report the whole
number of weeks you actually have to work, rounded up, so `0.9` becomes `1` and
`3.2` becomes `4`.

**Hint, not the answer.** Rounding up has a specific name in programming, and it is
not `round()`, which goes to the nearest. Python keeps it in a module called `math`.
Read the top of the standard library page at
`https://docs.python.org/3/library/math.html` and look for the function whose
description mentions the smallest integer greater than or equal to the value. You
will need one line to bring the module in and one line to use it.

**Second added requirement.** In your README, write two or three sentences on why
rounding up is correct here and rounding to nearest would be wrong. Use your own
numbers as the example.

**Acceptance criteria:** all STANDARD criteria, plus a whole-number weeks value
that rounds up, plus the README explanation.

**Grading:** same scale. A student who attempts this, fails, and documents the
attempt honestly loses very little. A student who pastes code they cannot explain
fails the course standard on explanation.

---

## APPLIED

**For the student who says this does not apply to them.** Same skills, different
domain, and the point is that the domain never mattered.

**Changed scenario.** Pick anything you personally track that has a rate and a
target. Real options: minutes of practice against a goal for the season, pages read
against a book you want finished, gas money per week against a trip, subscribers or
followers per week against a number you want to hit, calories or protein against a
daily target.

**What you build.** The same program shape: at least five variables, at least two
calculated from others, all user-supplied values asked for with `input()` and
converted deliberately, one value that stays text.

**The extra requirement that makes it the same lab.** Your program must include one
value that **looks like a number and must not be converted**, and your README must
name it and explain why. A jersey number, a room number, a date written as digits,
a course code. Getting this right is the whole point of Thursday.

**Acceptance criteria:** all STANDARD criteria, applied to your domain, plus the
named unconverted value with its justification in the README.

**Grading:** same scale. Requirements Fit is judged on whether the conversion
choices are defensible for the domain the student chose, which is a harder question
than the standard version asks.
