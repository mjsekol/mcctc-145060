# Lab U5-03: Streak Tracker
## 145060 Programming · Unit 5 · Week 11

**Gate:** 3 (open tooling). **Duration:** two Build 1 blocks, Monday and Tuesday.
**Competencies:** 5.3.11 (access data repositories), 5.5.7 (read inputs from a data file),
5.3.10 (error handling), 5.5.1 (data validation), 5.1.5 (data management).

---

## The scenario

You are tracking habits: practising guitar, reading twenty pages, drinking water before
school. What keeps you going is the streak, the number of days in a row, and it is only
worth anything if it survives closing the program. Months of streaks living in one file
means the program must never destroy that file, no matter how the file gets damaged.

## What you will build

A command-line tracker that loads streaks from JSON, adds a day to the habits you did,
saves them back, and handles a missing, damaged, or nonsense file with a clear message and
without ever writing over data it could not read.

---

## Files you need

From `05-labs/fixtures/`, copy these into your lab folder:

- `streaks.json`, four habits with streaks and best runs
- `streaks_corrupt.json`, the same file cut off partway through
- `streaks_bad_values.json`, valid JSON with one value that makes no sense

**Before you start, make a backup copy of `streaks.json` called `streaks_backup.json`.**
You are going to damage `streaks.json` on purpose, twice.

---

## Starter code

Create `streaks.py`. It runs. It does nothing useful.

```python
# streaks.py
# Tracks habit streaks, days in a row, in a JSON file that survives
# closing the program.
#
# This file runs right now. It does not do anything useful yet.
#
# Part 1 (Monday): read and write JSON.
# Part 2 (Tuesday): a missing, damaged, or wrong file never costs you your data.

import json
import sys

STREAKS_FILE = "streaks.json"


def load_streaks(filename):
    """TODO Part 1: open the file with 'with', json.load it, and return the data."""
    return {"habits": {}}


def save_streaks(data, filename):
    """TODO Part 1: write the data to the file with json.dump and indent=2."""
    pass


def main():
    data = load_streaks(STREAKS_FILE)
    print("STREAK TRACKER")
    print(f"Habits loaded: {len(data['habits'])}")
    # Do not call save_streaks until load_streaks works. Saving the empty
    # starter data would overwrite the real streaks.json.
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Running it produces:

```
STREAK TRACKER
Habits loaded: 0
```

---

## Part 1: Monday, JSON in and out

### Step 1. Starter running, backup made, committed
**Observable result:** the two lines above, `streaks_backup.json` exists, and a commit.

### Step 2. Load the file
Finish `load_streaks` using `with open(...)` and `json.load`.
**Observable result:** `Habits loaded: 4`.

### Step 3. Show the habits
Write `show(habits)` that prints each habit name, its streak, and its best, lined up. Loop
over `.items()`.
**Observable result:** four lines. `Drink water before school` shows 12 days, best 12.

### Step 4. Add a day and save
Write `add_a_day(habits, name)`: add one to the streak, and if the streak is now higher
than the best, raise the best too. Finish `save_streaks`. In `main`, ask for habit names
with `input()` until a blank line, add a day to each one that exists, then save.
**Observable result:** type `Practice guitar`, then Enter. The program says it is at 5
days. Open `streaks.json` in the editor and see `"streak": 5`, spread over several readable
lines because of `indent=2`.

### Step 5. A new habit
If the typed name is not a habit, ask whether to start it. If the answer is `y`, add it with
streak 1 and best 1.
**Observable result:** a new habit appears in `streaks.json` after the run.

### Step 6. Break the file by hand, twice
Open `streaks.json`. Change one habit name's double quotes to single quotes. Run the program
and copy the last line of the error into your README under `What I learned`. Restore the
quotes. Then add a comma after the last habit's closing brace, run it, and record that error
too. Restore `streaks.json` from `streaks_backup.json` and commit.
**Observable result:** two different `JSONDecodeError` messages, each naming a line and a
column. Both recorded in your README.

### Acceptance criteria, Part 1
1. Loads four habits and shows them lined up
2. Adding a day updates the streak and, when beaten, the best, and the change is saved
3. A new habit can be started
4. README records both step 6 errors

---

## Part 2: Tuesday, never lose the data

Right now, your program crashes on a damaged file. That is annoying. Today you make sure it
is never worse than annoying.

### Step 7. A missing file is a first run
Rename `streaks.json` so it is gone, and run the program. Catch `FileNotFoundError` in
`main`: print that there is no file yet and start with no habits.
**Observable result:** no traceback, a message, and after you start one habit and finish,
a new `streaks.json` holding only that habit. Restore the real file from your backup.

### Step 8. Watch a damaged file get eaten, on purpose
Copy `streaks_corrupt.json` over `streaks.json`. In a **scratch copy** of your program, catch
`json.JSONDecodeError` by printing "Starting fresh" and setting the data to
`{"habits": {}}`, and let the program continue to its save. Run it and press Enter at the
first prompt. Open `streaks.json`.
**Observable result:** the damaged file, which still held most of someone's streaks, has
been replaced by an empty habits section. **There was no error.** Write in your README what
was lost and why a person could have repaired the damaged file but cannot repair this one.
Delete the scratch copy.

### Step 9. Catch a damaged file correctly
In your real program, catch `json.JSONDecodeError` and **stop**: print that the file is
damaged, with the line and column from the error, print that nothing was changed, and return
`1` without saving.
**Observable result:** with `streaks_corrupt.json` copied over `streaks.json`, the program
prints two lines and exits. The file is byte-for-byte unchanged afterwards. Check by opening
it.

### Step 10. Valid JSON, nonsense data
Write `check_data(data)` that returns a sentence describing the first problem, or an empty
string when there is none. Check that there is a `habits` dictionary, that every habit has
`streak` and `best`, that both are whole numbers of zero or more, and that best is not lower
than streak. Have `load_streaks` raise `ValueError` with that sentence, and have `main` catch
it, print it, and stop without saving.
**Observable result:** with `streaks_bad_values.json` copied over `streaks.json`, the program
names `Drink water before school` and the value `'twelve'`, and saves nothing.

### Step 11. Put the except clauses in the right order
`json.JSONDecodeError` is a kind of `ValueError`. Make sure the damaged file still gets the
**damaged** message, not the **problem** message. Test it by running step 9's file again.
**Observable result:** the damaged file prints "damaged," not "has a problem." Explain the
order in a comment.

### Step 12. The `true` trap, README, push
Change one streak in a copy of the file to `true` and run. If it loads, your whole-number
check is letting a boolean through. Fix it so it does not. Then add a `Bad files` section to
your README: a table with each kind of bad file you tested and the exact message your
program printed. Restore the real file. Push.

### Acceptance criteria, Part 2
5. Missing file: a message and a fresh start, no traceback
6. Damaged file: a message with line and column, exit, file unchanged
7. Bad values: a message naming the habit and value, exit, file unchanged
8. `"streak": true` is rejected
9. README has step 8's data loss explained and a `Bad files` table from real runs

---

## Acceptance criteria, full lab

- [ ] Runs from the lab folder with no traceback on any of the three fixture files
- [ ] Adds days, raises the best, starts new habits, and saves readable JSON
- [ ] Every file is opened with `with` and `encoding="utf-8"`
- [ ] No code path saves after a failed load
- [ ] `except json.JSONDecodeError` comes before `except ValueError`
- [ ] README has `What I learned` (steps 6 and 8) and `Bad files` (step 12)
- [ ] Commits at the end of each day, pushed

---

## If it breaks

### 1. Single quotes in the JSON

```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 3 column 5 (char 20)
```

**Cause:** JSON requires double quotes. The line and column point at the first single
quote. This is step 6 when you do it on purpose.

### 2. Writing to a file you opened for reading

```
io.UnsupportedOperation: not writable
```

**Cause:** `open(filename)` with no mode opens for reading. Saving needs
`open(filename, "w", encoding="utf-8")`.

### 3. Adding to a streak that is text

```
TypeError: can only concatenate str (not "int") to str
```

**Cause:** the file says `"streak": "twelve"` or `"streak": "4"`, and `+= 1` on a string
fails. JSON gave you exactly what the file said. That is what step 10's check prevents.

### 4. The file has no habits section

```
KeyError: 'habits'
```

**Cause:** the JSON loaded, but it is not shaped the way your program expects, for example
the habits were saved at the top level. Check the shape before you use it.

### Not an error: "No streaks.json yet" when you know you have one

**Cause:** your terminal is in a different folder from the file, so Python did not find it
and your program treated it as a first run. If you save now, you create a second, empty
`streaks.json` in the wrong folder. Check the folder in your terminal prompt.

---

## Stretch goal

A real streak resets to 0 when you miss a day. Add a `missed` command that resets one
habit's streak to 0 and leaves its best alone. Then write in your README why the program
still cannot tell on its own that you missed a day, and what it would need to store to know.

---

## Submission checklist

- [ ] All three fixture files tested, with results in the README
- [ ] `streaks.json` restored to a real file before the final commit
- [ ] `git status` clean, pushed
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Monday, 15 minutes in, still getting `KeyError: 'habits'` or unsure what `json.load` returns | SCAFFOLDED |
| Load and save working; questions are about how to structure the checks | STANDARD |
| Part 1 done Monday and asks "what if the computer crashes during the save" | EXTENDED |
| Says nobody tracks streaks, or asks where saving a file matters at a job | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `load_streaks`, `save_streaks`, and `show` are provided complete.
- **Part 1:** starts at step 4, and step 5 is removed.
- **Part 2:** step 10's `check_data` is provided with two of its checks written; the student
  writes the whole-number check and the best-versus-streak check.
- **Steps 6 and 8 stay.** Breaking the file and watching data get eaten are the lesson.
- **Checkpoints:** show you after steps 4, 9, and 10.

**Acceptance criteria:** adds a day and saves; missing, damaged, and bad-value files each
handled with no save; steps 6 and 8 recorded.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a genuinely harder problem.

**Added requirement.** Your save opens `streaks.json` for writing, which empties it, then
writes. If the program crashes halfway through `json.dump`, the file is left half-written
and the old data is gone. You saw this happen in the Tuesday lecture notes. Make the save
safe: a crash during saving must leave the previous `streaks.json` exactly as it was.

**Hint, not the answer.** Write somewhere else first. Then read the documentation for
`os.replace` in the `os` module, `https://docs.python.org/3/library/os.html#os.replace`, and
look at what it says about replacing a file that already exists.

**How to prove it.** Deliberately put a set into the data before saving, so `json.dump`
raises `TypeError` partway through, and show that `streaks.json` still loads afterwards.

**Added README question.** After your proof runs, is there anything left over on disk? Is
that a problem, and what would you do about it?

**Acceptance criteria:** all STANDARD criteria, a save that survives a mid-write crash, the
proof recorded, and the question answered.

---

## APPLIED

**For the student who asks where saving matters.** The school greenhouse.

**Changed scenario.** The environmental club waters plants on a schedule, and the substitute
on Fridays has no idea what was watered on Thursday. Build `greenhouse.py`, backed by
`plants.json`, where each plant has `days_since_watered` and `water_every_days`. Each run
lists every plant that is due, lets the user type the plants they watered (resetting those
to 0), adds one day to every other plant, and saves.

**The extra requirement that makes it the same lab.** The same three bad files: missing
means a first run, damaged means stop and change nothing, and nonsense values (negative days,
`water_every_days` of 0, text where a number goes) mean stop and name the plant. A README
`Bad files` table from real runs.

**Grading:** same scale and dimensions. Requirements Fit is judged on the greenhouse version
of each acceptance criterion.
