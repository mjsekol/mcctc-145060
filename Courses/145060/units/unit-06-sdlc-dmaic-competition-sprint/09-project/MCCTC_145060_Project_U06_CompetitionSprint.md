# Project: The Competition Sprint
## 145060 Programming · Unit 6 · Weeks 12-14

**Mode:** team of 3 or 4, assigned by your instructor. **Gate:** 3, full tooling,
decision log required. **Duration:** fifteen class days, one of which is a week
with no instruction at all. **Acceptance demo:** Week 14, Friday.

**Competencies:** 5.6.1 (requirements specification), 5.6.2 (constraints and
processing requirements), 5.6.3 (timelines), 5.6.9 (design review by peer
walkthrough), 5.6.10 (present the design to stakeholders), 5.6.11 (develop the
application), 5.6.12 (agile and waterfall), 5.6.13 (code reviews), 5.6.14
(testing), 1.2.3, 1.2.4, 1.2.7, 1.2.10 (communication, conflict, consensus,
leadership), 1.8.2 (organize resources). Configuration management (5.7) is
introduced here and assessed in Unit 8.

---

## Why this project is different

Every project so far had one author. You. This one has a team, a stakeholder who
is not you, and a calendar that fights back.

Week 13 is BPA Regional week. Some of your teammates will be competing.
Your instructor will be supervising competitors and will not be teaching. **You
will lose a week of help in the middle of your sprint, and you know it now.** That
is the realistic part. Real teams lose people to other deadlines, sick days, and
other projects. The teams that finish are the ones that planned for it on day one.

There is no new syntax in this unit. Everything you need to write the program you
already have: functions, `try` and `except`, lists, dictionaries, sets, CSV, JSON,
and files. What is new is everything around the code.

---

## The brief

Your team is assigned one stakeholder from the bank below. Read your stakeholder's
words as though they said them to you, because on Tuesday of Week 12, they will.
Your instructor plays the stakeholder in a four-minute interview.

**Every stakeholder below is a composite.** They are invented from the kinds of
requests school programs and clubs really make. None of them is a real person.

Notice what each one does not say. None of them tells you what to build, what the
input file looks like, or what counts as done. **Finding that out is the first week
of the project.** A team that starts typing code on Monday is building an answer to
a question nobody has asked yet.

### S1 · The culinary lab instructor

> Every Friday I order ingredients for next week's recipes, and every Monday we are
> either out of butter or drowning in it. I scale recipes on paper for however many
> students are in each lab, add it all up, and then order. Something in that chain is
> wrong and I cannot find it. I would like to stop thinking about butter.

### S2 · The robotics team mentor

> We have six build benches and a shared parts cabinet. Things get checked out and
> never come back. The night before a competition we discover the good drill kit is
> missing and nobody knows which bench had it last. I do not want to police people. I
> want to know what is missing before we pack the van.

### S3 · The greenhouse advisor

> The greenhouse has forty trays and a watering log on a clipboard. During the week
> it mostly works. Over long weekends and breaks, plants die, and a long break is
> coming. I need to know which trays are going to be in trouble and who is covering
> which days, before we leave.

### S4 · The automotive program lab manager

> We track about two hundred pieces of equipment. Lifts get inspected, torque wrenches
> get calibrated, and everything has a due date in a spreadsheet nobody reads until an
> inspector asks. I do not need more data. I need the few things that matter this week
> to stop hiding among the ones that do not.

### S5 · The theater club director

> Every rehearsal we lose twenty minutes looking for props. Each scene needs certain
> props, some props are in more than one scene, and some of them live in a different
> room. I want to walk into rehearsal knowing what should be on the table for the
> scenes we are running today.

### S6 · The BPA chapter advisor

> Our competitors practice all year. When results come back, it turns out half the
> chapter practiced the same three topics and nobody touched the rest. I do not want to
> track anybody's scores. I want to see which topics the chapter as a whole is
> ignoring, while there is still time to fix it.

### Instead of the bank

A team may pitch a problem from a member's **Problem Inventory** from Week 1 instead,
if the person with the problem can be interviewed in the building during class on
Tuesday of Week 12, and your instructor approves it by the end of Build 1 that day. The
stakeholder cannot be a member of your team. The rule exists because a team that
interviews itself learns nothing about requirements.

---

## Team roles

Every member writes code. Every member also owns one role. The role is the thing
you are accountable for when the team is asked "whose job was that."

| Role | You own | Evidence you did it |
|---|---|---|
| **Facilitator** | The timeline, the stand-ups, and calling decisions under the working agreement | Stand-up log, timeline kept current, decision log entries |
| **Stakeholder Liaison** | Requirements, acceptance criteria, the question log, stakeholder sign-off | Requirements doc, question log, signed Define/Measure gate |
| **Test Lead** | The acceptance test file and the test plan | Test file, test plan mapping every criterion to a check |
| **Integration Lead** | The repository: `main` stays runnable, the baseline tag, the change log | Commit history, tag `v1.0`, change impact record |

**Team of three:** the Facilitator also serves as Integration Lead.

### Backups, and why they are required

Every role has a named backup, written in the charter on Monday. **If a role owner is
at BPA Regional, the backup does that job that day.** A team whose Test Lead is
competing on Tuesday and whose tests therefore do not move on Tuesday has a planning
failure, not an attendance problem.

**Rule for team assignment.** Your instructor builds teams so that every team has at
least two members who are not competing at Regional. If that is impossible with this
year's roster, the instructor tells you on Monday and the team plans around it.

---

## Technical requirements

1. **It runs with `python yourprogram.py`** on a lab machine with Python 3.14 and
   nothing else installed. Standard library only.
2. **It reads at least one data file** in CSV or JSON. The stakeholder's data shape,
   not one you invented.
3. **It refuses bad input out loud.** Every bad row or bad value is reported with
   where it is and why. Nothing is silently dropped and nothing is silently counted.
4. **It is built from functions**, each with a docstring, and each small enough to
   test on its own.
5. **It has an acceptance test file**, `test_yourprogram.py`, that runs with
   `python test_yourprogram.py`, uses the `check(label, actual, expected)` pattern
   from Thursday's lesson, names the acceptance criterion in every label, and prints
   a pass and fail count.
6. **Every acceptance criterion the stakeholder signed has at least one check.**
   Boundaries get a check on both sides.
7. **No personal information** in any file, fixture, or test. Invented names only, and
   most stakeholders here do not need names at all.

## Process requirements

These are graded under Process and Documentation. Templates for each are in
[`MCCTC_145060_Templates_U06_SprintDocs.md`](MCCTC_145060_Templates_U06_SprintDocs.md).

- Project charter with roles, backups, and the working agreement
- Requirements with acceptance criteria, signed by the stakeholder
- Constraints and a timeline on real class days
- Test plan
- Design notes from Analyze
- Stand-up log, one entry per team per build day
- Two peer code reviews received, and two written by each member
- Change impact record for the change request
- Retrospective and control plan
- Decision log and AI usage log, same as every Gate 3 project

### Required repository structure

```
team-name-sprint/
  README.md                 what it is, how to run it, a real run, known limitations
  yourprogram.py
  test_yourprogram.py
  data/                     sample data in the stakeholder's shape, invented values
  docs/
    charter.md
    requirements.md
    timeline.md
    test_plan.md
    design.md
    standups.md
    question_log.md
    sprint_review_1.md      written Friday Dec 11, when the stakeholder is away
    review_1.md             the review your code received, with your response
    review_2.md
    reviews_given.md        the two reviews your team wrote for other teams
    change_impact.md
    retrospective.md
    control_plan.md
    decision_log.md
    ai_usage_log.md
```

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Install a package | The stakeholder's machine is a lab machine. A tool that needs an install is a tool nobody runs after you leave. |
| Use classes | They are Unit 7. Writing code you cannot explain fails the course standard, and that applies to every member, not whoever wrote it. |
| Use a commercial AI API | Commercial developer APIs require users to be 18 or older. Local models only, logged in the AI usage log. |
| Put any real person's information in the repository | The repository is public. Invented data only, every time. |
| Change requirements without the stakeholder | A requirement you changed quietly is a requirement you will fail at the demo. Changes go in the question log and get an answer. |
| Merge the change request straight into `main` | The Wednesday of Week 14 lesson is about protecting an accepted baseline. The change goes on a branch and gets reviewed first. |

---

## DMAIC phases and deliverables

DMAIC is the frame for the whole sprint. The agile ceremonies (planning, stand-ups,
review, retrospective) run **inside Improve**, which is where the uncertainty is.

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 12 Mon, end of Build 2 | Charter draft: problem statement, stakeholder, scope in and out, roles and backups, working agreement |
| **Define** | Week 12 Tue, end of Build 2 | Requirements v1 with acceptance criteria, question log started |
| **Measure** | Week 12 Wed, end of Build 2 | Baseline measurement of how the stakeholder does it today, constraints list, timeline on class days |
| **Measure** | Week 12 Thu, end of Build 2 | Acceptance test file with every check written and failing, test plan |
| **Gate** | Week 12 Fri, end of Build 2 | Stakeholder signs requirements and acceptance tests. Week 13 plan written. |
| **Analyze** | Week 13 Tue, end of Build 1 | Design notes: every function with its docstring and inputs and outputs, data file shapes, top three risks |
| **Improve** | Week 13 Fri, end of Build 1 | Sprint 1 increment: a runnable program and a written sprint review listing which checks pass |
| **Improve** | Week 14 Mon, end of Build 2 | Peer code review 1 received and written |
| **Improve** | Week 14 Tue, end of Build 2 | Review findings triaged by consensus and fixed. Every acceptance check passes. |
| **Control** | Week 14 Wed, end of Build 1 | Tag `v1.0` on `main`. Change impact record for the change request. |
| **Control** | Week 14 Thu, end of Build 1 | Peer code review 2 on the change branch, merged, tagged `v1.1` |
| **Control** | Week 14 Fri, end of block | Acceptance demo, control plan, retrospective |

**Measure is the phase teams skip and it is the one that decides the demo.** On
Friday of Week 14 the stakeholder does not ask whether you worked hard. They run the
acceptance tests they signed on Friday of Week 12. A team with vague criteria cannot pass
a test that was never defined.

---

## Milestone schedule, on real class days

| Day | Date | Build 1 | Build 2 |
|---|---|---|---|
| 1 | Week 12 Mon | Team formed, roles and backups, working agreement | Define: charter draft |
| 2 | Week 12 Tue | Interview questions prepared, practice transcript | Four-minute stakeholder interview, requirements v1 |
| 3 | Week 12 Wed | Constraints and baseline measurement | Timeline on class days, including Week 13 |
| 4 | Week 12 Thu | Lab U06-01, tests for code you did not write | Your own acceptance tests, all failing, and the test plan |
| 5 | Week 12 Fri | Gate 2 W12 | Stakeholder sign-off. Week 13 plan. |
| 6 | Week 13 Mon | **BPA.** Lab U06-02 Sprint Board, Part 1 | Analyze: design notes |
| 7 | Week 13 Tue | **BPA.** Lab U06-02, Part 2, and design notes due | Sprint 1 planning, then build |
| 8 | Week 13 Wed | **BPA.** Build | Build |
| 9 | Week 13 Thu | Gate 2 W13, independent | Build |
| 10 | Week 13 Fri | **BPA presentations.** Written sprint review | Catch-up and Gate 1 reps |
| 11 | Week 14 Mon | Lab U06-03 Structured Peer Review | Peer code review 1 |
| 12 | Week 14 Tue | Gate 2 W14 | Triage findings by consensus, fix, all checks pass |
| 13 | Week 14 Wed | Tag `v1.0`, change request arrives, impact record | Build the change on a branch |
| 14 | Week 14 Thu | Peer code review 2, merge, tag `v1.1` | Problem Drop #3, individual |
| 15 | Week 14 Fri | Acceptance demos | Unit quiz, then retrospective |

**Week 13 is written out day by day** in
[`MCCTC_145060_Guide_W13_SelfDirectedSprint.md`](MCCTC_145060_Guide_W13_SelfDirectedSprint.md).
Read it on Friday of Week 12, before you leave. Nobody will be available to explain
it on Monday.

---

## Peer code reviews

The syllabus requires two, and they are real reviews, not a formality.

- **Review 1, Week 14, Monday.** Your team reviews another team's Sprint 1 code.
  Another team reviews yours.
- **Review 2, Week 14, Thursday.** Your team reviews another team's change branch
  before it is merged into their baseline.

Both follow [`MCCTC_145060_PeerReview_Protocol.md`](MCCTC_145060_PeerReview_Protocol.md)
and are scored on [`MCCTC_145060_PeerReview_ScoringForm.md`](MCCTC_145060_PeerReview_ScoringForm.md),
using the five-dimension rubric: Correctness, Security, Readability, Performance, and
Requirements Fit, 20 points each.

**You review the code, never the coder.** A finding names a line, a consequence, and a
fix. "This is messy" is not a finding.

---

## Three worked scope examples

These exist so your team can calibrate. **Do not build any of these three.** The
middle one is the reference implementation and it is occupied.

### Too small

> A program that prints the greenhouse watering schedule, with the schedule typed into
> the code.

No data file, nothing to validate, nothing a test could fail, and the stakeholder
cannot change the schedule without editing Python. It meets almost none of the
technical requirements, and it does not touch the stakeholder's real problem, which is
coverage over breaks.

### About right

> **Food Drive Tracker** for a service club advisor. Reads a donation log CSV and a
> goals JSON file. Reports progress toward the total goal, ranks food categories by
> how far each is from its goal so the club knows what to ask for next, ranks the
> collection bins, and writes a one-sentence morning announcement. Every bad row is
> reported with its line number. Twenty acceptance checks, all passing. About 250
> lines including docstrings.

It reads real-shaped data, refuses bad input out loud, answers the stakeholder's
actual question ("what do we ask for next," not "how many cans"), and its whole
behavior fits in three sentences. The full sample sprint, documents and all, is in
`reference-implementation/` and your instructor will show parts of it.

### Too big

> A web dashboard for every club in the building, with logins, a database, text
> message alerts, and charts.

Web servers and databases are later units and later courses. Logins mean personal
data. Text alerts need an outside service. Each of those is a good idea and none of
them fits fifteen days with a week missing. A team that scopes this ships nothing on
Friday of Week 14.

**The calibration question:** can your team describe the program's entire behavior in
three sentences, and does each sentence map to at least one acceptance criterion? If
not, cut until it does.

---

## The acceptance demo

Week 14, Friday. Five minutes per team, with the stakeholder in the room.

1. **The problem, in the stakeholder's words.** Quote the charter. (30 seconds)
2. **Run the acceptance tests live.** The whole file, in the terminal, with the pass
   count visible. (60 seconds)
3. **Run the program on the stakeholder's sample data.** Point at the output that
   answers their real question. (60 seconds)
4. **One decision and why.** Something you cut, something you changed after review,
   or how you handled the change request. (60 seconds)
5. **One known limitation.** Something it does not handle, and what happens if
   somebody tries. (30 seconds)
6. **Stakeholder questions, answered by any member.** Your instructor chooses who
   answers. (60 seconds)

**Item 6 is where "work you cannot explain" shows up.** Every member must be able to
explain any function in the program, not only the ones they wrote.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Runs clean on the stakeholder's sample data. Every signed acceptance check passes. Bad input refused out loud. |
| **Code Quality** | 20 | Functions with docstrings, readable names, no swallowed errors, findings from both peer reviews addressed or answered in writing. |
| **Documentation** | 20 | Every document in `docs/` present and specific. README a stranger could follow. Change impact record names real affected functions and checks. |
| **Process** | 15 | DMAIC deliverables on their due dates. Stand-up log kept, including Week 13. Commits from every member across the sprint. Baseline tagged. |
| **Demonstration** | 10 | Scored **per member**. Can explain any function when asked. Names a real decision and its reason. |
| **Polish** | 10 | Output the stakeholder can read without asking. Messages that say what to do next. |

**How team and individual scores combine.** Functionality, Code Quality,
Documentation, and Polish are scored for the team. Demonstration is scored for each
member. Process is scored for the team, except that a member with no commits and no
stand-up entries across the sprint earns zero Process points individually.

**The fastest way to lose points** is a repository with one enormous commit on
Thursday of Week 14. Commit at the end of every block, every day, including Week 13.

---

## If you are stuck

**"Our stakeholder did not answer a question we needed."** Write it in the question
log, make the most reasonable assumption, write the assumption next to it, and keep
moving. That is exactly what professionals do when a client is unavailable.

**"Half our team is at BPA today."** Open the charter, find the backups, and do what
the timeline says for today with the people in the room. Write it in the stand-up log.

**"We disagree about what to build."** Use the decision rule in your working
agreement. If you did not write one, that is your first task.

**"Our tests all fail."** On Thursday of Week 12, that is correct. Tests written before the code
are supposed to fail. They start passing as you build.

**"Our tests all pass and the program is wrong."** Look at where the expected values in
your checks came from. If any of them came from running your own program, they prove
nothing. Thursday's lesson covers why.

**"We are behind."** Run the Sprint Board from Lab U06-02. If remaining work is bigger
than capacity, cut scope now, with the stakeholder's agreement, and log the decision.
Cutting on Thursday of Week 14 is not a decision. It is a surrender.
