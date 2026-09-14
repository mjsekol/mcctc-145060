# Additional Resources · Week 13
## 145060 Programming · November 30 - December 4, 2026
### Topics: DMAIC outside and agile inside, requirements and acceptance criteria, constraints and timelines, acceptance tests

Every URL is marked Confident or [VERIFY]. Click every [VERIFY] link before assigning it.

**Confident** here means the page loaded and matched its description when this file was
written on September 14, 2026. Pages move. Check again the week you assign one.

**No new syntax this week.** Every resource below supports the four lecture notes in
`03-lecture-notes/`. None of them teaches a Python feature students have not already used.
If a resource drifts into `unittest`, classes, or a testing framework, tell students to stop
reading there. That is Unit 7 and later.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The Agile Manifesto and its twelve principles | Mon | On-level | 15 min |
| 2 | The history of the Agile Manifesto | Mon | Extension | 15 min |
| 3 | Agile Alliance glossary: Given When Then | Tue | On-level | 10 min |
| 4 | Martin Fowler, "Given When Then" | Tue | Extension | 10 min |
| 5 | Official docs: what `in` really compares | Wed | On-level | 10 min |
| 6 | Automate the Boring Stuff, Chapter 5, the Assertions section | Thu | On-level | 20 min |
| 7 | Python tutorial: Raising Exceptions | Thu | On-level | 10 min |
| 8 | Python Tutor with a boundary test file | Thu | Remediation | 15 min |
| 9 | Agile Alliance glossary: ATDD | Thu-Fri | Extension | 10 min |
| 10 | A short video on acceptance criteria | Tue | Remediation | under 20 min |
| 11 | SQ-24 Ship for a Real Stakeholder, as a preview | Fri | Extension | multi-week |

---

## 1. Primary reading, the source the argument started from

**Manifesto for Agile Software Development** · `https://agilemanifesto.org/` ·
**Confident.** The twelve principles are one click away at
`https://agilemanifesto.org/principles.html` · **Confident.**

**What it is.** The one-page statement that named "agile" in software, plus the
principles behind it. It is short enough to read twice.

**Why this one.** Monday's lesson asks you to make the strongest case for waterfall and
for agile. You cannot argue fairly with a position you only know from a summary. This is
the position in its own words.

**Assign a question, not the page.**

> Read the four value statements. Each one says "X over Y." Pick one pair. Write one
> sentence about a project where Y should win anyway, and why.

That question is Monday's exit ticket from the other direction. A student who can answer
it has understood that the manifesto ranks values and does not ban anything.

**Time.** 15 minutes. **Level.** On-level.

---

## 2. Where the manifesto came from

**History: The Agile Manifesto** · `https://agilemanifesto.org/history.html` ·
**Confident.**

**What it is.** An account of the 2001 meeting that produced the manifesto, written by one
of the people who signed it.

**Why this one.** It is an advocate's document, and that is the point. Read it as a
primary source written by someone with a side. Ask what the author thinks waterfall got
wrong, then ask what a project manager on a fixed-price contract would say back. The
lecture notes' "strongest case for waterfall" section gives you that answer.

**Time.** 15 minutes. **Level.** Extension, for the student who wants to argue Monday's
question with evidence.

---

## 3. The shape of an acceptance criterion

**Agile Alliance glossary, "Given When Then"** ·
`https://www.agilealliance.org/glossary/given-when-then/` · **Confident.**

**What it is.** A one-screen definition of the Given, When, Then template, with a short
example.

**Why this one.** Tuesday's criteria use this exact shape. The glossary says it more
briefly than the lecture notes, and it comes from an industry organization rather than from
your teacher. It also makes clear that the template is a habit, not a rule enforced by a
tool, which matches the notes.

**Assign a question, not the page.**

> Write the "13 through 19" ticket rule from Tuesday as two Given, When, Then criteria.
> One must name age 13 and one must name age 19.

**Time.** 10 minutes. **Level.** On-level.

---

## 4. A practitioner's short version

**Martin Fowler, "Given When Then"** · `https://martinfowler.com/bliki/GivenWhenThen.html` ·
**Confident.**

**What it is.** A short essay by a well-known software author, written for working
development teams. It dates from 2013, and the three-part shape it describes is the same one in this week's notes.

**Why this one.** This fills the "real industry work" slot. It shows that the template
you use on a food drive project is the same one professional teams use to agree on
behavior before code exists. It is short, and it treats the template as a way to structure
a conversation.

**Warning worth passing on.** It mentions tools and terms this course does not use. Read
for the three-part shape and skip the tool names.

**Time.** 10 minutes. **Level.** Extension.

---

## 5. Official documentation, why the timeline gained three days

**Common Sequence Operations** ·
`https://docs.python.org/3/library/stdtypes.html#common-sequence-operations` · **Confident.**

**Why this one.** Wednesday's deliberate error copied BPA dates as `"Mon Dec 07"`, and a
competitor gained three class days that do not exist. The table on this page states in one
line what `in` checks for a list. Once you read it, the bug stops being mysterious.

**Assign a question, not the page.**

> Find `x in s` in the table. What does it say an item must be for the answer to be
> `True`? Use that wording to explain why `"Mon Dec 07" in class_days` is `False`.

The answer is that an item must be **equal** to `x`. `"Mon Dec 07"` and `"Mon Dec 7"` are
different strings, so they are not equal, and no amount of looking alike changes that.

**Time.** 10 minutes. **Level.** On-level, and remediation for any team whose capacity
number looked too comfortable.

---

## 6. Why this unit uses `check` instead of `assert`

**Automate the Boring Stuff with Python, 3rd edition, Chapter 5, "Debugging," the section
on Assertions** · `https://automatetheboringstuff.com/3e/chapter5.html` · **Confident.**

**What it is.** A section on the `assert` statement as a sanity check inside a program.

**Why this one.** Students will find `assert` online and ask why the unit wrote its own
`check` helper. This section answers it if you read it with the right question. An
assertion stops the program at the first failure. A test file that stops at the first
failure hides every failure after it.

**Assign a question, not the page.**

> Your team's test file has 14 checks and 5 of them fail. If every check were an
> `assert`, how many failures would you see in one run? Why does that matter on demo day?

**Skip:** the Logging and debugger sections. Not this week.

**Time.** 20 minutes. **Level.** On-level.

---

## 7. Official documentation, how a refusal happens

**Python tutorial, Errors and Exceptions, "Raising Exceptions"** ·
`https://docs.python.org/3/tutorial/errors.html#raising-exceptions` · **Confident.**

**Why this one.** Thursday's `outcome()` helper turns a `ValueError` into the plain value
`"refused"` so a check can compare it. That only makes sense once you know what `raise`
does and what `try` and `except` catch. This is the official version, and it is short.

**Assign a question, not the page.**

> Read the Raising Exceptions section. Then look at `outcome()` in the acceptance tests
> lecture notes. If `split_bill` raised `TypeError` instead of `ValueError`, what would
> happen to the test file?

The answer is that the test file itself would crash, because `outcome()` only catches
`ValueError`. That is a real failure mode worth naming before a team hits it.

**Time.** 10 minutes. **Level.** On-level.

---

## 8. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Paste in Tuesday's boundary bug with four checks and step through it:

```python
results = []


def check(label, actual, expected):
    if actual == expected:
        results.append(True)
        print("PASS", label)
    else:
        results.append(False)
        print("FAIL", label, "expected", expected, "got", actual)


def ticket_price(age):
    if 13 < age < 19:
        return 6
    return 10


check("AC-2.1 age 13 pays teen price", ticket_price(13), 6)
check("AC-2.1 age 19 pays teen price", ticket_price(19), 6)
check("AC-2.2 age 12 pays adult price", ticket_price(12), 10)
check("AC-2.2 age 20 pays adult price", ticket_price(20), 10)
print(results.count(True), "passed,", results.count(False), "failed")
```

It prints two FAIL lines for 13 and 19, two PASS lines, and `2 passed, 2 failed`.

**Why this one.** Watching `13 < age < 19` evaluate to `False` with `age` equal to 13 does
more than any explanation. Then have the student fix the comparison, not the expected
values, and step through again.

**Time.** 15 minutes. **Level.** Remediation.

---

## 9. What goes wrong when teams write tests first

**Agile Alliance glossary, "Acceptance Test Driven Development (ATDD)"** ·
`https://www.agilealliance.org/glossary/atdd/` · **Confident.**

**What it is.** A glossary entry on writing acceptance tests together, before the code.

**Why this one.** It has a pitfalls section. One pitfall is teams letting a testing tool
take over a practice whose real purpose is a conversation about requirements. That is
Thursday's lesson and Friday's sign-off meeting, stated by practitioners. Assign it to the
student who thinks the test file is the goal instead of the agreement behind it.

**Time.** 10 minutes. **Level.** Extension.

---

## 10. On the video slot

**No specific video is named here, deliberately.** This file could not confirm the length
or current location of any single video on acceptance criteria.

**What to search for.** A short explainer on "Given When Then acceptance criteria" or
"acceptance criteria examples" from a named organization's official channel, such as an
industry association or a tool vendor's own learning channel. **[VERIFY]** before assigning.
Watch the whole thing first. Confirm it is under 20 minutes, it does not require an account,
and it loads through district filtering.

**Reject any video that** presents agile as the correct answer and waterfall as
outdated. Monday's lesson is that this is a real tradeoff, and a video that says otherwise
teaches the misconception.

**If you cannot find one you trust, do not assign a link.** Replay Tuesday's two
`teen_discount` readings on the projector for any student who missed it. That five-minute
argument about 13 and 19 is better than a video anyway, because the students had it.

**Level.** Remediation, for students who were absent Tuesday.

---

## 11. Side quest

**SQ-24 Ship for a Real Stakeholder**, as a preview only. Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. The catalog lists it as unlocking in
the 145010 capstone, or any time with instructor approval, and as a multi-week quest.

**Why it fits here.** This week you work with a stakeholder your teacher plays. SQ-24 is the
same process with a real person outside the class: a written scope agreement, at least two
meetings, a working thing, and a handoff document. A student who comes alive during
Tuesday's interview is the student to name it to.

**Do not start it this week.** The sprint needs every student through December 18. Mention
it, and let an interested student write a Problem Inventory entry for later.

**Week 14's side quest is SQ-12 Read the Source,** offered Friday, December 11. It unlocks any
time after Unit 4 in the catalog, so no early unlock is needed.

---

## For the student who is behind

1. Python Tutor with the ticket price checks, stepped one line at a time
2. The acceptance tests lecture notes, the `check` pattern and Worked example 2 only, typed and run
3. Rewrite one of your team's acceptance criteria so it names both sides of a boundary

Do not assign all eleven resources. A student who is behind and gets eleven links reads none of
them. Friday's sign-off is the deadline that matters, and the third item moves it forward.
