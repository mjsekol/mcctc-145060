# Problem Drop 2: The Chore Chart
## 145060 Programming · Unit 5 · Friday, November 13, 2026

**Time:** 5 minutes to read, 45 minutes to build, 5 minutes to commit. **Mode:** individual.
**Gate:** 3, full tooling, AI usage log required if you use a model.
**What you may use:** anything from Units 0 through 5 so far: loops, functions, error
handling, lists, dictionaries, sets, and tables of dictionaries.

---

## Read this as though a parent sent it to you

> Our house has three kids, Nia who is 15, Sam who is 13, and Eli who is 10, and five chores
> every day. We have a whiteboard chart. Every single night somebody says it is not fair.
> Mostly Sam. Last week Sam said he "always gets the bathroom," and Nia said Sam does fewer
> chores than anybody, which is true, I counted.
>
> I am done refereeing. Can you make a program that picks who does which chore, randomly, so
> nobody can say I play favorites? Random is fair, right?
>
> I typed in the last two weeks from photos of the whiteboard, and the minutes are my guess at
> how long each chore takes.

---

## The data the parent typed in

Copy this into a file called `chore_history.py` in your repository.

```python
# The last two weeks of the whiteboard, typed in by a parent.
CHORES = {
    "dishes": 20,
    "trash and recycling": 5,
    "bathroom": 30,
    "vacuum living room": 15,
    "feed the dog": 5,
}

# One entry per day: who did which chore. Week 1 is days 1 to 7.
HISTORY = [
    {"day": 1, "dishes": "Nia", "trash and recycling": "Eli", "bathroom": "Sam", "vacuum living room": "Eli", "feed the dog": "Nia"},
    {"day": 2, "dishes": "Sam", "trash and recycling": "Nia", "bathroom": "Sam", "vacuum living room": "Nia", "feed the dog": "Eli"},
    {"day": 3, "dishes": "Eli", "trash and recycling": "Nia", "bathroom": "Sam", "vacuum living room": "Nia", "feed the dog": "Nia"},
    {"day": 4, "dishes": "Nia", "trash and recycling": "Sam", "bathroom": "Eli", "vacuum living room": "Sam", "feed the dog": "Eli"},
    {"day": 5, "dishes": "Sam", "trash and recycling": "Eli", "bathroom": "Sam", "vacuum living room": "Eli", "feed the dog": "Nia"},
    {"day": 6, "dishes": "Nia", "trash and recycling": "Nia", "bathroom": "Nia", "vacuum living room": "Sam", "feed the dog": "Eli"},
    {"day": 7, "dishes": "Eli", "trash and recycling": "Sam", "bathroom": "Sam", "vacuum living room": "Eli", "feed the dog": "Eli"},
    {"day": 8, "dishes": "Sam", "trash and recycling": "Eli", "bathroom": "Eli", "vacuum living room": "Nia", "feed the dog": "Nia"},
    {"day": 9, "dishes": "Nia", "trash and recycling": "Eli", "bathroom": "Sam", "vacuum living room": "Eli", "feed the dog": "Sam"},
    {"day": 10, "dishes": "Eli", "trash and recycling": "Nia", "bathroom": "Nia", "vacuum living room": "Sam", "feed the dog": "Eli"},
    {"day": 11, "dishes": "Sam", "trash and recycling": "Eli", "bathroom": "Sam", "vacuum living room": "Nia", "feed the dog": "Nia"},
    {"day": 12, "dishes": "Nia", "trash and recycling": "Sam", "bathroom": "Eli", "vacuum living room": "Eli", "feed the dog": "Sam"},
    {"day": 13, "dishes": "Eli", "trash and recycling": "Nia", "bathroom": "Sam", "vacuum living room": "Sam", "feed the dog": "Nia"},
    {"day": 14, "dishes": "Sam", "trash and recycling": "Eli", "bathroom": "Nia", "vacuum living room": "Nia", "feed the dog": "Eli"},
]
```

The family, the names, and the data are invented.

---

## What you are being asked to do

**Build something in 45 minutes that would actually make this house argue less.**

That is deliberately not the same as "build a random chore picker." The parent told you what
hurts and suggested a fix. Your first job is deciding whether the suggested fix solves what
hurts. You are allowed to build what they asked for. You are also allowed to build something
else, if you can show why.

**You will not finish everything this family needs in 45 minutes.** Nobody will. Choosing what
to leave out is part of what is graded.

---

## What to hand in

In your repository, in a folder called `problem-drop-02`:

1. **`chore_history.py`**, the data above.
2. **Your program**, one or more `.py` files, that runs with `python` and no installs.
3. **`README.md`** with four short sections:
   - **The real problem.** One or two sentences. What is actually making this house argue?
   - **What I built and why.** What your program does, and why that addresses the real problem.
   - **What I left out.** At least one thing the family needs that you chose not to build.
   - **A real run.** Paste your program's output.
4. **A commit** before the end of the block.

## During the last part of the block

Your instructor will come to you and ask you one question about a choice you made. It takes
about a minute. You do not need to prepare a speech. You need to know why you built what you
built.

---

## How it is graded

30 points, under Lab & Practice.

| Part | Points | What earns it |
|---|---|---|
| **Problem Identification** | 15 | The README names what is actually causing the arguments, and it is supported by the data, not by a guess. |
| **Working Artifact** | 10 | The program runs, uses the data, and does what the README says it does. |
| **Tradeoff** | 5 | You can explain, out loud, what your design gives up and who in that family would object. |

**A small program aimed at the real problem scores higher than a large program aimed at the
wrong one.**
