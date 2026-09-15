# Project: Text Adventure Version 3
## 145060 Programming · Unit 5 · Due Friday, November 20, 2026

**Mode:** solo. **Gate:** 3, full tooling, decision log required. **Periods:** seven Build 2
blocks across Weeks 10 and 11, plus Friday flex time.

**Competencies:** 5.3.11 (access data repositories), 5.5.7 (read inputs from a data file),
5.1.5 (data management through programming languages), 5.2.2 (scope of data, including
arrays), 5.5.3 (operating system calls: file paths), 5.3.10 (error handling), 5.5.1 (data
validation), 5.4.4 and 5.4.5 (define test cases and test against them).

---

## The brief

Two people have been playing your version 2. Read what they said, because they said it to you.

> **From your playtester:**
> I got all the way to the end. Flashlight, the thing on the roof, the whole route. Three moves
> from winning and the bell rang. Tomorrow I start from the very first room again, so honestly I
> probably will not. Can it remember where I was? And if I break something, do not let it
> eat my progress.
>
> **From your friend who writes:**
> I wrote four new rooms for your game in my notes app. I tried to add them myself and I could
> not find where the rooms even are in the code, and when I changed one word the game would not
> start. I do not want to learn Python. I want to open a file, type a room, and have it be in the
> game. And if I mess up a comma, tell me where, instead of crashing.

**That is the brief.** Two people, two different complaints. Neither one mentions lists,
dictionaries, sets, or JSON. Turning what they said into requirements is your job.

**Build from your own version 2.** Your world, your rooms, your items, your win and lose
conditions. Version 3 must still be recognizably the same game. The course's reference game,
Storm Relay, shows one way to do this; do not copy it. Your world is yours.

---

## Requirements

### Technical

1. **The world lives in a JSON file**, `world.json`, next to your program. Every room's name,
   description, exits, and starting items come from the file. Your code decides how the game works;
   the file describes the place.
2. **The program finds `world.json` no matter which folder you run it from.** Build the path from the
   location of your `.py` file.
3. **The world is checked at startup.** If `world.json` is missing, is not valid JSON, or has an exit
   leading to a room that does not exist, the game prints one clear message saying what and where,
   and exits without a traceback.
4. **Collections, each chosen on purpose.** At minimum: rooms looked up in a **dictionary**, the
   inventory in a **list** (or another structure you justify), and the rooms visited in a **set**. A
   comment above each says why that structure fits.
5. **No global variables change during play.** Everything that changes lives in one state dictionary
   that functions receive and return or modify. Version 2's `global` inventory flags are gone.
6. **`save` writes the game to a JSON file**, and **`load` reads it back**, restoring room, inventory,
   visited rooms, move count, and anything else your game needs to continue exactly where it was.
7. **Three different bad saves, three different messages**, and the current game unchanged after each:
   - no save file yet
   - a damaged file that is not valid JSON
   - a file that is valid JSON but describes an impossible game, such as a room that does not exist or
     a move count that is not a whole number
8. **The game ends by printing how many rooms were explored**, out of how many exist.
9. **Your version 2 win and lose paths still work.**
10. **Tests.** Update your version 2 tests so they pass, and add at least five new ones: a save followed by
    a load that restores the state, each of the three bad saves, and a broken `world.json`. Every test that
    saves must work in a temporary folder or clean up after itself.

### Repository

```
text-adventure/
  v2/                  unchanged from Unit 4
  v3/
    adventure.py
    world.json
    test_adventure.py
    README.md
  decision-log.md      add Unit 5 entries
  ai-usage-log.md
  .gitignore           ignores savegame.json and __pycache__
```

### README for v3, six sections

1. **What changed from v2**, in plain language, for someone who played v2.
2. **Structures I chose**: a table with each piece of data, the structure, and why.
3. **How to run it and how to test it.**
4. **A real run** that includes `save`, walking away, and `load`.
5. **Bad saves**: a table of each bad save you tested and the exact message.
6. **Known limitations**: at least two, observed, not guessed.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use classes | They are Unit 7. Version 4 is where the game becomes objects. Code you cannot explain fails the course standard. |
| Use a database, `pickle`, or any third-party package | JSON is readable by your writer friend and by you. `pickle` files are not human-readable, and loading a `pickle` from someone else can run code they wrote. |
| Move the rules into `world.json` | The file describes the place. Which room is dark and what wins the game stay in code, so a typo in the world file cannot change how the game is won. |
| Load a save without checking it | A save file is data from outside the program. The playtester might edit it, and so might you while testing. |
| Ship a save file in the repository | It is personal progress, it changes every run, and a stale save in the repository makes tests pass for the wrong reason. |

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Mon Nov 9, end of Build 2 | The two complaints restated as requirements in your own words, in `decision-log.md` |
| **Measure** | Mon Nov 9, end of Build 2 | A list of every place your v2 hardcodes a room, an exit, or an item, with line numbers |
| **Analyze** | Tue Nov 10, end of Build 2 | Your world drawn as nested dictionaries on paper or in a comment, before code, and a first decision log entry naming each structure you chose |
| **Improve** | Wed Nov 11 to Tue Nov 17 | Build it, in the order of the milestone schedule |
| **Control** | Fri Nov 20, end of Build 2 | Tests passing, README complete, three bad saves demonstrated |

**Measure is the checkpoint that saves the most time.** Students who skip the list of hardcoded places
find the last one on Thursday night, when a room they "moved" still has a description inside an `if`.

---

## Milestone schedule, against actual class days

| Day | Build 2 goal |
|---|---|
| Mon Nov 9 | Define and Measure. No new code. |
| Tue Nov 10 | Analyze. Rooms and exits as a dictionary in code. `find_exit` deleted. |
| Wed Nov 11 | Inventory as a list, visited rooms as a set. Every v2 `global` gone. |
| Thu Nov 12 | All changing values in one state dictionary. Items left in each room as a dictionary of lists. v2 tests pass again. |
| Fri Nov 13 | Problem Drop 2 runs in Build 2. No v3 time unless you finish the drop early. |
| Mon Nov 16 | World data moved into `world.json`, loaded and checked at startup. |
| Tue Nov 17 | `save` and `load`, with all three bad-save messages. |
| Wed Nov 18, Thu Nov 19 | Build 2 belongs to the data pipeline project. Fix v3 bugs in flex time only. |
| Fri Nov 20 | New tests, README, decision log, final push. **Due at the end of the block.** |

---

## Three worked scope examples

These are here so you can calibrate. **Do not build any of these.** They are occupied.

### Too small

> Moves the room descriptions into `world.json` and nothing else. The exits are still `if`
> statements. Adds a `save` command that writes the room name to a text file. `load` crashes if the
> file is missing.

The writer still cannot add a room, because exits live in code. The save loses the inventory. The
playtester's second request, "do not eat my progress," is not addressed at all.

### About right

> **Night Shift at the Aquarium.** The v2 game with eight rooms, now in `world.json`, validated at
> startup. Inventory is a list, visited tanks are a set, and everything else is in one state dictionary.
> `save` and `load` work, with three distinct messages, and loading a save that names a room like
> `shark_tank_2` that is not in the world prints which room it was. The ending says "Tanks explored: 6 of 8."
> Nine new tests. The README's known limitations say that a save made before the writer adds a room still
> loads, but the new room's items appear as if never taken.

Every requirement, each structure justified, and a limitation that shows the student thought about how the
two complaints interact.

### Too big

> Multiple save slots with names, an autosave every five moves, a map editor that writes `world.json`, a
> scrolling colored text interface, and a hint system that tracks which puzzles the player has tried.

Each piece is reasonable. Together they are two weeks of work, and the parts that are graded, validation and
bad saves, get squeezed. **The calibration question:** can you name the three bad-save messages your game
prints before you build anything else? If not, the extras are hiding the requirements.

---

## The five-minute demo

Friday, November 20, in pairs, with your instructor visiting. Everyone demos to a partner; some demo to the
room.

1. **Play for 60 seconds, then `save`.** Walk somewhere else. **`load`.** Show that you are back. (90 seconds)
2. **Break it three ways, on purpose.** Delete the save and load. Damage the save and load. Edit the save to
   an impossible value and load. Read each message. (90 seconds)
3. **Open `world.json` and change one exit to a room that does not exist.** Run the game. Show the message.
   Put it back. (45 seconds)
4. **One decision.** Point at one structure in your code and say why you chose it over the other two. (45
   seconds)
5. **Questions.** (30 seconds)

**Step 4 is the graded part of the demo.** Anybody can show a save working. The decision is the evidence that
you built it.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | World loads from JSON and is validated. Save and load restore everything. Three distinct bad-save messages, game unchanged after each. v2 win and lose still work. |
| **Code Quality** | 20 | A dictionary, list, and set each used where they fit, with a comment saying why. No globals changing during play. No bare `except`. Load checks every value before using any. |
| **Documentation** | 20 | All six README sections. The bad-save table copied from real runs. Decision log entries for the structures and for what stays in code. |
| **Process** | 15 | DMAIC checkpoints on time, especially Measure. Commits across both weeks, each saying why. At least five new tests. |
| **Demonstration** | 10 | The demo script, including breaking it three ways live, and one structure decision explained. |
| **Polish** | 10 | Messages a player understands. A `world.json` a non-programmer could edit, with `indent`. The save file readable. |

**The fastest way to lose Functionality points** is a load that crashes on a damaged file, or one that fails
halfway and leaves you in a room with somebody else's inventory.

---

## If you are stuck

**"I do not know where to start."** Measure. List every line of v2 that names a room or an item. That list is
your to-do list.

**"My world.json will not load."** Read the line and column in the error, then look for single quotes and
trailing commas. The Monday lecture notes show both.

**"Save works but load crashes on a set."** JSON has no set. Save it as a sorted list and turn it back into a set
when you load.

**"My v2 tests fail after the refactor."** Good, that is what they are for. Fix one test at a time. If a test
checks a v2 detail you deliberately changed, update the test and write down why in the decision log.

**"I want to add more rooms."** Add them to `world.json` after every requirement works. That is exactly what the
writer asked for, and it proves your validation.
