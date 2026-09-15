# Lecture Notes: break, continue, and Validation Loops
## 145060 Programming · Unit 3 · Week 7, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W07_LoopControl.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W07_LoopControl.pptx)

If you missed class, you can learn this concept from this file alone. Know where Ctrl+C is before
you start. Today's wrong version does not crash and does not stop.

---

## Why this exists

Players type anything. Somebody will type `loud` when your game asks for a frequency. Somebody will
type `12` when it asks for a number from 1 to 8. Somebody will press Enter on an empty line to see
what happens.

Right now your programs have two responses to a bad answer: crash, or refuse once and move on with
a bad value. A real program does a third thing. **It keeps asking until the answer is usable.** That
is a validation loop, and it is how every form, kiosk, and game you have ever used behaves.

To write one cleanly you need two new words that change how a loop runs from the inside:

- **`break`** ends the loop immediately.
- **`continue`** skips the rest of this pass and goes straight to the next one.

Both are part of outcome 5.3.6, and the validation loop is your first real taste of 5.5.1, data
validation, which Unit 4 finishes.

---

## The concept in plain language

```python
while True:
    answer = input("...")
    if the answer is not usable:
        print("what was wrong, and what to type instead")
        continue        # back to the top: ask again
    break               # the answer is usable: leave the loop

# only a usable answer ever reaches this line
```

**`while True:`** is a loop whose condition never becomes False on its own. That sounds like an
infinite loop, and it would be one, except that a `break` inside it provides the exit. You use it when
the natural place to decide "stop" is in the middle of the block, after the input, not at the top.

| Keyword | What happens | Where the program goes next |
|---|---|---|
| `break` | The loop ends now | The first line after the loop |
| `continue` | This pass ends now | The top of the loop, for the next pass |

Both apply to **the loop they are directly inside**. Thursday you will see why that detail matters.

---

## Worked example 1: a validation loop for a whole number in a range

```python
# Keep asking until the answer is usable. Only a usable answer gets past the loop.
MAX_TICKETS = 8

while True:
    tickets_text = input(f"How many tickets, 1 to {MAX_TICKETS}? ").strip()
    if not tickets_text.isdecimal():
        print("Type a whole number, like 2.")
    elif int(tickets_text) < 1 or int(tickets_text) > MAX_TICKETS:
        print(f"You can buy between 1 and {MAX_TICKETS} tickets.")
    else:
        break

tickets = int(tickets_text)
print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
```

Typing `two`, `12`, `0`, then `  3 `:

```
How many tickets, 1 to 8? two
Type a whole number, like 2.
How many tickets, 1 to 8? 12
You can buy between 1 and 8 tickets.
How many tickets, 1 to 8? 0
You can buy between 1 and 8 tickets.
How many tickets, 1 to 8?   3 
Ordering 3 tickets at $12 each: $36
```

**Order matters inside the loop.** `.isdecimal()` is checked **before** `int()` ever touches the text.
If `int("two")` ran first, the program would crash with a `ValueError` and the loop would never get a
chance to ask again. Check that text can convert, then convert it.

`.isdecimal()` is a string method, like `.strip()` and `.lower()` from Week 3. It is True only when the
string is not empty and every character is an ordinary digit. `"-5"`, `""`, and `" 12"` are all False,
which is why `.strip()` comes first. You may find a similar method called `.isdigit()`. Do not use it for
this job: it also says True for characters such as a superscript two, which `int()` cannot convert.

---

## Worked example 2: the same loop, written with continue

When there are several checks, `continue` keeps each one flat and separate. This is the frequency dial
from the class adventure, Storm Relay, rewritten as a loop that keeps asking.

```python
# Validation loop for a number the program will convert.
LOWEST_FREQUENCY = 530
HIGHEST_FREQUENCY = 1700

while True:
    frequency_text = input("Frequency in kHz: ").strip()
    if not frequency_text.isdecimal():
        print("The dial takes whole numbers only, like 880.")
        continue
    frequency = int(frequency_text)
    if frequency < LOWEST_FREQUENCY or frequency > HIGHEST_FREQUENCY:
        print(f"The dial only runs from {LOWEST_FREQUENCY} to {HIGHEST_FREQUENCY} kHz.")
        continue
    break

print(f"Tuned to {frequency} kHz.")
```

Typing `loud`, `-5`, `2000`, `1470`:

```
Frequency in kHz: loud
The dial takes whole numbers only, like 880.
Frequency in kHz: -5
The dial takes whole numbers only, like 880.
Frequency in kHz: 2000
The dial only runs from 530 to 1700 kHz.
Frequency in kHz: 1470
Tuned to 1470 kHz.
```

Read it as a gate with two guards. Each guard either sends the input back to the top with `continue`, or
lets it through. The `break` at the bottom is only reachable by input that passed every guard.

---

## Worked example 3: break ends a search as soon as it has an answer

```python
# break: stop the loop the moment you have your answer.
SHOE_PRICE = 140
WEEKLY_PAY = 45

saved = 0
week = 0
while True:
    week = week + 1
    saved = saved + WEEKLY_PAY
    if saved >= SHOE_PRICE:
        break
print(f"Week {week}: you have ${saved}, enough for the shoes.")
```

```
Week 4: you have $180, enough for the shoes.
```

Nobody knows the number of weeks in advance, so this is a `while`. The loop stops on the first week the
savings are enough. Check it by hand: 45, 90, 135 are short, 180 is not.

---

## Worked example 4: continue skips one pass

```python
# continue: skip the rest of THIS pass and go straight to the next one.
REST_DAY = 4
for day in range(1, 8):
    if day == REST_DAY:
        print(f"Day {day}: rest")
        continue
    print(f"Day {day}: run 2 miles")
```

```
Day 1: run 2 miles
Day 2: run 2 miles
Day 3: run 2 miles
Day 4: rest
Day 5: run 2 miles
Day 6: run 2 miles
Day 7: run 2 miles
```

On day 4, `continue` skips the `run 2 miles` line and the `for` moves to day 5.

**A `continue` inside a `while` has a trap a `for` does not.** A `for` gets its next value from `range`
automatically. A `while` only moves on if the update line runs. Put the update **below** a `continue`,
and the skipped pass skips the update too:

```python
day = 1
while day <= 7:
    if day == 4:
        continue
    print(f"Day {day}: run")
    day = day + 1
```

```
Day 1: run
Day 2: run
Day 3: run
```

Then nothing. No error, no more output, and the program never ends. `day` is 4 forever. Press Ctrl+C.
In a `while`, update first, then `continue`.

---

## Worked example 5: a flag instead of break

`break` is not the only way out. Last week's `playing` flag works here too.

```python
# The same validation with a flag instead of break.
answer_ok = False
while not answer_ok:
    answer = input("Play again? (yes/no) ").strip().lower()
    if answer == "yes" or answer == "no":
        answer_ok = True
    else:
        print("Please type yes or no.")
print(f"You chose {answer}.")
```

Typing `maybe`, then `YES`:

```
Play again? (yes/no) maybe
Please type yes or no.
Play again? (yes/no) YES
You chose yes.
```

**Which is better?** Reasonable programmers disagree, and both sides have a point.

- **For `break`:** the exit sits exactly where the decision is made. No extra variable to track.
- **For the flag:** the `while` line tells a reader how the loop ends without reading the body, and there
  is exactly one exit. `while True:` with three `break` lines scattered through forty lines is hard to
  follow.

A reasonable rule for this course: **short validation loops use `break`. Game loops use a flag**, because
the game loop is long, has several endings, and needs to report which one happened.

---

## The wrong version: the check that never lets you out

A student writes the play-again question with a `while` condition instead of `break`:

```python
answer = input("Play again? (yes/no) ").strip().lower()
while answer != "yes" or answer != "no":
    print("Please type yes or no.")
    answer = input("Play again? (yes/no) ").strip().lower()
print(f"You chose {answer}.")
```

Typing `maybe`, then `yes`, then `no`:

```
Play again? (yes/no) maybe
Please type yes or no.
Play again? (yes/no) yes
Please type yes or no.
Play again? (yes/no) no
Please type yes or no.
Play again? (yes/no) 
```

**No error. Every answer is refused, forever.**

Build the truth table, the way you did in Unit 2:

| `answer` | `answer != "yes"` | `answer != "no"` | `or` result | Loop keeps going? |
|---|---|---|---|---|
| `"yes"` | False | True | **True** | yes |
| `"no"` | True | False | **True** | yes |
| `"maybe"` | True | True | **True** | yes |

Any single word is always different from at least one of `"yes"` and `"no"`, so the `or` is True for every
possible input. The exit condition can never fire. The fix is `and`: keep asking while the answer is not yes
**and** not no.

```python
while answer != "yes" and answer != "no":
```

```
Play again? (yes/no) maybe
Please type yes or no.
Play again? (yes/no) yes
You chose yes.
```

This is De Morgan's law from your truth tables, arriving in a place where getting it wrong freezes a program.
"Not yes or no" in English means "neither," and neither is `and`.

---

## Why the wrong version is tempting

**English lies.** "Keep asking while it is not yes or no" sounds exactly right out loud, and `or` is the word
you said.

**It looks like a working program.** It prints a sensible message every time. The only symptom is that it never
accepts anything, and a person testing with one wrong answer followed by Ctrl+C never sees the right answer
refused.

**The test that catches it is the valid answer.** Most people test validation by typing garbage. Always also type
every valid answer, and confirm the loop lets each one through.

---

## Vocabulary

| Term | What it means |
|---|---|
| **`break`** | Ends the loop it is directly inside, immediately. |
| **`continue`** | Ends the current pass of the loop it is directly inside and starts the next pass. |
| **`while True:`** | A loop with no condition of its own. It needs a `break` to end. |
| **Validation loop** | A loop that keeps asking until the input is usable. |
| **Data validation** | Checking that input is usable before the program relies on it, outcome 5.5.1. |
| **Guard** | A check that sends bad input back before the rest of the code sees it. |
| **`.isdecimal()`** | True when every character in a non-empty string is a digit, so `int()` is safe. |
| **Flag** | A `bool` a loop checks, such as `answer_ok` or `playing`. |

---

## Self-check

**Question 1.** Write the exact output.

```python
for number in range(1, 10):
    if number == 3:
        continue
    if number == 6:
        break
    print(number)
print("after")
```

**Question 2.** A club sign-up asks for a grade from 9 to 12. Write a validation loop that refuses anything
that is not a whole number, refuses numbers outside 9 to 12, and never crashes. Then say which single input
you would test first to prove the loop lets good answers through.

**Question 3.** This loop is supposed to ask for a size until it gets `s`, `m`, or `l`. It never ends, even on
`m`. Explain why using one row of a truth table, and fix the condition.

```python
size = input("Size (s/m/l): ").strip().lower()
while size != "s" or size != "m" or size != "l":
    size = input("Size (s/m/l): ").strip().lower()
```

---

### Answers

**1.**

```
1
2
4
5
after
```

3 is skipped by `continue`. When `number` is 6, `break` ends the loop before 6 prints, so 7, 8, and 9 never
happen.

**2.** One correct version:

```python
while True:
    grade_text = input("Grade (9-12): ").strip()
    if not grade_text.isdecimal():
        print("Type a whole number, like 10.")
        continue
    grade = int(grade_text)
    if grade < 9 or grade > 12:
        print("Sign-ups are for grades 9 through 12.")
        continue
    break
print(f"Grade {grade} signed up.")
```

Typing `ten`, `8`, `10`:

```
Grade (9-12): ten
Type a whole number, like 10.
Grade (9-12): 8
Sign-ups are for grades 9 through 12.
Grade (9-12): 10
Grade 10 signed up.
```

Test `9` and `12` first, the boundaries. A loop that refuses bad answers but also refuses a good one is broken,
and the boundaries are where it breaks. Full credit for any loop that checks `.isdecimal()` before `int()`, checks
the range, and has an exit reachable only by a valid grade.

**3.** For `size = "m"`: `"m" != "s"` is True, so the whole `or` is True before the other parts even matter. Every
possible input is different from at least one of the three letters, so the condition is always True. The fix:

```python
while size != "s" and size != "m" and size != "l":
```
