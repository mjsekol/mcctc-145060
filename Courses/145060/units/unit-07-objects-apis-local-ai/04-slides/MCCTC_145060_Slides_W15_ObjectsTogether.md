# Objects Working Together
---
## Slide 1: One gear is not a program
- You built the Gear class
- A real club has a cabinet full
- Something has to hold them all
- And find the right one on request
Speaker notes: You built one Gear. A real club has a cabinet full of them, and something has to hold them all, find the right one by its tag, and coordinate. That something is another class, the GearLocker. Today objects start holding other objects.
Image: A single gear on the left, a full cabinet of gear on the right.
---
## Slide 2: A holder that delegates
- An attribute can be another object
- Or a whole collection of them
- The holder finds the right one
- Then asks it to do its own job
Speaker notes: An attribute does not have to be a number or a string. It can be another object, or a dictionary full of them. The holder's job is to find the right object and let it do the work. This is called delegation, and it keeps each object minding its own business.
Image: A locker box holding several gear objects, an arrow "delegates" to one of them.
---
## Slide 3: The locker holds and finds
```python
class GearLocker:
    def __init__(self):
        self.items = {}

    def add(self, gear):
        self.items[gear.tag] = gear

    def check_out(self, tag, borrower):
        gear = self.items.get(tag)
        if gear is None:
            return f"No gear has the tag '{tag}'."
        return gear.check_out(borrower)
```
Speaker notes: The locker keeps a dictionary of gear, keyed by tag. Its check_out does two things only. Find the gear, and if it exists, ask the gear to check itself out. The locker does not repeat the already-loaned rule. The gear holds that. The locker delegates.
Image: None. This slide is code.
---
## Slide 4: The locker in action
```python
locker = GearLocker()
locker.add(Gear("CTRL-01"))
print(locker.check_out("CTRL-01", "NovaFox"))
print(locker.check_out("CTRL-99", "NovaFox"))
```
Speaker notes: First call finds CTRL-01 and asks it to check itself out. Second call asks for a tag that does not exist, so the locker returns a clear message instead of crashing. Two layers, each doing its own small job. The locker finds, the gear decides.
Image: None. This slide is code.
---
## Slide 5: Asking every object a question
- Loop over your own collection
- Ask each object about itself
- Collect the answers
- The loop is on the holder
Speaker notes: A holder can walk its whole collection and ask each object a question. Which gear is ready. The loop lives on the holder, but the state lives on each object. The holder never needs to know how a gear decides it is ready. It only asks.
Image: A locker looping over gears, each returning ready or not.
---
## Slide 6: This is the text adventure
- Game holds Rooms and a Player
- You type a command
- Game finds the room, asks it to describe
- The gear locker is the same shape
Speaker notes: Open the anchor project, v4 slash game.py. Game holds a dictionary of Room objects and one Player. When you type a command, Game finds the current room and asks it to describe itself, asks the player to walk. It is the gear locker pattern at project size. Your lab rehearses the project.
Image: Game at the top holding Room objects and a Player, arrows of delegation down.
---
## Slide 7: A typo in a held method
```python
gear = locker.items["CTRL-01"]
print(gear.checkout("NovaFox"))     # method is check_out
```
Speaker notes: A common slip. The method is check_out with an underscore, and I typed checkout. Watch the error. Python is going to compare my name against the ones that exist and offer a suggestion, the same helpfulness we saw with NameError back in Unit 1.
Image: None. This slide is code.
---
## Slide 8: Did you mean check_out
```
AttributeError: 'Gear' object has no attribute 'checkout'. Did you mean: 'check_out'?
```
Speaker notes: Python compared checkout against the methods that exist on Gear and suggested check_out. Read it, do not paste it blindly. It only checks spelling, so it is right often but not always. It is a spelling suggestion, not understanding.
Image: None. This slide is code.
---
## Slide 9: Why this pattern is worth it
- A bug lives inside one small object
- You can test one gear alone
- You can read one room alone
- Not one giant function
Speaker notes: You could keep everything in one huge function with a pile of dictionaries, the way version 3 did. It works until it does not. When each object minds its own state, a bug is usually inside one small object. You can test one gear on its own. That is why the adventure grew into classes.
Image: A tidy set of small objects versus one tangled giant function.
---
## Slide 10: What you are about to build
- Write GearLocker and build_locker
- Pass the Part 3 tests
- Then open the anchor v4/game.py
- Match a Gear method to a Room or Player method
Speaker notes: Build one is writing GearLocker and build_locker and passing the Part 3 tests. Build two opens the anchor project and asks you to match one Gear method to one Room or Player method that does the same kind of job. That match is your ticket into next week.
Image: The lab tests green next to an open game.py, navy and accent blue.
