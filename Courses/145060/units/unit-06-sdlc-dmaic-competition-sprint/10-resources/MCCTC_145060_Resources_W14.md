# Additional Resources · Week 14
## 145060 Programming · December 7-11, 2026 · BPA Regional Week
### Topics: nothing new. Review of Week 13, CSV and dictionaries from Unit 5, reading test output

Every URL is marked Confident or [VERIFY]. Click every [VERIFY] link before assigning it.

**Nothing new is introduced this week.** Your teacher is at BPA Regional and a substitute
is running the room. Every resource here reviews something you already learned. If a page
starts teaching something you have never seen, stop reading. You do not need it this week.

**You can use this whole file with nobody to ask.** Items 3, 4, and 5 have their answers at
the bottom of the file. Try each one before you look.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Which lecture note answers my question | Any day | Remediation | 5 min |
| 2 | Automate the Boring Stuff, Chapters 7 and 18 | Mon-Tue | On-level | 25 min |
| 3 | Official docs: `csv.DictReader` | Mon-Tue | On-level | 10 min |
| 4 | Python Tutor: count with a dictionary | Mon | Remediation | 15 min |
| 5 | Practice: read a test file's output | Wed-Fri | On-level | 15 min |
| 6 | Python for Everybody, dictionaries video | Any day | Remediation | under 20 min |
| 7 | SQ-12 Read the Source | Fri | Extension | 1 block |

---

## 1. Which lecture note answers my question

**No link. These are files in your course repository.** Guide rule 4 says to check the
lecture note first when you are stuck. This table tells you which one.

| If you are stuck on | Read this in `03-lecture-notes/` | Part to read |
|---|---|---|
| What goes in a sprint planning meeting or stand-up | `MCCTC_145060_Notes_DMAICAgileWaterfall.md` | The ceremonies table |
| Whether a requirement is testable | `MCCTC_145060_Notes_RequirementsAndAcceptanceCriteria.md` | Worked example 2 |
| Whether your work still fits the days left | `MCCTC_145060_Notes_ConstraintsAndTimelines.md` | Worked example 3 |
| Why a check fails, or how to test a refusal | `MCCTC_145060_Notes_AcceptanceTests.md` | Worked example 2 |

**Why this one.** The notes were written for exactly the situation you are in: a student
who missed class and has nobody to explain it. Type and run the examples. Reading alone
is not enough.

**Time.** 5 minutes to find the part. **Level.** Remediation.

---

## 2. Reading: dictionaries and CSV files with headers

**Automate the Boring Stuff with Python, 3rd edition** · **Confident** for both pages.

- Chapter 7, "Dictionaries and Structuring Data" · `https://automatetheboringstuff.com/3e/chapter7.html`.
  Read only "Checking Whether a Key Exists" and "Setting Default Values."
- Chapter 18, "CSV, JSON, and XML Files" · `https://automatetheboringstuff.com/3e/chapter18.html`.
  Read only "Reading CSV Files" and "Handling Header Rows."

**Why this one.** Lab U06-02 reads `tasks.csv` into dictionaries and counts things. These
four short sections are the Unit 5 skills that lab uses, and nothing more.

**Skip:** JSON, XML, and the chessboard project. Not this week.

**Time.** 25 minutes. **Level.** On-level.

---

## 3. Official documentation: what `DictReader` does with a short row

**`csv.DictReader`** · `https://docs.python.org/3/library/csv.html` · **Confident.**

**Why this one.** `tasks_messy.csv` has rows that are wrong in several ways. You need to
know what Python hands you when a row is short, before your program tries to use it.

**Answer this question, not the whole page.**

> Find `DictReader`. Read what it says about a row that has fewer fields than the header.
> What value goes in the missing spots by default? What happens if your program calls
> `int()` on that value?

Answer at the bottom of this file.

**Time.** 10 minutes. **Level.** On-level.

---

## 4. Interactive practice: count with a dictionary

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Four friends order snacks for a gaming night. Paste this in and **predict both printed
lines before you click Visualize.** Write your prediction down.

```python
orders = [
    {"name": "Player 1", "snack": "pizza", "cost": "4"},
    {"name": "Player 2", "snack": "chips", "cost": "2"},
    {"name": "Player 3", "snack": "pizza", "cost": "4"},
    {"name": "Player 4", "snack": "Pizza", "cost": "4"},
]

counts = {}
for order in orders:
    snack = order["snack"]
    counts[snack] = counts.get(snack, 0) + 1
print(counts)

total = 0
for order in orders:
    total = total + int(order["cost"])
print(total)
```

Then step through it one line at a time. Watch `counts` grow in the right-hand panel.

**Two questions.**

1. How many pizzas does the dictionary say were ordered? How many were really ordered?
2. Why does the second loop need `int()`?

Answers at the bottom of this file.

**Why this one.** This is the same shape as counting tasks by status on the Sprint Board.
It is a different example on purpose, so you practice the pattern without copying the lab.

**Time.** 15 minutes. **Level.** Remediation.

---

## 5. Practice: read a test file's output

**No link.** On Friday you paste your whole test output into `docs/sprint_review_1.md` and
explain every failure. This is practice on output that is not yours.

A team is building a volunteer hours tracker. Their stakeholder signed these criteria:

- AC-1.1 The total counts only rows with a whole number of hours.
- AC-1.2 The average is shown to one decimal place.
- AC-2.1 Every bad row is counted, so the report can say how many were skipped.
- AC-2.2 A bad row is left out of the total.

Their test file printed this:

```
PASS  AC-1.1 total of clean rows
FAIL  AC-1.2 average to one decimal place
        expected: 3.3
        actual:   3.3333333333333335
FAIL  AC-2.1 bad rows are counted
        expected: 1
        actual:   0
PASS  AC-2.2 bad row is left out of the total

2 passed, 2 failed
```

**Answer in writing.**

1. Which criteria are not met yet?
2. For AC-1.2, is the program wrong or is the test wrong? How do you know?
3. A teammate says, "Change the expected value to `3.3333333333333335` and it passes." What
   do you say?
4. For AC-2.1, the program leaves the bad row out, because AC-2.2 passes. It still reports
   `0` skipped. What does that tell you to look for in the code?

Answers at the bottom of this file.

**Why this one.** Reading a FAIL line is a skill. It is tempting to see the word FAIL and
stop. The expected and actual lines together tell you what to fix and where to look.

**Time.** 15 minutes. **Level.** On-level.

---

## 6. Video: dictionaries, explained again

**Python for Everybody** · `https://www.py4e.com/` · **[VERIFY].** The site refused an
automated check when this file was written. Python for Everybody pairs its chapters with
recorded lectures. **[VERIFY]** that, the dictionaries lesson link, and that the video is under 20
minutes.

**For your teacher, before Friday, December 4.** Load the dictionaries video on a lab
machine through district filtering. If it plays and is under 20 minutes, write "checked" next
to this item on the printed copy. If not, cross this item out.

**For you.** If this item is crossed out, skip it. Do not search for a replacement video in
class. Use item 4 instead.

**Why this one.** It is free and it explains dictionaries to beginners. Some students need
to hear an idea said out loud by a person before the written version makes sense.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## On the "current article" slot

**Not filled this week, on purpose.** An industry article would be new content, and this
week introduces none. Week 13's resources already include one.

---

## 7. Side quest

**SQ-12 Read the Source.** Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. It unlocks any time after Unit 4.

**Only on Friday, and only if your team work is fully current.** The Week 14 guide says so.

**What to do.** Follow the catalog: find a small open-source Python project, read it, and write
the report it describes, including one thing you would change and what its license would require
of you.

**Done when** your report is specific enough to quote line numbers, which is the catalog's own
standard.

**Why it fits here.** On Monday, December 14, another team reads your code and you read theirs.
Reading a stranger's code carefully, before anyone asks you to judge it, is the warm-up for that.

---

## For the student who is behind

1. Item 1: find the lecture note part for the thing you are stuck on, and type every example
2. Item 4: Python Tutor with the snack orders, stepped one line at a time
3. Write your question in `docs/question_log.md` with your best assumption, then keep going

Do not try to do all seven items. Pick the one that matches what is stopping you.

---

## Answers

**Item 3.** The missing spots are filled with `None` by default. Calling `int(None)` raises
`TypeError`, so a short row crashes the program unless you check for it first.

**Item 4.**

The program prints:

```
{'pizza': 2, 'chips': 1, 'Pizza': 1}
14
```

1. The dictionary says 2 pizzas under `'pizza'` and a separate 1 under `'Pizza'`. Three pizzas
   were really ordered. `'pizza'` and `'Pizza'` are different strings, so they are different
   keys. This is the same silent bug as Week 13's `"Mon Dec 07"`. Cleaning the text first with
   `.strip().lower()` from Unit 1 fixes it.
2. Every value read from a CSV file is a string. `"4" + "2"` would join text, and `0 + "4"`
   raises `TypeError`. `int()` turns the text into a number you can add.

**Item 5.**

1. AC-1.2 and AC-2.1.
2. The program is wrong. The expected value `3.3` comes from the signed criterion, which says
   one decimal place. The actual value was never rounded. Rounding to one decimal place in the
   program makes the check pass.
3. No. That makes the test agree with the bug, so it proves nothing. Expected values come from
   the stakeholder or from arithmetic done by hand, never from your program's output. If you
   really believe the criterion is wrong, write it in the question log and keep going.
4. Something skips the bad row without adding one to the count. Look at the code that handles
   a bad row. The count is never increased there, or the error is caught and ignored.
