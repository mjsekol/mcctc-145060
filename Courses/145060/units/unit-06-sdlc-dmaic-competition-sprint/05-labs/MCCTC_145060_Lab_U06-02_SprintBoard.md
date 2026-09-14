# Lab U6-02: Sprint Board
## 145060 Programming · Unit 6 · Week 14 · Self-directed

**Gate:** 3 (open tooling). **Duration:** two Build 1 blocks, Monday December 7 and Tuesday December 8.
Individual, sitting with your team. **Competencies:** 5.6.3 (develop and adhere to timelines), 1.8.2
(organize resources), with 5.3.11 and 5.5.7 from Unit 5 applied (read a data file).

**This lab runs with no instructor.** Every step has an observable result you can check yourself. When
you are stuck, use the order in your Week 14 guide: lecture notes, team, another team, then the STUCK board.

**Files:** `05-labs/lab-u06-02-files/sprint_board.py`, `tasks.csv`, and `tasks_messy.csv`. Copy all three into
one folder.

---

## The scenario

This week your team is working without an instructor, and some of you are at BPA Regional on different days.
Stand-ups only help if everyone can see the same answer to "are we on track," and a list of tasks in your head
is not that. A program that reads the team's task list and prints the honest state of the sprint is.

## What you will build

A command-line tool that reads a task list CSV and prints a stand-up board: status counts, remaining work
against capacity, overdue tasks, blocked tasks, and remaining work by role.

**No new syntax.** Everything here is Unit 4 and Unit 5: functions, `try` and `except`, lists, dictionaries,
and `csv.DictReader`.

---

## The data

`tasks.csv` is a sample team's task list:

```
task,owner_role,estimate_blocks,status,due_day
Write project charter,Facilitator,1,done,1
Interview stakeholder,Stakeholder Liaison,1,done,2
Write requirements with acceptance criteria,Stakeholder Liaison,2,done,3
Build timeline on class days,Facilitator,1,done,3
Write failing acceptance tests,Test Lead,2,doing,5
Design functions and data files,Integration Lead,2,doing,6
Read watering log CSV,Integration Lead,2,todo,7
Flag trays overdue for water,Test Lead,3,todo,8
Break coverage report,Stakeholder Liaison,2,blocked,9
Weekly summary printout,Facilitator,2,todo,10
Handle bad rows in the log,Test Lead,2,todo,11
Write README and user help,Facilitator,1,todo,14
```

| Column | Meaning |
|---|---|
| `estimate_blocks` | How many build blocks the task needs. One class day has two: Build 1 and Build 2. |
| `status` | One of `todo`, `doing`, `blocked`, `done` |
| `due_day` | The sprint day it is due. Day 1 is Monday, November 30. Day 15 is Friday, December 18. |

---

## Starter code

`sprint_board.py` runs right now. It prints a header and nothing useful.

```python
# sprint_board.py
#
# Reads the team's task list and prints a stand-up board: what is done, what
# is late, what is blocked, and whether the remaining work fits the days left.
#
# Usage:
#     python sprint_board.py tasks.csv TODAY PEOPLE
#     python sprint_board.py tasks.csv 8 3
#
# This file runs right now. It prints a header and nothing useful.

import csv
import sys

# The sprint runs on class days, not calendar days. Day 1 is Monday Nov 30.
# Weekends and winter break are not in the list, so they cannot be counted.
DAY_LABELS = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
LAST_BUILD_DAY = 14      # Day 15 is acceptance demos, not building
BLOCKS_PER_DAY = 2       # Build 1 and Build 2
STATUSES = ["todo", "doing", "blocked", "done"]

# TODO 1: read_tasks(path) returns (tasks, problems). Each task is a dictionary.
# TODO 2: count_by_status(tasks) returns a dictionary from status to count.
# TODO 3: remaining_blocks(tasks) adds up the estimates of tasks not done.
# TODO 4: capacity(today, people) returns build blocks left for the team.
# TODO 5: overdue(tasks, today) lists tasks due before today that are not done.
# TODO 6: remaining_by_role(tasks) totals the remaining estimate per role.


def main():
    """Read the arguments and print the board. Right now it only prints the header."""
    if len(sys.argv) != 4:
        print("Usage: python sprint_board.py tasks.csv TODAY PEOPLE")
        sys.exit(1)

    today = int(sys.argv[2])
    print(f"SPRINT BOARD | Day {today} of {len(DAY_LABELS)} ({DAY_LABELS[today - 1]})")
    print("=" * 52)
    print("Nothing on the board yet.")


if __name__ == "__main__":
    main()
```

Running it:

```
$ python sprint_board.py tasks.csv 8 3
SPRINT BOARD | Day 8 of 15 (Wed Dec 9)
====================================================
Nothing on the board yet.
```

---

## Part 1: Monday, steps 1 through 6

### Step 1. Run the starter and commit
**Observable result:** the three lines above. Commit.

### Step 2. `read_tasks(path)`
Read `tasks.csv` with `csv.DictReader`. Build one dictionary per row with the keys `task`, `role`, `estimate`,
`status`, and `due_day`. **Convert `estimate` and `due_day` to whole numbers with `int()` the moment you read them.**
Clean `status` with `.strip().lower()`. For now, return `(tasks, [])`. Validation is step 11.

In `main`, print `len(tasks)` temporarily.
**Observable result:** `12`.

### Step 3. `count_by_status(tasks)`
Start a dictionary with every status in `STATUSES` set to 0, then count. Print one line per status.
**Observable result:** `todo` 5, `doing` 2, `blocked` 1, `done` 4.

### Step 4. `remaining_blocks(tasks)`
Add up `estimate` for every task that is not `done`.
**Observable result:** for `tasks.csv`, `16`.

### Step 5. `capacity(today, people)`
Build blocks left from today through `LAST_BUILD_DAY`, **including today**, for the whole team. It must never be
negative.
**Observable result:** `capacity(8, 3)` is `42`, `capacity(14, 1)` is `2`, and `capacity(15, 3)` is `0`.

### Step 6. The status line, then commit
If remaining work is bigger than capacity, print `AT RISK: cut scope or ask for help`. Otherwise print
`Fits, if the estimates are honest`.
**Observable result:** `python sprint_board.py tasks.csv 8 3` prints `Fits`, and `python sprint_board.py tasks.csv 14 1`
prints `AT RISK`. Commit.

### Acceptance criteria, Part 1
1. The program runs with no traceback on `tasks.csv 8 3`
2. Status counts are 5, 2, 1, 4
3. Remaining work is 16 blocks, capacity is 42 on Day 8 with 3 people, and the status line is right for both Day 8 and Day 14

---

## Part 2: Tuesday, steps 7 through 12

### Step 7. `overdue(tasks, today)`
Return the tasks due **before** today that are not done, earliest due day first. Print each with its day, name, and role.
**Observable result:** on Day 8, exactly three tasks, due on Days 5, 6, and 7, in that order.

### Step 8. Break it on purpose
In `read_tasks`, temporarily store `due_day` **without** `int()`, as the text from the file. In `overdue`, compare against
`str(today)` so it runs. Run the board for Day 8.

**Observable result:** tasks due on Days 10, 11, and 14 appear as overdue on Day 8, and **no error appears.** `"10" < "8"`
is `True` for text, because text is compared one character at a time and `"1"` comes before `"8"`. Write what you saw in
your README under `What I learned`. Then put `int()` back and confirm step 7's output returns.

### Step 9. Blocked tasks
Print every task with status `blocked`, or `none`.
**Observable result:** `Break coverage report`, owned by the Stakeholder Liaison.

### Step 10. `remaining_by_role(tasks)`
Total the remaining estimate for each role, and print the roles in alphabetical order.
**Observable result:** Facilitator 3, Integration Lead 4, Stakeholder Liaison 2, Test Lead 7.

### Step 11. Refuse bad rows out loud
Now make `read_tasks` validate. A row is skipped and reported with its spreadsheet line number (the header is line 1)
when the task name is blank, the status is not one of the four, or `estimate_blocks` or `due_day` is not a whole number in
range (estimate 1 to 20, due day 1 to 15). In `main`, refuse a TODAY that is not 1 to 15 and a PEOPLE that is not 1 to 6
with a message instead of a traceback. Print skipped rows at the bottom of the board.

**Observable result:** `python sprint_board.py tasks_messy.csv 3 4` does not crash, reports **4** skipped rows on lines 3,
5, 6, and 7, and counts the row whose status is `Doing ` with a trailing space as `doing`. And
`python sprint_board.py tasks.csv 16 3` prints a message, not a traceback.

### Step 12. Use it for real
Run the board on your own team's `tasks.csv` for today's day number and the number of people present. Paste the output
into today's stand-up entry.
**Observable result:** the board output in `docs/standups.md`. Commit and push.

### Acceptance criteria, Part 2
4. Overdue tasks on Day 8 are exactly Days 5, 6, and 7, earliest first
5. `tasks_messy.csv` is handled with 4 skipped rows named by line, and bad arguments print a message and exit
6. Your team's board output is in the stand-up log, and your README records step 8's silent wrong answer

---

## If it breaks

### 1. Comparing text to a number

```
TypeError: '<' not supported between instances of 'str' and 'int'
```

**Cause:** `due_day` is still the text from the file and `today` is a number. Convert with `int()` when you read the row.
If you "fix" this by turning `today` into text instead, you get step 8's silent wrong answer.

### 2. A column name that does not exist

```
KeyError: 'estimate_blocks'
```

**Cause:** the name you used does not match the header in the CSV exactly. Your team's `tasks.csv` might say `estimate`.
Match the header, character for character.

### 3. Counting a status that was never added

```
KeyError: 'doing'
```

**Cause:** `counts["doing"] = counts["doing"] + 1` on a dictionary that has no `"doing"` key yet. Start every status at 0
first, or use `counts.get(status, 0) + 1`.

### 4. A day that does not exist

```
IndexError: list index out of range
```

**Cause:** TODAY was larger than 15, so `DAY_LABELS[today - 1]` reached past the end. Step 11's range check fixes it.

### Not an error, and worse: Day 0

`python sprint_board.py tasks.csv 0 3` on the starter prints `Day 0 of 15 (Fri Dec 18)`. **No error.** `DAY_LABELS[-1]` is a
valid index meaning "the last item." Step 11's check refuses 0 too.

---

## Stretch goal

Your capacity number assumes every person is present every remaining day. Add an optional fourth argument, blocks lost to
absences, and subtract it. Then answer in your README: what does your team's board say on Day 8 with BPA absences counted,
and does the answer change what your team should do?

---

## Submission checklist

- [ ] Runs with no traceback on `tasks.csv` and `tasks_messy.csv`
- [ ] All six acceptance criteria met
- [ ] README includes `What I learned` with step 8's result
- [ ] Your team's board output is in the stand-up log
- [ ] Committed after each part, and pushed
- [ ] AI usage log updated if a model was used at any point

---

# Extended Lab Options

All four assess 5.6.3 on the same 100-point five-dimension scale.

## Which version to hand a student

This week there is no instructor to hand anything out. **Choose your own version** using these signals, and write which one
you chose at the top of your README.

| What you notice about yourself | Choose |
|---|---|
| At 15 minutes you still do not have step 2 printing `12` | SCAFFOLDED |
| You are working through the steps and checking each observable result | STANDARD |
| Part 1 took under 20 minutes | EXTENDED |
| You think a sprint board is pointless outside this class | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** use this `read_tasks` instead of writing your own in step 2. It does no validation, so step 11 is not required.

```python
def read_tasks(path):
    """Read the task list. Returns (tasks, problems). No validation in this version."""
    tasks = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            tasks.append({
                "task": row["task"].strip(),
                "role": row["owner_role"].strip(),
                "estimate": int(row["estimate_blocks"]),
                "status": row["status"].strip().lower(),
                "due_day": int(row["due_day"]),
            })
    return tasks, []
```

- **Steps:** skip step 10 and step 11.
- **Step 8 stays.** The silent wrong answer is the most important thing in the lab.

**Acceptance criteria:** criteria 1, 2, 3, 4, and 6.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition that needs something not taught.

**Added requirement.** Typing the day number every morning is how a tired team types the wrong day. Make TODAY optional:
when it is left out, the program works out the sprint day number from the computer's real date, and refuses to run on a
weekend or any date outside the sprint with a clear message.

**Hint, not the answer.** The standard library's `datetime` module has a class for calendar dates, a way to get today's date,
and dates can be compared with `==` and found in a list. Read `https://docs.python.org/3/library/datetime.html` and look for
the `date` object. Build a list of the fifteen class dates, in order, and think about what `.index()` gives you.

**The honest warning:** you cannot easily test "today" on a day that is not in the sprint. Write your function so it takes a
date as a parameter, and test it with dates you choose.

**Acceptance criteria:** all STANDARD criteria, plus a function that returns the right day number for any date you pass it and
refuses weekend dates, plus three example dates tested in your README.

---

## APPLIED

**For the student who says this does not apply to them.** Same skill, your own deadline.

**Changed scenario.** Pick a real deadline in your life with several tasks: a college or scholarship application, a car
purchase, a competition entry, a family event you are helping plan. Make your own `tasks.csv` with at least eight tasks and a
due day for each, using real dates you choose in place of the sprint's fifteen days.

**What you build.** The same board, with your own day labels list.

**The extra requirement that makes it the same lab.** Your README must include the board's output for today, and one decision
you made because of it: something you moved, cut, or started earlier.

**Acceptance criteria:** all STANDARD criteria applied to your own task list, plus the decision in your README.

**Grading:** same scale. Requirements Fit is judged on whether the decision follows from the board's output.
