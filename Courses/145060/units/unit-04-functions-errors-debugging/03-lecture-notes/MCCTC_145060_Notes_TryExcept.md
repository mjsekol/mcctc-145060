# Lecture Notes: try and except for Failures You Can See Coming
## 145060 Programming · Unit 4 · Week 9 · Tuesday, November 3

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W09_TryExcept.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W09_TryExcept.pptx)

If you missed class, you can learn this concept from this file alone. Every example uses functions
from Week 8 and loops from Unit 3. The one new piece of Python is `try` and `except`.

**Today is one concept: catching a failure you can predict, and doing something useful instead of
crashing.** Tomorrow is the other half: what to do about the failures you did not predict.

---

## Why this exists

In Week 2 you typed `twelve` where a program wanted hours, and it crashed with `ValueError`. You pasted
that error into your README under Known limitations, and the notes said handling it properly was Unit 4.

This is Unit 4.

Some failures are not bugs in your code. They are facts about the world your code runs in. People type
words where numbers belong. Somebody forgets to copy `goal.txt` onto the laptop. A test script runs out of
lines before the game ends. You know these will happen. You do not know when. An **anticipated failure**
is one you can name before it happens, and every one of them deserves a plan.

Until today, your only plan was to check first: `.isdecimal()` before `int()`. That works for some inputs.
It cannot check whether a file exists before another program deletes it, or whether input will run out.
`try` and `except` handle all of them the same way.

Outcomes: 5.3.10, **code error handling techniques**, and 5.5.1, **develop programs using data validation
techniques**.

---

## The concept in plain language

When Python cannot do what a line asks, it **raises an exception**: an object that describes the failure,
such as `ValueError` or `FileNotFoundError`. If nothing handles it, the program stops and prints a traceback.
You have seen hundreds of these.

`try` and `except` let you handle one:

```python
try:
    # the line that might fail
except ValueError:
    # what to do instead, if that line raised ValueError
# the program carries on here either way
```

- Python runs the **`try` block** line by line.
- If a line raises the exception named in `except`, Python **stops the `try` block right there**, skips the
  rest of it, and runs the **`except` block** instead.
- If nothing is raised, the `except` block is skipped.
- Either way, the program **carries on** after the whole statement.
- If a line raises a **different** exception from the one named, the `except` does not match and the program
  crashes as usual.

**How do you know which name to write?** Read the last line of the traceback. It starts with the exception's
name. `ValueError: invalid literal for int() with base 10: 'two'` tells you to write `except ValueError:`.

The three anticipated failures you will handle this week:

| Exception | Raised when | Example |
|---|---|---|
| `ValueError` | A value has the right type but a wrong value for the job | `int("two")`, `int("4.5")`, `int("")` |
| `FileNotFoundError` | `open()` cannot find the file | `open("practise_log.txt")`, spelled wrong |
| `EOFError` | `input()` has nothing left to read | the last line of a test script was already used |

---

## Worked example 1: the crash you have had since Week 2

```python
tickets = int(input("How many tickets? "))
print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
```

Typing `two`:

```
How many tickets? two
Traceback (most recent call last):
  File "...", line 1, in <module>
    tickets = int(input("How many tickets? "))
ValueError: invalid literal for int() with base 10: 'two'
```

Now with `try` and `except`:

```python
# try runs the risky line. except runs only if that line raises ValueError.
text = input("How many tickets? ")
try:
    tickets = int(text)
    print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
except ValueError:
    print(f"'{text}' is not a whole number, so nothing was ordered.")
print("Thanks for using the ticket kiosk.")
```

Typing `3`, then running again and typing `two`:

```
How many tickets? 3
Ordering 3 tickets at $12 each: $36
Thanks for using the ticket kiosk.
```

```
How many tickets? two
'two' is not a whole number, so nothing was ordered.
Thanks for using the ticket kiosk.
```

**Trace the second run line by line.** `int("two")` raises `ValueError`. The `print` inside the `try` block **never runs**,
which is why no order is printed. The `except` block runs. Then the program carries on to `Thanks for using the ticket kiosk.`
and ends normally.

Notice that `input` is **outside** the `try`. Only `int(text)` can raise the `ValueError` you are planning for, so only it,
and the line that depends on it, belong inside.

---

## Worked example 2: a validation loop that returns the number

In Week 7 you wrote validation loops with `.isdecimal()`. Here is the same idea as a function, with `try`, that you can reuse
for every number your program asks for:

```python
# A validation loop as a function: it only returns a whole number in range.
def read_whole_number(prompt, low, high):
    """Ask until a whole number from low to high is typed. Return it as an int."""
    while True:
        text = input(prompt)
        try:
            number = int(text)
        except ValueError:
            print("Type a whole number, like 4.")
            continue
        if number < low or number > high:
            print(f"Pick a number from {low} to {high}.")
        else:
            return number


seats = read_whole_number("Seats in the car, 1 to 7: ", 1, 7)
print(f"Carpool booked for {seats}.")
```

Typing `four`, `4.5`, `-2`, `9`, and then `4` with spaces around it:

```
Seats in the car, 1 to 7: four
Type a whole number, like 4.
Seats in the car, 1 to 7: 4.5
Type a whole number, like 4.
Seats in the car, 1 to 7: -2
Pick a number from 1 to 7.
Seats in the car, 1 to 7: 9
Pick a number from 1 to 7.
Seats in the car, 1 to 7:  4 
Carpool booked for 4.
```

Two things to see:

- **`continue` inside `except`** sends the loop back to ask again. `return number` is the only way out, and only a valid number
  reaches it. That is Week 7's rule: the exit is reachable only by good input.
- **`-2` got past `int()`.** This is the part people miss. `int()` is not a validator. It answers "does this text spell a whole
  number?" and `-2` does. So do these:

```python
print(int(' 7 '), int('-5'), int('+7'), int('1_000'))
```

```
7 -5 7 1000
```

`.isdecimal()` said False to both `'-5'` and `' 7 '`. When you switch from checking first to `try`, **the range check is no longer
optional.** Without `number < low`, a program that asked for 1 to 7 seats would book a carpool for -2 people and raise no error.
That is the course's running thread again: the dangerous bugs are the ones that do not crash.

---

## Worked example 3: a file that is not there

```python
# open() raises FileNotFoundError when the file is not where Python looks.
LOG_FILE = "practice_log.txt"


def count_log_days(filename):
    """Return how many lines the practice log has, or 0 if the file is missing."""
    try:
        log = open(filename)
    except FileNotFoundError:
        print(f"Cannot find {filename}. Run this from the folder that holds it.")
        return 0
    days = 0
    line = log.readline()
    while line != "":
        days = days + 1
        line = log.readline()
    log.close()
    return days


print(f"Days logged: {count_log_days(LOG_FILE)}")
print(f"Days logged: {count_log_days('practise_log.txt')}")
```

Run from a folder holding a two-line `practice_log.txt`:

```
Days logged: 2
Cannot find practise_log.txt. Run this from the folder that holds it.
Days logged: 0
```

The second call misspells the file name. Without the `try`, it would end with
`FileNotFoundError: [Errno 2] No such file or directory: 'practise_log.txt'`. With it, the message says what to do.

The message printed **before** `Days logged: 0` because the f-string has to call the function to get the number, and the function
prints while it runs. `return 0` inside `except` ends the call early, the same way an early `return False` did on October 29.

**Is returning 0 the right plan?** For a count shown on the screen, it is reasonable. For something like a bank balance, pretending a
missing file means zero would be a silent lie. Deciding what the program should do instead is the design part of error handling, and
tomorrow's lesson is about getting that decision wrong.

---

## Worked example 4: input that runs out

When you test your adventure with a script, `python adventure.py < test-scripts\win.txt`, the game reads one line per `input()`. If the script
ends before the game does, version 1 crashes with `EOFError: EOF when reading a line`. EOF means end of file. It is anticipated, because every
short script causes it.

```python
# input() raises EOFError when there is no more input to read, such as the
# end of a test script. Returning "quit" ends the game through its normal path.
def read_command():
    """Return the next command, trimmed and lowercased, or "quit" if input ran out."""
    try:
        return input("> ").strip().lower()
    except EOFError:
        print()
        return "quit"


playing = True
while playing:
    command = read_command()
    if command == "quit":
        print("You leave the station to the storm.")
        playing = False
    else:
        print(f"You typed {command}.")
print("GAME OVER")
```

With a script of two lines, `north` and `look`, and no `quit`:

```
> You typed north.
> You typed look.
> 
You leave the station to the storm.
GAME OVER
```

Piped commands do not appear after the prompt, which is why the `>` lines look empty. The third `input()` found nothing, raised `EOFError`,
and the function turned it into `"quit"`. The game ended through the same path a player's `quit` takes. **That is the pattern to copy into v2:**
handle the failure in the one function that reads input, and turn it into something the rest of the program already understands.

In PowerShell, run scripts with `cmd /c "python ex4.py < script.txt"`. Piping with `Get-Content` can add an invisible character to the first line.

---

## The wrong version: the wrong exception name

```python
text = input("How many tickets? ")
try:
    tickets = int(text)
    print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
except TypeError:
    print(f"'{text}' is not a whole number, so nothing was ordered.")
print("Thanks for using the ticket kiosk.")
```

Typing `two`:

```
How many tickets? two
Traceback (most recent call last):
  File "...", line 3, in <module>
    tickets = int(text)
ValueError: invalid literal for int() with base 10: 'two'
```

The `except` only handles `TypeError`. `int("two")` raises `ValueError`, so nothing matches and the program crashes exactly as if the `try` were
not there. **An `except` handles the exception it names and nothing else.**

---

## Why the wrong version is tempting

**"Type" sounds right.** The problem feels like a wrong type of input, so `TypeError` seems like the obvious name. Python's categories are more
specific: `TypeError` means an operation got a value of the wrong **type**, like `"5" + 3`. `int("two")` gets a string, which is the right type
for `int()`, with a value it cannot use. That is `ValueError`.

**Guessing is faster than reading.** The traceback's last line gives you the exact name for free. Run the failing input first, copy the name, then
write the `except`. That is step 1 of yesterday's method.

**It looks handled.** A `try` with an `except` under it looks finished in a code review. Only a run with the bad input shows whether it catches
anything. Test every `except` you write with the input it exists for.

---

## Check first, or try it?

Both are legitimate, and programmers argue about which to prefer.

**Check first** (`if text.isdecimal():`) makes the rule visible, and it refused `-2` on its own. It cannot handle failures you cannot check in
advance, like input running out.

**Try it** (`try: int(text)`) handles every way a conversion can fail, including ones you did not think of, and it is how Python code usually handles
conversions and files. It accepts more than you might expect, so it needs a separate range check.

The course uses `try` for conversions, files, and input from now on, and keeps range checks as plain `if` statements.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Exception** | Python's report that a line could not do its job, such as `ValueError`. |
| **Raise** | What Python does when a line fails: it creates an exception and stops running that line. |
| **`try` block** | The indented lines that might raise an exception you plan to handle. |
| **`except` block** | The lines that run instead, if the `try` block raised the exception named on the `except` line. |
| **Handle** | Catch an exception and do something useful instead of crashing. |
| **Anticipated failure** | A failure you can name before it happens, like a word typed where a number belongs. |
| **`ValueError`** | The right type with a value the operation cannot use, like `int("two")`. |
| **`FileNotFoundError`** | `open()` could not find the file. |
| **`EOFError`** | `input()` had nothing left to read. EOF means end of file. |
| **Outcome 5.3.10** | The WebXam competency for coding error handling techniques. |
| **Outcome 5.5.1** | The WebXam competency for data validation techniques. |

---

## Self-check

**Question 1.** Write the exact output when the user types `12.5`.

```python
def to_whole_hours(text):
    try:
        hours = int(text)
        print("Converted")
    except ValueError:
        print("Not whole")
        return 0
    return hours

print("Hours:", to_whole_hours(input("Hours worked: ")))
```

**Question 2.** A student's `read_whole_number(prompt, 1, 10)` uses `try` and `int()`, and has no range check. List three things a user could type
that the function would return without complaint, and say which of them is a silent bug.

**Question 3.** This crashes when `scores.txt` does not exist. Write the `try` and `except` so it prints `No scores yet.` and the program keeps going.

```python
scores = open("scores.txt")
print(scores.readline())
scores.close()
print("Done")
```

---

### Answers

**1.**

```
Hours worked: 12.5
Not whole
Hours: 0
```

`int("12.5")` raises `ValueError`, so `print("Converted")` never runs. The `except` prints `Not whole` and returns 0. Verified by running.

**2.** Any whole number outside 1 to 10 gets through, such as `0`, `-3`, or `50`, and so does text like ` 5 ` or `+5` that `int()` accepts. Every
out-of-range number is a silent bug: `-3` is returned as if it were a valid choice, with no error anywhere. (` 5 ` and `+5` both give 5, which is
harmless.)

**3.**

```python
try:
    scores = open("scores.txt")
    print(scores.readline())
    scores.close()
except FileNotFoundError:
    print("No scores yet.")
print("Done")
```

This prints `No scores yet.` then `Done` when the file is missing. Verified by running it in a folder without the file.

A stronger version puts **only** `open` inside the `try`, using a function and an early `return`, the way worked example 3 does:

```python
def show_first_score(filename):
    try:
        scores = open(filename)
    except FileNotFoundError:
        print("No scores yet.")
        return
    print(scores.readline())
    scores.close()


show_first_score("scores.txt")
print("Done")
```

Same output. Both earn full credit today. Tomorrow's lesson explains why the second is stronger: the smaller the `try` block, the fewer
failures it can catch by accident.
