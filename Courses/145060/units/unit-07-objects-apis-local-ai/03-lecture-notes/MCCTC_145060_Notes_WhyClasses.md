# Lecture Notes: Why Classes
## 145060 Programming · Unit 7 · Week 16 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_WhyClasses.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_WhyClasses.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example.

**This is the start of the last big idea in the course, and the foundation of next
semester.** Object-oriented programming is most of 145065. You are meeting it here so
it is not new in the spring.

---

## Why this exists

In Unit 5 you built the text adventure's world out of dictionaries. A room was a
dictionary of values, and separate functions reached into it to do things. It worked.
It also had a seam: the data lived in one place and the rules about that data lived
somewhere else, in functions that had to be handed the data every time.

Here is that seam in your own version 3 code:

```python
# The room is a dictionary. describe_room is a function somewhere else.
def describe_room(world, state):
    room = world["rooms"][state["room"]]
    ...
```

The room does not know how to describe itself. A function has to be told which room and
which world. Nothing keeps the description rules next to the room they describe. When a
program grows, that distance is where bugs move in.

**A class closes that seam.** It puts the data and the rules that act on it in one
place, so the room knows how to describe itself.

---

## The concept in plain language

**A class is a template. An object is one filled-in copy of that template.**

An object knows things and can do things. The things it knows are its **attributes**.
The things it can do are its **methods**. Both live on the same object.

Think about a phone. It knows its battery level, its volume, whether it is locked. It
can ring, take a photo, lock itself. The knowing is attributes. The doing is methods.
A `Phone` class would hold both.

---

## Worked example 1: the same idea two ways

The Unit 5 way, a dictionary and a separate function:

```python
pad = {"tag": "CTRL-01", "condition": "good", "borrower": None}

def is_available(gear):
    return gear["borrower"] is None and gear["condition"] != "broken"

print(is_available(pad))
```

Output:

```
True
```

The Unit 7 way, a class that carries its own rule:

```python
class Gear:
    def __init__(self, tag, condition="good"):
        self.tag = tag
        self.condition = condition
        self.borrower = None

    def is_available(self):
        return self.borrower is None and self.condition != "broken"

pad = Gear("CTRL-01")
print(pad.is_available())
```

Output:

```
True
```

Both print `True`. The difference is not length. In the second version, `pad` carries
its own rule for being available. Nothing else has to remember that rule or be handed
the data. The gear knows how to answer a question about itself.

---

## Worked example 2: one template, many objects

```python
pad = Gear("CTRL-01")
headset = Gear("HEAD-01", "broken")

print(pad.tag, pad.is_available())        # CTRL-01 True
print(headset.tag, headset.is_available())  # HEAD-01 False
```

Output:

```
CTRL-01 True
HEAD-01 False
```

One class, `Gear`, made two different objects. Each remembers its own values. This is
the payoff of a class: when you have many of a thing, the template is written once and
every object fills it in differently.

---

## Worked example 3: a class that holds objects

```python
class GearLocker:
    def __init__(self):
        self.items = []

    def add(self, gear):
        self.items.append(gear)

    def ready_count(self):
        count = 0
        for gear in self.items:
            if gear.is_available():
                count += 1
        return count

locker = GearLocker()
locker.add(Gear("CTRL-01"))
locker.add(Gear("HEAD-01", "broken"))
print(locker.ready_count())
```

Output:

```
1
```

The locker holds `Gear` objects and asks each one whether it is available. This is the
exact shape of the text adventure's `Game`, which holds `Room` and `Player` objects and
asks each one to do its own work.

---

## The wrong version, and what it does instead of an error

The tempting first move is to call a method without the parentheses:

```python
pad = Gear("CTRL-01")
print(pad.is_available)
```

Output:

```
<bound method Gear.is_available of <__main__.Gear object at 0x000001F2A3B7C4D0>>
```

**No error, and no answer.** Without `()`, you printed the method itself, not its
result. Python is telling you `is_available` is a method sitting on `pad`, waiting to be
called. The fix is `pad.is_available()`.

### Write this down

> A method without parentheses is a thing, not an answer.

This is a new face on the running thread: the program did not crash, and it did not do
what you meant. It printed a description of a method instead of running it.

---

## Why the wrong version is tempting

An attribute has no parentheses: `pad.tag` gives you the tag. A method does the same
kind of reaching, so it looks like it should work the same way: `pad.is_available`. The
difference is that a method is a piece of code you have to run, and running it needs the
parentheses. An attribute is a value already sitting there.

The habit that prevents it: when you want a thing the object knows, use no parentheses.
When you want the object to do something, use parentheses. Knowing is `pad.tag`. Doing
is `pad.is_available()`.

---

## Four ways to organize a program

Classes are one style of programming, not the only one, and this course has now used
several. Naming them helps you see what changed.

- **Procedural:** a program written as a sequence of steps and function calls that pass
  data around. Your Unit 1 CLI Toolsmith was procedural. So was the dictionary version of
  the gear at the top of this file: data in a dictionary, functions handed that data.
- **Structured:** procedural code organized with clear control structures, loops,
  conditionals, and functions, instead of jumps. Everything you have written is
  structured. It is a discipline layered on procedural code, not a separate world.
- **Object-oriented:** data and the behaviour that acts on it are bundled into objects,
  which is what this unit adds. The `Gear` class is object-oriented.
- **Event-driven:** the program waits for events, a click or a message, and runs code in
  response. You will meet this in the senior web course. A button that runs a function
  when clicked is event-driven.

The same problem can be solved in more than one style. The gear tracker works as
procedural code with dictionaries or as object-oriented code with classes. Object-oriented
wins here because the gear has rules about itself that are better kept with the gear.
Knowing the names lets you say why you chose one, which is a real interview question.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Class** | A template that describes what a kind of object knows and can do. |
| **Procedural** | A program organized as steps and functions that pass data around. |
| **Object-oriented** | A program organized as objects that bundle data with behaviour. |
| **Event-driven** | A program that runs code in response to events like clicks. |
| **Object** | One filled-in copy made from a class. Also called an instance. |
| **Instance** | Another word for one object made from a class. |
| **Attribute** | A value an object knows about itself, like `pad.tag`. |
| **Method** | A function that belongs to a class and acts on an object. |
| **Instantiate** | To make an object from a class, by writing `Gear(...)`. |

---

## Self-check

**Question 1.** For a `Backpack` class, sort these into attributes and methods: color,
open, weight, add an item, current items, zip closed.

**Question 2.** What does this print, and why is it not `True`?

```python
class Light:
    def __init__(self):
        self.on = True
    def is_on(self):
        return self.on

lamp = Light()
print(lamp.is_on)
```

**Question 3.** In one sentence, what does a class give you that a dictionary does not?

---

### Answers

**1.** Attributes, the things it knows: color, weight, current items. Methods, the
things it does: open, add an item, zip closed. The test is whether it is a value the
thing has, or an action the thing performs.

**2.** It prints something like `<bound method Light.is_on of <__main__.Light object at
0x...>>`. It is not `True` because `lamp.is_on` with no parentheses is the method
itself, not the result of calling it. The fix is `lamp.is_on()`. This is the wrong
version from the notes: a method without parentheses is a thing, not an answer.

**3.** A class keeps the rules about the data together with the data, so the object can
protect and act on itself instead of relying on separate functions to be handed its
values.
