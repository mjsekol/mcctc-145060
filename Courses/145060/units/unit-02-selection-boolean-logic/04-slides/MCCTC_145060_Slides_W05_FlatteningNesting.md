# Flatten the Pyramid
---
## Slide 1: Which if does this else belong to
- Your code has drifted to the right edge
- An else sits nine lines below its if
- You changed one rule last week
- Now the wrong person gets the message
Speaker notes: You have probably already written an if inside an if inside an if. It works. Then you come back a week later to change one rule, and you cannot tell which else belongs to which if without counting spaces. Today is not new syntax. Today is a judgment call. When should a decision be nested, and when should you flatten it. It is the hardest lesson of the week because the answer depends on the shape of the problem.
Image: Code indentation drawn as a staircase pyramid drifting to the right, flat navy and accent blue.
---
## Slide 2: The pyramid
```python
if on_team:
    if has_slip:
        if fee_paid or has_waiver:
            if gpa >= 2.0:
                print("You are on the bus.")
            else:
                print("You need a 2.0 GPA to travel.")
        else:
            print("Pay the fee or ask about a waiver.")
    else:
        print("Get your permission slip signed.")
else:
    print("This trip is for team members.")
```
Speaker notes: The robotics team road trip. Four requirements, each with its own message. This code is correct. Now, without counting spaces, tell me which if the permission slip message belongs to. Its else is nine lines below its if. The happy path is buried in the middle four levels deep. This shape has a nickname, the pyramid, and it is correct right up until somebody edits it.
Image: None. This slide is code.
---
## Slide 3: Same rules, flattened
```python
if not on_team:
    print("This trip is for team members.")
elif not has_slip:
    print("Get your permission slip signed.")
elif not (fee_paid or has_waiver):
    print("Pay the fee or ask about a waiver.")
elif gpa < 2.0:
    print("You need a 2.0 GPA to travel.")
else:
    print("You are on the bus.")
```
Speaker notes: Turn it inside out. Check every reason to say no, one at a time, and say yes last. Every rule now sits right next to its message. Adding a fifth rule is one elif. I ran both versions on all 48 combinations of answers and they printed the same thing every time. That is the standard for a refactor. Same inputs, same outputs, every row of the truth table.
Image: None. This slide is code.
---
## Slide 4: When you only need yes or no
```python
can_travel = on_team and has_slip and (fee_paid or has_waiver) and gpa >= 2.0
print("Can travel:", can_travel)

age = 15
print(13 <= age <= 19)
```
Speaker notes: If nobody needs a separate message for each rule, the whole pyramid is one compound condition. The parentheses around the or are not decoration. Without them a student who is not on the team but has a fee waiver gets on the bus. The bottom line is a Python shortcut. Thirteen less than or equal to age less than or equal to nineteen means age is at least 13 and age is at most 19.
Image: None. This slide is code.
---
## Slide 5: Nesting that is correct
```python
if weather == "rain":
    has_ride = input("Can someone drive you? (y/n): ").strip().lower() == "y"
    if has_ride:
        print("Movie theater.")
    else:
        print("Board games at home.")
else:
    friends_free = input("Are your friends free? (y/n): ").strip().lower() == "y"
    if friends_free:
        print("Meet at the park.")
    else:
        print("Shoot hoops in the driveway.")
```
Speaker notes: Flat is not always better. Here the question you ask next depends on the answer you got a moment ago. On a rainy day we never ask whether your friends are free. On a clear day we never ask about a ride. That shape is a decision tree, and nesting is the honest way to write it. Your Decision Engine is built from exactly this shape.
Image: None. This slide is code.
---
## Slide 6: The decision rule
- Inner if with no else: combine with and
- Each level has its own no message: elif chain
- Next question depends on this answer: keep nesting
- Deeper than three levels: stop and look again
Speaker notes: Here is the rule, in order. If an inner if has no else, it only adds a requirement, so join it with and. If every level is a requirement with its own failure message, flatten to an elif chain with the no answers first. If the next question depends on the answer to this one, keep the nesting, because that is a tree. And if you are more than three levels deep, it is almost always one of the first two cases wearing a disguise.
Image: A four-row flowchart legend with a small icon for each case, navy and accent blue.
---
## Slide 7: The wrong way, and no error
```python
if on_team:
    if has_slip:
        print("You are on the bus.")
else:
    print("Get your permission slip signed.")
```
```
On the robotics team? (y/n): n
Permission slip signed? (y/n): y
Get your permission slip signed.
```
Speaker notes: No error. Someone who is not on the team and already has a slip is told to get a slip. And a team member without a slip gets no message at all, only silence. The else lines up with if on team, so it belongs to on team. The author meant it for the inner if and was off by four spaces. Python did exactly what the indentation said. The flat elif version cannot have this bug.
Image: None. This slide is code.
---
## Slide 8: Eighth time, same shape
- 121212, 2.5 people, 202
- Nine beats ten, a 95 earns a D
- Monday is the weekend, practice in the rain
- Today: the wrong person gets the message
- The flat version makes this bug impossible
Speaker notes: Eight appearances now. Every one of them ran without a single error. Here is what is different about today. For the first time, the fix is not a better test. It is a better shape. When every message sits on the same level as its own rule, there is no else that can drift to the wrong if. Sometimes the best defense against a silent bug is writing code where that bug has nowhere to hide.
Image: Eight small terminal snippets in a grid, each with a wrong value circled in accent blue.
---
## Slide 9: The one that crashes
```python
age = 16
if age >= 16:
    print("Old enough.")
        print("Book the test.")
```
```
IndentationError: unexpected indent
```
Speaker notes: Indentation has to mean something. Four extra spaces that do not start a new block are an error, and Python stops before running anything. This is the friendly version of today's bug. The unfriendly version is the one on the last slide, where the spaces were legal and wrong.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: Decision Engine, keep building
- Apply the decision rule to your own nesting
- Build 2: run every decision table row against your engine
- Tomorrow: Gate 2 review of AI code
Speaker notes: Build 1 is your Decision Engine. Before you add anything, look at every place you nested. For each one, name which of the four cases it is. If your nesting is a tree, keep it and say so in a comment. If it is a pyramid of requirements, flatten it and prove the outputs did not change. Build 2 is still your engine. Run it once for every row of your decision table, typing exactly what the row says, and mark each row match or no match. Fix a mismatch, run the row again, and commit. Tomorrow is Gate 2. An AI wrote a program that checks whether someone is eligible for something. It is well formatted and confident, and one of its five defects sits exactly on a boundary.
Image: A code review checklist on a clipboard beside a terminal, navy and accent blue.
---
