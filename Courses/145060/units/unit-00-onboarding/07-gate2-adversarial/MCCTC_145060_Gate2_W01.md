# Gate 2: Adversarial Review · Week 1
## 145060 Programming · Unit 0 · Week 1, Friday

**Gate 2 is the gate where AI is the opponent.** You are not writing this code. You
are reviewing it, and you are scored on what you catch against what you miss.

**35 minutes.** Individual work. You may run the code. You may use the terminal.
You may not ask a model whether the code is correct, because the model is the one
being reviewed.

---

## What you are looking at

A student in another section asked an AI assistant to build a setup helper for this
course. They gave it the requirements below. It produced the three files in Part B.

The code runs. It is formatted well, the comments are confident, and the names are
sensible. **It looks right at a glance.** That is exactly the problem, and it is why
this exercise exists.

**There are exactly five defects, one in each of these categories:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It creates a risk of exposing something that should stay private |
| **Readability** | A name or a comment that misleads the next person to read it |
| **Performance** | Work being done that does not need to be done |
| **Requirements Fit** | Something the spec asked for that is missing, or something invented that nobody asked for |

One of the five is genuinely hard to see. You are expected to miss it. Finding four
is a good score.

---

## PART A: The requirements the code was built from

> Write a program called `setup_check.py` that new students run before their first
> day of hands-on lab work. It should:
>
> 1. Print a checklist of the six setup steps, numbered, in the order they must be
>    done.
> 2. For each step, print the exact command that verifies the step worked.
> 3. Finish with one line telling the reader what to do if any step fails.
> 4. Print a reminder that credentials never go in a repository.
>
> Package it as a small repository with:
>
> 5. A `.gitignore` that keeps a personal scratch file named `scratch.txt` out of
>    the repository permanently.
> 6. A `README.md` giving the exact command to run the program, and step-by-step
>    setup instructions a brand new student could follow without help.

---

## PART B: What the AI produced

### File 1: `setup_check.py`

When you cite a line number, count from the first line of the file below,
`# setup_check.py`, as line 1. Blank lines count.

```python
# setup_check.py
#
# Onboarding helper for new students in 145060 Programming.
# Prints the setup checklist and the exact command that verifies each step.
#
# Written to be run before the first day of hands-on lab work.

# ----- Header -----
# The header block orients the reader before the checklist begins.
print("=========================================")
print("  145060 PROGRAMMING - SETUP CHECKLIST")
print("  Work through all 6 steps in order.")
print("  Do not skip ahead.")
print("=========================================")

# ----- The checklist -----

print("1. Install Python 3.14")
print("   Verify with:  python --version")

print("2. Install Git")
print("   Verify with:  git --version")

print("3. Install VS Code and open this folder in it")
print("   Verify with:  code --version")

print("4. Tell Git who you are")
print("   Verify with:  git config --global user.name")

print("5. Create your GitHub account")
print("   Verify with:  open github.com and sign in")

print("7. Make your first repository")
print("   Verify with:  git status")

# ----- Closing warning -----
# The header block is repeated here so the reader sees it again at the bottom
# without having to scroll back up to the top of the output.
print("=========================================")
print("  145060 PROGRAMMING - SETUP CHECKLIST")
print("  Work through all 6 steps in order.")
print("  Do not skip ahead.")
print("=========================================")

# Print a blank line so the warning stands out from the checklist above.
print(" ")

print("REMINDER: never put a password, API key, or token in a repository.")
```

### File 2: `.gitignore`

```
scratch.txt
```

### File 3: `README.md`

```markdown
# Setup Check

A helper program for new students in 145060 Programming. It prints the setup
checklist and the command that verifies each step.

## Running it

Requires Python 3.14.

    python setup_check.py

## Setting up your repository

Follow these steps in order:

1. Create a folder for the project and open it in VS Code.
2. Save `setup_check.py` and your `scratch.txt` notes file into that folder.
3. Turn the folder into a repository:

        git init -b main

4. Stage everything and make your first commit:

        git add .
        git commit -m "Initial commit"

5. Now create your `.gitignore` file so your scratch notes stay private:

        scratch.txt

6. Commit the `.gitignore`:

        git add .gitignore
        git commit -m "Add gitignore"

7. Push to GitHub:

        git remote add origin <your repository URL>
        git push -u origin main

Your scratch file is now excluded from the repository.
```

---

## What to submit

For each defect you find, write one entry containing all four of these:

1. **File and line.** Be specific. "Somewhere in the README" does not score.
2. **Dimension.** Which of the five categories it belongs to.
3. **What goes wrong.** Not "this is bad." Describe the actual consequence for an
   actual person.
4. **The fix.** One or two lines.

Then add one final entry:

5. **What I was unsure about.** Name at least one thing you suspected and could not
   confirm. This is scored, and leaving it blank costs you more than a wrong guess.

**You may run the code.** You should. Two of the five defects are faster to prove in
a terminal than to find by reading, and one of them is close to invisible on screen.
If you can demonstrate a defect with a command, put the command in your entry.

---

## Scoring

Five defects, one point each. See the scoring sheet in the key for how the security
defect is weighted, and hear the rule from your instructor before you start.

The honest expectation: **four out of five is a strong score for Week 1.** One of
these is designed to get past you.
