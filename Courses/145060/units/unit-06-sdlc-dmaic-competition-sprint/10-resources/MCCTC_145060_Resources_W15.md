# Additional Resources · Week 15
## 145060 Programming · December 14-18, 2026
### Topics: code review and static analysis, team roles and conflict, baselines and change impact, the fair workplace

Every URL is marked Confident or [VERIFY]. Click every [VERIFY] link before assigning it.

**Confident** here means the page loaded and matched its description when this file was
written on September 14, 2026. Pages move. Check again the week you assign one.

**Wednesday is an introduction only.** Baselines, tags, and branches (5.7) are taught fully in
Unit 8. The Git resources below are for the one baseline and one change branch you make this
week. Skip anything about rebasing or merge conflicts.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Google Engineering Practices: what to look for in a code review | Mon | On-level | 20 min |
| 2 | Official docs: `py_compile` | Mon | On-level | 10 min |
| 3 | Terminal practice: `python -m ast` | Mon | On-level | 15 min |
| 4 | Official docs: `ast` | Mon | Extension | 15 min |
| 5 | Agile Alliance glossary: Heartbeat Retrospective | Tue, Fri | On-level | 10 min |
| 6 | Pro Git: Tagging, and Basic Branching and Merging | Wed | On-level | 25 min |
| 7 | Official docs: `hashlib` | Wed | Extension | 10 min |
| 8 | git-scm.com videos | Wed | Remediation | under 10 min each |
| 9 | Official government sources on labor law | Thu | On-level | 20 min |
| 10 | Official docs: `str.isascii` | Thu | On-level | 5 min |
| 11 | SQ-12 Read the Source | Fri or break | Extension | 1 block |

---

## 1. Primary reading, how a professional team reviews code

**Google Engineering Practices, "What to look for in a code review"** ·
`https://google.github.io/eng-practices/review/reviewer/looking-for.html` · **Confident.**
The introduction to the whole guide is at `https://google.github.io/eng-practices/review/` ·
**Confident.**

**What it is.** A public guide written for code reviewers at a large software company. The
page is organized into short sections such as Design, Functionality, Tests, Naming, and Good
Things.

**Why this one.** This fills the "real industry work" slot. It shows that the review you run
Monday is a normal professional practice, not a school exercise. It also names things a
reviewer should look for that no static tool can find, which is Monday's lesson.

**Assign a question, not the page.**

> Read the Tests section. What does it say a reviewer should check about the tests
> themselves? Connect your answer to the test in Gate 2 W13 that agreed with the bug.

**Warning worth passing on.** It uses terms from that company's own tools, such as "CL." Read
past them. A CL is the change being reviewed.

**Time.** 20 minutes. **Level.** On-level.

---

## 2. Official documentation, what a passing compile check promises

**`py_compile`** · `https://docs.python.org/3/library/py_compile.html` · **Confident.**

**Why this one.** Monday's `greet.py` passes `python -m py_compile` and still crashes when
it is called with an afternoon hour. This page is short, and its Command-Line Interface section says
exactly what the exit status means.

**Assign a question, not the page.**

> Read the Command-Line Interface section. What does a nonzero exit status mean? Now write
> one sentence on what an exit status of 0 does **not** promise about `greet.py`.

It promises only that Python could read the file. It says nothing about whether every name
exists or the logic is right.

**Time.** 10 minutes. **Level.** On-level.

---

## 3. Practice, see the tree a checker searches

**No link. Run this in your own terminal.** The `ast` module has a command-line mode that
prints the tree for any file. It is documented in the Command-Line Usage section of the page
in item 4.

Save this as `greet_small.py`:

```python
def greet(hour):
    return "Good " + tiem_of_day
```

Run both commands:

```
python -m py_compile greet_small.py
python -m ast greet_small.py
```

The first prints nothing, because the file compiles. The second prints the whole program as
nested pieces. Find the line that contains `Name(id='tiem_of_day'`. The layout can differ a
little between Python versions.

**Why this one.** Monday's `tiny_checker.py` walks a tree you cannot see. Seeing it once makes
`ast.walk` and `isinstance(node, ast.ExceptHandler)` stop feeling like magic. It also shows
that the misspelled name is right there in the tree, and a checker could flag it if someone
wrote that check.

**Time.** 15 minutes. **Level.** On-level.

**Optional, not required and not installed on the lab machines.** Professional teams use
installable linters such as `pylint`, `flake8`, and `ruff`. They work on the same idea at a
much larger scale. You do not need them for this unit.

---

## 4. Official documentation, the `ast` module

**`ast`** · `https://docs.python.org/3/library/ast.html` · **Confident.**

**Warning worth passing on.** Most of this page is a long list of node types, and it reads like
a specification because it is one. Go to the section on `ast` helpers and read only `ast.parse`
and `ast.walk`.

**Assign a question, not the page.**

> Read the entry for `ast.walk`. Does it promise to visit nodes in line order? If your
> checker printed findings straight from `ast.walk`, what would you have to do before
> showing them to a reviewer?

It visits nodes in no specified order. Sort findings by line number before printing them.

**Time.** 15 minutes. **Level.** Extension.

---

## 5. Retrospectives, and how they go wrong

**Agile Alliance glossary, "Heartbeat Retrospective"** ·
`https://www.agilealliance.org/glossary/heartbeat-retrospective/` · **Confident.**

**What it is.** A glossary entry on the recurring end-of-sprint retrospective, with a section
on common pitfalls.

**Why this one.** Friday's retrospective is a ceremony, not a lesson, so this is the only
reading for it. The pitfalls section describes a retrospective turning into an argument or a
complaint session. That is Tuesday's lesson from the other side: keep the conflict about the
task and the process, and resolve it.

**Assign a question, not the page.**

> Read the Common Pitfalls section. Pick the pitfall your team is most likely to fall into
> on Friday. Write one rule for your retrospective that prevents it.

**On positions, interests, and consensus: no link, deliberately.** Tuesday's lecture notes and
your team's working agreement are the resources. A general article on negotiation would be
less useful than your own decision rule, which you wrote before any disagreement.

**Time.** 10 minutes. **Level.** On-level.

---

## 6. Pro Git, tags and branches

**Pro Git, 2.6 "Git Basics - Tagging"** ·
`https://git-scm.com/book/en/v2/Git-Basics-Tagging` · **Confident.**

**Pro Git, 3.2 "Git Branching - Basic Branching and Merging"** ·
`https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging` · **Confident.**

**What it is.** The free Git book hosted on the official Git site. These two sections cover creating an annotated
tag, sharing it, and creating and merging a branch.

**Why this one.** Wednesday's most expensive mistake is a tag that exists only on one laptop.
The Tagging section has its own part on sharing tags, and it says this in the book's own
words.

**Assign a question, not the page.**

> In the Tagging section, find Sharing Tags. Does a normal `git push` send your tags? What
> command sends one tag named `v1.0`?

No. `git push origin v1.0` sends that one tag. Pushing `main` alone leaves the baseline on
your laptop.

**Warning worth passing on.** The branching section creates branches with
`git checkout -b`. The lecture notes use `git switch -c`. Both create a branch and move you
onto it. Use the lecture notes' version in class. **Skip** "Basic Merge Conflicts." If Git
reports a conflict, stop and get your teacher. Conflicts are taught in 145065.

**Time.** 25 minutes. **Level.** On-level.

---

## 7. Official documentation, what a fingerprint is

**`hashlib`** · `https://docs.python.org/3/library/hashlib.html` · **Confident.**

**Why this one.** `baseline.py` records a SHA-256 fingerprint of every file. The deliberate
error fingerprinted the file's name instead of its contents, so a real edit went unnoticed.
This page explains what `hexdigest()` returns.

**Assign a question, not the page.**

> Find `hexdigest()` in the Hash Objects section. What kind of value does it return? Then
> explain in one sentence why hashing `path.encode("utf-8")` cannot detect an edit to the file.

The name of a file does not change when you edit it, so its fingerprint does not change either.

**Skip:** everything from key derivation onward. Not this course.

**Time.** 10 minutes. **Level.** Extension.

---

## 8. Video

**Git's official videos page** · `https://git-scm.com/videos` · **Confident.**

**What it is.** A short set of introductory videos on the official Git site. When checked,
each listed video ran under ten minutes. "What is Version Control?" is the one to start with.

**Why this one.** A student who is still unsure what a commit is will not understand a tag. This
is the fastest honest route back to the idea that a tag is a permanent name on one commit.

**Time.** Under 10 minutes. **Level.** Remediation.

---

## 9. Official government sources on labor law

**Read this first. Your teacher is not a lawyer, and these links are not legal advice.** They
point to the agencies that govern each topic, so you know where to look when a real situation
affects you. This file deliberately gives no wage amounts, hour limits, age cutoffs, or
employer size thresholds. Those numbers change and some differ between federal and Ohio law.

**Every link below is marked [VERIFY], even ones that loaded when this file was written.**
Government sites reorganize often. Click each one before you assign it.

**Federal wage, hour, and youth employment rules: U.S. Department of Labor, Wage and Hour Division.**

- YouthRules, the division's information for young workers, parents, educators, and employers ·
  `https://www.dol.gov/agencies/whd/youthrules` · **[VERIFY].** Loaded September 14, 2026.
- Child labor information from the same division ·
  `https://www.dol.gov/agencies/whd/child-labor` · **[VERIFY].** Loaded September 14, 2026.

**Instructor note.** An earlier draft of the lecture notes pointed at a Department of Labor
youth-employment address that returned a not-found error on September 14, 2026. The lecture notes now
use the YouthRules address above.

**Ohio minor labor and minimum wage rules: Ohio Bureau of Wage and Hour Administration.**
Find it from the State of Ohio's official site, `https://ohio.gov` · **[VERIFY].** The site returned
an error to an automated check when this file was written. Confirm you land on a `.gov` page.

**Discrimination, harassment, and the ADA in employment: U.S. Equal Employment Opportunity Commission.**

- Home · `https://www.eeoc.gov/` · **[VERIFY].** Loaded September 14, 2026.
- Youth@Work, the commission's site for young workers · `https://www.eeoc.gov/youth` ·
  **[VERIFY].** Loaded September 14, 2026.
- Harassment · `https://www.eeoc.gov/harassment` · **[VERIFY].** Loaded September 14, 2026.
- Disability-related resources · `https://www.eeoc.gov/eeoc-disability-related-resources` ·
  **[VERIFY].** Loaded September 14, 2026.

**Why these.** Thursday's lesson ends with the same move as Unit 0: when you need the rule, go to
the source that governs it. A blog summary of labor law can be out of date the day a rule changes.
These pages are the rule makers and enforcers.

**Assign a navigation task, not a number.**

> Open YouthRules. Find where a young worker would go to ask a question or file a complaint.
> Then open Youth@Work and find the list of laws the EEOC enforces. Write down which agency you
> would contact about each line of the composite café posting in the lecture notes.

**Do not ask students to copy any figure from these pages.** If a student asks a personal legal
question, answer the way the lesson plan says: "I am not a lawyer. Here is who governs that. Let us
find the page."

**On the video slot for Thursday.** Youth@Work lists a section of videos, fact sheets, and
classroom materials. **[VERIFY]** that section, and the length of any video, before showing one.

**Time.** 20 minutes. **Level.** On-level.

---

## 10. Official documentation, why the filter removed José and Zoë

**`str.isascii`** · `https://docs.python.org/3/library/stdtypes.html#str.isascii` ·
**Confident.**

**Why this one.** Thursday's AI-suggested cleanup step removed real names and called them
corrupted. The official definition is two sentences long, and it makes the bias in that rule
visible in plain words.

**Assign a question, not the page.**

> Read the definition. Which characters count as ASCII? Would the filter keep a completely blank
> name? What does that tell you about what the rule was really checking?

It returns `True` for an empty string, so a blank name passes and `José` does not. The rule
checked which alphabet a name uses, not whether the record was damaged.

**Time.** 5 minutes. **Level.** On-level.

---

## 11. Side quest

**SQ-12 Read the Source.** Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. It unlocks any time after Unit 4, takes one
block, and lists 5.6.13 among its competencies.

**Why it fits here.** Monday you review a classmate's code with a protocol. SQ-12 is a walkthrough
with nobody to explain the code to you: a small open-source Python project, a written report on how
it is organized, one thing the author did that you would not have thought of, one thing you would change, and what its license
would require of you. It is a good winter break quest for a student who liked Monday.

**A preview, not an assignment.** **SQ-19 The Bias Audit** is a 145130 quest for next year. It asks
for a repeatable test of bias in a locally hosted model's output. Mention it to the student who is
still thinking about Thursday's filter. Do not assign it now.

---

## For the student who is behind

1. Item 3: run `python -m py_compile` and `python -m ast` on `greet_small.py`, and find the misspelled name
2. Item 6: the Sharing Tags part of Pro Git only, then confirm your team's `v1.0` tag is on GitHub
3. The lecture notes for whichever day you missed, with a terminal open, typing every example

Do not assign all eleven resources. Friday is the last day anything in this unit can be finished,
and item 2 on this list protects the one thing your team cannot rebuild over break.
