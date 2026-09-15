# Lecture Notes: Narrow Excepts and the Failures You Did Not See Coming
## 145060 Programming · Unit 4 · Week 9 · Wednesday, November 4

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W09_NarrowExcepts.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W09_NarrowExcepts.pptx)

If you missed class, you can learn this concept from this file alone. Read yesterday's notes,
[try and except for Failures You Can See Coming](MCCTC_145060_Notes_TryExcept.md), first.

**Today is one concept: an `except` should catch only the failure it has a plan for, and everything
else should crash loudly.** It sounds backwards. By the end of this file it should sound obvious.

---

## Why this exists

Yesterday you learned to catch failures you could predict. The natural next thought is: why not catch
**everything**, so the program never crashes at all?

Because a crash is information. A traceback names the exception, the file, the line, and the reason. It is
the most useful bug report you will ever get, and it is free. An `except` that catches everything throws that
report away and replaces it with whatever message you guessed at before the bug existed.

An **unanticipated failure** is one you did not predict: a typo in a variable name, a blank line in a data
file, a division by a count that turned out to be zero. You cannot write a helpful message for a failure you
did not imagine. What you can do is make sure it is **loud**, so you find it on the first run instead of the
fortieth.

This is the running thread of this course in its newest form. `"12" * 3` gave `121212`. A loop ran one time too
few. A function returned `None` silently. **An `except` that swallows an error turns a loud bug into a silent
one,** and the dangerous bugs are the ones that do not crash.

Outcomes: 5.3.10, **code error handling techniques**, 5.4.6, **correct syntax and runtime errors**, and 5.4.7,
**debug logic errors**.

---

## The concept in plain language

Four rules. They are the whole lesson.

| Rule | Why |
|---|---|
| **1. Name the exception.** `except ValueError:`, never `except:` | A name says what you have a plan for. No name catches everything, including your typos. |
| **2. Keep the `try` block small.** Put in only the line that can raise it | Every extra line inside `try` is a line whose failures you might catch by accident. |
| **3. Let unanticipated failures crash.** | A traceback tells you what, where, and why. A guessed message tells you nothing true. |
| **4. When you learn about a new failure, decide on purpose.** | Handle it with its own honest message, or fix the cause. Do not widen an `except` to hide it. |

Three pieces of Python go with the rules:

- **Bare `except:`** has no exception name. It catches every exception there is, including `KeyboardInterrupt`, which is how Python
  reports Ctrl+C. A program with a bare `except` around its input can refuse to stop.
- **`except Exception:`** catches almost everything except Ctrl+C. It is still too broad, for the same reason: it catches your bugs.
- **`except ValueError as error:`** catches one kind of exception and ties it to a name, so you can print its message.

And one statement you have seen in error messages but never written:

- **`raise ValueError("a clear message")`** raises an exception on purpose. A function that cannot do its job should raise, and let the
  caller decide what to do, rather than return a fake value that looks real.

---

## Worked example 1: the except that hides a typo

```python
# An except with no name catches everything, including your own typos.
LOWEST_JERSEY = 0
HIGHEST_JERSEY = 99


def read_jersey_number():
    """Ask until a jersey number from 0 to 99 is typed. Return it."""
    while True:
        try:
            number = int(input("Jersey number: "))
            if number >= LOWEST_JERSEY and number <= HIGHEST_JERSY:
                return number
            print(f"Jersey numbers run from {LOWEST_JERSEY} to {HIGHEST_JERSEY}.")
        except:
            print("Type a whole number, like 23.")


jersey = read_jersey_number()
print(f"Jersey {jersey} is yours.")
```

Look at the `if` line. `HIGHEST_JERSY` is missing an E. Typing `23`, `7`, and `0`:

```
Jersey number: 23
Type a whole number, like 23.
Jersey number: 7
Type a whole number, like 23.
Jersey number: 0
Type a whole number, like 23.
```

**No error. Every jersey number is refused, and the message blames the player.** The misspelled name raises `NameError`, the bare `except`
catches it, and prints a message that was written for a completely different failure. The player types `23` and is told to type a number like
`23`.

It gets worse. Press Ctrl+C to get out, and the bare `except` catches that too:

```
Jersey number: ^C
Type a whole number, like 23.
Jersey number: ^C
Type a whole number, like 23.
```

With the typo in place, no input escapes the loop. The only way out is to kill the terminal. In VS Code that is the trash can icon on the terminal
panel. If input runs out, as it does at the end of a test script, the bare `except` catches `EOFError` on every pass and the loop prints its message
over and over, as fast as the terminal can show it, until you kill it.

## The same function, narrowed

```python
# Only the conversion is inside try, and except names the one failure it handles.
LOWEST_JERSEY = 0
HIGHEST_JERSEY = 99


def read_jersey_number():
    """Ask until a jersey number from 0 to 99 is typed. Return it."""
    while True:
        text = input("Jersey number: ")
        try:
            number = int(text)
        except ValueError:
            print("Type a whole number, like 23.")
            continue
        if number >= LOWEST_JERSEY and number <= HIGHEST_JERSY:
            return number
        print(f"Jersey numbers run from {LOWEST_JERSEY} to {HIGHEST_JERSEY}.")


jersey = read_jersey_number()
print(f"Jersey {jersey} is yours.")
```

The typo is still there. Typing `23`:

```
Jersey number: 23
Traceback (most recent call last):
  File "...", line 20, in <module>
    jersey = read_jersey_number()
  File "...", line 15, in read_jersey_number
    if number >= LOWEST_JERSEY and number <= HIGHEST_JERSY:
                                             ^^^^^^^^^^^^^
NameError: name 'HIGHEST_JERSY' is not defined. Did you mean: 'HIGHEST_JERSEY'?
```

**This crash is the good outcome.** It names the line, points at the word, and suggests the fix. Correct the spelling, and typing `twenty`, `150`, `23`
gives exactly what the program promised:

```
Jersey number: twenty
Type a whole number, like 23.
Jersey number: 150
Jersey numbers run from 0 to 99.
Jersey number: 23
Jersey 23 is yours.
```

Two rules did the work. The `except` names `ValueError`, so it cannot catch a `NameError`. And the `try` block holds one line, so even a `ValueError`
from somewhere else in the function could not be caught by accident.

---

## Worked example 2: the big try block whose message lies

A practice log reader, written to "handle errors":

```python
# One big try block, and an except that catches every kind of failure.
def average_minutes(filename):
    """Return the average minutes per day in the practice log."""
    try:
        log = open(filename)
        total = 0
        days = 0
        line = log.readline()
        while line != "":
            total = total + int(line[7:10])
            days = days + 1
            line = log.readline()
        log.close()
        return total / days
    except Exception:
        print(f"Cannot find {filename}.")
        return 0


print(average_minutes("practice_log.txt"))
print(average_minutes("blank_log.txt"))
print(average_minutes("empty_log.txt"))
print(average_minutes("no_such_log.txt"))
```

`practice_log.txt` has three good lines. `blank_log.txt` is the same with a blank line in the middle. `empty_log.txt` exists and has nothing in it. The
last file does not exist.

```
35.0
Cannot find blank_log.txt.
0
Cannot find empty_log.txt.
0
Cannot find no_such_log.txt.
0
```

**Three different failures, one message, and two of those messages are false.** `blank_log.txt` and `empty_log.txt` were both found. The blank line made
`int("")` raise `ValueError`. The empty file made `total / days` divide by zero. The `except Exception` caught both and reported a missing file. Anyone
reading that message goes looking for a file that is sitting right there.

And the program says the average is 0 for all three. For a practice tracker, a false 0 is annoying. For a grade or a paycheck, it is a serious bug that
never crashes.

Narrow it. Only `open` can raise `FileNotFoundError`, so only `open` goes inside the `try`:

```python
# The try block holds only open(). Everything else is allowed to fail loudly.
def average_minutes(filename):
    """Return the average minutes per day in the practice log."""
    try:
        log = open(filename)
    except FileNotFoundError:
        print(f"Cannot find {filename}.")
        return 0
    total = 0
    days = 0
    line = log.readline()
    while line != "":
        total = total + int(line[7:10])
        days = days + 1
        line = log.readline()
    log.close()
    return total / days


print(average_minutes("practice_log.txt"))
print(average_minutes("no_such_log.txt"))
print(average_minutes("blank_log.txt"))
```

```
35.0
Cannot find no_such_log.txt.
0
Traceback (most recent call last):
  File "...", line 22, in <module>
    print(average_minutes("blank_log.txt"))
          ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "...", line 13, in average_minutes
    total = total + int(line[7:10])
                    ~~~^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: ''
```

The missing file gets a true message. The blank line crashes, on the exact line, with the exact value `''`. Run it on `empty_log.txt` and it crashes with
`ZeroDivisionError: division by zero`. **Now you know about two failures you did not anticipate.** That is rule 4: decide on purpose.

```python
# Now that testing has shown blank lines and empty files, both are anticipated.
# Each gets its own honest handling. Anything else still fails loudly.
def average_minutes(filename):
    """Return the average minutes per day in the practice log, or 0 if there are no days."""
    try:
        log = open(filename)
    except FileNotFoundError:
        print(f"Cannot find {filename}.")
        return 0
    total = 0
    days = 0
    line = log.readline()
    while line != "":
        if line.strip() != "":          # a blank line is not a day
            total = total + int(line[7:10])
            days = days + 1
        line = log.readline()
    log.close()
    if days == 0:
        print(f"{filename} has no days logged yet.")
        return 0
    return total / days


print(average_minutes("practice_log.txt"))
print(average_minutes("blank_log.txt"))
print(average_minutes("empty_log.txt"))
print(average_minutes("no_such_log.txt"))
```

```
35.0
35.0
empty_log.txt has no days logged yet.
0
Cannot find no_such_log.txt.
0
```

Neither new failure was handled with `except`. A blank line is skipped with an `if`, and an empty file is caught with a check before dividing. **When you
can check for a condition cheaply, checking is often clearer than catching.** A line like `Oct 19  3x` would still crash loudly, and that is correct:
nobody has decided what it should mean yet.

---

## Worked example 3: raising your own exception

Sometimes your function is the one that discovers the problem. It should not print a message and return a made-up value. It should **raise**, and let the
caller decide.

```python
# A function that cannot do its job raises an exception with a clear message.
# The caller decides what to do about it, and "as error" gives it the message.
MAX_MINUTES = 600


def parse_minutes(text):
    """Return typed text as practice minutes. Raise ValueError if it cannot be used."""
    try:
        minutes = int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a whole number of minutes.")
    if minutes < 0 or minutes > MAX_MINUTES:
        raise ValueError(f"Minutes must be from 0 to {MAX_MINUTES}.")
    return minutes


def log_practice(text):
    """Try to log one day of practice and say what happened."""
    try:
        minutes = parse_minutes(text)
    except ValueError as error:
        print(f"Not logged. {error}")
        return
    print(f"Logged {minutes} minutes.")


log_practice("45")
log_practice("forty")
log_practice("-10")
log_practice("900")
```

```
Logged 45 minutes.
Not logged. 'forty' is not a whole number of minutes.
Not logged. Minutes must be from 0 to 600.
Not logged. Minutes must be from 0 to 600.
```

`parse_minutes` never returns a fake number like 0 or -1 for bad input. A fake number can be added to a total by somebody who forgot to check it, and that is a
silent bug. An exception cannot be ignored by accident: if nothing catches it, the program stops and says why. `as error` ties the exception to the name `error`,
and printing it prints the message you wrote.

This is exactly why the text adventure's version 2 has `has_item` raise `ValueError` for a misspelled item name instead of returning `False`. A typo that returned
`False` would make the game quietly unwinnable.

---

## Worked example 4: Ctrl+C and running out of input, on purpose

Ctrl+C and the end of input are not bugs. A player pressing Ctrl+C wants out, and a test script that ends wants the game to end. Handle them **where input is read,**
with their own names, and turn them into the command the game already understands:

```python
def read_command():
    """Return the next command, trimmed and lowercased, or "quit" if the player wants out."""
    try:
        return input("> ").strip().lower()
    except EOFError:
        print()
        return "quit"
    except KeyboardInterrupt:
        print()
        return "quit"
```

One `try` can have several `except` clauses. Python checks them in order and runs the first one whose name matches. Nothing else is caught, so a typo anywhere else in
the game still crashes loudly.

On lab machines, confirm what Ctrl+C does at an `input()` prompt with and without this function. It should end with a traceback whose last line is `KeyboardInterrupt`
without it, and print `You leave the station to the storm.` with it.

---

## The wrong version, one more time

```python
except:
    print("Type a whole number, like 23.")
```

**What it produces:** no error at all. Every failure, including your own typos, Ctrl+C, and the end of input, gets the same message. The error it was hiding in worked
example 1 was:

```
NameError: name 'HIGHEST_JERSY' is not defined. Did you mean: 'HIGHEST_JERSEY'?
```

---

## Why the wrong version is tempting

**"It never crashes" sounds like quality.** A program that never shows a traceback looks finished. But a program that shows a false message looks finished too, and it is
harder to fix than one that crashes.

**AI assistants suggest it.** Ask a model to make code "more robust" and a very common answer is to wrap everything in `try` with a broad `except`. It is confident, well
formatted, and wrong for exactly the reasons in this file.

**Widening an `except` makes a crash go away today.** It does. It also makes every future bug in that block go away from your screen and stay in the program.

**Big `try` blocks are less typing.** One `try` around twenty lines is less work than one around the single line that can fail. You pay for it the first time a different
line fails.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Unanticipated failure** | A failure you did not predict, such as a typo, a blank line in a file, or dividing by a count of zero. |
| **Bare `except`** | `except:` with no exception name. It catches everything, including Ctrl+C. Never use it. |
| **Broad `except`** | `except Exception:`. Catches nearly everything. Too wide for the same reason. |
| **Narrow `except`** | An `except` that names the one exception it has a plan for. |
| **Swallow an error** | Catch an exception and hide it, so the program carries on as if nothing happened. |
| **Fail loudly** | Stop with a traceback that says what went wrong, instead of carrying on with a wrong result. |
| **`KeyboardInterrupt`** | The exception Python raises when you press Ctrl+C. |
| **`as error`** | Ties a caught exception to a name, so you can use its message. |
| **`raise`** | Raises an exception on purpose, with a message you write. |
| **`ZeroDivisionError`** | Raised when a number is divided by zero. |
| **`NameError`** | Raised when a name is used that was never defined, usually a typo. |

---

## Self-check

**Question 1.** Write the exact output. Then explain in one sentence why `Saved` never prints.

```python
def save_score(text):
    try:
        score = int(text)
        bonus = score / 0
        print("Saved")
    except ValueError:
        print("Not a number")
    print("Finished")

save_score("abc")
save_score("40")
```

**Question 2.** A classmate says: "`except Exception:` is fine, because unlike a bare `except` it lets me press Ctrl+C." What is right about that, and what is still wrong?

**Question 3.** Rewrite this so a missing file gets a true message and any other failure crashes with its real traceback. Keep the same function name and return value.

```python
def first_song(filename):
    """Return the first line of the playlist file."""
    try:
        playlist = open(filename)
        song = playlist.readline().strip()
        playlist.close()
        return song.title()
    except:
        return "No playlist found"
```

---

### Answers

**1.**

```
Not a number
Finished
Traceback (most recent call last):
  File "...", line 11, in <module>
    save_score("40")
    ~~~~~~~~~~^^^^^^
  File "...", line 4, in save_score
    bonus = score / 0
            ~~~~~~^~~
ZeroDivisionError: division by zero
```

For `"abc"`, `int` raises `ValueError`, the `except` catches it, and `Finished` prints. For `"40"`, dividing by zero raises `ZeroDivisionError`, which the `except ValueError`
does not name, so the program crashes before `Saved` and before `Finished`. Verified by running. `Saved` never prints because in both calls a line above it inside the `try`
raised first.

**2.** Right: `except Exception:` does not catch `KeyboardInterrupt`, so Ctrl+C still works. Still wrong: it catches `NameError`, `ZeroDivisionError`, `TypeError`, and nearly
every other bug, so a typo gets the same message as the failure it was written for, and the program carries on with a wrong result.

**3.**

```python
def first_song(filename):
    """Return the first line of the playlist file."""
    try:
        playlist = open(filename)
    except FileNotFoundError:
        return "No playlist found"
    song = playlist.readline().strip()
    playlist.close()
    return song.title()
```

Only `open` is inside `try`, and the `except` names `FileNotFoundError`. A typo in `.title()` or anything else below now crashes with its real name and line. Verified: with a
file whose first line is `static hallway` it returns `Static Hallway`, and with no file it returns `No playlist found`.
