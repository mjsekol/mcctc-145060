# Hand the Answer Back
---
## Slide 1: The tip that says None
- A function works out an 18 percent tip
- It prints Tip: $7.20. Looks perfect
- The next line prints Tip saved for later: None
- No error on that line
- The line after that finally crashes
Speaker notes: Yesterday every function you wrote did its job by printing. That works for a heading. It does not work for a tip you need to add to a bill, or a check that decides whether a frequency is on the dial. Those functions need to hand an answer back to the line that called them. Today you learn return, and the bug of the day is a function that looks like it worked and handed back nothing.
Image: A receipt showing a correct tip line followed by a line that reads None, flat navy and accent blue.
---
## Slide 2: return
- return value ends the call immediately
- It sends the value back to the caller
- The call becomes that value
- A function with no return still returns None
- Python does that silently
Speaker notes: Return does two things. It ends the function right there, and it sends a value back. The call expression is then replaced by that value, as if you had typed the number yourself. And here is the rule behind today's bug. A function that reaches its end without a return still returns something. It returns None, which means no value, and Python never mentions it.
Image: An arrow leaving a function box and returning to the calling line with a value attached.
---
## Slide 3: The caller decides what to do
```python
def tip_amount(bill, tip_percent):
    return bill * tip_percent / 100

tip = tip_amount(40, 18)
print(f"Tip: ${tip:.2f}")
print(f"Total: ${40 + tip:.2f}")
print(f"Split four ways: ${(40 + tip_amount(40, 18)) / 4:.2f}")
```
```
Tip: $7.20
Total: $47.20
Split four ways: $11.80
```
Speaker notes: The function prints nothing. The caller stores it, adds it, formats it, or uses the call directly inside a bigger expression like the last line. A printed value is finished. A returned value can keep being used. That is the whole difference.
Image: None. This slide is code.
---
## Slide 4: Returning True or False
```python
def is_on_dial(text):
    if not text.isdecimal():
        return False
    frequency = int(text)
    return frequency >= LOWEST_FREQUENCY and frequency <= HIGHEST_FREQUENCY

print(is_on_dial("880"))
print(is_on_dial("2000"))
print(is_on_dial("loud"))
```
```
True
False
False
```
Speaker notes: Week 7's guard now has a name, and if is on dial reads like English. The early return False ends the call for loud, so int never touches it and it can never crash. An early return works like break for a function. And the function reads the two constants from the top of the file. Reading a global constant is fine. That is what constants are for.
Image: None. This slide is code.
---
## Slide 5: Local variables live inside the call
- Variables assigned inside a function are local
- Parameters are local too
- They disappear when the call returns
- Only the returned value comes back
- A local can share a name with a global without touching it
Speaker notes: Scope is where a variable exists. Anything assigned inside a function, including every parameter, is local. It exists while that call runs and then it is gone. Print a local name from outside and you get a NameError. And a local called total does not touch a global called total. They are two variables that happen to share a name.
Image: A function box with variables drawn inside it and a single value crossing the border outward.
---
## Slide 6: The scope error you will meet in version 2
```python
MAX_MOVES = 20
moves = 0

def take_step():
    moves = moves + 1
    print(f"Moves left: {MAX_MOVES - moves}")

take_step()
```
```
UnboundLocalError: cannot access local variable 'moves' where it is not associated with a value
```
Speaker notes: The body assigns to moves, so Python treats moves as local for the whole body. On the right side of that same line, the local moves has no value yet. Reading MAX MOVES is fine because the body never assigns to it. The fix is the pattern for state in version two. Pass moves in, return the new value, and let the caller store it. Moves equals take step of moves.
Image: None. This slide is code.
---
## Slide 7: Watch this: the tip, printed instead of returned
```python
def tip_amount(bill, tip_percent):
    tip = bill * tip_percent / 100
    print(f"Tip: ${tip:.2f}")

tip = tip_amount(40, 18)
print(f"Tip saved for later: {tip}")
print(f"Total: {40 + tip}")
```
Speaker notes: This is how yesterday's functions were written. It works out the tip and prints it. Then the caller stores the result and uses it twice. Predict all three lines of output, and predict which line, if any, crashes.
Image: None. This slide is code.
---
## Slide 8: The wrong way: None, then a crash
```
Tip: $7.20
Tip saved for later: None
Traceback (most recent call last):
  File "...", line 7, in <module>
    print(f"Total: {40 + tip}")
                    ~~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```
Speaker notes: The first line looks perfect because the function printed. But there is no return, so the call handed back None, and None got tied to tip. The second line printed the word None and did not crash. Only arithmetic finally failed. If the program had never added anything, nothing would ever have told you. This is the bug that does not crash, newest edition.
Image: None. This slide is code.
---
## Slide 9: The version that never crashes
- is_on_dial with the return left off the last line
- The comparison is worked out, then thrown away
- The function returns None, and if treats None as False
- 1470 is refused. Every frequency is refused. No error
- Habit: print what a new function returns, once
Speaker notes: Forget the return on the dial check and it is worse. The comparison is computed and discarded, the function falls off the end and returns None, and the if treats None like False. Every correct frequency is refused, forever. In a game, the player can never win and nothing says why. The habit that catches it is cheap. The first time you call a new function, print what it gives back. If you see None, look for the missing return.
Image: A radio dial with a correct frequency marked and a red refusal message beside it.
---
## Slide 10: What you are about to build
- Build 1: return practice in functions_practice.py
- Two functions that return a value, one returns True or False
- Print every return value once. No None allowed
- Build 2: destination_from for your own map
- Call it for every exit and compare with your map
Speaker notes: Build one goes back to yesterday's practice file. Add two functions that return a value and one that returns True or False, and print what each one returns the first time you call it. If any of them prints None, you have found today's bug in your own code. Build two is a function called destination from, for your own map. It takes a room and a direction and returns the room you end up in, or an empty string. Call it once for every exit on your map and check every answer against the map you drew.
Image: A hand-drawn room map beside a column of function calls and their returned room names, navy and accent blue.
---
