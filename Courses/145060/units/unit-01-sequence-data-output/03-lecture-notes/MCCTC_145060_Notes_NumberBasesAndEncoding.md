# Lecture Notes: Number Bases, Encoding, and Files
## 145060 Programming · Unit 1 · Week 4 · Monday through Wednesday

If you missed class, you can learn these three concepts from this file alone. Type
every example.

**Exam note.** Outcome 2.3 is 4.44% of the WebXam and Monday and Tuesday are the only
instruction it gets all semester. This file is the whole of it.

---

# Part 1 · Number bases (Monday)

## Why this exists

A computer stores everything as switches that are on or off. There is no third
position. Every number, letter, image, and sound in the machine is a pattern of those
switches, so if you want to understand what a computer is actually holding, you have to
be able to read that pattern.

## The concept in plain language

**A written number is a value plus a base.** The value is a quantity. The base is how
many digits you have to write it with.

In decimal, base 10, you have ten digits, 0 through 9. Each place is worth ten times
the place to its right:

```
    1     3
   10s   1s      =  1 x 10  +  3 x 1  =  13
```

In binary, base 2, you have two digits, 0 and 1. Each place is worth **two** times the
place to its right:

```
    1     1     0     1
    8s    4s    2s    1s   =  8 + 4 + 0 + 1  =  13
```

**`13` and `1101` are the same number.** Not similar. The same. They are two ways of
writing one quantity, the way "thirteen" and "trece" are two ways of saying it.

## Decimal to binary, by hand

Ask which powers of two add up to your number, biggest first.

Convert 13:

| Place | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|
| Does it fit in what's left? | no | yes, 5 left | yes, 1 left | no | yes, 0 left |
| Digit | | 1 | 1 | 0 | 1 |

Answer: `1101`.

## Binary to decimal, by hand

Add the place values wherever there is a 1.

`101010` has 1s in the 32s, 8s, and 2s places. 32 + 8 + 2 = **42**.

## Hexadecimal, and why it exists

Base 16. Sixteen digits, so after 9 it keeps going with letters:

| Dec | 0-9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|
| Hex | 0-9 | a | b | c | d | e | f |

**Hex exists because four binary digits are exactly one hex digit.** Always. That makes
hex a shorthand for binary that a human can actually read.

```
1101  ->  d
1111 1111  ->  ff   (which is 255)
```

That is why colours on the web are written like `#57A1EB`. It is three pairs of hex
digits, each pair one byte, each byte a number from 0 to 255.

## Checking yourself with Python

```python
print(bin(13))        # 0b1101
print(hex(13))        # 0xd
print(int("1101", 2)) # 13
print(int("d", 16))   # 13
print(f"{13:b}")      # 1101
print(f"{13:08b}")    # 00001101
```

The `0b` and `0x` prefixes are Python telling you which base it is showing you. They
are not part of the number.

**Use these to check your hand work, not to replace it.** The exam asks you to convert
by hand.

## The wrong version

Converting `1101` by adding the digits: 1 + 1 + 0 + 1 = 3.

**Wrong, and it is wrong for a reason worth naming.** Adding the digits throws away
place value, which is the entire idea. The 1 on the left is not worth one. It is worth
eight.

**Why it is tempting:** because you were taught to add digits when checking whether a
number divides by 3, and because `1101` looks like four small things rather than one
number.

---

# Part 2 · Characters are numbers (Tuesday)

## The concept

**A character is a number.** The letter `A` is not stored as a letter. It is stored as
65, and something at the other end knows to draw an A when it sees 65.

**ASCII** assigned numbers to 128 characters: the English alphabet in both cases, the
digits, punctuation, and some control codes. **Unicode** extended that to essentially
every writing system that exists, plus emoji.

```python
print(ord("A"))    # 65
print(ord("a"))    # 97
print(ord("0"))    # 48
print(ord(" "))    # 32

print(chr(65))     # A
print(chr(97))     # a
```

`ord()` gives you the number for a character. `chr()` gives you the character for a
number.

## Three things worth noticing

**The alphabet is in order.** `ord("B")` is 66 because B comes after A. That means
letters can be done arithmetic on:

```python
print(chr(ord("A") + 25))   # Z
```

**The digit `0` is 48, not 0.** The character `"0"` and the number `0` are unrelated
values. This is the Week 2 lesson again in a new place.

**Upper and lower case are exactly 32 apart.** 97 minus 65 is 32, and 32 is 2 to the
power of 5, which is one single bit. The people who designed ASCII put the cases 32
apart deliberately so a machine could switch case by flipping one bit.

## Unicode, and the error that is not your fault

```python
print(ord("é"))       # 233
print(ord("🔥"))      # 128293
```

Now try printing that emoji on a default Windows terminal:

```python
print(chr(128293))
```

```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f525' in position 0:
character maps to <undefined>
```

**Your program is correct.** Nothing you wrote is wrong. The terminal is set to an
older encoding called `cp1252` that can represent 256 characters, and the one you asked
for is not among them.

Check what yours is set to:

```python
import sys
print(sys.stdout.encoding)
```

**This is the first failure you will meet that is not in your code.** The distinction
between "my program is wrong" and "my environment cannot do what my program asked" is
one you will use for the rest of your career, and most beginners never learn to make it.

## `len()` counts characters, not bytes

```python
print(len("cafe"))   # 4
print(len("café"))   # 4
```

Both are four characters as far as Python is concerned, even though the second one
takes more space to store. Python is counting characters. How many bytes those take is
a separate question and it is beyond this course.

---

# Part 3 · Reading from a file (Wednesday)

## Why this exists

Every program so far got its data from a person typing. That does not scale past about
four values, and it means the data disappears when the program ends. Real data lives in
files.

## The concept

Three steps, always in this order.

```python
f = open("roster.txt")   # get a handle on the file
text = f.read()          # read from it
f.close()                # release it
```

`open()` does not give you the contents. It gives you a **handle**, an object that
knows how to read the file. You then ask the handle for the text.

**Closing matters.** An open file is a resource the operating system is holding for
you. Forgetting to close it works fine on a four-line program and causes real problems
later.

## Two ways to read

**`.read()` gives you the entire file as one string:**

```python
f = open("roster.txt")
whole = f.read()
f.close()
print(repr(whole[:40]))
```

```
'Ava Ruiz,ROBO-2026-114\nMarcus Delgado,BA'
```

Notice the `\n` sitting inside it. Those are the line breaks, and they are ordinary
characters in the string.

**`.readline()` gives you one line at a time:**

```python
f = open("roster.txt")
first = f.readline()
second = f.readline()
f.close()
print(repr(first))
print(repr(second))
```

```
'Ava Ruiz,ROBO-2026-114\n'
'Marcus Delgado,BAND-2027-9\n'
```

**Look at the end of each one.** `.readline()` includes the newline character. That is
why `.strip()` follows it almost everywhere you will ever see it:

```python
print(repr(first.strip()))    # 'Ava Ruiz,ROBO-2026-114'
```

## The wrong version, and the exact error

```python
f = open("missing.txt")
```

```
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'
```

Straightforward when the file genuinely is not there. Here is the version that costs
students real time: **the same error, for a file that exists.**

The filename you give `open()` is looked for relative to **where you ran the program
from**, not where the program file lives. Run the same script from a different folder
and the file it found a minute ago is now missing.

**The check:** read the path in the error message. It tells you exactly where Python
looked. Compare that to where the file actually is.

## Why the wrong version is tempting

Because you can see the file. It is right there in the editor sidebar, two inches from
the error message that says it does not exist. Everything in your visual field says the
file is present, and the one thing that matters, which folder your terminal is sitting
in, is not visible anywhere.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Base** | How many digits a number system uses. Decimal is 10, binary 2, hex 16. |
| **Binary** | Base 2. Digits 0 and 1. |
| **Hexadecimal** | Base 16. Digits 0-9 then a-f. |
| **Bit** | One binary digit. |
| **Byte** | Eight bits. Holds 256 different values, 0 to 255. |
| **Place value** | What each position in a written number is worth. |
| **`bin()` `hex()`** | Show a number in binary or hex, with a prefix. |
| **`int(text, base)`** | Read text as a number in the given base. |
| **ASCII** | The original 128-character encoding. |
| **Unicode** | The encoding covering essentially every writing system. |
| **Code point** | The number assigned to a character. |
| **`ord()` `chr()`** | Character to number, and number back to character. |
| **Encoding** | The scheme mapping characters to the bytes stored for them. |
| **`UnicodeEncodeError`** | The output destination cannot represent a character. |
| **File handle** | What `open()` gives you. Not the contents. |
| **`.read()`** | The whole file as one string. |
| **`.readline()`** | One line, including its newline character. |
| **`FileNotFoundError`** | Python looked where you pointed and found nothing. |
| **Relative path** | A filename read relative to where you ran the program. |

---

## Self-check

**1.** Convert 42 to binary by hand, showing the place values. Then convert `10110` to
decimal.

**2.** `ord("A")` is 65. Without running anything, what is `chr(ord("A") + 2)`, and why?

**3.** A student's program prints an emoji fine on their laptop and crashes on the lab
machine with `UnicodeEncodeError`. Is the program wrong? Explain in two sentences.

**4.** This prints the first line with a stray line break at the end. Why, and what is
the one-word fix?

```python
f = open("roster.txt")
line = f.readline()
f.close()
print("[" + line + "]")
```

---

### Answers

**1.** 42 in binary is `101010`.

| Place | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|
| Fits? | yes, 10 left | no | yes, 2 left | no | yes, 0 left | no |
| Digit | 1 | 0 | 1 | 0 | 1 | 0 |

`10110` is 16 + 4 + 2 = **22**.

**2.** `C`. The alphabet is stored in order, so 65 is A, 66 is B, and 67 is C. Adding 2
to the code point moves two letters along.

**3.** The program is not wrong. The lab machine's terminal is set to an encoding that
cannot represent that character, so the failure is in the output destination rather
than in the code. The fix is to change the terminal's encoding, not the program.

**4.** `.readline()` returns the line **including** the newline character at the end, so
the closing bracket gets pushed onto the next line. The fix is `.strip()`.

The brackets are doing something worth copying: they make an invisible character
visible. Same technique as `repr()` from Week 3.
