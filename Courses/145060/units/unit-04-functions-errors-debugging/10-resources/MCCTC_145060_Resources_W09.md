# Additional Resources · Week 9
## 145060 Programming · Week 9
### Topics: the troubleshooting method, try and except, narrow excepts, test cases

Links marked **Confident** or **[VERIFY]**. A site marked Confident with a section marked [VERIFY] means the site is certainly there and the exact chapter or
in-page address should be clicked before assigning.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Official tutorial: Errors and Exceptions | Tue-Wed | On-level | 25 min |
| 2 | Official docs: Built-in Exceptions | Tue-Wed | Extension | 10 min |
| 3 | Automate the Boring Stuff, the debugging chapter | Mon, Wed | On-level | 30 min |
| 4 | Think Python 3e, the debugging material | Mon | On-level | 20 min |
| 5 | Python Tutor, for try and except | Tue-Wed | Remediation | 15 min |
| 6 | Official docs: the assert statement | Thu | Extension | 5 min |
| 7 | A short video on exceptions | Tue | Remediation | under 20 min |
| 8 | A chapter on writing up what went wrong | Mon, Fri | Extension | 25 min |
| 9 | SQ-12 Read the Source | Fri | Extension | 1 block |

---

## 1. Errors and exceptions, from the source

**The Python Tutorial, Errors and Exceptions** · `https://docs.python.org/3/tutorial/errors.html` · **Confident.**

**What it is.** The official tutorial's section on syntax errors, exceptions, `try` and `except`, and raising exceptions.

**Why this one.** It is short, it is the authority, and its first `try` example is the same `int()` conversion students met on Tuesday.

**Assign a question, not the page.**

> Find the paragraph that explains what happens when an exception occurs inside a `try` block and does **not** match the `except` clause. Copy its key sentence, and connect it to
> Tuesday's `except TypeError` that did not catch `ValueError`.

**Watch for:** the handling section and the sections after it also use `else`, `finally`, classes, and exception groups. None are needed this week. Stop after the section on raising exceptions.

**Time.** 25 minutes. **Level.** On-level.

---

## 2. The list of exception names

**The Python Standard Library, Built-in Exceptions** · `https://docs.python.org/3/library/exceptions.html` · **Confident.**

**Why this one.** It answers the question "which name do I put after `except`?" for good. Find `ValueError`, `TypeError`, `FileNotFoundError`, `EOFError`, `KeyboardInterrupt`, and
`ZeroDivisionError`, and read one sentence on each.

**The detail that explains Wednesday.** The page shows the exception hierarchy. `KeyboardInterrupt` is **not** under `Exception`, which is exactly why `except Exception:` lets Ctrl+C through
and a bare `except:` does not. Have the extension student find that on the page and explain it to the class.

**Time.** 10 minutes. **Level.** Extension.

---

## 3. Debugging, in a free book

**Automate the Boring Stuff with Python** · `https://automatetheboringstuff.com/` · **Confident** for the site. **[VERIFY]** the chapter number and title for debugging in the current edition
before assigning. Earlier editions have a chapter titled "Debugging."

**What it is.** A free book for beginners that covers raising exceptions, reading tracebacks, and assertions as everyday tools.

**Why this one.** Its treatment of tracebacks and assertions matches Monday and Thursday closely, in plain language.

**Watch for:** the debugging chapter in earlier editions also covers `logging` and a debugger. Neither is needed this week. Assign the sections on exceptions, tracebacks, and assertions only.

**Time.** 30 minutes. **Level.** On-level.

---

## 4. Debugging, a second voice

**Think Python, 3rd edition** · `https://allendowney.github.io/ThinkPython/` · **Confident** for the book. **[VERIFY]** which chapter or section carries its debugging advice in the third edition.
The book is known for ending chapters with a short debugging section.

**Why this one.** Downey's debugging advice is hypothesis-driven, the same shape as the Six-Step Troubleshooting Method, written for students.

**Watch for:** examples that use lists or dictionaries. Skip them.

**Time.** 20 minutes. **Level.** On-level.

---

## 5. Python Tutor, for try and except

`https://pythontutor.com/` · **Confident.**

Paste in Tuesday's worked example 1 with a fixed value instead of `input`:

```python
text = "two"
try:
    tickets = int(text)
    print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
except ValueError:
    print(f"'{text}' is not a whole number, so nothing was ordered.")
print("Thanks for using the ticket kiosk.")
```

Step through it and watch execution jump from the `int` line straight to the `except` line, skipping the `print`. Then change `"two"` to `"3"` and step again. Verified to print
`'two' is not a whole number, so nothing was ordered.` and `Thanks for using the ticket kiosk.` when run.

**Time.** 15 minutes. **Level.** Remediation.

---

## 6. The assert statement

**The Python Language Reference, Simple statements** · `https://docs.python.org/3/reference/simple_stmts.html` · **Confident** for the page. **[VERIFY]** the in-page anchor for
"The assert statement."

**Why this one.** It is three paragraphs, and it states the one fact students need: `assert` raises `AssertionError` when its condition is false. It also says asserts can be switched off when Python
runs with optimization, which is a good reason the course's `check` helper does not rely on them. Mention that only if a student asks.

**Time.** 5 minutes. **Level.** Extension.

---

## 7. A short video

**[VERIFY]** before assigning. No video is named here, because none was confirmed live and under 20 minutes when this file was written. Python for Everybody's free lecture videos, reached from
`https://www.py4e.com/`, cover `try` and `except` early in the course. Watch it first, confirm the length, and check that its examples do not rely on lists.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 8. How working engineers document what went wrong

**Site Reliability Engineering, the chapter on postmortem culture** · `https://sre.google/sre-book/postmortem-culture/` · **[VERIFY]** that this address still resolves before assigning.

**What it is.** A chapter from a free online book about running large software systems, on writing up incidents after something breaks: what happened, the timeline, the cause, and what will stop it
happening again, written without blaming a person.

**Why this one.** It is the professional version of the troubleshooting log. A student who reads it will recognize reproduction, cause, fix, and prevention, and will see why the log keeps wrong
theories in it.

**How to use it.** For the extension student only, after v2 is submitted. Ask for three sentences: one thing their v2 log already does that the chapter recommends, one thing it does not, and one
sentence on why "without blame" matters on a team.

**Time.** 25 minutes. **Level.** Extension.

---

## 9. Side quest

**SQ-12 Read the Source** unlocks any time after Unit 4. Full description in `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.

**What it is.** Read a small open-source Python project and write a two-page report on how it is organized and one thing you would change.

**Why it fits here.** Students have split their own program into functions and read somebody else's code in Gate 2. Reading a real project's functions and error handling is the next step. The
catalog asks them to check its license, too.

**Also available:** **SQ-05 Bug Hunt**, for anyone who has not done it. Every one of its defects makes a good troubleshooting log entry.

**Time.** One block. **Level.** Extension.

---

## For the student who is behind

1. Monday: the troubleshooting notes, worked example 2 only, typed and run, including both theory tests
2. Tuesday: resource 5, Python Tutor, then the `read_whole_number` example from the notes
3. Wednesday: the narrow excepts notes, worked example 1 only, with and without the typo
4. Thursday: the test cases notes, worked example 2, run against both versions of the store

Do not assign all nine resources. Pick the one that matches the day the student missed.
