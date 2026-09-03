# Lecture Notes: Strings, Build Reach Clean
## 145060 Programming · Unit 1 · Week 3 · Tuesday through Thursday

If you missed class, you can learn these three concepts from this file alone. Type
every example. Reading string code without running it is close to worthless, because
the mistakes are invisible.

---

## Why this exists

Almost everything a program receives from a human is text. A name, a command, a
search box, a room description in your text adventure, a line from a file, a response
from an API. Numbers arrive as text and have to be converted. Everything else stays
text and has to be handled.

Three skills cover most of it. **Build** a string out of pieces. **Reach** into a
string and take a piece out. **Clean** a string somebody typed carelessly.

---

# Part 1 · Building strings (Tuesday)

## Three ways, and they are not the same

```python
first = "Ava"
last = "Ruiz"

print(first + last)          # AvaRuiz
print(first + " " + last)    # Ava Ruiz
print(first, last)           # Ava Ruiz
```

**`+` joins two strings into one new string.** Nothing is inserted between them, so
line 1 gives `AvaRuiz` with no space. If you want a space, you supply it.

**A comma hands `print` two separate values** and `print` puts a single space between
them. The output looks the same as line 2, and the mechanism is completely different.
Line 2 made one string. Line 3 made two and let `print` deal with it.

**The difference matters when you are not printing.** If you need the full name
stored in a variable, only `+` gives you that:

```python
full_name = first + " " + last     # this is one string
```

## f-strings, the third way

An f-string is a string with an `f` in front of the opening quote. Anything inside
curly braces is worked out and dropped into the text.

```python
name = "Ava"
hours = 13.5
rate = 11.5

print(f"{name} worked {hours} hours at {rate} per hour")
```

Output:

```
Ava worked 13.5 hours at 11.5 per hour
```

You can put a whole calculation inside the braces:

```python
print(f"Pay: {hours * rate}")     # Pay: 155.25
```

## The part you have been waiting for

Remember `0.9006211180124224` from the Shift Pay lab. Here is the fix.

```python
print(f"Pay: ${hours * rate:.2f}")
```

```
Pay: $155.25
```

`:.2f` means "show this as a number with exactly 2 digits after the decimal point."
The colon starts the formatting instruction, and everything after it describes how
the value should look, not what it is.

Alignment works the same way:

```python
print(f"Pay: {hours * rate:>10.2f}|")
```

```
Pay:     155.25|
```

`>10` means "right-align this in a space 10 characters wide." That is how you make
columns line up, which is Unit 5's report work starting early.

## The wrong version, and the exact error

```python
laps = 7
print("You ran " + laps + " laps")
```

```
    print("You ran " + laps + " laps")
          ~~~~~~~~~~~^~~~~~
TypeError: can only concatenate str (not "int") to str
```

`+` between a string and a number is not defined. You have seen this error before,
in Week 2. It is the same rule arriving in a new place.

**Three fixes, all correct:**

```python
print("You ran", laps, "laps")            # commas
print("You ran " + str(laps) + " laps")   # convert to text
print(f"You ran {laps} laps")             # f-string
```

The f-string is the one to reach for. It is shorter, it handles the conversion, and
it is the only one of the three that can also format.

**Why the wrong version is tempting:** `+` reads like "and." "You ran and 7 and
laps" is how the sentence sounds in your head, and English does not care about
types. Python does.

---

# Part 2 · Reaching inside (Wednesday)

## Positions start at zero

Every character in a string has a position number, and the first one is 0.

```
M  C  C  T  C  1  4  5  0  6  0
0  1  2  3  4  5  6  7  8  9  10
```

```python
code = "MCCTC145060"

print(code[0])      # M
print(code[4])      # C
print(code[-1])     # 0
print(len(code))    # 11
```

`code[-1]` counts backward from the end, so it is the last character. That is often
what you want and it saves you doing arithmetic with `len`.

**The last valid position is `len - 1`.** The string above has length 11 and its last
position is 10. There is no position 11.

## Slicing takes a range

```python
print(code[0:5])    # MCCTC
print(code[5:])     # 145060
print(code[:5])     # MCCTC
```

**The rule, and say it out loud every time: from the first number, up to but not
including the second.**

`code[0:5]` gives positions 0, 1, 2, 3, and 4. Not 5. Five characters, which is why
the count works out even though the numbers look off by one.

Leaving a number out means "from the start" or "to the end."

## The wrong version, and this one does not crash

```python
code = "ROBO-2026-114"
print("Year is:", code[5:8])
```

```
Year is: 202
```

**No error. No traceback. A year that is missing its last digit.**

Write the positions down and it is obvious:

```
R  O  B  O  -  2  0  2  6  -  1  1  4
0  1  2  3  4  5  6  7  8  9 10 11 12
```

Position 8 holds the `6`. The slice stops **before** 8, so the `6` is left out. The
fix is `code[5:9]`, which stops before position 9, and position 9 is the second dash.

**This is the third time this course has shown you the same shape.** Week 2 Thursday
it was `121212` from a forgotten conversion. Week 2 Friday it was a headcount of 2.5
people accepted silently. Today it is `202`. Learn the pattern, not the three
examples: **a program producing output is not the same as a program producing the
right output.**

## The one string error that does crash

```python
code = "MCCTC"
print(code[5])
```

```
IndexError: string index out of range
```

Position 5 does not exist in a five-character string. Its positions are 0 through 4.

Now compare that with this:

```python
print("MCCTC"[0:99])    # MCCTC, no error
```

**Indexing past the end raises. Slicing past the end does not.** Indexing asks for
one specific character and Python cannot invent it. Slicing asks for a range and
Python quietly clips the range to what exists.

That asymmetry catches people, and knowing it tells you something useful: a slice
will never crash on you, which means a slice can be wrong without telling you.

---

# Part 3 · Cleaning (Thursday)

## Methods return a copy

A method is something a string can do to itself. You call it with a dot.

```python
raw = "  ava RUIZ  "

print(repr(raw.strip()))            # 'ava RUIZ'
print(repr(raw.strip().title()))    # 'Ava Ruiz'
print(raw.upper())                  # "  AVA RUIZ  "
print(raw)                          # "  ava RUIZ  "  <- unchanged
```

**Look at the last line.** `raw` is exactly what it always was. String methods do not
change the string. They hand you back a new one. If you want to keep the result, you
have to store it:

```python
clean = raw.strip().title()
```

This is the single most common Thursday mistake: calling `.strip()` and then
wondering why the spaces are still there.

## Why `repr()` matters here

```python
print("  Ava  ".strip())          # Ava
print(repr("  Ava  ".strip()))    # 'Ava'
```

The first line proves nothing. Trailing spaces are invisible on a terminal, so you
cannot tell whether `.strip()` did anything. `repr()` shows you the quotes, so you
can see exactly where the string starts and stops. **Use it whenever whitespace is
the thing you are checking.**

## The useful ones

```python
print("  Ava Ruiz  ".strip())          # 'Ava Ruiz', ends only
print("ava ruiz".title())              # Ava Ruiz
print("Ava Ruiz".upper())              # AVA RUIZ
print("Ava Ruiz".lower())              # ava ruiz
print("Ruiz, Ava".replace(", ", " "))  # Ruiz Ava
print("MCCTC145060".startswith("MCCTC"))  # True
print("ruiz" in "Ava Ruiz".lower())    # True
```

`in` asks whether one string appears anywhere inside another. It gives back `True` or
`False`, which is a **bool**, the fourth type from Week 2. You will use `in` heavily
in Unit 2 when conditions arrive.

## `.strip()` does not do what its name suggests

A very common wrong belief:

> "`.strip()` removes all the spaces from a string."

It does not. It removes whitespace from the **two ends only**.

```python
print(repr("  Ava  Ruiz  ".strip()))    # 'Ava  Ruiz'
```

The two spaces in the middle survive. If you genuinely want every space gone,
`.replace(" ", "")` does it, and for a name that gives you `AvaRuiz`, which is
almost certainly not what you wanted.

## Where cleaning stops working

Run `.title()` on real names:

```python
print("mcdonald".title())        # Mcdonald
print("o'brien".title())         # O'Brien
print("van der berg".title())    # Van Der Berg
```

The first is wrong. The second happens to be right. The third is wrong for most
people who have that name.

**No method handles every name, and no method ever will.** Names are one of the
genuinely hard problems in software and people whose names break systems deal with it
constantly. The professional habit is not to find a better method. It is to know
where your cleaning fails and write it down, which is why every lab this week asks
you to name one input your program gets wrong.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Concatenation** | Joining strings with `+` into one new string. |
| **f-string** | A string prefixed with `f` where `{}` holds expressions to insert. |
| **Format specifier** | The part after `:` inside braces, such as `.2f` or `>10`. |
| **Index** | The position number of one character. Starts at 0. |
| **Negative index** | Counts backward from the end. `-1` is the last character. |
| **Slice** | A range of characters, from one position up to but not including another. |
| **`len()`** | How many characters are in the string. |
| **`IndexError`** | You asked for a position that does not exist. |
| **Method** | Something a value can do to itself, called with a dot. |
| **Immutable** | Cannot be changed in place. Strings are immutable. |
| **`.strip()`** | Returns a copy with whitespace removed from both ends. |
| **`.title()`** | Returns a copy with the first letter of each word capitalized. |
| **`.replace(a, b)`** | Returns a copy with every `a` swapped for `b`. |
| **`in`** | Asks whether one string appears inside another. Gives `True` or `False`. |
| **`bool`** | The type whose only values are `True` and `False`. |

---

## Self-check

**1.** Write the exact output.

```python
tag = "LOCKER-214-B"
print(tag[0:6])
print(tag[7:10])
print(tag[-1])
```

**2.** A student writes this and reports that the spaces are still there. Explain in
two sentences what they misunderstood, and write the corrected code.

```python
name = "  priya patel  "
name.strip().title()
print(name)
```

**3.** `"MCCTC"[5]` raises `IndexError`. `"MCCTC"[0:99]` returns `MCCTC` with no
error. Explain why Python treats these two differently.

**4.** Write one line that prints `Total: $42.50` given `amount = 42.5`.

---

### Answers

**1.**

```
LOCKER
214
B
```

Positions: `tag[0:6]` is 0 through 5, which is `LOCKER`. Position 6 is the dash, left
out because the slice stops before 6. `tag[7:10]` is 7, 8, 9, which is `214`.
`tag[-1]` is the last character, `B`.

If you wrote `LOCKER-` for the first one, you included position 6. Up to but not
including.

**2.** String methods return a copy and do not change the original. Line 2 built a
cleaned-up string and then threw it away, because nothing stored it. The fix:

```python
name = "  priya patel  "
clean_name = name.strip().title()
print(clean_name)      # Priya Patel
```

Assigning back to `name` also works. What does not work is calling the method and
ignoring what it hands back.

**3.** Indexing asks for one specific character. Position 5 does not exist in a
five-character string, and Python cannot return something that is not there, so it
raises. Slicing asks for a range, and Python clips the range to whatever actually
exists rather than failing. The practical consequence: **a slice will never crash on
you, so a slice can be silently wrong.**

**4.**

```python
print(f"Total: ${amount:.2f}")
```

`str(amount)` gives `42.5`, with one decimal place, which is not what money looks
like. The `.2f` is doing the real work here.
