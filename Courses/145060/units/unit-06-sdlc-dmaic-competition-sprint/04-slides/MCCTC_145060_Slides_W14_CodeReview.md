# Two Kinds of Review
---
## Slide 1: Your tests only check what you thought of
- Every check in your file came from your head
- The defect you never imagined has no check
- You cannot see your own blind spot
- Today, somebody else looks
Speaker notes: Welcome back. Your test file checks what your team thought to check, and nobody thinks of everything. That is not a flaw in you. It is what being the author means. Your eyes slide right past your own assumptions because they are yours. This afternoon another team reads your code and you read theirs. Before that, you learn the two kinds of review and exactly what each one misses.
Image: A single flashlight beam lighting part of a dark code listing, leaving the rest in shadow, navy and blue.
---
## Slide 2: People and programs miss different things
- Peer walkthrough: people read it with the author
- People understand purpose, and get tired
- Static analysis: a program reads it, never runs it
- Programs are fast, and have no idea of purpose
Speaker notes: There are two kinds of code review. In a peer walkthrough, people read the code while the author explains it, requirement by requirement. People are slow and they get tired, but they know what the code is for. Static analysis is a program reading your code without running it, looking for patterns that are usually mistakes. It is fast and tireless and has no idea what the code is for. You need both.
Image: Two icons side by side, a group of people at a screen and a gear scanning a document, with a small Venn overlap.
---
## Slide 3: The check that ships with Python
```
$ python -m py_compile door.py
  File "door.py", line 2
    if door_open
                ^
SyntaxError: expected ':'

$ python -m py_compile greet.py
$ python greet.py
Good morning
```
Speaker notes: Python ships with a static check you can run right now. py compile asks one question. Can Python read this file at all. door dot py is missing a colon, so it fails. greet dot py prints nothing, which means it passed. It runs and says good morning. But greet has a misspelled variable on a line that only runs in the afternoon. py compile cannot see that. It only checks that the file can be read.
Image: None. This slide is code.
---
## Slide 4: Build a checker in eight lines
```python
import ast
import sys

with open(sys.argv[1], encoding="utf-8") as file:
    tree = ast.parse(file.read())

for node in ast.walk(tree):
    if isinstance(node, ast.ExceptHandler):
        if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            print(f"line {node.lineno}: this except block hides the failure")
```
Speaker notes: This is a real static analysis tool and you can read every line of it. ast parse reads the file the same way Python does before running it and hands back a tree, the whole program as nested pieces. ast walk visits every piece. For each one we ask, is this an except block, and is its whole body the word pass. If so, that block makes failures disappear, and we print the line. The file being checked is never run. It is only read.
Image: None. This slide is code.
---
## Slide 5: The full checker on a peer's code
```
Static review of cart_checkout.py
------------------------------------------------------------
line 19   Security     'RESET_PIN' looks like a secret written into the code
line 44   Correctness  bare except catches every error, including your own typos
line 44   Correctness  except block only says pass, so the failure disappears silently
line 48   Readability  function 'chk' has no docstring
line 48   Readability  one-letter name 'c'
line 48   Readability  one-letter name 'n'
line 82   Performance  open() inside a loop reads or writes the file on every pass
------------------------------------------------------------
7 finding(s)
Not checked by this tool: Requirements Fit, and whether the logic is right.
```
Speaker notes: review check dot py is the same idea with six checks, each tied to a review dimension. Here it is on the laptop cart program from your lab. Seven findings in under a second, across four dimensions. Now read the last line out loud with me. Not checked by this tool, requirements fit, and whether the logic is right. It cannot check requirements, because the requirements are not in the file.
Image: None. This slide is output.
---
## Slide 6: Tools are wrong in both directions
- False alarm: shopping_list flagged as a secret
- Because shopping contains the letters p, i, n
- A person dismisses it in two seconds
- Silent miss: a clean report on broken code
Speaker notes: Static tools make mistakes both ways. A false alarm: the checker flags a variable named shopping list as a possible secret, because the word shopping contains p i n. You look at it for two seconds and dismiss it. That kind of mistake is cheap. The other direction is the dangerous one, and I am going to show you.
Image: Two warning lights, one lit with a small green check beside it, one dark with a red question mark beside it.
---
## Slide 7: Watch this
```
$ python review_check.py concessions.py
Static review of concessions.py
------------------------------------------------------------
------------------------------------------------------------
0 finding(s)
Not checked by this tool: Requirements Fit, and whether the logic is right.
```
Speaker notes: This is concessions dot py from Lab U06-01 on Thursday. Zero findings. Before I say anything, what did your tests find in this file on Thursday.
Image: None. This slide is output.
---
## Slide 8: Zero findings, three real defects
- Refuses a legal order of 20 hot dogs
- Ignores sports drinks when counting combos
- Applies the member discount in the wrong order
- Every defect is about purpose. Tools cannot see purpose.
Speaker notes: Three real defects, the ones your acceptance tests caught. Zero findings from the checker. No error, no warning, a clean report on broken code. The wrong move is the conclusion, zero findings so it is clean. It is the same shape as a test that agrees with the bug. A tool says fine and a person stops looking. So the protocol order is tools first, then the walkthrough anyway.
Image: A clean checklist with three red markers hidden underneath the page edge, navy and blue.
---
## Slide 9: A finding has four parts
- Where: function and line number
- Dimension: one of the five
- Consequence: what goes wrong for a real person
- Fix: what to change
- Review the code, never the coder
Speaker notes: When you find something this afternoon, write it with four parts. Where, the function and the line. Which dimension. The consequence for a real person, not the word inefficient. And the fix. And one rule above everything. Review the code, never the coder. If your sentence would still make sense with the author's name in it, rewrite it.
Image: A four-column finding table with where, dimension, consequence, and fix headers, navy header row.
---
## Slide 10: What you are about to build
- Build 1: Lab U06-03, a structured review of practice code
- Run both tools, then walk through by requirement
- Find what the checker could not
- Build 2: Peer Code Review 1, on another team's Sprint 1
Speaker notes: Build one is Lab U06-03. You review the laptop cart program using the full protocol. Run py compile and the checker, then walk through it requirement by requirement and find what the checker could not. There are several. Build two is the real thing. Peer Code Review one, on another team's Sprint 1 code, while another team reviews yours. Authors, your only word during the review is noted. You respond in writing tomorrow.
Image: A scoring form with five dimension rows and a findings table beneath, navy and blue.
---
