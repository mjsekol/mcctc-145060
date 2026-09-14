# Loops Inside Loops
---
## Slide 1: The seating chart that stopped after one row
- Print seats for 3 rows of 4
- The program prints Row 1, seats 1 to 4
- Then it says Seating chart done
- Eight seats are missing
- No error, and the first row is perfect
Speaker notes: A lot of real information comes in two directions at once. Rows and seats. Weeks and days. Players and attempts. One loop walks one direction. To walk both, you put a loop inside a loop. Today you learn the one rule that explains every nested loop, and the one misplaced line that makes a chart stop after its first row while announcing that it finished.
Image: A small theater seating grid with only the first row filled in, flat navy and accent blue.
---
## Slide 2: The rule
- A nested loop is a loop inside another loop's body
- The inner loop runs start to finish
- On every single pass of the outer loop
- Inner body runs outer count times inner count
- Indentation is the only thing that says what is inside
Speaker notes: Say the rule with me. The inner loop runs all the way through on every pass of the outer loop. So three outer passes of four inner passes is twelve. It works like a clock. The minute hand goes all the way around before the hour hand moves one step. And indentation is doing all the work. Move a line four spaces left, and it belongs to a different loop.
Image: A clock face with the minute hand completing a full circle for one step of the hour hand.
---
## Slide 3: Weeks and practices
```python
for week in range(1, 4):
    print(f"Week {week}:")
    for practice in range(1, 5):
        print(f"  Practice {practice}")
```
```
Week 1:
  Practice 1
  Practice 2
  Practice 3
  Practice 4
Week 2:
  Practice 1
  ...
```
Speaker notes: Predict the number of lines before I run it. Three week headings, and four practices per week. Fifteen. And watch practice. It starts over at one for every week, because the inner for begins fresh every time the outer loop reaches it.
Image: None. This slide is code.
---
## Slide 4: Building a seat map
```python
ROWS = 3
SEATS_PER_ROW = 5
for row in range(ROWS):
    row_letter = chr(ord("A") + row)
    row_text = ""
    for seat in range(1, SEATS_PER_ROW + 1):
        row_text = row_text + f"{row_letter}{seat} "
    print(row_text.strip())
```
```
A1 A2 A3 A4 A5
B1 B2 B3 B4 B5
C1 C2 C3 C4 C5
```
Speaker notes: Week 4 is back. Letters are numbers, so row zero plus the code for A is A, and row one is B. Now look where row text equals empty string sits. Inside the outer loop, above the inner loop. It resets once per row. And the print is in the outer loop, after the inner loop, so it prints once per row when the row is complete. Those two placements are the whole skill.
Image: None. This slide is code.
---
## Slide 5: Your game is already nested
- An if on the room, inside the while
- An if on the direction, inside the room's branch
- Four levels deep, and every level is correct
- Keep nesting when the next question depends on the answer
- destination = "" first, so a blocked move costs nothing
Speaker notes: Your text adventure has had nested structures since last week. Which room, then which direction, inside the game loop. That is Unit 2's rule for when nesting is the right call. The next question depends on the answer. Set destination to empty before the room check, and one place handles you cannot go that way, and only a real move adds to moves.
Image: A decision tree with room at the top branching to directions, inside a loop arrow.
---
## Slide 6: break only leaves one loop
```python
SECRET_DIGIT = "7"
for friend in range(1, 4):
    print(f"Friend {friend}")
    tries = 0
    while tries < 3:
        tries = tries + 1
        guess = input("  Guess a digit: ").strip()
        if guess == SECRET_DIGIT:
            print("  Correct")
            break
```
Speaker notes: Three friends, three tries each, to guess a locker digit. Friend one guesses right and the program breaks. Then it goes straight on to friend two. The break ended the inner while only. The outer for never noticed. That is yesterday's rule, the loop it is directly inside. And notice tries equals zero, inside the for, above the while. Every friend gets a fresh three tries. Hold on to that.
Image: None. This slide is code.
---
## Slide 7: Watch this: the seating chart
```python
row = 1
seat = 1
while row <= 3:
    while seat <= 4:
        print(f"Row {row}, seat {seat}")
        seat = seat + 1
    row = row + 1
print("Seating chart done")
```
Speaker notes: Same chart, written with while loops. Three rows of four seats. Twelve lines, then done. Everything is set up before the loops, the way we always say to. Predict the output before I run it.
Image: None. This slide is code.
---
## Slide 8: The wrong way: four seats, and done
```
Row 1, seat 1
Row 1, seat 2
Row 1, seat 3
Row 1, seat 4
Seating chart done
```
Speaker notes: Four seats instead of twelve. No error. And it says done. Trace it. After row one, seat is five. Row becomes two, and the inner while checks seat less than or equal to four. Seat is still five. Nothing reset it. The inner loop runs zero times for rows two and three. The fix is one line in a different place. Seat equals one goes inside the outer loop, right above the inner loop. And this bug is impossible with for seat in range, because range starts over by itself.
Image: None. This slide is code.
---
## Slide 9: Testing a nested loop
- Count the lines: outer count times inner count
- Check the SECOND pass of the outer loop
- The first pass hides reset bugs
- A done message proves nothing
- Prefer for when the inner count is known
Speaker notes: How do you catch this in your own code. Predict the line count and then count. Look at the second pass of the outer loop, not the first, because the first pass is always correct when a reset is misplaced. Do not trust a message that says done, because it prints no matter what happened above it. And when you know the inner count, use for, and the bug cannot exist.
Image: A checklist beside a grid where the second row is circled.
---
## Slide 10: What you are about to build
- Build 1: Lab U03-01 Training Plan, Part 2
- The same plan as a grid: weeks down, days across
- Rest days marked on Wednesday and Sunday
- Grid total must equal your Part 1 total
- Build 2: v1 lose states, blocked moves, and a for loop
Speaker notes: Build one takes Monday's training plan and prints it as a grid, one row per week, one column per day, with rest days marked. The grid adds up the minutes a second way, and the two totals have to match. If they do not, one of your loops is wrong, and that is a built in test. Build two is your adventure. At least one lose state a player can reach by playing, blocked moves that cost nothing, and a for loop that does real work.
Image: A seven-column weekly grid with two shaded rest columns, navy and accent blue.
---
