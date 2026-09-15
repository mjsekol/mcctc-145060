# Lecture Notes: Common Vulnerabilities and Secure Coding
## 145060 Programming · Unit 7 · Week 18 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W18_VulnerabilitiesSecureCoding.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W18_VulnerabilitiesSecureCoding.pptx)

If you missed class, you can learn this concept from this file alone.

---

## Why this exists

Yesterday you checked one kind of input, player text going into a prompt. Today you meet
the named categories of vulnerability that show up across all kinds of input, and the
one habit that fixes most of them: validate before you trust, or do not do the dangerous
thing at all. These categories are on the Ohio competency list (9.3.1), and they are what
you hunt for in the security review lab.

A vulnerability is a bug an attacker can use. Not every bug is a vulnerability, and not
every vulnerability crashes. The most dangerous ones do exactly what the code says, for
an attacker instead of for you.

---

## The concept in plain language

A handful of categories cover most of what goes wrong in a program that takes input:

- **Arbitrary code execution**, usually from running input as code, like `eval`.
- **Path traversal**, using `..` to reach files outside an intended folder.
- **Secrets in code**, a key or password written into a file.
- **Verbose error leakage**, an error message that hands out internal details.
- **Missing input validation**, trusting a value without checking it.
- **Missing timeouts**, a call that can hang forever, an availability problem.

The fixes rhyme. Do not run input as code. Reject names that can climb folders. Read
secrets from the environment. Show plain errors. Check values against rules. Bound every
network call with a timeout.

---

## Worked example 1: eval is arbitrary code execution

```python
# WRONG: eval runs whatever the user typed, as code.
def calc_bad(expression):
    return eval(expression)

# RIGHT: parse it yourself, and do only arithmetic.
OPERATORS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
             "*": lambda a, b: a * b, "/": lambda a, b: a / b}

def calc_ok(expression):
    left, op, right = expression.split()
    return OPERATORS[op](float(left), float(right))

print(calc_ok("3.5 * 12"))     # 42.0
```

Output:

```
42.0
```

`calc_bad("__import__('os').getcwd()")` runs real code and leaks the working directory,
and worse inputs can read files or run programs. `calc_ok` on that same input raises a
clean `ValueError`, because the input is not three parts. The safe version does the one
job it was meant to and refuses everything else.

---

## Worked example 2: path traversal, and the one-function fix

```python
import os
NOTES_FOLDER = "data/notes"

# WRONG: a name with .. climbs out of the folder.
def read_bad(name):
    with open(os.path.join(NOTES_FOLDER, name)) as note_file:
        return note_file.read()

# RIGHT: reject any name that is not a plain file name.
SAFE = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")

def safe_name(name):
    if name == "" or len(name) > 40:
        raise ValueError("bad name")
    for character in name:
        if character not in SAFE:
            raise ValueError("bad name")
    return name

def read_ok(name):
    with open(os.path.join(NOTES_FOLDER, safe_name(name) + ".txt")) as note_file:
        return note_file.read()
```

`read_bad("../../settings.py")` reads a file of secrets, no crash. `read_ok` on the same
name raises `ValueError` at `safe_name`, because a dot and a slash are not on the
allowlist. One small function, run before every path is built, closes the whole category.

---

## Worked example 3: a plain error instead of a leak

```python
import traceback

# WRONG: the error message hands out internal details.
def run_bad(action):
    try:
        action()
    except Exception as error:
        print(f"Error: {error}")
        traceback.print_exc()
        print("Config:", {"API_KEY": "NOT-A-REAL-KEY-abc", "DB": "internal-db-01"})

# RIGHT: one plain line for the user; details only in a private log.
def run_ok(action, debug=False):
    try:
        action()
    except Exception:
        print("Something went wrong. Please tell an officer what you were doing.")
        if debug:
            traceback.print_exc()

run_ok(lambda: 1 / 0)
```

Output:

```
Something went wrong. Please tell an officer what you were doing.
```

The bad version prints a traceback and a dump of config, including a key, to anyone who
triggers an error. That is a gift to an attacker: file paths, variable names, secrets.
The good version says one calm sentence, and shows the traceback only when a person has
turned debug on for themselves.

---

## The wrong version, and why it is the whole week

Every one of these ships in the security review lab, and every one runs without crashing.
The `eval` calc works for `2 + 2`. The path traversal reads a real file. The verbose
error prints helpful details. That is what makes them dangerous: they look like features.
An attacker uses them exactly as written.

### Write this down

> A vulnerability is a bug an attacker can use, and most of them do not crash.

The fix is almost never a bigger version of the dangerous thing. It is to stop doing the
dangerous thing, or to check the input first.

---

## Why these mistakes are tempting

Each one is the shortest path to a working feature. `eval` is the fastest calculator.
Joining a name to a folder is the fastest file lookup. Dumping the config on an error is
the fastest way to debug. Skipping the timeout is one less thing to type. The shortcut
works on the inputs you tried, so it feels done. The cost is a door you did not know you
left open, and the door only matters when someone looks for it.

The habit that prevents it: for every input, ask "what is the worst thing someone could
put here," and check for it before you use the value. Reach for the specific safe tool,
not the general dangerous one.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Vulnerability** | A bug an attacker can use to do something they should not. |
| **Arbitrary code execution** | Running attacker-chosen code, often via `eval`. |
| **Path traversal** | Using `..` to reach files outside an intended folder. |
| **Injection** | Slipping commands into input that is treated as data. |
| **Verbose error leakage** | An error message that reveals internal details. |
| **Input validation** | Checking input against rules before using it. |
| **Allowlist** | Accepting only what you decided is safe, rejecting the rest. |
| **Hardening** | Reducing what a program exposes, so there is less to attack. |

---

## Self-check

**Question 1.** Why is `eval` on user input a vulnerability and not only a style choice?
Give one thing an attacker could do with it.

**Question 2.** A program reads files by joining a user-supplied name to a folder. Name
the vulnerability and give the one-function fix.

**Question 3.** Why is a detailed error message with a stack trace and config values a
security problem, not a helpful feature, when a real user hits it?

---

### Answers

**1.** Because `eval` runs the input as Python code, so a user controls what the program
runs, not only what data it uses. An attacker could read files, delete files, or run
other programs, depending on what the input says. The fix is to parse the input and do
only the specific operation you meant.

**2.** Path traversal. The fix is a `safe_name` function that rejects any name containing
a dot, a slash, or other path characters, run before the name is joined to the folder, so
`..` can never climb out.

**3.** Because the details help an attacker more than the user. A stack trace reveals file
paths, function names, and internal structure, and a config dump can reveal keys and
server names. A real user cannot act on any of that, so it belongs in a private log, not
on the screen. Show the user one plain sentence.
