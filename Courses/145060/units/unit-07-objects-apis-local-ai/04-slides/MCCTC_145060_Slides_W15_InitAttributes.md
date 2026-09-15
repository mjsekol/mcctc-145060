# Building an Object
---
## Slide 1: How does a new object get its stuff
- You wrote a Gear class yesterday
- But how does a gear get its tag
- And its condition, and its borrower
- Every object needs a starting state
Speaker notes: Yesterday you saw that a class bundles data and behaviour. Today the missing piece: how does an object get its data in the first place. A brand new gear needs a tag and a condition. That starting state is set in one special place.
Image: An empty object outline on the left, a filled-in one on the right, an arrow labeled "__init__".
---
## Slide 2: __init__ runs automatically
- It runs once, when you make the object
- You never call it yourself
- Writing Gear(...) calls it for you
- Every attribute is created here
Speaker notes: The special method is called init, with two underscores on each side. It runs once, the moment you write Gear with parentheses. You never call it directly. Its job is to set up every attribute the object will ever have, so every object has the same shape.
Image: A timeline showing Gear("CTRL-01") triggering __init__ once.
---
## Slide 3: Attaching attributes to self
```python
class Gear:
    def __init__(self, tag, kind, condition="good"):
        self.tag = tag
        self.kind = kind
        self.condition = condition
        self.borrower = None
        self.times_loaned = 0
```
Speaker notes: Each self dot something equals value line creates one attribute on the new object. Condition has a default of good, so it is optional. Borrower and times_loaned are not passed in at all, they get sensible starting values. Now every gear has all five attributes, guaranteed.
Image: None. This slide is code.
---
## Slide 4: Reading them back
```python
pad = Gear("CTRL-01", "controller")
print(pad.tag)             # CTRL-01
print(pad.condition)       # good
print(pad.borrower)        # None
print(pad.times_loaned)    # 0
```
Speaker notes: The default filled in for condition. Borrower started as None, meaning it is in the cabinet. Times_loaned started at zero. None of that was passed in. Init set it up so the rest of the program can count on it being there.
Image: None. This slide is code.
---
## Slide 5: A class can refuse a bad value
- Check the value inside __init__
- Raise ValueError if it is wrong
- The object is never built badly
- A dictionary could not do this
Speaker notes: Because init is code, it can guard against nonsense. If someone passes a condition that is not good, worn, or broken, raise a ValueError and the object is never created. A dictionary would happily store sticky. The class protects its own rules. That is why we use one.
Image: A gate labeled __init__ turning away a value marked "sticky".
---
## Slide 6: The deepest trap of the week
```python
class GearLocker:
    items = {}                 # WRONG: on the class body
    def add(self, gear):
        self.items[gear.tag] = gear
```
Speaker notes: This looks fine. Every locker starts with an empty dictionary, right. Watch what happens when I make two lockers and add to only one of them. Predict the result before the next slide.
Image: None. This slide is code.
---
## Slide 7: Two lockers, one shared dictionary
```python
a = GearLocker()
b = GearLocker()
a.add(Gear("CTRL-01", "controller"))
print(len(a.items), len(b.items))   # 1 1
```
Speaker notes: No error. I added to a, and b has it too. The dictionary was made once, when the class was defined, so every locker points at the same one. This is the two-names-one-list bug from Unit 1, now with two objects sharing one dictionary.
Image: None. This slide is code.
---
## Slide 8: The fix, and the rule
- Create it inside __init__
- self.items = {} gives each its own
- Runs once per object, not once ever
- Lists, dicts, sets always go in __init__
Speaker notes: The fix is one line. Put self dot items equals empty dictionary inside init. Now it runs once per object, so each locker gets its own. The rule to carry forever: any attribute that is a list, dictionary, or set goes in init, always. Numbers and strings hide the bug. Collections show it.
Image: Two lockers now with separate dictionaries, an arrow from __init__ to each.
---
## Slide 9: Why the trap is tempting
- items = {} reads like "each starts empty"
- It even looks tidier up top
- Python runs the class body once
- So that one dictionary is shared
Speaker notes: The trap is tempting because items equals empty dictionary at the top reads exactly like what you want, every locker starts empty. But Python runs the class body one time, not once per object, so all of them share it. Put it in init and each object gets its own.
Image: A class body running once versus __init__ running per object, side by side.
---
## Slide 10: What you are about to build
- Write the Gear class __init__
- Give it all five attributes
- Add the ValueError guard
- Prove two gears do not share
Speaker notes: Build one is writing the Gear class init with all five attributes and the guard against a bad condition. Build two proves two gear objects do not share attributes, which is the trap you watched. Run the Part 1 tests until they pass.
Image: A test runner showing five green Part 1 tests, navy and accent blue.
