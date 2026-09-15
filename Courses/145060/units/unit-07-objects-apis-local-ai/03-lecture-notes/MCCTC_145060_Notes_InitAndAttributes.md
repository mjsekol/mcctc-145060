# Lecture Notes: __init__ and Attributes
## 145060 Programming · Unit 7 · Week 15 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W15_InitAttributes.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W15_InitAttributes.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example, especially the shared-list bug near the end.

---

## Why this exists

Yesterday you saw that a class bundles data with behaviour. Today you learn how an
object gets its data in the first place. Every object needs a starting state: a gear
item needs its tag, a player needs an empty inventory. `__init__` is where that
starting state is set, once, the moment the object is made.

Getting this right matters because it is where the object's shape is decided. Every
attribute an object will ever have should be created here, so every object of the class
has the same shape and nothing is ever missing.

---

## The concept in plain language

**`__init__` is a special method that runs automatically when you make an object.** You
never call it yourself. Writing `Gear("CTRL-01", "controller")` calls it for you and
hands it those two values.

Inside `__init__`, you attach values to `self`. Each `self.something = value` line
creates an attribute on the new object.

The two underscores on each side of `init` mark it as a method Python calls for you.
You will meet a few of these. You do not call them directly.

---

## Worked example 1: setting up an object

```python
class Gear:
    def __init__(self, tag, kind, condition="good"):
        self.tag = tag
        self.kind = kind
        self.condition = condition
        self.borrower = None       # None means it is in the cabinet
        self.times_loaned = 0

pad = Gear("CTRL-01", "controller")
print(pad.tag)             # CTRL-01
print(pad.kind)            # controller
print(pad.condition)       # good
print(pad.borrower)        # None
print(pad.times_loaned)    # 0
```

Output:

```
CTRL-01
controller
good
None
0
```

`condition` had a default of `"good"`, so it was not required. `borrower` and
`times_loaned` were not passed in at all; they were set to sensible starting values
inside `__init__`. Every `Gear` now has all five attributes, guaranteed.

---

## Worked example 2: defaults and overrides

```python
new_pad = Gear("CTRL-02", "controller")
worn_pad = Gear("CTRL-03", "controller", "worn")

print(new_pad.condition)    # good
print(worn_pad.condition)   # worn
```

Output:

```
good
worn
```

The default fills in when you do not supply a value. Supplying one overrides it. This is
the same defaulting you saw in functions in Unit 4, now on `__init__`.

---

## Worked example 3: guarding a bad value

A class can refuse to build an object that would not make sense.

```python
CONDITIONS = ["good", "worn", "broken"]

class Gear:
    def __init__(self, tag, kind, condition="good"):
        if condition not in CONDITIONS:
            raise ValueError(f"condition must be one of {CONDITIONS}, not '{condition}'")
        self.tag = tag
        self.kind = kind
        self.condition = condition

print(Gear("CTRL-01", "controller", "sticky"))
```

Output:

```
ValueError: condition must be one of ['good', 'worn', 'broken'], not 'sticky'
```

The object is never built with a nonsense condition. This is the class protecting its
own rules, the whole reason to use a class instead of a dictionary. A dictionary would
have happily stored `"sticky"`.

---

## The wrong version, and the bug that does not crash

Here is the deepest trap in the week. Put an attribute on the class body instead of
inside `__init__`:

```python
class GearLocker:
    items = {}                 # WRONG: on the class, not in __init__
    def add(self, gear):
        self.items[gear.tag] = gear

a = GearLocker()
b = GearLocker()
a.add(Gear("CTRL-01", "controller"))
print(len(a.items))            # 1
print(len(b.items))            # 1  -- b never had anything added
```

Output:

```
1
1
```

**No error. Two separate lockers share one dictionary.** Adding to `a` changed `b`,
because `items` was created once, when the class was defined, and every locker points at
that same one dictionary.

The fix is to create it inside `__init__`, so each object gets its own:

```python
class GearLocker:
    def __init__(self):
        self.items = {}        # made fresh for every locker
```

With the fix, `len(b.items)` is `0`.

### Write this down

> Create every attribute in `__init__`, so each object gets its own.

This is the object version of a bug the course promised back in Unit 1: two names
pointing at the same list, so changing one appears to change the other. Here two objects
point at the same dictionary. Same bug, new shape.

---

## Why the wrong version is tempting

Writing `items = {}` at the top of the class reads like "every locker starts with an
empty dictionary," which is what you want. It even looks tidier than putting it in
`__init__`. The problem is that Python runs the class body once, not once per object, so
that one dictionary is shared. Numbers and strings do not show the bug, because
reassigning them makes a new value. Lists, dictionaries, and sets show it, because you
change them in place.

The habit that prevents it: any attribute that is a list, dictionary, or set goes in
`__init__`, always.

---

## Vocabulary

| Term | What it means |
|---|---|
| **`__init__`** | The method that runs automatically when an object is made. |
| **`self`** | The object being built or acted on. More on this Wednesday. |
| **Attribute** | A value stored on an object with `self.name = value`. |
| **Default value** | A value a parameter takes when none is supplied. |
| **Instance attribute** | An attribute created per object, in `__init__`. |
| **Class attribute** | An attribute on the class body, shared by every object. |

---

## Self-check

**Question 1.** How many times does `__init__` run for `Gear("CTRL-01", "controller")`,
and who calls it?

**Question 2.** Write the exact output.

```python
class Note:
    def __init__(self, title):
        self.title = title
        self.tags = []

a = Note("Algebra")
b = Note("History")
a.tags.append("exam")
print(len(a.tags), len(b.tags))
```

**Question 3.** A classmate's `Bag` class has `contents = []` on the class body and
finds every bag shares one list. Give the one-line fix and say why it works.

---

### Answers

**1.** Once. You do not call it. Writing `Gear(...)` calls `__init__` for you and passes
it the arguments.

**2.** `1 0`. Each `Note` got its own `tags` list because the list is created in
`__init__`, so appending to `a.tags` does not touch `b.tags`. This is the correct
version of the shared-list bug.

**3.** Move it into `__init__` as `self.contents = []`. It works because `__init__` runs
once per object, so each bag gets a fresh, separate list, instead of all bags sharing
the one list created when the class was defined.
