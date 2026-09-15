# Lab U4-01: The Practice Report That Lies
## 145060 Programming · Unit 4 · Week 9

**Gate:** 3 (open tooling), with one rule: **no AI tool may be asked to find or fix these bugs.** The method is what is being
practiced. **Duration:** Build 1, 35 minutes, Monday, November 2. Entry 3 is due at the start of the block on Tuesday.
**Competencies:** 5.4.6 (correct syntax and runtime errors), 5.4.7 (debug logic errors), 5.3.9 (functions).

---

## The scenario

You are trying to practice guitar for at least 30 minutes a day, and a friend wrote you a program that reads your practice log and
reports how you are doing. It crashes halfway through the report. When you fix the crash, the report looks finished, and it is still
wrong in two places that never produce an error.

## What you will build

A corrected `practice_report.py` and a troubleshooting log with one complete Six-Step entry for each of the three bugs.

---

## The files

Copy both files from [`lab-u04-01-files/`](lab-u04-01-files/) into one folder, and run the program from that folder:

- [`practice_report.py`](lab-u04-01-files/practice_report.py), the program
- [`practice_log.txt`](lab-u04-01-files/practice_log.txt), two weeks of practice, fixed width: the date in positions 0-5, minutes in positions 7-9

```
Oct 19  35
Oct 20  40
Oct 21  30
Oct 22   0
Oct 23  20
Oct 24  45
Oct 25  50
Oct 26   0
Oct 27  60
Oct 28  30
Oct 29  75
Oct 30  90
Oct 31  40
Nov 01  35
```

Also make a new file, `troubleshooting-log.md`, from the course template:
[`MCCTC_145060_Template_TroubleshootingLog.md`](../09-project/MCCTC_145060_Template_TroubleshootingLog.md). This is practice. Your v2
log is a separate file in your text adventure repository.

**Read the program before you run it.** Every function has a docstring that says what it promises. Bugs live where the code breaks a promise.

---

## The requirement the program is supposed to meet

> Print the number of days logged, the total practice time, the average per day in whole minutes, the best day with its time, and the
> longest run of days in a row with **at least 30 minutes** of practice. Times of an hour or more print as hours and minutes, like `1 h 5 min`.
> Times under an hour print as minutes, like `45 min`.

---

## Steps

### Step 1. Run it, and commit the broken version

Run `python practice_report.py` and commit the untouched files before you change anything, with the message `Broken version, before troubleshooting`.

**Observable result:** four lines of report, a line that says `39 min` by itself, and a traceback. A commit you can compare against later.

### Step 2. Entry 1, step 1 of the method: identify

In your log, fill in the Identify table for the crash: the command, the input (the log file), what the requirement says the average line of the report should be, and
what actually happened. Paste the traceback exactly.

**Observable result:** a complete Identify table. The Actual row names the exception.

### Step 3. Entry 1, steps 2 and 3: theory and test

The traceback names line 85. **Before you change line 85,** write a theory about the cause, then test it. A good test calls one function by itself and prints
what it gives back, with `repr()`, so you can see exactly what came out.

**Observable result:** a theory, and the real output of a test that confirms or rules it out. If your first theory is wrong, keep it in the log and mark it
WRONG.

### Step 4. Entry 1, steps 4 and 5: fix and verify

Make one change. Then verify: run the program again, **and** check that the other times in the report still format correctly.

**Observable result:** the program runs to the end with no traceback. All seven lines of the report print. Record the before and after of the line you changed, and the
new output.

### Step 5. Entry 2: the streak

The report now says the longest streak is **2** days. Look at the log file and work out the right answer by hand, using the requirement's words, **at least 30
minutes.** Write your hand count in the Expected row before you look at the code again.

**Observable result:** an Identify table with an Expected value you worked out yourself, and an Actual of `2 days`.

### Step 6. Entry 2: theories and tests with tiny logs

Guessing at a streak over fourteen days is slow. Make tiny log files that each test one idea, and point `LOG_FILE` at one at a time. For example, a log of three days
where the middle day has 0 minutes. Before you run each one, write what the requirement says it should print.

**Observable result:** at least two tiny logs, each with its expected streak and its real output recorded in the log. **Warning:** there are two separate bugs affecting
the streak. A test that changes the number without making it right is a real result. Write it down.

### Step 7. Fix, verify, and document both streak bugs

Fix each cause with one change at a time, running after each change, and record which change moved the streak from 2 to what. Entry 2 covers the first cause you fix.
Entry 3 covers the second.

**Observable result:** the corrected program prints this report exactly:

```
PRACTICE REPORT
===============
Days logged:     14
Total practice:  9 h 10 min
Average per day: 39 min
Best day:        Oct 30 (1 h 30 min)
Longest streak:  6 days at 30+ minutes
```

Set `LOG_FILE` back to `practice_log.txt`, delete any line you added only for testing, and commit with the message `Fix three bugs, log entries 1 to 3`.

---

## Acceptance criteria

- [ ] `practice_report.py` prints the report above exactly, from `practice_log.txt`
- [ ] Every fix is the smallest change that fixes a cause. Nothing else in the program was rewritten
- [ ] `troubleshooting-log.md` has three entries, one per bug
- [ ] Every entry has a reproduction, at least one theory, a test with **real pasted output**, the fix before and after, and a verification with real output
- [ ] Entries 2 and 3 each verify with at least one tiny log file, not only the full two-week log
- [ ] At least two commits: the broken version first, the fixed version after
- [ ] No AI tool was asked to find or fix a bug

---

## If it breaks

These are the errors you are likeliest to cause yourself while you work. The three planted bugs are not listed here. Finding them is the lab.

### 1. `FileNotFoundError: [Errno 2] No such file or directory: 'practice_log.txt'`

```
  File "...", line 50, in main
    log = open(LOG_FILE)
FileNotFoundError: [Errno 2] No such file or directory: 'practice_log.txt'
```

**Cause:** Python looks for the log in the folder you ran the program **from**, not the folder the program is saved in. Or `LOG_FILE` still points at a tiny test
log you have since deleted. `cd` into the folder that holds both files, and check the name in `LOG_FILE`.

### 2. `ValueError: invalid literal for int() with base 10: ''`

```
  File "...", line 24, in minutes_on
    return int(line[7:10])
ValueError: invalid literal for int() with base 10: ''
```

**Cause:** one of your tiny test logs has an empty line, usually an extra Enter at the end. A blank line is `"\n"`, not `""`, so the loop tries to read minutes from it.
Delete the empty line. This is not one of the three bugs: the real log has no blank lines.

### 3. `IndentationError: unexpected indent`

```
    average = total // days   # whole minutes
IndentationError: unexpected indent
```

**Cause:** you added a line inside `main()` with **no** indentation. A line at the left edge ends the function, so Python finds the next indented line with nothing to belong
to. Every line that belongs to `main()` is indented one level, four spaces.

### 4. `NameError: name 'longest_streak' is not defined`

```
  File "...", line 91, in <module>
    longest_streak = longer_of(longest_streak, streak)
                               ^^^^^^^^^^^^^^
NameError: name 'longest_streak' is not defined
```

**Cause:** you added a line **below** the call to `main()`, at the bottom of the file. `longest_streak` is local to `main()` and stopped existing when `main()` returned. That
is October 29's scope lesson. Anything that uses `main()`'s variables goes inside `main()`.

---

## Stretch goal

Add a sixth line to the report: `Goal days:  N of 14`, the number of days that met the goal. Write the expected number from the log file first, by hand, then make the program
print it. Log it as an entry only if it did not work the first time.

---

## Submission checklist

- [ ] Report matches the acceptance output exactly
- [ ] Three entries, each with all five required parts and real output
- [ ] Tiny test logs committed alongside the log, so your reproductions can be rerun
- [ ] Pushed, `git status` clean
- [ ] AI usage log states that no AI tool was used to find or fix these bugs

---

# Extended Lab Options

All four assess the same competencies, 5.4.6 and 5.4.7, on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 10 minutes, still no Identify table, or has changed the code before writing a theory | SCAFFOLDED |
| Entry 1 done, working on the streak with tiny logs | STANDARD |
| All three bugs fixed with entries in 20 minutes | EXTENDED |
| Says "I would never write a program like this," or asks when anyone troubleshoots anything but code | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Where to look:** you are told the functions involved. The crash is caused inside `format_minutes`. One streak bug is in `met_goal`. The other is in `main()`,
  somewhere between the loop and the report.
- **Tests given:** run these instead of designing your own tiny logs.
  - `print(repr(format_minutes(39)))`, typed on the line above the call to `main()` in `practice_report.py`, and deleted after you record its output
  - a log of three lines, each `Nov 02  45`, `Nov 03  45`, `Nov 04  45`, which should give a streak of 3
  - a log of two lines, `Nov 02  30` and `Nov 03  30`, which should give a streak of 2
- **Log:** entries 1 and 2 are required in class. Entry 3 may be three sentences: what was wrong, the fix, and the output that proved it.
- **Checkpoints:** show your instructor the Identify table for entry 1 before you change any code, and again after the crash is fixed.

**Acceptance criteria:** the report output exactly, entries 1 and 2 complete, entry 3 in three sentences.

**Grading:** same 100-point scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a requirement that needs something not taught yet.

**Added requirement.** Turn each bug's reproduction into a one-line **`assert`** statement, placed near the bottom of `practice_report.py`, above the call to `main()`. Each assert must
**pass** on your fixed program and **fail** when you temporarily put that one bug back. Put each bug back one at a time, run, paste the failing result into the matching log entry, and
undo it.

**Hint, not the answer.** `assert` is a Python statement that crashes when its condition is False. Read "The assert statement" in the Python Language Reference, simple statements page,
`https://docs.python.org/3/reference/simple_stmts.html` **[VERIFY]** the section name on that page. The streak is worked out inside `main()`, which prints and returns nothing, so an
assert cannot reach it. You may move the streak into its own function that takes a file name and returns the streak, as long as the report still prints exactly the same.

**The honest warning:** tests arrive Thursday. You must be able to explain why each assert fails when its bug is back. An assert that passes either way tests nothing.

**Acceptance criteria:** all STANDARD criteria, plus three asserts, each with a pasted failing run when its bug was put back, and the report still exactly as shown.

---

## APPLIED

**For the student who asks when anybody troubleshoots anything except code.** Same method, completely different domain: IT support.

**Changed scenario.** Pick a real problem with a device or app **you own** that you can safely reproduce: a controller that will not pair, a laptop that will not see a printer, a
playlist that will not sync to your phone, a game that will not launch. No school-owned device settings, no accounts that are not yours, and no changes you cannot undo.

**What you build.** Three log entries using the same template: the reproduction, every theory, a test for each, the fix or the escalation, and the verification. If you cannot fix it,
step 4 is "escalate": write exactly what you would tell a support person, including your reproduction and every theory you ruled out.

**The extra requirement that makes it the same lab.** At least one entry must contain a theory that your test proved WRONG, and the entry must say what that ruled out. **Keep personal
information out:** no account names, email addresses, serial numbers, or network names in the log.

**Acceptance criteria:** three entries meeting the five required parts, one disproved theory, no personal information.

**Grading:** same scale. Correctness is judged on whether each test could really have disproved its theory.
