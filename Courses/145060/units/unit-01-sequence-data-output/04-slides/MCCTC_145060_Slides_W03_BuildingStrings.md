# Putting Text Together
---
## Slide 1: Your money numbers look wrong and you know it
- Last week your program said 0.9006211180124224
- Nobody writes a price that way
- You have been ignoring it
- Today it gets fixed
Speaker notes: Open your Shift Pay program from last week and look at the weeks number. Zero point nine zero zero six two one one and so on. Every one of you saw that, decided it was probably fine, and moved on. It was not fine and you knew it. Today you get the tool that fixes it, and on the way there you get two other ways to build text that you will use constantly.
Image: A terminal showing a long ugly decimal next to a clean formatted price, contrasted.
---
## Slide 2: Three ways to join text
```python
first = "Ava"
last = "Ruiz"

print(first + last)          # AvaRuiz
print(first + " " + last)    # Ava Ruiz
print(first, last)           # Ava Ruiz
```
Speaker notes: Look at line one. No space. Plus glues two strings together and adds absolutely nothing between them, so if you want a space you supply it yourself, which is line two. Line three is different underneath even though the output matches. The comma hands print two separate values and lets print put the space in. One of these makes a new string. One of them does not.
Image: None. This slide is code.
---
## Slide 3: The difference shows when you stop printing
- Plus makes one new string you can store
- A comma only tells print how to display things
- If you need the full name in a variable, use plus
- Same output, different mechanism
Speaker notes: Here is when it matters. If you want the whole name stored in one variable so you can use it later, only the plus version gives you that. The comma version never made a full name at all. It made two separate things and let print deal with them. Watch for this, because students who learn them as interchangeable get stuck the first time they need the value rather than the display.
Image: Two boxes. Left, one box labelled full underscore name containing Ava Ruiz. Right, two separate boxes going into a print icon.
---
## Slide 4: f-strings, the one you will actually use
```python
name = "Ava"
hours = 13.5
rate = 11.5

print(f"{name} worked {hours} hours at {rate} per hour")
print(f"Pay: {hours * rate}")
```
```
Ava worked 13.5 hours at 11.5 per hour
Pay: 155.25
```
Speaker notes: An f in front of the quote, and anything in curly braces gets worked out and dropped in. Notice the second line. That is a whole calculation inside the braces, not only a name. This is shorter than plus, it handles the conversion for you, and it does one more thing that the other two cannot do at all.
Image: None. This slide is code.
---
## Slide 5: Here is your fix
```python
print(f"Pay: ${hours * rate:.2f}")
```
```
Pay: $155.25
```
Speaker notes: The colon starts a formatting instruction. Dot two f means show this as a number with exactly two digits after the decimal point. That is it. That is the thing that has been bothering you since last Thursday. Everything before the colon says what to show. Everything after it says how to show it.
Image: None. This slide is code.
---
## Slide 6: Columns, while we are here
```python
print(f"Pay: {hours * rate:>10.2f}|")
```
```
Pay:     155.25|
```
Speaker notes: Greater than ten means right align this inside a space ten characters wide. I put a pipe character at the end so you can see where the field stops. This is how every report you will ever build lines its columns up, and you will need it in the lab today to make a badge whose edges do not wobble.
Image: None. This slide is code.
---
## Slide 7: Now I break it on purpose
```python
laps = 7
print("You ran " + laps + " laps")
```
```
TypeError: can only concatenate str (not "int") to str
```
Speaker notes: You have met this error before. Week two, when we tried to add three to a piece of text. Same rule, new place. Plus between a string and a number is not defined, because Python will not guess whether you meant glue or add. Give me the fixes. There are three and I want all of them.
Image: None. This slide is code.
---
## Slide 8: Three fixes, and one of them wins
- Commas: print handles the spaces
- str(laps): convert it yourself
- f-string: shortest, and the only one that formats
- Pick the f-string unless you have a reason
Speaker notes: All three are correct and you will see all three in real code. The f-string wins for one reason that has nothing to do with typing less. It is the only one of the three that can also format, and the moment you need two decimal places or an aligned column the other two stop being options. Learn all three, reach for the third.
Image: Three code fragments stacked, the third highlighted in accent blue.
---
## Slide 9: Why plus feels right and is wrong
- Plus reads like the word "and" in your head
- English does not care what type a thing is
- Python does, and it will not guess
- The error is telling you it refused to guess
Speaker notes: The reason everybody writes this bug is that the sentence sounds fine. You ran and seven and laps. That is how the line reads out loud, and in English nobody stops you. Python stops you, and it is worth noticing that stopping you is the friendly behaviour here. It could have guessed. Guessing is how you get one two one two one two.
Image: A sentence in plain English above the same sentence as code, with the type mismatch marked in accent blue.
---
## Slide 10: What you are about to build
- Reopen Shift Pay and convert every print
- Every money value gets two decimal places
- No plus signs joining text and numbers
- Then lab U1-02, steps one through five
Speaker notes: Build one is going back to last week's program and fixing the thing that has been bothering you. Every print becomes an f-string, every money value gets dot two f. Then you start the badge maker lab, which is the first three steps only. Do not run ahead into slicing. That is tomorrow and it needs its own head.
Image: A split panel, before and after, showing an ugly decimal becoming a formatted price.
---
