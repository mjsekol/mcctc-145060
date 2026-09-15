# Plan for the Failure You Can See Coming
---
## Slide 1: The crash in your README
- Week 2: you typed twelve where hours belonged
- ValueError, pasted under Known limitations
- The notes said: handling this properly is Unit 4
- This is Unit 4
- Some failures are facts about the world, not bugs
Speaker notes: In Week 2 you typed the word twelve into a program that wanted hours, it crashed, and you pasted the error into your README. People type words where numbers belong. Somebody forgets to copy a file onto the laptop. A test script runs out of lines. You know these will happen. You do not know when. A failure you can name before it happens deserves a plan, and today you learn to write one.
Image: A README page with a Known limitations heading and a highlighted ValueError line, flat navy and accent blue.
---
## Slide 2: How try and except work
- Python runs the try block line by line
- A line raises the named exception: try stops there
- The except block runs instead
- Either way, the program carries on afterward
- A different exception is not caught
Speaker notes: When a line cannot do its job, Python raises an exception, like ValueError. Try and except let you handle one. Python runs the try block. If a line raises the exception you named, the rest of the try block is skipped and the except block runs. Then the program carries on normally. And the name matters. An except only catches the exception it names. How do you know the name? It is the first word on the last line of the traceback.
Image: A flow diagram with a try box, a raised exception arrow jumping to an except box, and both paths rejoining below.
---
## Slide 3: The kiosk that no longer crashes
```python
text = input("How many tickets? ")
try:
    tickets = int(text)
    print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
except ValueError:
    print(f"'{text}' is not a whole number, so nothing was ordered.")
print("Thanks for using the ticket kiosk.")
```
```
How many tickets? two
'two' is not a whole number, so nothing was ordered.
Thanks for using the ticket kiosk.
```
Speaker notes: Trace it with two. The int line raises ValueError, so the print inside the try never runs, which is why nothing gets ordered. The except runs. Then the program carries on and thanks you. Notice input is outside the try. Only the conversion can raise the failure we planned for, so only it, and the line that depends on it, go inside.
Image: None. This slide is code.
---
## Slide 4: A validation loop you can reuse
```python
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
```
Speaker notes: This is Week 7's validation loop as a function you can call for every number your program asks for. Continue inside the except sends the loop back to ask again. Return number is the only way out, and only a valid number reaches it. Look at the range check below the try. You are about to see why it is not optional.
Image: None. This slide is code.
---
## Slide 5: int is not a validator
- int("-2") gives -2. So do " 7 " and "+7"
- isdecimal said False to "-2"
- Switch to try, and the range check becomes required
- Without it: a carpool booked for -2 people
- No error. The running thread again
Speaker notes: Int answers one question. Does this text spell a whole number? Negative two does. So does seven with spaces around it, and plus seven. The isdecimal check you used in Week 7 refused negative two on its own. When you switch to try, the range check is the only thing standing between you and a carpool booked for negative two people, with no error anywhere. The dangerous bugs are the ones that do not crash.
Image: A carpool booking screen showing Seats: -2 with a small warning triangle nobody noticed.
---
## Slide 6: A file that is not there
```python
def count_log_days(filename):
    """Return how many lines the practice log has, or 0 if the file is missing."""
    try:
        log = open(filename)
    except FileNotFoundError:
        print(f"Cannot find {filename}. Run this from the folder that holds it.")
        return 0
    # ... count the lines with readline, the Unit 3 way, then return the count ...
```
```
Days logged: 2
Cannot find practise_log.txt. Run this from the folder that holds it.
Days logged: 0
```
Speaker notes: Open raises FileNotFoundError when the file is not where Python looks. Only open goes inside the try. The except prints a message that says what to do, then returns zero, which ends the call early, the same way an early return False did last week. Is zero the right answer for a missing file? For a count on the screen, it is reasonable. For a bank balance it would be a lie. Choosing what to do instead is the design part of error handling.
Image: None. This slide is code.
---
## Slide 7: Input that runs out
```python
def read_command():
    """Return the next command, trimmed and lowercased, or "quit" if input ran out."""
    try:
        return input("> ").strip().lower()
    except EOFError:
        print()
        return "quit"
```
```
> You typed north.
> You typed look.
> 
You leave the station to the storm.
GAME OVER
```
Speaker notes: When a test script runs out of lines, input raises EOFError, end of file. Version one of your game crashes on it. This function catches it in the one place input is read and turns it into quit, a command the game already understands. The game ends through its normal path. That is the pattern for version two. Handle the failure where it happens, and turn it into something the rest of the program already knows how to deal with.
Image: None. This slide is code.
---
## Slide 8: Watch this: I name the exception
```python
text = input("How many tickets? ")
try:
    tickets = int(text)
    print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
except TypeError:
    print(f"'{text}' is not a whole number, so nothing was ordered.")
print("Thanks for using the ticket kiosk.")
```
Speaker notes: A word where a number belongs feels like the wrong type of input, so I write except TypeError. It looks handled. If you saw this in a code review you would probably approve it. Before I run it and type two, predict. Does the kiosk thank me, or not?
Image: None. This slide is code.
---
## Slide 9: The wrong way: the crash was never caught
```
How many tickets? two
Traceback (most recent call last):
  File "...", line 3, in <module>
    tickets = int(text)
ValueError: invalid literal for int() with base 10: 'two'
```
Speaker notes: It crashes exactly as if the try were not there. Int of two raises ValueError, and the except only catches TypeError, so nothing matches. TypeError means an operation got the wrong type, like the text five plus the number three. Int got a string, which is the right type, with a value it cannot use. That is ValueError. The fix costs nothing. Run the bad input first, and copy the name from the last line of the traceback.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: Lab U4-02 Part 1, the car wash tally
- Refactor a Unit 3 program into functions
- Save its output first. Compare with fc after
- try and except for bad tips and a missing goal file
- Build 2: v2 refactor, with an EOFError-proof read_command
Speaker notes: Build one is a car wash tally written with Unit 3 tools, one long loop with the same code pasted three times. You save what it prints before you touch it, refactor it into functions, add try and except for a bad tip and a missing goal file, and then prove with fc that it still prints exactly the same thing. One step asks you to type negative five in both versions. Build two is your own version two, starting with a read command function that survives the end of a test script.
Image: A car wash sign with a laptop beside it showing a progress bar, flat navy and accent blue.
---
