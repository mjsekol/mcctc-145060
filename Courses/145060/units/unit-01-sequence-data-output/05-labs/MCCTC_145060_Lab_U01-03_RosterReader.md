# Lab U1-03: Roster Reader
## 145060 Programming · Unit 1 · Week 4 · Wednesday, September 30

**Gate:** 3 (open tooling). **Duration:** Build 1, 35 minutes.
**Competencies:** 5.5.7 (read inputs, including data files), 5.2.4 (string operations
including substring), 5.5.6 (format output), 5.4.6.

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W04_ReadingFiles.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W04_ReadingFiles.pptx)

---

## The scenario

The club's sign-up system exports its roster as a plain text file, and the export was
designed a long time ago. Every line has exactly the same layout, with the name padded
out to a fixed width and the member code starting at the same position on every line.

Nobody on the club board can read it comfortably, and somebody retypes it into a
spreadsheet every week.

## What you will build

A program that reads the roster file and prints a clean report: each member's name,
season year, and member number, lined up in columns.

**Why a fixed-width file.** You do not have loops yet, and you do not have a way to
split a line on commas. You do have slicing, and a fixed-width file is exactly the
format slicing was made for. Older systems really do export data this way, so this is
not a classroom invention.

---

## The data file

`roster.txt` is in `05-labs/fixtures/`. Copy it into the same folder as your program.
Here it is with a column ruler above it so you can see the layout:

```
0         1         2         3
0123456789012345678901234567890123
Ava Ruiz            ROBO-2026-114
Marcus Delgado      BAND-2027-009
Priya Patel         ROBO-2026-207
```

| Positions | Field |
|---|---|
| 0 to 19 | Member name, padded with spaces to 20 characters |
| 20 to 32 | Member code, for example `ROBO-2026-114` |

Inside the code, the season year is positions 5 to 8 and the member number is
positions 10 to 12.

---

## Starter code

Create `roster_reader.py`. It runs. It does nothing useful.

```python
# roster_reader.py
# Reads the club roster file and prints a clean report, one member per line.
#
# roster.txt is a FIXED-WIDTH file. Every line has the same layout:
#   positions 0-19   member name, padded with spaces to 20 characters
#   positions 20-32  member code, like ROBO-2026-114
#
# This file runs right now. It does not do anything useful yet.

print("CLUB ROSTER REPORT")
print("------------------")

# TODO 1: Open roster.txt, read the whole file, close it, and print its length.

# TODO 2: Open it again and read the first line.

# TODO 3: Pull the name and the code out of that line by position.

# TODO 4: Pull the season year and member number out of the code.

# TODO 5: Print a formatted report line for the member.

# TODO 6: Repeat TODOs 2 through 5 for the second and third lines.

print("Nothing is in the report yet.")
```

Running it produces:

```
CLUB ROSTER REPORT
------------------
Nothing is in the report yet.
```

---

## Steps

### Step 1. Get the file next to your program
Copy `roster.txt` into your project folder.
**Observable result:** it appears in the VS Code sidebar next to `roster_reader.py`.

### Step 2. Read the whole file and report its size
Replace TODO 1. Open, read, close, then print the length with a label.
**Observable result:** `File size: 102 characters`. If you get `FileNotFoundError`, your
terminal is not in the folder that holds the file. Read the path in the error.

### Step 3. Read the first line and look at it honestly
Replace TODO 2. Open the file again and read one line. Print it wrapped in `repr()`.
**Observable result:** the line ends in `\n`. That newline is part of what you read.

### Step 4. Take the line apart by position
Replace TODO 3. Slice the name and the code out of the line. Strip the padding off the
name.
**Observable result:** printing `repr(name)` shows `'Ava Ruiz'` with no trailing spaces.

### Step 5. Take the code apart
Replace TODO 4. Slice the year and member number out of the code. Write the position
map as a comment above the slices.
**Observable result:** `2026` and `114`. If either is one character short, you stopped
one position too early.

### Step 6. Print the report line
Replace TODO 5 with an f-string. Pad the name so the columns line up.
**Observable result:** one clean line for Ava Ruiz.

### Step 7. Do it two more times
Replace TODO 6. Copy your block for the second and third members. Close the file at the
end.
**Observable result:** three aligned lines.

**Notice what you have done.** You copied the same five lines three times. With three
members that is tolerable. With three hundred it is absurd. **That feeling is the reason
loops exist**, and you get them in Unit 3.

### Step 8. Read a line that is not there
Add a fourth `readline()` call after the third member and print the name and code you
slice out of it, each wrapped in `repr()`. Then delete it.
**Observable result:** empty strings. **No error.** Write down what you saw.

---

## Acceptance criteria

- [ ] The report prints all three members with name, season year, and member number
- [ ] Names have no trailing padding, proved with `repr()` at least once
- [ ] Every slice has a position-map comment above it
- [ ] The columns line up
- [ ] The file is closed after each time it is opened
- [ ] Step 8's result is recorded in your README under `Known limitations`
- [ ] Committed and pushed

---

## If it breaks

### 1. The file is not found

```
FileNotFoundError: [Errno 2] No such file or directory: 'rooster.txt'
```

**Cause:** a typo in the filename, or your terminal is in a different folder from the
file. The path is looked up relative to where you **ran** the program. The error message
tells you exactly where Python looked.

### 2. Everything comes out as empty strings, and nothing crashes

**Cause:** you called `readline()` more times than there are lines. At the end of a file
`readline()` returns `''`, and every slice of an empty string is another empty string.
**This is the bug that does not crash**, and it is the reason for step 8.

### 3. The member number is two digits

**Cause:** your slice stops one position too early. `code[10:12]` gives two characters.
Up to but not including: `code[10:13]`.

### 4. The name has spaces after it and the columns wobble

**Cause:** you sliced the name field and did not strip it. The field is padded to 20
characters on purpose. `.strip()` removes the padding.

### Not an error: the file size is 102

Three lines of 33 characters plus a newline each is 102. Python reads line endings as a
single `\n` character even on Windows, so the count is the same on every machine.

---

## Stretch goal

Somebody asks for the roster exported with commas instead of padding:

```
Ava Ruiz,ROBO-2026-114
```

Try your position slices on that line. Record what comes out. Then write two sentences in
your README: why does slicing by position work on one format and fail on the other, and
what would you need in order to handle the comma version?

---

## Submission checklist

- [ ] Runs with no traceback
- [ ] Three aligned report lines, full years and three-digit member numbers
- [ ] Step 8 recorded in `Known limitations`
- [ ] Pushed

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still stuck on `FileNotFoundError` at 10 minutes | SCAFFOLDED |
| Working steadily, question is about a slice position | STANDARD |
| Finished step 7 in 15 minutes, or asked how to handle more members | EXTENDED |
| Asked why anyone would store data like this | APPLIED |

## SCAFFOLDED

**Changed sections:** the starter already opens the file and reads the first line, and
includes the position map as a comment. The student writes the slices and the print for
member 1 only. Steps 7 and 8 are removed. One checkpoint: show the terminal after step 5.

**Acceptance criteria:** member 1 printed with name, year, and member number, all correct,
name stripped.

**Grading:** same 100-point scale. A complete SCAFFOLDED earns what a complete STANDARD
earns. The scope is smaller, not the standard.

## STANDARD

The base lab above, unchanged.

## EXTENDED

Everything in STANDARD, plus: **handle the comma-separated version of the roster** from
the stretch goal, for all three members.

**Hint, not the answer.** You need to know where the comma is, because it moves depending
on how long the name is. Strings carry a method that reports the position of the first
occurrence of a character. You met it in the Badge Maker EXTENDED option. Remember the
warning that came with it: it returns `-1` when nothing is found, and `-1` is a valid
slice position.

**Acceptance criteria:** STANDARD, plus the comma version prints identical report lines,
plus a README note on what happens with a line that has no comma.

## APPLIED

**Changed scenario.** Real fixed-width formats are everywhere once you look. Pick one you
can describe honestly: a line from a printed bus schedule, a scoreboard export, a bank
statement layout, a sports results table. Invent three lines of data in that layout,
document the positions in a table like the one above, and write the same reader for it.

**Acceptance criteria:** STANDARD, applied to your own layout, with a positions table in
the README.

**Grading:** same scale. Requirements Fit is judged on whether the positions table
matches the data file exactly.
