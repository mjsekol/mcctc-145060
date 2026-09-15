# The Bug That Does Not Crash
---
## Slide 1: Yesterday your program knew the numbers
- You typed them into the file
- Only you can change them
- Nobody else can use it
- Today it asks
Speaker notes: Yesterday you built something real, and it still has one number written into the file. Today it asks the person running it. That is the difference between a thing you made and a thing somebody can use. And it introduces one problem, which is the single most important idea in this unit.
Image: A file icon with numbers baked into it, next to a terminal showing a question prompt.
---
## Slide 2: Everything typed is text
- input always hands back text
- Always. No exceptions
- Digits typed are still text
- Converting is a separate step you ask for
Speaker notes: Here is the rule, and I want you to write it down word for word. Input always hands back text. It does not matter what the person typed. If they type one two, you do not have the number twelve, you have two characters that happen to be digits. Turning that into a number is a separate step, and Python will not do it for you, and it will not warn you that it did not.
Image: A keyboard with digits going in and a text label coming out, one-way arrow.
---
## Slide 3: Prove it to yourself
```python
hours = input("How many hours did you work? ")
print("Python thinks that is a:", type(hours).__name__)
```
```
How many hours did you work? 12
Python thinks that is a: str
```
Speaker notes: I typed one two. Nothing but digits. And Python is holding str, which means text. Most of you will not believe this until you run it yourself, so run it yourself in the first five minutes of build one. This is the whole day in three lines.
Image: None. This slide is code.
---
## Slide 4: Watch what happens next
```python
hours = input("How many hours did you work? ")
print("Three weeks of that is:", hours * 3)
```
Speaker notes: I am going to type twelve. Before I press enter, tell me what you expect to see. Thirty six, right. Watch the screen and do not say anything yet.
Image: None. This slide is code.
---
## Slide 5: One two one two one two
```
How many hours did you work? 12
Three weeks of that is: 121212
```
Speaker notes: No error. No traceback. No red text. Nothing anywhere on this screen tells you something went wrong. Python did exactly what I asked. Hours is the text one two, and multiplying text by three repeats it three times, which is a real feature that works correctly. I asked for it by accident and it obliged.
Image: None. This slide is code.
---
## Slide 6: The dangerous bugs are the ones that do not crash
- Plus between text and a number stops
- Times between text and a number succeeds
- One tells you immediately
- The other hands you garbage and says nothing
Speaker notes: Write this sentence down. The dangerous bugs are the ones that do not crash. If I had written plus instead of times, Python would have raised a TypeError, pointed at the line, and I would have fixed it in ten seconds. Instead it succeeded. You find this one weeks later, when somebody reports a weird number in your text adventure, and by then you have no idea which line did it. An error message is a gift.
Image: Two panels. Left, a red error with a clear arrow at one line. Right, a clean output with a wrong number and no marks at all.
---
## Slide 7: So convert, on the way in
```python
hours = int(input("How many hours did you work? "))
print("Three weeks of that is:", hours * 3)
```
```
How many hours did you work? 12
Three weeks of that is: 36
```
Speaker notes: Wrap the conversion around the input on the same line. Read it inside out. Ask the question, take the text that comes back, convert it, then attach the name. Do it on one line every time, so there is never a moment where an unconverted value has a name you could reach for by mistake.
Image: None. This slide is code.
---
## Slide 8: Which converter, and it is a real decision
- int for things that cannot be half
- float for things that can
- People splitting a bill: int
- Hours worked: float, because 7.5 is real
Speaker notes: This is a decision, not a habit. Ask one question about the value. Could this reasonably be a half of something. Hours worked, yes, so float. Number of people, no, so int. Get this backwards and you either crash on a perfectly reasonable input or silently accept two and a half people, and one of those two failures is much harder to notice.
Image: A two-column decision diagram with the question at the top and examples under each branch.
---
## Slide 9: Converting has its own failure
```python
print(int("abc"))
print(int("11.5"))
```
```
ValueError: invalid literal for int() with base 10: 'abc'
ValueError: invalid literal for int() with base 10: '11.5'
```
Speaker notes: The first one you expected. The second one surprises people, because eleven point five reads as a number to you. Int does not ask whether it is a number. It asks whether the text spells a whole number, and that one does not. Use float. And notice that fixing one problem introduced another, which is normal. Handling this properly has a name, error handling, and it is Unit 4.
Image: None. This slide is code.
---
## Slide 10: Some things that look like numbers are not
- A jersey number
- A phone number
- A zip code
- Would adding two of them ever mean anything
Speaker notes: Last idea, and it is the one that separates people who understand this from people who memorized it. Not everything written in digits is a quantity. Here is the test question. Would adding two of these together ever mean anything. Add two jersey numbers and you get nothing. Add two zip codes and you get nothing. If the answer is no, it is a label, and it stays text, and converting it would throw away the leading zero anyway.
Image: A jersey, a phone, and an envelope, each with digits on them and a crossed-out plus sign between them.
---
## Slide 11: What you are about to build
- Every number in yesterday's program becomes a question
- Every one converted on the way in
- Then lab U1-01, steps seven through twelve
- Step eleven breaks it on purpose
Speaker notes: Take yesterday's calculator and make every hardcoded number a question. Convert each one on the line you ask for it. Then finish the lab. Step eleven asks you to break your own program on purpose by typing a word where a number goes, and to copy the error into your README exactly. Do not skip it and do not fix it. Knowing what breaks your program is worth more today than a program that never breaks.
Image: A terminal mid-run showing three prompts answered and a labeled result, navy and accent blue.
---
