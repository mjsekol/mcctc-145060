# Additional Resources · Week 5
## 145060 Programming · October 5-8, 2026
### Topic: elif chains, logical operators, truth tables, and flattening nesting

Links marked **Confident** or **[VERIFY]**, same standard as every week. **Confident** here means the
URL returned a working page with the expected title when this file was built on September 14, 2026.
Links still move. Click each one once before assigning it.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff 3e, Chapter 2 | Mon-Tue | On-level | 40 min |
| 2 | Think Python 3e, Chapter 5 | Mon, Wed | On-level | 25 min |
| 3 | PY4E video: Conditional Execution, Parts 1 and 2 | Mon-Tue | Remediation | 25 min |
| 4 | Python Tutor | Mon, Thu | Remediation | 15 min |
| 5 | Official docs: `if` statements, and Boolean operations | Tue | On-level | 15 min |
| 6 | OWASP Input Validation Cheat Sheet, "Allowlist vs Denylist" | Thu | Extension | 15 min |
| 7 | Exercism Python track, conditionals and bools concepts | Any | Extension | 30 min |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, 3rd edition, Chapter 2: if-else and Flow Control** ·
`https://automatetheboringstuff.com/3e/chapter2.html` · **Confident.**

**Why this one.** It covers Boolean values, comparison operators, `and`, `or`, `not`, and `if`/`elif`/`else`
in one chapter, in the order this week teaches them, with small practical examples.

**What to skip.** The brief mention of `sys.exit()` near the end, which this course does not use.

**What to point out.** Near the end, the chapter describes a program where neither the `if` nor the `elif` matches, a
variable is never created, and Python raises a `NameError` later. That is the ticket lab's If it breaks item 3, written by
somebody else, which is a good sign to students that it is a real and common bug.

**Time.** 40 minutes for the whole chapter. Assign the Boolean and comparison sections Monday and the rest Tuesday.

---

## 2. Second reading, more precise

**Think Python, 3rd edition, Chapter 5: Conditionals and Recursion** ·
`https://allendowney.github.io/ThinkPython/chap05.html` · **Confident.**

**Why this one.** Downey is careful about the difference between a Boolean expression and a statement, and about
nested conditionals. His section on nested conditionals is a good second explanation for Thursday.

**What to skip.** Everything about recursion. That is Unit 3, and it will confuse a student reading this for Week 5.

**Level.** On-level. 25 minutes for the conditional sections only.

---

## 3. Free video, under 20 minutes each

**Python for Everybody, Conditional Execution, Part 1 (11:06) and Part 2 (13:52)**, by Chuck Severance ·
Part 1: `https://www.youtube.com/watch?v=DmzEdsqxTbU` · Part 2: `https://www.youtube.com/watch?v=OczkNrHPBps` ·
**Confident.** Both are linked from the PY4E lesson page `https://www.py4e.com/lessons/logic`, which is the better
link to hand students because it also carries the slides.

**Why this one.** A calm, unhurried walkthrough of `if`, `elif`, `else`, and indentation. Good for a student who missed
Monday and needs to hear it rather than read it.

**Honest note.** The video titles say "Chapter 3" because the PY4E book numbers chapters differently from this course.
The PY4E book's conditional chapter also covers `try` and `except`. **[VERIFY]** whether Part 2 of the video reaches that
material before assigning it. If it does, tell students that part is Unit 4 and they can stop there.

**Level.** Remediation. 25 minutes for both parts.

---

## 4. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Paste in Monday's wrong-order grade chain and step through it with a score of 95:

```python
score = 95
if score >= 60:
    letter = "D"
elif score >= 70:
    letter = "C"
elif score >= 80:
    letter = "B"
elif score >= 90:
    letter = "A"
else:
    letter = "F"
print(letter)
```

Watching the arrow jump from the first condition straight to `print` does more for "first True wins" than any
explanation. On Thursday, do the same with the robotics trip pyramid and count how many steps the arrow takes.

---

## 5. Official documentation

**The Python Tutorial, section 4.1, `if` Statements** ·
`https://docs.python.org/3/tutorial/controlflow.html#if-statements` · **Confident.**

**The Python Language Reference, Boolean operations** ·
`https://docs.python.org/3/reference/expressions.html#boolean-operations` · **Confident.**

**Assign a question, not the page.** The reference page is written for people who build Python itself.

> Find the paragraph about `x and y`. It says what Python returns and when it stops evaluating. In one sentence, explain
> how that paragraph proves Tuesday's pizza-split program cannot divide by zero.

The same page also explains why `day == "saturday" or "sunday"` hands back `"sunday"`, if a student wants the primary
source for Tuesday's bug.

**Level.** On-level for the tutorial, extension for the reference.

---

## 6. An industry connection

**OWASP Cheat Sheet Series, Input Validation Cheat Sheet** ·
`https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html` · **Confident.** Point students at the
section titled **Allowlist vs Denylist**.

**What it is.** OWASP is a nonprofit whose security guidance is widely used by working developers. This page is its practical
guide to checking input.

**Why this one, this week.** Thursday's Gate 2 security defect is exactly the mistake this section warns about: the consent check
refused one known bad answer and accepted everything else. A student who reads the section after Gate 2 will see that a Week 5
validation bug is a real professional category with a name.

**Warning worth passing on.** Most of the page is beyond this course, including regular expressions and server code. Read only the
allowlist section.

**Level.** Extension. 15 minutes.

---

## 7. More practice, for the student who wants reps

**Exercism, Python track** · `https://exercism.org/tracks/python` · **[VERIFY]** before assigning. The site refused the automated
check used to build this file, which usually means bot protection rather than a dead page. The concept pages for conditionals and
Booleans were at `https://exercism.org/tracks/python/concepts/conditionals` and
`https://exercism.org/tracks/python/concepts/bools` **[VERIFY]**.

**Honest note.** Exercism requires a free account. Do not require it. Offer it.

**Level.** Extension. 30 minutes.

---

## Side quest

**No quest in the catalog unlocks during Unit 2.** `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md` has SQ-04 in Week 4 and SQ-06
in Week 6, and nothing for selection and Boolean logic. That gap is recorded in the unit README.

**Use instead this week:** the EXTENDED option of Lab U2-01, which is a genuine untaught-concept challenge with a real trap in it.

---

## For the student who is behind

1. Python Tutor with the wrong-order grade chain, stepped one line at a time
2. The PY4E Conditional Execution Part 1 video
3. The Week 5 Monday notes, typing every example, then the three self-check questions without looking at the answers

Do not assign all seven resources. A student who is behind and gets seven links reads none of them.
