# The Problem Inside the Problem
---
## Slide 1: How many people are ahead of you?
- You are in the lunch line
- You cannot see the front
- You can only ask the person ahead of you
- They cannot see the front either
- How do you get a number?
Speaker notes: You are somewhere in the lunch line and you want to know how many people are ahead of you. You cannot see the front. You can tap the person ahead of you. That is all. Take thirty seconds with the person next to you and work out a way to get the exact number using only that. Then we will name what you invented.
Image: A side view of a line of simple figures with a question passing forward from person to person, flat navy and accent blue.
---
## Slide 2: Ask a smaller version of the same question
- You ask: how many are ahead of you?
- They ask the person ahead of them
- The person at the front says zero
- Each answer comes back plus one
- You hear three, add one: four
Speaker notes: Here is the version most of you came up with. Everyone asks the person ahead the same question. The question travels forward until it reaches the front, where the answer is obvious. Nobody. Zero. Then the answers travel back, and each person adds one. This is recursion. Solving a problem by solving a smaller copy of the same problem.
Image: Arrows going forward along the line labeled with a question, and arrows coming back labeled 0, 1, 2, 3.
---
## Slide 3: Every recursion has two parts
- Base case: small enough to answer directly
- The person at the front says zero
- Recursive case: ask a smaller question, use the answer
- Ask the person ahead, then add one
- Every question must move toward the base case
Speaker notes: Two parts, every time. The base case is the version so small you answer it without asking anyone. The recursive case asks a smaller version and uses that answer. And the questions must move toward the base case. If each question went further back in the line instead of forward, it would never reach the front.
Image: A two-panel diagram, one panel with a stop sign labeled base case, one with a smaller copy arrow labeled recursive case.
---
## Slide 4: As pseudocode
```
TO FIND people_ahead(position)
    IF position is 1
        ANSWER 0
    OTHERWISE
        ASK people_ahead(position - 1)
        ANSWER that answer plus 1
```
Speaker notes: This is the same kind of pseudocode you wrote for your game. Tomorrow you get def, which is how Python writes TO FIND. Thursday you get return, which is how Python writes ANSWER. That is why today is on paper. The syllabus puts recursion in this unit, and Python needs functions to do it, so today you learn how it works and when to use it, and on Thursday you run it.
Image: None. This slide is code.
---
## Slide 5: The trace table
```
Step  Position  Base case?  What happens
1     5         No          ask people_ahead(4), WAIT
2     4         No          ask people_ahead(3), WAIT
3     3         No          ask people_ahead(2), WAIT
4     2         No          ask people_ahead(1), WAIT
5     1         Yes         answer 0
6     2                     heard 0, answer 1
7     3                     heard 1, answer 2
8     4                     heard 2, answer 3
9     5                     heard 3, answer 4
```
Speaker notes: Questions go down, answers come back up. Look at steps one through four. Four people, each paused in the middle of their own question, waiting. The computer does exactly this. It keeps a stack of paused tasks, one for every question still waiting for an answer. That stack is the key to everything else today.
Image: None. This slide is code.
---
## Slide 6: The wrong way: no base case
```
TO FIND people_ahead(position)
    ASK people_ahead(position - 1)
    ANSWER that answer plus 1
```
```
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```
Speaker notes: I deleted the base case. Trace it. Five asks four, four asks three, one asks zero, zero asks negative one. Nobody ever answers, so nobody finishes, and the stack of paused tasks grows until Python stops it. That error is the real output from a countdown written this way. It printed nine hundred ninety eight lines, from three down to negative nine hundred ninety four, then stopped. You will run it yourself on Thursday. Notice this one crashes. An infinite while loop never does.
Image: None. This slide is code.
---
## Slide 7: When recursion is the right tool
- Data nested inside itself, depth unknown
- Folders that contain folders
- Replies that have replies
- Brackets made of smaller brackets
- The problem really is a smaller copy of itself
Speaker notes: Reach for recursion when the data is nested inside itself and you do not know how deep it goes. The size of a folder is its files plus the size of each folder inside it, which is the same question again, one level down. A loop handles the next item in a line. Recursion handles the items inside this item.
Image: A folder icon containing smaller folder icons containing smaller folder icons.
---
## Slide 8: When it is the wrong tool: your game loop
- Take a turn, then ask for the next turn
- Every turn waits for the next turn to finish
- 1,500 turns means 1,500 paused tasks
- Python stops at about 1,000
- A while loop has no stack. Turn 5,000 costs nothing extra
Speaker notes: This is the example to remember. Somebody learns recursion this week and writes the game as take a turn, then take the next turn by calling the same thing again. It reads beautifully. Look at the trace table. Every turn is paused, waiting for the next turn. Python allows about a thousand paused calls by default and then stops with a RecursionError. A player who explores long enough crashes your game by playing it. A while loop repeats in place. Use loops for repetition. Use recursion for nesting.
Image: A tall teetering stack of turn cards next to a single circular loop arrow.
---
## Slide 9: Loop or recursion
- Until the player quits: loop
- Seven times: loop
- Every character or line: loop
- Every file in nested folders: recursion
- Anything a loop does cleanly, recursion does worse
Speaker notes: Here is the honest summary. Anything recursion can do, a loop can also do, sometimes with a lot more bookkeeping. Anything a loop does cleanly, recursion does worse. Professional programmers use recursion for nested data and loops for everything else, and they argue about the cases in between. Know the two ends cold, and on the quiz you will be asked to explain why your game loop is a while.
Image: A two-column sort with four items on the loop side and one on the recursion side.
---
## Slide 10: What you are about to build
- Build 1: three trace tables on paper, 15 minutes
- Then run your v1 win and lose scripts
- Build 2: finish text adventure v1
- README, known limitations, final commit and push
- Due at the end of today's block
Speaker notes: Build one starts on paper. Three trace tables from the lecture notes self check, fifteen minutes, then put them away and run your test scripts one more time. Build two is the finish. Your README needs every required section, including known limitations that you actually observed. Your last commit must be pushed before the end of the block, because that is the deadline. Anything you have not pushed does not exist.
Image: A checklist with README, test scripts, and push checked off, navy and accent blue.
---
