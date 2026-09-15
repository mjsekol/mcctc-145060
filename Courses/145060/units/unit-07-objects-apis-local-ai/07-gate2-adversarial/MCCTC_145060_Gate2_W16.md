# Gate 2: Adversarial Review · Week 16
## 145060 Programming · Unit 7 · Friday, January 8

**40 minutes.** Individual. You may and should run the code. You may not ask a model
whether it is correct, because the model is what is being reviewed.

The program is `gate2-w16-files/playlist.py`. Copy it and run it.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got the program in
`playlist.py`. It runs. It is formatted well and the comments sound sure of themselves.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

**One of these does not show up until you make two playlists.** With one playlist, the
program looks perfect. Read the spec, then try things the sample run does not.

---

## PART A: The requirements

> Write `playlist.py` with a `Song` class and a `Playlist` class.
>
> A `Song` has a title, an artist, and a length in **seconds**.
>
> A `Playlist` has a name and its own list of songs. It must:
>
> 1. Add a song with `add_song`. **Refuse a song whose length is zero or negative**, since
>    that is not a real song.
> 2. Report the total length with `total_minutes`, as **whole minutes rounded down**.
> 3. Report the **title of the longest song** with `longest`.
> 4. Print a one-line `summary` with the name, the number of songs, the total minutes,
>    **and the title of the longest song**.
> 5. Two different playlists must not share songs.

---

## PART B: What the AI produced

The code is in `gate2-w16-files/playlist.py`. Run it:

```
python playlist.py
```

A real run:

```
Party Mix: 3 songs, 9 minutes total.
```

**Read that one line against the five requirements before you read the code.** One
requirement is not met in that line alone.

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real person or
playlist**, and **the fix**. Then one final entry: **what I was unsure about**, naming
something specific. That entry is scored and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** run it. Compare the output line to the five requirements.
- **Next 10:** make a second playlist and add different songs to each. Watch what happens.
- **Next 10:** add a song with 0 seconds, and a song with a negative length.
- **Rest:** read each comment against the code under it. Ask whether it is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states
the security weighting before you start.

**Four of five is a strong score.**
