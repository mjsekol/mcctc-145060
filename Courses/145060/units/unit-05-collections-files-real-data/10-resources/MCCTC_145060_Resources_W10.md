# Additional Resources · Week 10
## 145060 Programming · Week 10
### Topics: lists, dictionaries, sets, and tables of dictionaries

Links marked **Confident** or **[VERIFY]**, same standard as every week. A **[VERIFY]** link has
not been confirmed live and must be clicked before it is assigned.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff: lists, then dictionaries | Mon-Tue | On-level | 40 min |
| 2 | Think Python 3e: lists, dictionaries | Mon-Thu | On-level | 35 min |
| 3 | Python Tutor | Mon, Thu | Remediation | 15 min |
| 4 | Official tutorial: Data Structures | Tue-Wed | On-level | 20 min |
| 5 | Official docs: `time.perf_counter` | Wed | Extension | 5 min |
| 6 | Exercism Python track | Any | Practice | 20 min per exercise |
| 7 | A free video on Python dictionaries | Tue | Remediation | under 20 min |
| 8 | SQ-12 Read the Source | Fri | Extension | 1 block |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, the chapters on lists and on dictionaries** ·
`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the third
edition's chapter numbers and paths before assigning.

**Why this one.** Sweigart teaches lists and dictionaries with programs a teenager would write, and
the dictionaries chapter includes a counting program that is the same pattern as Tuesday's lunch vote.

**Skip for now:** anything using `pprint`, or data structures for a board game model if it goes deeper
than nested dictionaries. Tuples, if the chapter covers them, can be skimmed.

**Time.** About 40 minutes for both chapters. **Level.** On-level.

---

## 2. Second reading, more precise

**Think Python, 3rd edition, the chapters on lists and dictionaries** ·
`https://allendowney.github.io/ThinkPython/` · **Confident** for the site, **[VERIFY]** the chapter
numbers.

**Why this one.** Downey is careful about aliasing: two names for one list. Assign the aliasing section to
any student who got Thursday's three-Devs bug and still does not see why.

**Time.** 35 minutes. **Level.** On-level.

---

## 3. Interactive practice, to see aliasing

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Paste Thursday's wrong version and step through it:

```python
players = [
    {"name": "Jaylen", "games": 12, "points": 138},
    {"name": "Sofia", "games": 12, "points": 101},
]
report = []
row = {}
for player in players:
    row["name"] = player["name"]
    report.append(row)
print(report)
```

The diagram draws two arrows from the list to **one** dictionary. That picture fixes the misconception
faster than any explanation. Do the same with Monday's remove-while-looping example.

**Time.** 15 minutes. **Level.** Remediation.

---

## 4. Official documentation

**The Python Tutorial, section 5, Data Structures** ·
`https://docs.python.org/3/tutorial/datastructures.html` · **Confident.**

**Assign a question, not the page:** *Find the section on sets. What does it say you must use to create
an empty set, and why can you not use `{}`?* That settles Wednesday's deliberate error from the primary
source.

**Time.** 20 minutes. **Level.** On-level.

---

## 5. The stopwatch, for the student who wants to time their own code

**`time.perf_counter` in the `time` module documentation** ·
`https://docs.python.org/3/library/time.html#time.perf_counter` · **Confident.**

**Why this one.** Wednesday's timing uses it. The documentation explains why it is the right clock for
measuring short durations, in one paragraph.

**Time.** 5 minutes. **Level.** Extension.

---

## 6. Practice exercises

**Exercism, Python track** · `https://exercism.org/tracks/python` · **Confident** for the track.
Exercism requires a free account.

**Why this one.** Its learning exercises on lists, dictionaries, and sets come with automated tests, which
is how Unit 4 taught students to check their own work. **[VERIFY]** the current names of the lists,
dictionaries, and sets exercises before assigning specific ones.

**Account note.** Students under the age of any account terms should not sign up without checking the
site's current terms and the school's policy. Nothing in this unit requires it.

**Time.** 20 minutes per exercise. **Level.** Practice, on-level to extension.

---

## 7. A free video

**[VERIFY]** No specific video is linked, because none was confirmed live for this pack. Python for
Everybody, `https://www.py4e.com/`, **Confident** for the site, publishes free lecture videos for its
chapters on lists and dictionaries. Find the dictionaries lecture there, confirm it is under 20 minutes,
and watch it yourself before assigning it.

**Level.** Remediation, for a student who needs Tuesday explained a second way.

---

## 8. Side quest

**SQ-12 Read the Source**, from `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. Unlocks any time after
Unit 4.

**Why it fits this week.** Reading a small open-source project with this week's question in mind, "why did
the author choose a list here and a dictionary there," turns data structure choice into something students
spot in real code. Ask them to include one structure choice they would change in their report, with the cost.

---

## For the student who is behind

1. Python Tutor with the three-Devs example, stepped one line at a time
2. The lecture notes for whichever day they missed, with a terminal open, typing every example
3. Gate 1 Reps 01, 03, and 09, in that order

Do not assign all eight resources. A student who is behind and receives eight links opens none of them.

## For the student who is ahead

- Lab U5-01 EXTENDED (`collections.Counter`) and Lab U5-02 EXTENDED (sorting with a key)
- The Sorting Techniques how-to: `https://docs.python.org/3/howto/sorting.html` · **Confident**
