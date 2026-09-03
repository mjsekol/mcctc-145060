# Taking a String Apart
---
## Slide 1: One string, three facts inside it
- ROBO-2026-114
- That is a club, a season, and a member number
- Packed into one value
- You need them separately
Speaker notes: Look at that code. It is one string as far as Python is concerned, and it is three pieces of information as far as a human is concerned. Your club code, a licence plate, a flight number, a tracking number, a student ID. All of them do this. Today you learn how to reach in and take one piece out, and you learn the one counting rule that everybody gets wrong the first time.
Image: A single string with three coloured regions marked underneath, deep navy and accent blue.
---
## Slide 2: Every character has a number, starting at zero
```
M  C  C  T  C  1  4  5  0  6  0
0  1  2  3  4  5  6  7  8  9  10
```
Speaker notes: Write this down, because it stays on the board all week. Every character sits at a position and the first one is zero, not one. That feels wrong for about two days and then it never bothers you again. The reason is that the position number is really a distance from the start, and the first character is zero away from the beginning.
Image: None. This slide is code.
---
## Slide 3: Asking for one character
```python
code = "MCCTC145060"

print(code[0])      # M
print(code[4])      # C
print(code[-1])     # 0
print(len(code))    # 11
```
Speaker notes: Square brackets with one number gives you one character. Negative one counts backwards from the end, which is often exactly what you want and saves you doing arithmetic. And len tells you how many characters there are. Notice the trap in those last two lines. The length is eleven and the last position is ten. There is no position eleven.
Image: None. This slide is code.
---
## Slide 4: Asking for a range
```python
print(code[0:5])    # MCCTC
print(code[5:])     # 145060
print(code[:5])     # MCCTC
```
Speaker notes: Two numbers separated by a colon gives you a range. Leave the first one out and it means from the start. Leave the second out and it means to the end. Now here is the rule that the whole day depends on and I am going to say it the same way every single time.
Image: None. This slide is code.
---
## Slide 5: Up to but not including
- A slice runs from the first number
- Up to but NOT including the second
- code[0:5] gives positions 0, 1, 2, 3, 4
- Five characters. Not six
Speaker notes: From the first number, up to but not including the second. Say it with me. From the first number, up to but not including the second. I am going to say that phrase identically every time this week and I want it in your head by Friday, because the mistake it prevents does not produce an error message. It produces a wrong answer that looks fine.
Image: The string with a bracket spanning positions 0 to 4 and position 5 clearly outside it.
---
## Slide 6: Watch this
```python
code = "ROBO-2026-114"
print("Year is:", code[5:8])
```
Speaker notes: I want the year out of that code. The year starts at position five. I am going to write five to eight, because there are four digits and five plus four is nine, no wait, I will write eight and see. Predict what comes out before I press enter.
Image: None. This slide is code.
---
## Slide 7: Two zero two
```
Year is: 202
```
Speaker notes: No error. No red text. Nothing anywhere on this screen tells you something went wrong. The year is missing its last digit and the program is perfectly happy. Position eight holds the six, and the slice stops before eight, so the six never made it. The fix is five to nine, and position nine is the second dash, which is exactly what we do not want.
Image: None. This slide is code.
---
## Slide 8: You have seen this shape three times now
- Week 2 Thursday: 121212 from a missing conversion
- Week 2 Friday: two and a half people accepted
- Today: a year that lost a digit
- None of them crashed
Speaker notes: Stop and notice the pattern rather than the three examples. Three times in three weeks, a program has done exactly what it was told, produced output, and been wrong. Not one of them raised an error. Start assuming that a program producing output is a completely different claim from a program producing the right output. That assumption is what separates people who can debug from people who can only write.
Image: Three small terminal snippets stacked, each with a wrong value circled in accent blue, no error text anywhere.
---
## Slide 9: The one that does crash, and the one that does not
```python
print("MCCTC"[5])      # IndexError: string index out of range
print("MCCTC"[0:99])   # MCCTC, no error at all
```
Speaker notes: Reaching for one character past the end raises an error, because Python cannot invent a character that is not there. Slicing past the end does not, because a range is clipped to whatever exists. That asymmetry is worth knowing for a practical reason. A slice will never crash on you. Which means a slice can be silently wrong, and an index cannot.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Five real codes, pull one named piece from each
- Write the position numbers as a comment first
- Then lab U1-02, steps six through ten
- Step eight breaks your own slice on purpose
Speaker notes: Build one is five extractions from five real-shaped strings, and the requirement that matters is writing the position map as a comment before you write the slice. Counting first is the whole defence against what you watched happen. Then the lab, steps six through ten. Step eight asks you to break your own slice deliberately and write down that it produced a wrong answer with no error. Do not skip it. That is the assignment.
Image: A code file showing a position-number comment directly above a slice line, navy and accent blue.
---
