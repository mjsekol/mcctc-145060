# Draw It Before You Build It
---
## Slide 1: Three days in, there is no way to lose
- You start typing a text adventure
- It grows for three days
- Then you notice: nobody can ever lose
- The fix means rewriting half of it
Speaker notes: Unit 3 is a text adventure, and it is the biggest program you have written. Here is how big programs usually go wrong. You start typing, it grows, and on day three you discover one room has no exit, or there is no way to lose, or the game never ends. Every one of those problems is visible on paper in ten minutes. Today you write no Python. That is the lesson, not a gap in it.
Image: A half-built maze drawn on graph paper with one corridor that leads nowhere, flat navy and accent blue.
---
## Slide 2: Four tools, four questions
- IPO chart: what goes in, happens, comes out
- Flowchart: what order, where it splits or repeats
- Pseudocode: precise steps, one per line
- Decision tree: which question comes next
Speaker notes: Each tool answers a different question. The IPO chart is inputs, process, outputs. The flowchart is order. Pseudocode is the steps written precisely enough to become code. And a decision tree you already know, because your Decision Engine is one. The WebXam outcome is 5.1.3, model the solution with graphic tools and pseudocode, and the syllabus says your model comes before your adventure code.
Image: Four small icons in a row: a three-column table, a flowchart, indented text lines, and a branching tree.
---
## Slide 3: The IPO chart, plus state
```
INPUT                PROCESS                               OUTPUT
command typed        clean the command                     room description
                     decide: move, broadcast, quit, other  blocked-move message
                     move: change room, add 1 to moves     thunder warning
                     check moves against the storm limit   win or lose message

STATE (remembered between turns)
  room     starts as "lobby"
  moves    starts as 0
  playing  starts as True
```
Speaker notes: This is one turn of a three-room slice of Storm Relay, our class adventure. Inputs, process, outputs. And for a game, a fourth list, state, the things the program remembers from one turn to the next. Here is the rule that matters. If a value shows up in the process column and it is not an input and not in state, it does not exist. Remember that for slide nine.
Image: None. This slide is code.
---
## Slide 4: Flowchart shapes
- Oval: start or end
- Parallelogram: input or output
- Rectangle: a process step
- Diamond: a decision, one labeled arrow per answer
- An arrow pointing back up is a loop
Speaker notes: Four shapes carry almost every flowchart you will ever draw. The one that causes trouble is the diamond. A decision needs one arrow out for every possible answer, and each arrow needs a label. And any arrow that points back up to an earlier step is a loop. The game loop is one big arrow that goes back to the top after every command.
Image: The four flowchart shapes drawn with labels, and a curved arrow returning to the top.
---
## Slide 5: Two checks every game-loop flowchart must pass
- Every diamond has an arrow for every answer
- At least one path from inside the loop to End
- A diamond with one arrow is a dead end
- A loop with no exit never finishes
Speaker notes: Before you show me a flowchart, run these two checks. First, every diamond has an arrow for every answer. If a diamond only has a yes arrow, the no answer goes nowhere, and your code will do whatever you happen to type. Second, there is at least one path from inside the loop to the End oval. If there is not, the game can never finish. Tomorrow you will see exactly what that does to a real program.
Image: A flowchart with one diamond circled in accent blue because it has only one outgoing arrow.
---
## Slide 6: The same loop as pseudocode
```
SET room TO "lobby"
SET moves TO 0
SET playing TO True

WHILE playing
    DISPLAY the description of room
    INPUT command, cleaned to lowercase
    IF command is "quit"
        SET playing TO False
    ELSE IF command is a direction AND room has an exit that way
        SET room TO the destination
        ADD 1 TO moves
        IF moves equals MAX_MOVES
            DISPLAY "The storm has reached the ridge."
            SET playing TO False
    ELSE IF command is "broadcast" AND room is "studio"
        DISPLAY the win message
        SET playing TO False
    ELSE
        DISPLAY "You cannot do that here."

DISPLAY "GAME OVER"
```
Speaker notes: Pseudocode is the flowchart written as precise, indented English. Match every line to a shape. Every if and the while are diamonds. Every set and add is a rectangle. Every input and display is a parallelogram. While playing means repeat this block as long as playing is True. You have never written a loop in Python, and you do not need to, to model one. Tomorrow this exact line becomes code.
Image: None. This slide is code.
---
## Slide 7: A decision tree for one decision
```
Which room are you in?
  lobby    -> north?  yes: hallway   no: blocked
  hallway  -> south?  yes: lobby
              west?   yes: studio
              other:  blocked
  studio   -> east?   yes: hallway   no: blocked
```
Speaker notes: The move step hides a second decision. Where does a move go? That depends on the room first and the direction second, and which directions you check depends on the room. That is a decision tree, and last Thursday's rule says keep the nesting when the next question depends on the answer. You can already write this in Python with an if on the room and an if on the direction inside each branch.
Image: None. This slide is code.
---
## Slide 8: Precise enough to code
- Not precise: IF the player can win
- Precise: IF room is studio AND power_on is True
- Every value must be an input or in state
- A classmate should not need to ask you anything
Speaker notes: Pseudocode fails when it hides a decision inside a vague phrase. If the player can win is not a condition. It is a wish. Which room, which values, compared to what. The test for good pseudocode is simple to say and hard to pass. Hand it to a classmate. If they have to ask you a single question before they can type the Python, it is not finished.
Image: Two index cards, one with a vague line crossed out and one with a precise condition, navy and accent blue.
---
## Slide 9: The wrong way: code from an incomplete model
```python
room = "hallway"
command = input("> ").strip().lower()

if command == "down":
    if has_flashlight:
        print("Your flashlight finds the basement stairs.")
    else:
        print("You step into total darkness.")
```
```
NameError: name 'has_flashlight' is not defined
```
Speaker notes: Somebody skipped the IPO chart and coded the dark basement rule from memory. They never listed the flashlight in state. It crashes, but only when a player walks down the stairs, which might be the forty-first thing somebody tries. On paper this was a missing row in a chart. Ten seconds to fix. And the worse version does not crash at all. It is a path through the game where nobody can win and nothing says so.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: IPO chart and flowchart for the slice
- Pass both checks before you move on
- Build 2: pseudocode and the move decision tree
- No Python today. Tomorrow the loop becomes code
Speaker notes: Build 1 is the IPO chart with state, and the flowchart for the three-room slice of Storm Relay. Run both checks on your own diagram before you show it to anybody. Build 2 is pseudocode that matches your flowchart line for line, and the decision tree for moves. No Python today. Keep all of it, because tomorrow the while line in your pseudocode becomes the first loop you ever write.
Image: A desk with graph paper showing a flowchart and a sheet of indented pseudocode, navy and accent blue.
---
