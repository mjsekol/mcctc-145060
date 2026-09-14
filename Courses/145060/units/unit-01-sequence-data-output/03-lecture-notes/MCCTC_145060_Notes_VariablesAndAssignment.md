# Lecture Notes: Variables and Assignment
## 145060 Programming · Unit 1 · Week 2 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W02_Variables.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W02_Variables.pptx)

If you missed class, you can learn this concept from this file alone. Type every
example. Reading code you did not type is close to worthless at this stage.

---

## Why this exists

Every program in Week 1 printed the same thing every time it ran. That is a
poster, not a program. Software is useful when it works on values that change, and
to work on a value you have to be able to refer to it.

That is all a variable is: a way to refer to a value so you can use it more than
once, use it in a calculation, and change it later without rewriting everything
that mentions it.

---

## The concept in plain language

**A variable is a name tied to a value.**

Not a box. Not a container that holds something. A tag, tied to a thing.

```python
hours_worked = 12
```

Read that out loud as **"`hours_worked` gets 12."** Do not read it as "equals." The
word "equals" is what causes almost every problem in this file, and it comes from
algebra, where `x = 5` is a claim that is true or false and reads in both
directions.

In Python, `=` is an instruction, and it goes one direction only:

1. Work out whatever is on the right side.
2. Attach the name on the left to that result.

Right side first, then the name. Always that order.

That single rule explains the line every beginner stares at:

```python
count = count + 1
```

In algebra this is false for every number. In Python it is an instruction: take
what `count` currently points at, add one to it, and point `count` at the new
result. Say "gets" and it stops being strange.

---

## Worked example 1: naming values and using them

```python
hours_worked = 12
pay_rate = 11
total_pay = hours_worked * pay_rate

print("Hours:", hours_worked)
print("Rate:", pay_rate)
print("Total:", total_pay)
```

Output:

```
Hours: 12
Rate: 11
Total: 132
```

Three things to notice.

**The names carry meaning.** `hours_worked` tells a reader what the 12 is. A `12`
sitting alone in a program is a mystery in three weeks, including to you.

**`total_pay` was calculated from other names.** Line 3 did not need to know the
numbers. It needed to know the names.

**`print` put a space between the label and the value.** Nobody typed that space.
That is `print` separating the values you gave it, the same as Week 1.

---

## Worked example 2: a name can be re-tied

```python
score = 0
print("Start:", score)

score = 10
print("After the first round:", score)

score = score + 5
print("After the bonus:", score)
```

Output:

```
Start: 0
After the first round: 10
After the bonus: 15
```

The third assignment is the interesting one. Python worked out `score + 5` using
the value `score` pointed at right then, which was 10. It got 15. Then it re-tied
`score` to 15. The old 10 is not stored anywhere. Nothing remembers it.

---

## Worked example 3: the one that surprises everyone

Predict the output before you read it.

```python
shifts = 3
hours_each = 5
total_hours = shifts * hours_each

shifts = 6

print("Shifts:", shifts)
print("Total hours:", total_hours)
```

Output:

```
Shifts: 6
Total hours: 15
```

**`total_hours` is 15, not 30.**

Most people predict 30. Here is why it is 15. Line 3 ran when Python reached it.
At that moment `shifts` pointed at 3 and `hours_each` pointed at 5, so the right
side worked out to 15, and `total_hours` was tied to 15.

Line 5 re-tied `shifts` to 6. It did not touch `total_hours`, and nothing sent
Python back to redo line 3. **Nothing is watching anything.**

If you want `total_hours` to reflect the new value, you have to run the
calculation again:

```python
shifts = 6
total_hours = shifts * hours_each
print("Total hours:", total_hours)   # 30
```

---

## The wrong version, and the exact error

The most common Week 2 failure is a misspelled name.

```python
hours_worked = 12
print("Hours:", hours_wroked)
```

Output:

```
Traceback (most recent call last):
  File "...", line 2, in <module>
    print("Hours:", hours_wroked)
                    ^^^^^^^^^^^^
NameError: name 'hours_wroked' is not defined. Did you mean: 'hours_worked'?
```

Read it the way you learned in Week 1. What file. What line. What is under the
carets. What kind of error.

`NameError` means Python reached a name and found nothing tied to it. Note that it
suggests the fix. Python compared your unknown name against names that do exist
and found a close one.

**Trust the suggestion enough to look, not enough to paste.** It is based on
spelling similarity alone. It has no idea what you meant.

Here is a second version of the same error with a different cause:

```python
print("Your total is:", total_cost)
price = 8
quantity = 3
total_cost = price * quantity
```

```
NameError: name 'total_cost' is not defined
```

**No suggestion this time.** The name is spelled correctly. It does not exist
**yet**, because Python runs top to bottom and had not reached line 4. The fix is
to move the `print` to the bottom.

Same error type, opposite problem. The presence or absence of `Did you mean:` is
itself a clue.

---

## Why the wrong version is tempting

Two reasons, and they are different for the two errors above.

**The misspelling is tempting because you read what you meant.** Same as the
missing quote in Week 1. Your eye supplies the correct spelling because your brain
put it there. This is why you look at the carets instead of re-reading the line.

**The ordering mistake is tempting because the program looks complete.** Every name
is defined somewhere in the file, and a human reading the whole file understands
it. Python does not read the whole file and then decide. It runs line 1, then line
2, and at line 1 the value genuinely does not exist yet.

The general habit: when Python says a name is not defined, ask two questions in
this order. Is it spelled the same everywhere? Is the line that creates it above
the line that uses it?

---

## Naming, and why it is graded

These are all legal:

```python
x = 12
h = 12
hw = 12
hours_worked = 12
```

Only the last one is worth writing. In six weeks, `x` tells you nothing, and in
this course the name is part of the grade under Readability.

The rules Python enforces: letters, digits, and underscores; not starting with a
digit; not one of Python's own words like `print` or `if`. Names are case
sensitive, so `Hours` and `hours` are two different names, the same way `Print`
and `print` were two different names in Week 1.

The convention this course uses: lowercase words joined by underscores.
`hours_worked`, not `HoursWorked` or `hoursworked`.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Variable** | A name tied to a value. |
| **Assignment** | Attaching a name to a value, with `=`. |
| **`=`** | The assignment instruction. Read it as "gets." |
| **Right side / left side** | The right side is worked out first, then the left name is attached. |
| **Rebinding** | Tying an existing name to a different value. |
| **Expression** | Anything that works out to a value, such as `shifts * hours_each`. |
| **`NameError`** | Python reached a name with nothing tied to it. |
| **Case sensitive** | `Hours` and `hours` are different names. |
| **Snake case** | The naming style used here: `hours_worked`. |
| **Literal** | A value written directly in the code, such as `12`. |

---

## Self-check

**Question 1.** Write the exact output.

```python
price = 4
price = price + 2
price = price * 2
price = price - 4
print(price)
```

**Question 2.** A student writes this and reports that "Python is broken because
`total` did not update." Explain in two sentences what actually happened, without
using the word "variable."

```python
a = 5
b = 3
total = a + b
a = 100
print(total)
```

**Question 3.** Both of these produce a `NameError`. One error message includes a
`Did you mean:` suggestion and the other does not. Say which is which and why.

```python
# Program A
laps = 7
print(lapz)
```

```python
# Program B
print(distance)
distance = 400
```

---

### Answers

**1.** `8`

Step through one line at a time and write the value down after each one:

| After this line | `price` is |
|---|---|
| `price = 4` | 4 |
| `price = price + 2` | 6 |
| `price = price * 2` | 12 |
| `price = price - 4` | 8 |

The two wrong answers to watch for. **12** means you stopped a line early, which
happens because 12 looks like a finished number. **4** means you applied every line
to the original value instead of to the running one. Both are cured by writing the
value down after each line rather than holding four numbers in your head.

**2.** When line 3 ran, Python worked out 5 plus 3 and attached the name `total` to
the answer 8. Changing `a` on line 4 does not send Python back to redo line 3, so
`total` is still tied to 8.

**3.** Program A gets the suggestion. `lapz` is a misspelling of `laps`, which does
exist, so Python finds a close match and offers it.

Program B gets no suggestion. `distance` is spelled correctly and matches the name
on line 2 exactly. The problem is not spelling, it is order: Python runs top to
bottom and had not reached line 2 yet. There is no close match to suggest, because
the name it is looking for is the name it cannot find.
