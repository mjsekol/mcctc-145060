# Lab U7-04: Study Hall Security Review
## 145060 Programming · Unit 7 · Week 18

**Gate:** 2 in spirit, you are reviewing code you did not write, then repairing it.
**Duration:** three Build blocks, Tuesday through Thursday.
**Competencies:** 9.3.1 (identify vulnerabilities), 9.3.3 (secure coding, input
validation), 9.3.4 (secure configuration), 2.1.1 (CIA), 5.5.1 (data validation).

**Files for this lab are in** `lab-u07-04-files/`: the `study_hall/` app (five files and
a `data/` folder) and `helper_model_stub.py`. Copy the whole folder into your repository.
The review template is `MCCTC_145060_Lab_U07-04_ReviewTemplate.md` in this folder.

---

## The scenario

The student tutoring club runs a command-line helper called Study Hall Helper. Members
log in, ask a local model for a hint, share notes, thank each other with points, and do
quick math. It runs. It is also full of security problems, and the club wants a review
before it goes on the shared lab machines. You are the reviewer.

## What you will do

Find at least eight vulnerabilities, prove each one with a command you can rerun, map
each to confidentiality, integrity, or availability, and fix at least four across four
different categories. This is a real review: the code runs, and every problem is real.

---

## The rule that makes this hard

**You may not rewrite the app from scratch.** You read code somebody else wrote, find
what is wrong, and change it safely. Deleting it and starting over is not a review and it
is not what this teaches. Reading unfamiliar code, understanding it well enough to change
one thing without breaking the rest, is most of a real security job.

---

## Before you start

Start the stub model server in one terminal:

```
python helper_model_stub.py
```

Run the app in a second terminal, from inside the `study_hall` folder:

```
cd study_hall
python study_hall.py
```

Log in as `pixelmoth` and try the commands. Type `help`. Play with it for five minutes
before you read a line of code. A reviewer who has not run the program is guessing.

---

## The categories to hunt

There are at least eight planted vulnerabilities, at least one in each of these:

- **Input validation:** a value used without being checked.
- **Path traversal:** a file name that can climb out of its folder.
- **Secrets in code:** a key or code written into a file.
- **Unsafe evaluation:** input run as code.
- **Prompt injection:** player text that can steer the model.
- **Verbose error leakage:** an error that hands out internal details.
- **Missing timeout:** a call that can hang forever, an availability problem.
- **Save-file integrity:** a way to write something false into a saved file.

---

## The steps

### Part 1: Tuesday, reconnaissance and the input defects

**Step 1.** Run the app and play with it. In the review template, fill in the first three
rows from what you observe, not from the code.

**Step 2.** Find the two input-driven defects: the `calc` command and the way the model
helper handles a member's question. Reproduce each with a recorded command. For the
model one, run the stub in `obedient` mode:

```
python helper_model_stub.py --mode obedient
```

**Observable result:** two defects located, each with a command that reproduces it, in the
template.

### Part 2: Wednesday, the rest of the defects, and four fixes

**Step 3.** Read every file and find the remaining defects: secrets, verbose errors, the
missing timeout, the path traversal, and the way `thank` handles the point amount.
Reproduce each.

**Step 4.** Fix at least four defects across four different categories. Rerun the app and
confirm each fix holds and nothing else broke.

**Observable result:** at least eight defects in the template, and four fixed and verified.

### Part 3: Thursday, CIA mapping and the write-up

**Step 5.** Complete the CIA column for every defect. For each, say whether it breaks
confidentiality, integrity, or availability, and why in one line.

**Step 6.** Finish the template's five-dimension scores and the summary. Commit and push.

**Observable result:** the review template is complete: every defect has a location, a
reproduction command, a CIA letter, and a fix.

---

## Acceptance criteria

- [ ] At least eight defects found, each with a location and a reproduction command
- [ ] At least one defect in each of the eight categories
- [ ] At least four defects fixed across four categories, verified by rerunning
- [ ] Every defect mapped to a CIA letter with a one-line reason
- [ ] The five-dimension review scored with a sentence per dimension
- [ ] The app still runs after your fixes
- [ ] Committed and pushed

---

## If it breaks

### 1. The app crashes on a command you did not expect

That may be a defect, not your mistake. Record the command and the crash. A program that
crashes on ordinary input is a real finding.

### 2. Your fix broke a normal command

Good, that is the review doing its job. Your change touched something another part relied
on. Read your change and ask what else used that value. Fix it so both work.

### 3. The model command hangs

That is the missing-timeout defect, reproduced. Run the stub in `slow` mode to see it on
purpose. Your fix is to add a timeout, from `settings`, to the model call.

### 4. You cannot reproduce a defect you are sure is there

Run the exact command by hand and read the output slowly. Some defects, like the secrets
in the file, are not triggered by running the app; they are found by reading. Say how you
found each one.

---

## Stretch goal

The app has one more weakness that none of the eight categories names, in how it handles
what the model sends back. Find it, and say what happens when the model reply is missing
its `response` field. Then, like SQ-05 taught, note in your write-up that a review is not
finished merely because you found the ones you were looking for.

---

## Submission checklist

- [ ] Review template complete: eight-plus defects, each with location, command, CIA, fix
- [ ] Four fixes applied and verified by rerunning the app
- [ ] No real credentials anywhere, even fake-looking ones, in your fixes
- [ ] `git status` clean, pushed, template renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Found fewer than three after Part 1, unsure how to look | SCAFFOLDED |
| Working steadily, finding and reproducing defects | STANDARD |
| Found all eight and the bonus early | EXTENDED |
| Says security is not their thing | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **A category checklist with a hint per category** is provided, naming which file to look
  in for each, without naming the line.
- **Steps:** find at least six, fix at least three across three categories.
- **Step 5 stays.** Do not cut the CIA mapping. It is the point of the week.

**Acceptance criteria:** six defects with reproduction commands, three fixed across three
categories, CIA mapped for all six. Full completion earns what a STANDARD student earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring judgment.

**Added requirement.** Rank all your defects by how much damage each would do if this app
ran on the shared lab machines, and defend the ranking in a paragraph. Then pick the two
you would fix first if you had one hour, and say why those two.

**Hint, not the answer.** Ranking is not by category, it is by impact. Ask which defect
lets an attacker do the most, and which is simplest to trigger. A defect that is both is
your top priority. Use the CIA letters: a confidentiality leak of a key is often worse
than an availability hiccup, but not always.

**The honest warning:** there is no single correct ranking, and a good defense of a
defensible order earns full credit. A ranking with no reasoning does not, even if it
matches the key's suggested order.

**Acceptance criteria:** all STANDARD criteria, plus a ranked list with a reasoned
defense and a top-two-to-fix-first choice.

---

## APPLIED

**For the student who says security is not their thing.** Same skills, their own code.

**Changed scenario.** Review one of your own past projects from this course, the CLI
Toolsmith or a text adventure version, for the same eight categories. Your own code is
the codebase.

**What you do.** Find every place your project takes input it does not fully check, reads
a file by a name it does not validate, or could hang on a call with no timeout. You may
find zero of some categories; that is a real result, and saying so is part of the review.

**The extra requirement that makes it the same lab.** Your write-up must cover all eight
categories, stating for each whether your project has that weakness, with evidence, and
what you would change. "Not applicable" must be justified, not assumed.

**Acceptance criteria:** all eight categories addressed for your own project, with
evidence and a fix or a justified "not applicable" for each.

**Grading:** same scale. Requirements Fit is judged on whether every category was honestly
checked, including the ones where the answer was "not present."
