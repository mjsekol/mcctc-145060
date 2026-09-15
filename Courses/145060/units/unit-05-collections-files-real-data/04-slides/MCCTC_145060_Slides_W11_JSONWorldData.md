# Data Out of Code: JSON and the World File
---
## Slide 1: Your friend wants to add a room
- They can write a great haunted greenhouse
- They cannot read Python
- Right now the rooms live inside adventure.py
- One wrong comma and your game will not start
Speaker notes: Your friend writes better room descriptions than you do. They want to add a haunted greenhouse to your game. Right now that means editing your Python file, and one misplaced quote breaks everything. Today you move the world out of the code and into a data file. The code will know how the game works. The file will know what the place looks like.
Image: A notebook page of room descriptions next to a code editor, with a line separating them.
---
## Slide 2: JSON is a text format for your collections
- Objects in curly braces become dictionaries
- Arrays in square brackets become lists
- Strings always use double quotes
- true, false, and null become True, False, None
Speaker notes: JSON is plain text that almost every language can read. It maps straight onto what you learned last week. A JSON object is a dictionary, a JSON array is a list. The rules are stricter than Python, though. Double quotes only, lowercase true and false, and null where Python says None. Those differences are where the errors come from.
Image: A two-column table pairing JSON syntax on the left with Python types on the right.
---
## Slide 3: with opens a file and always closes it
```python
with open("world.json", "w", encoding="utf-8") as world_file:
    json.dump(world, world_file, indent=2)

with open("world.json", encoding="utf-8") as world_file:
    loaded = json.load(world_file)
```
Speaker notes: In Unit 1 you opened a file and had to remember to close it. with does the closing for you, when the indented block ends, even if something inside it crashes. From today on, every file you open uses with. dump writes a Python collection out as JSON text. load reads JSON text back into a Python collection. indent equals two makes the file readable by a person, which matters, because a person is going to edit it.
Image: None. This slide is code.
---
## Slide 4: The round trip
```python
world = {
    "start_room": "lobby",
    "rooms": {
        "lobby": {"name": "Lobby", "exits": {"north": "hallway"}, "items": []},
        "hallway": {"name": "Hallway", "exits": {"south": "lobby"}, "items": ["flashlight"]},
    },
}
# dump it to world.json, then load it back into loaded
print(type(loaded).__name__)                      # dict
print(loaded["rooms"]["lobby"]["exits"]["north"]) # hallway
print(loaded == world)                            # True
```
Speaker notes: Dump the world, load it back, and you get an equal dictionary. Nested keys read exactly like last week: rooms, then the lobby, then its exits, then north. Your version 3 world is this structure with more rooms. The file on disk is text. The moment it is loaded, it is dictionaries and lists again.
Image: None. This slide is code.
---
## Slide 5: Your friend edits the file by hand
```
{
  'start_room': 'lobby'
}
```
```
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 3 (char 4)
```
Speaker notes: This is what happens the first time someone who knows Python edits JSON. Single quotes are fine in Python and illegal in JSON. The error is loud and specific. It even tells you line two, column three. Read the line and column before you read anything else.
Image: None. The error is the content.
---
## Slide 6: The other one everyone makes
```
    "lobby": {"name": "Lobby", "exits": {"north": "hallway"},},
```
```
json.decoder.JSONDecodeError: Illegal trailing comma before end of object: line 4 column 61 (char 100)
```
Speaker notes: A comma after the last item. Python allows it. JSON does not. On Python 3.13 the message names the problem exactly. Older versions said something less helpful, so if your machine words it differently, the line and column are still right. This is exactly the error your game must catch and explain, instead of showing your friend a traceback.
Image: None. The error is the content.
---
## Slide 7: JSON cannot hold a set
- json.dump on a set raises TypeError
- Convert it to a sorted list on the way out
- Convert the list back to a set on the way in
- Sorted, so the same game saves the same file
Speaker notes: One more rule before you build. JSON has no set type. Hand json.dump a set and it raises TypeError: Object of type set is not JSON serializable. Your visited rooms are a set. So you convert to a sorted list when you write, and back to a set when you read. Tomorrow you will see what that crash does to a save file halfway through writing it.
Image: A set of tokens being lined up into a sorted row on the way into a file.
---
## Slide 8: Check the world before the game starts
- A typo in an exit does not crash on load
- It crashes when someone walks that way
- Validate every exit and item at startup
- Turn a crash next week into a message now
Speaker notes: Here is the failure to name before you hit it. If world.json says north leads to hallawy, loading works fine. The crash comes later, when a player walks north, maybe during your demo. So after loading, walk through every room and check that every exit leads to a room that exists. Version 3 does this in a function called validate world. A clear message at launch beats a crash in front of a judge.
Image: A checklist running down a list of rooms, one exit flagged with a warning mark.
---
## Slide 9: What you are about to build
- Lab U5-03 Part 1: the Streak Tracker
- Load streaks from JSON, add a day, save
- Break the file by hand and read the error
- Build 2: move your v3 world into world.json
Speaker notes: Build one is part one of the Streak Tracker. Habits and their streaks live in a JSON file. Your program loads them, adds a day, and saves. Then you open the file, break it with a single quote and a trailing comma, and record both errors. Build two is the big one for your text adventure. Move every room, exit, and item out of your code into world dot json, and load it at startup.
Image: A JSON file on the left and a running tracker in a terminal on the right.
