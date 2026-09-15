# Decide the Answer Before You Run It
---
## Slide 1: You played version one forty times
- You tested v1 by playing it
- Then you changed something and played it again
- This week every change can break something else
- A feature that worked, then stopped, is a regression
- You will skip replaying on the day it matters
Speaker notes: How did you know your text adventure worked? You played it, changed something, and played it again. This week you are rebuilding it out of functions, and every change can break something that used to work, somewhere you are not looking. That is called a regression. Playing the whole game after every change does not scale. A test checks one thing for you, in one command, every time.
Image: A tally of forty playthrough marks on a whiteboard beside a single terminal command, flat navy and accent blue.
---
## Slide 2: A test case has four parts
- ID: TC-3
- Input: order_total(35)
- Expected: 35, worked out from the rule by hand
- Why: exactly the free shipping amount
- Expected never comes from running your program
Speaker notes: A test case is an ID, an input, the output you expect, and the reason the case exists. The rule for the spirit store is that orders of thirty five dollars or more ship free. So order total of thirty five should be thirty five. Here is the one rule that makes a test worth anything. The expected value comes from the requirement, worked out by hand, before you run the code. If you copy it from the program, the test agrees with the program whether the program is right or not.
Image: A single index card labeled with ID, input, expected, and why fields.
---
## Slide 3: Which cases to choose
- Normal: a value in the middle
- Boundary: the exact edge, and one step each side
- Invalid: input the function must refuse
- A bug you fixed: the reproduction from your log
- Middle values alone pass almost any code
Speaker notes: You met this in Unit 2 when you wrote boundary tests for an eligibility rule. Normal cases catch code that is completely wrong. Boundary cases catch greater than where greater than or equal belongs, which is where bugs actually live. Invalid cases catch missing validation. And the reproduction from your troubleshooting log becomes a test, so the same bug cannot come back quietly.
Image: A number line with a marked boundary at 35 and test points at 34, 35, and 36.
---
## Slide 4: A check function and a test file
```python
import spirit_store


def check(label, actual, expected):
    """Print PASS or FAIL for one check. Return 1 if it failed, 0 if it passed."""
    if actual == expected:
        print(f"PASS  {label}")
        return 0
    print(f"FAIL  {label}")
    print(f"        expected: {repr(expected)}")
    print(f"        actual:   {repr(actual)}")
    return 1


# TC-1, TC-5, and TC-6 are in the full file in the lecture notes.
failures = 0
failures = failures + check("TC-2 one dollar below free shipping", spirit_store.order_total(34), 40)
failures = failures + check("TC-3 exactly the free shipping amount", spirit_store.order_total(35), 35)
failures = failures + check("TC-4 one dollar above free shipping", spirit_store.order_total(36), 36)
print(f"{failures} failed")
```
Speaker notes: Import spirit store lets this file call the store's functions. The check function compares actual to expected, prints pass or fail with the label, shows both values when it fails, and returns one for a failure. The caller adds them up, the same pass it in, get it back, store it pattern as moves equals take step of moves. Every label starts with the test case ID, so a failure takes you straight back to the table.
Image: None. This slide is code.
---
## Slide 5: All six cases run: one boundary catches the bug
```
PASS  TC-1 normal order pays shipping
PASS  TC-2 one dollar below free shipping
FAIL  TC-3 exactly the free shipping amount
        expected: 35
        actual:   41
PASS  TC-4 one dollar above free shipping
PASS  TC-5 zero is refused
PASS  TC-6 negative is refused

1 failed
```
Speaker notes: The slide before showed three of the cases. This is the full six-case test file from the lecture notes, run against a store where somebody wrote greater than instead of greater than or equal. Five of six pass. Only the boundary, exactly thirty five, catches it, and the failure shows the expected value and the actual value side by side. A customer ordering exactly thirty five dollars would have paid six dollars of shipping they were promised they would not pay.
Image: None. This slide is code.
---
## Slide 6: Two pieces of plumbing
- import spirit_store runs that file and shares its functions
- Call them as spirit_store.order_total(20)
- if __name__ == "__main__": goes above main()
- Run directly: main runs. Imported: it does not
- Forget it, and importing the store starts the store
Speaker notes: Two small pieces of plumbing. Import loads your other file so its functions can be reused, and that makes your own file a small library. And the if name equals main line protects main. When you run a file directly, that condition is True. When a test imports it, it is False. Forget that line and your test file stops at the store's input prompt before a single test runs.
Image: Two files side by side with an arrow labeled import from the test file to the program file.
---
## Slide 7: Testing the whole game with a script
```
cmd /c "python adventure.py < test-scripts\win.txt > test-scripts\win_v1_output.txt"
cmd /c "python adventure.py < test-scripts\win.txt > win_v2_output.txt"
cmd /c "fc test-scripts\win_v1_output.txt win_v2_output.txt"
```
```
Comparing files TEST-SCRIPTS\win_v1_output.txt and WIN_V2_OUTPUT.TXT
FC: no differences encountered
```
Speaker notes: Your game loop reads input and prints, so for the game as a whole, the test case is a script, and the expected output is what a version you trust printed. Save version one's output before you change anything. After the refactor, run the same script into a second file and compare them with fc. No differences means no regression. Any difference you did not mean is one.
Image: None. This slide is code.
---
## Slide 8: Watch this: I copy the expected value
```python
failures = 0
failures = failures + check("normal order", spirit_store.order_total(20), 26)
failures = failures + check("big order", spirit_store.order_total(50), 50)
failures = failures + check("exactly 35", spirit_store.order_total(35), 41)
print(f"{failures} failed")
```
Speaker notes: I am testing the store with the greater than bug. For the boundary case I am not sure what to expect, so I run it, it says forty one, and I type forty one. Before I run the tests, predict how many fail, and whether that is good news.
Image: None. This slide is code.
---
## Slide 9: The wrong way: every test passes
```
PASS  normal order
PASS  big order
PASS  exactly 35
0 failed
```
Speaker notes: Everything passes, and the bug is still there. Worse, the suite now defends the bug. When somebody fixes the store correctly, this test fails and tells them to put the bug back. And the first two tests are middle values that pass the broken code and the correct code equally. All green feels like done. A suite that has never failed has never proven it can.
Image: None. This slide is code.
---
## Slide 10: assert, the shortest test
```python
import spirit_store

assert spirit_store.order_total(20) == 26
assert spirit_store.order_total(35) == 35
assert spirit_store.order_total(36) == 36
print("All asserts passed")
```
```
Traceback (most recent call last):
  File "...", line 4, in <module>
    assert spirit_store.order_total(35) == 35
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
Speaker notes: Assert is the shortest test Python has. If its condition is False, it crashes with AssertionError. Here it caught the boundary bug on line four. Two weaknesses. It stops at the first failure, so you never learn about line five, and it does not tell you the actual value. That is why your test files use check. You will see a module called unittest in real projects, including the text adventure reference. It uses classes, so you will read it in Unit 7.
Image: None. This slide is code.
---
## Slide 11: What you are about to build
- Build 1: the GP1 exam
- Build 2, first: a test case table for your v2
- At least eight cases: normal, boundary, invalid, a fixed bug
- test_adventure.py with check. Run it
- Compare every v1 script with fc. v2 due Friday 8:30
Speaker notes: Build one today is the grading period exam. After it, fill in a test case table for your version two, with expected values worked out before you run anything. At least eight cases, including a boundary, an invalid input, and the reproduction of a bug from your troubleshooting log. Then write test adventure dot py with check and run it, and compare every version one script with fc. Version two is due at eight thirty tomorrow morning.
Image: A test case table on paper beside a terminal showing PASS lines and 0 failed.
---
