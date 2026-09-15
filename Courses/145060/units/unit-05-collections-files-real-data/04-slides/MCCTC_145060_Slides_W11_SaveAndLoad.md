# Save, Load, and the File You Cannot Trust
---
## Slide 1: The bell rings on the roof
- You got to the roof with the fuse
- Fourth period is over
- Tomorrow you start from the lobby again
- And a bad save could be worse than no save
Speaker notes: You are on the roof, fuse in your pocket, three moves from winning, and the bell rings. Close the program and it is all gone. Your playtesters have asked for a save button. Today you build one, and you build the part most people skip: what happens when the save file is missing, damaged, or lying.
Image: A game screen with a school bell icon and a fading progress bar.
---
## Slide 2: Saving is converting your state to JSON
```python
def save_game(state):
    data = {
        "room": state["room"],
        "inventory": state["inventory"],
        "visited": sorted(state["visited"]),
        "moves": state["moves"],
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
        json.dump(data, save_file, indent=2)
```
Speaker notes: Save builds a plain dictionary of exactly the things that need to come back, and dumps it. Notice visited is sorted into a list, because yesterday you learned JSON has no set. Save only what you need. Anything you save, you will have to check when you load it.
Image: None. This slide is code.
---
## Slide 3: Watch this: forget to convert the set
```python
state = {"room": "archive", "inventory": ["flashlight"],
         "visited": {"lobby", "hallway", "archive"}, "moves": 2}

with open("savegame.json", "w", encoding="utf-8") as save_file:
    json.dump(state, save_file, indent=2)
```
```
TypeError: Object of type set is not JSON serializable
```
Speaker notes: Here is the version that forgets. It crashes, which you expected. Now the part nobody expects. Open savegame dot json.
Image: None. This slide is code.
---
## Slide 4: The crash left half a file behind
```
{
  "room": "archive",
  "inventory": [
    "flashlight"
  ],
  "visited": 
```
- json.dump wrote until it hit the set
- The file is now damaged JSON
- Your old good save is gone
Speaker notes: That is the real contents of the file after the crash. json dump had already written the room and the inventory when it reached the set and stopped. Opening a file for writing empties it first, so the good save that was there before is gone too. This is why every load must expect a damaged file. It is not a rare case. You made one in eight seconds.
Image: None. This slide shows the file.
---
## Slide 5: A load either fully succeeds or changes nothing
```python
def load_game():
    try:
        with open(SAVE_FILE, encoding="utf-8") as save_file:
            data = json.load(save_file)
    except FileNotFoundError:
        raise ValueError("There is no save file yet.") from None
    except json.JSONDecodeError:
        raise ValueError("The save file is damaged.") from None

    if not isinstance(data, dict) or data.get("room") not in ROOMS:
        raise ValueError("The save file puts you somewhere that does not exist.")
    return {"room": data["room"], "inventory": data["inventory"],
            "visited": set(data["visited"]), "moves": data["moves"]}
```
Speaker notes: Three different failures, three different messages. Missing file, damaged file, and a file that is valid JSON but describes something impossible. The last check matters most. Only after every value is checked does the function build a new state. The caller keeps the old game if anything raises, so a bad load never leaves you half loaded.
Image: None. This slide is code.
---
## Slide 6: What the player sees
```
load before any save: There is no save file yet. You are still in the lobby.
load a damaged file: The save file is damaged. You are still in the lobby.
save, then load: loaded, you are in the archive
```
Speaker notes: These are real runs. No traceback in any of them, and every message tells the player what happened and that their current game is safe. Compare that with a traceback full of json decoder internals. Same information for you. Useless for the person playing.
Image: None. This slide is code.
---
## Slide 7: Valid JSON is not a valid save
- "moves": true loads as a bool, not a number
- True counts as 1 in Python, so it sneaks through
- A room called control_tower is valid JSON
- Check every value against your world
Speaker notes: Someone will edit a save file by hand. Maybe you, while testing. The JSON can be perfect and the data nonsense. moves equals true is valid JSON, and because Python treats True as the number one, a lazy check lets it through. A room name that is not in your world is valid JSON too. Checking the format is not checking the data.
Image: A JSON file with two values circled, each with a question mark.
---
## Slide 8: Order your except clauses
- JSONDecodeError is a kind of ValueError
- Catch ValueError first and JSONDecodeError never runs
- The player gets the wrong message, silently
- Most specific exception first
Speaker notes: One trap in the code on slide five. JSONDecodeError is a special kind of ValueError. If you write except ValueError above except JSONDecodeError, the first one catches everything and the second never runs. Nothing crashes. The damaged file gets the wrong message forever. Put the most specific exception first.
Image: Two stacked filters, the wide one on top catching everything before the narrow one.
---
## Slide 9: What you are about to build
- Lab U5-03 Part 2: a tracker that never eats data
- Missing, damaged, and wrong files each get a message
- A damaged file is never overwritten
- Build 2: save and load commands in v3
Speaker notes: Build one finishes the Streak Tracker. Your program must handle a missing file, a damaged file, and a file with a bad value, each with its own message, and it must never save over a damaged file, because that file might be months of somebody's streaks. Build two adds save and load commands to your text adventure, with three distinct bad save messages you can trigger on demand in your demo.
Image: Three small terminal panels each showing a different calm error message.
