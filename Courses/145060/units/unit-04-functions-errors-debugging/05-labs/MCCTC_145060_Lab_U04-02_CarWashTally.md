# Lab U4-02: The Car Wash Tally, Rebuilt
## 145060 Programming · Unit 4 · Week 9

**Gate:** 3 (open tooling). You may use a model to explain an error message. You may not ask one to refactor the program for you:
the refactor is the skill. **Duration:** two Build 1 blocks, 35 minutes each. **Part 1:** Tuesday of Week 9. **Part 2:** Wednesday of Week 9.
**Competencies:** 5.3.9 (create and call functions), 5.3.10 (error handling), 5.5.1 (data validation), 5.4.5 (test the program using
defined test cases), 5.4.6 (correct runtime errors).

---

## The scenario

The band is washing cars in the school parking lot on Saturday to pay for its spring trip, and a volunteer at the sign keeps the tally on
a laptop. Last year's program works, but it is one long loop with the same twenty lines pasted three times, it crashes if somebody forgets
`goal.txt`, and one accidental Ctrl+C at 2 pm wiped out the running total. You are rebuilding it so it does exactly the same job, in a shape
that can be fixed, and so that nothing a tired volunteer does loses the day's money.

## What you will build

The same car wash tally, refactored into functions, proven to print exactly what the old one printed, with `try` and `except` for every
failure you can see coming and nothing that hides the ones you cannot.

---

## The files

Copy all three files from [`lab-u04-02-files/`](lab-u04-02-files/) into one folder:

- [`car_wash.py`](lab-u04-02-files/car_wash.py), last year's program, written with Unit 3 tools only
- [`goal.txt`](lab-u04-02-files/goal.txt), one line: `500`
- [`wash_script.txt`](lab-u04-02-files/wash_script.txt), a test script of commands and tips

The starter runs. Try it, type `car`, a tip of `5`, then `done`.

**Where this matters for you.** Your text adventure v2 is this lab, bigger: the same game, the same output, a new shape, and failures handled on
purpose. Every step here has a v2 equivalent.

---

# Part 1 · Tuesday · Refactor, then add the failures you can see coming

### Step 1. Save the baseline before you change anything

In PowerShell or the VS Code terminal, from the folder with the files:

```
cmd /c "python car_wash.py < wash_script.txt > before.txt"
```

Open `before.txt`. Commit all four files with the message `Baseline output before refactor`.

**Observable result:** `before.txt` exists and ends with `Washes: 4`, `Raised: $90`, `Still needed: $410`. This file is your test case for the whole
program: every later version must print it exactly.

### Step 2. Find the repeated shapes

Read `car_wash.py`. In a comment at the top, list every block that appears more than once, and the one thing that changes between the copies.

**Observable result:** a comment naming at least three repeated shapes: the tip validation loop, the progress bar, and the price for each vehicle.

### Step 3. `price_for` and `progress_bar`

Write `price_for(vehicle)`, which returns the price or a constant `NO_PRICE` for anything that is not a vehicle. Write `progress_bar(raised, goal)`, which
**returns** the bar as text. Neither function prints anything.

**Observable result:** in a scratch line, `print(repr(progress_bar(250, 500)))` prints a 20-character bar, half `#` and half `-`, in quotes. Remove the
scratch line.

### Step 4. `read_tip` with `try` and `except`

Write `read_tip()`. It asks until a valid tip is typed and returns it as an `int`. Use `try` around `int()` and `except ValueError`, instead of `.isdecimal()`.
Keep both old messages exactly.

**Observable result:** typing `five`, then nothing, then `80`, then `5` prints `Type a whole number of dollars, like 5.` twice, then the donation jar message,
then records a tip of $5.

### Step 5. Type `-5`. In both versions.

Run the original `car_wash.py` and your new version. At the tip prompt, type `-5`.

**Observable result:** write both outputs in a comment. If the two differ, fix yours so it behaves like the original, and say in the comment **why** switching
from `.isdecimal()` to `int()` made them differ.

### Step 6. `main()`, and the long `if` chain collapses

Move the tally into `def main():`, with the state variables inside it. Use `price_for` so that one branch handles every vehicle. Call `main()` at the bottom.

**Observable result:** a loop body of about fifteen lines instead of seventy. The program runs.

### Step 7. Prove it prints the same thing

```
cmd /c "python car_wash.py < wash_script.txt > after.txt"
cmd /c "fc before.txt after.txt"
```

(Your refactored file keeps the name `car_wash.py`. The original is safe in the step 1 commit.)

**Observable result:** `FC: no differences encountered`. If `fc` shows a difference, fix your code until it does not. **Do not edit `before.txt`.**

### Step 8. A missing goal file

Write `read_goal(filename)`. If `open` raises `FileNotFoundError`, print a message and return a constant `DEFAULT_GOAL` of 300. Only `open` goes inside `try`.
Test it by renaming `goal.txt` to `goal_backup.txt`, running, and renaming it back.

**Observable result:** with the file renamed, the tally starts with `No goal.txt found. Using a goal of $300.` and `Goal: $300`. With it back, `fc` still reports no
differences. Commit: `Part 1: functions, tip and goal file handling`.

---

# Part 2 · Wednesday · Narrow excepts, and the failures you did not see coming

### Step 9. Find your terminal's kill switch first

In VS Code, find the **trash can icon** on the terminal panel. It kills the running program and the terminal. You will need it in step 11.

**Observable result:** you can point to it.

### Step 10. Paste in the AI's "robust" version

A volunteer asked an AI assistant to make `read_tip` "robust so the tally never crashes," and got this. Replace your `read_tip` with it:

```python
def read_tip():
    """Ask until a whole-dollar tip from 0 to MAX_TIP is typed. Return it as an int."""
    # Robust version: any problem at all is caught, so the tally never crashes.
    while True:
        try:
            tip = int(input(f"Tip in whole dollars, 0 to {MAX_TIP}: ").strip())
            if tip >= 0 and tip <= MAX_TIP:
                return tip
            print(f"Tips over ${MAX_TIP} go in the donation jar, not the tally.")
        except:
            print("Type a whole number of dollars, like 5.")
```

Run it: `car`, `five`, `5`, `done`. Then run it again: `car`, and at the tip prompt press **Ctrl+C**, twice. Then type `5` and `done`.

**Observable result:** the first run works. In the second run, write down what Ctrl+C did. It should have stopped the program.

### Step 11. Break it the way real code breaks

In the pasted function, change `MAX_TIP` on the `if` line to `MAX_TIPS`, a typo. Run it, type `car`, then type `5` three times. Then kill the terminal with the trash
can.

**Observable result:** a comment recording exactly what the program said to a correct tip of `5`, and whether any error message appeared. Then undo the typo.

### Step 12. Narrow it

Rewrite `read_tip` so that **only** `int(...)` is inside `try` and the `except` names `ValueError`, like your Part 1 version. Now put the `MAX_TIPS` typo back in and run it
once more.

**Observable result:** a `NameError` traceback naming the line and suggesting `MAX_TIP`. Paste its last line in a comment, with one sentence on why this crash is better
than step 11. Fix the typo.

### Step 13. Ctrl+C and the end of input, on purpose

Run your program with a script that has **no** `done` line. Make one, `no_done.txt`, with three lines: `car`, `5`, `truck`. Run
`cmd /c "python car_wash.py < no_done.txt"`.

Then write `read_line(prompt)`, which returns the typed text trimmed and lowercased, or `"done"` if `input` raises `EOFError` or `KeyboardInterrupt`. Use it for the command
prompt and inside `read_tip`. If the volunteer stops at a tip prompt, the wash is not recorded, and the totals still print.

**Observable result:** before the change, `EOFError` and no totals. After, the run ends with `That wash was not recorded.`, then `Washes: 1`, `Raised: $15`,
`Still needed: $485`.

### Step 14. The goal file you did not anticipate

Change `goal.txt` to say `five hundred`. Run. Then change it to `0`, run, and type `car` and `5`. Each is a failure nobody planned for. **Decide on purpose** what the tally
should do for each, and make it do that, with a message that names the file. Do not use a bare `except` or `except Exception`.

**Observable result:** neither file content crashes the tally. Each prints a message naming `goal.txt` and what it should hold. Put `goal.txt` back to `500`, run step 7's
`fc` one last time, and commit: `Part 2: narrow excepts, EOF and Ctrl+C, bad goal file`.

---

## Acceptance criteria

- [ ] `fc before.txt after.txt` reports no differences, after Part 1 **and** after Part 2
- [ ] At least five functions, including `price_for`, `progress_bar`, `read_tip`, `read_goal`, and `main`. Only `main` holds the running totals
- [ ] `progress_bar` and `price_for` return values and print nothing
- [ ] A tip of `-5` is refused
- [ ] A missing `goal.txt`, a `goal.txt` of `five hundred`, and a `goal.txt` of `0` each give a message naming the file, and none crash
- [ ] A script with no `done`, and Ctrl+C at any prompt, end with the totals printed
- [ ] No bare `except:`, no `except Exception:`, and every `try` block holds only the line that can raise the exception it names
- [ ] The step 5, 11, and 12 comments are present
- [ ] At least three commits: baseline, Part 1, Part 2

---

## If it breaks

### 1. The bar shows `None`

```
> Tip in whole dollars, 0 to 50: --------------------
Car $10 + tip $5. Raised $15 [None]
```

**Cause:** `progress_bar` prints the bar instead of returning it. The bar appears on its own line, and the call hands `None` to the f-string. No error. This is the bug from Thursday of
Week 8. Replace the `print` with `return`.

### 2. `TypeError: progress_bar() missing 1 required positional argument: 'goal'`

```
    print(f"{label_for(command)} ${price} + tip ${tip}. Raised ${raised} [{progress_bar(raised)}]")
                                                                           ~~~~~~~~~~~~^^^^^^^^
TypeError: progress_bar() missing 1 required positional argument: 'goal'
```

**Cause:** the call passes one argument and the `def` line asks for two. The message names the missing parameter. Your names and line may differ.

### 3. `UnboundLocalError: cannot access local variable 'raised' where it is not associated with a value`

```
  File "...", line 90, in add_wash
    raised = raised + price + tip
             ^^^^^^
UnboundLocalError: cannot access local variable 'raised' where it is not associated with a value
```

**Cause:** a function tries to add to a running total that lives outside it. Any name a function assigns to is local for the whole function. Pass the total in and return the
new total, or keep the adding inside `main`. The notes from Thursday of Week 8 have this exact error. Your names and line may differ.

### 4. `fc` reports `Suv $15` where `before.txt` says `SUV $15`

```
Comparing files before.txt and AFTER.TXT
***** before.txt
Tip in whole dollars, 0 to 50: Type a whole number of dollars, like 5.
Tip in whole dollars, 0 to 50: SUV $15 + tip $10. Raised $40 [#-------------------]
> Tip in whole dollars, 0 to 50: Truck $20 + tip $0. Raised $60 [##------------------]
***** AFTER.TXT
Tip in whole dollars, 0 to 50: Type a whole number of dollars, like 5.
Tip in whole dollars, 0 to 50: Suv $15 + tip $10. Raised $40 [#-------------------]
> Tip in whole dollars, 0 to 50: Truck $20 + tip $0. Raised $60 [##------------------]
*****
```

**Cause:** `"suv".title()` is `Suv`. The original typed `SUV` by hand. No error, and only the comparison catches it, which is the reason step 1 exists. The label needs its own
rule for SUV.

### 5. `ZeroDivisionError: integer division or modulo by zero`

```
  File "...", line 76, in progress_bar
    filled = raised * BAR_WIDTH // goal
             ~~~~~~~~~~~~~~~~~~~^^~~~~~
ZeroDivisionError: integer division or modulo by zero
```

**Cause:** `goal.txt` says `0`. This is step 14. The fix is a decision about what a goal of 0 means, not an `except` around the division.

### 6. The program will not stop and fills the screen

**Cause:** a bare `except` is catching `EOFError` or Ctrl+C. Kill the terminal with the trash can icon, then narrow the `except`.

---

## Stretch goal

Add a `report` command that prints the running totals without ending the tally, and a matching line in `wash_script.txt`. You will need a new baseline. Explain in a comment why
changing the test script means `before.txt` must be regenerated **from the original program**, and what goes wrong if you regenerate it from your refactor instead.

---

## Submission checklist

- [ ] `before.txt` committed in the first commit and never edited
- [ ] `fc` output after Part 2 pasted in a comment at the bottom of `car_wash.py`
- [ ] Steps 5, 11, 12, and 14 comments present
- [ ] Pushed, `git status` clean
- [ ] AI usage log updated for any explanation you asked a model for

---

# Extended Lab Options

All four assess the same competencies, 5.3.9 and 5.3.10, on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 15 minutes on Tuesday, no function written, or `main()` not yet attempted and `fc` never run | SCAFFOLDED |
| `fc` passing by the end of Tuesday's block | STANDARD |
| Part 1 done in 20 minutes, or asking how to test `read_tip` without typing | EXTENDED |
| Says they will never run a car wash, or asks what else is shaped like this | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the `def` lines and docstrings for `price_for`, `progress_bar`, `read_tip`, `read_goal`, and `main` are given, with empty bodies of `pass`. Your job is to move the
  existing code into them.
- **Steps:** steps 2 and 14 are skipped. Step 13 covers `EOFError` only. Ctrl+C is not required.
- **Checkpoints:** show your instructor the step 1 commit, a passing `fc` at the end of Part 1, and a passing `fc` at the end of Part 2.

**Acceptance criteria:** `fc` passes after both parts; the five functions; `-5` refused; missing `goal.txt` handled; a script with no `done` prints totals; no bare `except`.

**Grading:** same 100-point scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a requirement that needs something not taught yet.

**Added requirement.** Test `read_tip` **without typing anything.** Write a short test file that feeds `read_tip` a planned list of inputs, including `five`, `-5`, `80`, and `5`,
and checks that it returns 5. Then test that pressing Ctrl+C at the tip prompt returns your stop value.

**Hint, not the answer.** Python's standard library can temporarily replace a built-in function such as `input` during a test. Read about `unittest.mock.patch` in the official
documentation, `https://docs.python.org/3/library/unittest.mock.html`, and look for how `side_effect` can return a different value, or raise an exception, on each call.

**The honest warning:** this uses a list for `side_effect` and a `with` statement, both beyond Unit 4. You must be able to explain each line. If you cannot, stop at STANDARD.

**Acceptance criteria:** all STANDARD criteria, plus a test file that runs with no typing, passes, and fails when `read_tip` goes back to the bare-`except` version.

---

## APPLIED

**For the student who asks what else is shaped like this.** Same skills, different domain.

**Changed scenario.** Pick a Unit 3 style program of your own from this semester: your Lab U3-02 or U3-03 solution, your Unit 2 decision engine, or your CLI Toolsmith. Anything with repeated code and at
least one `int()` or `open()`.

**What you build.** Steps 1 through 14 applied to your program: a committed baseline from a script, at least three functions, `fc` proving identical output, `try` and `except` for every
anticipated failure, and a decision recorded for at least one failure you did not anticipate.

**The extra requirement that makes it the same lab.** A comment at the top listing every input your program reads and, for each, what can go wrong and which line handles it. That list is the
same failure inventory your text adventure v2 needs.

**Acceptance criteria:** all STANDARD criteria, applied to the student's program, plus the failure inventory.

**Grading:** same scale. Requirements Fit is judged against the student's own failure inventory.
