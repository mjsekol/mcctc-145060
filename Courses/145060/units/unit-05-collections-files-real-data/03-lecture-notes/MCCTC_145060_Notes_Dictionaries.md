# Lecture Notes: Dictionaries
## 145060 Programming · Unit 5 · Week 10, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W10_Dictionaries.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W10_Dictionaries.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example, and pay attention to the two versions of the same typo near the bottom.

**Every program below was run on Python 3.13.7.** The output shown is the real output.

---

## Why this exists

Open `find_exit` in your text adventure version 2. It is a staircase of `if` and
`elif`: if the room is the lobby, if the direction is north, return the hallway. Room
after room, direction after direction.

What that function really holds is a map. This room, this direction, that room. A map
is data, and burying it in `if` statements means a new room costs you new code in
several places.

A list cannot fix this. A list finds things by **position**, and nobody thinks of
"north" as position 0. You need a structure that finds things by **name**.

---

## The concept in plain language

**A dictionary stores pairs. You give it a key, and it gives you back the value paired
with that key.**

```python
exits = {"north": "hallway", "east": "archive"}
```

- Curly braces. Each pair is written `key: value`. Pairs are separated by commas.
- `"north"` is a key. `"hallway"` is its value.
- **Keys are unique.** North from one room cannot lead to two places.
- Values can repeat. Two directions could lead to the same room.
- There are no positions. You never ask for item number 2. You ask for `"north"`.
- Dictionaries remember the order you added keys, so printing one shows that order.

Keys are usually strings. They can also be numbers. A key cannot be a list, because a
list can change, and a key that changes would get lost:

```python
d = {"Ava": 7}
d[["a"]] = 1
```

```
TypeError: unhashable type: 'list'
```

---

## Worked example 1: read, check, add, replace, walk

```python
exits = {"north": "hallway", "east": "archive"}
print(exits["north"])
print("west" in exits)

exits["west"] = "studio"
print(exits)
print(len(exits))

for direction, room in exits.items():
    print(direction, "->", room)

print(exits.get("down"))
print(exits.get("down", "no exit that way"))
```

Output:

```
hallway
False
{'north': 'hallway', 'east': 'archive', 'west': 'studio'}
3
north -> hallway
east -> archive
west -> studio
None
no exit that way
```

- `exits["north"]` reads the value for a key.
- `"west" in exits` checks whether a **key** exists. It does not search the values.
- Assigning to a new key adds a pair. Assigning to an existing key replaces its value.
- `.items()` gives you each key and value together, so the loop can name both.
- `.get(key)` returns `None` instead of crashing when the key is missing, and
  `.get(key, default)` returns your default instead. More on when that is a mistake
  below.

---

## Worked example 2: change and remove

```python
jersey_numbers = {"Ava": 7, "Marcus": 23, "Priya": 11}
jersey_numbers["Dev"] = 4
jersey_numbers["Ava"] = 10
del jersey_numbers["Marcus"]
print(jersey_numbers)
print(list(jersey_numbers.keys()))
print(list(jersey_numbers.values()))
```

Output:

```
{'Ava': 10, 'Priya': 11, 'Dev': 4}
['Ava', 'Priya', 'Dev']
[10, 11, 4]
```

`del` removes a pair. Ava's key kept its place when her number changed, because
replacing a value does not move the key. `.keys()` and `.values()` give you one
side of each pair, and wrapping them in `list()` turns them into ordinary lists.

---

## Worked example 3: counting, the pattern you will write all year

```python
votes = ["tacos", "pizza", "tacos", "wings", "tacos", "pizza"]
counts = {}
for vote in votes:
    if vote in counts:
        counts[vote] += 1
    else:
        counts[vote] = 1
print(counts)
```

Output:

```
{'tacos': 3, 'pizza': 2, 'wings': 1}
```

If the key is already there, add one. If it is not, start it at one. The lunch vote,
songs per artist, hoodies per size, visits per room. Same six lines.

A shorter version you will see online uses `.get` with a default of 0:

```python
votes = ["tacos", "pizza", "tacos", "wings", "tacos", "pizza"]
counts = {}
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
print(counts)
```

```
{'tacos': 3, 'pizza': 2, 'wings': 1}
```

Same result. Use whichever you can explain. In an interview, the longer version is
clearer to talk through.

---

## Worked example 4: dictionaries inside dictionaries

This is the shape your version 3 map takes.

```python
rooms = {
    "lobby": {"name": "Lobby", "exits": {"north": "hallway"}},
    "hallway": {"name": "Hallway", "exits": {"south": "lobby", "east": "archive"}},
}
room = "hallway"
print(rooms[room]["name"])
for direction in rooms[room]["exits"]:
    print("Exit:", direction)
destination = rooms[room]["exits"]["south"]
print("Walking south takes you to the", rooms[destination]["name"])
```

Output:

```
Hallway
Exit: south
Exit: east
Walking south takes you to the Lobby
```

Read `rooms[room]["exits"]["south"]` from left to right: the rooms dictionary, then this
room's dictionary, then its exits dictionary, then the value for south. Looping over a
dictionary directly, as in `for direction in ...`, walks its **keys**.

Your whole `find_exit` function becomes one line:
`rooms[room]["exits"][direction]`, after checking `direction in rooms[room]["exits"]`.

---

## The wrong version, twice

### The loud version

```python
exits = {"north": "hallway", "east": "archive"}
print("You walk to the", exits["nroth"])
```

```
    print("You walk to the", exits["nroth"])
                             ~~~~~^^^^^^^^^
KeyError: 'nroth'
```

A typo in a key, and square brackets refuse to guess. Python stops and prints the exact
key it could not find. You see `nroth`, you fix it. Ten seconds.

### The quiet version

Somebody tells you `.get()` is safer because it never crashes.

```python
exits = {"north": "hallway", "east": "archive"}
print("You walk to the", exits.get("nroth"))
```

```
You walk to the None
```

**No error.** The same typo now produces a sentence that looks almost right and walks
the player into a room called `None`. In a real game, the next line tries to describe
room `None`, and the crash happens somewhere else entirely, far from the typo.

> **The dangerous bugs are the ones that do not crash.** `.get()` did not fix the bug.
> It hid it, and moved the eventual failure somewhere harder to find.

### When `.get()` is the right tool

`.get()` with a default is correct when a missing key is a **normal answer**, not a
mistake:

```python
prices = {"nachos": 4.50, "pretzel": 3.00}
print(prices.get("hot dog", "not on the menu"))
```

```
not on the menu
```

A customer asking for something that is not sold is normal. A typo in your own code is
not. The test: **if this key were missing, would that be a bug?** If yes, use square
brackets and let it crash while you are testing.

---

## Why the wrong version is tempting

**"It never crashes" sounds like a feature.** Nobody likes red text, and `.get()` makes
it go away.

**Many tutorials use `.get()` everywhere.** It is genuinely useful, so it shows up
constantly, often without the reason.

**The quiet failure shows up later.** You test the happy path, it works, and the typo
only fires when a player walks a direction you did not try.

---

## One more trap: dictionaries do not have positions

```python
scores = {"Maya": 90, "Theo": 85}
print(scores[0])
```

```
KeyError: 0
```

Python did not complain about a position. It looked for a **key** called `0`, and there
is none. If you want the first player, you need a list, or you need to know their name.

---

## When a dictionary is the right choice

| Use a dictionary when | Example |
|---|---|
| You look things up by a name or ID | A room by its id, a price by item |
| You count how many of each | Votes per food, songs per artist |
| You translate one spelling into another | `"med"` and `"medium"` both become `"M"` |
| Each value needs a label | A player's points, games, and position |

---

## Vocabulary

| Term | What it means |
|---|---|
| **Dictionary** | A collection of key and value pairs. Written with curly braces. |
| **Key** | The name you look up. Unique within one dictionary. |
| **Value** | What is stored for a key. |
| **`d[key]`** | Reads the value. `KeyError` if the key is missing. |
| **`d[key] = value`** | Adds a new pair or replaces an existing value. |
| **`key in d`** | Checks whether a key exists. Does not search values. |
| **`.get(key, default)`** | Reads the value, or returns the default if the key is missing. |
| **`.items()`** | Every key with its value, for looping over both. |
| **`.keys()` / `.values()`** | Only the keys / only the values. |
| **`del d[key]`** | Removes a pair. |
| **`KeyError`** | The key you asked for is not in the dictionary. |
| **Nested dictionary** | A dictionary whose values are dictionaries. |

---

## Self-check

**Question 1.** Write the exact output.

```python
stock = {"hoodie": 12, "beanie": 5}
stock["beanie"] = stock["beanie"] - 2
stock["sticker"] = 40
print(stock)
print("hat" in stock, len(stock))
```

**Question 2.** A classmate's program prints `Your locker is None` for one student and
never crashes. Their code is below. What is the most likely cause, and what change makes
the real problem visible?

```python
lockers = {"Ava": 214, "Marcus": 108, "Priya": 330}
name = "Marcos"
print("Your locker is", lockers.get(name))
```

**Question 3.** Your version 2 `find_exit` has a branch for every room and direction.
Write the dictionary that replaces it for these three rooms: the lobby leads north to
the hallway; the hallway leads south to the lobby and east to the archive; the archive
leads west to the hallway.

---

### Answers

**1.**

```
{'hoodie': 12, 'beanie': 3, 'sticker': 40}
False 3
```

**2.** The name is misspelled, `Marcos` instead of `Marcus`, so the key does not exist
and `.get()` returns `None` instead of crashing. Switching to `lockers[name]` makes it
crash with `KeyError: 'Marcos'`, which names the typo exactly. If a missing name is a
normal situation, the right fix is to check `name in lockers` and print a clear message.

**3.**

```python
exits = {
    "lobby": {"north": "hallway"},
    "hallway": {"south": "lobby", "east": "archive"},
    "archive": {"west": "hallway"},
}
```

The lookup that replaces the whole function is `exits[room][direction]`, after checking
`direction in exits[room]`.
