# Programming · 145060
## AI Automation & Software Development · Mahoning County Career & Technical Center

Student materials for **145060 Programming**, junior year, semester 1.
Instructor: Michael Sekol.

Everything here is written to you, the student. Read it, run it, break it.

---

## How this course runs

**118-minute block, Periods 1-3.** Every day looks like this:

| Minutes | What happens |
|---|---|
| 15 | Bell ringer and a Gate 1 rep |
| 15 | Instruction. One concept, live-coded, including a deliberate mistake |
| 35 | Build 1 |
| 5 | Reset |
| 40 | Build 2 |
| 8 | Commit and close |

**Friday introduces no new content.** Fridays are BPA preparation, credentials, side
quests, and catch-up.

## The three gates

All three run in every unit.

| Gate | AI use | What it is |
|---|---|---|
| **Gate 1, Closed** | None | Short timed reps in a plain editor. Trace, predict, fix. |
| **Gate 2, Adversarial** | AI is the opponent | You receive generated code and find what is wrong with it. Scored on caught against missed. |
| **Gate 3, Open** | Full tooling | Ambitious builds with everything available. Decision log required. |

## The rules that matter most

- **No work is graded that is not in a repository.** Every period ends with a commit.
- **Every project includes an AI usage log**: what you asked, what came back, what you
  changed, and why.
- **No personal information, real names, or school data enters any AI tool.**
- **The only way to fail outright is to submit work you cannot explain.**

## Where the AI comes from

Commercial AI developer APIs require users to be 18 or older. This course uses
**locally hosted models running on lab hardware**, which carry no such terms and send
no data outside the building.

Local models are slower and less capable than cloud models. For a text adventure that
generates room descriptions, that is a feature.

---

## What is in here

```
Courses/145060/units/
  unit-00-onboarding/
  unit-01-sequence-data-output/
    03-lecture-notes/   read these if you missed class, or before you build
    04-slides/          the decks from class, and their outlines
    05-labs/            the guided labs
    07-gate2-adversarial/  the code review exercises
    09-project/         project briefs
    10-resources/       readings, practice, documentation
```

Plus `Courses/Misc/` for the Side Quest Catalog, the Lab Acceptable Use and Safety
Agreement, and the SQ-05 Bug Hunt materials.

**Lecture notes are written so you can learn a concept from the file alone.** If you
were out, start there rather than asking someone what you missed.

## What is not in here, and why

Answer keys, quizzes, lesson plans, and the instructor's notes live in a separate
private repository. That is not secrecy for its own sake. A published answer key is
not recoverable, and the labs are worth more to you unspoiled.

---

## Getting set up

You need three things installed. Unit 0 walks through all of it.

- **Python 3.14**
- **VS Code**
- **Git**, and a GitHub account

Then run anything in here with:

```
python whatever_the_file_is.py
```

## The free books this course uses

All three are free to read online and all three are good.

- **Automate the Boring Stuff with Python** · automatetheboringstuff.com
- **Think Python** · allendowney.github.io/ThinkPython
- **Python for Everybody** · py4e.com

---

## A note on how these materials are built

This repository is generated from a private instructor repository by a script that
copies only student-facing files and refuses to run if an answer key reaches the
output. If you find something in here that looks like it was not meant for you, tell
Mr. Sekol. That is a bug, and reporting it is the same skill Gate 2 grades.

Every program in these materials was executed before it was published. If something
does not run, that is worth reporting too.
