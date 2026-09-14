# And, Or, Not
---
## Slide 1: Your alarm thinks Monday is Sunday
- You wrote a sleep-in program for weekends
- You tested Saturday. It worked
- You tested Sunday. It worked
- Monday morning, it let you sleep
Speaker notes: Here is a program that passed every test its author ran. Saturday, sleep in. Sunday, sleep in. Then Monday came and it said sleep in again, and somebody missed first period. The author did not skip testing. They tested the wrong values. Today you learn the three words that join conditions together, and the one English habit that turns them into this bug.
Image: A phone alarm screen showing Monday with the alarm switched off, flat navy and accent blue.
---
## Slide 2: Three words that join conditions
- and: True only when both sides are True
- or: True when at least one side is True
- not: flips True to False, False to True
- Order: not first, then and, then or
Speaker notes: Real rules are rarely one question. You can go to the concert if you have a ticket and a ride. You sleep in if it is Saturday or Sunday. No video games if your homework is not done. Python gives you those exact three words. They are called logical operators, which is the term the WebXam uses. Multiplication happens before addition, and in the same way not happens first, then and, then or.
Image: Three labeled switches, two wired in series for and, two wired in parallel for or, one with an inverter for not.
---
## Slide 3: A ticket and a ride
```python
has_ticket = True
has_ride = False

print(has_ticket and has_ride)
print(has_ticket or has_ride)
print(not has_ride)

if has_ticket and has_ride:
    print("You are going to the concert.")
else:
    print("Not tonight.")
```
```
False
True
True
Not tonight.
```
Speaker notes: A ticket and no ride. And needs both, so it is False, and you are not going. Or needs one, so it is True. Not flips False to True. Notice I did not write has ticket double equals True. When a variable is already a bool, the variable is the condition. Write if has ticket, and read it as English.
Image: None. This slide is code.
---
## Slide 4: The right way to say weekend
```python
day = input("What day is it? ").strip().lower()

if day == "saturday" or day == "sunday":
    print("Sleep in.")
else:
    print("Alarm is set for 6:45.")
```
Speaker notes: Look at both sides of the or. Day double equals saturday is one complete question. Day double equals sunday is another complete question. Or joins two questions. It does not join two words. I am going to delete one piece of this line, the piece that English lets you skip, and run it with monday.
Image: None. This slide is code.
---
## Slide 5: The wrong way, and no error
```python
if day == "saturday" or "sunday":
    print("Sleep in.")
```
```
What day is it? monday
Sleep in.
```
Speaker notes: No error. Monday is the weekend. Python split this into two things. Day double equals saturday, which is False on Monday. And the word sunday standing alone, which is not a question at all. When an if needs True or False and gets a string, an empty string counts as False and every other string counts as True. So the right side is always True, and the whole thing is True every day forever.
Image: None. This slide is code.
---
## Slide 6: Sixth time, same shape
- It passed the Saturday test
- It passed the Sunday test
- It fails the five days nobody tried
- Always test a value that should be False
Speaker notes: This is the sixth time this course has shown you a bug that does not crash. What makes this one sneaky is that it passes the two most natural tests. If you only test values that should make the condition True, you will never see it. So here is the rule for every condition you write. Test at least one value that should make it False, and watch it be False.
Image: A seven-day calendar with Saturday and Sunday checked and the other five days marked untested in accent blue.
---
## Slide 7: Python stops early
```python
bill = float(input("Pizza bill: "))
people = int(input("How many people are paying? "))

if people > 0 and bill / people <= 10:
    print("Everyone pays ten dollars or less.")
else:
    print("Either nobody is paying or it costs more than ten each.")
```
Speaker notes: Python reads and from left to right and stops the moment it knows the answer. If people is zero, people greater than zero is False, and False and anything is False. So Python never runs the division. That is called short circuiting. Watch what happens if I put the division first and type zero people.
Image: None. This slide is code.
---
## Slide 8: Swap the sides and it crashes
```python
if bill / people <= 10 and people > 0:
```
```
ZeroDivisionError: float division by zero
```
Speaker notes: Same two conditions, opposite order, and now the division runs before the check. Dividing by zero crashes. Put the check that protects something on the left. The same trick protects string indexing. Checking that a nickname is not empty before you look at its first character is the difference between Okay and an index error.
Image: None. This slide is code.
---
## Slide 9: Mixing and with or
- Members or coupon holders get a discount
- Only on totals over 20 dollars
- and happens before or
- Without parentheses, members skip the total check
- Parentheses make your grouping visible
Speaker notes: A store gives a discount to members or people with a coupon, but only on totals over twenty dollars. If you write is member or has coupon and total greater than 20, a member gets the discount on an eighteen dollar order, because and grabs its neighbors first. No error. Put parentheses around the or part and it means what the store meant. Whenever a condition mixes and with or, use parentheses.
Image: The condition written twice, once with invisible grouping shown by faint brackets and once with explicit parentheses.
---
## Slide 10: What you are about to build
- Build 1: Lab U02-01 Ticket Pricing, Part 2
- Tuesday, student ID, and the weekend surcharge
- Step 9 needs both and and or
- Build 2: Decision Engine, Analyze phase
Speaker notes: Build 1 finishes the ticket lab. You add the day and the student ID, and step nine asks for a surcharge on Friday or Saturday for adult and student tickets. That condition needs both and and or, so it needs parentheses, and If it breaks item four is today's Monday bug waiting for you. Build 2 is the Decision Engine Analyze phase. Write every rule your engine follows as a sentence, and underline every and, or, and not you find in those sentences.
Image: A laminated price card with the Friday and Saturday row highlighted in accent blue.
---
