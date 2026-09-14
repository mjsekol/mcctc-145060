# Lab U2-01: Ticket Pricing
## 145060 Programming · Unit 2 · Week 5

**Gate:** 3 (open tooling). **Duration:** two Build 1 blocks, Monday and Tuesday.
**Competencies:** 5.3.5 (conditional control structures), 5.3.4 (relational operators
and compound conditions), 5.3.3 (logical operators), 5.4.7 (debug logic errors).

---

## The scenario

Your cousin works the ticket window at a small movie theater. The price depends on the
customer's age, the day of the week, and whether they show a student ID, and the rules
live on a laminated card taped next to the register. On a busy Friday night the line
is out the door and people get charged the wrong price, which means refunds, arguments,
and a manager who is not happy.

## What you will build

A program that asks three questions and prints exactly one correct ticket price, even
at the boundary ages where people misread the laminated card most often.

---

## The laminated card

These are the rules. Everything you build comes from this card.

| Rule | Price |
|---|---|
| Under 3 | Free, as a lap child, every day |
| Tuesday | $6.00 for everyone 3 and older |
| 3 through 12 | Child, $7.50 |
| 65 and older | Senior, $8.00 |
| 13 through 64 with a student ID | Student, $9.00 |
| 13 through 64 without a student ID | Adult, $11.00 |
| Friday or Saturday | Adult and Student tickets cost $1.00 more |
| Any age below 0 or above 120 | Refuse it and ask again |

**Reminder line.** If the customer is 13 through 22, has no student ID, and it is not
Tuesday, print a reminder that a student ID saves $2.00.

---

## Starter code

Create `ticket_pricing.py` and type this in. It runs. It does nothing useful.

```python
# ticket_pricing.py
# Prices one movie ticket from the customer's age, the day, and a student ID.
#
# This file runs right now. It does not do anything useful yet.

print("TICKET WINDOW")
print("-------------")

age_text = input("Age: ")

# TODO 1 (Part 1): Convert the age to a whole number at the moment you ask.

# TODO 2 (Part 1): Choose the ticket type and price with one if/elif/else chain.
#   Under 3: free.  3 to 12: Child $7.50.  65 and up: Senior $8.00.
#   Everyone else: Adult $11.00.

# TODO 3 (Part 2): Ask for the day and whether they have a student ID.

# TODO 4 (Part 2): Add the Tuesday price, the student price, and the
#   Friday and Saturday surcharge.

# TODO 5 (Part 2): Refuse an age that cannot be real, and print the
#   student ID reminder.

print("No ticket priced yet.")
```

Running it and typing `16` produces:

```
TICKET WINDOW
-------------
Age: 16
No ticket priced yet.
```

---

## Part 1: Monday, steps 1 through 6

### Step 1. Starter running and committed
Create it, run it, commit it.
**Observable result:** four lines of output, and a new commit in `git log --oneline`.

### Step 2. Convert at the moment you ask
Replace the `age_text` line so the age is converted with `int()` on the same line as
`input()`. Delete TODO 1.

**Observable result:** the program still runs. If you type `16`, nothing new prints yet.

### Step 3. Write the age chain
Replace TODO 2 with one `if`/`elif`/`else` chain that sets two variables,
`ticket_type` and `price`, using the four age rules only. Then replace the last
`print` with one that shows both, with the price to two decimal places.

**Observable result:** typing `16` prints `Ticket: Adult      $11.00` or something with
the same information.

### Step 4. Test every boundary
Run the program six times with these ages: `2`, `3`, `12`, `13`, `64`, `65`. Write each
result in a comment block at the bottom of your file.

**Observable result:** six results. `2` is free, `3` and `12` are Child, `13` and `64`
are Adult, `65` is Senior. If any one is wrong, your cutoff uses `<` where it needed
`<=` or the other way around. Fix it before step 5.

### Step 5. Break the order on purpose
Copy your file to `ticket_wrong_order.py`. In the copy, replace the `else` at the end
of your chain with an explicit adult condition, `elif age >= 13:`, and **place it above
the senior check**. Run the copy with age `70`.

**Observable result:** a 70-year-old is charged the Adult price, and **there is no error
message**. Write what it printed, and one sentence explaining why, in your README under
`What I learned`. Do not fix the copy. It is evidence.

### Step 6. Commit
**Observable result:** `git log --oneline` shows at least two commits. Your original
`ticket_pricing.py` still prices a 70-year-old as a Senior.

### Acceptance criteria, Part 1
1. `python ticket_pricing.py` runs with no traceback for all six boundary ages
2. All six boundary ages produce the price on the laminated card
3. `ticket_wrong_order.py` exists and your README records what age 70 paid

---

## Part 2: Tuesday, steps 7 through 12

### Step 7. Ask the other two questions
Replace TODO 3. Ask for the day, cleaned with `.strip().lower()`. Ask whether the
customer has a student ID, and store the answer as a `bool` in one line:

```python
has_student_id = input("Student ID? (y/n): ").strip().lower() == "y"
```

**Observable result:** add a temporary `print(has_student_id)`. Typing `Y` prints `True`
and typing `n` prints `False`. Then delete the temporary print.

### Step 8. Tuesday and the student price
Add the Tuesday rule and the Student rule to your chain. **Decide where each one goes
before you type it.** A lap child is free even on Tuesday. A 70-year-old on Tuesday pays
$6.00.

**Observable result:** age `2` on `tuesday` is free. Age `30` on `Tuesday` pays $6.00.
Age `16` on `monday` with an ID pays $9.00.

### Step 9. The weekend surcharge
After the chain, add a condition that adds $1.00 when the ticket is Adult or Student
**and** the day is Friday or Saturday. Store the surcharge amount in a named variable,
not a bare `1.00` in the middle of a condition.

**Observable result:** age `16` on `Friday` with an ID pays $10.00. Age `12` on `friday`
still pays $7.50. Age `40` on `monday` still pays $11.00.

### Step 10. Refuse impossible ages
Add a check, **first** in your chain, that catches an age below 0 or above 120 and prints
a message instead of a ticket.

**Observable result:** ages `-4` and `121` print your refusal message and no price. Ages
`0` and `120` are still priced.

### Step 11. The reminder line
Replace TODO 5's reminder with one condition using `and` and `not`.

**Observable result:** age `13` on `friday` with no ID prints the reminder. Age `23` on
`monday` with no ID does not. Age `13` on `tuesday` with no ID does not.

### Step 12. README and push
Four sections: what it is, how to run it, a table of at least ten test runs with the
inputs and the price, and `Known limitations`. Push.

---

## Acceptance criteria, full lab

- [ ] The age is converted with `int()` on the same line as `input()`
- [ ] One `if`/`elif`/`else` chain chooses the ticket type, so exactly one type is chosen
- [ ] All six Part 1 boundary ages price correctly
- [ ] `ticket_wrong_order.py` shows a senior charged the Adult price, recorded in README
- [ ] The day is cleaned before it is compared
- [ ] Tuesday, Student, and lap-child rules interact correctly (step 8 results)
- [ ] The weekend surcharge uses `or` for the days, `and` for the ticket types, and a named amount
- [ ] Ages below 0 and above 120 are refused; 0 and 120 are priced
- [ ] The reminder uses `not` and appears only in the step 11 cases
- [ ] README test table has at least ten runs
- [ ] Three or more commits with messages saying why
- [ ] Pushed

---

## If it breaks

### 1. A word typed where the age goes

```
ValueError: invalid literal for int() with base 10: 'sixteen'
```

**Cause:** `int()` cannot convert text that does not spell a whole number. Handling this
properly is Unit 4. For now, write it in `Known limitations`. The EXTENDED option below
shows one way to refuse it.

### 2. Comparing the age as text

```
TypeError: '<' not supported between instances of 'str' and 'int'
```

**Cause:** the age came from `input()` and was never converted. It is still a `str`, and
Python refuses to decide whether text is smaller than a number. Wrap `int()` around
`input()` on the same line.

### 3. The price variable does not exist

```
NameError: name 'price' is not defined. Did you mean: 'print'?
```

**Cause:** one branch of your chain prints a message but never sets `price`, and a later
line uses `price` anyway. Every branch has to set every variable you use after the chain.
Ignore the suggestion to use `print`. Python matched the spelling, not your intent.

### 4. Every day gets the weekend surcharge, and nothing crashes

A 30-year-old on Monday pays $12.00.

**Cause:** you wrote `day == "friday" or "saturday"`. The right side of `or` is the string
`"saturday"` on its own, not a comparison, and a non-empty string counts as True. Each
side of `or` needs its own complete comparison: `day == "friday" or day == "saturday"`.

### 5. Tuesday pricing never happens, and nothing crashes

**Cause:** the customer typed `Tuesday` and you compared it to `"tuesday"` without
`.lower()`. Clean first, compare second.

---

## Stretch goal

A family of four walks up together. Change nothing about your chain, and answer this in
your README instead: what would it take for your program to price all four tickets and
print a total? Name the thing you do not know how to do yet. You will learn it in Unit 3.

---

## Submission checklist

- [ ] Runs with no traceback for every age in your test table
- [ ] Tested at ages 2, 3, 12, 13, 22, 23, 64, 65, and one impossible age
- [ ] Tested on a Tuesday, a Friday, and a Monday
- [ ] `ticket_wrong_order.py` committed and explained
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 15 minutes on Monday, no chain written yet, or they are writing separate `if` statements for each band | SCAFFOLDED |
| Chain written, testing boundaries, asking about the rules rather than the syntax | STANDARD |
| Finished Part 1 with all six boundaries tested in under 20 minutes, or asked what happens when somebody types a word | EXTENDED |
| Said nobody they know works at a movie theater, or asked when they would ever price anything | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the Part 1 chain is provided with the conditions blank. The student fills
  in four conditions and four prices.

```python
if ____:
    ticket_type = "Lap child"
    price = 0.00
elif ____:
    ticket_type = "Child"
    price = 7.50
elif ____:
    ticket_type = "Senior"
    price = 8.00
else:
    ticket_type = "Adult"
    price = 11.00
```

- **Steps:** Part 2 drops step 9, the weekend surcharge, and step 11, the reminder line.
- **Step 5 stays.** The wrong-order copy is the point of Monday. Do not cut it.
- **Checkpoints:** show your instructor the terminal after step 4 and after step 8.
- **README:** test table of six runs instead of ten.

**Acceptance criteria:** runs; six boundary ages correct; wrong-order copy recorded;
Tuesday and Student rules correct; impossible ages refused.

**Grading:** same 100-point scale, Requirements Fit judged against this list. A student
who completes SCAFFOLDED fully earns what a student completing STANDARD fully earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not yet taught.

**Added requirement.** Right now, typing `sixteen` crashes the program. Make the program
refuse anything that is not a whole number of digits, and print the same refusal message
as an impossible age, **without crashing and without `try`**.

**Hint, not the answer.** Strings carry methods that answer yes-or-no questions about
their own characters. Read the string methods section of the Python documentation,
`https://docs.python.org/3/library/stdtypes.html#string-methods`, and look for methods
whose names start with `is`. Two of them sound almost identical. Read what each one
counts as a digit before you pick one.

**Second added requirement.** In your README, list three inputs you tried that you
expected might get past your check, and what actually happened with each. Include an
empty input, where the person presses Enter without typing.

**The honest warning.** One of those two similar methods says yes to some characters that
`int()` still refuses. If you picked that one, a strange enough input still crashes your
program. Finding which characters those are, and documenting it, earns more than avoiding
it by luck.

**Acceptance criteria:** all STANDARD criteria; `sixteen`, an empty input, and `-5` are all
refused without a traceback; README lists three tested inputs with real results.

---

## APPLIED

**For the student who says they will never price a movie ticket.** Same skills, and the
theater was never the point.

**Changed scenario.** You mow lawns on weekends. The price depends on the size of the yard,
whether it is a weekend, and whether the customer is a neighbor on your street. Write your
own laminated card first. It must have:

- At least four size bands with different prices, in square feet or in a size word you
  define
- One day-based rule that overrides the size price, like Tuesday does in the standard lab
- One yes-or-no discount stored as a `bool`
- One surcharge that needs both `and` and `or`
- A refusal for a yard size that cannot be real

**What you build.** A program that prices one job from your card, with the same structure
as the standard lab.

**The extra requirement that makes it the same lab.** Your README must include your card
as a table, a test table covering every boundary on your card, and a wrong-order copy that
misprices one band with no error.

**Acceptance criteria:** all STANDARD criteria applied to your own card, plus the card
itself in the README.

**Grading:** same scale. Requirements Fit is judged against the card the student wrote,
which is harder than the standard version because the instructor has to be able to check
every boundary from the README alone.
