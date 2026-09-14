# Additional Resources · Week 4
## 145060 Programming · September 28 - October 2, 2026
### Topics: number bases, character encoding, reading files

Links marked **Confident** or **[VERIFY]**.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff, reading and writing files | Wed | On-level | 30 min |
| 2 | Python docs: Reading and Writing Files tutorial section | Wed | On-level | 15 min |
| 3 | Python docs: Unicode HOWTO | Tue | Extension | 25 min |
| 4 | Python docs: built-ins `bin`, `hex`, `int`, `ord`, `chr` | Mon-Tue | On-level | 10 min |
| 5 | Python Tutor | Wed | Remediation | 15 min |
| 6 | SQ-04 Number Bases by Hand | Fri | Extension | 1 block |

---

## 1. Reading files, primary reading

**Automate the Boring Stuff with Python, the chapter on reading and writing files** ·
`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the
third-edition chapter path.

**Why this one.** It covers `open`, `read`, `readline`, and closing in the order this week
teaches them, with file paths explained, which is exactly Wednesday's trap.

**Skip for now:** anything using `with`, `pathlib`, `os`, or `shelve`. Those come later.

## 2. The official tutorial section

`https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files` ·
**Confident.**

**Assign a question, not the page:** *what does `f.readline()` return when the end of the
file has been reached, and how is that different from a blank line?* That is Wednesday's
silent bug stated in the official words.

## 3. Unicode, for the student who wants the real explanation

`https://docs.python.org/3/howto/unicode.html` · **Confident.**

**Warning worth passing on:** dense. Read the first two sections, through the definition of
an encoding, and stop. Tuesday needs nothing past that.

## 4. The built-in functions this week uses

`https://docs.python.org/3/library/functions.html` · **Confident.**

**Assign:** find `int()` and read what it says about the `base` argument. Then answer: what
does `int("ff", 16)` give, and why?

## 5. Python Tutor

`https://pythontutor.com/` · **Confident.** Step through the Roster Reader lab's member 1
block and watch each slice take its piece.

## 6. Side quest

**SQ-04 Number Bases by Hand** pairs exactly with Monday. Write a converter between binary,
decimal, and hexadecimal without `bin()`, `hex()`, or `int(x, base)`. Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.

**Also this week:** Congressional App Challenge teams form Friday. The deadline is October
26. Point interested students at their Problem Inventories rather than at a list of app
ideas.

---

## For the student who is behind

1. Redo Monday's twelve conversions on paper, checking each with Python immediately
2. Python Tutor on the Roster Reader lab, member 1 only
3. Nothing else. Outcome 2.3 is small on the exam and mastery of place value is the whole of it.
