# How Code Actually Runs
---
## Slide 1: You have never seen where software lives
- You have used apps for twelve years
- You have never seen one as a file
- Today that gap closes
- Three things are involved, not one
Speaker notes: Put your hand up if you have opened an app today. Keep it up if you could tell me, right now, where that app is on the disk. Nobody can, and that is not a knowledge gap you should feel bad about. It is a gap nobody ever showed you. By the end of this block you will have written a file, found it on the disk, and run it on purpose. Three separate things are involved every time software runs, and once you can name all three, error messages stop being noise.
Image: A simple three-box diagram, unlabeled, with an arrow from box one to box two to box three. Deep navy boxes, accent blue arrows.
---
## Slide 2: The three things
- The file: text on a disk, does nothing
- The interpreter: the program named python
- The terminal: where you hand one over
- A recipe is not a cook
Speaker notes: Here they are. The file is a document. It has no more power to act than a note on your fridge. The interpreter is a program already installed on this machine, and its entire job is to read a document like that and carry it out, line by line, top to bottom. The terminal is where you hand the recipe to the cook. Say that back to me. A recipe is not a cook. You are going to write recipes. Python does the cooking.
Image: The same three boxes, now labeled file, interpreter, terminal, with a small document icon and a gear.
---
## Slide 3: Our first file
```python
# status_card.py
# Prints a short status card to the terminal.

print("MCCTC Programming 145060")
print("Name: Ava Ruiz")
print("Day 1 goal: run one file I wrote myself")
print()
print("Battery on my phone right now: 41 percent")
```
Speaker notes: This is the entire program. Eight lines, two of which do nothing at all. I am going to type it in front of you and I want you to watch what I do before I run it, because that step is where half of you will get stuck this week. I write it. Then I save it. Then I run it. If I skip the save, the machine reads the old version and I will swear the computer is broken.
Image: None. This slide is code.
---
## Slide 4: Running it
```
python status_card.py
```
```
MCCTC Programming 145060
Name: Ava Ruiz
Day 1 goal: run one file I wrote myself

Battery on my phone right now: 41 percent
```
Speaker notes: One command. The word python is the cook. The word after it is the recipe I am handing over. Look at the output and find three things nobody typed. There is a blank line in the middle. There are no quote marks anywhere, even though the file is full of them. And the lines came out in the order I wrote them, which nothing in the file asked for. Top to bottom is the only order there is.
Image: None. This slide is code.
---
## Slide 5: Three things nobody typed
- Blank line came from print with empty parentheses
- Quotes told Python where text starts and stops
- Order came from the file, nothing else
- Lines starting with hash produced nothing at all
Speaker notes: Take these one at a time. The empty print printed nothing and then ended the line, and an ended line with nothing on it is a blank line. The quotes are punctuation for Python, not for you, so they never come out. The two lines starting with a hash are comments. Python reads them and moves straight past. You write those for the next person who opens this file, which is usually you, three weeks from now, with no memory of what you were doing.
Image: The output block with three callout arrows pointing at the blank line, a missing quote position, and a comment line.
---
## Slide 6: Now I break it on purpose
```python
print("MCCTC Programming 145060")
print("Name: Ava Ruiz)
print("done")
```
Speaker notes: I am going to take the closing quote off line two and run it. Do not tell me what happens. I want you to look at the error with me, because reading error messages is the actual skill this week, more than anything about Python. Watch the screen.
Image: None. This slide is code.
---
## Slide 7: The error, read in four steps
```
  File "C:\...\status_card.py", line 2
    print("Name: Ava Ruiz)
          ^
SyntaxError: unterminated string literal (detected at line 2)
```
Speaker notes: Four questions, in this order, every time. What file. What line. What is the caret sitting under. What kind of error. This message answers all four and most of you skipped past it looking for the word wrong. Notice something else. Nothing printed. Not even line one, which was perfectly fine. That tells you something specific and we are about to say what.
Image: None. This slide is code.
---
## Slide 8: Two kinds of broken
- SyntaxError: found while reading, nothing printed
- NameError: found while running, output came first
- Got output before the crash? Problem is below it
- The caret points. Trust it over your reading
Speaker notes: This table is a debugging shortcut you will use all year. If your program printed nothing before it died, Python could not understand the file and never started it. If your program printed six lines and then died, the file was fine as Python and the trouble is at line seven or later. That single distinction cuts your search in half before you read any code. And when the caret points at a character, believe the caret. You cannot proofread your own work, because your eye supplies what you meant to type.
Image: Two-column comparison, navy headers, one column per error type.
---
## Slide 9: Where the line number lies to you
- Error said line 2, line 3 also stopped working
- Python reports where it noticed, not where you erred
- Read the named line, then read upward
Speaker notes: Here is the trap inside the trap. The missing quote is on line two, so line two is where Python noticed. But because that text never ended, Python kept reading forward and swallowed line three into it. Line three stopped being code without ever being mentioned. About half the time in this course, the fix is one or two lines above the line the error names. Read the named line first, then walk upward.
Image: The three-line broken file with a bracket spanning lines 2 and 3.
---
## Slide 10: What you are about to build
- Install Python, Git, and VS Code, verified
- Write status_card.py yourself, not copied
- Five lines of output, one of them blank
- Point at the line that made any output line
Speaker notes: Two blocks. First we get the tools installed and proven working, and that will be the loudest thirty-five minutes of the week, which is fine. Then you write your own status card from scratch. Not copied off this board, typed. Five lines of output, one of them blank, and one line that says something true about your day that the person next to you could check. The bar for done is this: I point at any line of your output and you point at the line in your file that made it.
Image: A split panel, terminal on the left showing a version check, editor on the right showing a short file.
---

