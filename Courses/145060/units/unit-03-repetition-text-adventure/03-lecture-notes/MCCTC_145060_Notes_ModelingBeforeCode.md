# Lecture Notes: Modeling Before Code
## 145060 Programming · Unit 3 · Week 6 · Wednesday, October 14

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W06_ModelingBeforeCode.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W06_ModelingBeforeCode.pptx)

If you missed class, you can learn this concept from this file alone. You need paper, or a
drawing tool, for this one. **Today you do not write Python.** That is the lesson, not a gap
in it.

---

## Why this exists

Unit 3 builds a text adventure: rooms, a game loop, a way to win, and a way to lose. It is
the biggest program you have written, and it is the first one that runs over and over until
something tells it to stop.

A program that size has a failure mode your earlier programs did not. You start typing, it
grows, and three days in you discover that there is no way to lose, or that one room has no
exit, or that the game never ends. By then the fix means rewriting half of it.

Every one of those problems can be seen **on paper, before any code exists**, in about ten
minutes. That is what modeling is for. The syllabus requires your flowchart and pseudocode to
be produced **before** any adventure code is written, and outcome 5.1.3 on the WebXam is
"model the solution using graphic tools and pseudocode."

**Be honest with yourself about this.** Most students do not believe in modeling until it
saves them. Today's deliberate error is designed to show you the moment it would have.

---

## The concept in plain language

A **model** is a simplified picture of how a program will work, made in a form that is faster
to change than code. You will use four kinds. Each one answers a different question.

| Tool | The question it answers |
|---|---|
| **IPO chart** | What goes in, what happens to it, and what comes out? |
| **Flowchart** | In what order do things happen, and where does the path split or repeat? |
| **Pseudocode** | What are the steps, written precisely enough to turn into code line by line? |
| **Decision tree** | For one decision, which question comes next after each answer? |

You have already built two relatives of these. Your Decision Engine's nested conditions are a
**decision tree**. Last Wednesday's truth tables are a **logic table**, which 5.1.3 also lists.

The world you model today is the class text adventure, **Storm Relay**: a storm is coming, and
you have a limited number of moves to get an old radio transmitter on the air.

---

## Tool 1: the IPO chart

**I**nput, **P**rocess, **O**utput. Three columns. Fill them before anything else, because a
value you forget to list here becomes a crash later.

For one turn of a three-room slice of Storm Relay:

| Input | Process | Output |
|---|---|---|
| The command the player types | Clean the command | The description of the current room |
| | Decide whether the command is a move, a broadcast, a quit, or unknown | A message when a move is blocked |
| | For a move: find the destination from the current room, update the room, add 1 to moves | A thunder warning as the storm gets close |
| | Check whether moves has reached the storm limit | The win message or the lose message |
| | For a broadcast: check the player is in the studio | |

**Also list what the program remembers between turns.** An IPO chart for a game loop needs a
fourth list, sometimes called **state**:

```
STATE (remembered from one turn to the next)
  room       starts as "lobby"
  moves      starts as 0
  playing    starts as True
```

If a value is used in the Process column and it is not an Input and not in State, **it does not
exist**. Hold that thought until the wrong version below.

---

## Tool 2: the flowchart

A flowchart draws the order of steps. Four shapes carry almost everything:

| Shape | Means |
|---|---|
| **Oval** | Start or End |
| **Parallelogram** | Input or output: the player types, or the program prints |
| **Rectangle** | A process step: set a value, do arithmetic |
| **Diamond** | A decision, with one arrow out for each answer, labeled |

Arrows show what happens next. **An arrow that points back up to an earlier step is a loop.**

The game loop for the three-room slice, described shape by shape so you can draw it:

1. **Oval:** Start
2. **Rectangle:** set room to lobby, moves to 0, playing to True
3. **Diamond:** playing? **No** arrow goes to step 10. **Yes** arrow goes to step 4.
4. **Parallelogram:** show the room description
5. **Parallelogram:** read a command
6. **Diamond:** which command? Four labeled arrows: quit, a move, broadcast, anything else.
7. **Quit** path, **rectangle:** set playing to False. Arrow back to step 3.
8. **Move** path, **rectangle:** change room, add 1 to moves. Then **diamond:** moves equals the
   limit? **Yes:** print the storm message, set playing to False. Both answers arrow back to step 3.
9. **Broadcast** path, **diamond:** in the studio? **Yes:** print the win message, set playing to
   False. **No:** print "there is no transmitter here." Both arrow back to step 3. **Anything else**
   path: print "not a command," arrow back to step 3.
10. **Oval:** End, after printing GAME OVER

Two checks every game-loop flowchart must pass:

- **Every diamond has an arrow for every answer.** A diamond with one arrow out means one answer
  leads nowhere.
- **There is at least one path from inside the loop to End.** If every arrow leads back to step 3
  and nothing ever sets playing to False, the game can never finish. You will see what that does to
  a real program tomorrow.

---

## Tool 3: pseudocode

Pseudocode is the flowchart written as indented, precise English. It is not Python, so it does
not need exact syntax. It **does** need to be precise enough that each line becomes one or two
lines of code.

```
SET room TO "lobby"
SET moves TO 0
SET playing TO True
DISPLAY the intro

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

**Read it against the flowchart.** Every diamond is an `IF` or the `WHILE`. Every rectangle is a
`SET` or `ADD`. Every parallelogram is an `INPUT` or `DISPLAY`. If you can match each line to a
shape and each shape to a line, the two models agree.

`WHILE playing` means "repeat this indented block as long as playing is True." You have not written
a loop in Python yet. You do not need to, to model one. Tomorrow's lesson turns this exact line into
code.

---

## Tool 4: a decision tree for one decision

The flowchart's step 6 hides a second decision: for a **move**, where does it go? That depends on
two things, the room and the direction, and the next question depends on the first answer. That is
a decision tree.

```
Which room are you in?
├── lobby
│     └── direction north?  yes -> hallway    no -> blocked
├── hallway
│     ├── direction south?  yes -> lobby
│     ├── direction west?   yes -> studio
│     └── anything else     -> blocked
└── studio
      └── direction east?   yes -> hallway    no -> blocked
```

You know how to write this in Python already: an `if`/`elif` on the room, with an `if`/`elif` on the
direction nested inside each branch. Last Thursday's decision rule said to keep nesting exactly when
the next question depends on the answer, and it does here.

---

## The wrong version: code built from an incomplete model

Somebody skips the IPO chart and starts coding the full game. They remember that the basement is
dark and you need a flashlight, so they write the rule. They never listed the flashlight in State.

```python
room = "hallway"
command = input("> ").strip().lower()

if command == "down":
    if has_flashlight:
        print("Your flashlight finds the basement stairs.")
    else:
        print("You step into total darkness.")
```

Typing `down`:

```
    if has_flashlight:
       ^^^^^^^^^^^^^^
NameError: name 'has_flashlight' is not defined
```

The rule used a value that was never set. That is exactly the check from Tool 1: **used in Process,
not an Input, not in State, so it does not exist.** On paper, this is a missing row in a chart, and
you add it in ten seconds. In code, it is a crash that only happens when a player walks down the
stairs, which might be the forty-first thing somebody tries.

### The worse version, which does not crash

Now imagine the same author **did** set the flashlight, but their flowchart had no arrow for the case
where the player never picks it up. In code, that turns into a rule that quietly assumes the flashlight
is always found. The game runs. No error. And there is a path through it where the player can never win
and nothing tells them. You have seen that shape ten times across Units 1 and 2. A flowchart with a
dead-end diamond **is** that bug, drawn before it exists.

---

## Why skipping the model is tempting

**Typing feels like progress.** A page of code looks like work. A page of boxes looks like homework.
The code is usually further from done.

**Small programs did not need it.** Every program before today was short enough to hold in your head.
The text adventure is not, and it will grow for four units.

**The model gets thrown away.** It does not. Your flowchart becomes your README diagram, your pseudocode
becomes your comments, and your IPO chart becomes your test plan. None of that work is wasted.

**You can ask an AI to draw one.** You can, and 5.1.3 even lists AI as a modeling tool. The same rule as
every Gate 2 applies: you must be able to find the diamond with a missing arrow in a model somebody else
made. If you cannot, you are not ready to use one.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Model** | A simplified description of a program, faster to change than code. |
| **IPO chart** | A table of Inputs, Processes, and Outputs. |
| **State** | Values a program remembers from one turn to the next. |
| **Flowchart** | A diagram of steps and their order, using standard shapes. |
| **Decision symbol** | The diamond. One labeled arrow out for each possible answer. |
| **Pseudocode** | Precise, indented English describing steps, one step per line. |
| **Decision tree** | A model of one decision where each answer leads to the next question. |
| **Game loop** | The repeated cycle of showing the state, reading a command, and updating the state. |
| **Dead end** | A path in a model that never reaches End, or a diamond answer with no arrow. |

---

## Self-check

**Question 1.** A flowchart for a guessing game has a diamond labeled "guess is correct?" with only a
**Yes** arrow. What will the program built from it do when a guess is wrong, and what is missing from the
model?

**Question 2.** Write the IPO chart, including State, for this program: a vending machine takes a
two-letter code from the player, looks up the price, takes a number of quarters, and either delivers the
snack and says how much change is owed or says the money is not enough.

**Question 3.** Here is a line of pseudocode. Rewrite it so a classmate could turn it into Python without
asking you a question.

```
IF the player can win
    DISPLAY win
```

---

### Answers

**1.** The model does not say, which means the program's behavior is whatever the programmer happens to type.
Most likely a wrong guess reaches no branch and the program either does nothing or ends without a message.
The missing piece is a **No** arrow from the diamond, labeled, leading somewhere: usually back to asking for
another guess.

**2.** One reasonable chart:

| Input | Process | Output |
|---|---|---|
| Two-letter snack code | Clean the code and find its price | The price of the snack |
| Number of quarters | Multiply quarters by 25 to get cents | "Here is your snack" and the change owed |
| | Compare cents to the price | "Not enough money" and the amount short |
| | If enough, subtract price from cents for change | |

State: none is needed for one purchase. If the machine tracks how many snacks remain, that count is State.
Full credit requires both inputs, the conversion from quarters to cents, a comparison, and both outcomes.

**3.** One precise version:

```
IF room is "studio" AND power_on is True AND frequency equals EMERGENCY_FREQUENCY
    DISPLAY "You are on the air."
    SET won TO True
    SET playing TO False
```

Any version earns credit if it names the exact conditions, uses values that are listed in State or
Inputs, and says what changes afterward. "The player can win" is not a condition. It is a wish.
