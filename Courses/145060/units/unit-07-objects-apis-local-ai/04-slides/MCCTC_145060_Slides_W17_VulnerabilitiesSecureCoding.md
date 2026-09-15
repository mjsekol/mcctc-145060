# Bugs an Attacker Can Use
---
## Slide 1: A calculator that runs anything you type
- A quick calc command uses eval
- Type 2 plus 2, get 4
- Type something worse, and it runs
- It works, and it is dangerous
Speaker notes: Here is a calculator someone built with eval. Type 2 plus 2 and get 4. It works perfectly, they say. But eval runs whatever you type as code, so a worse input runs too. It works and it is dangerous at the same time, and that combination is what makes it a vulnerability.
Image: A calculator input box with "2 + 2" and a second one with "__import__('os')..." beside it.
---
## Slide 2: A vulnerability is a bug an attacker can use
- Not every bug is a vulnerability
- Most vulnerabilities do not crash
- They do exactly what the code says
- For an attacker instead of for you
Speaker notes: A vulnerability is a bug an attacker can use to do something they should not. Not every bug is one. And most do not crash. They do exactly what the code says, for an attacker instead of for you. That is why they hide. They look like working features.
Image: A bug icon and a subset of it labeled "an attacker can use this".
---
## Slide 3: eval is arbitrary code execution
```python
def calc_bad(expression):
    return eval(expression)       # runs the input as code

OPERATORS = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
             "*": lambda a, b: a * b, "/": lambda a, b: a / b}
def calc_ok(expression):
    left, op, right = expression.split()
    return OPERATORS[op](float(left), float(right))
```
Speaker notes: calc_bad runs the input as Python. Someone can read files or run programs through it. calc_ok parses the input itself and does only the four operations. Same feature, one is a door for an attacker and one is not. The fix is never a bigger eval. It is a specific safe parser.
Image: None. This slide is code.
---
## Slide 4: Path traversal, and the one-function fix
```python
SAFE = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
def safe_name(name):
    if name == "" or len(name) > 40:
        raise ValueError("bad name")
    for character in name:
        if character not in SAFE:
            raise ValueError("bad name")
    return name
```
Speaker notes: A user asks for a note by name, and the code joins the name to a folder. A name of dot dot slash dot dot slash settings dot py climbs out and reads a file of secrets. No crash. The fix is one function, safe_name, that rejects any dot or slash, run before every path is built. It closes the whole category.
Image: None. This slide is code.
---
## Slide 5: The category names
- Arbitrary code execution, from eval
- Path traversal, from dot dot
- Secrets in code, a key in a file
- Missing timeouts, a call that hangs
Speaker notes: Learn the category names. Arbitrary code execution, usually from running input as code. Path traversal, using dot dot to climb folders. Secrets in code, a key written in a file. Verbose error leakage, and missing input validation, and missing timeouts. These are on the Ohio competency list you are tested on.
Image: A list of five vulnerability categories, each with a tiny icon.
---
## Slide 6: The trap, a helpful error message
```python
except Exception as error:
    print(f"Error: {error}")
    traceback.print_exc()
    print("Config:", {"API_KEY": "NOT-A-REAL-KEY-abc", "DB": "internal-db-01"})
```
Speaker notes: This looks helpful. When something breaks, it prints the error, the full traceback, and the config. Predict who this helps most. A real user cannot act on any of it. Watch what an attacker gets from an error message like this.
Image: None. This slide is code.
---
## Slide 7: That is a gift to an attacker
- File paths, variable names, secrets
- A user cannot use any of it
- An attacker uses all of it
- Show one plain sentence instead
Speaker notes: A stack trace hands out file paths, function names, and internal structure. A config dump hands out keys and server names. A real user cannot use any of that. An attacker uses all of it. Show the user one calm sentence, and keep the details in a private log only you can read.
Image: An attacker reading a detailed error, a user shrugging at it.
---
## Slide 8: The fixes rhyme
- Do not run input as code
- Reject names that can climb folders
- Read secrets from the environment
- Bound every call with a timeout
Speaker notes: Notice the fixes rhyme. Do not run input as code. Reject names that can climb folders. Read secrets from the environment, never a file. Show plain errors. Check values before you use them. Bound every network call with a timeout. One habit underneath all of it, validate before you trust.
Image: A short list of fixes, each paired with its vulnerability.
---
## Slide 9: Why the shortcuts are tempting
- Each is the shortest path to working
- eval is the fastest calculator
- The shortcut works on inputs you tried
- The cost is a door you did not see
Speaker notes: Each mistake is the shortest path to a working feature. eval is the fastest calculator. Dumping config is the fastest debugging. The shortcut works on the inputs you tried, so it feels done. The cost is a door you left open, and the door only matters when someone looks for it. Assume someone will.
Image: A short path labeled "works now" leading to an open door labeled "later".
---
## Slide 10: What you are about to build
- Find the rest of the planted defects
- Secrets, verbose errors, missing timeout, traversal
- Fix at least four across four categories
- Rerun and confirm each fix holds
Speaker notes: Build one finds the remaining planted vulnerabilities in the Study Hall lab and reproduces each. Build two fixes at least four across four categories and reruns the app to confirm each fix holds and nothing else broke. Finding and mapping is the graded skill. Fixing four proves you can act on it.
Image: The review template mostly filled, four fixes marked verified, navy and accent blue.
