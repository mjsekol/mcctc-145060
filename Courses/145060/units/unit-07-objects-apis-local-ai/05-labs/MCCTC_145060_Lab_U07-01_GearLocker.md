# Lab U7-01: Gear Locker
## 145060 Programming · Unit 7 · Week 16

**Gate:** 3 (open tooling). **Duration:** three Build blocks, Tuesday through Thursday.
**Competencies:** 5.3.12 (classes, objects, methods), 5.5.5 (naming and comments).

**Files for this lab are in** `lab-u07-01-files/`: `gear_locker.py` (the starter) and
`test_gear_locker.py` (the acceptance tests). Work in a copy inside your own repository.

---

## The scenario

The esports club lends controllers and headsets. Right now the loan list is a pile of
dictionaries, and it has already lied to somebody: a controller showed as available when
it was out. Somebody has to check gear out, take it back, and print a report that is
correct.

## What you will build

Two classes. `Gear` is one piece of equipment that knows its own state and can check
itself out. `GearLocker` is the whole cabinet, which holds `Gear` objects and finds the
right one by its tag. Borrowers are gamer tags, never real names.

---

## Before you start

Copy `gear_locker.py` and `test_gear_locker.py` into your repository. Run the starter:

```
python gear_locker.py
```

It runs and does almost nothing useful. Read the dictionary version at the top of the
file. It has a real bug in it, and finding that bug is step 2.

Run the tests. They all fail, because you have not written the classes yet:

```
python -m unittest test_gear_locker.Part1Tests
```

**A note on the tests.** In Units 4 through 6 you tested with a `check(label, actual,
expected)` helper you wrote yourself. `test_gear_locker.py` uses Python's built-in
`unittest`, which is that helper grown up. `assertEqual` is your `check`. `assertRaises`
is a check that some code raises an error on purpose. `unittest` needs classes to group
tests, which is exactly the thing you learn this week, so this is the right moment to meet
it. Read the anchor project's `v4/test_adventure.py` to see the same tool on a real
project.

---

## Part 1: Tuesday, __init__ and attributes

### Step 1. Starter running and committed
Run it, read it, commit it.
**Observable result:** the starter prints its lines, and `git log --oneline` shows a new
commit.

### Step 2. Find the bug in the dictionary version
Read `make_gear_dict`, `lend_dict`, and `is_available_dict` at the top. One of them has a
typo that means a lent-out item still shows as available. Write what you found in a
comment.
**Observable result:** you can say which line stores the borrower under the wrong key,
and why `is_available_dict` never sees it. This is the exact kind of bug a class prevents.

### Step 3. Write the Gear class
Replace TODO 1 and TODO 2. Write `class Gear` with an `__init__` that takes `tag`,
`kind`, and a `condition` that defaults to `"good"`. Store all three on `self`, plus
`borrower` set to `None` and `times_loaned` set to `0`. Raise `ValueError` if the
condition is not in `CONDITIONS`.
**Observable result:** `python -m unittest test_gear_locker.Part1Tests` passes all five.

### Step 4. Prove two objects do not share
Make two `Gear` objects, change the condition of one, and print the condition of the
other.
**Observable result:** changing one does not change the other, because each got its own
attributes in `__init__`. Commit.

### Acceptance criteria, Part 1
1. `python gear_locker.py` runs with no traceback
2. All five `Part1Tests` pass
3. You can explain why two `Gear` objects do not share attributes

---

## Part 2: Wednesday, methods and self

### Step 5. Write is_available
Return `True` only when the gear is in the cabinet (`borrower is None`) and not broken.
**Observable result:** `is_available` returns a real `True` or `False`, checked by the
test.

### Step 6. Write check_out
Take a `borrower`. Refuse if the gear is broken or already out, with a clear message.
Otherwise record the borrower, add one to `times_loaned`, and return a message.
**Observable result:** checking out twice gives a "already out" message the second time,
and `times_loaned` is 1, not 2.

### Step 7. Write check_in
Take a `condition`. Refuse if the gear is not out. Otherwise clear the borrower and record
the returned condition.
**Observable result:** after check-in, `borrower` is `None` and the condition is updated.

### Step 8. Write label
Return one line describing the gear, including its tag and where it is. No newline inside.
**Observable result:** `label()` returns a single line containing the tag.

### Acceptance criteria, Part 2
4. All six `Part2Tests` pass
5. `check_out` on already-out gear does not increase `times_loaned` a second time

---

## Part 3: Thursday, objects working together

### Step 9. Write the GearLocker class
`__init__` makes an empty `items` dictionary. Write `add`, `find` (match a tag in any
case, trimmed), `check_out`, `check_in`, `available`, and `report`.
**Observable result:** `find("ctrl-01")` and `find("CTRL-01")` return the same gear.

### Step 10. Write build_locker
Return a `GearLocker` holding the club's four pieces of gear: `CTRL-01` good, `CTRL-02`
worn, `CTRL-03` broken, and `HEAD-01` a headset.
**Observable result:** `python -m unittest test_gear_locker.Part3Tests` passes all six.

### Step 11. Read the anchor project
Open the text adventure `v4/game.py`. Find `Room`, `Player`, and `Game`. In a comment in
your lab file, match one `Gear` method to one method on `Room` or `Player` that does the
same kind of job.
**Observable result:** a comment naming a real match, for example `Gear.check_out`
changing the gear's state the way `Player.pick_up` changes the player's.

### Step 12. README and push
Three sections: what it is, how to run it and the tests, and one thing you learned about
classes that you did not know Monday.
**Observable result:** README renders on GitHub, tests all pass, pushed.

### Acceptance criteria, Part 3
6. All six `Part3Tests` pass, so all 17 tests pass together
7. The anchor comment names a real method match

---

## Acceptance criteria, full lab

- [ ] `python -m unittest test_gear_locker` reports 17 passed
- [ ] Every attribute is created in `__init__`, none on the class body
- [ ] `check_out` refuses broken and already-out gear
- [ ] `find` matches tags in any case
- [ ] README has all three sections
- [ ] The anchor comment names a real `Gear`-to-`Room`-or-`Player` match
- [ ] Three or more commits with messages saying why
- [ ] Pushed

---

## If it breaks

### 1. TypeError about positional arguments

```
TypeError: Gear.is_available() takes 0 positional arguments but 1 was given
```

**Cause:** you left `self` out of the method definition. Python always passes the object,
and the method needs `self` to catch it. Add `self` as the first parameter.

### 2. AttributeError, no attribute

```
AttributeError: 'Gear' object has no attribute 'borrower'
```

**Cause:** you did not create `self.borrower` in `__init__`, or you spelled it
differently there. Every attribute a method uses must be created in `__init__`.

### 3. Two objects share a list or dictionary

**Cause:** you put `items = {}` on the class body instead of inside `__init__`. Move it
into `__init__` as `self.items = {}` so each object gets its own. No error appears, which
is why the test `test_two_lockers_do_not_share_gear` exists.

### 4. A method prints instead of returns

**Cause:** the tests check the return value. If your method uses `print` instead of
`return`, the test sees `None`. Return the string; let the caller print it.

---

## Stretch goal

Add a `Member` class with a gamer tag and a list of tags they currently hold. Give the
locker a `check_out` that also records the loan on the member, and a method that lists
everything one member has out. Keep borrowers as gamer tags, never real names.

Then answer in your README: what happens if two members try to check out the same gear?
Which object should hold the rule that stops it, and why?

---

## Submission checklist

- [ ] `python -m unittest test_gear_locker` reports 17 passed
- [ ] No attribute is defined on a class body
- [ ] Tested by hand: check out, check in, and report all read correctly
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still unsure what `self` is at 20 minutes into Part 2 | SCAFFOLDED |
| Working steadily, asking about wording rather than mechanics | STANDARD |
| Finished Part 3 early, or asked about inheritance before it was taught | EXTENDED |
| Says a gear locker is pointless, or is not in a club | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** the `Gear.__init__` is already written for you, with all five attributes.
  You write the methods and the `GearLocker`.
- **Steps:** Part 1 becomes reading and running the given `__init__` and writing the
  Part 4 dictionary-bug comment. Part 3 drops `report`; the locker only needs `add`,
  `find`, `check_out`, and `available`.
- **Step 4 stays.** Do not cut the two-objects proof. It is the point of the day.
- **Checkpoints:** show you the terminal after Part 1 and after Part 2.

**Acceptance criteria:** `Part1Tests` and `Part2Tests` pass, plus `add`, `find`, and
`check_out` on the locker. A student who completes this fully earns what a STANDARD
student earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not taught.

**Added requirement.** A headset and a controller behave almost the same, but a headset
should also track whether its ear cushions have been replaced. Make `Headset` a separate
kind of gear that has everything `Gear` has plus a `cushions_replaced` flag, without
copying the whole `Gear` class.

**Hint, not the answer.** Python lets one class build on another, so the new class gets
everything the first one has and adds to it. Read the "Inheritance" section of
`https://docs.python.org/3/tutorial/classes.html` and look for how a class names a parent
in its `class` line, and how `super().__init__(...)` calls the parent's setup. This is
the first idea of 145065, so you are getting a head start.

**The honest warning:** it is tempting to copy the whole `Gear` class and add one attribute.
That works and it is exactly what inheritance exists to avoid. If you copy it, you now
have two `check_out` methods to fix every time. Doing it with inheritance is the point.

**Acceptance criteria:** all STANDARD criteria, plus a `Headset` that reuses `Gear`'s
methods without copying them, plus a README note on what breaks if you had copied instead.

---

## APPLIED

**For the student who says this does not apply to them.** Same skills, different cabinet.

**Changed scenario.** Model something you actually lend or track: library books, a tool
shed, phone chargers in a classroom, board games at a game night, camera gear. Pick one
thing that gets checked out and returned.

**What you build.** Two classes: one `Item` that knows its own state and can check itself
out and in, and one holder that finds items by an id and reports what is available.

**The extra requirement that makes it the same lab.** Your README must include a section
called `The rules` listing at least three rules an item enforces about itself, for
example "a damaged book cannot be checked out." At least one rule must live on the item,
not the holder, and you must say why.

**Acceptance criteria:** all STANDARD criteria applied to your chosen domain, plus
`The rules` section, plus one rule that lives on the item with a reason.

**Grading:** same scale. Requirements Fit is judged on whether the rules are enforced by
the right object, which is harder than the standard version, because you chose the domain
and the README has to justify where each rule lives.
