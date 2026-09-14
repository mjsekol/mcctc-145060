# The Fork in the Road
---
## Slide 1: Your tool makes the reader do the thinking
- Your CLI Toolsmith prints a number
- Then it prints: above 100 means out of reach
- The person has to check that themselves
- The program already knows the number
Speaker notes: Look at the last two lines of most of your CLI Toolsmith output. You print a number, and then you print a sentence telling the reader how to judge it. That sentence is a confession. It says my program cannot make a decision, so you make it. Every program you have written so far is a straight line. Today it gets a fork in the road.
Image: A straight road that splits into two paths at a signpost, deep navy and accent blue, flat and diagrammatic.
---
## Slide 2: A comparison is a question
```python
score = 7
print(score > 5)
print(score == 10)
print(score <= 7)
print(score >= 8)
print(type(score > 5))
```
Speaker notes: Predict all five lines before I run this. Each comparison asks a yes or no question about two values, and Python answers it with True or False. The last line matters most. The answer has a type, and the type is bool. You met bool in Week 2 and had nothing to do with it. Now it is the most important type in the unit.
Image: None. This slide is code.
---
## Slide 3: What came back
```
True
False
True
False
<class 'bool'>
```
Speaker notes: Five answers, and every one is either True or False. Capital T, capital F, no quotes. Double equals asks whether two things are the same. Less than or equal and greater than or equal include the boundary, so 7 is less than or equal to 7. There is also a not-equal operator, and it is in your notes. Hold on to that word boundary, because it is where most of the bugs in this unit live.
Image: None. This slide is code.
---
## Slide 4: One equals assigns, two equals asks
- score = 7 stores 7 in score
- score == 7 asks whether score is 7
- An if needs a question, not an order
- Say it with me until it is automatic
Speaker notes: Here is the rule and I am going to say it the same way every time. One equals assigns. Two equals asks. In math class the single equals sign was a question you checked. In Python it is an order. Your hands are going to type one equals sign for about three weeks after your head knows better, so let me show you what happens when they do.
Image: Two labeled symbols side by side, a single equals marked store and a double equals marked ask.
---
## Slide 5: The wrong way
```python
score = 7
if score = 7:
    print("yes")
```
```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```
Speaker notes: I typed one equals sign inside an if, which is the most common mistake anybody makes today. Python refuses to run the file and look at the message. It names the fix. Maybe you meant double equals. Ignore the colon equals part, that operator exists and it is not in this course. Read the last line of every error. Python is often telling you the answer.
Image: None. This slide is code.
---
## Slide 6: if and else
```python
battery = int(input("Battery percent: "))

if battery < 20:
    print("Plug in your phone before practice.")
    print("It will not survive the bus ride home.")
else:
    print("You are fine for now.")

print("Battery check done.")
```
Speaker notes: Read it as English. If battery is less than 20, do the indented lines. Otherwise do the other indented line. The colon says a block starts here. The indentation says which lines are inside it. The last line is not indented, so it runs every time no matter which path we took. I am going to run this three times, with 12, with 64, and with exactly 20. Predict the third one.
Image: None. This slide is code.
---
## Slide 7: Indentation is meaning
- Indented lines belong to the if or else
- The first unindented line runs every time
- Four spaces, which Tab gives you in VS Code
- Move one line and the program changes
Speaker notes: At exactly 20 percent the program said you are fine, because 20 is not less than 20. That is a boundary decision, and you make it by choosing less than or less than or equal. Now watch what indentation does. If I add four spaces in front of battery check done, it moves inside the else, and it only prints when the battery is fine. No error. Python did exactly what the spaces said.
Image: The battery program with the if block and else block shaded in two different blues and the final line outside both.
---
## Slide 8: Nine beats ten
```python
my_score = input("Your score: ")
best_score = input("Best score so far: ")

if my_score > best_score:
    print("New high score.")
else:
    print("Not this time.")
```
```
Your score: 9
Best score so far: 10
New high score.
```
Speaker notes: No error. Nine beat ten. Both values came from input, so both are text, and text compares one character at a time like a dictionary. The first character of nine is 9, the first character of ten is 1, and 9 comes after 1, so Python stops there. Here is the part to remember. If I compared text to a number, Python would crash. Text to text is allowed, so it quietly gives a wrong answer.
Image: None. This slide is code.
---
## Slide 9: Fourth time, same shape
- Week 2: twelve times three gave 121212
- Week 2 Gate 2: two and a half people accepted
- Week 3: a year sliced down to 202
- Today: nine beats ten
- None of them crashed
Speaker notes: Stop and look at the list rather than the examples. Four times now a program has run, printed something that looks like an answer, and been wrong. The dangerous bugs are the ones that do not crash. The fix today is the Week 2 habit. Convert with int at the moment you ask. And clean text before you compare it, because Yes with a capital Y is not equal to yes.
Image: Four small terminal snippets stacked, each with a wrong value circled in accent blue and no error text anywhere.
---
## Slide 10: What you are about to build
- Build 2: finish your CLI Toolsmith
- Add at least one condition that judges your output
- Replace a sentence telling the reader to check something
- Test the exact boundary value, not only numbers far away
Speaker notes: Build 1 is the Unit 1 quiz. In Build 2 you finish the CLI Toolsmith, and it gets smarter. Find a line in your output that tells a human to judge a number, and replace it with a condition that judges the number itself. If the target is above 100, say it is out of reach. Then run it with the exact boundary value. If your condition flips at 100, run it with 100. That one run is the difference between a condition you wrote and a condition you tested.
Image: A terminal showing a tool output line that reads out of reach, with the old instruction sentence crossed out, navy and accent blue.
---
