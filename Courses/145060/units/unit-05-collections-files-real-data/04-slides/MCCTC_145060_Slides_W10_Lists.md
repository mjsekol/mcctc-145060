# Many Things, One Name: Lists
---
## Slide 1: Adding one item meant editing five places
- Your v2 inventory is one True or False per item
- A third item needs a new variable
- Plus new branches in has_item, take_item, use_item
- Forget one and nothing crashes
Speaker notes: Open your version 2 text adventure and count how many places the word fuse appears. Every item you carry has its own variable, its own branch in three functions, and its own lines in the inventory sentence. Add a third item and you edit five places. Miss one and the game does not crash. It quietly gives a wrong answer. That was clumsy on purpose. Today you learn the tool that fixes it.
Image: A code file with five scattered highlights all marking the same item name, deep navy and accent blue.
---
## Slide 2: A list holds many values in order
- Square brackets, values separated by commas
- The order you put them in is kept
- The same value can appear twice
- One name for the whole collection
Speaker notes: A list is one name that holds many values in a row. The order you add things is the order they stay in, and a list does not mind if the same thing appears twice. That makes it the right shape for a playlist, a queue, an inventory, or the order people arrived. Watch how short the code gets.
Image: A row of labelled boxes with position numbers zero to three underneath.
---
## Slide 3: Build it, count it, reach into it
```python
inventory = ["flashlight", "fuse"]
print(inventory)        # ['flashlight', 'fuse']
print(len(inventory))   # 2
print(inventory[0])     # flashlight
print(inventory[-1])    # fuse
```
Speaker notes: Positions start at zero, the same as the strings you sliced in Unit 1. Negative one is the last item. len tells you how many there are. Notice that the last position is one less than the length. That fact is about to matter.
Image: None. This slide is code.
---
## Slide 4: Change it while the program runs
```python
inventory.append("key card")
print("fuse" in inventory)   # True
inventory.remove("fuse")
print(inventory)             # ['flashlight', 'key card']

for item in inventory:
    print("You are carrying:", item)
```
Speaker notes: append adds to the end. The word in asks whether something is there and gives you True or False. remove takes out the first match. And a for loop visits every item in order, which is the loop you already know, pointed at a list instead of a range. Compare this to your version 2 describe_inventory function. Five lines of branches became two.
Image: None. This slide is code.
---
## Slide 5: Two loud errors you will meet this week
```
print(inventory[2])
IndexError: list index out of range

inventory.remove("fuse")
ValueError: list.remove(x): x not in list
```
Speaker notes: Both of these crash, and both tell you exactly what went wrong. The first reached past the end. A list of two items has positions zero and one, and there is no position two. The second tried to remove something that is not there. Crashes like these are the friendly kind. The next slide is not friendly.
Image: None. This slide is code.
---
## Slide 6: Watch this: no more Static Lemonade
```python
queue = ["Static Lemonade - Porch Light", "Static Lemonade - Snow Day",
         "Mira Vance - Group Chat", "Juno Okafor - Low Battery"]

for song in queue:
    if song.startswith("Static Lemonade"):
        queue.remove(song)

print(queue)
```
Speaker notes: Your friend has heard enough Static Lemonade. I will loop over the queue and remove every song by that band. Before I run it, predict how many songs are left. Write the number down.
Image: None. This slide is code.
---
## Slide 7: One of them survived
```
['Static Lemonade - Snow Day', 'Mira Vance - Group Chat', 'Juno Okafor - Low Battery']
```
- No error, no warning
- Removing shifted every later song one place left
- The loop stepped forward and skipped Snow Day
- Fix: build a new list of songs to keep
Speaker notes: Three songs, and one of them is Static Lemonade. When remove took out the first song, everything slid one position to the left, and Snow Day moved into the spot the loop had already finished. The loop moved on and never looked at it. Nothing crashed. This is the bug that does not crash, again. The fix is to build a new list of the songs you keep, and never change a list while a for loop is walking through it.
Image: Four boxes shifting left with a loop arrow jumping past the second box.
---
## Slide 8: The fix builds a new list
```python
kept = []
for song in queue:
    if not song.startswith("Static Lemonade"):
        kept.append(song)
queue = kept

print(queue)   # ['Mira Vance - Group Chat', 'Juno Okafor - Low Battery']
```
Speaker notes: Start with an empty list. Walk the old list without touching it, and append every song you want to keep. When the loop is done, point the name at the new list. The old list was never changed while you were reading it, so nothing can be skipped. Remember this shape. You will write it again on Thursday.
Image: None. This slide is code.
---
## Slide 9: When a list is the right choice
- Order matters: a queue, a playlist, arrival order
- Duplicates are allowed or even meaningful
- You mostly walk through every item
- Not when you look things up by name
Speaker notes: A list is right when order matters, when the same thing can appear twice, and when you usually go through everything. It is the wrong tool when the question is find the one with this name, because a list has to check every item one at a time to answer that. Tomorrow you get the tool for that question.
Image: A simple two-column checklist, list is right on the left, list is wrong on the right.
---
## Slide 10: What you are about to build
- Lab U5-01 Part 1: the road trip playlist
- Read the file into a list, count it
- Remove duplicates without the skip bug
- Build 2: find every inventory flag in your v2
Speaker notes: Build one is part one of the Playlist Doctor lab. You read a shared road trip playlist into a list, count it, find duplicates, and remove songs without falling into the trap you watched a minute ago. Step six asks you to trigger the skip bug on purpose and write down what survived. Build two starts text adventure version 3. You are not changing code yet. You are listing every place your version 2 tracks an item, so you know exactly what a list replaces.
Image: A terminal showing a playlist count and a short list of songs, navy and accent blue.
