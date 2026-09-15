# Lecture Notes: Lists
## 145060 Programming · Unit 5 · Week 10 · Monday, November 9

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W10_Lists.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W10_Lists.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example. The one near the bottom does not crash, and that is the one to type twice.

**Every program below was run on Python 3.13.7.** The output shown is the real output.

---

## Why this exists

Open your text adventure version 2 and search for the word `fuse`.

It appears in a global variable, in `has_item`, in `take_item`, in `use_item`, and in
`describe_inventory`. Every item you can carry needs its own variable and its own
branch in four functions. Adding a third item means editing five places. Forgetting
one of them does not crash. It gives a wrong answer.

That was clumsy on purpose. You did not have a way to keep many values under one name.
Now you do.

---

## The concept in plain language

**A list is one name that holds many values, in order.**

```python
inventory = ["flashlight", "fuse"]
```

Four facts about a list, and each one decides when you use it:

| Fact | What it means for you |
|---|---|
| **It keeps order** | The first thing you add stays first. Good for a queue, a playlist, arrival order. |
| **It allows duplicates** | The same value can appear twice. A playlist can repeat a song. |
| **Positions start at 0** | Same counting as the strings you sliced in Unit 1. |
| **It can change** | You can add, remove, and replace items while the program runs. |

A list can hold any type: strings, numbers, even other lists and dictionaries. Most
of the time every item in one list is the same kind of thing.

---

## Worked example 1: build, count, reach in, change

```python
inventory = ["flashlight", "fuse"]
print(inventory)
print(len(inventory))
print(inventory[0])
print(inventory[-1])

inventory.append("key card")
print(inventory)
print("fuse" in inventory)

inventory.remove("fuse")
print(inventory)

for item in inventory:
    print("You are carrying:", item)

last = inventory.pop()
print(last, inventory)
```

Output:

```
['flashlight', 'fuse']
2
flashlight
fuse
['flashlight', 'fuse', 'key card']
True
['flashlight', 'key card']
You are carrying: flashlight
You are carrying: key card
key card ['flashlight']
```

Read it line by line:

- `len()` counts the items. The last position is always `len - 1`.
- `[0]` is the first item and `[-1]` is the last, exactly like strings.
- `.append()` adds one item to the end.
- `in` asks a question and answers `True` or `False`.
- `.remove()` takes out the **first** item equal to what you give it.
- A `for` loop visits every item, in order. It is the loop you know, pointed at a list.
- `.pop()` removes the last item **and hands it back to you**, so you can keep it.

Compare the `for` loop with your version 2 `describe_inventory`. Five lines of branches
become two lines.

---

## Worked example 2: a line of people

A list is the natural shape for anything that waits its turn.

```python
lunch_line = []
lunch_line.append("Jordan")
lunch_line.append("Priya")
lunch_line.append("Luis")
print(lunch_line)

served = lunch_line.pop(0)
print("Now serving:", served)
print("Still waiting:", lunch_line)
print("Luis is number", lunch_line.index("Luis") + 1, "in line")
```

Output:

```
['Jordan', 'Priya', 'Luis']
Now serving: Jordan
Still waiting: ['Priya', 'Luis']
Luis is number 2 in line
```

Two new tools. `.pop(0)` removes the item at position 0, the front of the line, and
gives it back. `.index("Luis")` tells you where `"Luis"` is. The `+ 1` is there because
people count from 1 and Python counts from 0.

---

## Worked example 3: numbers in a list

```python
quiz_scores = [88, 92, 79, 95, 84]
print(len(quiz_scores), sum(quiz_scores), max(quiz_scores), min(quiz_scores))
print(sum(quiz_scores) / len(quiz_scores))
print(quiz_scores[1:3])
quiz_scores.sort()
print(quiz_scores)
print(sorted(["Theo", "ava", "Maya"]))
```

Output:

```
5 438 95 79
87.6
[92, 79]
[79, 84, 88, 92, 95]
['Maya', 'Theo', 'ava']
```

- `sum`, `max`, and `min` work on a list of numbers. The average is the sum divided by
  the count.
- Slicing works like strings: `[1:3]` is positions 1 and 2, up to but not including 3.
- `.sort()` changes the list itself. `sorted()` gives you a new sorted list and leaves
  the original alone.
- **Watch the last line.** `"ava"` sorted after `"Theo"`. Capital letters come before
  lowercase letters in Python's ordering, because their character codes are smaller.
  That is Week 4's encoding lesson turning up in a place you would not expect.

---

## The two loud errors

Both of these crash, and both tell you exactly what happened.

**Reaching past the end:**

```python
inventory = ["flashlight", "key card"]
print(inventory[2])
```

```
    print(inventory[2])
          ~~~~~~~~~^^^
IndexError: list index out of range
```

Two items means positions 0 and 1. There is no position 2.

**Removing something that is not there:**

```python
inventory = ["flashlight", "key card"]
inventory.remove("fuse")
```

```
    inventory.remove("fuse")
    ~~~~~~~~~~~~~~~~^^^^^^^^
ValueError: list.remove(x): x not in list
```

If a value might be missing, check with `in` before you remove it.

---

## The wrong version, and what it does instead of an error

Your friend has heard enough of one band. Remove every song by Static Lemonade:

```python
queue = ["Static Lemonade - Porch Light", "Static Lemonade - Snow Day",
         "Mira Vance - Group Chat", "Juno Okafor - Low Battery"]

# Your friend says: no more Static Lemonade.
for song in queue:
    if song.startswith("Static Lemonade"):
        queue.remove(song)

print(queue)
```

Output:

```
['Static Lemonade - Snow Day', 'Mira Vance - Group Chat', 'Juno Okafor - Low Battery']
```

**No error. One Static Lemonade song survived.**

Here is what happened, one pass at a time:

1. The loop is at position 0, `Porch Light`. It matches, so it is removed.
2. Every song slides one place left. `Snow Day` is now at position 0.
3. The loop moves on to position 1, which is now `Group Chat`. **It never looks at
   `Snow Day`.**

Changing a list while a `for` loop is walking through it skips the item after every
removal. It does not crash. It gives you a wrong answer that looks finished.

### The fix: build a new list

```python
queue = ["Static Lemonade - Porch Light", "Static Lemonade - Snow Day",
         "Mira Vance - Group Chat", "Juno Okafor - Low Battery"]

kept = []
for song in queue:
    if not song.startswith("Static Lemonade"):
        kept.append(song)
queue = kept

print(queue)
```

Output:

```
['Mira Vance - Group Chat', 'Juno Okafor - Low Battery']
```

Walk the old list without touching it. Append everything you want to keep. Point the
name at the new list when you are done.

> **You have seen this shape before.** `"12" * 3` gave `121212` in Unit 1 and nothing
> complained. A slice that stopped one place early gave `202`. This is the same kind
> of bug: **the dangerous bugs are the ones that do not crash.**

---

## Why the wrong version is tempting

**It reads exactly like the English.** For each song, if it is by that band, remove
it. That is how you would say it out loud.

**It works on most test data.** If the two Static Lemonade songs are not next to each
other, nothing is skipped and the output is correct. You can test it three times, see
the right answer three times, and ship it.

**Nothing warns you.** Python allows changing a list during a loop. It is legal. It is
almost never what you meant.

The defense is a habit: **never change the list a `for` loop is reading. Build a new
one.**

---

## One more thing to know now: two names, one list

```python
inventory = ["flashlight"]
backpack = inventory
backpack.append("fuse")
print(inventory)
```

Output:

```
['flashlight', 'fuse']
```

`backpack = inventory` does not copy the list. It ties a second name to the **same**
list, which is the name tag model from Unit 1. Change it through either name and both
names see the change. If you want a separate copy, write `list(inventory)`. Thursday's
lesson depends on this.

---

## When a list is the right choice

| Use a list when | Do not use a list when |
|---|---|
| Order matters | You mostly look things up by a name |
| The same value can appear twice | You only ever ask "is it in there" on a big collection |
| You usually go through every item | Each value needs a label, like a player's points |

Tomorrow's structure, the dictionary, handles the second column.

---

## Vocabulary

| Term | What it means |
|---|---|
| **List** | One name holding many values in order. Written with square brackets. |
| **Item** or **element** | One value inside a list. |
| **Index** | An item's position. Starts at 0. |
| **`len()`** | How many items. The last index is `len - 1`. |
| **`.append(x)`** | Adds `x` to the end. |
| **`.remove(x)`** | Removes the first item equal to `x`. `ValueError` if there is none. |
| **`.pop()`** | Removes and returns the last item. `.pop(0)` does the first. |
| **`.index(x)`** | Returns the position of the first `x`. |
| **`in`** | Asks whether a value is in the list. |
| **`.sort()` / `sorted()`** | Sorts the list itself / returns a new sorted list. |
| **`IndexError`** | You asked for a position that does not exist. |
| **Alias** | A second name tied to the same list. Not a copy. |

---

## Self-check

**Question 1.** Write the exact output.

```python
bag = ["charger", "notebook"]
bag.append("water bottle")
bag.remove("notebook")
print(len(bag), bag[-1])
print("notebook" in bag)
```

**Question 2.** This is supposed to remove every score under 70 and keep the rest. Say
what it prints, whether an error appears, and why.

```python
scores = [65, 62, 90, 58, 77]
for score in scores:
    if score < 70:
        scores.remove(score)
print(scores)
```

**Question 3.** For each, say whether a list is a good choice, and why in one sentence.

- The order songs will play at a party
- Looking up a student's locker number by their name
- The moves a chess player made, in order

---

### Answers

**1.**

```
2 water bottle
False
```

After the append the list has three items. Removing `"notebook"` leaves two, and the
last one is `"water bottle"`.

**2.** It prints:

```
[62, 90, 77]
```

**No error.** `62` should have been removed and survived. When `65` was removed, `62`
slid into position 0, and the loop had already finished position 0, so it went on to
`90` and never checked `62`. The fix is to build a new list of the scores to keep.

**3.**

| Situation | List? | Why |
|---|---|---|
| Party song order | Yes | Order is the whole point, and a song could play twice. |
| Locker number by name | No | You look it up by a name. That is tomorrow's dictionary. |
| Chess moves in order | Yes | The order is the game. Replaying it means walking the list. |
