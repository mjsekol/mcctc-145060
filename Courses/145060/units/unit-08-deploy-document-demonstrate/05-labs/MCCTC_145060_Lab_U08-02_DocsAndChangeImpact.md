# Lab U8-02: Documentation and Change Impact
## 145060 Programming · Unit 8 · Week 18, Tuesday and Wednesday

**Gate:** 3 (open tooling). **Duration:** Tuesday Build 1 for Parts 1 and 2 (35 minutes), and
Wednesday Build 1 for Part 3 (30 minutes, because the exam follows). **Competencies:** 5.6.8 (implementation plan, contingency plan,
data dictionary, user help), 5.7.1 (version management and interface control), 5.7.3 (analyze
the impact of changes), 1.2.5 (communicate for an intended audience), 1.2.11 (write
professional documents).

**You need:** your final project repository for Parts 1 and 2, and your finished Playlist Namer
from Lab U8-01 with `check_ready.py` for Part 3. If your Lab U8-01 is not at 9 passed, tell your
teacher before Wednesday.

**Parts 1 and 2 are not practice.** The two documents you write Tuesday are the first drafts of your
final project's `docs/IMPLEMENTATION_PLAN.md` and `docs/USER_HELP.md`. Part 3 uses Playlist Namer,
because everyone in the room has the same version of it and the results can be compared.

---

## The scenario

By Friday, strangers will use your final project, and a classmate may have to redeploy it while you
are at a game Thursday night. Neither of them can ask you anything. Meanwhile your study group wants
a change to Playlist Namer that sounds like one word and is not.

## What you will build

An implementation plan and user help for your own project that a classmate can follow without you,
tested by that classmate, and a change impact analysis written before a change and checked against
what actually broke.

---

## Starter templates

In your final project repository, create a `docs/` folder. Copy these headings into two new files.
Every heading must have real content under it when you finish.

`docs/IMPLEMENTATION_PLAN.md`:

```markdown
# Implementation Plan · <your project name> <version>

**Reader:**

## 1. What is being deployed
## 2. Before you start
## 3. Steps
## 4. Settings (data dictionary)
## 5. How to verify it worked
## 6. If it goes wrong (contingency plan)
## 7. Known limits
```

`docs/USER_HELP.md`:

```markdown
# <your project name>: How to Use It

## What this is
## How to use it
## Things that look like problems and are not
## What does not work
## Something went wrong
```

---

## Part 1: Tuesday, the implementation plan for your project

### Step 1. Name your reader
Under **Reader**, write one sentence describing the person who will follow this plan, and what
they already have.

**Observable result:** a sentence that names a person who is not you.

### Step 2. What is being deployed
Fill in the app name, the version you intend to ship (`1.0.0` is normal), the start command, and
what needs installing.

**Observable result:** four facts, each checkable against your repository.

### Step 3. Write the steps
Number them. One action per step. **Every step ends with what the reader should see when it
worked.** Include opening a terminal in the right folder. Render screens change, so write
**[VERIFY]** next to any Render menu name you have not seen yourself.

**Observable result:** no step that says only "check it works."

### Step 4. The data dictionary
A table with one row per environment variable your app reads: name, type, default, whether it is
set on Render, and what it controls. Then one row describing what `/health` returns.

**Observable result:** every `os.environ` in your code has a row. Search your files for
`os.environ` to be sure. `PORT` is always one of them.

### Step 5. Verification with real commands
Run your app locally with `$env:PORT = "10000"`. Paste the exact command and the exact output for
the start line, `/health`, and one real page, with no model running.

**Observable result:** three commands, each followed by output you copied from your terminal, not
typed from memory.

### Step 6. The contingency plan
A table of at least three things that can go wrong, how the reader recognizes each one (the exact
log line or page text), and what to do. One row must be rolling back to the last working version.

**Observable result:** every "how you recognize it" cell quotes real text.

---

## Part 2: Tuesday, user help and a real test

### Step 7. Write the user help
Use the template. Write for someone who has never heard of Python. No words from this list may
appear: `server`, `PORT`, `model endpoint`, `fallback`, `deploy`, `environment`.

**Observable result:** a partner reads it aloud and does not stop to ask what a word means.

### Step 8. Explain the fallback
Under **Things that look like problems and are not**, explain what your page says when the model or
API is missing, in words a stranger would understand, and why it is honest to show it.

**Observable result:** two or three sentences, no technical words.

### Step 9. Swap and follow
Push your project. Trade implementation plans with a partner. **Clone their repository into a new
folder**, then follow their plan **exactly as written**, from a fresh terminal, as far as the local
steps go. They do the same with yours. **The author may not speak** while the plan is being followed.

A fresh clone matters. It contains only what was committed, the same as Render gets.

**Observable result:** a list, on paper or in a file, of every place you had to guess or stop.

### Step 10. Fix and commit
Add every missing step your partner found to your plan. Commit with a message that says the plan
was tested by a partner.

**Observable result:** at least one change to your plan. If your partner found nothing, they were
helping you. Ask a different partner.

---

## Part 3: Wednesday, one real change request

Your group sends this:

> **Change request CR-01.** "Mood" sounds like a therapy app. Please rename it to "vibe"
> everywhere: the question on the page, the form, and the web address. So `/name?mood=rainy+day`
> becomes `/name?vibe=rainy+day`. Should be a two-minute change.

### Step 11. Predict before you touch anything
In your Playlist Namer folder, create `docs/CHANGE_IMPACT.md`. Fill in this table **before you edit
any code.**

| Area | What I predict the change touches or breaks |
|---|---|
| Code | |
| Tests and `check_ready.py` | |
| Documentation | |
| Settings on Render | |
| Stored data | |
| People who already use it | |
| Version number | |

**Observable result:** a complete table, committed, before any code change. The commit is your
proof that the prediction came first.

### Step 12. Make the change exactly as requested, on a branch
Create a branch named `vibe-rename`. Rename `mood` to `vibe` in the page question, the form field,
and the query parameter your handler reads, exactly as CR-01 asks.

**Observable result:** `/name?vibe=rainy+day` gives a saved name when you try it by hand.

### Step 13. Run the checker and compare
Run `python check_ready.py`. Add a second column to your table, **What actually happened**, and fill
it in from real results.

**Observable result:** at least one checker line that changed, pasted exactly. Look carefully at
every PASS too. A check can pass for a different reason than before.

### Step 14. Decide
Write one of these three decisions under the table, with your reasoning:

- **Reject** the change, and say what the group gets instead.
- **Accept it as breaking**, and give the version number it earns.
- **Accept it in a backward-compatible way**, meaning the old address keeps working, and give the
  version number that earns.

**Observable result:** a decision, a version number, and at least two sentences of reasoning that
mention a person who would notice.

### Step 15. Finish the note and commit
Complete `docs/CHANGE_IMPACT.md` with a section called **Alternatives considered** listing the two
decisions you did not choose and why. If you accepted the change, make your code match your
decision and run the checker again. Commit on the branch.

**Observable result:** the note is finished and the checker output for your final code is pasted
in it.

---

## Acceptance criteria

- [ ] Your final project has `docs/IMPLEMENTATION_PLAN.md` with all seven sections and real content
- [ ] Every step says what success looks like
- [ ] Data dictionary lists every environment variable the app reads
- [ ] Verification commands and outputs are copied from real runs
- [ ] Contingency plan has at least three rows, including a rollback
- [ ] Your final project has `docs/USER_HELP.md`, using none of the banned words, explaining the fallback
- [ ] A partner followed your plan from a fresh clone, and your plan changed because of it
- [ ] Change impact prediction committed before the code change
- [ ] Predicted and actual columns both filled in, with real checker output
- [ ] A decision with a version number, reasoning, and alternatives considered
- [ ] Work committed on the `vibe-rename` branch

---

## If it breaks

### 1. `can't open file` while following a partner's plan

```
C:\Python313\python.exe: can't open file 'C:\\Users\\...\\playlist_namer.py': [Errno 2] No such file or directory
```

**Cause:** not a bug in your partner's code. Their plan skipped the step that puts the terminal in
the right folder. Write it down. That is exactly what Step 9 exists to find. The path before the
colon depends on where Python is installed.

### 2. Check 5 fails after the rename

```
FAIL  5. a name page still works with no model, labelled as a saved name
      got status 400; the words 'saved name' were not on the page
```

**Cause:** `check_ready.py` still asks for `/name?mood=rainy+day`. After the rename your handler
looks for `vibe`, finds nothing, and treats it as an empty mood. **That is not a checker bug.** The
checker is standing in for everyone who already uses the old address. Record it as an actual impact.

### 3. The app will not start in your partner's fresh clone

For Storm Relay web, a missing `world.json` looks like this:

```
Cannot start: world.json could not be loaded ([Errno 2] No such file or directory: 'C:\\Users\\...\\world.json').
```

**Cause:** the file exists on your laptop and was never committed, so the clone does not have it.
Render builds from the same repository and would fail the same way. Commit the file, push, and have
your partner pull and try again. Your app's message will name a different file, or be a traceback if
your app does not catch it.

### 4. The checker cannot find your app

```
Cannot find playlist_namer.py. Put check_ready.py in the same folder as your app.
```

**Cause:** you copied `check_ready.py` into `docs/` along with your documents. The checker looks for
the app in its own folder, wherever you run it from. Keep it next to `playlist_namer.py`.

---

## Stretch goal

Add a data dictionary row for the `vibe` query parameter itself: its name, what characters it
accepts, its length limit, and what happens when it is missing. Then answer in your change impact
note: is a URL parameter an interface, the same way `PORT` is? Who depends on it?

---

## Submission checklist

- [ ] Final project: `docs/IMPLEMENTATION_PLAN.md` and `docs/USER_HELP.md` committed and pushed
- [ ] Partner's findings list included, or noted in the commit message
- [ ] Playlist Namer: `docs/CHANGE_IMPACT.md` committed on the `vibe-rename` branch
- [ ] `vibe-rename` branch pushed: `git push -u origin vibe-rename`
- [ ] AI usage log updated if a model helped write any document
- [ ] Both repository URLs submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Final project not yet running locally, or the plan is still three lines at the 15-minute mark | SCAFFOLDED |
| Writing steps and running commands to copy real output | STANDARD |
| Finished Part 1 early, or asked "shouldn't the old address still work?" before Step 12 | EXTENDED |
| Says documentation is only for software, or asks when anyone outside tech writes a plan like this | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Parts 1 and 2 document Playlist Namer, not your final project.** Your teacher gives you the
  finished Lab U8-01 solution, so this does not depend on how far your project has come.
- **Implementation plan:** sections 1, 2, and 4 are written for you. You write sections 3, 5, and 6.
- **Part 3:** the prediction table has the first two rows filled in as an example. You fill in the rest.
- **Checkpoints:** show your teacher after Step 5, after Step 9, and after Step 13.
- **Afterward:** your final project still needs its own plan and user help by Thursday. Use your
  Playlist Namer documents as the pattern.

**Acceptance criteria:** sections 3, 5, and 6 complete with real output; user help complete; partner
test done; Part 3 prediction and actual columns complete; a decision with a version number.

**Grading:** same 100-point scale, Requirements Fit judged against this list. Prediction before change
is still required.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus the backward-compatible version built and proved.

**Added requirement 1.** Build the compatible version: both `vibe` and `mood` work, `vibe` wins if
both are sent. Prove it with three recorded requests: `vibe=rainy+day`, `mood=rainy+day`, and
`vibe=%3Cscript%3E`.

**Added requirement 2.** Add a check to your own copy of `check_ready.py` that fails if
`/name?vibe=rainy+day` does not return a saved name. Now the checker protects both addresses.

**Hint, not the answer.** A dictionary's `get` method takes a default. Read about `dict.get` at
`https://docs.python.org/3/library/stdtypes.html#dict.get` and think about what the default could be
when the first key is missing.

**The honest warning.** After the rename, check 6 in the original checker still passes. Find out
why, and explain in your note whether it passes for the right reason. It is the most useful sentence
you will write this week.

**Acceptance criteria:** all STANDARD criteria, plus the three recorded requests, plus your new check
passing against your compatible version and failing against your Lab U8-01 version, which has never
heard of `vibe`.

---

## APPLIED

**For the student who thinks implementation plans and change impact only exist in software.**

**Changed scenario.** Parts 1 and 2 stay on your final project, because it is due. Part 3 moves to a
completely different domain: a process somebody really runs. The club's concession stand opening
checklist. A gaming tournament's check-in and bracket rules. The way your team hands off the
scorebook at a game.

**What you build in Part 3.** A short implementation plan for that process, written for a new
volunteer, then a change request against it in the voice of whoever runs it, such as "switch
check-in from paper to a sign-up form" or "change the bracket from single to double elimination."
Then Steps 11, 14, and 15: predict what the change touches, decide, and write the alternatives.

**The extra requirement that makes it the same lab.** Your prediction table uses the same rows:
the steps that change, what people must be told, what records already exist in the old format, who
notices first, and whether the old way must keep working during the switch. Then interview the
person who actually runs the process for five minutes, and add a column for what they said you
missed.

**Acceptance criteria:** STANDARD criteria for Parts 1 and 2; for Part 3, the plan, the change
request, the full prediction table, the interview column, and a decision with alternatives.

**Grading:** same scale. Requirements Fit is judged on whether the interview column changed your
analysis, which is the part that proves you tested your prediction against reality.
