# Lecture Notes: The Game Loop Pattern
## 145060 Programming · Unit 3 · Week 7, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W07_TheGameLoop.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W07_TheGameLoop.pptx)

If you missed class, you can learn this concept from this file alone. Have your own text
adventure flowchart and pseudocode open next to this file. Everything below is those two
documents turning into Python.

---

## Why this exists

Last Wednesday you drew a flowchart with an arrow that points back up. Last Thursday that arrow
became `while playing:`. Neither one is a game yet.

A game needs more than a loop. It needs to **remember** where you are, how many moves you have
used, and what you are carrying. It needs to know when the game is **over**. And after it is over,
it needs to know **why**, because "you win" and "game over" are different endings.

Every text adventure, every turn-based game, and a surprising amount of real software (a checkout
kiosk, a chat bot, a vending machine) runs on one pattern. Learn the pattern once and you can build
all of them. It is outcome 5.3.6, repetition, used for the job loops exist to do.

---

## The concept in plain language

**A game loop is a `while` loop around four steps, working on a set of state variables.**

```
set up the state
WHILE the game is running
    1. show the state
    2. read one command
    3. update the state
    4. check whether the game is over
report how it ended
```

**State** is every value the game has to remember from one turn to the next. For the class adventure
that is `room`, `moves`, what you are carrying, and two flags. Your IPO chart from last week listed
them under State. **If a value is not in State, the loop forgets it at the end of every turn.**

Two flags do two different jobs, and mixing them up is today's bug:

| Flag | Question it answers | Who reads it |
|---|---|---|
| `playing` | Should the loop run another turn? | The `while` line |
| `won` | Why did the loop stop? | The report after the loop |

---

## Worked example 1: three rooms of Storm Relay

This is the three-room slice you modeled on paper on Wednesday of Week 6, as working code. The storm arrives
in 6 moves here so you can lose quickly while testing. The full game uses 20.

```python
# relay_slice.py  ·  three rooms of Storm Relay, as one complete game loop

MAX_MOVES = 6

# ----- State: everything the game remembers from one turn to the next -----
room = "lobby"
moves = 0
won = False
playing = True

print("STORM RELAY, three-room slice")
print(f"Get to the studio and broadcast before the storm arrives in {MAX_MOVES} moves.")

while playing:

    # 1. Show the state
    print()
    print(f"== {room.title()} ==")
    if room == "lobby":
        print("Exits: north.")
    elif room == "hallway":
        print("Exits: south, west.")
    elif room == "studio":
        print("A transmitter hums. Exits: east.")

    # 2. Read one command
    command = input("> ").strip().lower()

    # 3. Update the state
    if command == "north" and room == "lobby":
        room = "hallway"
        moves = moves + 1
    elif command == "south" and room == "hallway":
        room = "lobby"
        moves = moves + 1
    elif command == "west" and room == "hallway":
        room = "studio"
        moves = moves + 1
    elif command == "east" and room == "studio":
        room = "hallway"
        moves = moves + 1
    elif command == "broadcast" and room == "studio":
        print("The needle jumps. You are on the air.")
        won = True
        playing = False
    elif command == "quit":
        print("You leave the station to the storm.")
        playing = False
    else:
        print("You cannot do that here.")

    # 4. Check for a loss
    if playing and moves == MAX_MOVES:
        print("Thunder cracks overhead. The storm has reached the ridge.")
        playing = False

# ----- The loop has ended. The state says how. -----
print()
if won:
    print(f"YOU WIN in {moves} moves.")
else:
    print("GAME OVER")
```

Typing `north`, `west`, `broadcast`:

```
STORM RELAY, three-room slice
Get to the studio and broadcast before the storm arrives in 6 moves.

== Lobby ==
Exits: north.
> north

== Hallway ==
Exits: south, west.
> west

== Studio ==
A transmitter hums. Exits: east.
> broadcast
The needle jumps. You are on the air.

YOU WIN in 2 moves.
```

**Match it to your model.** The four state variables are the State box on your IPO chart. The `while`
is the diamond with the arrow back up. The four numbered comments are the four steps. The report after
the loop is the End oval. If your pseudocode and your code do not line up this closely, one of them is
wrong, and it is cheaper to find out now.

---

## Worked example 2: losing, and why step 4 checks `playing` first

Typing `north`, `south`, `north`, `dance`, `south`, `north`, `south`. The end of that run:

```
== Lobby ==
Exits: north.
> north

== Hallway ==
Exits: south, west.
> south
Thunder cracks overhead. The storm has reached the ridge.

GAME OVER
```

Six real moves. `dance` did not count, because only the four movement branches add to `moves`.

**Why `if playing and moves == MAX_MOVES`?** Imagine you broadcast on the exact move the storm arrives.
The broadcast branch already set `playing` to False and `won` to True. Without the `playing and` check,
step 4 would still print the storm message, and the player would read "you are on the air" and "the storm
has reached the ridge" on the same turn. Checking `playing` first means **the first ending wins.**

---

## Worked example 3: setting `playing` to False does not stop this turn

This surprises almost everybody, so prove it to yourself.

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

`playing = False` does **not** jump out of the loop. The `while` checks its condition only at the top.
Every line below the assignment in the same pass still runs. That is Thursday's rule, and in a game
it matters every turn: **after you set `playing` to False, ask what else still runs this turn.**

This is the failure mode behind a player who dies and then wins on the same turn, or who quits and then
walks into another room. Read the rest of your loop body every time you end the game from inside it.

---

## The wrong version: the win that says GAME OVER

Remove one line from worked example 1, the `won = True` in the broadcast branch:

```python
    elif command == "broadcast" and room == "studio":
        print("The needle jumps. You are on the air.")
        playing = False
```

Typing `north`, `west`, `broadcast`, the end of the run:

```
== Studio ==
A transmitter hums. Exits: east.
> broadcast
The needle jumps. You are on the air.

GAME OVER
```

**No error. The player won and the program says GAME OVER.**

The loop ended correctly, because `playing` became False. But the report after the loop does not read
`playing`. It reads `won`, and nobody changed `won`. Stopping the loop and recording **why** it stopped
are two separate pieces of state, and the code updated only one.

The same bug in the other direction is worse: a lose branch that sets `playing = False` and forgets that
`won` might already be True from an earlier turn. **Every branch that ends the game must set every flag the
ending depends on.** When you add a new way to win or lose, trace it all the way to the final report.

### The mistakes that do crash

A state variable used before it is set:

```
NameError: name 'moves' is not defined
```

Every state variable gets a value **above** the `while`. If you set `moves = 0` inside the loop, it resets
every turn and the storm never comes, which does not crash and is worse.

A script of commands that runs out before the game ends. When you test by piping commands into the game,
and the game is still asking after the last one:

```
EOFError: EOF when reading a line
```

That means your test script did not reach an ending. The game is fine. The script is short.

---

## Why the wrong version is tempting

**The ending text is already printed.** "You are on the air" is on the screen, so the branch feels done.
The report at the bottom is thirty lines away and out of sight.

**The loop did stop.** You tested that the game ends, and it does. You did not test that it ends with the
right message, because stopping felt like the hard part.

**One flag feels like enough.** It is, until you have two endings. A text adventure always has two.

---

## Checklist for your own game loop

- [ ] Every state variable is set above the `while`, and is on your IPO chart
- [ ] Each turn shows the state, reads one command, updates, and checks for an ending
- [ ] Every branch that ends the game sets `playing` to False **and** records why
- [ ] After setting `playing` to False, nothing below it in the same turn contradicts the ending
- [ ] The report after the loop reads the state and prints the right ending
- [ ] You have played to a win, played to a loss, and quit, and read all three endings

---

## Vocabulary

| Term | What it means |
|---|---|
| **Game loop** | A `while` loop that shows the state, reads a command, updates the state, and checks for an ending, every turn. |
| **State** | Every value a program remembers from one turn to the next. |
| **State variable** | One of those values, set before the loop and changed inside it. |
| **Flag** | A `bool` that records a yes-or-no fact, such as `playing` or `won`. |
| **Win state** | A combination of state values that ends the game in a win. |
| **Lose state** | A combination of state values that ends the game in a loss. |
| **Turn** | One pass through the game loop. |
| **`EOFError`** | Python ran out of input while `input()` was waiting. Common when a test script ends too soon. |

---

## Self-check

**Question 1.** List the state variables in this loop and say which one the `while` line reads and which
one the final report reads.

```python
lives = 3
coins = 0
alive = True
while alive:
    command = input("> ")
    if command == "coin":
        coins = coins + 1
    elif command == "spike":
        lives = lives - 1
    if lives == 0:
        alive = False
print(f"Final coins: {coins}")
```

**Question 2.** A player types `broadcast` in the studio on the same turn the storm arrives. In worked example
1, which ending does the player see, and which line makes that happen?

**Question 3.** This game loop runs forever when the player reaches the exit. Find the bug.

```python
room = "hall"
escaped = False
while not escaped:
    command = input("> ")
    if command == "out" and room == "hall":
        print("You push the door open and step outside.")
        room = "outside"
print("You escaped.")
```

---

### Answers

**1.** The state variables are `lives`, `coins`, and `alive`. The `while` line reads `alive`. The final report
reads `coins`. `lives` is state too: it is remembered between turns and it decides when `alive` changes.

**2.** The player sees the win. The broadcast branch sets `won = True` and `playing = False`. Step 4 begins with
`if playing and ...`, and `playing` is already False, so the storm message never prints and the report reads `won`.
In worked example 1, a broadcast does not add to `moves` at all, so the storm cannot arrive on that turn anyway. The
`playing and` check protects you on the day somebody adds a move cost to broadcasting.

**3.** The loop reads `escaped`, and nothing ever sets it to True. The branch changes `room` and prints the message,
then the loop checks `not escaped`, which is still True, so it asks for another command forever. Add
`escaped = True` inside the `if`. This is the same shape as today's wrong version: the ending changed one piece of
state and forgot the one the loop depends on.
