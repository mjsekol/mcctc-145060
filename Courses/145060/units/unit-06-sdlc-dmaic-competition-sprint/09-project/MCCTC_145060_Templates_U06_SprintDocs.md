# Sprint Document Templates
## 145060 Programming · Unit 6 · The Competition Sprint

Copy each section into its own file in your repository's `docs/` folder, using the
file name in the heading. Replace every line in angle brackets. Delete the
instructions in italics once you have read them.

**Why templates at all.** A blank page makes a team argue about format instead of
content. These give you the shape so the thinking goes into what fills it. They are
a floor, not a ceiling. A section you need that is not here, add.

The finished sample sprint in `reference-implementation/docs/` shows every one of
these filled in for an invented stakeholder. Look at it when a section confuses you.
Do not copy its content. It solves a different problem.

For the decision log and the AI usage log, keep using the templates from Unit 0:
`unit-00-onboarding/09-project/MCCTC_145060_Template_AIUsageLog.md`.

---

## docs/charter.md

*Due Week 12, Monday, end of Build 2. Updated Tuesday after the interview.*

```markdown
# Project Charter · <team name>

## Stakeholder
<Who they are, in one line. Composite from the stakeholder bank, or the approved person.>

## Problem statement
<One sentence. Who has the problem, what hurts, and how often.
Not what you will build.>

## In scope
- <what this sprint will deliver>

## Out of scope
- <what this sprint will NOT deliver, stated plainly so nobody expects it>

## Roles and backups
| Role | Owner | Backup | Owner at BPA Regional on |
|---|---|---|---|
| Facilitator | <name> | <name> | <days, or "not competing"> |
| Stakeholder Liaison | <name> | <name> | |
| Test Lead | <name> | <name> | |
| Integration Lead | <name> | <name> | |

## Working agreement
- We meet for a stand-up at the start of Build 1 every day, spoken or written.
- We commit at the end of every block.
- We review code, never the coder.
- Our decision rule: <for example: fist to five, any 0 or 1 is heard first,
  10-minute timebox, then the Facilitator decides and logs the reason>
- When we disagree, we: <your steps, in order>
- When someone is absent, their backup: <what the backup does>
- If a member stops contributing, we: <what you do, and when you tell the instructor>

## Signatures
Every member types their name to agree: <names>
```

---

## docs/requirements.md

*Version 1 due Week 12, Tuesday. Signed by the stakeholder on Friday of Week 12.*

*Every requirement gets at least one acceptance criterion. A criterion is written so
that a person who has never met you could run it and agree whether it passed.*

```markdown
# Requirements · <team name>

## R1 · <short name>
<What the program must do, in the stakeholder's terms.>

- AC-1.1 Given <a situation>, when <an action>, then <an exact, checkable result>.
- AC-1.2 Given <...>, when <...>, then <...>.

## R2 · <short name>
...

## Processing requirements
<What happens to input nobody expected: blank values, wrong types, unknown labels,
a missing file. Each one gets a criterion.>

## Sign-off
Stakeholder reviewed these requirements and acceptance criteria on <date>.
Stakeholder signature: <typed name>
Changes after sign-off go through the question log and a change request.
```

---

## docs/question_log.md

*Started on Tuesday of Week 12. Used most in Week 13, when the stakeholder is not in
the room.*

```markdown
# Question Log · <team name>

| # | Date | Question | Asked by | Assumption we made meanwhile | Answer | Answered on |
|---|---|---|---|---|---|---|
| 1 | Dec 1 | <question> | <role> | <assumption> | <answer, or "open"> | <date> |
```

---

## docs/timeline.md

*Due Week 12, Wednesday, end of Build 2. Kept current by the Facilitator.*

```markdown
# Timeline · <team name>

## Constraints
| Constraint | Kind | Why it exists | What it rules out |
|---|---|---|---|
| Runs on a lab machine, standard library only | Technical | <why> | <what> |
| Acceptance demo Week 14 Fri | Time | <why> | <what> |
| Week 13 has no instruction and some members are at BPA | People | <why> | <what> |

## Baseline measurement (Measure)
<How does the stakeholder do this today, and how do you know it is a problem?
A number you counted from their sample data, not a guess.
Example shape: "In the sample log, 3 of 24 rows have a problem nobody would notice.">

## Milestones
| Day | Date | Milestone | Owner | Done when |
|---|---|---|---|---|
| 5 | Week 12 Fri | Requirements and acceptance tests signed | Stakeholder Liaison | Signature in requirements.md |
| ... | | | | |

## Capacity
Build blocks available from today through Day 14, minus known absences: <number>
Estimated work remaining: <number>
If work is bigger than capacity, what we cut first: <item>
```

---

## docs/test_plan.md

*Due Week 12, Thursday, end of Build 2.*

```markdown
# Test Plan · <team name>

Run all acceptance tests: `python test_<program>.py`

| Criterion | Check label in the test file | Kind | Boundary on both sides? |
|---|---|---|---|
| AC-1.1 | AC-1.1 <label> | normal case | n/a |
| AC-1.2 | AC-1.2 <label> | bad input refused | yes: <values> |

## Where expected values came from
<For each check: the stakeholder's example, or arithmetic you did by hand.
Never from running your own program.>

## Criteria with no check yet
<Should be empty by Friday. If not, say why.>
```

---

## docs/design.md

*Due Week 13, Tuesday, end of Build 1. Written in Week 13.*

```markdown
# Design Notes (Analyze) · <team name>

## Data files
<Each file's name, columns or keys, and one example row in the stakeholder's shape.>

## Functions
| Function | Takes | Returns | Raises or reports | Criteria it serves |
|---|---|---|---|---|
| read_<thing>(path) | a file path | (records, problems) | missing file | AC-1.1, AC-1.2 |

## Pseudocode for the hardest function
<Plain steps, before any Python.>

## Top three risks
1. <Risk>. If it happens: <plan>.
```

---

## docs/standups.md

*One entry per build day, starting Monday of Week 12. In Week 13 these are written,
because nobody is running them for you.*

```markdown
# Stand-up Log · <team name>

## Day <n> · <date> · present: <names> · absent: <names and why, e.g. BPA>
| Member | Did since last stand-up | Will do today | Blocked by |
|---|---|---|---|
| <name> | <specific> | <specific> | <nothing, or what> |

Sprint Board: remaining <n> blocks, capacity <n> blocks, <fits / at risk>
Decision made today, if any: <see decision log #>
```

---

## docs/sprint_review_1.md

*Due Week 13, Friday, end of Build 1. Written, because the stakeholder is not in
the room that day.*

```markdown
# Sprint 1 Review · <team name>

## What we planned to finish in Sprint 1
- <items from sprint planning>

## What is actually done
Paste the full output of `python test_<program>.py` here.

## Checks still failing, and why
| Check | Why it fails | Plan |
|---|---|---|

## Questions for the stakeholder when they are back
<Copy the open rows from the question log.>
```

---

## docs/review_1.md and docs/review_2.md

*The review your team **received**, pasted here by the reviewing team, plus your
response. Use the scoring form in
[`MCCTC_145060_PeerReview_ScoringForm.md`](MCCTC_145060_PeerReview_ScoringForm.md).*

```markdown
# Response to Review <1 or 2>

| Finding # | Accepted, rejected, or deferred | What we did, or why not | Commit |
|---|---|---|---|
```

---

## docs/change_impact.md

*Due Week 14, Wednesday, end of Build 1. The change request arrives that
morning.*

```markdown
# Change Impact Record · <team name>

## The baseline
Tag: v1.0 · Commit: <short hash> · All acceptance checks passing at the tag: <yes/no, count>

## The change request
<Paste it exactly as the stakeholder wrote it.>

## Impact analysis, before any code
| Affected | Function or file | Criteria and checks affected | Risk |
|---|---|---|---|
| Changes directly | | | |
| Uses something that changes | | | |
| Must NOT change | | | |

## Decision
<Accept, accept with a condition, or push back, and why. Record in decision log.>

## After the change
Branch: <name> · Reviewed in review_2.md · Merged: <yes/no> · Tag: v1.1
Checks before: <count passing> · Checks after: <count passing> · New checks added: <list>
```

---

## docs/control_plan.md

*Due Week 14, Friday.*

```markdown
# Control Plan · <team name>

## How the stakeholder runs it
<Exact steps, for someone who has never opened a terminal.>

## How they know it is still working
<Which command, and what output means healthy.>

## What will break it first
<The data change or situation most likely to cause a wrong answer, and how it shows up.>

## Accepted baseline
v1.1 at commit <hash>. Any change after this starts with a change impact record.
```

---

## docs/retrospective.md

*Week 14, Friday, Build 2. Fifteen minutes as a team, written down.*

*A retrospective is about the process, not the people. "A teammate was slow" is not a
retrospective finding. "We assigned the Test Lead two roles during BPA week and the
tests fell three days behind" is.*

```markdown
# Retrospective · <team name>

## What the data says
Planned checks passing by Day 10: <n> · Actual: <n>
Stand-up entries logged: <n> of <n> days
Change request impact: <n> functions, <n> checks

## Keep doing
- <specific practice, with evidence>

## Stop doing
- <specific practice, with evidence>

## Try next time
- <one concrete change, and how you would know it worked>

## The Week 13 question
What did your plan get right or wrong about losing a week, and what would you plan
differently for a team that loses its instructor mid-sprint?
```
