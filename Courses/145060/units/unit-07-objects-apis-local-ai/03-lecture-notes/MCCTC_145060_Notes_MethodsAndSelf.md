# Lecture Notes: Methods and self
## 145060 Programming · Unit 7 · Week 16 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W16_MethodsAndSelf.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W16_MethodsAndSelf.pptx)

If you missed class, you can learn this concept from this file alone. This is the day
`self` finally makes sense. Type every example with two objects, not one.

**This is the hardest idea in the week.** Not because it is complicated, but because it
looks pointless until you see it with two objects. Do not skip the two-object examples.

---

## Why this exists

An object should be able to do things, not only hold values. A gear item should check
itself out. A player should pick up an item. Those actions belong on the object,
because they change the object's own data. A method is how you put an action on a class.

The puzzle is: when a method runs, how does it know which object to change? If you have
two gear items and call `check_out` on one, the method must change that one and not the
other. The answer is `self`.

---

## The concept in plain language

**A method is a function that belongs to a class. Its first parameter is `self`, the
specific object it was called on.**

When you write `pad.check_out("NovaFox")`, Python does two things:

1. It finds `check_out` on the `Gear` class.
2. It hands `pad` to that method as the first argument, `self`.

So inside the method, `self` is `pad`. If you had written
`headset.check_out("NovaFox")`, then `self` would be `headset`. You never type the
object at the call. Python fills in `self` from whatever is before the dot.

---

## Worked example 1: a method that changes its object

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

pad = Gear("CTRL-01")
print(pad.check_out("NovaFox"))
print(pad.check_out("PixelMoth"))
```

Output:

```
CTRL-01 is now out with NovaFox.
CTRL-01 is already out with NovaFox.
```

The first call set `self.borrower`. The second call saw it was already set and refused.
The method read and wrote the object's own attribute through `self`.

---

## Worked example 2: two objects prove what self is

This is the example that makes `self` click. Run it.

```python
first = Gear("CTRL-01")
second = Gear("CTRL-02")

first.check_out("NovaFox")

print(first.borrower)     # NovaFox
print(second.borrower)    # None
```

Output:

```
NovaFox
None
```

You called `check_out` on `first`, so `self` was `first`, so only `first` changed.
`second` was never touched. The same method, called on a different object, would change
that object instead. That is the entire meaning of `self`.

---

## Worked example 3: a method that answers a question

Methods do not have to change anything. Some only report.

```python
class Gear:
    def __init__(self, tag, condition="good"):
        self.tag = tag
        self.condition = condition
        self.borrower = None

    def is_available(self):
        return self.borrower is None and self.condition != "broken"

pad = Gear("CTRL-01")
broken = Gear("CTRL-03", "broken")

print(pad.is_available())      # True
print(broken.is_available())   # False
```

Output:

```
True
False
```

`is_available` takes no arguments except `self`, because it only needs the object's own
data. Two objects, two different answers, from one method.

---

## The wrong version, and the error it produces

Forget `self` in the definition:

```python
class Gear:
    def __init__(self, tag):
        self.tag = tag
    def label():               # WRONG: no self
        return "gear"

pad = Gear("CTRL-01")
print(pad.label())
```

Output:

```
TypeError: Gear.label() takes 0 positional arguments but 1 was given
```

The "1 argument" you supposedly gave is `pad` itself. Python always hands the object to
the method, and the method has no parameter to catch it, because you left `self` out.
The fix is `def label(self):`.

### Write this down

> Python always passes the object to the method as the first argument. `self` is the
> parameter that catches it.

---

## Why the wrong version is tempting

`label` does not use the object, so it feels like it should not need `self`. But Python
does not know that. It passes the object to every method, whether the method uses it or
not, so every method definition needs `self` first. A method that ignores its object
still has to accept it.

The habit that prevents it: every method's first parameter is `self`, always, even when
the method never uses it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Method** | A function that belongs to a class and takes the object as `self`. |
| **`self`** | The specific object the method was called on. |
| **Call** | Running a method, with `object.method(arguments)`. |
| **Argument** | A value you pass at the call, after `self`. |
| **`is not None`** | The safe way to test whether an attribute has been set. |

---

## Self-check

**Question 1.** For the call `locker.check_out("CTRL-01", "NovaFox")`, name `self` and
name the other two arguments.

**Question 2.** Write the exact output.

```python
class Counter:
    def __init__(self):
        self.count = 0
    def bump(self):
        self.count = self.count + 1

a = Counter()
b = Counter()
a.bump()
a.bump()
b.bump()
print(a.count, b.count)
```

**Question 3.** A method is defined as `def reset():` and calling it raises a
`TypeError` about arguments. Explain what happened and give the fix.

---

### Answers

**1.** `self` is `locker`, the object before the dot. The other two arguments are
`"CTRL-01"` (the tag) and `"NovaFox"` (the borrower), which match the method's
parameters after `self`.

**2.** `2 1`. `a` and `b` are separate counters. Calling `bump` on `a` twice changed
`a.count` to 2, because `self` was `a` both times. Calling it on `b` once changed
`b.count` to 1. Each object kept its own count.

**3.** Python passed the object to `reset` as the first argument, but `reset` was
defined with no parameters, so it received one argument it could not accept. The fix is
`def reset(self):`, so `self` catches the object.
