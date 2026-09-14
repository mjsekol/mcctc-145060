# Additional Resources · Week 6
## 145060 Programming · October 12-15, 2026
### Topic: match and case, machine learning against decision trees, modeling, and while loops

Links marked **Confident** or **[VERIFY]**, same standard as every week. **Confident** here means the
URL returned a working page with the expected title when this file was built on September 14, 2026.
Click each one once before assigning it.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | PEP 636, Structural Pattern Matching: Tutorial | Mon | Extension | 25 min |
| 2 | Official docs: `match` statements | Mon | On-level | 10 min |
| 3 | Google for Developers, Decision Forests course: Decision trees | Tue | Extension | 20 min |
| 4 | scikit-learn user guide: Decision Trees | Tue | Extension | 15 min |
| 5 | Automate the Boring Stuff 3e, Chapter 3: Loops | Thu | On-level | 30 min |
| 6 | PY4E video: Loops and Iteration, Part 1 | Thu | Remediation | 10 min |
| 7 | Python Tutor | Thu | Remediation | 15 min |
| 8 | SQ-06 Flowchart the Thing You Already Built | Wed on | Side quest | 1 block |

---

## Monday · match and case

### 1. PEP 636, the official pattern matching tutorial

`https://peps.python.org/pep-0636/` · **Confident.**

**What it is.** The tutorial written by the people who added `match` to Python, built around a text adventure's command parser.

**Why this one.** It is the primary source for the EXTENDED option of Lab U2-02, and its running example is a game that reads
commands like `go north`, which is where Unit 3 is headed.

**Warning worth passing on.** It moves fast into sequence patterns, class patterns, and dictionaries. Tell students to read until
the first example that uses a list or a class, and stop. It also explains the capture-pattern behavior from Monday's bug, which is
worth pointing a curious student to.

**Level.** Extension. 25 minutes.

### 2. Official docs: the tutorial section on `match`

`https://docs.python.org/3/tutorial/controlflow.html#match-statements` · **Confident.**

**Assign a question, not the page.**

> Find the sentence that says `_` acts as a wildcard. Then find where the page says a variable in a pattern "binds a value from
> the subject." Copy both sentences into your notes and explain, in your own words, how the second one causes Monday's snack bar bug.

**Level.** On-level. 10 minutes.

---

## Tuesday · how machine learning differs from a hand-written decision tree

### 3. Google for Developers, Decision Forests course, "Decision trees"

`https://developers.google.com/machine-learning/decision-forests/decision-trees` · **Confident.**

**What it is.** A page from Google's free machine learning course material showing decision trees as a machine learning model:
trees whose questions and thresholds are learned from data.

**Why this one.** It is the honest complication from Tuesday's notes, from a primary source: decision trees are not the opposite of
machine learning, and a training process can build one. A student who read Tuesday's notes and asks "then what is the difference?"
should read this.

**Honest note.** It assumes some vocabulary the course has not taught, such as "features" and "labels." Tell students that features
are the inputs and labels are the known right answers, and that is enough to follow it.

**Level.** Extension. 20 minutes.

### 4. scikit-learn user guide, Decision Trees

`https://scikit-learn.org/stable/modules/tree.html` · **Confident.**

**What it is.** The documentation for a widely used Python machine learning library's decision tree models.

**Why this one.** Scroll to the first diagram of a trained tree and show it on the projector. Every box is a question with a threshold,
exactly like a student's Decision Engine, except that no person chose those thresholds. That one picture does Tuesday's lesson in ten
seconds. **Students do not install or run the library.** It is not part of this course.

**Level.** Extension, instructor projection. 15 minutes.

---

## Wednesday · modeling before code

No external reading is assigned for Wednesday. The notes and the Storm Relay slice are the whole lesson, and the day is deliberately
paper only. Resource 8 is the follow-up.

---

## Thursday · while loops

### 5. Automate the Boring Stuff with Python, 3rd edition, Chapter 3: Loops

`https://automatetheboringstuff.com/3e/chapter3.html` · **Confident.**

**Why this one.** It opens with `while` loops, including an infinite loop and how to escape it, before moving to `for`.

**What to skip.** Everything from `for` loops onward, and `break` and `continue`. The Unit 3 builder schedules those.

**Level.** On-level. 30 minutes for the `while` sections.

### 6. PY4E video: Loops and Iteration, Part 1 (9:59)

`https://www.youtube.com/watch?v=FzpurxjwmsM` · **Confident.** Also linked from `https://www.py4e.com/lessons/loops`.

**Why this one.** It covers `while`, the loop variable, and infinite loops in under ten minutes.

**Honest note.** The PY4E loops chapter also teaches `break` and `continue`, and **[VERIFY]** whether Part 1 of the video reaches
them before assigning it. This course has not taught either one yet. Say so if a student asks.

**Level.** Remediation. 10 minutes.

### 7. Python Tutor

`https://pythontutor.com/` · **Confident.**

Paste the three-laps loop from Thursday's notes and step through it. Count the number of times the arrow enters the loop body. Then
change `<` to `<=` and count again. The off-by-one becomes something a student can see instead of something they are told.

---

## Side quest

### 8. SQ-06 Flowchart the Thing You Already Built

`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`, SQ-06. Unlocks Unit 3, Week 6.

**Why it fits.** Wednesday teaches flowcharts and IPO charts. The quest asks students to flowchart a program they already wrote, and the
Decision Engine was pushed the day before. A student who flowcharts their own engine after the fact sees exactly which dead end the diagram
would have caught.

---

## For the student who is behind

1. **Monday or Tuesday missed:** the notes for that day, then Python Tutor with the notes' wrong version
2. **Wednesday missed:** the Wednesday notes with paper out, and nothing else
3. **Thursday missed:** the PY4E loops video, then the Thursday notes, typing every example

Do not assign all eight resources. Pick one per missed day.
