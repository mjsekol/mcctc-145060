# Count It For Me
---
## Slide 1: Seven days, three chances to mess up
- Print a pushup plan for seven days
- Thursday's while loop needs a start value
- A condition, and an update line
- Forget the update and it never stops
- Get the condition wrong and a day disappears
Speaker notes: On Thursday you learned the while loop, and you learned that it asks three things of you every single time. Set the counter. Check it. Change it. Most loops you will ever write have a simpler shape than a game loop. Do this seven times. Do this once for every character. For that shape, Python has a loop that does all three jobs for you, and today you learn it.
Image: A seven-day calendar strip with one day visibly missing, flat navy and accent blue.
---
## Slide 2: The same loop, twice
```python
# Thursday
day = 1
while day <= 7:
    print(f"Day {day}: 20 pushups")
    day = day + 1

# Today
for day in range(1, 8):
    print(f"Day {day}: 20 pushups")
```
Speaker notes: Both of these print the same seven lines. Look at what is missing from the second one. No day equals one. No day equals day plus one. The range supplies every value day will take, in order, and there is no update line to forget. The most common infinite loop in this course is a while with a missing update. A for loop over a range cannot have one.
Image: None. This slide is code.
---
## Slide 3: How for works
- A for loop walks a sequence, one item per pass
- The loop variable holds the current item
- When the sequence runs out, the loop ends
- range produces a sequence of whole numbers
- A string is a sequence of characters
Speaker notes: No condition to write and no counter to update, because the sequence decides both. On every pass, the loop variable holds the next item. When the items run out, the loop is over. The sequence you will use most is range. But a string is also a sequence, so a for loop can walk through every character of a username without a single index number.
Image: A row of numbered boxes with an arrow stepping from one box to the next.
---
## Slide 4: range stops before its stop number
- range(5) gives 0, 1, 2, 3, 4
- range(1, 8) gives 1 through 7
- range(10, 31, 5) gives 10, 15, 20, 25, 30
- range(5, 0, -1) counts down 5 to 1
- Up to but not including. Same as a slice
Speaker notes: This is the rule you already know from Week 3. A slice runs from here up to but not including there. So does range. One number means this many, starting at zero. Two numbers means from the first up to but not including the second. A third number is the step, and a negative step is the only way range counts down. Say it with me. Up to but not including.
Image: A number line from 0 to 8 with a bracket covering 1 through 7 and the 8 visibly outside it.
---
## Slide 5: Repeating a broadcast
```python
BROADCAST_REPEATS = 3
EMERGENCY_FREQUENCY = 1470

for repeat in range(1, BROADCAST_REPEATS + 1):
    print(f"({repeat} of {BROADCAST_REPEATS}) This is Kestrel Ridge relay on {EMERGENCY_FREQUENCY} kHz.")
```
```
(1 of 3) This is Kestrel Ridge relay on 1470 kHz.
(2 of 3) This is Kestrel Ridge relay on 1470 kHz.
(3 of 3) This is Kestrel Ridge relay on 1470 kHz.
```
Speaker notes: In Storm Relay the emergency message repeats so a listener who tunes in late still hears it. The number of repeats is a constant. Memorize the plus one. When you count from one and want the last number to be the limit itself, the stop is the limit plus one. Change the constant to five and you get one of five through five of five with no other edit.
Image: None. This slide is code.
---
## Slide 6: Walking a string, with an accumulator
```python
username = "xX_SkaterAva_Xx"
underscores = 0
for character in username:
    if character == "_":
        underscores = underscores + 1
print(f"{username} has {underscores} underscores")
```
```
xX_SkaterAva_Xx has 2 underscores
```
Speaker notes: Each pass, character holds one character of the username. The if inside runs once per character. Everything from Unit 2 still works inside a loop. And underscores is an accumulator. It is set to zero before the loop, it is updated inside, and after the loop it holds a result built from every pass. Set it inside the loop and it resets every pass.
Image: None. This slide is code.
---
## Slide 7: Watch this: the plan for the week
```python
for day in range(1, 7):
    print(f"Day {day}: 20 pushups")
print("Week complete")
```
Speaker notes: I want seven days. Days one through seven. I am going to type the seven, because seven is the number in my head. Before I run it, predict how many lines print. Write the number down. Then we count.
Image: None. This slide is code.
---
## Slide 8: The wrong way: six days and no error
```
Day 1: 20 pushups
Day 2: 20 pushups
Day 3: 20 pushups
Day 4: 20 pushups
Day 5: 20 pushups
Day 6: 20 pushups
Week complete
```
Speaker notes: Six days. No error. And it says week complete. Range stopped before seven, exactly like it always does. This is Thursday's practice that ran two laps instead of three, and it is Week 3's year that came out as two zero two. The dangerous bugs are the ones that do not crash. The defense is counting, not staring. Count the output lines of every new loop at least once. The version that does crash is range of a string from input, which gives a TypeError saying a str cannot be interpreted as an integer.
Image: None. This slide is code.
---
## Slide 9: for or while
- Known number of passes before the loop starts: for
- Once per character in a string: for
- Until the player types quit: while
- Until the answer is valid: while
- Your game loop is a while. The broadcast repeat is a for
Speaker notes: One test question decides it. Before the loop starts, can the program know how many passes it will make? If yes, for. If no, while. Nobody knows how many commands a player will type, so the game loop is a while. Everybody knows the broadcast repeats three times, so that is a for. Your text adventure will have both.
Image: A two-column sort, known count on one side and unknown count on the other.
---
## Slide 10: What you are about to build
- Build 1: Lab U03-01 Training Plan, Part 1
- A running plan that builds week by week to tryouts
- Step 5 breaks your range on purpose. Record the result
- Build 2: design YOUR text adventure. No code today
- Room map, IPO chart, flowchart, pseudocode, committed
Speaker notes: Build one is the training plan lab, part one. You will ask for starting minutes, a weekly increase, and the number of weeks, and a for loop will print the whole plan and a season total. Step five tells you to remove the plus one and record what happens. Do it, even though you know what happens now. Build two is the design of your own text adventure. On Wednesday you modeled Storm Relay. Today you make the same four models for your world, and you commit them before adventure dot py exists. I will be checking the order in your history.
Image: A terminal showing a six-line weekly plan and a season total, navy and accent blue.
---
