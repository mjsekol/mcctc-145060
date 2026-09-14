# One Turn, Over and Over
---
## Slide 1: You won. The game says GAME OVER
- You reach the studio
- You type broadcast
- The screen says you are on the air
- Then it says GAME OVER
- No error anywhere
Speaker notes: Imagine you playtest a friend's game, you do everything right, you win, and the last line on the screen is game over. That is a real bug, it does not crash, and by the end of today you will know exactly which line causes it. Last Wednesday you drew the flowchart. Thursday you wrote while playing. Today we turn the whole model into a game.
Image: A terminal ending with a win message immediately followed by GAME OVER, flat navy and accent blue.
---
## Slide 2: A game loop is four steps
- Show the state
- Read one command
- Update the state
- Check whether the game is over
- Repeat while playing. Report how it ended after
Speaker notes: Every text adventure, every turn based game, and a surprising amount of real software, a checkout kiosk, a vending machine, a chat bot, runs on this. A while loop around four steps. Show, read, update, check. After the loop ends, report how it ended. Match these four steps against the pseudocode you committed last week. They should line up one to one.
Image: A circular diagram with four labeled stages and an exit arrow to a report box.
---
## Slide 3: State is everything the game remembers
- room, where you are
- moves, how many you have used
- What you are carrying, as True or False flags
- playing: should the loop run another turn
- won: why did the loop stop
Speaker notes: State is every value the game has to remember from one turn to the next. It is the State box on your IPO chart. Every state variable gets its value above the while. And look at the last two. Playing and won are both flags, and they answer different questions. Playing is read by the while line. Won is read by the report after the loop. Mixing those two up is today's bug.
Image: A labeled panel of five variables with their starting values.
---
## Slide 4: Steps 1 and 2: show and read
```python
room = "lobby"
moves = 0
won = False
playing = True

while playing:
    print()
    print(f"== {room.title()} ==")
    if room == "lobby":
        print("Exits: north.")
    elif room == "hallway":
        print("Exits: south, west.")
    elif room == "studio":
        print("A transmitter hums. Exits: east.")

    command = input("> ").strip().lower()
```
Speaker notes: This is the three room slice of Storm Relay you modeled on paper. State at the top, above the loop. Inside the loop, step one shows the room. Step two reads exactly one command and cleans it, so NORTH with spaces around it still works. Every turn, one command.
Image: None. This slide is code.
---
## Slide 5: Steps 3 and 4: update and check
```python
    if command == "north" and room == "lobby":
        room = "hallway"
        moves = moves + 1
    elif command == "broadcast" and room == "studio":
        print("The needle jumps. You are on the air.")
        won = True
        playing = False
    elif command == "quit":
        playing = False
    else:
        print("You cannot do that here.")

    if playing and moves == MAX_MOVES:
        print("Thunder cracks overhead. The storm has reached the ridge.")
        playing = False

if won:
    print(f"YOU WIN in {moves} moves.")
else:
    print("GAME OVER")
```
Speaker notes: I have cut the other three movement branches and the quit message to fit the slide. The full file is in the lecture notes. Step three updates state. A move changes room and adds one to moves. A broadcast in the studio sets won and playing. Step four checks for a loss, and it checks playing first, so if you already won this turn, the storm message cannot also print. The first ending wins. Then, after the loop, the report reads won.
Image: None. This slide is code.
---
## Slide 6: playing = False does not stop this turn
```python
playing = True
turn = 0
while playing:
    turn = turn + 1
    playing = False
    print(f"Still finishing turn {turn}")
print("Loop over")
```
```
Still finishing turn 1
Loop over
```
Speaker notes: This surprises almost everybody. Setting playing to False does not jump out of the loop. The while checks its condition at the top, so every line below the assignment in the same pass still runs. In a game, that is how a player dies and then wins on the same turn. Every time you end the game from inside the loop, read what else still runs that turn.
Image: None. This slide is code.
---
## Slide 7: The wrong way: I delete one line
```python
    elif command == "broadcast" and room == "studio":
        print("The needle jumps. You are on the air.")
        playing = False
```
```
> broadcast
The needle jumps. You are on the air.

GAME OVER
```
Speaker notes: I removed won equals True. North, west, broadcast. The loop stops, because playing is False. And the report says game over, because the report does not read playing. It reads won, and nobody changed won. No error. The player won and the program says they lost. Stopping the loop and recording why it stopped are two separate pieces of state, and this branch updated one of them.
Image: None. This slide is code.
---
## Slide 8: Every ending sets every flag
- A win sets won and playing
- A loss sets playing, and never touches won
- A quit sets playing
- Trace each ending to the final report
- Play to a win, a loss, and a quit
Speaker notes: Here is the rule that prevents it. Every branch that ends the game sets every flag the ending depends on. When you add a new way to win or lose, trace it all the way down to the report and read the message it will print. And test all three endings every time you change the loop. Not one. All three.
Image: Three arrows labeled win, lose, and quit converging on one report box.
---
## Slide 9: When a test script runs out
- Testing by piping commands into your game
- The game is still asking after the last command
- Python stops with EOFError: EOF when reading a line
- The game is fine. The script never reached an ending
- Add commands until the script wins or loses
Speaker notes: You will test your game by feeding it a file of commands instead of typing them every time. If the file runs out while the game is still waiting at the prompt, Python reports EOFError, EOF when reading a line. That does not mean your game crashed on its own. It means your script never reached an ending. That is useful information, not a disaster.
Image: A text file of commands flowing into a terminal prompt, with the last arrow empty.
---
## Slide 10: What you are about to build
- Build 1: Lab U03-02 Locked Out, Part 1
- Three locations, a battery limit, a key to find
- Win, lose by battery, and quit must all work
- Build 2: v1 first code, from yesterday's committed design
- Loop, every room, movement, a win state, the report
Speaker notes: Build one is Locked Out, part one. It is the same pattern in a completely different world, and you will write the state, the loop, the four steps, and the report yourself. Your acceptance test is three runs, one win, one loss, one quit. Build two is the first code of your own adventure, and it starts from the design you committed yesterday, not from a blank file. The loop, every room, movement for every exit on your map, your win state, and the report after the loop. Before you commit, play it to the win and read the last line.
Image: A small three-location map of a porch, backyard, and shed, navy and accent blue.
---
