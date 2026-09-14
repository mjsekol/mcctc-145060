# Additional Resources · Week 8
## 145060 Programming · October 26-30, 2026
### Topics: algorithms and data structures, recursion, defining functions, return values and scope

Links marked **Confident** or **[VERIFY]**. A site marked Confident with a section marked [VERIFY] means the site is
certainly there and the exact chapter address should be clicked before assigning.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Think Python 3e, the recursion chapter | Tue | On-level | 30 min |
| 2 | Official tutorial: Defining Functions | Wed-Thu | On-level | 20 min |
| 3 | Official docs: `sys.getrecursionlimit` | Tue, Thu | Extension | 5 min |
| 4 | Python Tutor, for recursion and scope | Tue-Thu | Remediation | 15 min |
| 5 | Python for Everybody, the functions chapter | Wed-Thu | On-level | 30 min |
| 6 | A short functions video | Wed | Remediation | under 20 min |
| 7 | Congressional App Challenge official site | Mon | Required for CAC teams | as needed |
| 8 | SQ-07 The Halloween Build | Fri | Extension | 2 blocks |

---

## 1. Recursion, primary reading

**Think Python, 3rd edition** · `https://allendowney.github.io/ThinkPython/` · **Confident** for the book, **[VERIFY]** which chapter introduces recursion
in the third edition before assigning a chapter number.

**What it is.** A free textbook that treats recursion carefully, with stack diagrams that show every paused call.

**Why this one.** Tuesday's trace table is a paper version of a stack diagram. Downey's diagrams show the same thing with real function calls, which is what students
see on Thursday.

**Timing warning.** The chapter uses `def` throughout. Assign it **after Thursday, October 29**, as reading alongside Part 2 of the Recursion notes, not on Tuesday.

**Time.** 30 minutes. **Level.** On-level.

---

## 2. Defining functions, from the source

**The Python Tutorial, More Control Flow Tools, the section on defining functions** · `https://docs.python.org/3/tutorial/controlflow.html` · **Confident** for the
page, **[VERIFY]** the in-page anchor for the functions section.

**Assign a question, not the page.**

> Find the paragraph that explains what a function returns when it has no `return` statement. Copy the name of the value, then write one sentence connecting it to
> Thursday's `Tip saved for later: None`.

**Time.** 20 minutes. **Level.** On-level.

---

## 3. The recursion limit, in the official docs

**Python Standard Library, `sys` module** · `https://docs.python.org/3/library/sys.html` · **Confident.** Find `sys.getrecursionlimit()` and `sys.setrecursionlimit()`
on the page.

**Why this one.** Tuesday says the default limit is about 1,000, and `sys.getrecursionlimit()` printed `1000` on the machine these materials were built on. The documentation
explains what the limit protects against in two sentences. It is a good primary source for the student who asks "why not raise it?"

**Warning worth passing on:** do not let students raise the limit to make a recursive game loop "work." That hides the design problem and can crash Python outright.

**Time.** 5 minutes. **Level.** Extension.

---

## 4. Python Tutor, for recursion and scope

`https://pythontutor.com/` · **Confident.**

After Thursday, paste in Part 2 Example B from the Recursion notes:

```python
def people_ahead(position):
    if position == 1:
        return 0
    return 1 + people_ahead(position - 1)

print(people_ahead(5))
```

Step through it and watch the frames stack up and come back down. It is Tuesday's trace table, drawn by the computer. Then paste Thursday's `UnboundLocalError` example and
watch where Python looks for `moves`.

**Time.** 15 minutes. **Level.** Remediation.

---

## 5. Functions, second reading

**Python for Everybody, the functions chapter** · `https://www.py4e.com/` · **Confident** for the site, **[VERIFY]** the chapter link.

**Why this one.** It separates parameters from arguments and printing from returning in plain language, the two distinctions Wednesday and Thursday depend on.

**Watch for:** examples that use lists or `import`. Skip them.

**Time.** 30 minutes. **Level.** On-level.

---

## 6. A short video

**[VERIFY]** before assigning. No video is named here, because none was confirmed live and under 20 minutes when this file was written. Python for Everybody's free lecture
videos, reached from `https://www.py4e.com/`, include one on functions. Watch it first, confirm the length, and check that its examples do not rely on lists.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 7. Congressional App Challenge

**Official site:** `https://www.congressionalappchallenge.us/` · **[VERIFY].** Confirm this is the official site before sending students to it.

**What it is for this week.** The competition's own rules, eligibility requirements, required materials, and deadline. The course syllabus lists the deadline as October 26,
12:00 pm ET. **The official site is the only authority on the rules.** Nothing in this course's materials states them.

Use it with `09-project/MCCTC_145060_Checklist_CAC_Submission.md`.

**Time.** As needed. **Level.** Required for CAC teams only.

---

## 8. Side quest

**SQ-07 The Halloween Build** unlocks late October. Full description in `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.

**What it is.** Extend a finished text adventure with a state change: a room that changes when you return, an item that goes missing, an exit that appears only after you
visit three other rooms. **Setting is the student's choice and horror is optional.**

**Why it fits here.** It is a v1 extension built from exactly Unit 3's tools, and it is a good Friday task for a student whose v1 is submitted and meets every requirement.
Do not let it replace a v1 requirement that is still missing.

**Also available:** SQ-05 Bug Hunt, for anyone who did not start it last Friday.

**Time.** Two blocks. **Level.** Extension.

---

## For the student who is behind

1. Monday: the Algorithms notes, count and total only, typed and run against `playlist.txt`
2. Wednesday and Thursday: the two Unit 4 lecture notes, typing every example, then printing what each function returns
3. Nothing about recursion until the student can write a function that returns a value. Recursion depends on it

Do not assign all eight resources. Pick the one that matches the day the student missed.
