# Additional Resources · Week 12
## 145060 Programming · November 23-24, 2026
### Unit 5 review, the data pipeline finish, and the break

Two days, no new content. These resources support the quiz, the pipeline's last stages, and anyone
who wants to keep going over the break. Links marked **Confident** or **[VERIFY]**.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | This unit's lecture notes, self-check sections | Mon, before the quiz | Review | 20 min |
| 2 | Gate 1 Collections bank, Reps 12-20 | Mon | Review | 10 min each |
| 3 | Official docs: `os.makedirs` and `os.path.join` | Mon | On-level | 10 min |
| 4 | Official tutorial: Errors and Exceptions | Mon | Remediation | 15 min |
| 5 | Python Tutor, the mutable default argument | Tue | Remediation | 10 min |
| 6 | Data pipeline reference numbers, for self-checking | Mon-Tue | On-level | 5 min |
| 7 | SQ-13 The Scraper, continued | Break | Extension | 2 blocks |

---

## 1. The self-checks you already have

Every Unit 5 lecture note ends with three self-check questions and worked answers, in `03-lecture-notes/`.
**Before Monday's quiz, a student should be able to answer all 24 without reading the answers first.** The ones most
worth the time: Lists question 2, Dictionaries question 2, Tables question 1, Save and Load question 1, and CSV
question 1.

**Level.** Review.

---

## 2. Gate 1 reps

The later reps in the Collections bank are the best short review for the quiz: Rep 12 (JSON types), Rep 13 (except
order), Rep 16 (the Windows blank row), Rep 18 (the mutable default), and Rep 20 (choosing a structure). Your
instructor assigns them from the instructor copy.

---

## 3. Files and folders

`https://docs.python.org/3/library/os.html#os.makedirs` · **Confident.**
`https://docs.python.org/3/library/os.path.html#os.path.join` · **Confident.**

**Why these.** The pipeline creates an `output` folder and builds paths with `os.path.join`. **Assign a question:**
*What does `exist_ok` do in `os.makedirs`?* It is quiz item 9.

**Time.** 10 minutes. **Level.** On-level.

---

## 4. Errors and exceptions, for the except-order question

**The Python Tutorial, section 8, Errors and Exceptions** · `https://docs.python.org/3/tutorial/errors.html` ·
**Confident.**

**Assign a question:** *When a `try` has several `except` clauses, how many of them run?* That settles the except-order
misconception from Tuesday of Week 11.

**Time.** 15 minutes. **Level.** Remediation.

---

## 5. Seeing the mutable default

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Step through Gate 1 Rep 18. Python Tutor draws both calls pointing at the one list created with the `def`. It is the
fastest way to understand Tuesday's Gate 2 subtle defect after the reveal.

**Time.** 10 minutes. **Level.** Remediation.

---

## 6. Checking your pipeline against known numbers

For **Route A** students only. If your pipeline reads the Swap Shelf site and the provided sales log with rules like the
project's "about right" example, these are numbers you can compare with. **Your numbers can differ if your rules differ.
If they do, your README must explain which rule causes the difference.**

- Listings on the shelf: 28, across 3 pages
- Listings marked sold on the site: 11
- Sales log data rows: 16, including one blank row and one repeated header

The rest is your analysis to do, not a key to copy.

---

## 7. Over the break

**SQ-13 The Scraper**, `Courses/Misc/side-quests/SQ-13-The-Scraper/`. It runs entirely on your own computer, with no
network needed, so it works over the break. Remember to stop the site when you are done.

---

## For the student who is behind

Before Monday: the Save and Load notes, the CSV notes, and Reps 13 and 15. Nothing else.
