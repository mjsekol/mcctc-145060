# Lecture Notes: Objects Working Together
## 145060 Programming · Unit 7 · Week 16 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_ObjectsTogether.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_ObjectsTogether.pptx)

If you missed class, you can learn this concept from this file alone. This is the day
the pieces connect into the shape of the real project.

---

## Why this exists

A single object is useful. A program is many objects working together. The gear locker
holds gear. The text adventure's game holds rooms and a player. When one object holds
others and asks each to do its own job, you get a program that is clear to read, because
each object minds its own business.

This is the shape you will see in the anchor project and in almost every program you
write from here on: one object in charge, holding a collection of smaller objects, each
of which knows how to handle itself.

---

## The concept in plain language

**An attribute can be another object, or a collection of objects.** A method on the
holder can reach into its objects and call their methods. The holder does not need to
know how each object does its job. It only asks.

This is called delegation: the locker delegates checking-out to the gear, because the
gear knows its own rules. The locker's job is to find the right gear and let it do the
work.

---

## Worked example 1: a holder that finds and delegates

```python
class Gear:
    def __init__(self, tag):
        self.tag = tag
        self.borrower = None
    def check_out(self, borrower):
        if self.borrower is not None:
            return f"{self.tag} is already out with {self.borrower}."
        self.borrower = borrower
        return f"{self.tag} is now out with {borrower}."

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

locker = GearLocker()
locker.add(Gear("CTRL-01"))
print(locker.check_out("CTRL-01", "NovaFox"))
print(locker.check_out("CTRL-99", "NovaFox"))
```

Output:

```
CTRL-01 is now out with NovaFox.
No gear has the tag 'CTRL-99'.
```

The locker's `check_out` does two things only: find the gear, and if it exists, ask the
gear to check itself out. The gear's own `check_out` holds the rule about being already
loaned. The locker does not repeat that rule. It delegates.

---

## Worked example 2: asking every object a question

```python
class GearLocker:
    def __init__(self):
        self.items = {}
    def add(self, gear):
        self.items[gear.tag] = gear
    def ready_tags(self):
        ready = []
        for gear in self.items.values():
            if gear.borrower is None:
                ready.append(gear.tag)
        return ready

locker = GearLocker()
locker.add(Gear("CTRL-01"))
locker.add(Gear("HEAD-01"))
locker.items["CTRL-01"].check_out("NovaFox")
print(locker.ready_tags())
```

Output:

```
['HEAD-01']
```

The locker walks its own collection and asks each gear about itself. `CTRL-01` is out,
so only `HEAD-01` is ready. The loop is on the holder; the state is on each object.

---

## Worked example 3: this is the anchor project's shape

Open the text adventure version 4, `v4/game.py`. It has three classes:

```python
class Room:     # knows its name, description, exits, items
class Player:   # knows where it is, what it carries, where it has been
class Game:     # holds the rooms and the player, runs the rules
```

`Game` holds a dictionary of `Room` objects and one `Player`. When you type a command,
`Game.handle` finds the current room, asks the player to walk, and asks the room to
describe itself. It is the gear locker pattern, one class holding others and delegating.
The gear locker you built this week is the same idea at a smaller size. That is the
whole point of the lab: it rehearses the project.

---

## The wrong version, and the error it produces

A common slip is a typo in a method name on a held object:

```python
locker = GearLocker()
locker.add(Gear("CTRL-01"))
gear = locker.items["CTRL-01"]
print(gear.checkout("NovaFox"))     # method is check_out, not checkout
```

Output:

```
AttributeError: 'Gear' object has no attribute 'checkout'. Did you mean: 'check_out'?
```

Python compared the name against the ones that exist on `Gear` and suggested the closest.
This is the same helpfulness as the `NameError` suggestion from Unit 1. Read it, do not
paste it blindly, because it only checks spelling.

### Write this down

> One object in charge, holding many smaller objects, each minding its own state.

---

## Why this pattern is worth the trouble

You could keep everything in one giant function with a pile of dictionaries, the way
version 3 did. It works until it does not. When each object minds its own state and its
own rules, a bug is usually inside one small object, not spread across a huge function.
You can test one `Gear` on its own. You can read one `Room` without reading the whole
game. That is why the anchor project grew from loose dictionaries in Unit 5 into classes
in Unit 7: the same game, simpler to change and to trust.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Delegation** | A holder asking a held object to do its own job. |
| **Composition** | Building a class whose attributes are other objects. |
| **`.values()`** | Looping over the objects in a dictionary, ignoring the keys. |
| **Holder** | An object whose job is to hold and coordinate others. |

---

## Self-check

**Question 1.** In `Game`, `Room`, and `Player`, which one is the holder, and what does
it hold?

**Question 2.** Write the exact output.

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says woof"

class Kennel:
    def __init__(self):
        self.dogs = []
    def add(self, dog):
        self.dogs.append(dog)
    def roll_call(self):
        return "\n".join(dog.speak() for dog in self.dogs)

k = Kennel()
k.add(Dog("Rex"))
k.add(Dog("Bo"))
print(k.roll_call())
```

**Question 3.** Why is it better for the gear's own `check_out` to hold the
already-loaned rule, rather than the locker checking it?

---

### Answers

**1.** `Game` is the holder. It holds a dictionary of `Room` objects and one `Player`
object, and it runs the rules that connect them.

**2.**

```
Rex says woof
Bo says woof
```

The kennel holds two `Dog` objects and asks each to speak. Each dog reports its own
name, because `self` is that dog inside `speak`.

**3.** Because the rule about being already loaned is about the gear's own state, so it
belongs with the gear. If the locker held it, every place that checks out gear would
have to repeat the rule, and they could get it wrong differently. Keeping it on the gear
means the rule lives in one place, next to the data it protects.
