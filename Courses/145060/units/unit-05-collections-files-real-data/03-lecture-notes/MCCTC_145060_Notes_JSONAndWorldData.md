# Lecture Notes: JSON and Moving Data Out of Code
## 145060 Programming · Unit 5 · Week 11 · Monday, November 16

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W11_JSONWorldData.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W11_JSONWorldData.pptx)

If you missed class, you can learn this concept from this file alone. Run the round trip
example first, then break the file on purpose with both of the errors near the bottom.

**Every program below was run on Python 3.13.7.** The output shown is the real output.
One error message in this file is newer wording that should be confirmed on Python 3.14;
it is marked where it appears.

---

## Why this exists

Right now your text adventure's world lives inside `adventure.py`. Every room name, every
description, every exit is Python code. That causes three problems:

1. **Only a programmer can change the world.** A friend who writes great room
   descriptions cannot add one without editing Python, and one stray quote breaks the
   game.
2. **Nothing survives closing the program.** Every value lives in memory and vanishes
   when the program ends.
3. **The code and the content are tangled.** Fixing a typo in a description means
   touching the same file as the game rules.

The fix is to store data in a **file**, in a format that people can read and
for programs to load. The format almost everyone uses for this is JSON.

---

## The concept in plain language

**JSON is a text format for lists and dictionaries.** It stands for JavaScript Object
Notation, but nearly every language reads and writes it, Python included.

It maps straight onto what you learned last week:

| JSON | Python |
|---|---|
| object `{"key": value}` | dictionary |
| array `[1, 2, 3]` | list |
| `"text in double quotes"` | string |
| `42`, `7.5` | int, float |
| `true`, `false` | `True`, `False` |
| `null` | `None` |

JSON's rules are **stricter** than Python's:

- Strings and keys **must** use double quotes. Single quotes are an error.
- No comma after the last item.
- `true`, `false`, and `null` are lowercase.
- **There is no set type.** A set cannot be written to JSON.

Python's `json` module does two jobs:

| Function | Direction |
|---|---|
| `json.dump(data, file)` | Python collection → JSON text in a file |
| `json.load(file)` | JSON text in a file → Python collection |

(`json.dumps` and `json.loads`, with an s, do the same with a string instead of a file.
The s stands for string.)

---

## New habit: `with`

In Unit 1 you opened a file, used it, and called `.close()`. If your program crashed in
between, the close never happened. From today on, open files like this:

```python
with open("world.json", encoding="utf-8") as world_file:
    world = json.load(world_file)
```

`with` opens the file and names it `world_file`. When the indented block ends, Python
closes the file for you, **even if something inside the block raised an error**. You
cannot forget the close, because you never write it.

`encoding="utf-8"` says how the text is stored. Include it every time. Windows does not
default to UTF-8, and a room description with an accented letter or an emoji will fail
to load on a different computer without it.

---

## Worked example 1: the round trip

```python
# Monday Week 11 live-code: data moves out of the code and into a file.
import json

world = {
    "start_room": "lobby",
    "rooms": {
        "lobby": {"name": "Lobby", "exits": {"north": "hallway"}, "items": []},
        "hallway": {"name": "Hallway", "exits": {"south": "lobby"}, "items": ["flashlight"]},
    },
}

with open("world.json", "w", encoding="utf-8") as world_file:
    json.dump(world, world_file, indent=2)

with open("world.json", encoding="utf-8") as world_file:
    loaded = json.load(world_file)

print(type(loaded).__name__)
print(loaded["rooms"]["lobby"]["exits"]["north"])
print(loaded == world)
```

Output:

```
dict
hallway
True
```

And the first lines of `world.json`, which a person can read and edit:

```
{
  "start_room": "lobby",
  "rooms": {
    "lobby": {
      "name": "Lobby",
      "exits": {
        "north": "hallway"
      },
      "items": []
    },
    "hallway": {
      "name": "Hallway",
```

- `"w"` opens the file for **writing**, which empties it first.
- `indent=2` puts each item on its own line, indented. Without it the whole world is one
  long line. The program does not care. The friend editing it does.
- Loading gives back a dictionary equal to the one you saved. Nested lookups work exactly
  like last week.

---

## Worked example 2: what the types become

```python
import json
text = json.dumps({"name": "Theo", "done": False, "best": None, "scores": [9, 7.5]})
print(text)
print(type(json.loads(text)["scores"][1]).__name__)
print(json.loads("[1, 2, 3]"))
```

Output:

```
{"name": "Theo", "done": false, "best": null, "scores": [9, 7.5]}
float
[1, 2, 3]
```

`False` became `false`, `None` became `null`, and the single quotes Python prints became
the double quotes JSON requires. Loading turns them back. A number stays a number, so
you do **not** need `int()` after loading JSON the way you did after `input()`.

---

## Worked example 3: load the world and check it before the game starts

A typo in an exit does not break loading. The file is still valid JSON. It breaks the
moment a player walks that way, which might be during your demo. So check the world right
after loading it, and turn every problem into a clear message.

```python
import json


def load_world(filename):
    """Read the world file and check it. Raises ValueError naming the first problem."""
    with open(filename, encoding="utf-8") as world_file:
        world = json.load(world_file)
    for room_id, room in world["rooms"].items():
        for direction, destination in room["exits"].items():
            if destination not in world["rooms"]:
                raise ValueError(f"room '{room_id}' exit '{direction}' leads to '{destination}', which is not a room")
    return world


try:
    world = load_world("typo_world.json")
    print("World loaded.")
except FileNotFoundError:
    print("Cannot find the world file.")
except json.JSONDecodeError as error:
    print(f"The world file is not valid JSON. Line {error.lineno}, column {error.colno}: {error.msg}.")
except ValueError as error:
    print(f"The world file has a problem: {error}.")
```

Run three ways, output:

With a world file whose lobby exit says `"hallawy"`:

```
The world file has a problem: room 'lobby' exit 'north' leads to 'hallawy', which is not a room.
```

With a world file that has a trailing comma:

```
The world file is not valid JSON. Line 4, column 44: Illegal trailing comma before end of object.
```

With no world file at all:

```
Cannot find the world file.
```

**The order of the `except` clauses matters.** `json.JSONDecodeError` is a special kind of
`ValueError`. If `except ValueError` came first, it would catch the JSON error too, and
the player would get the wrong message. Most specific first. Version 3 of the text
adventure has a comment saying exactly this.

---

## The wrong version: editing JSON like Python

Someone who knows Python opens `world.json` and writes this:

```
{
  'start_room': 'lobby'
}
```

Loading it:

```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 3 (char 4)
```

Single quotes are fine in Python and illegal in JSON. Line 2, column 3 is exactly where
the first single quote sits.

And the other one everyone makes, a comma after the last item:

```
    "lobby": {"name": "Lobby", "exits": {"north": "hallway"},},
```

```
json.decoder.JSONDecodeError: Illegal trailing comma before end of object: line 4 column 61 (char 100)
```

**Confirm this wording on Python 3.14.** This exact message was produced by Python 3.13.7.
Older versions reported a trailing comma with a less specific message. Whatever your
version says, the line and column point at the problem.

### The error you will hit on Tuesday

```python
import json

state = {"room": "lobby", "visited": {"lobby", "hallway"}}
with open("save.json", "w", encoding="utf-8") as save_file:
    json.dump(state, save_file)
```

```
TypeError: Object of type set is not JSON serializable
```

JSON has no set. Convert a set to a sorted list before you write it, and back to a set
after you read it. Tomorrow's lesson opens with what this crash leaves behind in the file.

---

## Why the wrong versions are tempting

**JSON looks like Python.** Curly braces, square brackets, colons, commas. It is close
enough that your fingers type Python habits into it.

**Python forgives trailing commas.** Many people add one deliberately so the next line
needs no extra comma. JSON refuses.

**A set feels like it should save.** You can print it, loop over it, and put it inside a
dictionary. Nothing warns you it cannot be written until the moment you try.

---

## Where the line goes: data versus rules

Moving the world into a file does not mean moving everything. Version 3 keeps a deliberate
split:

| In `world.json` | In `adventure.py` |
|---|---|
| Room names and descriptions | Which room is dark |
| Exits | Which item makes light |
| Which items start in which room | The emergency frequency and the move limit |
| Text shown when you take an item | What happens when you win or lose |

**The file describes the place. The code decides what happens.** A friend can add a room
without being able to change how the game is won. Your version 3 should make the same kind
of choice and write down why.

---

## Vocabulary

| Term | What it means |
|---|---|
| **JSON** | A text format for lists, dictionaries, strings, numbers, true, false, and null. |
| **`json.dump(data, file)`** | Writes a Python collection to a file as JSON. |
| **`json.load(file)`** | Reads JSON from a file into Python collections. |
| **`json.dumps` / `json.loads`** | The same, to and from a string. |
| **`indent=2`** | Writes one item per line so people can read the file. |
| **`with`** | Opens a file and always closes it when the block ends. |
| **`encoding="utf-8"`** | How the file's text is stored. Always include it. |
| **`JSONDecodeError`** | The file is not valid JSON. Has `.lineno`, `.colno`, and `.msg`. |
| **Serializable** | Able to be written out as JSON. A set is not. |
| **Validation** | Checking loaded data makes sense before using it. |

---

## Self-check

**Question 1.** Write exactly what `print(text)` shows.

```python
import json
settings = {"volume": 7, "subtitles": True, "nickname": None, "keys": ["w", "a"]}
text = json.dumps(settings)
print(text)
```

**Question 2.** A classmate's game loads `world.json` fine, starts fine, and crashes with
`KeyError: 'hallawy'` twenty minutes into playtesting. Explain why loading did not catch
it, and what the program should do right after loading.

**Question 3.** Find every error in this JSON file. There are three.

```
{
  "title": "Night at the Aquarium",
  'start_room': "ticket_booth",
  "rooms": ["ticket_booth", "shark_tunnel",],
  "has_map": True
}
```

---

### Answers

**1.**

```
{"volume": 7, "subtitles": true, "nickname": null, "keys": ["w", "a"]}
```

`True` becomes `true` and `None` becomes `null`. All quotes are double quotes.

**2.** A typo in an exit is still valid JSON, so `json.load` has nothing to object to. The
program only fails when a player walks that direction and the code looks up a room that
does not exist. Right after loading, the program should check every exit against the list
of rooms and stop with a clear message naming the bad exit.

**3.** Line 3 uses single quotes around `start_room`. Line 4 has a trailing comma after
`"shark_tunnel"`. Line 5 uses `True`, which must be lowercase `true` in JSON.
