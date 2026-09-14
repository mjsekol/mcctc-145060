# Project: Decision Engine
## 145060 Programming · Unit 2 · Due Tuesday, October 13, 2026, end of block

**Mode:** solo. **Gate:** 3, full tooling. **Periods:** five work blocks between Monday,
October 5 and Tuesday, October 13, listed in the milestone schedule.

**Competencies:** 5.3.5 (conditional control structures), 5.3.4 (relational operators and
compound conditions), 5.3.3 (logical operators), 5.3.2 (solve a truth table, through your
decision table), 5.3.7 (selection structures, optional). Latent 145130: 2.14.1 (how machine
learning differs from a decision tree). You also practice modeling with a decision tree and
writing test cases, which are formally taught and assessed in Units 3 and 4.

---

## The brief

Read this as though a person said it to you, because a person did.

> I make the same call over and over, all day, and I do not make it the same way twice. When
> I am rested I get it right. When I am tired, or rushed, or somebody is arguing with me, I
> guess. And when I hand the job to somebody else, they make it a completely different way,
> and then people complain that it is not fair.
>
> The rules are not secret. They live in my head. I want to answer a few questions about
> the thing in front of me and have something tell me which pile it goes in. Same answer every
> time. And when somebody asks why, I want to be able to show them.

**That is the whole brief.** It does not say what the decision is, what the piles are, or what
the questions are. Finding a real person with a real repeated decision, and getting their rules
out of their head and into a structure, is most of the work.

## Where the decision comes from

**Your Problem Inventory, or a person you actually know.** A coach deciding which team a
tryout player goes on. A parent deciding whether a chore counts as done. A manager at your job
deciding whether to approve a shift swap. A librarian deciding whether a book gets repaired,
discounted, or recycled. You deciding what to do on a Saturday.

It must be a **classification**: something comes in, and it goes into exactly one of several
categories. If your idea is really a calculation, that was the CLI Toolsmith. If your idea
needs to remember previous runs, it is too big for this unit.

**Use invented names and made-up examples in your code, README, and test table.** Never a
classmate's real information.

---

## Requirements

### Technical

1. **At least three inputs.** At least one is a number with a boundary that matters, and at
   least one is text or a yes-or-no answer.
2. **At least four distinct outcome categories.** A refusal message for bad input does not
   count as one of the four.
3. **A real decision tree.** Somewhere in your engine, **the next question depends on the answer
   to an earlier one**, so some inputs are never asked about. That is the nesting this project is
   named for.
4. **At least one compound condition** using `and`, `or`, or `not`.
5. **Refuse at least one impossible input value** with a clear message instead of classifying it.
6. **Clean text before you compare it.** Capital letters and stray spaces must not change the outcome.
7. **Name every cutoff.** No bare `18` or `2.5` inside a condition.
8. **No more than three levels of nested decisions,** unless your README explains why deeper is the
   honest shape of the problem. Apply Thursday's decision rule.
9. **Optional:** use `match` where one variable is compared to exact values. It earns Code Quality
   credit only if it is the right tool where you used it.
10. **It runs with `python yourengine.py`** and nothing else installed.

### Repository

```
your-engine-name/
  yourengine.py
  README.md
  .gitignore
```

### README, six sections

1. **The decision.** Who makes it, how often, and what goes wrong now.
2. **How to run it.** The exact command.
3. **The decision tree.** A drawing, a photo of a drawing, or a text tree. It must match your code.
4. **Test table.** One row per test: the answers typed, the expected outcome, the actual outcome. Every
   outcome at least once. Every boundary value and the value one step past it. **Actual must come from a
   real run.** Your instructor will run two rows of your table live during your demo.
5. **Known limitations.** At minimum, what happens when somebody types a word where a number goes. Run
   it and paste the error.
6. **How this differs from machine learning.** One paragraph. Who chose your rules, what a trained model
   would need instead, and one thing your engine can do that a trained model would struggle with.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use a loop | Loops arrive Thursday, October 15. Your engine classifies one thing per run. |
| Use a function, list, or dictionary | Units 4 and 5. Writing one you cannot explain fails the course standard. |
| Import a library | The stakeholder wants something that runs anywhere, and you have not been taught dependencies. |
| Train or call any AI model to make the decision | The brief asks for rules a person can see and defend. That is the point of a hand-written decision tree. |
| Put anyone's real personal information in the repository | It is public. Same rule as every week. |

AI tools are allowed for help, under the usual Gate 3 rules, with an AI usage log. Every line of the
engine must be something you can explain.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Mon Oct 5, end of Build 2 | The decision in one sentence, who makes it, how often, and what goes wrong now |
| **Measure** | Mon Oct 5, end of Build 2 | Every input with its type and its valid range; every outcome category |
| **Analyze** | Tue Oct 6 and Wed Oct 7, Build 2 | The rules written as sentences with every **and**, **or**, and **not** underlined; the decision tree drawn; a decision table listing input combinations and the outcome each one should get |
| **Improve** | Wed Oct 7 Build 2 and Thu Oct 8 Build 1 | Build it. Flatten any nesting that is a pyramid of requirements. |
| **Control** | Tue Oct 13, Build 2 | Run every row of your test table and record the actual results. README complete. Push. Demo. |

**Analyze is the phase that saves you.** Your decision table from Wednesday **is** your test table. Write
the expected outcome for every row before you write a line of code, and you will know the instant your
program disagrees with you.

---

## Milestone schedule, against actual class days

| Day | Block | Goal |
|---|---|---|
| Mon Oct 5 | Build 2 | Define and Measure. **No code.** |
| Tue Oct 6 | Build 2 | Analyze: rules as sentences, decision tree drawn |
| Wed Oct 7 | Build 2 | Analyze: decision table, 15 minutes. Improve: start the engine. |
| Thu Oct 8 | Build 1 | Improve: every path runs. Apply the flattening rule to your own nesting. |
| Fri Oct 9 | No class | |
| Mon Oct 12 | none | Build 1 is the club sign-up lab and Build 2 is Problem Drop 1. |
| Tue Oct 13 | Build 2 | Control: run the test table, finish README, push, demo circles. **Due end of block.** |

**Monday October 12 has no project time.** If your engine does not run every path by the end of Thursday,
October 8, tell your instructor on Thursday, not Tuesday.

---

## Three worked scope examples

These are here so you can calibrate. **Do not build any of these three.** They are taken.

### Too small
> **Is It a School Day?** Asks the day of the week. Prints yes or no.

One input, two outcomes, no boundary, no tree. It classifies something, and it meets almost none of the
requirements.

### About right
> **Shift Swap Approver** for a manager at a fast-food restaurant. Asks the requesting employee's role
> (crew or shift lead). For crew, asks whether a replacement has agreed and how many hours the replacement
> already has this week. For shift leads, asks only whether another shift lead can cover. Outcomes:
> APPROVE, APPROVE WITH MANAGER SIGN-OFF, DENY: NO COVER, DENY: OVERTIME. Refuses negative hours. The
> overtime cutoff is a named constant.

Four inputs, four outcomes, a real tree (shift leads are never asked about hours), a compound condition,
a boundary that matters, and a refusal.

### Too big
> **Smart Shift Scheduler.** Reads the whole week's schedule from a file, approves every swap request in a
> queue, remembers who swapped last month, and learns which employees usually flake.

Files are Unit 5. A queue needs a loop and a list. Remembering last month needs saved data. "Learns" is
machine learning, which this project is specifically not. This is a good idea for the spring.

**The calibration question:** can you describe every path through your engine in the time it takes to
read your decision tree out loud? If the tree does not fit on one sheet of paper, it is too big for this week.

---

## The five-minute demo

Tuesday, October 13, in a circle of four classmates.

1. **The decision, in one sentence.** Who makes it and how often. (30 seconds)
2. **Show your decision tree.** Point to the place where the next question depends on the answer. (60 seconds)
3. **Run it live, twice.** Two different outcomes. Then run the one test-table row your circle picks. (90 seconds)
4. **One decision you made, and why.** A cutoff, a category you merged or split, a question you moved inside a
   branch, a place you chose not to flatten. (90 seconds)
5. **How this differs from machine learning,** in two sentences. (30 seconds)

**Part 4 is the graded part of Demonstration.** Anybody can run a program. The decision is the evidence that
you built it.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Runs clean on every row of your test table. Every requirement 1 through 7 met. Boundaries correct. Impossible input refused. |
| **Code Quality** | 20 | Real decision tree where the next question depends on the answer. Pyramids of requirements flattened. Named cutoffs. Comments explain why the tree has the shape it has. `match` used only where it fits, if used. |
| **Documentation** | 20 | All six README sections. Test table covers every outcome and every boundary, with actual results that came from real runs. Machine learning paragraph is accurate and specific. |
| **Process** | 15 | Every DMAIC checkpoint on time. The decision table existed before the code. Commits spread across the work days, not one commit on Tuesday. |
| **Demonstration** | 10 | Can explain any line. Names a real decision and the reason for it. The live test row matches the table. |
| **Polish** | 10 | A stranger can use it without asking a question. Prompts say what to type. Outcomes say why. |

**The fastest way to lose Documentation points** is a test table whose Actual column was copied from the
Expected column. Two rows get run live. If either disagrees, the table is scored as unverified.

---

## If you are stuck

**"I cannot think of a decision."** Think of the last time somebody said "it depends." On what? That list is
your inputs, and the possible answers are your outcomes.

**"My engine is one long elif chain."** That can be fine inside a branch. Ask which of your questions does not
matter for some answers, and move it inside the branch where it does. That is the tree.

**"Two of my outcomes both match the same input."** Your categories overlap. Decide which one wins and put it
first, or change the rule so they cannot both match. That is Week 5 Monday.

**"I want it to handle a whole list of things."** Not this project. Write it in Known limitations, and build it
in Unit 3 when you have loops.
