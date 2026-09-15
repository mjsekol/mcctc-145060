# Lab U5-01: Playlist Doctor
## 145060 Programming · Unit 5 · Week 10

**Gate:** 3 (open tooling). **Duration:** three Build 1 blocks, Monday through Wednesday.
**Competencies:** 5.1.5 (data management through programming languages: choosing a
structure), 5.2.2 (scope of data, including arrays), 5.5.7 (read inputs from a data
file), 5.3.6 (repetition).

---

## The scenario

Four friends built one shared road-trip playlist by each typing songs into a text file,
and nobody checked for repeats. Before the trip, there are two arguments to settle: how
many songs are actually on it once duplicates are gone, and whose favorite band took over.
You also want to know which songs you and a friend both picked, so those go first.

## What you will build

A program that reads the playlist into a list, removes duplicates without losing the
order, counts songs per artist with a dictionary, compares two playlists with sets, and
measures what choosing the wrong structure costs.

---

## Files you need

From `05-labs/fixtures/`, copy these two files into the folder where your program lives:

- `road_trip_playlist.txt`, the shared playlist, one `Artist - Title` per line
- `friend_playlist.txt`, a friend's separate list

The artists and songs are invented. **Open `road_trip_playlist.txt` and read it before
you write any code.** Look for the blank line, and for the line with spaces after the
title. Both matter.

---

## Starter code

Create `playlist_doctor.py` and type this in. It runs. It does nothing useful.

```python
# playlist_doctor.py
# Cleans up a shared road-trip playlist and settles the arguments about it.
#
# This file runs right now. It does not do anything useful yet.
#
# Part 1 (Monday): lists.  Part 2 (Tuesday): dictionaries.
# Part 3 (Wednesday): sets, and measuring why the choice matters.

PLAYLIST_FILE = "road_trip_playlist.txt"
FRIEND_FILE = "friend_playlist.txt"
SEPARATOR = " - "   # every line in the file is "Artist - Title"


def read_songs(filename):
    """Return every non-blank line of the file as a list, in file order."""
    # TODO Part 1: open the file, strip each line, skip blank lines,
    # append each song to a list, close the file, return the list.
    return []


def main():
    songs = read_songs(PLAYLIST_FILE)
    print(f"Songs in the file: {len(songs)}")

    # TODO Part 1: first song, last song, "in" check, count of one song,
    #              duplicates removed, one artist removed without the skip bug.

    # TODO Part 2: songs per artist in a dictionary, and the top artist.

    # TODO Part 3: sets, songs on both playlists, and the timing test.

    print("Nothing else yet.")


main()
```

Running it produces:

```
Songs in the file: 0
Nothing else yet.
```

---

## Part 1: Monday, lists

### Step 1. Starter running and committed
Create the file, copy in the two data files, run it, commit.
**Observable result:** the two lines above, and a commit in `git log --oneline`.

### Step 2. Read the file into a list
Finish `read_songs`. Strip every line. Skip lines that are empty after stripping. Append
the rest.
**Observable result:** `Songs in the file: 26`. If you see 27, a blank line got in. If
you see 0, the function still returns the empty starter list.

### Step 3. Reach in
In `main`, print the first song and the last song using an index, and print whether
`"Juno Okafor - Low Battery"` is on the list using `in`.
**Observable result:** the first song is `Static Lemonade - Porch Light`, the last is
`Ravi and the Late Bus - Friday Shift`, and the `in` check prints `True`.

### Step 4. Count one song
Use `.count()` to print how many times `"Mira Vance - Group Chat"` appears.
**Observable result:** `3`. If you see `2`, one copy still has spaces on the end, so
your strip is not happening. Look at step 2 again.

### Step 5. Remove duplicates, keeping the order
Write a function `without_duplicates(songs)` that returns a **new** list with each song
once, in the order first seen. Print how many songs are left.
**Observable result:** `17`.

### Step 6. Trigger the skip bug on purpose
Copy your song list, then loop over the copy with `for song in ...` and `.remove()` every
song whose text starts with `"Static Lemonade - "`. Print the songs by Static Lemonade
that are still there.
**Observable result:** at least one Static Lemonade song survives, and **there is no
error message**. Write which song survived, and why, in your README under
`What I learned`.

### Step 7. Remove an artist correctly
Write `without_artist(songs, artist)` that builds and returns a **new** list leaving that
artist out. Use it on your duplicate-free list for Static Lemonade and print the count.
**Observable result:** `14`. Commit.

### Acceptance criteria, Part 1
1. `read_songs` returns 26 songs, with no blank entries and no trailing spaces
2. The duplicate-free list has 17 songs, in first-seen order
3. README records the step 6 survivor and the reason, in your own words

---

## Part 2: Tuesday, dictionaries

### Step 8. Get the artist out of a song
Write `artist_of(song)` that returns the part before `" - "`. Use `.split(SEPARATOR)`.
**Observable result:** `artist_of("Mira Vance - Group Chat")` returns `"Mira Vance"`.

### Step 9. Count songs per artist
Write `count_by_artist(songs)` returning a dictionary of artist to number of songs. Use
the pattern from the lecture notes: if the key is there add one, otherwise start at one.
Run it on the **duplicate-free** list and print every artist and count, lined up.
**Observable result:** eight artists. Static Lemonade has 3. Every other artist has 2.

### Step 10. Find the top artist
Write `top_artist(counts)` that loops over `.items()` and returns the artist with the
most songs.
**Observable result:** `Static Lemonade`. The argument is settled.

### Step 11. Break a key both ways
Print `counts["Mira Vanse"]`, with the typo. Record the full error. Then change it to
`counts.get("Mira Vanse")` and record what prints instead.
**Observable result:** the first raises `KeyError: 'Mira Vanse'`. The second prints
`None` with **no error**. Write in your README which one you would rather have while
testing, and why. Put the correct spelling back and commit.

### Acceptance criteria, Part 2
4. `count_by_artist` returns the correct counts for all eight artists
5. `top_artist` returns `Static Lemonade` without hardcoding the name
6. README records both results from step 11

---

## Part 3: Wednesday, sets and the stopwatch

### Step 12. Count artists once
Print how many different artists there are, using a set.
**Observable result:** `8`.

### Step 13. Compare with a friend
Read `friend_playlist.txt` with your same `read_songs` function, turn both lists into
sets, and print how many songs you both have and each shared song in **sorted** order.
Then print how many songs are only on the friend's list.
**Observable result:** 6 shared songs, and 2 only on the friend's list. If your shared
songs print in a different order every run, you printed the set instead of `sorted()`.

### Step 14. Time the wrong choice
Build a list of 100,000 made-up track IDs with a loop (`f"TRACK{number:06d}"`) and a set
from that list. Build a list of 1,000 lookups from `99_500` up to `100_500`. Time how long
it takes to check every lookup with `in` against the list, then against the set, using
`time.perf_counter()`.
**Observable result:** two times printed. The list takes far longer. On the machine this
lab was tested on, the list took about 0.46 seconds and the set about 0.00015 seconds.
**Your numbers will be different, and that is expected.**

### Step 15. README and push
Add a section called `Choosing structures` with a small table: for the playlist, the
artist counts, and the shared songs, name the structure you used and one sentence on why.
Include your step 14 numbers and the computer you ran them on. Push.

### Acceptance criteria, Part 3
7. Shared songs and friend-only songs are correct and printed in a stable order
8. The timing runs and prints both numbers
9. README has `What I learned` and `Choosing structures`, with your own measured numbers

---

## Acceptance criteria, full lab

- [ ] `python playlist_doctor.py` runs from the folder holding the data files, no traceback
- [ ] 26 songs read, 17 after duplicates, 14 after removing Static Lemonade
- [ ] No list is changed while a `for` loop is walking through it, except in step 6's
      deliberate test
- [ ] Eight artists counted correctly; top artist found by the code
- [ ] 6 shared songs, printed sorted; 2 friend-only songs
- [ ] Timing prints two measured numbers
- [ ] README has `What I learned` (steps 6 and 11) and `Choosing structures` (step 15)
- [ ] Commits at the end of each part, with messages that say why
- [ ] Pushed

---

## If it breaks

### 1. The file is not found

```
FileNotFoundError: [Errno 2] No such file or directory: 'road_trip_playlist.txt'
```

**Cause:** the data file is not in the folder your terminal is running from. Python looks
relative to where you ran the command, not where your `.py` file is. Copy the file next
to your program and run from that folder.

### 2. Reaching into an empty list

```
IndexError: list index out of range
```

**Cause:** usually `songs[0]` on an empty list, because `read_songs` still returns `[]`,
or it never appended. Print `len(songs)` before you index.

### 3. A misspelled artist

```
KeyError: 'Mira Vanse'
```

**Cause:** the key is not in the dictionary, often a typo or different capitals. Keys are
exact. This is step 11 when you do it on purpose.

### 4. Using `{}` for an empty set

```
AttributeError: 'dict' object has no attribute 'add'
```

**Cause:** `{}` makes an empty dictionary. An empty set is `set()`.

### Not an error: 27 songs, or `Group Chat` counted twice instead of three times

**Cause:** a blank line got into the list, or a line kept its trailing spaces. The program
runs and the numbers are wrong. `line.strip()` removes the newline and the spaces, and an
`if song != ""` check skips the blank line.

---

## Stretch goal

A friend typed `mira vance - group chat` in lowercase. Your duplicate check does not catch
it. Make duplicates match regardless of capitals **while still printing each song with the
capitals from its first appearance**. Then write in your README one song title where
lowercasing everything would lose something that matters.

---

## Submission checklist

- [ ] Runs with no traceback from a clean terminal in the lab folder
- [ ] Numbers in the acceptance criteria all match
- [ ] Step 6 and step 11 results recorded, not guessed
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| At 15 minutes into Monday, `read_songs` still returns nothing, or they are copying songs into the file by hand | SCAFFOLDED |
| Working steadily; questions are about which method to use, not how a list works | STANDARD |
| Finished Part 1 by the end of Monday's Build 1, or asked "is there a built-in that counts things" | EXTENDED |
| Says they do not care about playlists, or asks when anyone would use this at a job | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `read_songs` is already written for them. They start at step 3.
- **Part 1:** step 7 gives them the empty `kept = []` line and the `for` line; they write
  the condition and the append.
- **Part 2:** step 9 gives the counting loop with the `else` branch blank.
- **Part 3:** step 14 is replaced with running the timing program from the lecture notes
  and recording the two numbers, rather than writing it.
- **Checkpoints:** show you the terminal after steps 5, 9, and 13.
- **Step 6 and step 11 stay.** The silent failures are the point of the week.

**Acceptance criteria:** 17 after duplicates, 14 after removing the artist, correct artist
counts, 6 shared songs, both silent-failure results recorded in the README.

**Grading:** same 100-point scale, Requirements Fit judged against this list. Completing
SCAFFOLDED fully earns what completing STANDARD fully earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus a challenge that needs something not taught.

**Added requirement 1.** Python's standard library has a tool built to count things.
Rewrite `count_by_artist` using it, and print the **three** most common artists with one
method call.

**Hint, not the answer.** Read the section for `Counter` in the `collections` module
documentation, `https://docs.python.org/3/library/collections.html#collections.Counter`.
Look for a method whose name says it returns the most common elements.

**Added requirement 2.** Print every artist sorted from most songs to fewest, using
`sorted()` with a `key`. Read the "Sorting Techniques" how-to,
`https://docs.python.org/3/howto/sorting.html`, the section on key functions.

**Added requirement 3.** In your README, answer: when two artists have the same count, what
order does your program print them in, and is that order guaranteed? Test it rather than
guessing.

**The honest warning:** every artist but one has exactly 2 songs, so ties are everywhere.
A program that looks like it "ranks" artists is mostly printing them in the order they
were first seen. Saying so in the README earns more than hiding it.

**Acceptance criteria:** all STANDARD criteria, plus `Counter` used correctly, a sorted
ranking, and the tie question answered from a test.

---

## APPLIED

**For the student who asks when anyone would use this.** Same skills, a completely
different kind of data: your own repository's history.

**Changed scenario.** In your own course repository, run:

```
git log --format=%ad --date=format:%a > commit_days.txt
```

That writes the day of the week of every commit you have made, one per line. It contains
nothing personal. **Run it in a Git Bash terminal.** Windows PowerShell's `>` writes the
file in a different encoding depending on the machine's settings, and the first line can
arrive with an invisible marker glued to it. If your first day reads as something like
`'﻿Mon'`, open the file with `encoding="utf-8-sig"`, which removes that marker. Your program answers: how many commits in total, how many on each day of
the week (dictionary), which days you have never committed on (set difference against the
seven days), and the day you commit most.

**The extra requirement that makes it the same lab.** Your README includes a section called
`What the data says` with the counts, and one honest sentence about your own work habits
that the numbers support. Then repeat step 6's deliberate bug on your list of days: remove
every `Fri` with a `for` loop and `.remove()`, and record whether any survived and why.

**Acceptance criteria:** all STANDARD criteria that apply, with the same structures used for
the same reasons, plus the `What the data says` section and the step 6 result.

**Grading:** same scale. Requirements Fit is judged on whether each structure matches the
question it answers.
