# Lab U3-02: Locked Out
## 145060 Programming · Unit 3 · Week 7

**Gate:** 3 (open tooling). **Duration:** two Build 1 blocks, 35 minutes each. Part 1 on
Tuesday, October 20. Part 2 on Wednesday, October 21. **Competencies:** 5.3.6 (repetition
control structures), 5.3.8 (nested structures), 5.1.3 (model the solution), 5.5.1 (data
validation, first taste), 5.4.7 (debug logic errors).

**This lab builds directly toward your text adventure v1.** It is the same pattern in a tiny,
different world. Do not submit it as your v1, and do not copy its rooms into your v1. Copy the
**shape**.

---

## The scenario

Practice ran late, nobody is home, and the front door is locked. Your phone is almost dead and
has enough battery for a few more moves before you cannot call anyone. Somewhere around the house
is a way in.

## What you will build

A three-location game with a game loop, state variables, a win, two ways to lose, and a keypad that
refuses badly typed codes without counting them as guesses.

---

## The world, as a model

Read this before you write any code. It is the model your code must match.

```
            shed
             |  north / south
porch --- backyard
   east / west
```

| State variable | Starts as | Changes when |
|---|---|---|
| `room` | `"porch"` | You move |
| `moves` | `0` | You move to a different location |
| `has_note` | `False` | You `take` on the porch |
| `has_key` | `False` | You enter the right `code` in the shed |
| `wrong_codes` | `0` | You enter a well-formed wrong code (Part 2) |
| `won` | `False` | You `unlock` on the porch with the key |
| `playing` | `True` | Any ending |

| Ending | Condition |
|---|---|
| **Win** | `unlock` on the porch while carrying the key |
| **Lose: battery** | `moves` reaches `MAX_MOVES`, which is 8 |
| **Lose: lockbox** | 3 well-formed wrong codes (Part 2) |
| **Quit** | `quit` |

The sticky note under the flowerpot says the shed code is `2718`.

---

## Starter code

Create `locked_out.py` and type this in. It runs. It does nothing useful.

```python
# locked_out.py
# A three-location game loop: find the spare key before your phone dies.
#
# This file runs right now. It does not do anything useful yet.

GAME_TITLE = "LOCKED OUT"
SHED_CODE = "2718"
MAX_MOVES = 8              # your phone battery lasts this many moves

print(GAME_TITLE)
print("=" * len(GAME_TITLE))
print("Practice ran late. Nobody is home and the front door is locked.")
print(f"Your phone has enough battery for {MAX_MOVES} moves.")

# TODO 1: Create the state variables: where you are, how many moves you
#         have made, what you are carrying, and whether the game is running.

# TODO 2: Write the game loop. Each pass shows the room, reads one command,
#         updates the state, and checks whether the game is over.

# TODO 3: After the loop, report whether you won.

print("The game loop is not written yet.")
```

Running it produces:

```
LOCKED OUT
==========
Practice ran late. Nobody is home and the front door is locked.
Your phone has enough battery for 8 moves.
The game loop is not written yet.
```

---

## Part 1: Tuesday, the game loop, steps 1 through 7

### Step 1. Starter running and committed
**Observable result:** five lines of output and a new commit.

### Step 2. State variables
Replace TODO 1 with every state variable from the model table except `wrong_codes`. Delete the last `print`.
**Observable result:** the program runs and prints the four intro lines only.

### Step 3. The loop and step 1 of each turn: show the state
Write `while playing:`. Inside it, print a heading with the room name and the battery left, then the description and exits for
the current room. Then read one command with `input("> ").strip().lower()`.
**Observable result:** the game shows the porch and waits for a command. Typing anything shows the porch again. Stop it with Ctrl+C.

### Step 4. Update the state: movement
Add the four movement branches from the map. Each one changes `room` and adds 1 to `moves`. Everything else prints
`You cannot do that here.`
**Observable result:** `east`, `north`, `south`, `west` walks you around the map and back. The battery goes down by 1 for each move.

### Step 5. Items and the win
Add `take` on the porch (sets `has_note`, prints the code), `code` in the shed (reads a code with `input()` and sets `has_key` if it
matches `SHED_CODE`), and `unlock` on the porch with the key (sets `won` and `playing`). Add `quit`.
**Observable result:** you can play from the porch to the key and back, and `unlock` ends the loop.

### Step 6. Check for a loss, and report after the loop
At the bottom of the loop body, end the game when `moves` reaches `MAX_MOVES`, but only if the game is still being played. After the
loop, print `YOU WIN` with the battery left, or `GAME OVER`.
**Observable result:** eight moves back and forth between porch and backyard prints a battery message and `GAME OVER`.

### Step 7. Prove all three endings, then commit
Create a file called `win.txt` with one command per line that wins the game, and `lose.txt` that loses on battery. Run them without typing:

```bash
python locked_out.py < win.txt
```

In PowerShell, use `cmd /c "python locked_out.py < win.txt"`. See "If it breaks" item 6 for why.

**Observable result:** `win.txt` ends with `YOU WIN`, `lose.txt` ends with `GAME OVER`, and typing `quit` by hand ends with `GAME OVER`.
Commit the game and both scripts.

### Acceptance criteria, Part 1
1. The loop shows, reads, updates, and checks, in that order, every turn
2. `win.txt` produces `YOU WIN. You got inside with 4 moves of battery left.` using the shortest route
3. Eight moves without winning ends with `GAME OVER`, and so does `quit`

---

## Part 2: Wednesday, input handling and the keypad, steps 8 through 13

### Step 8. Blocked moves cost nothing
Rewrite movement as a nested structure: if the command is a direction, work out a `destination` from the room and the direction, and only
move if there is one. Otherwise print `You cannot go west from here.` with the real direction.
**Observable result:** `west` on the porch prints the message and the battery does **not** go down.

### Step 9. Empty and unknown commands
An empty command prints `Type a command. Type help to see the list.` and uses `continue` to go straight to the next turn. An unknown word
prints `'dance' is not a command. Type help to see the list.` with the real word. Add `help`.
**Observable result:** pressing Enter, typing `dance`, and typing `  HELP ` each get a sensible response.

### Step 10. The keypad validation loop
Replace the single `input()` in the `code` branch with a `while True:` loop. Inside it:
- `cancel` leaves the keypad with `break`
- anything that is not exactly 4 digits prints `The keypad only takes 4 digits.` and asks again with `continue`
- a well-formed code is checked, and then `break` leaves the keypad

**Observable result:** `12`, `abcd`, and `27 18` are refused and asked again. `cancel` returns you to the shed.

### Step 11. Three wrong codes lose the game
Add `wrong_codes` to your state. A well-formed wrong code adds 1 and prints the tries left. The third one ends the game.
**Observable result:** `1111`, `2222`, `3333` ends with the lockbox message and `GAME OVER`. A badly typed code in between does **not**
use up a try.

### Step 12. Break it on purpose
Delete the `break` at the bottom of the keypad loop. Enter the right code. Write down what happened in a comment at the top of your file.
Put the `break` back.
**Observable result:** a comment recording that the keypad kept asking after the correct code.

### Step 13. Test scripts, README, commit
Add `lose_lockbox.txt`. Run all three scripts. Write a short README: how to play, how to run the scripts, and one known limitation you
actually observed. Commit and push.

### Acceptance criteria, Part 2
4. A blocked move costs no battery
5. No typed input of any kind crashes the game
6. Badly typed codes never count as wrong guesses, and 3 real wrong codes lose
7. Three test scripts, each reaching a different ending

---

## Acceptance criteria, full lab

- [ ] State variables match the model table
- [ ] Every ending sets `playing` to False, and the win also sets `won`
- [ ] The report after the loop prints the right ending for all four endings
- [ ] Blocked moves cost nothing
- [ ] No input crashes the game
- [ ] The keypad loop uses `break` and `continue` correctly
- [ ] `win.txt`, `lose.txt`, and `lose_lockbox.txt` each reach their ending
- [ ] Step 12 recorded in a comment
- [ ] README with a real known limitation
- [ ] Commits at the end of each part, pushed

---

## If it breaks

### 1. You typed `quit` and the game asked for another command

**Cause:** the `quit` branch prints a message but never sets `playing = False`. The loop only checks `playing`, at the top.

### 2. You won and it said `GAME OVER`

**Cause:** the `unlock` branch set `playing = False` but not `won = True`. The report after the loop reads `won`.

### 3. The game ends in a test script with this:

```
EOFError: EOF when reading a line
```

**Cause:** your script ran out of commands while the game was still waiting for one. The script never reached an ending. Count your
moves against the map, or add a command.

### 4. The keypad keeps asking after the right code

```
Lockbox code, 4 digits, or cancel: 2718
The lockbox clicks open. You take the spare key.
Lockbox code, 4 digits, or cancel: 2718
The lockbox clicks open. You take the spare key.
```

**Cause:** there is no `break` after the code is checked, so the `while True:` loop goes around again. This is step 12.

### 5. `ValueError: invalid literal for int() with base 10: 'abcd'`

```
    if int(entered) < 1000 or int(entered) > 9999:
       ~~~^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'abcd'
```

**Cause:** the code was converted to a number before anything checked that it is made of digits. You do not need `int()` for the keypad at
all. Compare the text to `SHED_CODE`, and check `.isdecimal()` and `len()` first.

### 6. In PowerShell, the first command of your script is "not a command"

With `win.txt`, whose first line is `take`, the first response is:

```
> 'take' is not a command. Type help to see the list.
```

It looks impossible, because `take` is a command. There is an invisible character between the first quote mark and the `t`. **Cause:** when you pipe a file into Python with `Get-Content win.txt | python locked_out.py`, Windows
PowerShell can put an invisible marker character in front of the first line, so your game receives something that looks like your command and
is not. Use `cmd /c "python locked_out.py < win.txt"` instead, or run the script from Git Bash with `python locked_out.py < win.txt`.

### Not an error: the battery goes down when you walk into a wall

That is Part 1 behaving as written. Step 8 fixes it.

---

## Stretch goal

Make the note matter: the keypad refuses to accept any code until the player has taken the note. Then answer in your README: is that a better game
or a worse one, and why? There is no single right answer.

---

## Submission checklist

- [ ] All three scripts run to their endings
- [ ] Played by hand to a win at least once
- [ ] No crash on an empty line, a random word, or a badly typed code
- [ ] Step 12 comment present
- [ ] README with a real known limitation
- [ ] Pushed, `git status` clean
- [ ] AI usage log updated if a model was used at any point

---

# Extended Lab Options

All four assess the same competencies, 5.3.6 and 5.3.8, on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 15 minutes into Part 1, still no working `while` loop, or state variables created inside the loop | SCAFFOLDED |
| Loop works, asking about specific messages or map details | STANDARD |
| Part 1 finished with all three endings in 20 minutes, or asking how to make a room change after you visit it | EXTENDED |
| Says games are pointless, or asks what this has to do with a real job | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** all state variables are given, and the loop is given with the "show the state" step already written.
- **Part 1:** the student writes the four movement branches, `take`, `code`, `unlock`, `quit`, the loss check, and the report. `win.txt` is given.
- **Part 2:** step 8's nested movement is given. The student writes steps 9 through 12. Step 12 stays.
- **Checkpoints:** show your terminal after step 5 and after step 11.

**Acceptance criteria:** win, battery loss, lockbox loss, and quit all reach the right report; no crash on bad input; badly typed codes do not count;
step 12 recorded.

**Grading:** same 100-point scale, Requirements Fit judged against this list. A complete SCAFFOLDED submission earns what a complete STANDARD submission
earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a requirement that needs something not taught.

**Added requirement.** Make the battery drain faster when it is cold. Every **third** move costs 2 battery instead of 1. The display must show the real battery
left, and the loss check must still fire at the right moment, never letting the battery display go below zero.

**Hint, not the answer.** You need to know when a number is a multiple of 3. Python has an arithmetic operator that gives the **remainder** of a division.
Find it in the official tutorial's section on using Python as a calculator, `https://docs.python.org/3/tutorial/introduction.html`, and ask yourself what
the remainder is when a move number is a multiple of 3.

**Second added requirement.** In your README, list the exact move numbers on which the battery changes by 2, and show that your `lose.txt` script still loses on
the correct move.

**The honest warning:** once a move can cost 2, the battery can jump from 1 straight to -1 and skip the exact number your loss check compares against. With a
battery of 8 it happens to land exactly on 0, so a check written with `==` works by luck. Change `MAX_MOVES` to 7 and test again. If your check uses `==`, the game
will not crash. It will keep playing on negative battery. Documenting that earns more than never hitting it.

**Acceptance criteria:** all STANDARD criteria, plus the cold-battery rule, plus a loss check that still fires with `MAX_MOVES` set to 7, plus the README list.

---

## APPLIED

**For the student who says games are not a real job.** Same loop, and the house was never the point.

**Changed scenario.** Build a text interface for a real machine that waits for commands until someone finishes: a school snack vending machine, a library self-checkout,
a bike rental kiosk, or a phone menu for a pizza shop. It must have at least three screens or states the user moves between, a way to finish successfully, a way to fail
or time out, and one validated input loop, such as a PIN or a quantity.

**The extra requirement that makes it the same lab.** Before any code, write the model table from this handout for your machine: every state variable, what it starts as,
and what changes it, and every ending with its condition. Commit the table before the code.

**Acceptance criteria:** all STANDARD criteria applied to the machine, plus the model table committed before the first code commit.

**Grading:** same scale. Requirements Fit is judged against the student's own model table, which is harder than the standard version, because the student has to design
the endings as well as build them.
