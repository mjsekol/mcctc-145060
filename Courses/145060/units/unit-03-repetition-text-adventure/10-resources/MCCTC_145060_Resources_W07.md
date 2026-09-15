# Additional Resources · Week 7
## 145060 Programming · Week 7
### Topics: for loops and range, the game loop, break and continue, nested loops

Links marked **Confident** or **[VERIFY]**, same standard as every week. A site marked Confident with a section marked
[VERIFY] means the site is certainly there and the exact chapter or page address should be clicked before you assign it.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Python for Everybody, the loops chapter | Mon-Thu | On-level | 30 min |
| 2 | Official Python tutorial: More Control Flow Tools | Mon, Wed | On-level | 20 min |
| 3 | Python Tutor | Mon, Thu | Remediation | 15 min |
| 4 | Automate the Boring Stuff, flow control chapter | Wed | On-level | 30 min |
| 5 | A short loops video | Mon | Remediation | under 20 min |
| 6 | Exercism Python track | Fri | Extension | open |
| 7 | An industry reading on off-by-one errors | Fri | Extension | 15 min |
| 8 | SQ-05 Bug Hunt | Fri | Extension | 1 block |

---

## 1. Primary reading

**Python for Everybody, the chapter on iteration and loops** · `https://www.py4e.com/` · **Confident** for the site,
**[VERIFY]** the chapter link from the site's book or lessons page.

**What it is.** A free textbook written for complete beginners, with `while`, `for`, `break`, `continue`, and the counting and
totaling loop patterns in one chapter.

**Why this one.** Its loop chapter builds the same patterns this week and Monday of next week use: counting, summing, and finding the
largest and smallest. A student who reads it this week is ahead for Monday of Week 8.

**Watch for:** it uses lists in some loop examples. Tell students to skip any example with square brackets. Lists are Unit 5.

**Time.** 30 minutes. **Level.** On-level.

---

## 2. The official tutorial

**The Python Tutorial, section 4, More Control Flow Tools** · `https://docs.python.org/3/tutorial/controlflow.html` · **Confident.**

**What it is.** The official documentation's walk through `if`, `for`, `range()`, `break`, and `continue`, written by the people who maintain
Python.

**Assign a question, not the page.** The page also covers functions and `match`, which students do not need this week.

> Find the part about the `range()` function. Copy the example that uses a step. Then answer in one sentence: is the end point ever part of the
> sequence `range` produces?

That question settles Monday's deliberate error from the primary source.

**Time.** 20 minutes. **Level.** On-level.

---

## 3. Python Tutor

`https://pythontutor.com/` · **Confident.**

**What it is.** A free site that runs a short program one line at a time and draws every variable as it changes.

**Why this one.** Two of this week's bugs are invisible without watching the variables. Paste in Thursday's seating chart and step through the second pass
of the outer loop:

```python
row = 1
seat = 1
while row <= 3:
    while seat <= 4:
        print(f"Row {row}, seat {seat}")
        seat = seat + 1
    row = row + 1
```

The moment `row` becomes 2 and `seat` is still 5 is the whole lesson.

**Time.** 15 minutes. **Level.** Remediation.

---

## 4. Second reading, with games

**Automate the Boring Stuff with Python, the flow control chapter** · `https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the
third-edition chapter address.

**Why this one.** It covers `while`, `break`, `continue`, and `for` with `range` using small interactive programs, which suits Wednesday's validation loops.

**Skip:** anything that uses `import random` or `sys.exit()`. Neither is needed, and `sys.exit()` hides the game loop's report after the loop.

**Time.** 30 minutes. **Level.** On-level.

---

## 5. A short video

**[VERIFY]** before assigning. No specific video is named here, because none was confirmed live and under 20 minutes when this file was written.

**What to look for.** Python for Everybody publishes free lecture videos alongside its chapters, reached from `https://www.py4e.com/` (Confident for the site).
Find the loops lecture, confirm it is under 20 minutes or assign a marked section, and watch it yourself first. It must not use lists for its main examples.

**Why a video at all.** For a student who missed Monday, hearing "up to but not including" from a second voice helps.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 6. Interactive practice

**Exercism, Python track** · `https://exercism.org/tracks/python` · **Confident.**

**What it is.** Free programming exercises with automated tests, and optional human mentoring.

**Why this one.** A student who finishes v1 early gets small, tested loop problems. **Caution:** many exercises assume functions and lists. Point students at
exercises that ask for a single calculation, and tell them to stop at any exercise that needs a list.

**Account note.** Exercism requires an account. Students may create one only under the program's acceptable use rules, and never with anything but their
school account. If in doubt, skip this item.

**Time.** Open. **Level.** Extension.

---

## 7. Why off-by-one errors are famous

**[VERIFY]**. No article is linked here. Search for the phrase **"off-by-one error"** together with **"fencepost."** The fencepost problem (how many posts does a
100-foot fence with a post every 10 feet need?) is the classic explanation, and it appears in many reputable programming references.

**If you cannot find a source you trust in five minutes, run the fencepost question as a Friday discussion instead.** The answer is 11, not 10, and students
who have spent a week on `range(1, n + 1)` will argue about it productively.

**Why this one.** It tells students that this week's bug has a name and a long history, which reframes a frustrating mistake as a known hard problem rather than
a personal failing.

**Time.** 15 minutes. **Level.** Extension.

---

## 8. Side quest

**SQ-05 Bug Hunt** unlocks this week. It is in `Courses/Misc/side-quests/SQ-05-Bug-Hunt/`, with the full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. It is named in the 145060 syllabus as a Unit 3 deliverable.

**Why it fits here.** `torch_run.py` is a game loop with seven planted defects, and several of them are exactly this week's lessons: a loss check that is off by one,
a `playing = False` that does not end the current turn, and a move counter that counts commands that are not moves. A test suite tells students what is wrong but
not where.

**Also this week:** SQ-06 Flowchart the Thing You Already Built, from the catalog, pairs with Monday's design block for a student who wants to check their model
against a program they have already written.

**Time.** One block. **Level.** Extension.

---

## For the student who is behind

1. Python Tutor on Thursday's seating chart, stepping through the second row
2. The lecture notes for the day they missed, with a terminal open, typing every example and counting every output line
3. Lab U3-02 Part 1 again from an empty file, without looking at their old one

Do not assign all eight resources. A student who is behind and gets eight links reads none of them.
