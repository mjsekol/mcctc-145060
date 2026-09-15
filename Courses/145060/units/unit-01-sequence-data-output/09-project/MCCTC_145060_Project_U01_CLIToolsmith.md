# Project: CLI Toolsmith
## 145060 Programming · Unit 1 · Due Week 4, Friday

**Mode:** solo. **Gate:** 3, full tooling. **Periods:** four Build 2 blocks,
Monday through Thursday of Week 4.

**Competencies:** 5.1.1 (how programs solve problems), 5.2.1, 5.2.2, 5.2.3
(types, scope, arithmetic), 5.2.4 (string operations), 5.5.5 (naming and comments),
5.5.6 (format output), 5.5.7 (read inputs), 1.2.12 (technical writing).

---

## The brief

Read this as though a person said it to you, because a person did.

> I keep doing the same calculation over and over and I keep getting it wrong. Every
> time I need the answer I open a calculator, remember the wrong formula, do it in the
> wrong order, and then second-guess it for a week. I do not need an app. I do not
> want to install anything. I want to type one command, answer a few questions, and
> see the number, laid out so I can actually read it.
>
> It has to be right, and I have to be able to tell that it is right.

**That is the whole brief.** Notice what it does not say. It does not tell you what
the calculation is, what the questions are, or what the output should look like. Those
are yours to decide, and deciding them is most of the work.

## Where the problem comes from

**Your Problem Inventory, from Week 1.** Pick one entry. It has to be a real problem
you actually wrote down about a real person, and that person can be you.

If nothing in your inventory fits a calculation, add an entry now. Do not invent a
problem to fit a program you already want to write. That is backwards and it shows.

---

## Requirements

### Technical

1. **At least four values collected from the user** with `input()`, each converted
   deliberately, and at least one of them left as text on purpose.
2. **At least three calculated values** built from other values, not typed in.
3. **No number appears twice in your file.** If you need it twice, name it.
4. **Formatted output.** Every number formatted with an f-string. Money to two decimal
   places. Columns aligned.
5. **At least one string operation** from Week 3: cleaning, slicing, or building.
6. **Comments explain why, not what.** A comment restating the code earns nothing.
7. **It runs from the command line** with `python yourtool.py` and nothing else
   installed.

### Repository

```
your-tool-name/
  yourtool.py
  README.md
  .gitignore
  sample-run.txt      <- a real run, pasted, showing questions and answers
```

### README, four sections

1. **The problem.** Quote your Problem Inventory entry. Who has it, how often.
2. **How to run it.** The exact command.
3. **A real run.** Paste one, showing what you typed and what came back.
4. **Known limitations.** What breaks it. At minimum, what happens when somebody types
   a word where a number goes. Run it and paste the error.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use a library you did not import from the standard library | You have not been taught dependency management, and a tool that needs an install is not a tool your stakeholder will run. |
| Use a loop or a function | You have not been taught them. Unit 3 and Unit 4. Writing one you cannot explain fails the course standard. |
| Copy a calculator off the internet and rename the variables | The brief says "I have to be able to tell that it is right." You cannot tell that about code you did not reason through. |
| Ask for anybody's personal information | It goes in a public repository. Same rule as every week. |

**On conditions:** `if` arrives Thursday. The project does not require one. If you add
one on Thursday to make the output smarter, that is a stretch and it earns credit under
Requirements Fit. It is not part of the base requirement and you will not lose points
for leaving it out.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Mon, end of Build 2 | Problem statement in one sentence, plus the inventory entry it came from |
| **Measure** | Mon, end of Build 2 | Every input listed, every output listed, with its type |
| **Analyze** | Tue, end of Build 2 | The arithmetic written out on paper before it is code |
| **Improve** | Wed and Thu | Build it |
| **Control** | Thu, end of Build 2 | README complete, three runs recorded, limitations named |

**Analyze is the one students skip and it is the one that saves them.** Write the
formula on paper first. Half the projects that go wrong go wrong because the arithmetic
was invented while typing.

---

## Milestone schedule, against actual class days

| Day | Build 2 goal |
|---|---|
| Week 4 Mon | Define and Measure. No code. |
| Week 4 Tue | Inputs collected and converted. Program runs and echoes them back. |
| Week 4 Wed | Calculations and formatted output. The tool works. |
| Week 4 Thu | README, sample run, limitations. Optional condition. Push. |
| Week 4 Fri | Demos and submission. |

---

## Three worked scope examples

These are here so you can calibrate. **Do not build any of these three.** They are
occupied.

### Too small
> Asks for two numbers and adds them.

Two inputs, one calculation, nothing formatted, no string work. It meets none of the
technical requirements and it solves no problem anybody has.

### About right
> **Gas Money Splitter.** Asks the trip distance, the car's miles per gallon, the price
> per gallon, and how many people are going. Works out total fuel used, total cost, and
> cost per person. Prints a small table. Names the driver, who is text and not
> converted.

Four inputs, three calculations, formatted output, one value deliberately left as text.
Solves a real recurring argument.

### Too big
> Tracks every trip you take all year, saves them to a file, and produces monthly
> reports with graphs.

Saving to a file is Unit 5. Monthly anything needs loops, which is Unit 3. Graphs need
a library you may not use. This is a good idea and it is a Unit 5 or Unit 6 idea.

**The calibration question:** can you describe your tool's entire behaviour in three
sentences? If not, it is too big for this week.

---

## The five-minute demo

Friday. Some of you present, everybody submits.

1. **The problem, in one sentence.** Who has it and how often. (30 seconds)
2. **Run it live.** Real inputs, real output. (90 seconds)
3. **One decision you made and why.** A conversion choice, a formatting choice, a thing
   you cut. (90 seconds)
4. **One thing it does not handle.** (60 seconds)
5. **Questions.** (30 seconds)

**Item 3 is the graded part.** Anybody can run a program. The decision is the evidence
that you built it.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Runs clean. Correct arithmetic on three different input sets. All four technical minimums met. |
| **Code Quality** | 20 | Readable names. Comments explain why. No number written twice. Deliberate conversions. |
| **Documentation** | 20 | Four README sections. Sample run pasted. Limitations real and observed, not guessed. |
| **Process** | 15 | DMAIC checkpoints hit on time. Commits spread across four days, not one lump Thursday. |
| **Demonstration** | 10 | Can explain any line. Names a real decision and its reasoning. |
| **Polish** | 10 | Output a stranger can read without asking. Aligned columns, sensible decimals, labelled values. |

**The fastest way to lose Process points** is a repository whose entire history is one
commit at 10:14 on Thursday. Commit at the end of every block.

---

## If you are stuck

**"I cannot find a problem in my inventory that is a calculation."** Look for entries
with a number in them, or entries where somebody is guessing at something. Guessing is
usually arithmetic somebody has not written down.

**"My tool feels too simple."** Read the "about right" example again. Four inputs and
three calculations is the bar. A tool that does one thing correctly and legibly beats
one that does four things badly.

**"My arithmetic gives a weird decimal."** That is floating point and it is normal. The
fix is formatting, not different arithmetic. `:.2f` in the f-string.

**"I want to use a loop."** Not this project. Write it in `Known limitations` as
something you would add, and build it in Unit 3 when you have the tool.
