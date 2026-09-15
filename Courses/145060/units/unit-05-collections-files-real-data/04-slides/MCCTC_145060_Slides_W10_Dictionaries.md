# Look It Up by Name: Dictionaries
---
## Slide 1: Your find_exit function is thirty lines of if
- Every room is an if
- Every direction inside it is another if
- A new room means new branches everywhere
- The map is buried inside the code
Speaker notes: Open find_exit in your version 2. Room by room, direction by direction, it is a wall of if and elif. What that function really holds is a map: this room, this direction, that room. A map is data. Today you learn the structure that stores a map directly, so the question which room is north of the lobby becomes one lookup instead of thirty lines.
Image: A long staircase of nested if statements beside a small two-column table of direction and room.
---
## Slide 2: A dictionary pairs a key with a value
- Curly braces, key colon value
- You find a value by its key, not its position
- Keys are unique, values can repeat
- Keys are usually strings you choose
Speaker notes: A dictionary stores pairs. The key is the name you look up, and the value is what you get back. There are no positions. You never ask for item number two. You ask for north. A key can only appear once, which makes sense, because north from the hallway cannot lead to two places.
Image: A small table with a key column and a value column, arrows from key to value.
---
## Slide 3: Build it, read it, change it
```python
exits = {"north": "hallway", "east": "archive"}
print(exits["north"])      # hallway
print("west" in exits)     # False

exits["west"] = "studio"
print(exits)   # {'north': 'hallway', 'east': 'archive', 'west': 'studio'}
print(len(exits))          # 3
```
Speaker notes: Square brackets with a key reads a value. The word in checks whether a key exists. Assigning to a key that is not there yet adds it, and assigning to one that is there replaces its value. Dictionaries keep the order you added keys, so printing it shows them in that order.
Image: None. This slide is code.
---
## Slide 4: Walk every pair, and count things
```python
for direction, room in exits.items():
    print(direction, "->", room)

votes = ["tacos", "pizza", "tacos", "wings", "tacos", "pizza"]
counts = {}
for vote in votes:
    if vote in counts:
        counts[vote] += 1
    else:
        counts[vote] = 1
print(counts)   # {'tacos': 3, 'pizza': 2, 'wings': 1}
```
Speaker notes: items gives you each key and its value together, so a for loop can name both. The second half is the counting pattern, and you will write it all year. If the key is already there, add one. If it is not, start it at one. The class lunch vote, the most-played artist, how many hoodies in each size. Same six lines.
Image: None. This slide is code.
---
## Slide 5: The loud mistake
```
print("You walk to the", exits["nroth"])

KeyError: 'nroth'
```
- One typo in the key
- Python stops and names the key it could not find
- That is the helpful outcome
Speaker notes: I typed n r o t h. Square brackets refuse to guess. They stop the program and print the exact key that does not exist. You read it, you see the typo, you fix it in five seconds. Hold on to that feeling, because the next slide is the same typo with a different tool.
Image: None. The error is the content.
---
## Slide 6: The quiet mistake
```python
print("You walk to the", exits.get("nroth"))
```
```
You walk to the None
```
Speaker notes: get looks a key up and hands back None if it is missing, instead of crashing. That sounds safer. It is not safer here. The same typo now produces a sentence that looks almost right and walks the player into a room called None. No error, no line number, nothing to find. You have met this shape before, all the way back to 121212 in Unit 1. It is the bug that does not crash. Get is for keys that are allowed to be missing. It is not a way to make errors go away.
Image: None. This slide is code.
---
## Slide 7: When get is the right tool
```python
print(exits.get("down", "no exit that way"))   # no exit that way

if "down" in exits:
    print("You go down to the", exits["down"])
else:
    print("You cannot go down from here.")
```
Speaker notes: get with a default is good when a missing key is a normal answer, like a room with no exit down. Checking with in first and then using square brackets is often clearer, because the reader can see both paths. What you should never do is reach for get to silence a KeyError you do not understand.
Image: None. This slide is code.
---
## Slide 8: When a dictionary is the right choice
- You look things up by a name or ID
- Each key means one thing
- Counting how many of each
- Translating one spelling into another
Speaker notes: Reach for a dictionary when the question is find the one with this name. Exits by direction. A player by jersey number. A price by item. A count by vote. It is also how you translate messy spellings into clean ones, which you will do next week with a sign-up sheet where people typed med, medium, and M.
Image: Four small key and value tables side by side, each labelled with a teenage example.
---
## Slide 9: What you are about to build
- Lab U5-01 Part 2: songs per artist
- The counting pattern on the real playlist
- Record the KeyError and the silent get
- Build 2: your v2 map as a dictionary
Speaker notes: Build one is part two of the Playlist Doctor. You count songs per artist with the pattern from slide four, find the artist with the most, and then misspell an artist on purpose both ways and write down what each one did. Build two is your text adventure. Draw your map as a dictionary of rooms, each with a dictionary of exits, first on paper and then in code, and delete find_exit.
Image: A hand-drawn room map beside the same map written as nested key and value pairs.
