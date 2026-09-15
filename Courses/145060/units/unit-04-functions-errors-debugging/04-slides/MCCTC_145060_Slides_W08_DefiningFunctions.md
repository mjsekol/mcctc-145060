# Write It Once, Call It Anywhere
---
## Slide 1: Six copies of the same three lines
- Your adventure prints a heading for every room
- Six rooms, six copies of the same lines
- Your playtester wants the headings in capitals
- You change five of them
- Nobody notices the sixth for a week
Speaker notes: Open your version one and count how many times you print a room heading, a line of dashes, and an exits line. Copy and paste makes a promise that you will change every copy together, forever. You will not keep that promise. Nobody does. Today you learn how to give a block of code a name so it lives in one place.
Image: Six identical code snippets stacked, with one visibly different from the others, flat navy and accent blue.
---
## Slide 2: The words
- def defines a function. Defining does not run it
- The body is the indented block
- A parameter is a placeholder name in the def line
- A call runs the body: name, then parentheses
- An argument is the real value in the call
Speaker notes: You have been calling functions since Week 1. Print is a function, len is a function. Today you write your own. Def teaches Python a new name. The body is what that name means. Parameters are placeholders. When you call it, each argument you pass gets tied to a parameter, first to first, second to second, and then the body runs.
Image: A labeled def line with arrows pointing to the name, the parameter, and the body.
---
## Slide 3: The copy problem, fixed
```python
def show_heading(room_name):
    print()
    print(f"== {room_name} ==")
    print("-" * 20)

show_heading("Kitchen")
show_heading("Porch")
show_heading("Bedroom")
```
```

== Kitchen ==
--------------------

== Porch ==
--------------------
```
Speaker notes: One definition, three calls. On the first call, room name is Kitchen. On the second, Porch. The body is the same three lines every time, and only the value tied to the parameter changes. Now make every heading capitals. One edit. That is the whole reason functions exist.
Image: None. This slide is code.
---
## Slide 4: Two parameters, matched by position
```python
def print_receipt_line(item, price):
    print(f"{item:<16}${price:>6.2f}")

print_receipt_line("Nachos", 4.5)
print_receipt_line("Sports drink", 2.25)
print_receipt_line("Pretzel", 3)
```
```
Nachos          $  4.50
Sports drink    $  2.25
Pretzel         $  3.00
```
Speaker notes: The first argument goes to item and the second goes to price. Python matches them by position, not by meaning. And the formatting from Week 3 now lives in one place, so every line of every receipt lines up without you trying.
Image: None. This slide is code.
---
## Slide 5: A body holds anything you know
```python
def repeat_message(message, times):
    for count in range(1, times + 1):
        print(f"({count} of {times}) {message}")

def warn_storm(moves_left):
    if moves_left == 1:
        print("Thunder rolls closer. The storm is 1 move away.")
    elif moves_left <= 5:
        print(f"Thunder rolls closer. The storm is {moves_left} moves away.")

repeat_message("Stay on high ground.", 3)
warn_storm(9)
warn_storm(4)
```
Speaker notes: Loops and decisions work inside a function body exactly as they do anywhere else. Repeat message prints three numbered lines. Warn storm with nine prints nothing at all, and that is correct, because nine matches neither condition. Warn storm with four prints the four moves warning. The body is ordinary code that happens to have a name.
Image: None. This slide is code.
---
## Slide 6: Defining is not running
- def celebrate() then no call: nothing prints
- celebrate without parentheses: legal, does nothing
- A call jumps into the body, then comes back
- The def must run before the first call reaches it
- Put every def near the top, below your constants
Speaker notes: A def by itself teaches Python a name and does nothing else. If you forget the call, nothing happens and nothing complains. If you write the name without parentheses, that is also legal and also does nothing. And Python reads top to bottom, so the def has to come before the first call. Constants first, then every def, then the code that calls them.
Image: A top-to-bottom file outline with a constants band, a functions band, and a main code band.
---
## Slide 7: Watch this: I forget the argument
```python
def show_heading(room_name):
    print()
    print(f"== {room_name} ==")
    print("-" * 20)

show_heading()
```
Speaker notes: I defined show heading with one parameter, room name. Now I call it with empty parentheses. Before I run it, what do you think Python will say, and will it name the problem?
Image: None. This slide is code.
---
## Slide 8: The wrong way: the missing argument
```
Traceback (most recent call last):
  File "...", line 6, in <module>
    show_heading()
    ~~~~~~~~~~~~^^
TypeError: show_heading() missing 1 required positional argument: 'room_name'
```
Speaker notes: Read it like a sentence. Show heading is missing one required positional argument, and it is called room name. Python names the function, the count, and the exact parameter. Too many arguments gives a message that says takes one positional argument but two were given. Calling before the def gives a NameError. The one that does not crash is passing two text arguments in the wrong order, because Python has no idea north is a direction.
Image: None. This slide is code.
---
## Slide 9: Arguments match by position, not meaning
- show_exit(room, direction) called as show_exit("north", "lobby")
- No error. The words land in the wrong roles
- It prints: From the north you can go lobby
- Read the def line before you write the call
- The def line tells you the order
Speaker notes: This is the silent one. If both parameters take text, swapping them raises nothing. The function happily prints from the north you can go lobby. The dangerous bugs are the ones that do not crash, and this one is waiting in every function with two parameters of the same type. When you call a function, look at its def line.
Image: Two labeled slots with two word cards placed in the wrong slots.
---
## Slide 10: What you are about to build
- Build 1: Unit 3 quiz, 30 minutes
- Build 2: functions_practice.py
- Find three repeated shapes in your v1
- Turn each into a function with a parameter
- Call each at least twice. Commit
Speaker notes: Build one is the Unit 3 quiz. Build two is a new practice file, not your version one. Find three places in your adventure where the same shape of code repeats with a different value. Write each one as a function with at least one parameter, and call each one at least twice with different arguments. Every function you write today prints. Tomorrow you learn how to make one hand a value back.
Image: A practice file with three short function definitions and six calls beneath them, navy and accent blue.
---
