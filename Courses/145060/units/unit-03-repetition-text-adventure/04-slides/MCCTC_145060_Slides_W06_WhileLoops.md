# Again, and Again, Until
---
## Slide 1: A game that ends after one command
- Your adventure shows a room
- You type north
- It prints the next room
- Then the program ends. Game over, after one move
Speaker notes: Every program you have written runs top to bottom one time and stops. That is fine for a ticket price. It is useless for a game. A game has to show the room, read a command, react, and then do it again, over and over, until you win, lose, or quit. Yesterday you wrote WHILE playing in pseudocode. Today it becomes Python. Before anything else, find Ctrl C on your keyboard. You will need it in about eight minutes.
Image: A terminal with one room description, one command, and then the prompt returning to the shell, flat navy and accent blue.
---
## Slide 2: How while works
- Check the condition at the top
- False: skip the block, the loop is over
- True: run the whole block
- Go back to the top and check again
- Something inside must change the condition
Speaker notes: A while loop is an if that keeps coming back. Check the condition. If it is False, skip the block and move on. If it is True, run the whole block, then go back up and check again. The check happens at the top, before each pass. A value that turns False halfway through the block does not stop that pass. And the last bullet is the one that bites. Something inside the loop has to change what the condition depends on.
Image: A flowchart diamond with a True arrow into a block and a curved arrow from the block back to the diamond.
---
## Slide 3: Count-controlled: the storm countdown
```python
moves_left = 3

while moves_left > 0:
    print(f"Thunder rolls. Moves until the storm: {moves_left}")
    moves_left = moves_left - 1

print("The storm has reached the ridge.")
```
```
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 2
Thunder rolls. Moves until the storm: 1
The storm has reached the ridge.
```
Speaker notes: Trace it with me. Three is more than zero, print three, moves left becomes two. Back to the top. Two, print, becomes one. Back to the top. One, print, becomes zero. Back to the top. Zero is not more than zero, so the loop ends. Three parts make this work. Set the counter before. Check it in the condition. Change it inside. Watch what happens when I delete the change.
Image: None. This slide is code.
---
## Slide 4: The wrong way: the loop that never ends
```python
moves_left = 3

while moves_left > 0:
    print(f"Thunder rolls. Moves until the storm: {moves_left}")

print("The storm has reached the ridge.")
```
```
Thunder rolls. Moves until the storm: 3
Thunder rolls. Moves until the storm: 3
...
KeyboardInterrupt
```
Speaker notes: I deleted one line. Moves left is three forever, so the condition is True forever. This is an infinite loop. When I tested it, it printed more than 370 thousand lines in a fifth of a second. Press Ctrl C. Python stops and ends the traceback with KeyboardInterrupt. That is not a Python bug. That is Python saying you stopped it by hand, and the traceback shows which line was running, which is almost always inside the loop that forgot to change its variable.
Image: None. This slide is code.
---
## Slide 5: Sentinel-controlled: the game loop
```python
playing = True

while playing:
    command = input("> ").strip().lower()
    if command == "look":
        print("Rain streaks the glass doors behind you.")
    elif command == "quit":
        print("You leave the station to the storm.")
        playing = False
    else:
        print(f"'{command}' is not a command. Try look or quit.")

print("GAME OVER")
```
Speaker notes: You cannot count how many commands a player will type. So this loop runs until a special value shows up. Quit is the sentinel. Playing is a flag, a bool, and the only line that changes it is inside the quit branch. Notice that all of Unit 2 lives inside this loop. The if, elif, else runs once per command. A loop does not replace decisions. It repeats them.
Image: None. This slide is code.
---
## Slide 6: Count or sentinel
- Count-controlled: you know how many times
- It stops when a counter hits a limit
- Sentinel-controlled: you do not know in advance
- It stops when a special value appears
Speaker notes: Two shapes. If you know how many times something should happen, three laps, five tickets, twenty moves before the storm, that is count-controlled, and it needs a counter. If you do not know, because a person decides, that is sentinel-controlled, and it waits for a value like quit. Storm Relay uses both at once. The game loop waits for the player, and the move counter decides when the storm arrives.
Image: A stopwatch icon on one side and a stop sign icon on the other, navy and accent blue.
---
## Slide 7: Three laps, two printed
```python
laps_required = 3
lap = 1

while lap < laps_required:
    print(f"Lap {lap} done.")
    lap = lap + 1

print("Practice complete.")
```
```
Lap 1 done.
Lap 2 done.
Practice complete.
```
Speaker notes: No error. Two laps. Your coach would notice. Python did not. Lap starts at one, and when lap is three, three is less than three is False, so the third lap never runs. Starting at one and using less than disagree about what the limit means. Use less than or equal, or start at zero. Count the iterations of every new loop by hand at least once.
Image: None. This slide is code.
---
## Slide 8: Eleventh time, same shape
- Week 3: a year sliced down to 202
- Week 4: exactly 20 percent battery missed
- Today: a loop one lap short
- Same bug: a boundary with the wrong comparison
- None of them crashed
Speaker notes: Eleven times now across three units, a program has run cleanly and been wrong, and three of those are the exact same bug in three costumes. A slice that stopped one early. A battery warning that missed exactly 20. A loop that ran one time too few. Every one is a boundary decided with the wrong comparison. The name for this is an off by one error, and it is one of the most common bugs in all of programming.
Image: Three small snippets side by side, each with the boundary character circled in accent blue.
---
## Slide 9: The mistakes that crash
- Missing colon: SyntaxError expected colon
- No indented block: IndentationError
- Same rules as if
- Ctrl C stops a runaway program
Speaker notes: The friendly mistakes. Forget the colon after the condition and Python says expected colon. Forget to indent the block and you get an indentation error that names the while line. These are the same rules you learned for if. And Ctrl C is not a mistake. It is the tool you use when your loop runs away from you, which will happen to everyone in this room this month.
Image: Two short terminal error lines stacked on a navy background.
---
## Slide 10: What you are about to build
- Build 1: Storm Relay game loop skeleton
- From yesterday's pseudocode: while playing
- move counts toward the storm, quit ends it
- Build 2: Gate 2 review of AI decision code
Speaker notes: Build 1 turns yesterday's pseudocode into your first real loop. No rooms yet. A while playing loop that reads a command, where move adds one toward a five move storm limit, quit sets playing to False, and anything else says it is not a command. Count your iterations. Five moves should end the game on the fifth, not the fourth or sixth. Build 2 is this week's Gate 2, reviewing AI code built from Unit 2 decisions, and it is due by the end of the block.
Image: A terminal showing a short game loop session ending in GAME OVER, navy and accent blue.
---
