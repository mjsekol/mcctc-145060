# Lab U3-03: Game Night Leaderboard
## 145060 Programming · Unit 3 · Week 8

**Gate:** 3 (open tooling). **Duration:** one Build 1 block, 35 minutes, Week 8, Monday.
**Competencies:** 5.1.2 (algorithms and data structures in information processing), 5.3.6
(repetition control structures), 5.5.7 (read inputs from a data file), 5.4.7 (debug logic errors).

---

## The scenario

Every Friday your friends play three games and somebody writes every round's score into a text file.
Every Saturday the group chat argues about who actually won, and nobody wants to scroll through the file
to prove it. You are going to settle it with a program.

## What you will build

A program that reads one night of results and reports the number of rounds, the total points, the high
score and who got it, the low score and who got it, and the first big round for any player you ask about.

---

## The data

Copy [`game_night.txt`](fixtures/game_night.txt) into the same folder as your program. It is fixed width,
one round per line:

```
NovaK         Kart Chaos       820
pixelpaz      Kart Chaos      1140
DJ_Tofu       Kart Chaos       655
ravenmoon     Tile Drop       1320
NovaK         Tile Drop        980
DJ_Tofu       Tile Drop       1015
pixelpaz      Word Sprint      410
ravenmoon     Word Sprint      575
NovaK         Word Sprint     1205
DJ_Tofu       Kart Chaos        90
ravenmoon     Kart Chaos       760
pixelpaz      Tile Drop       1480
```

| Positions | Field |
|---|---|
| 0-13 | Player tag |
| 14-29 | Game |
| 30-33 | Score |

---

## Starter code

Create `leaderboard.py` and type this in. It runs. It does nothing useful.

```python
# leaderboard.py
# Reads a night of game results and answers questions about it.
#
# game_night.txt is fixed width, one round per line:
#   positions 0-13   player tag
#   positions 14-29  game
#   positions 30-33  score
#
# This file runs right now. It does not do anything useful yet.

RESULTS_FILE = "game_night.txt"

print("GAME NIGHT LEADERBOARD")
print("======================")

results = open(RESULTS_FILE)
first_line = results.readline()
results.close()

# Look at one raw record before you write a loop over all of them.
print(repr(first_line))

# TODO 1: Count the rounds and add up every score.
# TODO 2: Find the highest score and who scored it.
# TODO 3: Find the lowest score and who scored it.
# TODO 4: Ask for a player tag. Find the first round where that player scored
#         1000 or more, stop reading as soon as you find it, and report how
#         many lines you read.
```

Running it from the folder that holds `game_night.txt` produces:

```
GAME NIGHT LEADERBOARD
======================
'NovaK         Kart Chaos       820\n'
```

---

## Steps

### Step 1. Starter running and committed
**Observable result:** the raw first record, with its spaces and `\n` visible. Commit.

### Step 2. Count and total, in one loop
Replace TODO 1 with a sentinel loop: read a line, and keep going while the line is not `""`. Count each round and add each score.
Remove the `repr` print when you are done.
**Observable result:** 12 rounds and a total of 10450 points. Check the total against the file with a calculator once.

### Step 3. High score, in the same loop
Keep the highest score seen so far **and** the player it belongs to. Do not write a second loop for this.
**Observable result:** a high score of 1480 by pixelpaz.

### Step 4. Low score, the wrong way on purpose
In the same loop, keep the lowest score and its player, starting the lowest score at `0` and the player at `""`, the same way you started
the high score. Run it. Write the exact line it printed in a comment at the top of your file.
**Observable result:** a comment recording a low score of 0 with no player name, and no error message.

### Step 5. Low score, fixed
Read the **first** record before the loop and use it as the starting value for every accumulator: rounds, total, high, and low. Then loop over
the rest.
**Observable result:** a low score of 90 by DJ_Tofu, with rounds and total still 12 and 10450. Commit.

### Step 6. The search
Replace TODO 4. Ask for a player tag, ignoring capitals and spaces. Open the file again, and loop until you find the first round where that player
scored 1000 or more. **Stop reading with `break` as soon as you find it.** Count the lines you read. Report the score, the game, and the line count,
or say there was no such round.
**Observable result:** `NovaK` finds 1205 in Word Sprint after reading 9 lines. `pixelpaz` finds 1140 after 2 lines. `Sam` reads all 12 lines and finds
nothing.

### Step 7. Explain the algorithms
At the bottom of your file, write a comment block called `Algorithms` that answers:
1. Which algorithm from the lecture notes table does each of your four answers use?
2. Why can the search stop early, but the high score cannot?
3. If `game_night.txt` were sorted from highest score to lowest, which of your answers could be found by reading one line, and which would still need
   the whole file?

**Observable result:** three answers, in your own words. Commit and push.

---

## Acceptance criteria

- [ ] Runs with no traceback from the folder holding `game_night.txt`
- [ ] Rounds 12, total 10450, high 1480 by pixelpaz, low 90 by DJ_Tofu
- [ ] Rounds, total, high, and low all come from **one** pass through the file
- [ ] The search stops at the first match and reports the lines it read
- [ ] The search ignores capitals: `novak` and `NovaK` give the same answer
- [ ] Step 4's silent wrong answer is recorded in a comment
- [ ] The `Algorithms` comment answers all three questions
- [ ] At least two commits

---

## If it breaks

### 1. `FileNotFoundError: [Errno 2] No such file or directory: 'game_night.txt'`

**Cause:** Python looks for the file in the folder you **ran** the program from, not the folder the program lives in. This is Week 4's lesson.
`cd` into the folder that holds both files, or copy the data file next to your program.

### 2. `ValueError: invalid literal for int() with base 10: ''`

```
    score = int(line[30:34])
ValueError: invalid literal for int() with base 10: ''
```

**Cause:** your copy of `game_night.txt` has an extra empty line at the end, and that line is `"\n"`, not `""`, so the loop tries to read a score from
it. Delete the blank last line, or skip lines whose stripped text is empty.

### 3. Every score is about a tenth of what it should be

```
Total points:  1043
High score:    148 by pixelpaz
```

**Cause:** the slice `line[30:33]` stops **before** position 33 and drops the last digit. Up to but not including: the score needs `line[30:34]`.
No error appears, which is why you check totals against the file.

### 4. `Low score: 0 by` with a blank name

**Cause:** the lowest score started at 0, and no real score is lower than 0, so nothing ever replaced it. This is step 4, and step 5 is the fix.

### 5. The search finds nothing for `NovaK`

**Cause:** usually the comparison. The tag field is 14 characters wide, so `line[0:14]` is `"NovaK         "` with trailing spaces. `.strip()` it,
and `.lower()` both sides.

---

## Stretch goal

Report the **total points per game**, for all three games, in a single pass through the file, without lists. Then write one sentence in your
`Algorithms` comment explaining what would make this painful if there were thirty games instead of three. That pain is what Unit 5's data structures
fix.

---

## Submission checklist

- [ ] Output checked against the numbers in the acceptance criteria
- [ ] Search tested with a player who has a big round, one who does not, and a tag that is not in the file
- [ ] Step 4 comment and `Algorithms` comment present
- [ ] Pushed, `git status` clean
- [ ] AI usage log updated if a model was used at any point

---

# Extended Lab Options

All four assess the same competencies, 5.1.2 and 5.3.6, on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 10 minutes, still no loop that reaches the end of the file, or slicing the wrong positions | SCAFFOLDED |
| Loop works, asking about the search or the comment questions | STANDARD |
| Steps 2 through 5 done in 15 minutes, or asking how to rank all four players | EXTENDED |
| Says they never play games with friends, or asks what this is for | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the sentinel loop is given, reading every line and printing each score, with empty `# count here` and `# total here` comments inside it.
- **Steps:** step 3 is kept, step 4 is kept, step 5 gives the "read the first record" lines. Step 6 searches for a tag with no score threshold, which
  removes the compound condition.
- **Step 7:** answer question 1 only.
- **Checkpoints:** show your terminal after step 2 and after step 5.

**Acceptance criteria:** rounds, total, high, and low correct; step 4 recorded; search stops at the first match; question 1 answered.

**Grading:** same 100-point scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a requirement that needs something not taught.

**Added requirement.** Print each player's **total** points for the night, one line per player, in a single pass through the file, **without** writing
the four player tags into your code. The program must still work if a fifth player shows up next Friday.

**Hint, not the answer.** With only variables, this cannot be done for players you do not know in advance. You need a data structure that maps a name
to a number. Read the section on dictionaries in the official Python tutorial, `https://docs.python.org/3/tutorial/datastructures.html`, and look for how to
add to a value that may not exist yet.

**Second added requirement.** In your `Algorithms` comment, explain why this requirement was impossible with the tools from Units 1 through 3, and name the
data structure that made it possible.

**The honest warning:** a dictionary is a Unit 5 tool. You must be able to explain every line of your EXTENDED code, and "the tutorial said so" is not an
explanation. If you cannot explain it, stop at STANDARD.

**Acceptance criteria:** all STANDARD criteria, plus per-player totals that work with an unknown fifth player, plus the explanation.

---

## APPLIED

**For the student who says this is only about games.** Same algorithms, completely different data.

**Changed scenario.** Make a fixed-width file of at least 10 records from something real in your life that you can share publicly: minutes of practice per day
for a month, songs and plays from your own listening, laps and times from a meet you ran, hours worked per shift at a job. No other person's information.

**What you build.** A program that answers the same four kinds of question about your data: a count, a total, a maximum or minimum with its label, and a search
that stops early.

**The extra requirement that makes it the same lab.** Your file starts with a comment table of positions and fields, exactly like the one in this handout, and your
`Algorithms` comment answers all three step 7 questions about **your** data.

**Acceptance criteria:** all STANDARD criteria applied to the student's file, plus the positions table, plus all three answers.

**Grading:** same scale. Requirements Fit is judged against the student's own positions table.
