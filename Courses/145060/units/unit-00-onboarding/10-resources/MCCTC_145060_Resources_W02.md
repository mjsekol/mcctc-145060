# Additional Resources · Week 2
## 145060 Programming · September 14-18, 2026
### Topics: evaluating AI output, ownership and licensing, variables and types

**About the links.** Marked **Confident** or **[VERIFY]**, same as Week 1. Broken
links cost a class period, so the marking is honest rather than optimistic.

---

## The week at a glance

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff, Ch. 1 | Wed/Thu | On-level | 30 min |
| 2 | Think Python 3e, Ch. 2 | Wed/Thu | On-level | 25 min |
| 3 | Python Tutor | Wed | Remediation | 15 min |
| 4 | Official docs: built-in functions | Thu | On-level | 10 min |
| 5 | Choose a License | Tue | Extension | 15 min |
| 6 | The tool's own terms of service | Tue | Required | 15 min |
| 7 | Python tutorial, Floating Point appendix | Thu | Extension | 20 min |

---

## 1. Primary reading, variables and types

**Automate the Boring Stuff with Python, Chapter 1** ·
`https://automatetheboringstuff.com/` · **Confident** for the site,
**[VERIFY]** the third-edition chapter path.

**What it is.** Expressions, data types, variables, and the `str`, `int`, and
`float` functions, which is Wednesday and Thursday in one chapter.

**Why this one.** It gives type conversion its own section rather than mentioning
it in passing, and it names the `'12' + 3` error explicitly. That is Thursday's
whole lesson.

**Time.** 30 minutes. **Level.** On-level, and remediation for anyone shaky after
Thursday.

---

## 2. Second reading, sharper

**Think Python, 3rd edition, Chapter 2, "Variables and Statements"** ·
`https://allendowney.github.io/ThinkPython/` · **Confident.**

**Why this one.** Downey is precise about the difference between an assignment
statement and a mathematical equation, which is Wednesday's misconception stated
better than most teachers say it. Assign it to any student who says "but that is
not what equals means."

**Time.** 25 minutes. **Level.** On-level, and the better choice for a strong
student.

---

## 3. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

**Why this one, this week.** Paste in the rebinding example from Wednesday:

```python
shifts = 3
hours_each = 5
total_hours = shifts * hours_each
shifts = 6
```

Step through it one line at a time and watch `total_hours` stay at 15 while
`shifts` changes. The spreadsheet misconception does not survive seeing it.

**Time.** 15 minutes. **Level.** Remediation, and worth assigning to the whole class
Wednesday if the exit ticket goes badly.

---

## 4. Official documentation

**Built-in functions** · `https://docs.python.org/3/library/functions.html` ·
**Confident.**

**Why this one.** Students met `print`, `input`, `int`, `float`, `str`, `type`, and
`round` this week, and every one is on this single page. Assign a question rather
than the page: **find `int()` and read what it says about strings. What does it
require of the text you give it?**

That question is why `int("11.5")` fails, in the official words rather than yours.

**Time.** 10 minutes. **Level.** On-level.

---

## 5. Licensing, for Tuesday

**Choose a License** · `https://choosealicense.com/` · **Confident.**

**What it is.** A plain-language comparison of the common open-source licenses,
maintained by GitHub. It states what each one permits and requires without legal
jargon.

**Why this one.** Tuesday's Build 1 asks students to say in one sentence what MIT,
Apache 2.0, and GPL require. This page is organized to answer exactly that, and it
is a primary-ish source rather than somebody's blog summary.

Use `https://choosealicense.com/appendix/` for the side-by-side comparison table.
**[VERIFY]** that appendix path.

**Time.** 15 minutes. **Level.** Extension for most, required reading for anyone
publishing a project.

---

## 6. The terms of service of the tool you use

**No URL given here, deliberately.** The document that matters is the one for the
model your lab actually runs, and it is the instructor who knows which that is.

**Why this is a resource and not a link.** Tuesday's lesson is that students should
read the governing document rather than trust a summary of it. Handing them a
summary would undercut the lesson. Find the terms for your tool, confirm it loads
through district filtering, and have students locate the ownership clause
themselves.

**If the local model has no terms** because it is open-weights software running on
your hardware, that is a genuinely interesting finding and worth saying out loud.
Then have students read the **model's license** instead, which does exist and does
impose conditions. The absence of a terms-of-service page is not the absence of
terms.

**Time.** 15 minutes. **Level.** Required Tuesday.

---

## 7. For the student who asks about `0.1 + 0.2`

**Python tutorial, Appendix: Floating Point Arithmetic** ·
`https://docs.python.org/3/tutorial/floatingpoint.html` · **Confident.**

**Why this one.** Somebody will find `0.30000000000000004` and want to know why.
This is the official explanation, it is written for people learning the language,
and it is honest that the behavior is normal rather than a defect.

**Warning.** It gets dense quickly. Tell the student to read the first section and
stop. The rest is genuinely beyond this course, and saying so is better than letting
them conclude they cannot understand it.

**Time.** 20 minutes for the first section. **Level.** Extension.

---

## On the "current article" slot

Not filled, for the same reason as Week 1: article URLs go stale and this file
cannot confirm what is live today.

If you want one for Tuesday, search for recent coverage of AI and copyright
litigation and pick something from the last few months yourself. **Read it before
assigning it**, and check whether it states outcomes as settled. An article that
overclaims is itself a Monday-lesson artifact, and using it that way is better than
using it as a source.

---

## Side quests

The syllabus names **SQ-02 The Regex Wrangler** as a Unit 1 deliverable. The Side
Quest Catalog was still not present in this repository when this file was written,
so no description is given. Add it once
`MCCTC_Side_Quest_Catalog_2026-2027.docx` is in `Courses/Misc/`.

---

## For the student who is behind

In this order, and no more than two.

1. Python Tutor with Wednesday's rebinding example, stepped one line at a time
2. Automate the Boring Stuff Chapter 1, the variables and type-conversion sections
3. Rewrite Lab U1-01 Part 1 from scratch without looking at their old file

The third one is the highest value and students resist it. A student who can rebuild
Wednesday's program from an empty file understands variables. One who can only edit
their existing file does not yet.
