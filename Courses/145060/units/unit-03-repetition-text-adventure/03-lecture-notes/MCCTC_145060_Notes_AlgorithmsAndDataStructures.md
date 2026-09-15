# Lecture Notes: Algorithms and Data Structures in Information Processing
## 145060 Programming · Unit 3 · Week 8, Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W08_AlgorithmsAndData.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W08_AlgorithmsAndData.pptx)

If you missed class, you can learn this concept from this file alone. You need two data files,
[`playlist.txt`](../05-labs/fixtures/playlist.txt) and
[`playlist_sorted.txt`](../05-labs/fixtures/playlist_sorted.txt). Save both in the same folder as
your program, and run the program from that folder, or `open()` will not find them.

---

## Why this exists

Every app you use is mostly information processing. A music app counts your plays and finds your top
song. A grade portal adds up points and finds the lowest quiz. A game finds the high score. None of
that is magic, and none of it is one giant clever line. It is a small number of **algorithms**, run over
data that has been organized in a particular way.

Two words carry this whole lesson, and the WebXam uses both in outcome 5.1.2: **explain how algorithms
and data structures are used in information processing.**

- An **algorithm** is a precise, finite sequence of steps that solves a problem. Your pseudocode is an
  algorithm written in English.
- A **data structure** is the way data is organized so a program can use it. A fixed-width file where
  every record is one line, with the title always in the same positions, is a data structure.

**The idea that makes this more than vocabulary:** the way data is organized decides which algorithms
are possible and how much work they take. Change the structure and the algorithm changes with it.

---

## The data: one song per line

`playlist.txt` is fixed width, the same kind of file as Week 4's roster:

```
Parking Lot Anthem      The Late Buses       41
Fourth Period Blues     Mira Castellano      12
Group Chat Silence      Static Hallway       87
Friday Lights           The Late Buses       63
Low Battery             Jonah Reyes           9
Snow Day Rumor          Static Hallway       28
Bus Seat Window         Mira Castellano      55
Last Lap                Jonah Reyes          30
```

| Positions | Field |
|---|---|
| 0-23 | Title |
| 24-43 | Artist |
| 44-46 | Plays |

Every record has the same shape. That sameness is what makes the structure useful: a loop can apply the
exact same slices to every line.

**The loop that reads it** is a sentinel loop. Week 4 taught you that `.readline()` returns `""` at the end
of the file and never before, because even a blank line comes back as `"\n"`. In Week 4 that empty string
was a trap. Today it is the sentinel.

```python
line = playlist.readline()
while line != "":
    # process one record
    line = playlist.readline()
```

Every algorithm below uses this loop. What changes is what happens to each record.

---

## Algorithm 1: count and total

```python
# Algorithm 1: count and total. Read one record at a time until the file runs out.
playlist = open("playlist.txt")
song_count = 0
total_plays = 0

line = playlist.readline()
while line != "":
    plays = int(line[44:47])
    song_count = song_count + 1
    total_plays = total_plays + plays
    line = playlist.readline()

playlist.close()
print(f"{song_count} songs, {total_plays} plays")
```

```
8 songs, 325 plays
```

Two accumulators, both set to 0 before the loop, both updated once per record. Check it: 41 + 12 + 87 + 63 +
9 + 28 + 55 + 30 is 325.

---

## Algorithm 2: the biggest value, and whose it is

```python
# Algorithm 2: the biggest value, and which record it belongs to.
playlist = open("playlist.txt")
most_plays = 0
top_song = ""

line = playlist.readline()
while line != "":
    title = line[0:24].strip()
    plays = int(line[44:47])
    if plays > most_plays:
        most_plays = plays
        top_song = title
    line = playlist.readline()

playlist.close()
print(f"Most played: {top_song} ({most_plays} plays)")
```

```
Most played: Group Chat Silence (87 plays)
```

**The algorithm in one sentence:** keep the best one seen so far, and replace it whenever a better one shows up.
The number alone is not useful. "87" answers nothing. So the algorithm keeps two pieces of state together: the
best value and the label that goes with it. When one changes, both change.

---

## Algorithm 3: search, and stop when you find it

```python
# Algorithm 3: search. Stop the moment you find what you came for.
wanted_artist = input("Artist to find: ").strip().lower()
playlist = open("playlist.txt")
lines_read = 0
found_title = ""

line = playlist.readline()
while line != "":
    lines_read = lines_read + 1
    if line[24:44].strip().lower() == wanted_artist:
        found_title = line[0:24].strip()
        break
    line = playlist.readline()

playlist.close()
if found_title == "":
    print(f"No songs by that artist. Read {lines_read} lines.")
else:
    print(f"First song by that artist: {found_title}. Read {lines_read} lines.")
```

Typing `static hallway`, then running it again and typing `Taylor`:

```
Artist to find: static hallway
First song by that artist: Group Chat Silence. Read 3 lines.
```

```
Artist to find: Taylor
No songs by that artist. Read 8 lines.
```

Wednesday's `break` is what makes this a search rather than a count: the loop stops as soon as the question is
answered. But look at the second run. **When the answer is "not here," a search has to read everything to be
sure.** There is no shortcut in this file, because the songs are in no particular order.

Notice also `==` on the whole artist field, not `in`. `"hall" in "static hallway"` is True. A search that matches
part of a field finds things you did not ask for.

---

## Same question, two data structures

Here is the idea from the top of this file, made concrete. The question is Algorithm 2's: **which song has the
most plays?** The only difference is how the same eight songs are organized.

```python
# Same question, two ways of organizing the same data.
# Question: which song has the most plays?

# Structure A: songs in the order they were added.
# A bigger number could be on any line, so every line has to be read.
playlist = open("playlist.txt")
lines_read = 0
most_plays = 0
top_song = ""
line = playlist.readline()
while line != "":
    lines_read = lines_read + 1
    plays = int(line[44:47])
    if plays > most_plays:
        most_plays = plays
        top_song = line[0:24].strip()
    line = playlist.readline()
playlist.close()
print(f"Added order: {top_song}, after reading {lines_read} lines")

# Structure B: the same songs, sorted from most plays to fewest.
# The answer is on the first line, so the algorithm is one read.
playlist = open("playlist_sorted.txt")
line = playlist.readline()
playlist.close()
print(f"Sorted order: {line[0:24].strip()}, after reading 1 line")
```

```
Added order: Group Chat Silence, after reading 8 lines
Sorted order: Group Chat Silence, after reading 1 line
```

Same answer. Eight reads against one. With eight songs that is nothing. With eight hundred thousand songs, one
algorithm reads eight hundred thousand lines and the other reads one.

**So why not always sort?** Because the structure has a cost too. Every time a song gets played, its count
changes, and a sorted file might need that song moved to a new position to stay sorted. The added-order file
never needs anything moved. **Neither structure is better. Each one makes some questions cheap and others
expensive,** and choosing is a real engineering decision.

You have already felt this in your text adventure. Your rooms live in `if`/`elif` branches inside the code.
That structure makes "describe this room" a single check. It makes "add a tenth room" a long edit in three
places. In Unit 5, rooms move into a data structure outside the code, and that single change is most of what
text adventure version 3 is.

---

## The wrong version: the least played song

Algorithm 2 found the biggest value by starting `most_plays` at 0. Flip it around to find the smallest:

```python
# The least played song. This runs, and it is wrong.
playlist = open("playlist.txt")
fewest_plays = 0
quiet_song = ""

line = playlist.readline()
while line != "":
    title = line[0:24].strip()
    plays = int(line[44:47])
    if plays < fewest_plays:
        fewest_plays = plays
        quiet_song = title
    line = playlist.readline()

playlist.close()
print(f"Least played: {quiet_song} ({fewest_plays} plays)")
```

```
Least played:  (0 plays)
```

**No error. A blank title and zero plays.** Every song has more than 0 plays, so `plays < fewest_plays` is False
on every single record, and nothing is ever replaced. The loop ran eight times and changed nothing.

The starting value was a guess, and the guess was already better than every real record. Starting at 0 happened to
work for the biggest value, because every real count is bigger than 0. It fails for the smallest for the same
reason.

**The fix: start from the first real record, not from a guess.**

```python
# The least played song, fixed: start from the first real record, not from a guess.
playlist = open("playlist.txt")
line = playlist.readline()
quiet_song = line[0:24].strip()
fewest_plays = int(line[44:47])

line = playlist.readline()
while line != "":
    title = line[0:24].strip()
    plays = int(line[44:47])
    if plays < fewest_plays:
        fewest_plays = plays
        quiet_song = title
    line = playlist.readline()

playlist.close()
print(f"Least played: {quiet_song} ({fewest_plays} plays)")
```

```
Least played: Low Battery (9 plays)
```

The first record becomes "the best seen so far," and the loop starts with the second record. This version would also
work for the biggest value, even if every count were negative. That is the version worth memorizing.

---

## Why the wrong version is tempting

**It worked last time.** Starting at 0 found the maximum correctly, so it feels like the standard way to start.

**The output is almost plausible.** A song with 0 plays is a real possibility. The blank title is the only visible
clue, and if you printed only the number you would have no clue at all.

**The algorithm is right and the setup is wrong.** Every line inside the loop is correct. The bug is one line above
it, where nobody looks when the loop "is the algorithm."

---

## Five algorithms worth recognizing

Almost every information-processing task you will meet this year is one of these, or a few of them in one loop.

| Algorithm | The question | Starting state | Can stop early? |
|---|---|---|---|
| **Count** | How many? | counter at 0 | No |
| **Total** | How much altogether? | total at 0 | No |
| **Maximum or minimum** | Which is biggest or smallest? | the first real record | No, unless the data is sorted |
| **Search** | Is it here, and where? | a "not found" value | Yes, with `break`, once found |
| **Filter** | Which ones match a rule? | a counter or nothing | No |

---

## Vocabulary

| Term | What it means |
|---|---|
| **Algorithm** | A precise, finite sequence of steps that solves a problem. |
| **Data structure** | The way data is organized so a program can use it. |
| **Record** | One complete entry in a data set, here one song on one line. |
| **Field** | One piece of a record, such as the title or the play count. |
| **Fixed-width file** | A file where each field sits in the same character positions on every line. |
| **Information processing** | Taking data in, applying algorithms to it, and producing useful output. |
| **Linear search** | Checking records one at a time, in order, until the target is found or the data runs out. |
| **Sorted** | Arranged in order by some field, which makes some questions cheaper to answer. |
| **Sentinel** | A special value that ends a loop. For `.readline()`, it is `""`. |

---

## Self-check

**Question 1.** Name the algorithm from the table above that each task needs, and say whether the loop can stop early.

- How many songs by Jonah Reyes are on the playlist?
- Is there any song called Low Battery?
- What is the total listening count across all songs?

**Question 2.** A class's quiz scores are in a file sorted from **lowest** score to highest. Which record holds the highest
score, and how many lines does the algorithm need to read to find it with only what you know today?

**Question 3.** A student writes a minimum-finding loop over game scores and starts `lowest = 1000`. It works on their test
file. Explain when it gives a wrong answer with no error, and give the fix.

---

### Answers

**1.**

| Task | Algorithm | Stop early? |
|---|---|---|
| How many songs by Jonah Reyes | Filter plus count | No, a later line could match too |
| Is there a song called Low Battery | Search | Yes, `break` once it is found |
| Total listening count | Total | No, every play count must be added |

**2.** The highest score is on the **last** line. With `.readline()`, the only way to reach the last line is to read every line
before it, so the algorithm reads all of them. The sort still helped: you know which line holds the answer without comparing
anything, but this file structure only lets you get to that line from the top. Being sorted the other way would make it one
read. Direction of the sort is part of the structure.

**3.** It fails when every real score is above 1000. `lowest` stays 1000 and the label never gets set, so the program reports a
score nobody scored. Starting from a guess only works if the guess is worse than every real value, and you cannot promise that
for data you have not seen. The fix is to read the first record, use it as the starting lowest, then loop over the rest.
