# Every Possible Answer
---
## Slide 1: Practice in the rain
- The coach wants a cancel-practice program
- Practice only happens when it is warm and dry
- A student simplified the condition
- The team practiced outside in a thunderstorm
Speaker notes: A coach asked for a tiny program. Cancel practice unless it is warm and dry. A student wrote it, then tidied it up to make it simpler, and the simpler version sent the team outside in the rain. The student tested it on a cold rainy day and it worked. Today you learn the tool that would have caught it in two minutes, and it fits on an index card.
Image: A sports field under rain clouds with a clipboard reading practice on, flat navy and accent blue.
---
## Slide 2: A table of every situation
- One column per input
- One row per combination of True and False
- Every input doubles the number of rows
- Two inputs, 4 rows. Three inputs, 8 rows
Speaker notes: A truth table lists every situation a condition can face and the answer in each one. Remember the eight light switches from last week that made 256 arrangements. Same counting. Every input you add doubles the rows. And here is the part that matters for your projects. Every row is a test case. If your program is right on every row, you have tested every combination that exists.
Image: A grid with two input columns and four rows, the rows labeled 11, 10, 01, 00 in small binary digits.
---
## Slide 3: The three basic tables
```
A      B      | A and B | A or B
True   True   | True    | True
True   False  | False   | True
False  True   | False   | True
False  False  | False   | False

A      | not A
True   | False
False  | True
```
Speaker notes: Three tables to know cold. And is True in exactly one row, the row where both are True. Or is False in exactly one row, the row where both are False. Not flips. Fill the input columns by counting down in binary, true true, true false, false true, false false, and you will never skip a row.
Image: None. This slide is code.
---
## Slide 4: Checking a row in Python
```python
print(True and not True)
print(True and not False)
print(False and not True)
print(False and not False)
```
```
False
True
False
False
```
Speaker notes: Here is A and not B. Each print is one row with the values typed in. You build the table on paper first, with a helper column for not B, and then you check each row here. The WebXam will ask you to build the table without a computer, so the paper is the skill and Python is the answer key.
Image: None. This slide is code.
---
## Slide 5: Cancel practice, the honest version
```python
is_warm = True
is_dry = False

cancel_practice = not (is_warm and is_dry)
print("Cancel practice:", cancel_practice)
```
```
Cancel practice: True
```
Speaker notes: Warm and raining. Practice happens only when warm and dry is True, so we cancel when it is not. The not goes around the whole parenthesized condition. This is right. Now watch the student tidy it up by pushing the not inside the parentheses, which looks like the algebra you learned in eighth grade.
Image: None. This slide is code.
---
## Slide 6: The wrong way, and no error
```python
cancel_practice = not is_warm and not is_dry
print("Cancel practice:", cancel_practice)
```
```
Cancel practice: False
```
Speaker notes: No error. False. The team practices in the rain. This version only cancels when it is cold and wet at the same time. The student tested a cold rainy day and got the right answer, so they believed it. Seventh time now. The code ran, it printed an answer, and it was wrong. Let us build the table and find every row where it is wrong.
Image: None. This slide is code.
---
## Slide 7: The table finds it
```
W      D      | not (W and D) | not W and not D | not W or not D
True   True   | False         | False           | False
True   False  | True          | False           | True
False  True   | True          | False           | True
False  False  | True          | True            | True
```
Speaker notes: Three conditions side by side. The first is the honest one. The second is the student's version, and it is wrong in two of the four rows, warm and wet, and cold and dry. The third column matches the first in every row. When two columns match in every row, the conditions mean the same thing, and when a single row differs, they do not.
Image: None. This slide is code.
---
## Slide 8: When not moves inside, the operator flips
- not (W and D) equals not W or not D
- not (W or D) equals not W and not D
- This is called De Morgan's law
- Prove any rewrite with a table
Speaker notes: Here is the rule. When you push not inside parentheses, and becomes or, and or becomes and. It has a name, De Morgan's law, and you do not need the name. You need the habit. Any time you rewrite a condition to make it simpler, build a table of the old version and the new version side by side before you trust it.
Image: Two columns of the table with matching rows connected by accent blue lines.
---
## Slide 9: Lowercase true is not a thing
```python
print(true and false)
```
```
NameError: name 'true' is not defined. Did you mean: 'True'?
```
Speaker notes: One mistake that does crash. On paper you might write T and F, or true and false in lowercase. In Python, True and False have capital letters. Lowercase true is a name nobody defined, and Python even suggests the fix. Read the suggestion, then check it, because a suggestion is a spelling match and not an understanding of what you meant.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: four truth tables by hand, then checked
- The last one compares two conditions
- Build 2: Decision Engine, your decision table
- Every row of it becomes a test case
Speaker notes: Build 1 is paper. Four tables, with helper columns, and then you check every row in Python. The last table compares two conditions and you decide whether they are the same. Build 2 is your Decision Engine. Take the rules you wrote as sentences yesterday and turn them into a table of inputs and the category each combination should get. That table is your test plan for next week, so every row you skip is a test you never run.
Image: A hand-drawn table on graph paper next to a laptop terminal showing True and False lines.
---
