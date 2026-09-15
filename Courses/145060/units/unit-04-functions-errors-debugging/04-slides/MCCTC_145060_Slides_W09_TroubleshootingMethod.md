# Stop Guessing: The Six-Step Troubleshooting Method
---
## Slide 1: It does not work
- A friend texts you: my game does not work
- Which input? What should happen? What happened instead?
- You cannot fix a bug you cannot make happen
- Most people start changing things anyway
- Twenty minutes later, four things are different
Speaker notes: This week you take your text adventure apart and rebuild it out of functions. Things will break. That is not a warning, it is a schedule. When something breaks, most people change whatever looks suspicious and run it again, then change something else. Programmers call that shotgun debugging. Today you get a method that replaces hope with a procedure, and a log that proves you used it.
Image: A phone screen with a text message reading my game does not work, flat navy and accent blue.
---
## Slide 2: Steps 1 to 3: find the cause
- 1. Identify: make the bug happen again on purpose
- Write the input, the expected result, the actual result
- 2. Theory: one specific guess that could be wrong
- 3. Test: an experiment that could prove it wrong
- Theory wrong? Back to step 2 with a new one
Speaker notes: The first three steps find the cause. Step one is a reproduction, the exact input that makes the bug happen, plus what you expected and what you got. Step two is a theory, and it has to be specific enough to be wrong. Something is wrong with the function is not a theory. Step three is a small experiment that could prove the theory wrong. If it does, that is progress. You learned where the bug is not.
Image: Three numbered stepping stones labeled identify, theory, and test.
---
## Slide 3: Steps 4 to 6: fix it and prove it
- 4. Fix: the smallest change. Change one thing
- 5. Verify: rerun the reproduction
- Also rerun the cases that already worked
- 6. Document: write the log entry
- No fix before a tested theory
Speaker notes: Steps four to six fix it and prove it. Change one thing, the smallest thing that fixes the cause. Then verify, which means running the reproduction again and also the cases that were already working, because fixes break their neighbors. Then write it down. The one rule that separates this from guessing is on the last line. No fix before a tested theory.
Image: Three more stepping stones labeled fix, verify, and document, continuing the path.
---
## Slide 4: A bug that does not crash
```python
def is_weekend(day):
    """Return True if the day is Saturday or Sunday."""
    return day == "saturday" or "sunday"


def alarm_for(day):
    """Return the alarm time for this day."""
    if is_weekend(day):
        return WEEKEND_ALARM
    return SCHOOL_ALARM
```
```
Day: monday
Set your alarm for 9:30.
```
Speaker notes: Here is a real bug. You type monday and it tells you to set your alarm for nine thirty. No error. You are late for school and nothing warned you. Step one is already done on this slide. The input is monday, the expected result is six fifteen, and the actual result is nine thirty. Before we touch anything, what is your theory?
Image: None. This slide is code.
---
## Slide 5: Testing two theories
```python
# Theory 1: the day has a capital letter.
day = input("Day: ").strip().lower()
print(repr(day))

# Theory 2: is_weekend returns something true for every day.
print(is_weekend("monday"))
print(is_weekend("saturday"))
```
```
Day: Monday
'monday'
sunday
True
```
Speaker notes: Theory one, the day has a capital letter. Test it by printing repr of day. It prints monday in lowercase, so theory one is wrong, and that rules out the whole input. Theory two, the function returns something true for every day. Test it by calling the function by itself. For monday it returns the word sunday. Not True, not False, a word. Python reads it as day equals saturday, or the text sunday, and any non-empty text counts as true. That is the Unit 2 bug hiding inside a function.
Image: None. This slide is code.
---
## Slide 6: Watch this: I skip to the fix
```python
def is_weekend(day):
    """Return True if the day is Saturday or Sunday."""
    return day.lower() == "saturday" and day.lower() == "sunday"
```
Speaker notes: Now watch what happens when I skip steps two and three. I see or, I remember and exists, and I also add lower in case capitals are the problem. Two changes at once. I run it with monday and it says six fifteen. Fixed, right? Before I run it with saturday, predict what it will say.
Image: None. This slide is code.
---
## Slide 7: The wrong way: Saturday breaks, silently
```
Day: monday
Set your alarm for 6:15.
Day: saturday
Set your alarm for 6:15.
```
Speaker notes: Monday looks fixed. Saturday is now broken, and so is Sunday, because no day can be saturday and sunday at the same time. The function returns False for everything. There is no error message. I only tested the day that was reported, so I find out at six fifteen on Saturday morning. And I changed two things, so I cannot even tell which one did it. Changing two things at once destroys the evidence.
Image: None. This slide is code.
---
## Slide 8: Reading a traceback, bottom up
```
Rider age: 15
Traceback (most recent call last):
  File "...", line 15, in <module>
    print("Fare: $" + fare_for(age))
          ~~~~~~~~~~^~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "float") to str
```
Speaker notes: When the bug does crash, step one hands you evidence. Read a traceback from the bottom up. The last line says what went wrong, a TypeError, text plus a float. The lines above say where, line fifteen, at the plus sign. Be careful with that second part. The traceback tells you where Python noticed. The cause can be somewhere else, like inside a function that returned the wrong thing. Today's lab has exactly that.
Image: None. This slide is code.
---
## Slide 9: The log entry
- Reproduction: input, expected, actual, crash or silent
- Every theory, including the ones that were wrong
- Each test and its real output
- The fix: the line before and after
- Verify: the reproduction plus cases that already worked
Speaker notes: Step six is the log entry, and the template is in the project folder. Keep the wrong theories in it. They save the next person from wasting time on capital letters. Paste real output, not what you think it printed. And the verify section needs cases on both sides of your fix. Your version two needs at least two entries from real bugs you hit this week, and at least one of them has to be a bug that did not crash.
Image: A single page log form with six labeled sections, navy headings on white.
---
## Slide 10: What you are about to build
- Build 1: Lab U4-01, a practice report that crashes
- Find three bugs. Log each one with all six steps
- Two of the three bugs do not crash
- Build 2: your v2 plan. Baseline, failure list, function map
- Log every bug you hit this week
Speaker notes: Build one is a practice report a friend wrote. It crashes, and when you fix the crash you will find two more bugs that do not crash at all. Log every one with all six steps. Build two starts version two of your text adventure. You save what version one prints today, list everything that could go wrong, and plan your functions before you change a line. Any bug you hit this week goes in your log.
Image: A practice log printout with three circled numbers beside a notebook open to a troubleshooting log.
---
