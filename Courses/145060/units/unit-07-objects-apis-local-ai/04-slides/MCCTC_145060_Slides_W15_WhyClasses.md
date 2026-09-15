# Why Classes
---
## Slide 1: Your room does not know how to describe itself
- In Unit 5 a room was a dictionary
- A function far away did the describing
- The rules live apart from the data
- That gap is where bugs move in
Speaker notes: Pull up your text adventure from Unit 5. A room is a dictionary, and describe_room is a function somewhere else that has to be handed the room every time. The room does not know anything about itself. Today we close that gap.
Image: A dictionary on the left and a function on the right, a wide gap between them labeled "where bugs live".
---
## Slide 2: An object knows things and can do things
- Attributes are what it knows
- Methods are what it can do
- Both live on the same object
- Your phone is one already
Speaker notes: Think about your phone. It knows its battery level and whether it is locked. It can ring and take a photo. The knowing is attributes. The doing is methods. A class puts both in one place, so the thing carries its own data and its own behaviour.
Image: A phone in the center, "knows" labels on one side, "does" labels on the other, navy and accent blue.
---
## Slide 3: The Unit 5 way
```python
pad = {"tag": "CTRL-01", "condition": "good", "borrower": None}

def is_available(gear):
    return gear["borrower"] is None and gear["condition"] in ("good", "worn")

print(is_available(pad))    # True
```
Speaker notes: Here is the old way. A dictionary of values, and a separate function that has to be handed the dictionary. The gear does not know its own rule for being available. Some other code holds it. Watch what changes on the next slide.
Image: None. This slide is code.
---
## Slide 4: The Unit 7 way
```python
class Gear:
    def __init__(self, tag, condition="good"):
        self.tag = tag
        self.condition = condition
        self.borrower = None

    def is_available(self):
        return self.borrower is None and self.condition in ("good", "worn")

print(Gear("CTRL-01").is_available())   # True
```
Speaker notes: Same answer, True. The difference is not length. Now the gear carries its own rule. Nothing else has to remember it or be handed the data. The gear knows how to answer a question about itself. That is the whole idea of a class.
Image: None. This slide is code.
---
## Slide 5: One template, many objects
- A class is a template
- An object is one filled-in copy
- Each object remembers its own values
- Write the rule once, reuse it everywhere
Speaker notes: One Gear class can make a hundred gear objects, each with its own tag and condition. You write the template once. Every object fills it in differently and carries its own state. That payoff grows with every object you need.
Image: One template shape at the top, three filled-in copies below it with different values.
---
## Slide 6: When a class earns its keep
- The thing has rules about itself
- You have many of the thing
- You want the rules next to the data
- Otherwise a dictionary is fine
Speaker notes: Do not put everything in a class. A one-line settings blob is fine as a dictionary. Reach for a class when the thing has rules, when you have many of them, or when you want behaviour to live with data. The gear locker has all three.
Image: A short checklist with three checkmarks and one line about dictionaries staying simple.
---
## Slide 7: The trap, watch closely
```python
pad = Gear("CTRL-01")
print(pad.is_available)
```
Speaker notes: I want to know if this gear is available. I call the method. Predict what prints before I press enter. It is not True and it is not False. Watch.
Image: None. This slide is code.
---
## Slide 8: A method without parentheses is a thing
```
<bound method Gear.is_available of <__main__.Gear object at 0x000001F2A3B7C4D0>>
```
Speaker notes: No error, and no answer. Without the parentheses I printed the method itself, not its result. Python is telling me is_available is a method sitting on pad, waiting to be called. The fix is pad dot is_available with parentheses. This is our running thread again.
Image: None. This slide is code.
---
## Slide 9: Knowing versus doing
- No parentheses for a value it knows
- Parentheses to make it do something
- pad.tag is knowing
- pad.is_available() is doing
Speaker notes: Here is the habit that prevents the trap. When you want a thing the object knows, use no parentheses. When you want the object to do something, add the parentheses. Knowing is pad dot tag. Doing is pad dot is_available with parentheses.
Image: Two rows, one labeled knowing with pad.tag, one labeled doing with pad.is_available().
---
## Slide 10: What you are about to build
- Read your Unit 5 describe_room and name the seam
- Then open the Gear Locker lab
- Run the starter and find its shipped bug
- Tomorrow you write the Gear class
Speaker notes: Build one is reading your own version 3 and naming the gap a class would close. Build two is opening the Gear Locker lab, running the starter, and finding the bug it already ships with. Tomorrow you write the class that fixes it.
Image: A split screen of the old dictionary version and the new class skeleton, navy and accent blue.
