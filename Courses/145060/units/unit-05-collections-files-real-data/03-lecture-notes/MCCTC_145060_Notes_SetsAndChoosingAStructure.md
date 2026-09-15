# Lecture Notes: Sets, and Choosing the Right Structure
## 145060 Programming · Unit 5 · Week 10, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W10_SetsAndChoosing.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W10_SetsAndChoosing.pptx)

If you missed class, you can learn this concept from this file alone. The timing
example is the one to run yourself, because your numbers will not match ours and that
difference is part of the lesson.

**Every program below was run on Python 3.13.7.** The output shown is the real output,
except where a set's printed order is noted as varying.

---

## Why this exists

You now have two structures. A list keeps order. A dictionary looks things up by name.

Plenty of questions are neither. Has this player already visited the roof? Is this
student ID on the sign-in list? How many **different** people signed up? Those are all
one question: **is it in there**. A list can answer it, slowly, by checking every item.
A set is built to answer it fast.

This lesson also does the thing the syllabus cares about most in this unit: choosing
between list, dictionary, and set on purpose, and saying what the wrong choice costs.

---

## The concept in plain language

**A set is a collection of unique values with no order.**

```python
visited = {"lobby", "hallway"}
```

- Curly braces with values and no colons. (Colons would make it a dictionary.)
- **Unique.** Adding a value that is already there changes nothing.
- **No order.** There is no first item, so there are no positions and no `[0]`.
- **Fast membership.** `"roof" in visited` is answered almost instantly, even with a
  huge set.

You give up order and duplicates. You get speed on one question. That is the whole
trade.

---

## Worked example 1: build, add, ask

```python
visited = {"lobby"}
visited.add("hallway")
visited.add("lobby")
print(visited)
print(len(visited))
print("roof" in visited)

sign_ups = ["Maya", "Theo", "Maya", "Jordan", "Theo"]
print(len(set(sign_ups)))
```

Output:

```
{'lobby', 'hallway'}
2
False
3
```

**The first line of output may be in a different order on your machine, or even on
your next run.** We ran a two-room version of this thirty times and saw
`{'lobby', 'hallway'}` fifteen times and `{'hallway', 'lobby'}` fifteen times. Python
makes no promise about the order a set prints in. Never write code that
depends on it. If you need a stable order for printing, use `sorted(visited)`, which
gives you a sorted list.

- `.add()` puts one value in. Adding `"lobby"` a second time did nothing, so the length
  is 2.
- `set(sign_ups)` builds a set from a list and throws away the duplicates. Five
  sign-ups, three different people.

---

## Worked example 2: comparing two groups

```python
my_classes = {"Programming", "English 11", "Chemistry", "Gym"}
friend_classes = {"Chemistry", "US History", "Programming", "Art"}
print(sorted(my_classes & friend_classes))
print(sorted(friend_classes - my_classes))
my_classes.discard("Gym")
my_classes.discard("Band")
print(sorted(my_classes))
```

Output:

```
['Chemistry', 'Programming']
['Art', 'US History']
['Chemistry', 'English 11', 'Programming']
```

| Operator | Meaning | Here |
|---|---|---|
| `a & b` | in both | classes you share |
| `a - b` | in `a` but not `b` | classes only your friend takes |
| `a \| b` | in either, no repeats | every class either of you takes |

`.discard()` removes a value if it is there and does nothing if it is not. Discarding
`"Band"`, which was never in the set, did not raise an error. (`.remove()` on a set
would have raised `KeyError`.)

---

## Worked example 3: the cost, measured

This is the example to run yourself.

```python
import time

# 100,000 made-up student ID codes, about the size of a big district's list.
id_list = []
for number in range(100_000):
    id_list.append(f"ID{number:06d}")
id_set = set(id_list)

# 1,000 lookups. Half are codes that are not there, the worst case for a list.
lookups = []
for number in range(99_500, 100_500):
    lookups.append(f"ID{number:06d}")

start = time.perf_counter()
for code in lookups:
    found = code in id_list
list_seconds = time.perf_counter() - start

start = time.perf_counter()
for code in lookups:
    found = code in id_set
set_seconds = time.perf_counter() - start

print(f"list: {list_seconds:.4f} seconds")
print(f"set:  {set_seconds:.6f} seconds")
```

Two notes on the code before the numbers. `100_000` is the number one hundred thousand;
Python lets you put underscores in a number so you can read it. And `f"ID{number:06d}"`
pads the number with zeros to six digits, so `42` becomes `ID000042`.

`time.perf_counter()` is a stopwatch. Read it before, read it after, and subtract.

**Real output, five runs on the Windows computer these notes were written on:**

```
list: 0.4635 seconds
set:  0.000161 seconds
list: 0.4671 seconds
set:  0.000174 seconds
list: 0.4660 seconds
set:  0.000159 seconds
list: 0.4647 seconds
set:  0.000161 seconds
list: 0.4631 seconds
set:  0.000162 seconds
```

The list took about 0.46 seconds for 1,000 lookups. The set took about 0.00016
seconds. On that machine, run by run, the set was between about 2,700 and 2,900 times
faster.

**Your numbers will be different.** A faster or slower computer, a different Python
version, or other programs running will all change them. Run it three times and look
at what stays the same: the gap.

**Why the gap exists, without the math.** To answer "is `ID100400` in this list," a
list has to compare it against every item, one at a time, until it finds it or runs out.
Half the lookups were for codes that are not there, so those checked all 100,000 items.
A set works out where a value would be stored and goes straight there, so its answer
takes about the same time whether it holds ten items or ten million.

Half a second sounds small. Put it inside a scanner that a thousand students walk past
before first bell, and it is the reason the line stops moving.

---

## Choosing the structure

**Ask what question your program asks most often.**

| If the main question is | Use | Because |
|---|---|---|
| What order did these happen in? Can one appear twice? | **list** | It keeps order and allows duplicates. |
| What is the value for this name or ID? | **dictionary** | It looks up by key directly. |
| Is this one in there? How many different ones? | **set** | Fast membership, duplicates removed. |

**And say the cost of the wrong choice out loud:**

| Wrong choice | What it costs |
|---|---|
| A list for "is it in there" on a big collection | Every check walks the whole list. It gets slower as the data grows. |
| A set when order matters | The order is gone, and it can change between runs. |
| A list of pairs instead of a dictionary | Every lookup becomes a loop you write, and forget, and get wrong. |
| A dictionary with made-up values only to get fast lookups | Confusing to read. That is what a set is for. |

### Sometimes the "slow" choice is right

The version 3 text adventure keeps its fourteen commands in a **list**, and the game
checks `command in COMMANDS` on every turn. That is a membership question, so why not a
set?

Because `help` prints the commands in a fixed order, and a set would scramble them. With
fourteen items, the speed difference is too small to measure. A good choice names what it
gives up. Fourteen is not a hundred thousand.

---

## The wrong version: empty braces

```python
visited = {}
visited.add("lobby")
```

```
    visited.add("lobby")
    ^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'add'
```

**Empty curly braces make an empty dictionary, not an empty set.** Dictionaries came
first in Python's history, so they got the braces. The error message tells you the truth:
you have a `dict`. An empty set is written `set()`.

### The second wrong version: asking a set for a position

```python
visited = {"lobby", "hallway"}
print(visited[0])
```

```
    print(visited[0])
          ~~~~~~~^^^
TypeError: 'set' object is not subscriptable
```

"Not subscriptable" means you cannot use square brackets on it. A set has no position 0,
because it has no order.

### And a third: a list inside a set

```python
seen = {["lobby", "hallway"]}
```

```
TypeError: unhashable type: 'list'
```

Sets, like dictionary keys, can only hold values that cannot change. A list can change,
so it cannot go in a set. Strings and numbers can.

---

## Why the wrong versions are tempting

**`{}` looks like the obvious empty set.** Every other set you have written used curly
braces.

**Printing a set looks ordered.** It shows the items in some order, so it is natural to
assume there is a first one.

**A list works for membership, and it is correct.** `code in id_list` gives the right
answer every time. Nothing crashes. It is only slow, and only on big data, which is
exactly the kind of problem you do not notice until real users show up. That is the
performance cousin of the bug that does not crash.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Set** | A collection of unique values with no order. |
| **Membership** | Whether a value is in a collection. Asked with `in`. |
| **`.add(x)`** | Adds `x`. Does nothing if it is already there. |
| **`.discard(x)`** | Removes `x` if present. No error if not. |
| **`set(some_list)`** | A new set holding the unique values of the list. |
| **`set()`** | An empty set. `{}` is an empty dictionary. |
| **`&`, `-`, `\|`** | In both, in the first but not the second, in either. |
| **`sorted(a_set)`** | A sorted list of the set's values, for stable printing. |
| **`time.perf_counter()`** | A stopwatch reading, in seconds, for timing code. |
| **Not subscriptable** | You used square brackets on something that has no positions or keys. |
| **Unhashable** | A value that can change, so it cannot be a set item or dictionary key. |

---

## Self-check

**Question 1.** Write the exact output.

```python
rsvps = ["Ava", "Dev", "Ava", "Luis", "Dev", "Ava"]
unique = set(rsvps)
unique.add("Priya")
unique.add("Luis")
print(len(rsvps), len(unique))
print("Dev" in unique, "Theo" in unique)
print(sorted(unique))
```

**Question 2.** Pick list, dictionary, or set for each, and name the cost of picking
wrong in one sentence.

- A text adventure's record of which rooms you have ever entered
- A school store's price for each item
- The order runners crossed the finish line
- Every word that has already been used in a word game, checked every turn

**Question 3.** A classmate says: "Sets are faster, so I am changing all my lists to
sets." Give the strongest reason they are right and the strongest reason they are wrong.

---

### Answers

**1.**

```
6 4
True False
['Ava', 'Dev', 'Luis', 'Priya']
```

Six items in the list. The set starts with three unique names, gains Priya, and adding
Luis again changes nothing, so four.

**2.**

| Situation | Structure | Cost of the wrong choice |
|---|---|---|
| Rooms ever entered | set | A list would count a room twice if you do not check, and the only question is "been here?" |
| Price per item | dictionary | A list would make every price lookup a search loop. |
| Finish order | list | A set would lose the order, which is the whole result. |
| Words already used | set | A list gets slower every turn as the game goes on. |

**3.** **Right:** for any collection where the main question is membership, especially a
big one, a set is dramatically faster, as the timing showed, and it removes duplicates for
free. **Wrong:** a set destroys order and duplicates. A playlist, a queue, a leaderboard,
or anything printed in a fixed order breaks, and it breaks quietly, because the program
still runs. The right structure depends on the question, not on which one is fastest.
