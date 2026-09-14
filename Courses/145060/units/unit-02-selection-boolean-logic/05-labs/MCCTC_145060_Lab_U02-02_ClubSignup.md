# Lab U2-02: Club Sign-Up Validator
## 145060 Programming · Unit 2 · Week 6

**Gate:** 3 (open tooling). **Duration:** one Build 1 block, Monday, 35 minutes.
**Competencies:** 5.3.7 (selection control structures, case and switch), 5.3.5
(conditional control structures), 5.3.4 (relational operators and compound conditions),
5.3.3 (logical operators).

---

## The scenario

Club sign-up week is a mess. Students write a club name on a paper sheet, and a week later
the advisor discovers that half of them were not eligible: a freshman on the yearbook list,
an esports sign-up with no permission form, somebody who wrote "robotic" for a club that
does not exist. The student council wants a kiosk program at the sign-up table that tells a
student on the spot whether they can join and exactly what is missing.

## What you will build

A program that routes a student to their chosen club with `match`, asks only the questions
that club needs, and prints either an approval or the one specific thing that is missing.

---

## The club rules

| Club | Who can join |
|---|---|
| Art | Any student in grades 9 through 12. No forms. |
| Robotics | Grades 9 through 12, with a signed safety form. |
| Esports (students also call it gaming) | Grades 9 through 12, a GPA of **at least** 2.0, **and** a parent permission form. |
| Yearbook | Grades 10 through 12 only. |
| Anything else | Not a club. Tell the student which clubs exist. |

Any grade below 9 or above 12 is refused before the club is even checked.

---

## Starter code

Create `club_signup.py` and type this in. It runs. It handles Art and nothing else.

```python
# club_signup.py
# Checks whether a student can join the club they picked.
#
# This file runs right now. It handles one club, Art, and nothing else yet.

print("CLUB SIGN-UP")
print("------------")

grade = int(input("Grade level (9-12): "))
club = input("Club: ").strip().lower()

# TODO 1: Refuse any grade outside 9 through 12 before checking the club.

match club:
    case "art":
        # Art Club has no requirements. This case is finished. Use it as a model.
        print("Approved for Art Club. No forms needed.")

    # TODO 2: robotics. Needs a signed safety form.

    # TODO 3: esports, also spelled gaming. Needs a GPA of at least 2.0
    #         AND a parent permission form. Say which one is missing.

    # TODO 4: yearbook. Grades 10 through 12 only.

    # TODO 5: anything else. List the clubs that exist.
```

Typing `10` and `Art`:

```
CLUB SIGN-UP
------------
Grade level (9-12): 10
Club: Art
Approved for Art Club. No forms needed.
```

Typing `10` and `robotics` prints the two prompts and then **nothing**, because no case
matches yet. That silence is TODO 5's job to fix.

---

## Steps

### Step 1. Starter running and committed
**Observable result:** `10` and `Art` prints the approval. `10` and `robotics` prints nothing
after the prompts. Commit.

### Step 2. Robotics
Replace TODO 2 with a `case`. **Inside that case**, ask whether the safety form is signed,
store the answer as a `bool`, and print an approval or the missing form.

**Observable result:** `9`, `robotics`, `y` is approved. `12`, `Robotics`, `n` is told to turn in
the form. The safety question is **never asked** when the club is Art.

### Step 3. Esports and gaming
Replace TODO 3. One `case` must accept both spellings. Inside it, ask for the GPA and the
permission form, then check them with reasons to say no first and the approval last. Store
`2.0` in a named variable.

**Observable result:** GPA `2.0` with permission is approved. GPA `1.99` with permission is told
about the GPA. GPA `3.4` with no permission is told about the form. `gaming` behaves exactly
like `esports`.

### Step 4. Yearbook
Replace TODO 4.

**Observable result:** grade `9` is told to try next year. Grade `10` is approved.

### Step 5. The catch-all
Replace TODO 5 with `case _:` and a message that lists the real clubs.

**Observable result:** `chess` prints the club list.

### Step 6. Test one name that should match nothing, on purpose
Type `robotic`, with no `s`. Then type `Robotics` with a capital R and spaces around it.

**Observable result:** `robotic` reaches the catch-all. `  Robotics  ` is routed to Robotics.
Write both results in a comment at the bottom of your file. **If `robotic` got approved for
anything, you have a capture pattern.** Read If it breaks item 1.

### Step 7. Refuse impossible grades
Replace TODO 1. The grade check must happen before the `match`, and the `match` must not run
at all for a bad grade.

**Observable result:** grade `8` with `art` is refused. Grade `13` with `robotics` is refused
**and is never asked about a safety form.**

### Step 8. Commit and push
Add a README with what it is, how to run it, and a table of at least eight test runs. Push.

---

## Acceptance criteria

- [ ] `match` routes the club; one `case` handles both `esports` and `gaming`
- [ ] Each club asks only the questions that club needs
- [ ] Esports: `2.0` is eligible, `1.99` is not, and the message names what is missing
- [ ] Yearbook refuses grade 9 and approves grades 10 through 12
- [ ] `case _:` lists the real clubs; `robotic` reaches it
- [ ] Club names are cleaned, so `  Robotics  ` works
- [ ] Grades outside 9 through 12 are refused before any club question is asked
- [ ] README test table with at least eight runs
- [ ] Committed and pushed

---

## If it breaks

### 1. A club name without quotes

```
    case robotics:
         ^^^^^^^^
SyntaxError: name capture 'robotics' makes remaining patterns unreachable
```

**Cause:** in a `case`, a bare name is not compared to anything. It **captures** whatever the
club is. Python noticed that this case would catch everything, so the cases under it could never
run. Put the value in quotes: `case "robotics":`. If this were your last case, Python would not
notice, and every unknown club would silently be treated as robotics.

### 2. or instead of the bar

```
    case "esports" or "gaming":
                   ^^
SyntaxError: invalid syntax
```

**Cause:** inside a `case`, "this or that" is written with `|`, not `or`:
`case "esports" | "gaming":`.

### 3. A letter grade typed as a GPA

```
ValueError: could not convert string to float: 'B+'
```

**Cause:** `float()` cannot convert text that does not spell a number. Handling this is Unit 4.
Record it in your README under `Known limitations`.

### 4. Nothing under a case

```
IndentationError: expected an indented block after 'case' statement on line 3
```

**Cause:** a `case` line needs at least one indented line under it, exactly like `if`.

### 5. Capital letters go to the catch-all, and nothing crashes

`Robotics` prints the club list.

**Cause:** the club was not cleaned with `.strip().lower()` before the `match`. A `case`
compares exactly.

---

## Stretch goal

The sign-up table has a line of thirty students. Right now the kiosk handles one student and
then the program ends. Write, in your README, what you would need the program to do to handle
the next student without somebody typing `python club_signup.py` again. Name the idea, not the
code. It arrives Thursday.

---

## Submission checklist

- [ ] Runs with no traceback for every row of your test table
- [ ] Tested every club, both esports spellings, the GPA boundary, grade 9 on yearbook, grade 8 and
      grade 13, and a club that does not exist
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 10 minutes, still on step 2, or writing `if club == "robotics"` inside the `match` | SCAFFOLDED |
| Working through cases in order, testing each one | STANDARD |
| All five cases done in 15 minutes, or asked whether `match` can do more than compare strings | EXTENDED |
| Said nobody uses sign-up sheets anymore, or asked what `match` is for in a real app | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the Robotics case is also provided, complete, as a second model. The student
  writes Esports, Yearbook, and the catch-all.
- **Step 3:** esports needs only the GPA check. The permission form is dropped.
- **Step 7:** dropped. The grade check is provided in the starter.
- **Checkpoint:** show your instructor the terminal after step 5.
- **README:** test table of five runs.

**Acceptance criteria:** runs; both esports spellings; GPA boundary at 2.0 correct; yearbook
boundary correct; `robotic` reaches the catch-all.

**Grading:** same 100-point scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not yet taught.

**Added requirement.** The student council wants the kiosk to accept short typed commands: `clubs`
prints the list, and `join art` or `join yearbook` signs up in one line. Build a second version,
`club_commands.py`, where one `match` handles the whole command.

**Hint, not the answer.** `match` can do much more than compare one string. Read the official
tutorial on structural pattern matching, PEP 636, at `https://peps.python.org/pep-0636/`, and
look for the section on matching a sequence of words. You will also need a string method that
breaks a line of text into separate words. You met it briefly in Week 3.

**The honest warning.** The tutorial shows you how to capture a word into a name, like the word
after `join`. A capture accepts **anything** in that position. Try `join chess` and `join` on its
own, and `join the robotics club`, and write in your README exactly what each one does. The capture
bug from this morning's lesson is waiting inside the feature that makes this version work.

**Acceptance criteria:** all STANDARD criteria in `club_signup.py`, plus `club_commands.py` handling
`clubs`, `join art`, and `join yearbook` for grades 9 and 10, plus a README section recording what
the three strange commands did.

---

## APPLIED

**For the student who asks what `match` is for outside a school.** Same skills, different world.

**Changed scenario.** A phone repair shop wants a help kiosk. The customer types the problem, and
the kiosk says what happens next. Write the shop's rules first. They must include:

- At least four problem types, one of which has two spellings, such as `screen` and `display`
- One problem type that asks a follow-up question only that problem needs, such as the age of the
  phone in months for a battery problem
- One compound condition with `and` or `or` and a boundary, such as a warranty that covers phones
  **12 months old or newer** with no water damage
- A catch-all that lists the problem types
- A refusal for a phone age that cannot be real

**What you build.** `repair_kiosk.py`, with the same structure as the standard lab.

**The extra requirement that makes it the same lab.** Your README must include your rules as a
table and a test table covering every boundary in your rules, plus one input that should match
nothing.

**Acceptance criteria:** all STANDARD criteria applied to your own rules.

**Grading:** same scale. Requirements Fit is judged against the rules the student wrote.
