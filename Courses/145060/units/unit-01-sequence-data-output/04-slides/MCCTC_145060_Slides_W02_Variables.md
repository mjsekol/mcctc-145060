# A Name Tied to a Value
---
## Slide 1: Every program you wrote says the same thing forever
- Your event card prints one event
- Change the time and you edit the code
- Only you can do that
- That is a poster, not a program
Speaker notes: Look at what you built last week. It prints the same five lines every single time it runs. If the meeting moves, you open the file and retype it. Nobody else can use it, because using it means editing it. That is a poster with extra steps. Today it becomes a program, and the thing that makes the difference has one job: letting you refer to a value instead of typing it.
Image: A printed poster pinned to a wall next to a small terminal window, contrasted.
---
## Slide 2: A tag, not a box
- A value sits somewhere in memory
- A name is a tag tied to it
- Equals ties the tag
- Say "gets", never "equals"
Speaker notes: Most people are taught that a variable is a box that holds a value. Do not learn it that way, because it breaks in Unit 5 and you will have to unlearn it. A value sits somewhere, and a name is a tag tied to it. And from today, when you read an equals sign out loud, say gets. Hours gets twelve. That one word choice prevents more confusion than anything else I will tell you this week.
Image: A luggage tag on a string tied to an object, deep navy, diagrammatic.
---
## Slide 3: One direction, one time
```python
hours_worked = 12
pay_rate = 11
total_pay = hours_worked * pay_rate
```
Speaker notes: The rule is two steps and it never varies. Work out everything on the right side first. Then attach the name on the left to that result. Right side, then name. In algebra, equals is a claim that reads both directions and is either true or false. Here it is an instruction that goes one way and happens once, at the moment Python reaches that line.
Image: None. This slide is code.
---
## Slide 4: The line that stops everyone
```python
count = count + 1
```
Speaker notes: In algebra this is false for every number there is. In Python it is an instruction. Take whatever count is currently tied to, add one, and tie count to the new result. Read it with the word gets and it stops being strange. Count gets count plus one. You will write this line hundreds of times before January.
Image: None. This slide is code.
---
## Slide 5: Predict this before I run it
```python
shifts = 3
hours_each = 5
total_hours = shifts * hours_each
shifts = 6
print("Total hours:", total_hours)
```
Speaker notes: Write your answer down before I press enter. Everybody commit to a number. I am going to take three answers out loud and then we run it.
Image: None. This slide is code.
---
## Slide 6: Fifteen, not thirty
- Line three ran once, when Python reached it
- It used the values that existed at that moment
- Changing shifts later changes nothing
- Nothing is watching anything
Speaker notes: Most of you said thirty and the reason is a good one. You have used a spreadsheet. In a spreadsheet a cell with a formula in it recalculates when its inputs change. That is a genuinely useful feature and Python does not have it. A line runs once, when it is reached, and then it is finished. If you want the new number, you run the calculation again.
Image: A spreadsheet cell with a formula next to a single line of code, with the recalculation arrow crossed out on the code side.
---
## Slide 7: Now I break it on purpose
```python
hours_worked = 12
print("Hours:", hours_wroked)
```
```
NameError: name 'hours_wroked' is not defined. Did you mean: 'hours_worked'?
```
Speaker notes: This is the most common mistake you will make this week. Read the message the way we practiced last week. What file, what line, what is under the carets. Then notice the last part. Python offered you the fix. It compared the name it could not find against names that do exist and picked the closest one. That is spelling, not understanding, so trust it enough to look and not enough to paste.
Image: None. This slide is code.
---
## Slide 8: Same error, opposite problem
- Spelled wrong: you get a suggestion
- Used too early: you get no suggestion
- Python runs top to bottom
- A name below the line that uses it does not exist yet
Speaker notes: There are two ways to get a NameError and they need different fixes. If the name is misspelled, Python finds a near match and suggests it. If the name is spelled perfectly but you used it above the line that creates it, there is nothing to suggest, because the name it is looking for is the name it cannot find. So when you see this error, ask two questions in order. Is it spelled the same everywhere. Is the line that creates it above the line that uses it.
Image: Two error messages side by side, one with a suggestion line highlighted and one without.
---
## Slide 9: The name is part of the grade
- x is legal and worth nothing
- hours_worked tells the next person what it holds
- The next person is you in three weeks
- Lowercase words joined by underscores
Speaker notes: Python will accept x as a name. This course will not give you full marks for it. Readability is one of the five dimensions on every rubric in this program, and naming is most of it at this stage. The convention we use is lowercase words joined with underscores. Write the name for the person who opens this file in three weeks with no memory of what you were doing, because that person is you.
Image: Two code snippets side by side, one with single letters and one with descriptive names.
---
## Slide 10: What you are about to build
- A calculator for something you actually want to know
- Four variables minimum, readable names
- Two values calculated from other values
- Then lab U1-01, steps one through six
Speaker notes: Build one first: pick something you genuinely want the answer to. Hours until a deadline, cost per person for something you are planning, points you need on the final. At least four named values and two calculations built from them. The bar is that I point at any number in your output and you point at the line that made it. Then you start the lab, which is Part 1 only. Part 2 needs tomorrow.
Image: A terminal showing a short labeled calculation output, navy and accent blue.
---
