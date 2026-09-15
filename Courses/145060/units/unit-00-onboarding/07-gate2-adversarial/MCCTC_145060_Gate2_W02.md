# Gate 2: Adversarial Review · Week 2
## 145060 Programming · Week 2, Friday

**Gate 2 is the gate where AI is the opponent.** You are reviewing this code, not
writing it, and you are scored on what you catch against what you miss.

**40 minutes.** Individual work. You may and should run the code. You may not ask a
model whether it is correct, because the model is what is being reviewed.

---

## What you are looking at

Somebody gave an AI assistant the requirements below and got back the program in
Part B. It runs. It is formatted well, the comments sound confident, and the names
look sensible. **It looks right at a glance.**

**There are exactly five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It creates a risk, including accepting input it should refuse |
| **Readability** | A name or comment that misleads the next person to read it |
| **Performance** | Work being done that does not need to be done |
| **Requirements Fit** | Something the spec asked for that is missing, or invented |

One is genuinely hard to see, and you will not find it by reading. You will find it
by running the program with an input nobody would think to try.

**Finding four out of five is a strong score.**

---

## PART A: The requirements the code was built from

> Write a program called `split_bill.py` that splits a group food order.
>
> It should:
>
> 1. Ask for the food total in dollars. Decimals are allowed.
> 2. Ask for the tip percent, for example 18. Decimals are allowed.
> 3. Ask for how many people are splitting it. **Whole people only.**
> 4. Print four things, each with a label saying what it is:
>    - the food total
>    - **the tip in dollars**
>    - the grand total
>    - what each person owes
> 5. Every prompt must say what it wants, including units.

---

## PART B: What the AI produced

When you cite a line number, count from the first line below, `# split_bill.py`,
as line 1. Blank lines count.

```python
# split_bill.py
#
# Splits a group food order across everyone who is paying.
# Asks for the bill, the tip, and the headcount, then reports what
# each person owes.

print("SPLIT THE BILL")
print("--------------")

food_total = float(input("Food total in dollars: "))
tip_percent = float(input("Tip percent, for example 18: "))
people = float(input("How many people are splitting it? "))

# The total before the tip is added.
total_before_tip = food_total + (food_total * tip_percent / 100)

# What each person owes, once the tip is included.
each_person = (food_total + (food_total * tip_percent / 100)) / people

print("Food total:", food_total)
print("Total before tip:", total_before_tip)
print("Grand total:", food_total + (food_total * tip_percent / 100))
print("Each person owes:", each_person)
```

### A real run, for reference

Typing `60`, then `18`, then `4`:

```
SPLIT THE BILL
--------------
Food total in dollars: 60
Tip percent, for example 18: 18
How many people are splitting it? 4
Food total: 60.0
Total before tip: 70.8
Grand total: 70.8
Each person owes: 17.7
```

**Read that output carefully before you read the code.** One defect is sitting in
plain sight in those four lines, and you do not need to understand any Python to
see it.

---

## What to submit

For each defect, write an entry with all four of these:

1. **File and line.** "Line 15," not "in the middle somewhere."
2. **Dimension.** Which of the five categories.
3. **What goes wrong.** The consequence for an actual person, not "this is bad."
4. **The fix.** One or two lines.

Then one final entry:

5. **What I was unsure about.** Name at least one thing you suspected and could not
   confirm. This is scored. Leaving it blank costs you more than a wrong guess.

### How to actually find these

You have 40 minutes. Spend them like this.

**First 5 minutes: run it.** Type `60`, `18`, `4`. Work out the four numbers
yourself on paper. Compare.

**Next 10 minutes: run it again with inputs nobody would choose.** What happens
with zero people? With a decimal number of people? With an empty answer? At least
two defects only appear this way.

**Next 10 minutes: read Part A one requirement at a time**, and point at the line
of code that satisfies each one. If you cannot point at a line, you have found
something.

**Remaining time: read the comments against the code they sit above.** Ask whether
each comment is true.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor
will state the security weighting before you start. Listen to it.

**The honest expectation: four out of five is a strong Week 2 score.**
