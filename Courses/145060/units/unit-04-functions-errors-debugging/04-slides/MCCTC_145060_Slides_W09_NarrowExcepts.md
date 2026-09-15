# Let the Surprise Crash
---
## Slide 1: Every jersey number refused
- A sign-up program asks for your jersey number
- You type 23. It says: type a whole number, like 23
- You type 7. Same message. You press Ctrl+C
- Same message again. Nothing stops it
- No error anywhere on the screen
Speaker notes: Yesterday you learned to catch failures you can predict. The natural next thought is, why not catch everything, so the program never crashes at all? Today you see what that costs. A program that catches everything can refuse every correct answer, blame the user for it, and refuse to stop, all without a single error message.
Image: A sign-up kiosk screen repeating the same polite refusal message down the whole display.
---
## Slide 2: Four rules for except
- 1. Name the exception. Never a bare except
- 2. Put only the line that can fail inside try
- 3. Let failures you did not predict crash
- 4. Found a new failure? Decide on purpose
Speaker notes: Four rules, and they are the whole lesson. Name the exception, so the except says what you have a plan for. Keep the try block small, so you cannot catch something by accident. Let the failures you did not predict crash, because a traceback is the most useful bug report you will ever get, and it is free. And when testing shows you a new failure, decide on purpose what should happen. Do not widen the except to make it go away.
Image: Four numbered cards in a row, each with a short rule, navy on white.
---
## Slide 3: Watch this: a robust jersey reader
```python
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
```
Speaker notes: This is the kind of code you get when you ask for something robust. Everything is inside the try, and the except catches anything at all. There is a typo in it. Find it before I run it. Then predict what happens when I type twenty three.
Image: None. This slide is code.
---
## Slide 4: The wrong way: no error, no way out
```
Jersey number: 23
Type a whole number, like 23.
Jersey number: 7
Type a whole number, like 23.
Jersey number: ^C
Type a whole number, like 23.
```
Speaker notes: HIGHEST JERSY is missing an E. That raises a NameError, the bare except catches it, and prints a message written for a completely different problem. The player types twenty three and is told to type a number like twenty three. Then Ctrl+C. A bare except catches KeyboardInterrupt too, so the program refuses to stop. The only way out is the trash can icon on the terminal. And at the end of a test script it catches EOFError on every pass and floods the screen.
Image: None. This slide is code.
---
## Slide 5: Narrowed: the error it was hiding
```python
        text = input("Jersey number: ")
        try:
            number = int(text)
        except ValueError:
            print("Type a whole number, like 23.")
            continue
```
```
    if number >= LOWEST_JERSEY and number <= HIGHEST_JERSY:
                                             ^^^^^^^^^^^^^
NameError: name 'HIGHEST_JERSY' is not defined. Did you mean: 'HIGHEST_JERSEY'?
```
Speaker notes: Same function, narrowed. Only the conversion is inside the try, and the except names ValueError. The typo is still there, and now typing twenty three crashes. That crash is the good outcome. It names the line, points at the word, and suggests the fix. Correct the spelling and the function does exactly what it promised.
Image: None. This slide is code.
---
## Slide 6: A big try block whose message lies
```python
    try:
        log = open(filename)
        # ... read every line, add int(line[7:10]) to total ...
        return total / days
    except Exception:
        print(f"Cannot find {filename}.")
        return 0
```
```
35.0
Cannot find blank_log.txt.
0
Cannot find empty_log.txt.
0
Cannot find no_such_log.txt.
0
```
Speaker notes: Here the try wraps the whole reader and the except catches Exception. The first file is fine. Then three files, three messages, and two are false. The blank log was found. Its blank line made int of an empty string raise ValueError. The empty log was found too. It made the program divide by zero. Both get reported as a missing file, and the function returns an average of zero for all three. A false zero never crashes. For a grade or a paycheck, that is a serious bug.
Image: None. This slide is code.
---
## Slide 7: Decide on purpose
- Only open goes inside try, with FileNotFoundError
- Now the blank line crashes, on its exact line
- Decide: a blank line is not a day, so skip it
- Decide: an empty file gets its own honest message
- A line nobody has decided about still crashes
Speaker notes: Narrow it, and the missing file gets a true message while the blank line crashes with its exact line and value. Now you know about two failures you did not predict, so decide. A blank line is not a day, so skip it with an if. An empty file gets a message that says it has no days yet. Neither needed an except. When you can check for a condition cheaply, checking is often clearer than catching. Anything nobody has decided about still crashes, and that is correct.
Image: A decision table with three rows, blank line, empty file, and unknown, each with its chosen action.
---
## Slide 8: Raise it, and let the caller decide
```python
def parse_minutes(text):
    """Return typed text as practice minutes. Raise ValueError if it cannot be used."""
    try:
        minutes = int(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a whole number of minutes.")
    if minutes < 0 or minutes > MAX_MINUTES:
        raise ValueError(f"Minutes must be from 0 to {MAX_MINUTES}.")
    return minutes
```
```
Logged 45 minutes.
Not logged. 'forty' is not a whole number of minutes.
Not logged. Minutes must be from 0 to 600.
Not logged. Minutes must be from 0 to 600.
```
Speaker notes: Sometimes your own function discovers the problem. It should not return a fake number like zero, because somebody will add a fake number to a total without checking it. It should raise an exception with a clear message. The caller catches it with except ValueError as error and prints the message. An exception cannot be ignored by accident. If nothing catches it, the program stops and says why.
Image: None. This slide is code.
---
## Slide 9: Ctrl+C and the end of input, on purpose
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
Speaker notes: Ctrl+C and the end of input are not bugs. A player pressing Ctrl+C wants out. So handle both where input is read, each by its own name, and turn them into quit. One try can have several excepts, and Python runs the first one whose name matches. Nothing else is caught, so a typo anywhere else in your game still crashes loudly. This is the read command function your version two needs.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: Lab U4-02 Part 2
- Paste an AI version with a bare except. Break it
- Narrow every except. Shrink every try block
- Ctrl+C and end of input end with totals printed
- Build 2: v2 error handling and your inventory command
Speaker notes: Build one is part two of the car wash lab. You paste in a version an AI assistant would call robust, with a bare except, and you find out what it does to a typo and to Ctrl+C. Before that step, find the trash can icon on your terminal panel. Then you narrow every except, shrink every try block, and make Ctrl+C and the end of input print the totals instead of losing the day's money. Build two is error handling and the inventory command in your version two.
Image: A terminal panel with its trash can icon circled, beside a car wash tally summary.
---
