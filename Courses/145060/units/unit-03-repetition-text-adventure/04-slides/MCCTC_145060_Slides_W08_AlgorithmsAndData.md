# How an App Finds Your Top Song
---
## Slide 1: Your music app knows your top song
- It counts your plays
- It finds your most played song
- It searches for an artist
- None of that is magic
- It is a few algorithms over organized data
Speaker notes: Every app you use is mostly information processing. Counting, adding up, finding the biggest, searching. None of it is one giant clever line. It is a small number of algorithms, run over data that somebody decided how to organize. Today you learn to name both halves, and you learn why the way data is organized changes how much work the program does. That is outcome 5.1.2.
Image: A phone screen showing a single top song card beside a long list of songs, flat navy and accent blue.
---
## Slide 2: Two words
- Algorithm: precise, finite steps that solve a problem
- Your pseudocode is an algorithm in English
- Data structure: how data is organized for a program
- One song per line, fields in fixed positions
- The structure decides which algorithms are possible
Speaker notes: An algorithm is a precise, finite sequence of steps. You have been writing them in pseudocode for two weeks. A data structure is the way data is organized so a program can use it. Our playlist file, one song per line, title in positions zero to twenty three, is a data structure. And here is the idea that makes this more than vocabulary. Change the structure, and the algorithm changes with it.
Image: Two labeled boxes, steps on one side and a table of records on the other, joined by an arrow.
---
## Slide 3: The loop every algorithm uses
```python
playlist = open("playlist.txt")
song_count = 0
total_plays = 0

while True:
    line = playlist.readline()
    if line == "":
        break
    plays = int(line[44:47])
    song_count = song_count + 1
    total_plays = total_plays + plays

playlist.close()
print(f"{song_count} songs, {total_plays} plays")
```
```
8 songs, 325 plays
```
Speaker notes: In Week 4, readline returning an empty string at the end of the file was a trap. Today it is the sentinel. A blank line comes back as a newline character, never as empty, so empty means the file is over. This slide writes the loop with Wednesday's break. The lecture notes write the same loop with the check in the while line. Both stop at the same moment. Every algorithm today uses this loop, and only the middle changes. Here it is count and total, two accumulators set to zero above the loop.
Image: None. This slide is code.
---
## Slide 4: Biggest value, and whose it is
```python
# Before the loop
most_plays = 0
top_song = ""

# Inside the loop, once per record
    title = line[0:24].strip()
    plays = int(line[44:47])
    if plays > most_plays:
        most_plays = plays
        top_song = title
```
```
Most played: Group Chat Silence (87 plays)
```
Speaker notes: The algorithm in one sentence. Keep the best one seen so far, and replace it whenever a better one shows up. And keep two pieces of state together, the value and the label. Eighty seven answers nothing. The song that got eighty seven is the answer. When one changes, both change.
Image: None. This slide is code.
---
## Slide 5: Search, and stop when you find it
- Compare each record to what you want
- break the moment it matches
- static hallway: found after reading 3 lines
- An artist who is not there: all 8 lines
- Not here always means reading everything
Speaker notes: Wednesday's break turns a loop into a search. The moment the artist matches, stop. Three lines read. But run it for an artist who is not on the playlist and it reads every line, because in an unordered file there is no way to be sure something is missing without checking everything. Also compare the whole artist field with double equals. The word hall is in static hallway, and a search that matches part of a field finds things you never asked for.
Image: A column of eight records with a pointer stopping at the third, and a second column scanned to the bottom.
---
## Slide 6: Same question, two structures
- Which song has the most plays?
- Songs in the order added: read all 8 lines
- Songs sorted by plays: read 1 line
- With 800,000 songs: 800,000 reads against 1
- Sorting costs work every time a count changes
Speaker notes: Same eight songs. Same question. In the order they were added, a bigger number could be on any line, so the algorithm reads everything. Sorted from most plays to fewest, the answer is on line one. Now scale it up. That is the difference between reading one line and reading all of them. So why not always sort? Because every play changes a count, and a sorted file may need that song moved. Neither structure is better. Each makes some questions cheap and others expensive.
Image: Two stacks of cards, one shuffled with a magnifier scanning every card, one sorted with the top card highlighted.
---
## Slide 7: Watch this: the least played song
```python
# Before the loop
fewest_plays = 0
quiet_song = ""

# Inside the loop, once per record
    title = line[0:24].strip()
    plays = int(line[44:47])
    if plays < fewest_plays:
        fewest_plays = plays
        quiet_song = title

# After the loop
print(f"Least played: {quiet_song} ({fewest_plays} plays)")
```
Speaker notes: The biggest value worked by starting at zero. So to find the smallest, I flip the less than and start at zero again. Same pattern, same file. Predict the song and the number before I run it.
Image: None. This slide is code.
---
## Slide 8: The wrong way: a blank title and zero plays
```
Least played:  (0 plays)
```
Speaker notes: No error. A blank title and zero plays. Every song has more than zero plays, so plays less than fewest plays is False on every single record, and nothing is ever replaced. The loop ran eight times and changed nothing. The starting value was a guess, and the guess was already better than every real record. The fix is to start from the first real record, not from a guess. Read one line, use it as the lowest so far, then loop over the rest. That prints Low Battery with nine plays.
Image: None. This slide is code.
---
## Slide 9: Five algorithms to recognize
- Count: how many
- Total: how much altogether
- Maximum or minimum: start from the first real record
- Search: stop early with break once found
- Filter: which records match a rule
Speaker notes: Almost every information processing task you meet this year is one of these five, or a few of them sharing one loop. When you get a data problem, name the algorithm first. Then ask whether it can stop early, and what its starting state has to be. That last question is exactly the one that went wrong a minute ago.
Image: Five small icons in a row, a tally, a sum, a trophy, a magnifier, and a funnel.
---
## Slide 10: What you are about to build
- Build 1: Lab U03-03 Game Night Leaderboard
- Count, total, high score, low score, and a search
- Step 4 starts the low score at 0 on purpose
- Build 2: v1 test scripts, playtest fixes, README
- CAC teams: final checks and submission first
Speaker notes: Build one is the leaderboard lab. One pass through a night of game results answers four questions, and a second loop searches for a player's first big round and stops as soon as it finds it. Step four makes you start the low score at zero and record the result. Build two is your text adventure. Write your win and lose test scripts, fix what your playtester found Friday, and draft your README, because v1 is due at the end of the day tomorrow. Congressional App Challenge teams, today is your last class day to submit, and I will check in with you first.
Image: A four-line leaderboard summary above a search result line, navy and accent blue.
---
