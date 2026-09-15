# Lecture Notes: Save, Load, and the File You Cannot Trust
## 145060 Programming · Unit 5 · Week 11 · Tuesday, November 17

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W11_SaveAndLoad.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W11_SaveAndLoad.pptx)

If you missed class, you can learn this concept from this file alone. Do not skip the
first example. It creates a damaged save file in about eight seconds, and every other
example in this file exists because of it.

**Every program below was run on Python 3.13.7.** The output shown is the real output.

---

## Why this exists

You are on the roof with the fuse, three moves from winning, and the bell rings. Close
the program and you start from the lobby tomorrow.

Your playtesters want a save command. Writing the state to a JSON file takes about six
lines, and you learned how yesterday. **That is not the hard part.** The hard part is that
a save file lives on a disk, between runs, where anything can happen to it:

- It may not exist yet, because nobody has saved.
- It may be damaged, because a save crashed halfway or someone edited it badly.
- It may be perfectly valid JSON that describes a game that cannot exist.

A good load handles all three, tells the player which one happened, and **never leaves
the game half loaded**. That is today's concept.

---

## The concept in plain language

**A load either fully succeeds or changes nothing.**

That rule gives you a three-step shape:

1. **Read.** Open and parse the file. Catch a missing file and a damaged file separately.
2. **Check.** Look at every value before using any of them. Is the room real? Is the move
   count a whole number?
3. **Build.** Only when everything passed, build the new game state and hand it back. If
   anything fails, raise an error with a message for the player, and the caller keeps the
   game it already had.

---

## Worked example 1: the crash that makes a damaged file

Here is a save that forgets JSON cannot hold a set.

```python
import json

state = {"room": "archive", "inventory": ["flashlight"], "visited": {"lobby", "hallway", "archive"}, "moves": 2}

with open("savegame.json", "w", encoding="utf-8") as save_file:
    json.dump(state, save_file, indent=2)
print("Game saved.")
```

Output, last line:

```
TypeError: Object of type set is not JSON serializable
```

You expected that. Now open `savegame.json`. This is exactly what is in it:

```
{
  "room": "archive",
  "inventory": [
    "flashlight"
  ],
  "visited": 
```

**Half a file.** `json.dump` writes as it goes. It had already written the room and the
inventory when it reached the set and raised. And because opening with `"w"` empties the
file first, whatever good save was there before is gone too.

That is why a damaged save file is not a rare case you can ignore. You watched one
get made by a normal mistake.

---

## Worked example 2: a save that works

```python
import json

ROOMS = ["lobby", "hallway", "archive", "basement", "studio", "roof"]
SAVE_FILE = "savegame.json"


def save_game(state):
    data = {
        "room": state["room"],
        "inventory": state["inventory"],
        # JSON has no set. Convert on the way out. Sorted, so the file is stable.
        "visited": sorted(state["visited"]),
        "moves": state["moves"],
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
        json.dump(data, save_file, indent=2)
```

Build a plain dictionary of exactly what must come back, convert anything JSON cannot
hold, and dump it. **Save only what you need.** Everything you save, you will have to
check when you load.

---

## Worked example 3: a load that fully succeeds or changes nothing

```python
def load_game():
    """Return the saved state. Raises ValueError with a message for the player."""
    try:
        with open(SAVE_FILE, encoding="utf-8") as save_file:
            data = json.load(save_file)
    except FileNotFoundError:
        raise ValueError("There is no save file yet.") from None
    except json.JSONDecodeError:
        raise ValueError("The save file is damaged.") from None

    if not isinstance(data, dict) or data.get("room") not in ROOMS:
        raise ValueError("The save file puts you somewhere that does not exist.")
    # Only now, with the data checked, build the state. Convert the list back to a set.
    return {"room": data["room"], "inventory": data["inventory"],
            "visited": set(data["visited"]), "moves": data["moves"]}
```

And the code that calls it:

```python
state = {"room": "lobby", "inventory": [], "visited": {"lobby"}, "moves": 0}
steps = ["load before any save", "load a damaged file", "save, then load"]
for step in steps:
    if step == "load a damaged file":
        with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
            save_file.write('{\n  "room": "archive",\n  "visited": ')
    if step == "save, then load":
        save_game({"room": "archive", "inventory": ["flashlight"],
                   "visited": {"lobby", "hallway", "archive"}, "moves": 2})
    try:
        state = load_game()
        print(f"{step}: loaded, you are in the {state['room']}")
    except ValueError as error:
        print(f"{step}: {error} You are still in the {state['room']}.")
```

Output:

```
load before any save: There is no save file yet. You are still in the lobby.
load a damaged file: The save file is damaged. You are still in the lobby.
save, then load: loaded, you are in the archive
```

Read what makes this work:

- **Two different `except` clauses, two different messages.** A missing file and a
  damaged file are different problems with different fixes for the player.
- **`raise ValueError(...) from None`** turns a technical error into one message the
  player can read. `from None` hides the original traceback, which the player does not
  need. You met this in version 2's `parse_frequency`.
- **`state = load_game()` only runs if `load_game` returns.** If it raises, the
  assignment never happens and `state` still holds the old game. That is the "changes
  nothing" half of the rule, and it costs you nothing extra to get.
- **`data.get("room")` is the right use of `.get()`.** A save file missing its room key
  is a normal thing to check for, not a typo in your own code.
- **`set(data["visited"])`** converts the saved list back into a set.

---

## Valid JSON is not a valid save

Someone will edit a save by hand. Maybe you, testing. The JSON can be perfect and the data
nonsense:

- `"room": "control_tower"` is valid JSON. The room does not exist.
- `"moves": -4` is valid JSON. No game has negative moves.
- `"moves": true` is valid JSON, and here is the trap:

```python
print(isinstance(True, int), True + 1)
```

```
True 2
```

In Python, `True` counts as the integer 1. A check that only asks "is it an int" lets
`true` through as move 1. That is a bug that does not crash. Version 3 of the text
adventure checks for it explicitly:

```python
def is_whole_number(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0

for v in [3, 0, True, -1, 2.5, "4"]:
    print(repr(v), is_whole_number(v))
```

```
3 True
0 True
True False
-1 False
2.5 False
'4' False
```

`isinstance(value, int)` asks whether a value is a certain type. It is the tool for
checking what a JSON file actually gave you.

---

## The wrong version: catch the errors in the wrong order

```python
import json

try:
    with open("broken_save.json", encoding="utf-8") as save_file:
        data = json.load(save_file)
    print("Loaded.")
except ValueError:
    print("The save file has a bad value.")
except json.JSONDecodeError:
    print("The save file is damaged.")
```

With `broken_save.json` holding the damaged text `{"room": "lobby",`, output:

```
The save file has a bad value.
```

**No crash, and the wrong message, every time, forever.** `json.JSONDecodeError` is a
special kind of `ValueError`. Python checks `except` clauses from the top, and the first
one that matches wins. `except ValueError` matches the JSON error, so the second clause
can never run.

Swap the two and the output becomes:

```
The save file is damaged.
```

**Most specific exception first.**

### The worse wrong version: starting over and saving

This one gets written by people trying to be helpful. It is a fragment of a streak
tracker, shown to explain the idea, not a complete program:

```python
try:
    data = load_streaks("streaks.json")
except json.JSONDecodeError:
    data = {"habits": {}}      # the file is broken, start fresh
...
save_streaks(data, "streaks.json")
```

The file was damaged, but it was **somebody's data**. Maybe one missing bracket away from
four months of streaks. Starting fresh and then saving writes an empty file over it. The
program runs happily and the data is gone. Lab U5-03 makes you avoid this: **when a file
is damaged, stop and change nothing.** A person can repair a damaged file. Nobody can
repair one that was overwritten.

---

## Why the wrong versions are tempting

**Catching `ValueError` feels thorough.** It is the broader net, so it seems safer. It is
broader in exactly the way that hides the specific case.

**"Start fresh" feels kind.** The player does not see an error, and the program keeps
going. It is kind for eight seconds.

**Testing only the happy path passes.** Save, load, it works. The failures only appear when
you deliberately break the file, which is why every lab and project this week makes you
break it on purpose.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Save file** | A file holding the state a program needs to continue later. |
| **State** | Every value that changes while the program runs. |
| **Serialize** | Convert state to a format that can be written, such as JSON. |
| **Damaged** or **corrupt** | Not valid JSON. `json.load` raises `JSONDecodeError`. |
| **Validate** | Check that loaded values make sense before using them. |
| **`isinstance(value, type)`** | True if the value is of that type. |
| **`raise ... from None`** | Raise a new, readable error and hide the technical one. |
| **All or nothing** | A load either returns a complete checked state or raises and changes nothing. |
| **Except order** | Python uses the first matching `except`. Put the most specific first. |

---

## Self-check

**Question 1.** A game's save code crashes with `TypeError: Object of type set is not
JSON serializable` in the middle of saving. The player had a good save from yesterday.
What is in the save file now, and what should the load code do about it?

**Question 2.** Write exactly what this prints when `savegame.json` does not exist.

```python
import json

def load():
    try:
        with open("savegame.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError("No save yet.") from None

room = "lobby"
try:
    room = load()["room"]
except ValueError as error:
    print(error)
print("You are in the", room)
```

**Question 3.** Name three different values of `"moves"` that are valid JSON but should be
rejected by a text adventure's load, and say why `true` is the sneakiest of them.

---

### Answers

**1.** A partial file: the keys written before the set, then nothing. Yesterday's good
save is gone, because opening for writing emptied the file first. The load code must catch
`json.JSONDecodeError`, tell the player the save is damaged, and leave the current game
unchanged. (Fixing the save code, by converting the set to a list, prevents it next time.)

**2.**

```
No save yet.
You are in the lobby
```

`load()` raised, so `room = load()["room"]` never assigned, and `room` kept `"lobby"`.

**3.** Any three of: `-1` (no negative moves), `2.5` (not a whole number), `"4"` (a string,
not a number), a number at or above the move limit (the game would already be over),
`true`. `true` is the sneakiest because Python treats `True` as the integer 1, so a check
that only asks `isinstance(value, int)` accepts it without any error.
