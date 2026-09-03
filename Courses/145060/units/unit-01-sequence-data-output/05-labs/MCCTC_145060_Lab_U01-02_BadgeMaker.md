# Lab U1-02: Badge Maker
## 145060 Programming · Unit 1 · Week 3

**Gate:** 3 (open tooling). **Duration:** three Build 2 blocks, Tuesday through
Thursday. **Competencies:** 5.2.4 (string operations including substring), 5.5.6
(format output), 5.5.5 (naming and comments), 5.4.6.

---

## The scenario

Your club runs a sign-in sheet and people type their names however they feel that
morning. `ava ruiz`, `AVA RUIZ`, and `  Ava Ruiz  ` are the same person and none of
them look the same to a computer. Somebody then has to make badges from that list.

Every member also has a code like `ROBO-2026-114` that carries the club, the season,
and the member number, all packed into one string.

## What you will build

A program that takes a carelessly typed name and a member code, cleans the name,
pulls the pieces out of the code, and prints a badge that looks deliberate.

---

## Starter code

Create `badge_maker.py` and type this in. It runs. It does nothing useful.

```python
# badge_maker.py
# Turns a messily typed name and a club code into a clean printed badge.
#
# This file runs right now. It does not do anything useful yet.

print("BADGE MAKER")
print("-----------")

raw_name = input("Type your name however you normally would: ")

# TODO 1: Clean the name. Remove stray spaces at the ends and fix the capitals.

# TODO 2: Store the club code, for example ROBO-2026-114.

# TODO 3: Pull the year out of the club code using its position.

# TODO 4: Pull the member number out of the club code.

# TODO 5: Print the badge using an f-string, with the name on its own line.

print("Nothing is on the badge yet.")
```

Running it and typing anything produces:

```
BADGE MAKER
-----------
Type your name however you normally would: ava
Nothing is on the badge yet.
```

**Use a real club and a real code shape.** Robotics, band, a job, a team, a group
chat. The code shape is yours to design as long as it packs at least three pieces of
information into one string.

---

## Part 1: Tuesday, steps 1 through 5

### Step 1. Starter running and committed
Create it, run it, commit it.
**Observable result:** three lines of output, and a new commit in `git log --oneline`.

### Step 2. Clean the name
Replace TODO 1. Handle stray spaces at both ends and fix the capitalisation, in one
expression, stored in a well-named variable.

**Observable result:** print your cleaned name temporarily and confirm that typing
`  ava RUIZ  ` gives `Ava Ruiz`.

### Step 3. Prove the spaces are gone
Print your cleaned name wrapped in `repr()`, or inside square brackets.

**Observable result:** you can see exactly where the string starts and stops. Without
this step you are trusting that `.strip()` worked. Do not trust it, check it.

### Step 4. Store the club code
Replace TODO 2 with your code as a string.

**Observable result:** the program runs unchanged, because nothing uses it yet.

### Step 5. Write the position map, then commit
In a comment above where you will slice, write out your code with position numbers
underneath it, exactly like the lecture notes do.

**Observable result:** a comment in your file that a reader could use to check your
slices without counting. Commit.

### Acceptance criteria, Part 1
1. `python badge_maker.py` runs with no traceback
2. Typing `  ava RUIZ  ` produces a correctly cleaned name, proved with `repr()`

---

## Part 2: Wednesday, steps 6 through 10

### Step 6. Pull out the year
Replace TODO 3 using a slice. Use your position map.

**Observable result:** printing it gives the full year. **If it is one character
short, you stopped one too early.** Up to but not including.

### Step 7. Pull out the member number
Replace TODO 4. This one runs to the end of the string, so you can leave the second
number out.

**Observable result:** the complete member number, with no leading dash.

### Step 8. Break your own slice on purpose
Change the year slice so it stops one position too early. Run it. Write down what it
printed and whether there was an error.

**Observable result:** a wrong year and **no error message**. Put both in your README
under `What I learned`. Then fix it.

### Step 9. Check the ends
Print the first character of your code and the last character, using an index and a
negative index.

**Observable result:** the first and last characters, confirming your code is the
length you think it is.

### Step 10. Commit
**Observable result:** `git log --oneline` shows at least three commits.

### Acceptance criteria, Part 2
3. Every slice has a position-number comment above it
4. The year and the member number are both correct and complete

---

## Part 3: Thursday, steps 11 through 14

### Step 11. Build the badge
Replace TODO 5. Use f-strings. The badge needs a border, the name on its own line,
and the pieces you extracted, each labelled.

**Observable result:** a badge whose edges line up. If they do not, you need
alignment, which is `:<26` or `:>26` inside the braces.

### Step 12. Make it a fixed width
Every line inside the border must be the same width regardless of how long the name
is. Test it with a short name and a long one.

**Observable result:** `Ava Ruiz` and `Bartholomew Fitzgerald` both produce a badge
with straight edges.

### Step 13. Find where your cleaner fails
Run your program with `mcdonald`, then `o'brien`, then `van der berg`.

**Observable result:** at least one of them comes out wrong. Write which one and what
it did in your README under `Known limitations`. **Do not try to fix it.** Naming the
failure is the assignment.

### Step 14. README and push
Four sections: what it is, how to run it, a real sample run, and `Known limitations`
containing step 8's silent wrong answer and step 13's name.

---

## Acceptance criteria, full lab

- [ ] The name is cleaned of end whitespace and capitalisation in one expression
- [ ] `repr()` or brackets used at least once to prove whitespace is gone
- [ ] Every slice has a position-number comment above it
- [ ] The year and member number extractions are complete and correct
- [ ] The badge border lines up for both a short and a long name
- [ ] Every printed value uses an f-string, not `+`
- [ ] README has all four sections
- [ ] `Known limitations` names the silent wrong slice **and** a name your cleaner breaks
- [ ] Three or more commits with messages saying why
- [ ] Pushed

---

## If it breaks

### 1. Your extracted piece is one character short

```
Season 202
```

**Cause:** the slice stopped one position too early. A slice runs from the first
number **up to but not including** the second. **No error appears**, which is why
step 5's position map exists. Count against the map rather than guessing.

### 2. Index out of range

```
IndexError: string index out of range
```

**Cause:** you asked for a position past the end. The last valid position is
`len(code) - 1`. Note that slicing past the end does **not** do this, so if you are
getting this error you used a single index, not a slice.

### 3. The spaces are still there

**Cause:** you called `.strip()` and did not store the result. String methods hand
back a new string and leave the original alone. You need `clean = raw.strip()`, not
`raw.strip()` on its own.

### 4. The badge edges do not line up

**Cause:** you are printing names of different lengths inside a fixed border without
padding them. Use `:<26` inside the f-string braces to pad to a fixed width.

### Not an error: `.title()` gets a name wrong

That is step 13 and it is expected. Record it, do not fix it.

---

## Stretch goal

Make the border width adapt to the longest line rather than being a number you typed.
You will need `len()` and a little arithmetic.

Then answer in your README: what happens to your badge if somebody types a name that
is 60 characters long? Try it. Decide whether you care, and say why.

---

## Submission checklist

- [ ] Runs with no traceback
- [ ] Tested with a short name, a long name, and a messy name
- [ ] Tested with `mcdonald`, `o'brien`, and `van der berg`
- [ ] `git status` clean, pushed, README renders on GitHub
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Still counting positions on their fingers at 15 minutes, or no position map written | SCAFFOLDED |
| Working steadily, asking about wording rather than mechanics | STANDARD |
| Finished Part 2 in 20 minutes, or asked about negative slicing before you taught it | EXTENDED |
| Said the badge is pointless, or that they are not in a club | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** TODO 2 and the position map are already filled in, with the code
  `ROBO-2026-114` and its positions written out.
- **Steps:** Part 2 drops step 9. Part 3 drops step 12, the fixed-width requirement.
  The badge may have ragged edges.
- **Step 8 stays.** Do not cut the deliberate break. It is the point of the week.
- **Checkpoints:** show you the terminal after step 3 and after step 7.
- **README:** two sections plus `Known limitations`.

**Acceptance criteria:** program runs; name cleaned and proved with `repr()`; year and
member number both extracted correctly; `Known limitations` records step 8.

**Grading:** same 100-point scale, Requirements Fit judged against this list. A
student who completes this fully earns what a student completing STANDARD fully earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not taught.

**Added requirement.** Your slices only work because you know exactly where the dashes
are. Make the program find them instead, so it works on `ROBO-2026-114` and
`BAND-2027-9` without you editing the numbers.

**Hint, not the answer.** Strings carry a method that reports the position of the
first occurrence of a character. Read the string methods section of
`https://docs.python.org/3/library/stdtypes.html#string-methods` and look for one
whose description mentions the lowest index where a substring is found. There is also
a nearly identical method that behaves differently when the character is absent, and
knowing which one you have matters.

**Second added requirement.** In your README, answer this: what does your program do
if the code has no dash in it at all? Try it. Report what happened, exactly.

**The honest warning:** the method you are most likely to find returns `-1` when it
finds nothing, and `-1` is a valid position in a slice. Your program will not crash.
It will quietly do something wrong. That is the whole lesson of this week arriving
one level up, and documenting it earns more than avoiding it.

**Acceptance criteria:** all STANDARD criteria, plus the program works on two codes of
different lengths without edits, plus the README reports what happens with no dash.

---

## APPLIED

**For the student who says this does not apply to them.** Same skills, and the badge
was never the point.

**Changed scenario.** Find any real string in your life that packs several pieces of
information into one value, and take it apart. Real options: a licence plate, a
flight number, a product SKU, a class period code, a video game item ID, a tracking
number, an ISBN, a VIN.

**What you build.** A program that takes one of these, extracts at least three named
pieces by position, and prints them labelled and aligned.

**The extra requirement that makes it the same lab.** Your README must include a
section called `The shape` explaining the format: how many characters, what each
region means, and one example of a value that would break your extraction. Then
actually run that breaking value and record what happened.

**Acceptance criteria:** all STANDARD criteria applied to your chosen string, plus
`The shape` section, plus the recorded result of the breaking value.

**Grading:** same scale. Requirements Fit is judged on whether the extraction is
right for the format the student chose, which is harder than the standard version,
because the instructor does not know their format and the README has to explain it.
