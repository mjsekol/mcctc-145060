# Week 13 Self-Directed Sprint Guide
## 145060 Programming · Unit 6 · Week 13 · BPA Regional Week

**Read this on Friday of Week 12, before you leave.** On Monday nobody will be able
to explain it. Your instructor is supervising BPA Regional competitors all week and a
substitute who is not a programmer will be in the room.

**This week introduces nothing new.** Every task uses something you already learned
in Week 12 or earlier. If a task seems to need something you have never seen, you
have misread the task. Read it again, then check the lecture note it names.

---

## Why this week matters more than it looks

Real teams lose their lead, their expert, or half their people to other deadlines all
the time. The work does not stop, and nobody writes a special plan for it at the last
minute. The team that planned for the gap keeps moving. The team that did not spends
the week waiting.

You have the plan. It is this document plus the timeline and charter your team wrote
last week. By Friday your team will have a design, a running first increment, and a
written sprint review, **without anyone telling you what to do next.** That is the
skill.

---

## Who is in the room

- **Competitors** are at BPA Regional events on some days. Your charter says which days.
  When they are back, they read the stand-up log and pick up where their backup left
  off.
- **Everyone else** works this plan with their team.
- **The substitute** keeps the room running, takes attendance, and collects questions
  on the STUCK board. The substitute does not answer programming questions and you
  should not ask them to.

---

## Rules for the week

1. **Stand-up first, every day, in writing,** in `docs/standups.md`. Ten minutes at
   the start of Build 1. Present members fill in their row. Absent members get a row
   that says where they are.
2. **Backups do the absent owner's job.** Check the roles table in your charter.
3. **Commit at the end of every block.** The commit history is how your instructor sees
   Week 13 happened.
4. **When you are stuck for 10 minutes:** check the lecture note, ask your team, ask
   another team, then write the question on the STUCK board **and** in your question
   log, make the most reasonable assumption, write it down, and keep going.
5. **When your team disagrees:** use the decision rule in your working agreement.
   Record the decision in `docs/decision_log.md`. Do not wait for Monday of Week 14 to
   settle it.
6. **Stakeholder questions go in the question log.** Your stakeholder is not available
   this week. That is realistic, and the log is how real teams handle it.
7. **No personal information in any file or any AI tool.** Same rule as every day.
8. **Gate 1 reps are closed.** Plain editor, no AI, no autocomplete, even with nobody
   watching. Especially with nobody watching.

---

## Week 13, Monday · Day 6 · BPA coding events

| Time | What you do |
|---|---|
| 0-15 | Bell ringer on the board, then Gate 1 Rep 05 on paper |
| 15-25 | Written stand-up in `docs/standups.md` |
| 25-60 | **Build 1.** Lab U06-02 Sprint Board, Part 1 (steps 1-6) |
| 60-65 | Stand up, walk, reset |
| 65-105 | **Build 2.** Analyze: start `docs/design.md` |
| 105-118 | Commit, push, and write tomorrow's first task at the bottom of the stand-up |

**Build 1 · Lab U06-02 Part 1.** `05-labs/MCCTC_145060_Lab_U06-02_SprintBoard.md`. Work
individually, sit with your team. Every step has an observable result you can check
yourself.

**Build 2 · Analyze.** Open the design notes template in
`MCCTC_145060_Templates_U06_SprintDocs.md`. As a team:

1. Write down every data file your program reads, with its columns or keys and one
   example row in the stakeholder's shape.
2. List the functions you will need. For each: what it takes, what it returns, what it
   refuses, and which acceptance criteria it serves. Use your signed requirements and
   your failing test file. **Every check in your test file should point at a function
   in this table.**
3. Split the list: who drafts which docstring tomorrow.

**Done when:** the data files section is complete and the functions table has a row for
every acceptance criterion.

---

## Week 13, Tuesday · Day 7 · BPA coding events

| Time | What you do |
|---|---|
| 0-15 | Bell ringer, then Gate 1 Rep 06 on paper |
| 15-25 | Written stand-up |
| 25-60 | **Build 1.** Finish `docs/design.md` (due end of Build 1), then Lab U06-02 Part 2 |
| 60-65 | Reset |
| 65-105 | **Build 2.** Sprint 1 planning, then build |
| 105-118 | Commit, push, stand-up note for tomorrow |

**Build 1 · Finish Analyze.** Add pseudocode for the hardest function, and the top three
risks with a plan for each. **Design notes are due at the end of Build 1.** Then Lab
U06-02 steps 7-12 for anyone who has not finished.

**Build 2 · Sprint 1 planning, 15 minutes.** This is the first agile ceremony you run
without your instructor. Follow these steps exactly.

1. Put every function from the design table into your `tasks.csv` as a task, with an
   owner role, an estimate in build blocks, `todo`, and a due day no later than Day 10.
2. Run your Sprint Board: `python sprint_board.py tasks.csv 7 <people present this week>`.
3. If it says AT RISK, move the lowest-value tasks to a due day of 12 or later, and
   write the decision in the decision log with the reason.
4. The Facilitator reads the Sprint 1 list aloud. Every member says one task they own.

Then build. Start with the function that reads the data file, because every other
function needs its output.

**Done when:** `tasks.csv` exists in your repository, the Sprint Board runs on it, and
every member has at least one task marked `doing`.

---

## Week 13, Wednesday · Day 8 · BPA coding events

| Time | What you do |
|---|---|
| 0-15 | Bell ringer, then Gate 1 Rep 07 on paper |
| 15-25 | Written stand-up, including the Sprint Board output |
| 25-60 | **Build 1.** Build |
| 60-65 | Reset |
| 65-105 | **Build 2.** Build |
| 105-118 | Commit, push, update `tasks.csv` statuses, stand-up note |

**Build 1 and Build 2 · Improve.** Build the functions in your Sprint 1 list. After each
function, run your acceptance tests:

```
python test_yourprogram.py
```

**Watch the pass count climb.** It is the most honest progress measure you have, as
long as every expected value came from the stakeholder and not from your own program.
A function that makes no new check pass is either unfinished or not needed.

**When a check fails and you are sure the code is right:** do not change the expected
value in the check to match your output. That expected value came from the stakeholder.
Put it in the question log and ask the stakeholder on Monday of Week 14. Changing a test
to agree with your code is how a team ships the wrong program with a perfect score.

**Done when:** at least one more acceptance check passes than yesterday, and
`tasks.csv` is current.

---

## Week 13, Thursday · Day 9 · No BPA events

| Time | What you do |
|---|---|
| 0-15 | Bell ringer, then Gate 1 Rep 08 on paper |
| 15-25 | Written stand-up |
| 25-65 | **Build 1.** Gate 2 W13, individually, in silence, 40 minutes |
| 65-70 | Reset |
| 70-105 | **Build 2.** Build |
| 105-118 | Commit, push, stand-up note |

**Build 1 · Gate 2 W13.** `07-gate2-adversarial/MCCTC_145060_Gate2_W13.md`. This is an
individual written review of AI-generated code. The instructions are complete in the
file. You may run the code. You may not ask a model whether it is correct, because the
model is what is being reviewed. You may not work with your team on this one.

**Build 2 · Improve.** Keep building. Most competitors are back today. They read the
stand-up log first, then take their tasks back from their backups.

**Done when:** Gate 2 is submitted, and the team has a program that runs start to
finish on the sample data, even if some checks still fail.

---

## Week 13, Friday · Day 10 · BPA presentation events

| Time | What you do |
|---|---|
| 0-15 | Bell ringer, then written stand-up |
| 15-50 | **Build 1.** Written sprint review, due end of Build 1 |
| 50-55 | Reset |
| 55-105 | **Build 2.** Catch-up, then Gate 1 reps or side quest |
| 105-118 | Commit, push, and check the Monday list below |

**Build 1 · Sprint 1 review.** Use the `docs/sprint_review_1.md` template.

1. Run `python test_yourprogram.py` and paste the **whole** output.
2. For every failing check, write why it fails and your plan.
3. Copy every open question from the question log into the review.
4. Run the Sprint Board for Day 10 and paste the output.

**This review is written, not presented.** Your stakeholder reads it Monday.

**Build 2 · Catch-up first.** In this order:

1. Anything from this week your team has not finished.
2. Gate 1 Reps 09 and 10, on paper, for everybody. Hand them to the substitute.
3. **SQ-12 Read the Source**, from the Side Quest Catalog, for anybody whose team work is
   fully current. Reading code somebody else wrote is exactly what Monday's peer review asks
   of you.

**Done when:** `docs/sprint_review_1.md` is committed with the real test output in it.

---

## Ready for Monday of Week 14

Your instructor is back. Before you leave Friday, check every line:

- [ ] `docs/standups.md` has an entry for every day this week
- [ ] `docs/design.md` is complete
- [ ] `tasks.csv` and the Sprint Board run
- [ ] `docs/sprint_review_1.md` has real test output in it
- [ ] Every question you could not answer is in `docs/question_log.md`
- [ ] Every decision is in `docs/decision_log.md`
- [ ] Gate 2 W13 is submitted by every member who was present Thursday
- [ ] Everything is pushed

**On Monday your team reviews another team's code and another team reviews yours.** The
code you push on Friday is the code that gets reviewed.

---

## If something goes wrong this week

**"The lab machines are down."** Your substitute has paper backups. For your team: write
design notes, pseudocode, and acceptance criteria by hand and photograph them into the
repository when the machines return.

**"A teammate is not doing anything."** Follow the step in your working agreement. If
it continues, write a factual note for your instructor: what was assigned, when, and
what happened. Facts, not feelings. Leave it with the substitute.

**"We think our requirements are wrong."** Maybe. Log the question, make an assumption,
keep building, and raise it Monday. Do not rewrite signed requirements alone.

**"Our whole team is at BPA today."** Then you are not on a team today. Work Gate 1 reps
and your own lab, and write that in the stand-up log for tomorrow.

**"We finished everything."** You have not. Read your acceptance criteria one at a time
and try to break each one with input the stakeholder did not mention. Every break you
find is a new question for the log and a new check for the file.
