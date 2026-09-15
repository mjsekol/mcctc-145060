# Lecture Notes: The Six-Step Troubleshooting Method
## 145060 Programming · Unit 4 · Week 9, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W09_TroubleshootingMethod.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W09_TroubleshootingMethod.pptx)

If you missed class, you can learn this concept from this file alone. You need Week 8's two
function lessons first: [Defining Functions](MCCTC_145060_Notes_DefiningFunctions.md) and
[Return Values and Scope](MCCTC_145060_Notes_ReturnValuesAndScope.md).

**Today is one concept: a named method for finding and fixing a bug, and a written log that proves
you used it.** No new Python. Every program in this file uses tools you already have.

---

## Why this exists

This week you take your text adventure apart and rebuild it out of functions. Things will break.
That is not a warning. It is a schedule.

When a program breaks, most people do the same thing. They change something that looks suspicious
and run it again. Then they change something else. Twenty minutes later the program is still broken,
four things are different, and nobody can say which change did what. That habit has a name among
programmers: **shotgun debugging.** You fire at everything and hope something hits.

A troubleshooting method replaces hope with a procedure. Every step produces something you can write
down, so when you are stuck you know exactly which step you are stuck on.

The syllabus asks you to **select and apply a troubleshooting methodology, then document the problem and
the verified solution.** Outcome 5.4.6 is correcting syntax and runtime errors. Outcome 5.4.7 is debugging
logic errors. This method handles both, and the troubleshooting log is a Unit 4 deliverable.

---

## The concept in plain language

**The Six-Step Troubleshooting Method** is the method this course uses. The same six ideas show up in IT
support work, where technicians troubleshoot hardware and networks, and in programming, where it is often
called scientific debugging. You make a guess you can prove wrong, and then you try to prove it wrong.

| Step | What you do | What you write down |
|---|---|---|
| **1. Identify the problem** | Make the bug happen again on purpose. Read the whole error message. | The exact input, what you expected, and what actually happened |
| **2. Establish a theory** | Make **one** specific guess about the cause | A sentence that could turn out to be false |
| **3. Test the theory** | Run a small experiment that could prove the guess wrong. If it does, go back to step 2 | The experiment and its real output |
| **4. Plan and implement the fix** | Make the smallest change that fixes the cause. Change one thing | The line you changed, before and after |
| **5. Verify** | Run the reproduction from step 1 again, **and** the cases that already worked | The runs and their output |
| **6. Document** | Finish the log entry | The whole entry |

Three rules make the method work:

- **No fix before a tested theory.** Step 4 comes after step 3. That is the entire difference between this and
  shotgun debugging.
- **A theory must be specific enough to be wrong.** "Something is wrong with the function" cannot be tested.
  "`fare_for` returns a number, and `+` cannot join a number to text" can.
- **A theory that turns out wrong is progress.** You learned where the bug is not. Write it down.

---

## Worked example 1: a runtime error

A friend's bus fare program:

```python
# bus_fare.py
# Prints the city bus fare for a rider's age.

def fare_for(age):
    """Return the one-ride fare in dollars for a rider of this age."""
    if age < 6:
        return 0
    if age < 18:
        return 1.25
    if age >= 65:
        return 1.00
    return 2.50

age = int(input("Rider age: "))
print("Fare: $" + fare_for(age))
```

**Step 1. Identify.** Run it and type `15`:

```
Rider age: 15
Traceback (most recent call last):
  File "...", line 15, in <module>
    print("Fare: $" + fare_for(age))
          ~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "float") to str
```

Read a traceback from the **bottom up.** The last line says **what** went wrong. The lines above it say **where**. Here
the crash is on line 15, at the `+`. Record the reproduction: input `15`, expected `Fare: $1.25`, actual `TypeError`.

**Step 2. Theory.** "`fare_for(15)` returns the number `1.25`, and `+` cannot join text to a number."

**Step 3. Test.** Ask the function directly, and ask for the type of what comes back:

```python
print(repr(fare_for(15)))
print(type(fare_for(15)))
```

```
1.25
<class 'float'>
```

The theory survives. The function is fine. The bug is on the line that **uses** its answer. Notice what the traceback did
not tell you: it pointed at line 15 because that is where Python noticed, and in this program that is also where the bug
is. That is not always true. Today's lab has a crash where the traceback points at one line and the cause is inside a function
somewhere else.

**Step 4. Fix.** One line changes. An f-string converts the number and formats it:

```python
print(f"Fare: ${fare_for(age):.2f}")
```

**Step 5. Verify.** The reproduction, plus one age from every branch, because a fix to one path can break another:

```
Rider age: 3
Fare: $0.00
Rider age: 15
Fare: $1.25
Rider age: 30
Fare: $2.50
Rider age: 70
Fare: $1.00
```

Age 3 matters. Before the fix it crashed too, with a slightly different message, `can only concatenate str (not "int") to
str`, because `fare_for(3)` returns the whole number `0`. One cause, two messages.

---

## Worked example 2: a logic error, and a theory that was wrong

Your alarm program:

```python
# alarm.py
# Tells you what time to set your alarm for a given day.

SCHOOL_ALARM = "6:15"
WEEKEND_ALARM = "9:30"


def is_weekend(day):
    """Return True if the day is Saturday or Sunday."""
    return day == "saturday" or "sunday"


def alarm_for(day):
    """Return the alarm time for this day."""
    if is_weekend(day):
        return WEEKEND_ALARM
    return SCHOOL_ALARM


day = input("Day: ").strip().lower()
print(f"Set your alarm for {alarm_for(day)}.")
```

**Step 1. Identify.**

```
Day: monday
Set your alarm for 9:30.
```

No error. Expected `6:15`. This is the most expensive kind of bug: it makes you late for school and says nothing.

**Step 2. Theory 1.** "The day has a capital letter, so it does not match."

**Step 3. Test theory 1.** Print exactly what `day` holds. `repr` shows hidden spaces and capitals:

```python
day = input("Day: ").strip().lower()
print(repr(day))
```

```
Day: Monday
'monday'
```

**Theory 1 is wrong.** The text is clean and lowercase. Write that down, because it rules out everything about the input.

**Step 2 again. Theory 2.** "`is_weekend` returns something true for every day."

**Step 3. Test theory 2.** Call the function by itself, once with a weekday and once with a weekend day:

```python
print(is_weekend("monday"))
print(is_weekend("saturday"))
```

```
sunday
True
```

**Theory 2 survives, and the output is stranger than predicted.** `is_weekend("monday")` did not return `True` or `False`.
It returned the word `sunday`. That is the clue that finishes the job. Python reads the line as
`(day == "saturday") or ("sunday")`. The comparison is `False`, so `or` hands back its right side, the text `"sunday"`, and
any non-empty text counts as true in an `if`. This is the Unit 2 bug `day == "saturday" or "sunday"`, now hiding inside a
function.

**Step 4. Fix.**

```python
    return day == "saturday" or day == "sunday"
```

**Step 5. Verify.** A weekday on each side of the weekend, both weekend days, and the return value itself:

```python
print("friday:  ", alarm_for("friday"))
print("saturday:", alarm_for("saturday"))
print("sunday:  ", alarm_for("sunday"))
print("monday:  ", alarm_for("monday"))
print(is_weekend("monday"), is_weekend("sunday"))
```

```
friday:   6:15
saturday: 9:30
sunday:   9:30
monday:   6:15
False True
```

The last line matters most. A function named `is_weekend` should return `True` or `False`, and now it does.

---

## Worked example 3: the troubleshooting log entry

Step 6 turns the work into a record. This is worked example 2 written up with the course template,
[`MCCTC_145060_Template_TroubleshootingLog.md`](../09-project/MCCTC_145060_Template_TroubleshootingLog.md).

```
## Entry 1 · alarm.py · Monday, November 2

Method: Six-Step Troubleshooting Method

1. Identify the problem
   Reproduction: python alarm.py, then type monday
   Expected:     Set your alarm for 6:15.
   Actual:       Set your alarm for 9:30.   (no error message)
   Crash or silent: silent

2. Theory 1: the typed day has a capital letter or a space, so it never matches.

3. Test of theory 1: printed repr(day) after typing Monday.
   Result: 'monday'. Clean and lowercase. Theory 1 is WRONG.

2. Theory 2: is_weekend returns something true for every day.

3. Test of theory 2: printed is_weekend("monday") and is_weekend("saturday").
   Result: sunday, then True. Theory 2 is RIGHT. The function returns the text
   "sunday" for a weekday, because the right side of or is a bare string.

4. Fix
   Before: return day == "saturday" or "sunday"
   After:  return day == "saturday" or day == "sunday"

5. Verify
   Reproduction again: monday gives 6:15.
   Still working: friday 6:15, saturday 9:30, sunday 9:30.
   is_weekend now returns False and True, not a word.

6. What I learned
   A function whose name asks a yes-or-no question should return True or False.
   Printing what it returns would have found this in one step.
```

Notice what makes this entry useful to somebody else. Anyone can repeat the reproduction. The wrong theory is still in it,
so the next person does not waste time on capital letters. And the verification shows cases on both sides of the fix.

---

## The wrong version: debugging by guessing

Here is the same alarm bug, fixed the way most people fix things the first time. Nothing is reproduced and no theory is
tested. The student sees `or`, remembers that `and` exists, and also adds `.lower()` in case capitals are the problem. Two
changes at once:

```python
def is_weekend(day):
    """Return True if the day is Saturday or Sunday."""
    return day.lower() == "saturday" and day.lower() == "sunday"
```

```
Day: monday
Set your alarm for 6:15.
Day: saturday
Set your alarm for 6:15.
```

Monday looks fixed, so the student moves on. **Saturday is now broken,** and so is Sunday. No day can be both `"saturday"`
and `"sunday"` at once, so the function now returns `False` for everything. There is no error message. The student tested only
the day that was reported, so they will find out on Saturday morning at 6:15.

And if they do notice, they cannot tell which of the two changes caused it. **Changing two things at once destroys the evidence.**

---

## Why guessing is tempting

**It feels faster.** Typing a change feels like progress. Writing "Theory 1" feels like paperwork. For a one-line bug you already
understand, the guess sometimes wins. For the bug you do not understand, it loses every time, and you cannot tell in advance which
kind of bug you have.

**The traceback line looks like the answer.** It tells you where Python noticed the problem. The cause can be somewhere else, such as
inside a function that returned the wrong thing three lines earlier.

**Verifying the reported case feels like enough.** The person said Monday was wrong, Monday is right now, done. Step 5 exists because
fixes break the cases next to them.

---

## When the method feels like too much

It is fair to ask whether a typo needs six written steps. It does not need a written log. It still goes through the steps in your head,
in about four seconds: the message names the line (identify), the name is misspelled (theory), the spelling does not match the definition
(test), fix it, run it (verify). Write a log entry when the bug took you more than a few minutes, when it did not crash, or when somebody
else will run into it too. Your v2 log needs at least two of those.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Troubleshooting method** | A fixed sequence of steps for finding and fixing a problem. This course uses the Six-Step Troubleshooting Method. |
| **Reproduction** | The exact steps and input that make a bug happen again. |
| **Expected and actual** | What should have happened, and what did. A bug report needs both. |
| **Theory** | One specific, testable guess about the cause. Also called a hypothesis. |
| **Test of a theory** | A small experiment whose result could prove the theory wrong. |
| **Verify** | Rerun the reproduction and the cases that already worked, after the fix. |
| **Shotgun debugging** | Changing several things without a theory and hoping one of them works. |
| **Traceback** | Python's error report. The last line says what went wrong. The lines above say where. |
| **Silent bug** | A bug that gives wrong output with no error message. |
| **Troubleshooting log** | The written record of each problem and its verified solution. |
| **Outcomes 5.4.6 and 5.4.7** | The WebXam competencies for correcting syntax and runtime errors and for debugging logic errors. |

---

## Self-check

**Question 1.** A classmate writes this in their log: "Theory: the loop is broken." Why is that not a usable theory, and what would a
usable one look like for a loop that prints 6 days instead of 7?

**Question 2.** Put these in method order, and say which one is missing entirely: *changed `range(1, 7)` to `range(1, 8)`* · *printed each
value of `day` and saw 1 through 6* · *ran the program and counted 6 lines when the plan has 7 days* · *ran it again and counted 7 lines*.

**Question 3.** This crashes. Before you touch the code, write the reproduction and one theory, then say what test would check your theory.

```python
def minutes_left(period_end, now):
    """Return the minutes left in the period."""
    return period_end - now

now = input("Minutes into the block: ")
print(minutes_left(118, now))
```

---

### Answers

**1.** It cannot be proven wrong, because it does not say **what** about the loop is broken, so no experiment can test it. A usable theory
names a cause you can check: "the loop variable stops at 6 because `range` does not include its stop number." That one can be tested by
printing each value the loop variable takes.

**2.** Method order: ran it and counted 6 lines (**1, identify**), printed each value and saw 1 through 6 (**3, test**), changed the range
(**4, fix**), ran it again and counted 7 (**5, verify**). **Step 2 is missing:** no theory was written before the test. Documenting it, step 6,
is also missing. Verify is thin, too: a strong verify also checks that the first day is still Day 1.

**3.** Reproduction: run it and type `40`. Verified output:

```
Minutes into the block: 40
Traceback (most recent call last):
  File "...", line 6, in <module>
    print(minutes_left(118, now))
          ~~~~~~~~~~~~^^^^^^^^^^
  File "...", line 3, in minutes_left
    return period_end - now
           ~~~~~~~~~~~^~~~~
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

A good theory: "`now` is text, because `input()` always returns text, so the subtraction mixes a number and a string." Test: add
`print(repr(now))` before the call. It prints `'40'` with quotes, which confirms it. The fix is `int(input(...))`, and verify is `40` giving `78`
plus `0` and `118`. Notice that this traceback has **two** locations. The bottom one is inside the function, where the crash happened. The one above it
is the call. The cause is on neither line: it is the `input` line above both.
