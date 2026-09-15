# Project: Text Adventure v2
## 145060 Programming · Unit 4 · Due 8:30 am, Week 9, Friday

**Mode:** solo. **Gate:** 3, full tooling, decision log required. **Built from:** your own text adventure v1, submitted on Tuesday of Week 8. **Periods:** the
function practice on Wednesday and Thursday of Week 8 is the warm-up, and Build 2 every day from Monday through Thursday of Week 9 is the build.

**Competencies:** 5.3.9 (create and call functions), 5.2.2 (scope of data), 5.3.10 (error handling), 5.5.1 (data validation), 5.4.4 (define test cases),
5.4.5 (test the program using defined test cases), 5.4.6 (correct syntax and runtime errors), 5.4.7 (debug logic errors), 5.5.2 (reuse libraries, through
importing your own file into a test).

**Deliverables in the syllabus:** TEXT ADVENTURE v2, refactored into functions, with inventory and full error handling · A WRITTEN TROUBLESHOOTING LOG USING A
NAMED METHODOLOGY. **Both are in this project.**

**This is version 2 of four.** Version 3, in Unit 5, moves your world into a data file and adds save and load. Every function you write now is a piece version
3 keeps.

---

## The brief

Read this as though a person said it to you.

> It's the Teen Game Night coordinator again, from the library. Your game has been on the laptops for a week, and the kids like it. Here is my list.
>
> Some kids hit Ctrl+C to see what happens, and the game dumps a wall of red text and dies, and then I have to restart it. One kid pasted a whole paragraph
> into it. One kid typed the number of a thing as a word, and that crashed it too. I don't know what half of that means. I know I'm the one who restarts it.
>
> A volunteer offered to add a couple of features for next month, and she opened your file and closed it again. She said it was "one enormous loop" and she
> couldn't change one room without being afraid of breaking three others. She wants to be able to test a piece without playing the whole game.
>
> And the kids keep asking what they're carrying. They pick something up and then forget whether they have it.
>
> **Do not change the game.** The kids know the routes. The same commands have to do the same things and the same endings have to happen. I need it to
> stop falling over, to have an inventory, and to be something another person can work on.
>
> Oh, and when it breaks while you're fixing it, and it will, write down what happened and how you fixed it. The volunteer wants to learn from it.

**That is the whole brief.** Notice what it does not say. It does not name the functions, say which failures matter, or say how you will prove the game did not
change. Those are yours to decide.

**The library and its game night are a composite scenario,** the same one as v1. The problems in it are the real problems of maintaining software.

---

## Requirements

### Same game

1. **Every v1 ending still happens the same way.** Every v1 test script reaches the same ending, and its output matches the v1 output you saved on Monday of Week 9,
   except for lines you changed on purpose. Every intended difference is listed in your README.
2. **No new rooms, items, endings, or routes.** Version 2 changes the shape of the code, not the game. A new room goes in your README under `Later versions`.

### Functions

3. **At least 8 functions** besides `main()`. At least 5 of them take parameters **and** return a value.
4. **`main()` holds the game state** as local variables, and passes values into functions and stores what they return: `room = ...`, `moves = ...`. A function that
   **computes** something returns it. A function that **shows** something may print.
5. **Every function has a docstring** saying what it returns, or what it prints.
6. **The file ends with `if __name__ == "__main__":` and `main()` under it,** so a test file can import your functions without starting the game.
7. **Nothing important is repeated.** A room description, a validation rule, or an exit lives in one place.

### Inventory

8. **An `inventory` command** that lists what the player carries, or says they carry nothing, and a `help` line that includes it.
9. **Without lists.** Lists are Unit 5. Each item is a True or False variable, and the rest of the game asks about items through functions, such as
   `describe_inventory(has_key, has_map)`. This will feel clumsy. **That is the point.** Write one sentence about the clumsiness in your README, and you will read it again
   in Unit 5.

### Error handling and validation

10. **Nothing a player types crashes the game.** Words, numbers, an empty line, and a 500-character paste.
11. **The end of input and Ctrl+C end the game through its normal ending,** not a traceback. A test script with no `quit` ends with your game's normal quit message.
12. **Every `try` block holds only the lines that can raise the exception it names.** Every `except` names an exception.
13. **No bare `except:` and no `except Exception:`** anywhere in the game.
14. **Every number the game asks for** goes through a validation function that checks both ends of its range.
15. **Commands have a length limit.** Anything too long gets a message, and the long text is not echoed back.

### Testing

16. **A test case table** in `test-cases.md` with at least **8** cases: ID, input, expected output, and why. It includes at least one boundary case, one invalid input, and the
    reproduction of one bug from your troubleshooting log. **Every expected value is decided from your game's rules before you run the test.**
17. **`test_adventure.py`** imports your game and checks at least 8 of those cases with the course's `check(label, actual, expected)` helper, and prints a count of failures.
    You may use `assert` too. You do not need `unittest`.
18. **The v1 scripts as regression tests.** `fc` output comparing each script's v1 and v2 output, pasted into `test-cases.md`.

### The troubleshooting log

19. **`troubleshooting-log.md`**, built from `MCCTC_145060_Template_TroubleshootingLog.md`, using the Six-Step Troubleshooting Method, with **at least 2 entries from real bugs you
    hit while building v2,** dated during the build.
20. **At least one of those entries is a bug that did not crash.** Every entry has a reproduction, at least one theory, a test with real output, the fix, and a verification with real
    output.

### Repository

```
text-adventure/
  design/                    (from v1, unchanged)
  test-scripts/
    win.txt
    lose-<name>.txt
    <name>_v1_output.txt     (saved Monday of Week 9, before any v2 change)
    no-quit.txt              (a script that ends without quit)
  adventure.py
  test_adventure.py
  test-cases.md
  function-map.md
  failure-inventory.md
  troubleshooting-log.md
  README.md
  decision-log.md
  AI-usage-log.md
  .gitignore                 (add __pycache__/ if it is not there)
```

### README, v2 sections

Keep the six v1 sections, updated. Add:

7. **What changed from v1.** The functions, the inventory, the error handling, and every intended output difference.
8. **How to test.** The exact commands for `test_adventure.py` and for the `fc` comparisons, and what passing looks like.
9. **The inventory problem.** One sentence on what is clumsy about items without a list. Observed, not guessed.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use lists, dictionaries, sets, tuples, or classes | They are Units 5 and 7. Version 2 exists so you feel what functions fix and what they do not. |
| Use `global` unless you can explain it line by line | It was not taught. Passing values in and returning them was, and it is what the tests expect. The reference build uses `global` in three inventory functions and explains why in a comment. |
| Use a bare `except:` or `except Exception:` | They turn loud bugs into silent ones. Wednesday's lesson. |
| Change the game's rooms, routes, or endings | The client asked for the same game. It also makes "did I break it?" answerable with `fc`. |
| Write expected test values by running your program | A test copied from the code agrees with the code whether it is right or not. |
| Write troubleshooting entries after the build from memory | The log is evidence. Theories you forgot are the most useful part. |
| Put personal information in any file, prompt, or log | The repository is public, and the log pastes real output. |

**On AI:** this is Gate 3. You may use a model to explain an error or suggest a function name, and every use goes in `AI-usage-log.md`. **You may not paste your game into a model and ask it to
refactor or "make it robust."** Wednesday showed you what that produces. You must be able to explain every function, every `try`, and every `except` in your file, and your demo will ask you to.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 9 Mon, first 5 minutes of Build 2 | Three sentences in the decision log: what v2 changes, what must stay identical, one thing v1 does that crashes today |
| **Measure** | Week 9 Mon, Build 2 | `test-scripts/*_v1_output.txt` for every v1 script, saved with `cmd /c "python adventure.py < test-scripts\win.txt > test-scripts\win_v1_output.txt"`. `failure-inventory.md`: every place the game reads input, and what can go wrong there |
| **Analyze** | Week 9 Mon, end of Build 2 | `function-map.md`: every planned function, its parameters, what it returns, and the v1 lines it replaces. **Committed before `adventure.py` changes** |
| **Improve** | Week 9 Tue to Wed | The refactor, then error handling and inventory. A daily goal line and a commit at the end of every Build 2. Log entries written as bugs happen |
| **Control** | Week 9 Thu to Fri, 8:30 am | `test-cases.md`, `test_adventure.py` passing, `fc` comparisons pasted, README complete |

**Measure is the phase that saves you.** Once you change one line of `adventure.py`, you can never again produce v1's output from the current file. If you skip it, you have no way to prove
requirement 1, and "it seems the same" is not proof.

**Agile lives inside Improve.** Each Build 2 starts with one line in your decision log, today's goal, and ends with a commit and one line: what got done and what did not.

---

## Milestone schedule, against actual class days

| Day | Build 2 goal |
|---|---|
| Week 8 Wed | `functions_practice.py`: three shapes from your v1 turned into functions. The warm-up, not submitted. |
| Week 8 Thu | Return practice, and `destination_from` for your own map. It becomes your v2 exit function. |
| Week 8 Fri | v1 demos. Your exit ticket names the first function you will write. **This brief is handed out.** |
| Week 9 Mon | Troubleshooting method. **Define, Measure, Analyze.** Baseline outputs, failure inventory, function map, empty troubleshooting log, all committed. `adventure.py` untouched. |
| Week 9 Tue | `try` and `except`. **Refactor:** constants, `main()` with the state, `read_command` handling `EOFError`, exits, descriptions, and endings as functions. `fc` on your win script shows no differences. |
| Week 9 Wed | Narrow excepts. **Error handling and inventory:** Ctrl+C, a script with no `quit`, validation functions, the length limit, the `inventory` command. Every script still matches. **Desk demos begin.** |
| Week 9 Thu | Test cases. **GP1 exam in Build 1.** Remaining Build 2: `test-cases.md`, `test_adventure.py`, `fc` for every script, log entries finished. **Desk demos continue.** |
| Week 9 Fri | **8:15-8:30: final commit window. Due at 8:30 am.** Gate 2 W09. Five-minute demos. GP1 ends. |

**The last commit pushed by 8:30 am Friday is the submission.**

---

## Three worked scope examples

These are here so you can calibrate. **Do not build any of these three.** They describe other people's games.

### Too small

> **The wrapper.** The student indents all of v1 under `def main():`, calls `main()` at the bottom, and wraps the whole thing in `try` with `except Exception:` and
> `print("Something went wrong.")`. They add `inventory` as one more `elif` that prints two flags.

One function. Nothing can be tested without playing the game. The `except` hides every bug, including the ones the refactor introduced, and Ctrl+C at a prompt still prints a
traceback, because `except Exception` does not catch `KeyboardInterrupt`. It looks like v2 in a file listing and it is v1 with a blindfold on.

### About right

> **Last Bus Home, v2.** Five locations, two items, two lose states, one validated item code at the vending machine. Eleven functions: `read_command`, `validate_command`,
> `read_item_code` with `try` and a range check, `find_exit`, `describe_location`, `describe_inventory`, `take_item_here`, `arrival_ending`, `minutes_warning`, `route_home_message`,
> and `show_intro`. `main()` holds the location, the minutes left, and two True or False item flags, passing them in and storing what comes back. The one `try` for the vending code and
> the one for reading input each name their exception. Ten test cases, including the exact minute the last bus leaves and the vending code `00`. Two log entries: a crash from a
> function called before it was defined, and a silent one where the fuse-style item check returned `None` on one path and the ending never fired.

Same game, `fc` proves it, every failure handled on purpose, and a test file that runs in a second. A spooky version with the same shape, a lighthouse during a storm, is exactly as good.

### Too big

> **The Academy, v2.** Twenty rooms moved into a separate file and read at startup, an inventory list with a `drop` command, a save file, random events, a `Player` class, and 40 `unittest`
> tests.

Every one of those is a real feature of a later version of this project. A list and a data file are Unit 5. Save and load is Unit 5. A class is Unit 7. `unittest` needs classes. Building them now means
code you cannot yet explain, and it breaks requirement 2, the same game. Put them under `Later versions` in your README.

**The calibration question:** could someone test your `find_exit` function without playing the game? If not, v2 is too small. Are you adding anything a player would notice as new? If so, it is too big.

---

## The five-minute demo

Friday of Week 9, for six or seven students. Everyone else demos at their desk on Wednesday or Thursday, using the same checklist, scored on the same 10 points.

1. **What changed, in two sentences.** (20 seconds)
2. **Run `python test_adventure.py`** and the `fc` comparison for your win script. (40 seconds)
3. **Let the audience try to crash it.** Ctrl+C at a prompt, an empty line, a word where a number goes, a 500-character paste. (60 seconds)
4. **Walk through one troubleshooting log entry,** the one with the theory that turned out wrong, if you have one. (90 seconds)
5. **Show the inventory, and name what is clumsy about it.** (30 seconds)
6. **Questions.** Your instructor will point at one `try` block and ask what it catches, what it lets through, and why. (60 seconds)

### Desk demo checklist, 10 points

| Points | What the instructor sees |
|---|---|
| 3 | `test_adventure.py` runs, and one `fc` comparison shows no unintended differences |
| 3 | Ctrl+C, an empty line, and a word at a number prompt are all handled on purpose |
| 2 | Explains one log entry: the reproduction, the theory, and the test |
| 2 | Explains the `try` block the instructor points at: what it catches and what it lets through |

**Item 6 is the course standard:** the only way to fail outright is to submit work you cannot explain.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Every v1 ending still happens, proven by `fc`. `inventory` works. Nothing typed crashes it. Ctrl+C and a script with no `quit` end through the normal ending. `test_adventure.py` runs. |
| **Code Quality** | 20 | At least 8 functions, 5 with parameters and return values. `main()` holds state and functions compute and return. Narrow `try` blocks, named exceptions, no bare or broad `except`. Validation checks both ends. No lists, dictionaries, or classes. |
| **Documentation** | 20 | Troubleshooting log with 2 or more real entries and all five required parts, one silent. `test-cases.md` with expected values from the rules. Function map, failure inventory, and README sections 7 through 9. |
| **Process** | 15 | Baseline outputs, failure inventory, and function map committed before `adventure.py` changed. A commit and a goal line every Build 2. Log entries dated during the build. |
| **Demonstration** | 10 | The desk demo checklist, or the full demo, on the same 10 points. |
| **Polish** | 10 | Error messages tell the player what to do next. `help` includes `inventory`. A volunteer could find where one room is described in under a minute. |

**The fastest way to lose Process points** is a history where `test-scripts/win_v1_output.txt` arrives in the same commit as a changed `adventure.py`. **The fastest way to lose Documentation
points** is a log whose every theory was right on the first try, with no test output before the fix.

---

## If you are stuck

**"`fc` shows differences and the game looks the same."** Read the two middle lines of each difference character by character. Spaces, capital letters, and blank lines count. If the difference is
one you meant, list it in the README.

**"My test file prints my game's intro and waits."** Your `adventure.py` calls `main()` with no `if __name__ == "__main__":` above it. Thursday's notes.

**"`UnboundLocalError` for `moves` or `room`."** A function is changing a variable that belongs to `main()`. Pass it in and return the new value. The notes from Thursday of Week 8.

**"My game says `None` somewhere."** A function that should return text printed it, or one path has no `return`. Print what the function returns. Then log it: it is your silent bug.

**"I have no bugs to log."** Run your no-quit script and press Ctrl+C at every kind of prompt before you add error handling. You will have bugs.

**"In PowerShell, the first command in my script is not a command."** Use `cmd /c "python adventure.py < test-scripts\win.txt"`. Piping with `Get-Content` can add an invisible character.
