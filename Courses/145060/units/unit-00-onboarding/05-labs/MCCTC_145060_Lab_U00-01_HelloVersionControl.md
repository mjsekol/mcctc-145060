# Lab U0-01: Hello, Version Control
## 145060 Programming · Unit 0 · Week 1 · SQ-01

**Gate:** 3 (open tooling). **Duration:** two 40-minute Build 2 blocks, Wednesday
and Thursday. **Competencies:** 5.1.8 (describe version control and the relevance of
documentation), 5.4.1 (configure options, preferences, and tools), 5.4.2 (write and
edit code in the IDE), 5.4.3 (interpret a working program), 1.2.12 (technical
writing, the README).

**This lab is required before any other work in this course is graded.** That is
not a scheduling threat. Every graded artifact from Unit 1 forward lives in a
repository, so until you have one that works, there is nowhere for your work to go.

---

## The scenario

You are the person in your group who gets the texts. What time does it start, where
is it, what do I need to bring, is it still happening. You answer the same four
questions eleven times, by hand, every week, and the eleventh person still shows up
without a laptop.

## What you will build

A repository on GitHub containing a small program that prints those details, a
README a stranger can follow, and a `.gitignore` that was written before anything
else.

**The program is small on purpose.** The graded artifact this week is the
repository: the ordering of your commits, the quality of your messages, and the
fact that nothing in it should not be there. In Unit 1 the programs get real. This
week the habits get installed.

---

## Starter code

Create a file called `event_card.py` and type this in. It runs right now. It does
nothing useful yet.

```python
# event_card.py
# Prints the details people always text me for.
#
# This file runs right now. It does not do anything useful yet.
# Your job is to replace each TODO with a real print line.

# TODO 1: Replace the placeholder below with the real name of your event.
print("EVENT NAME GOES HERE")

# TODO 2: Print the date and the start time on one line.

# TODO 3: Print where it is.

# TODO 4: Print one blank line, using print() with nothing inside the parentheses.

# TODO 5: Print one thing people need to bring.
```

Running it produces exactly one line:

```
EVENT NAME GOES HERE
```

Pick a real event. Something you actually go to: a practice, a shift, a club, a
meet, a group project session. Do not invent one. The README you write on Thursday
works better when the thing is real.

---

## Part 1: Wednesday, steps 1 through 6

### Step 1. Make the folder and open it

Create a folder named `event-card` somewhere you will find it again, and open that
folder in VS Code. Open the integrated terminal.

**Observable result:** The terminal prompt shows you are inside the `event-card`
folder. If it does not, everything after this step goes into the wrong place.

### Step 2. Create the repository

```
git init -b main
```

**Observable result:** Git prints a line saying it initialized an empty repository.
Run `git status` and confirm it says `On branch main` and `No commits yet`.

### Step 3. Write `.gitignore` first, before anything else exists

Create a file named exactly `.gitignore`, with the dot at the front, containing one
line:

```
scratch.txt
```

**Observable result:** `git status` lists `.gitignore` as an untracked file.

**Why this is step 3 and not step 8.** `.gitignore` controls whether Git *starts*
tracking a file. It has no power over a file already in the history. Committing it
first, before there is anything to protect, is the only ordering that works. On
Thursday you will watch this fail when it is done in the other order.

### Step 4. Commit `.gitignore` by itself

```
git add .gitignore
git commit -m "Ignore my scratch file so it never gets pushed"
```

**Observable result:** Git reports one file changed. `git log --oneline` shows
exactly one commit.

### Step 5. Create the starter file and run it

Create `event_card.py` with the starter code above. Save it. Then:

```
python event_card.py
```

**Observable result:** One line of output, `EVENT NAME GOES HERE`, and no error.

### Step 6. Replace every TODO, then run it again

Fill in all five TODOs with real details for your event. Delete the placeholder
line. Keep the comments, and rewrite them so they describe your actual choices.

**Observable result:** Five lines of output. The fourth is blank. No traceback.
Then commit it:

```
git add event_card.py
git commit -m "<a message that says what this does and why>"
```

`git log --oneline` now shows two commits.

### Acceptance criteria, Part 1

Check these yourself before you leave Wednesday.

1. `git log --oneline` shows at least two commits, and `.gitignore` is the first one
2. Running `python event_card.py` produces five lines with the fourth one blank
3. The blank line was made by `print()` with nothing inside, not by `print(" ")`
4. No commit message is `update`, `stuff`, `fixed`, `first commit`, or your name

---

## Part 2: Thursday, steps 7 through 12

### Step 7. Create the GitHub repository

On github.com, create a new repository named `event-card`. **Do not check the box
that adds a README, a `.gitignore`, or a license.** You already have those, and
letting GitHub create its own gives you two histories that have never met, which
produces an error message that is well beyond Week 1.

**Observable result:** GitHub shows you an empty repository page with setup
instructions and a URL ending in `.git`.

### Step 8. Connect your repository to it

```
git remote add origin <the URL GitHub showed you>
git remote -v
```

**Observable result:** `git remote -v` prints two lines, both containing your URL,
one marked `(fetch)` and one marked `(push)`.

### Step 9. Push

```
git push -u origin main
```

**Observable result:** Git reports the branch was set up to track the remote.
Refresh the GitHub page. Your two commits are there, with your messages.

### Step 10. Write the README

Create `README.md`. Assume the reader is a stranger, because at a CTAG review or a
BPA interview that is exactly who it is. Answer four questions in this order:

1. What is this. One or two sentences naming the *thing*, not the assignment.
2. How do I run it. The exact command, and what has to be installed.
3. What does it look like when it works. Show the real output.
4. What did you decide or learn. This part is yours.

**Observable result:** The file exists and contains all four sections.

### Step 11. Commit and push the README

```
git add README.md
git commit -m "<why this README exists, in your words>"
git push
```

Note that this push needs no arguments. Step 9's `-u` handled that.

**Observable result:** GitHub renders your README on the repository front page.

### Step 12. Read your own repository as a stranger

Open your GitHub page. Read only what is on the screen. Ask yourself: if I had
never met me, could I run this.

**Observable result:** A written answer, three sentences, added to the bottom of
your README under a heading called `Notes`. If you found something missing, fix it,
commit, and push again. That third commit is worth more than the first two.

---

## Acceptance criteria, full lab

- [ ] Your repository is visible at a GitHub URL and contains three or more commits
- [ ] `.gitignore` is the first commit in the history
- [ ] `scratch.txt` exists in your folder and does **not** appear on GitHub
- [ ] `python event_card.py` produces five lines, the fourth blank, no traceback
- [ ] Every comment in `event_card.py` describes your choices, not the starter's
- [ ] `README.md` names the program in its first sentence, not the assignment
- [ ] `README.md` contains the exact command that runs the program
- [ ] `README.md` shows the real output
- [ ] Nothing in the repository is a password, key, token, or anything personal
- [ ] Every commit message completes the sentence "This commit will..."

---

## If it breaks

These are the four you are most likely to hit, with the message you will actually
see.

### 1. A quote is missing

```
  File "C:\...\event_card.py", line 2
    print("Thursday, September 17, at 3:15 pm)
          ^
SyntaxError: unterminated string literal (detected at line 2)
```

**Cause:** the text on that line was opened with a quote and never closed. Note
that **nothing printed at all**, not even line 1. Python reads the whole file before
running any of it, and this file never made it past reading. Look at the caret, not
at the line you think is wrong.

### 2. You ran a file that is not there

```
C:\Python313\python.exe: can't open file 'C:\...\event_cart.py': [Errno 2] No such file or directory
```

**Cause:** one of two things, and both are common. You typed the filename wrong
(`event_cart` instead of `event_card`), or your terminal is not in the folder that
holds the file. Read the path in the message. It tells you exactly where Python
looked.

### 3. You committed and nothing was committed

```
On branch main

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        event_card.py

nothing added to commit but untracked files present (use "git add" to track)
```

**Cause:** you saved the file but never ran `git add`. Saving puts changes on the
disk, and Git is not watching the disk. Nothing turned red and no error appeared,
which is why this one gets past people. The fix is on the last line of Git's own
output.

### 4. You pushed with no remote connected

```
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
```

**Cause:** you skipped step 8, or you ran it in a different folder. Run
`git remote -v`. If it prints nothing, there is no remote here.

### Not an error: the CRLF warning

```
warning: in the working copy of 'event_card.py', LF will be replaced by CRLF the next time Git touches it
```

Windows ends lines with two characters and macOS and Linux use one. Git is telling
you it is converting between them. It says `warning`, not `error`, nothing is
broken, and you will see it on most `git add` commands in this lab. Keep going.

---

## Stretch goal

Produce byte-for-byte identical output using exactly **one** `print` call.

You will need `\n`, which is a single character meaning "new line," written with two
keystrokes. Two of them in a row make a blank line.

Then answer this in your README, in two sentences: which version would you rather
open in six months, and why. There is a defensible answer on both sides, and the
reasoning is what earns the credit.

---

## Submission checklist

Before you say you are done:

- [ ] `git status` prints nothing under changes to be committed
- [ ] `git log --oneline` shows three or more commits, `.gitignore` first
- [ ] The GitHub page shows the same commits as your local `git log`
- [ ] `scratch.txt` is on your machine and is not on GitHub
- [ ] Your README renders correctly on GitHub, with no broken formatting
- [ ] You have read your own README as though you had never met yourself
- [ ] Your AI usage log has an entry if you used a model at any point, including
      for a commit message or the README wording
- [ ] The repository URL is submitted

---

# Extended Lab Options

All four versions assess the same competency and are graded on the same 100-point
scale using the five-dimension standard in the instructor key. The difference is
scope and support, not rigor.

## Which version to hand a student

Three signals you can see while circulating, before anyone asks for help:

| What you observe | Hand them |
|---|---|
| Still on step 1 or 2 at the 12-minute mark, or the terminal is in the wrong folder and they have not noticed | SCAFFOLDED |
| Working steadily, occasional questions about wording rather than mechanics | STANDARD |
| Finished Part 1 inside 20 minutes and is editing their README unprompted, or asked what `-u` does | EXTENDED |
| Asked, out loud or in body language, "when would I ever use this" | APPLIED |

Do not announce the versions to the room. Hand them out individually.

---

## SCAFFOLDED

**For a student who is behind.** Same target: a pushed repository with a clean
history and a usable README.

**Changed sections:**

- **Starter code:** the file is provided complete except for TODO 1 and TODO 4.
  Three of the five lines are already written. The student edits one line and adds
  one line.
- **Steps:** Part 1 is split into eight smaller steps, and after steps 2, 4, and 6
  the student runs `git status` and writes down what it says before continuing.
  That written trail is the checkpoint.
- **Scope:** the stretch goal is removed. The README is reduced to sections 1 and 2
  only, what it is and how to run it.
- **Checkpoints:** the student shows you the terminal after step 4 and after step 9.
  Two check-ins, not one.

**Acceptance criteria for this version:**

1. Repository is on GitHub with at least two commits
2. `.gitignore` is the first commit
3. `python event_card.py` runs with no traceback and prints at least four lines
4. README names the program in its first sentence and gives the run command

**Grading:** same 100-point scale. Documentation is scored on sections 1 and 2 being
correct and useful rather than on four sections existing. A student who does this
version completely earns the same grade as a student who does STANDARD completely.
The scope is smaller, the standard is not.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

**For a student who finished Part 1 early.** Everything in STANDARD, plus one
genuine addition that uses something not taught.

**Added requirement.** Your event card currently prints the same thing forever. Make
it print today's date on its own line, calculated when the program runs rather than
typed in by you.

**Hint, not the answer.** Python ships with a module named `datetime`. Read the
first section of the standard library page for it at
`https://docs.python.org/3/library/datetime.html` and look specifically for `date`
and for a method named `today`. You will need one line to bring the module in and
one line to print. Getting the output format the way you want it is a second
problem, and there is a method for that too. Do not search for a complete solution.
Read the page.

**Second added requirement.** In your README, add a section called `What I did not
understand` describing the part of the `datetime` documentation that did not make
sense, and what you tried in order to work it out. Written honestly, this is worth
more than the working code.

**Acceptance criteria for this version:** all STANDARD criteria, plus the program
prints an accurate current date computed at run time, plus the README section
exists and names something specific.

**Grading:** same 100-point scale. The `datetime` work is scored under Requirements
Fit and Correctness. A student who attempts it and fails, and documents the attempt
accurately in the README, loses very little. A student who pastes working code they
cannot explain fails the course standard on explanation.

---

## APPLIED

**For the student who asked when they would use this.** Same skill, different
domain, and the answer is that the domain does not matter.

**Changed scenario.** You are not writing a program. You are documenting a physical
process. Pick something you actually do that has a sequence and that other people
get wrong: closing a shift at your job, tearing down and packing a robotics kit,
the pre-flight check on a 3D print, resetting the equipment room.

**What you build.** A repository containing only `README.md` and `.gitignore`. The
README is a real procedure somebody else could follow with no prior knowledge, with
numbered steps and a section listing what goes wrong and what to do about it.

**Then the part that makes it the same lab.** Do it in at least four commits, each
one a meaningful stage of writing, each with a message explaining why that change
was made. Then deliberately write something wrong into the procedure, commit it,
notice it, and fix it in a following commit. Your history now contains a mistake and
its correction, which is what real project history looks like.

**Acceptance criteria for this version:**

1. Repository on GitHub, `.gitignore` committed first
2. At least four commits with messages that state why
3. The history visibly contains a mistake and a later correction
4. The procedure is specific enough that a stranger could follow it
5. A section naming at least three things that go wrong and what to do

**Grading:** same 100-point scale. Correctness is judged on whether the procedure
actually works. Requirements Fit is judged on the commit history telling a story.
The point being made, and it should be made out loud to this student: version
control is not a programming tool. It is a tool for anything where the history of a
document matters, and lawyers, writers, and mechanical engineers use it for exactly
that reason.
