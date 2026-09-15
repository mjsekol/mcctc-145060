# Additional Resources · Week 15
## 145060 Programming · Week 15
### Topic: classes, objects, and methods

Links marked **Confident** or **[VERIFY]**, same standard as every week.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Python Tutorial, Classes chapter | Tue-Thu | On-level | 30 min |
| 2 | Think Python 3e, classes and objects chapters | Wed | On-level | 30 min |
| 3 | Python Tutor | Tue-Wed | Remediation | 15 min |
| 4 | Official docs: a first look at classes | Tue | On-level | 15 min |
| 5 | Real-world OOP article | Thu | Extension | 12 min |
| 6 | The anchor project v4 game.py | Thu | Extension | 20 min |
| 7 | SQ-12 Read the Source | Fri | Extension | 2 blocks |

---

## 1. Primary reading

**The Python Tutorial, the chapter titled "Classes"** ·
`https://docs.python.org/3/tutorial/classes.html` · **Confident.**

**Why this one.** It is the primary source, it is free, and its early sections cover exactly
this week: defining a class, `__init__`, instances, and methods. It goes further than the
week does; that is fine.

**Skip:** inheritance, class versus instance variables beyond the basics, and private
variables. Those are 145065. Read down to and including "Instance Objects" and "Method
Objects."

---

## 2. Second reading, gentler

**Think Python, 3rd edition, the chapters on classes and objects** ·
`https://allendowney.github.io/ThinkPython/` · **Confident** for the site, **[VERIFY]** the
exact chapter numbers, which shift between editions.

**Why this one.** Downey builds classes slowly, one idea per section, with small examples.
Assign it to any student who found the official tutorial dense.

---

## 3. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Paste Tuesday's shared-list trap and step through it:

```python
class Locker:
    items = []
    def add(self, tag):
        self.items.append(tag)

a = Locker()
b = Locker()
a.add("CTRL-01")
```

Watching one list with two arrows pointing at it does more for the class-attribute bug than
any explanation.

---

## 4. Official documentation, first look

`https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes` · **Confident.**

**Assign a question, not the page.**

> Read "Instance Objects." In one sentence, what is the difference between a data attribute
> and a method, and how do you call each?

That settles Monday's parentheses trap from the primary source.

---

## 5. A current article on why classes exist

Search for a recent, reputable article titled something like **"When to use a class in
Python"** or a plain-English piece on object-oriented programming in real codebases. ·
**[VERIFY]** the URL before assigning; good ones move.

**Why this one.** Students ask "when would I actually use this." A working developer's take
on when a class earns its place answers it better than a textbook. If you cannot verify a
current one, run the class discussion instead: name three things in an app they use, and
ask which would be classes.

---

## 6. The anchor project, read as a real example

`Courses/145060/anchor-project/text-adventure/v4/game.py` · **Confident**, it is in this
repository.

**Why this one.** It is the destination. `Room`, `Player`, and `Game` are the gear locker
pattern at project size. Read the three class definitions and match each `Gear` method to a
method here. This is Thursday's Build 2.

---

## 7. Side quest

**SQ-12 Read the Source.** A quest about reading unfamiliar code well enough to explain it,
which is exactly the skill of reading the anchor. Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. · **[VERIFY]** the catalog for the
current SQ-12 entry.

---

## For the student who is behind

1. Python Tutor with the shared-list example, stepped one line at a time
2. The `Notes_WhyClasses` and `Notes_MethodsAndSelf` lecture notes, Part by Part, typing
   every example
3. Rewrite the `Gear` class from an empty file without looking at their old one

Do not assign all seven. A student who is behind and gets seven links reads none.
