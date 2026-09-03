# Lecture Notes: How a Program Runs
## 145060 Programming · Unit 0 · Week 1 · Tuesday

If you missed class, you can learn this concept from this file alone. Read it with
a terminal open and type every example. Reading code you did not type is close to
worthless at this stage.

---

## Why this exists

You have used software your whole life without ever seeing where it lives. That
gap is the reason beginners get stuck on things that have nothing to do with
programming: they cannot tell the difference between writing instructions, storing
instructions, and carrying out instructions. Those are three separate events, and
until you can name which one is happening, every error message looks the same.

This is the concept that makes the rest of the semester possible. It is not
difficult. It is unfamiliar, which feels the same from the inside.

---

## The concept in plain language

Three separate things are involved every time you run a program.

**1. The file.** A file called `status_card.py` is a document. It is text on a
disk. It has no more power to do anything than a note on your fridge does. You can
open it, read it, print it out, email it. It sits there.

**2. The interpreter.** There is a program already installed on your machine called
`python`. Its whole job is to read a document like that one and carry out what it
says, one line at a time, starting at the top and moving down. It is a reader. It
does not write anything and it has no idea what your file is for.

**3. The terminal.** The terminal is where you hand one to the other. When you type
`python status_card.py`, you are saying: run the program called `python`, and give
it this document to read.

A recipe is not a cook. You wrote the recipe. `python` is the cook. The terminal is
you handing the recipe over.

**The order matters, and it is always the same order.** Save the file. Then run it.
If you change the file and do not save, the version on the disk is the old one, and
the old one is what `python` reads. This causes more Week 1 confusion than any
other single thing.

---

## Worked example 1: the file runs top to bottom

Type this into a file called `status_card.py`.

```python
# status_card.py
# Prints a short status card to the terminal.

print("MCCTC Programming 145060")
print("Name: Ava Ruiz")
print("Day 1 goal: run one file I wrote myself")
print()
print("Battery on my phone right now: 41 percent")
```

Save it. Then in the terminal, in the same folder:

```
python status_card.py
```

Output:

```
MCCTC Programming 145060
Name: Ava Ruiz
Day 1 goal: run one file I wrote myself

Battery on my phone right now: 41 percent
```

Three things to notice, because none of them are stated in the code.

**The lines came out in file order.** Nothing in the file asked for that order.
Top to bottom is the only order there is.

**The blank line came from `print()` with nothing inside it.** It printed nothing,
and then ended the line, which leaves an empty line behind. There are five `print`
lines in the file and five lines of output, one of them empty.

**The quotes are not in the output.** The quotes tell Python where your text starts
and stops. They are punctuation for the interpreter. They are not part of what you
said.

**The first two lines starting with `#` produced nothing.** Those are comments.
Python reads them and moves on. They are written for the next person to read the
file, which is usually you in three weeks.

---

## Worked example 2: quotes inside quotes

You will need a quote character inside your text eventually. This is how.

```python
print("It's 8:00 and the bus is late")
print('The sign said "no food in the lab"')
```

Output:

```
It's 8:00 and the bus is late
The sign said "no food in the lab"
```

The rule: **the outer quotes decide where the text starts and stops, and Python
stops at the first matching one it finds.** Line 1 wraps in double quotes, so the
apostrophe in `It's` passes through as ordinary text. Line 2 wraps in single quotes,
so the double quotes pass through.

If you wrap in the same kind of quote that appears inside your text, Python stops
early and the rest of the line stops being text. That is the wrong version below.

---

## Worked example 3: one print, two lines

`\n` is one character that means "start a new line." You write it with two
keystrokes, backslash and n, but it is a single character to Python.

```python
print("Monday\nTuesday")
print("Wednesday")
```

Output:

```
Monday
Tuesday
Wednesday
```

Three lines of output from two `print` calls. This is the first time in this course
that the number of `print` calls and the number of output lines are different
numbers. Do not assume they match. Count what comes out.

---

## The wrong version, and the exact error

Here is the mistake nearly everyone makes in the first week. The closing quote on
line 2 is missing.

```python
print("MCCTC Programming 145060")
print("Name: Ava Ruiz)
print("done")
```

Run it, and Python produces this:

```
  File "C:\...\status_card.py", line 2
    print("Name: Ava Ruiz)
          ^
SyntaxError: unterminated string literal (detected at line 2)
```

Read that message the way you will read every message this year, in this order:

1. **What file.** `status_card.py`. On a project with forty files this is the first
   thing you need.
2. **What line.** Line 2.
3. **What is the caret under.** The opening quote of the text that never ended.
4. **What kind of error.** `SyntaxError`, which means Python could not understand
   the file well enough to start running it.

**Nothing printed. Not even line 1.** That is the tell for a `SyntaxError`. Python
reads the entire file before running any of it, and if the file does not make sense
as Python, it never starts. Compare that to this:

```python
print("Checking inventory")
Print("You have 3 items")
```

Output:

```
Checking inventory
Traceback (most recent call last):
  File "...", line 2, in <module>
    Print("You have 3 items")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Here line 1 did print.** This file made sense as Python, so it started running,
got line 1 done, and then hit a problem on line 2. The capital `P` in `Print` is a
different name than `print`, and nothing on the machine has that name.

Learn to tell these two apart:

| Error type | When Python finds it | Did anything print first |
|---|---|---|
| `SyntaxError` | Before running, while reading the file | No |
| `NameError`, and most others | While running, at that line | Yes, everything above it |

That table is a debugging shortcut. If you got some output before the crash, the
problem is at or after the last line you saw.

---

## Why the wrong version is tempting

Nobody types a missing quote on purpose. It is tempting for a different reason:
**when you read your own code, you read what you meant.** Your eye supplies the
closing quote because your brain put it there. This is the same reason you cannot
proofread your own essay well.

The specific defense is not "be more careful." It is to stop reading and start
looking at the caret. The caret is not guessing. It is pointing at a character
position in a file. Trust it over your reading of your own work.

The second temptation is believing the error is on the line Python names. Sometimes
it is not. In the unterminated-quote example, line 3 also stopped working, because
Python kept reading forward looking for a closing quote and swallowed line 3 into
the text. Python reports where it *noticed*, which is often one or two lines below
where you erred. Read the named line, then read upward.

---

## Vocabulary

| Term | What it means |
|---|---|
| **File** | A document stored on the disk. Yours end in `.py`. |
| **Interpreter** | The program named `python` that reads your file and carries it out. |
| **Terminal** | The text window where you type commands to run programs. |
| **Run** / **execute** | To hand a file to the interpreter and have it carried out. |
| **Statement** | One instruction. In this week's code, one line. |
| **String** | A piece of text, written between quote marks. |
| **String literal** | The text exactly as you typed it between the quotes. |
| **Comment** | A line starting with `#`. Python reads it and ignores it. |
| **`print`** | The instruction that sends text to the terminal. |
| **Argument** | Something you put inside the parentheses for `print` to use. |
| **Escape sequence** | A backslash plus a letter that means one special character, like `\n` for a new line. |
| **Syntax** | The grammar rules of the language. |
| **`SyntaxError`** | Python could not understand the file, so it never ran. |
| **`NameError`** | Python was running and reached a name that does not exist. |
| **Traceback** | The report Python prints when a running program fails. |
| **Case sensitive** | `Print` and `print` are different names. Python is case sensitive. |

---

## Self-check

Answer these before you look. Write your answers down. Looking at the answer and
thinking "yes, that is what I would have said" is not the same as knowing it.

**Question 1.** Write the exact output of this file, including any blank lines.

```python
print("Room 1")
print()
print("Room 2", "Room 3")
```

**Question 2.** Two students each have one broken program. Student A's program
printed three lines and then showed a traceback. Student B's program printed
nothing at all before its error. Without seeing either file, what can you say about
where each error is and what kind it probably is.

**Question 3.** Write a program that prints exactly this, with the double quotes
appearing in the output.

```
Coach said "practice is cancelled"
The field is closed
```

---

### Answers

**1.** Three lines. The second is empty.

```
Room 1

Room 2 Room 3
```

Two things nobody typed appear in that output. The blank line came from `print()`.
The space between `Room 2` and `Room 3` came from `print` itself, which puts a
single space between values when you give it more than one. If you wrote
`Room 2Room 3`, that is the misconception to fix now rather than in Unit 1.

**2.** Student A's program started running, so the file was valid Python. The error
is at or after the fourth line, and it is a running-time error such as a
`NameError`. Student B's program never started, so it is almost certainly a
`SyntaxError`, and the error can be anywhere in the file, including line 1.

**3.**

```python
print('Coach said "practice is cancelled"')
print("The field is closed")
```

Wrapping line 1 in single quotes lets the double quotes through as ordinary text.
There is a second correct answer using a backslash before each inner quote, and
either one is right. Wrapping line 1 in double quotes is the wrong answer, because
Python would stop the text at the quote before the word `practice`.
