# Is It In There: Sets, and Choosing the Right Structure
---
## Slide 1: One hundred thousand IDs, one question
- The district sign-in list has 100,000 IDs
- A thousand kids scan in before first bell
- For each scan: is this ID on the list
- Pick the wrong structure and the line stops moving
Speaker notes: Picture a sign-in system for a whole district. One hundred thousand valid IDs. A thousand scans before the bell, and every scan asks one question: is this ID on the list. Today you learn a structure built for exactly that question, and you will see what the wrong structure costs, measured on a real computer, not described.
Image: A long line of students at a scanner with a clock above it.
---
## Slide 2: A set holds unique values, no order
- Curly braces with values, no colons
- Adding a duplicate does nothing
- There is no first item, so no positions
- Built to answer: is it in there
Speaker notes: A set is a bag of unique values. Add something twice and it is still there once. There is no order, so there is no position zero. What you give up in order you get back in speed on one question, membership. That is the whole deal.
Image: A loose circle of labelled tokens with no numbering, one duplicate token bouncing off.
---
## Slide 3: Build it and ask it
```python
visited = {"lobby"}
visited.add("hallway")
visited.add("lobby")
print(len(visited))          # 2
print("roof" in visited)     # False

sign_ups = ["Maya", "Theo", "Maya", "Jordan", "Theo"]
print(len(set(sign_ups)))    # 3
```
Speaker notes: add puts a value in, and adding lobby a second time changes nothing, so the length is two. set of a list throws away the duplicates, which is the fastest way to count how many different people signed up. One warning. If you print a set, the order you see can change from one run to the next. Never write code that depends on it.
Image: None. This slide is code.
---
## Slide 4: Compare two groups in one line
```python
mine = {"lobby", "hallway", "archive"}
yours = {"hallway", "studio", "roof"}

print(mine & yours)        # {'hallway'}
print(mine - yours)        # lobby and archive, in some order
print(len(mine | yours))   # 5
```
Speaker notes: The ampersand keeps what is in both. Minus keeps what is in the first and not the second. The bar combines both with no repeats. Rooms you both explored, songs on both playlists, classes you share with a friend. Each of those is one line.
Image: None. This slide is code.
---
## Slide 5: The empty braces trap
```python
visited = {}
visited.add("lobby")
```
```
AttributeError: 'dict' object has no attribute 'add'
```
Speaker notes: Empty curly braces make an empty dictionary, not an empty set. Python decided that long ago because dictionaries came first. So add fails, and the message tells you the truth. You have a dict. An empty set is written set with empty parentheses. Everyone hits this once.
Image: None. The error is the content.
---
## Slide 6: The same question, measured
```python
start = time.perf_counter()
for code in lookups:
    found = code in id_list
list_seconds = time.perf_counter() - start

start = time.perf_counter()
for code in lookups:
    found = code in id_set
set_seconds = time.perf_counter() - start
```
Speaker notes: Same one hundred thousand IDs, stored once as a list and once as a set. Same one thousand lookups, half of them for IDs that are not there. perf counter is a stopwatch built into Python. I am going to run this now. Predict how many times faster the set will be.
Image: None. This slide is code.
---
## Slide 7: What it cost on our test machine
- List: about 0.46 seconds for 1,000 lookups
- Set: about 0.00016 seconds for the same lookups
- Roughly 2,700 to 2,900 times faster across five runs
- Your machine will show different numbers
Speaker notes: These are real numbers from five runs on the machine these notes were written on. The list took about forty six hundredths of a second. The set took about sixteen hundred thousandths. Your numbers will differ, and they should. What will not differ is the gap. A list checks items one by one, so a missing ID means checking all one hundred thousand. A set jumps almost straight to the answer.
Image: Two horizontal bars, one very long and one a sliver, labelled list and set.
---
## Slide 8: Choose by the question you ask most
- Order or duplicates matter: list
- Look up by a name or ID: dictionary
- Is it in there, or keep only unique: set
- Wrong choice cost: slow, lost order, or impossible lookups
Speaker notes: This is the slide to copy. Ask what question your program asks most often. If order or repeats matter, a list. If you find things by a name, a dictionary. If you only ask whether something is there, or you need each thing once, a set. And name the cost of the wrong choice out loud: a list for membership gets slow as it grows, a set loses the order, and a list of pairs makes you search for every lookup.
Image: A three-row decision table, question on the left, structure on the right.
---
## Slide 9: Sometimes the list is still right
- The v3 command list has 14 commands
- help prints them in order
- A set would be faster by an amount you cannot measure
- And help would print them scrambled
Speaker notes: Choosing is not always picking the fast one. The version 3 text adventure keeps its commands in a list, even though the game asks whether a command is valid on every turn. With fourteen commands the difference is too small to measure, and a list keeps the order help prints them in. A good choice names what it gives up. Fourteen items is not one hundred thousand.
Image: A short numbered command list beside a small scrambled cloud of the same words.
---
## Slide 10: What you are about to build
- Lab U5-01 Part 3: sets and the stopwatch
- Songs on both playlists, artists counted once
- Time a list against a set yourself
- Build 2: inventory list and visited set in v3
Speaker notes: Build one finishes the Playlist Doctor. You find songs on both your playlist and a friend's with one set operation, then run the timing yourself and write your machine's numbers in your README next to ours. Build two goes back to the text adventure. Your boolean inventory flags become one list, and you add a set of rooms visited, with a comment above each saying why you chose it.
Image: A README table comparing two timing results from two different machines.
