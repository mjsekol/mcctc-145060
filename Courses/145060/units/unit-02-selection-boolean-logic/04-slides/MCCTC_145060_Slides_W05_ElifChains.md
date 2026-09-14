# More Than Two Roads
---
## Slide 1: A 95 should not be a D
- You got a 95 on the test
- The grade portal says D
- Nothing crashed. No error anywhere
- Somebody wrote every condition correctly
Speaker notes: Imagine opening the grade portal and seeing a D next to a 95. You would be in the office in ten minutes. Here is the uncomfortable part. The person who wrote that portal did not write a single wrong condition. Every rule in their code is true. By the end of today you will be able to write that bug, see why it happens, and never ship it.
Image: A grade portal card showing a score of 95 next to a letter D, flat navy and accent blue interface style.
---
## Slide 2: One decision, many outcomes
```python
score = int(input("Test score: "))

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Score {score}: letter grade {letter}")
```
Speaker notes: Thursday you had two roads. Most decisions have more than two. elif means else if, and it adds another condition to the same decision. I am going to run this with 95, 90, 89, and 59. Watch 90 and 89 in particular, because those two numbers sit on either side of the A boundary.
Image: None. This slide is code.
---
## Slide 3: First True wins
- Python checks conditions from the top down
- It runs the first True block
- Then it skips the rest of the chain
- Exactly one block runs. Never two
Speaker notes: Here is the rule for the whole day. Python walks down the chain and stops at the first condition that is True. Trace 89 with me. Is 89 at least 90? No. Is 89 at least 80? Yes. Letter becomes B, and Python never even asks whether 89 is at least 70. Now the question that matters. Is 95 at least 60? Also yes. So why did 95 get an A?
Image: A vertical ladder of four conditions with an arrow stopping at the first green rung and the remaining rungs greyed out.
---
## Slide 4: Same conditions, different order
```python
if score >= 60:
    letter = "D"
elif score >= 70:
    letter = "C"
elif score >= 80:
    letter = "B"
elif score >= 90:
    letter = "A"
else:
    letter = "F"
```
Speaker notes: I am going to keep every condition exactly as it was and only change the order. This is the order a lot of people think of grades in, bottom up. Every line on this slide is a true statement about the grading scale. Predict what 95 gets.
Image: None. This slide is code.
---
## Slide 5: The wrong way, and no error
```
Test score: 95
Score 95: letter grade D
Test score: 72
Score 72: letter grade D
```
Speaker notes: No error. A 95 is a D. Python asked whether 95 is at least 60, it is, so letter became D and the rest of the chain was skipped. The A line is still in the file and no score can ever reach it. That is called unreachable code. And notice this. If you tested with 45 and 65, you got F and D, both correct, and you would have called it done.
Image: None. This slide is code.
---
## Slide 6: The ordering rule
- Ask: can one value make two conditions True
- If yes, the most specific condition goes first
- With greater-than chains, start at the highest cutoff
- With less-than chains, start at the lowest cutoff
Speaker notes: Before you run any chain, ask one question. Could a single value make two of these conditions True? For grade bands the answer is always yes, because a 95 is at least 90 and at least 60. When the answer is yes, the narrowest band has to come first. If your conditions use greater than or equal, start at the top. If they use less than, start at the bottom. Either works as long as it is consistent.
Image: Two number lines, one read from the top down with greater-than cutoffs and one read from the bottom up with less-than cutoffs.
---
## Slide 7: Separate ifs are separate decisions
```python
if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
if score >= 60:
    print("D")
else:
    print("F")
```
```
Test score: 95
A
B
C
D
```
Speaker notes: Here is the other way this goes wrong. Four separate if statements are four separate decisions, and each one checks its own condition no matter what happened above it. A 95 passes all four and you get four letters. elif is the word that ties conditions together into one decision. If you want one outcome, you need one chain.
Image: None. This slide is code.
---
## Slide 8: Mistakes that do crash
- else if and elseif are not Python
- elif after else is invalid syntax
- else never takes a condition
- Read the last line of the error
Speaker notes: A few mistakes do crash, which is the good news. People coming from other languages type else if or elseif, and Python says expected colon or invalid syntax. Putting an elif after else fails, because else ends the chain. And putting a condition on else fails, because else catches everything left over. If you need a condition, that is what elif is for.
Image: Three short terminal error lines in a stacked list, each ending in SyntaxError, navy background.
---
## Slide 9: Five times now
- 121212 from a missing conversion
- Two and a half people accepted
- A year sliced to 202
- Nine beating ten
- A 95 that earns a D
Speaker notes: Same shape, fifth appearance. The program ran, printed something shaped like an answer, and was wrong. What the five have in common is that testing with one ordinary value would not have caught any of them. So here is the testing rule for every chain you write this unit. One value from every band, plus the exact boundary numbers. For grades that is 90 and 89, 80 and 79, and so on.
Image: Five small terminal snippets stacked, each wrong value circled in accent blue, no error text anywhere.
---
## Slide 10: What you are about to build
- Build 1: Lab U02-01 Ticket Pricing, Part 1
- Price a movie ticket by age band
- Step 5 puts your bands in the wrong order
- Build 2: Decision Engine opens. No code yet
Speaker notes: Build 1 is the ticket pricing lab, part one. You price a movie ticket by age, which is a chain with four bands, and step five tells you to break the order on purpose and record what a senior pays. Do not skip that step. Then Build 2 opens the Unit 2 project, the Decision Engine. Today is Define and Measure, on paper. You pick the decision you are automating and list every input before you write a line of code.
Image: A movie ticket stub with four price tiers printed on it, flat navy and accent blue.
---
