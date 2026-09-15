# Lecture Notes: Recursion, and When It Is the Wrong Tool
## 145060 Programming · Unit 3 · Week 8, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W08_Recursion.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W08_Recursion.pptx)

If you missed class, you can learn this concept from this file alone. **This file has two parts.**
Part 1 is today, on paper, with no Python to type. Part 2 is Python code you will run **after
Thursday of Week 8**, once you have functions and return values. The syllabus places recursion in
Unit 3, and recursion in Python needs functions, which arrive tomorrow. So today you learn how it works
and when to use it, and Thursday you get to watch it run.

---

# Part 1 · Today, on paper

## Why this exists

Some problems contain a smaller copy of themselves.

A folder on your computer holds files and other folders. Those folders hold files and more folders.
How big is the top folder? It is the size of its files plus the size of each folder inside it, and each
of those is **the same question again, one level down.** You do not know how deep it goes until you look.

A comment on a video has replies. Replies have replies. How many comments are in the whole thread? Same
shape.

**Recursion** solves a problem by solving a smaller copy of the same problem, and repeating that until the
copy is small enough to answer directly. It is the other half of outcome 5.3.8, **nested structures and
recursion**, and the syllabus asks for two things: that you can use it, and that you can **explain when it
is and is not the right tool.** The second part matters more, and it has a direct answer for your text
adventure.

---

## The concept in plain language

You are fifth in the lunch line and you want to know how many people are ahead of you. You cannot see the
front. So you tap the person ahead of you and ask them the same question: "how many people are ahead of
**you**?" They do not know either, so they ask the person ahead of them. That keeps happening until the
question reaches the person at the very front, who says "nobody. Zero."

Then the answers travel back. The second person hears "zero" and says "one." The third hears "one" and says
"two." You hear "three" from the person ahead of you, add one, and know the answer: four.

Every recursive process has exactly two parts:

| Part | What it is | In the lunch line |
|---|---|---|
| **Base case** | A version of the problem small enough to answer directly, with no further asking | The person at the front says zero |
| **Recursive case** | Answer by asking a **smaller** version of the same question, then using its answer | Ask the person ahead, then add one |

**The recursive case must move toward the base case.** Each question goes to somebody closer to the front.
If it ever went to somebody further back, it would never end.

As pseudocode, the same way you wrote your game model:

```
TO FIND people_ahead(position)
    IF position is 1
        ANSWER 0
    OTHERWISE
        ASK people_ahead(position - 1)
        ANSWER that answer plus 1
```

---

## The trace table: how the answers come back

Recursion confuses people because the work happens in two directions. The questions go **down** to the base
case. The answers come back **up**. A trace table shows both.

Trace `people_ahead(5)`:

| Step | Who is working | Position | Base case? | What happens |
|---|---|---|---|---|
| 1 | You | 5 | No | Ask `people_ahead(4)` and **wait** |
| 2 | Person 4 | 4 | No | Ask `people_ahead(3)` and **wait** |
| 3 | Person 3 | 3 | No | Ask `people_ahead(2)` and **wait** |
| 4 | Person 2 | 2 | No | Ask `people_ahead(1)` and **wait** |
| 5 | Person 1 | 1 | **Yes** | Answer **0** |
| 6 | Person 2 | 2 | | Heard 0, answer 0 + 1 = **1** |
| 7 | Person 3 | 3 | | Heard 1, answer 1 + 1 = **2** |
| 8 | Person 4 | 4 | | Heard 2, answer 2 + 1 = **3** |
| 9 | You | 5 | | Heard 3, answer 3 + 1 = **4** |

**Look at steps 1 through 4.** Four people are each in the middle of their own question, **waiting**. Nobody has
finished. They are stacked up, each one paused until the person ahead answers. The computer does exactly this: it
keeps a stack of paused tasks, one for each question still waiting for an answer, and it has to remember every one
of them until the base case is reached.

That stack is the key to the whole lesson, including when recursion is the wrong tool.

---

## When recursion is the right tool

Reach for recursion when **the data is nested inside itself to a depth you do not know in advance.**

| Problem | Why it fits |
|---|---|
| The total size of a folder that contains folders | Each folder is the same problem, one level down, to unknown depth |
| Counting every reply in a comment thread | Each reply can have its own replies |
| Working out who plays whom in a tournament bracket | Each half of a bracket is a smaller bracket |
| Finding every room reachable from a starting room in a map | Each room leads to more rooms |

A loop handles "the next item in a line." Recursion handles "the items inside this item." When the problem has that
inside-of-inside shape, the recursive version is often shorter and much closer to how you would describe the problem
out loud.

## When recursion is the wrong tool

**Your game loop.** This is the example to remember.

A student who learns recursion this week will be tempted to write the game as "take a turn, then take the next turn
by asking the same function again." Look at what the trace table says would happen. Every turn would be a paused task
waiting for the next turn to finish. Turn 1 waits for turn 2, which waits for turn 3. Nothing finishes until the game
ends. A game of 1,500 turns is a stack of 1,500 paused tasks.

Python refuses to stack that high. **By default it allows about 1,000 paused calls, then stops the program with an error.**
You will see that exact error in Part 2. A player who explores for long enough crashes the game by playing it.

A `while` loop has no stack. Turn 5,000 costs exactly what turn 1 cost.

| Situation | Right tool | Why |
|---|---|---|
| Repeat until the player quits | `while` loop | Unknown length, no nesting, no stack to fill |
| Do something 7 times | `for` loop | Known count, no nesting |
| Walk every character or every line | `for` or `while` loop | A flat sequence, nothing inside anything |
| Process data nested to unknown depth | Recursion | The problem really is a smaller copy of itself |

**The honest summary.** Anything recursion can do, a loop can also do, sometimes with a lot more bookkeeping. Anything a
loop does cleanly, recursion does worse. Professional programmers use recursion for nested data and use loops for
everything else, and they argue about the borderline cases. Know the two extremes cold.

---

## The wrong version: a recursion with no base case

Take the base case out of the lunch line:

```
TO FIND people_ahead(position)
    ASK people_ahead(position - 1)
    ANSWER that answer plus 1
```

Trace it:

| Step | Position | Base case? | What happens |
|---|---|---|---|
| 1 | 5 | none exists | Ask `people_ahead(4)` and wait |
| 2 | 4 | none exists | Ask `people_ahead(3)` and wait |
| 3 | 3 | none exists | Ask `people_ahead(2)` and wait |
| 4 | 2 | none exists | Ask `people_ahead(1)` and wait |
| 5 | 1 | none exists | Ask `people_ahead(0)` and wait |
| 6 | 0 | none exists | Ask `people_ahead(-1)` and wait |
| ... | ... | ... | the questions go past the front of the line and never stop |

Nobody ever answers, so nobody can finish, and the stack of paused tasks grows until Python stops it. Here is the real
output of that mistake as Python code, a countdown with no base case. You will run it yourself in Part 2.
It prints 998 lines of countdown, from 3 all the way down to -994, and then ends with:

```
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```

**This one crashes, which is the good news.** Compare it with a `while` loop whose condition never becomes False, which runs
forever and never tells you. Python puts a limit on recursion precisely so that this mistake stops loudly.

---

## Why recursion without a base case, or recursion for a loop, is tempting

**It reads beautifully.** "Take a turn, then take the next turn" sounds like a perfect description of a game. It is a perfect
description. It is a terrible program.

**Short tests pass.** A game loop written as recursion works fine for the 20 moves you test it with. It crashes on the player
who explores for an hour.

**The base case feels obvious, so it gets left out.** You know the person at the front says zero. The computer does not, unless
you write it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Recursion** | Solving a problem by solving a smaller copy of the same problem. |
| **Base case** | The smallest version of the problem, answered directly with no further recursion. |
| **Recursive case** | The part that asks a smaller version of the question and uses its answer. |
| **Call stack** | The stack of paused tasks, each waiting for a smaller question to be answered. |
| **Recursion depth** | How many paused tasks are stacked up at once. |
| **`RecursionError`** | Python's error when the recursion depth passes its limit, about 1,000 by default. |
| **Trace table** | A table recording each step, the values at that step, and what happens next. |
| **Outcome 5.3.8** | The WebXam competency for nested structures and recursion. |

---

## Self-check, Part 1

**Question 1.** Here is a recursive process in pseudocode. Build its trace table for `stairs(3)` and give the final answer.

```
TO FIND stairs(n)
    IF n is 0
        ANSWER 0
    OTHERWISE
        ASK stairs(n - 1)
        ANSWER that answer plus n
```

**Question 2.** For each task, say **loop** or **recursion** and give the reason in one sentence.

- Keep a chat bot answering until the user types `bye`
- Count every file inside a folder, including folders inside folders
- Print a countdown from 10 to 1

**Question 3.** A classmate says: "Recursion without a base case is the same thing as an infinite `while` loop." Say what is right about that
and what is wrong about it.

---

### Answers

**1.**

| Step | n | Base case? | What happens |
|---|---|---|---|
| 1 | 3 | No | Ask `stairs(2)`, wait |
| 2 | 2 | No | Ask `stairs(1)`, wait |
| 3 | 1 | No | Ask `stairs(0)`, wait |
| 4 | 0 | **Yes** | Answer 0 |
| 5 | 1 | | Heard 0, answer 0 + 1 = 1 |
| 6 | 2 | | Heard 1, answer 1 + 2 = 3 |
| 7 | 3 | | Heard 3, answer 3 + 3 = **6** |

The final answer is **6**, which is 3 + 2 + 1. Full credit needs the questions going down, the base case, and the answers
coming back up in reverse order.

**2.**

| Task | Tool | Reason |
|---|---|---|
| Chat bot until `bye` | Loop | It runs an unknown number of turns with no nesting, and recursion would crash a long conversation. |
| Every file in nested folders | Recursion | Each folder is the same problem one level down, to a depth you cannot know in advance. |
| Countdown from 10 to 1 | Loop | A known count in a flat sequence, which is exactly what `for` and `range` do. |

**3.** Right: in both cases nothing ever reaches a stopping point, so the work never finishes on its own. Wrong: the `while`
loop repeats in place and can run forever without using more memory, and it gives no error. Recursion stacks up a new paused task
every time, so it hits Python's limit and stops with `RecursionError`. One fails silently forever. The other fails loudly within a
fraction of a second.

---

# Part 2 · After Thursday of Week 8: run these

**Do not start this part before Thursday's lesson on return values.** Every example uses `def`, from Wednesday, and two use `return`,
from Thursday. Type each one and compare with the output shown.

## Example A: a countdown that calls itself

```python
# Recursion: a function that solves a smaller copy of its own problem.
def count_down(seconds):
    if seconds == 0:            # base case: small enough to answer directly
        print("Liftoff")
    else:
        print(seconds)
        count_down(seconds - 1)  # recursive case: the same problem, one smaller

count_down(3)
```

```
3
2
1
Liftoff
```

## Example B: the lunch line, as code

```python
# How many people are ahead of you in the lunch line?
# Each person asks the person in front, adds one, and passes the answer back.
def people_ahead(position):
    if position == 1:
        return 0                          # the first person has nobody ahead
    return 1 + people_ahead(position - 1)

print(people_ahead(5))
```

```
4
```

Compare every line with the pseudocode and the trace table from Part 1. `return 1 + people_ahead(position - 1)` is "ask the
person ahead, then add one."

## Example C: the missing base case

```python
# No base case. Every call makes another call, forever.
def count_down(seconds):
    print(seconds)
    count_down(seconds - 1)

count_down(3)
```

The countdown prints 3, 2, 1, 0, -1, and keeps going for 998 lines, down to -994. Then the end of the traceback:

```
  [Previous line repeated 995 more times]
  File "...", line 3, in count_down
    print(seconds)
    ~~~~~^^^^^^^^^
RecursionError: maximum recursion depth exceeded
```

The exact line counts can differ slightly between Python versions. The `RecursionError` is what matters.

## Example D: the game loop as recursion, and why it crashes

```python
# The wrong tool: a game loop written as recursion.
# Each turn starts the next turn before it has finished itself.
def take_turn(turn):
    if turn == 1 or turn == 500:
        print(f"Turn {turn}")
    take_turn(turn + 1)

take_turn(1)
```

```
Turn 1
Turn 500
Traceback (most recent call last):
...
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

It never reaches turn 1,000. Now the loop version:

```python
# The right tool for a game loop is a loop. Turn 5000 costs the same as turn 1.
turn = 1
while turn <= 5000:
    turn = turn + 1
print(f"Played {turn - 1} turns with no trouble")
```

```
Played 5000 turns with no trouble
```

You can check the limit on your own machine:

```python
import sys
print(sys.getrecursionlimit())
```

This printed `1000` when these notes were tested. `import` has not been taught yet, and you do not need it for anything else this
unit. It loads a module from Python's standard library, and `sys` holds information about the Python that is running.
