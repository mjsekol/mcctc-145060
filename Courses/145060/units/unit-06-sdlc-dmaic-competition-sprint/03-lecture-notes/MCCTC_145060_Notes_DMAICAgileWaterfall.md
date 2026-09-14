# Lecture Notes: DMAIC Outside, Agile Inside, and the Case for Waterfall
## 145060 Programming · Unit 6 · Week 13 · Monday, November 30

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W13_OrderingTheWork.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W13_OrderingTheWork.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 5.6.12 (compare and contrast agile and waterfall), 5.6.11 (develop the
application), 1.8.2 (select and organize resources to develop a product).

---

## Why this exists

You have used DMAIC on every project since Week 4. Define, Measure, Analyze, Improve,
Control. You have always used it alone, on a project you picked, with nobody else's
calendar in the way.

Starting today you are on a team, building for somebody else, with a week in the middle
where nobody is teaching. A team has to agree on **the order work happens in**. Not what
to build. The order. Get the order wrong and four people can each work hard all week and
produce nothing that fits together.

There are two big answers to "what order," and professionals have argued about them for
decades. This file gives you both, honestly, and shows where each lives inside DMAIC.

---

## The concept in plain language

### Waterfall: every phase once, in order

In a **waterfall** process, work flows downhill through phases: requirements, then design,
then build, then test, then deliver. Each phase finishes and is signed off before the next
begins. The whole schedule is planned at the start.

### Agile: small complete slices, repeated

In an **agile** process, the team builds a small piece that works from end to end, shows
it to the stakeholder, learns something, and plans the next piece. Each round is a
**sprint**. The work waiting to be done sits in a **backlog**, ordered by value, and the
order can change between sprints.

Agile teams run a few recurring meetings called **ceremonies**:

| Ceremony | When | What it is for |
|---|---|---|
| **Sprint planning** | Start of a sprint | Choose the backlog items that fit the time you have |
| **Stand-up** | Every day, 10 minutes or less | What I did, what I will do, what is blocking me |
| **Sprint review** | End of a sprint | Show the working piece to the stakeholder and get feedback |
| **Retrospective** | End of a sprint | Improve how the team works, not what it built |

### Where DMAIC fits

DMAIC is not a third competitor. It is the frame around the whole project, and the two
approaches above are ways of running one part of it.

```
Define   -> Measure  -> Analyze  -> Improve                         -> Control
(problem)  (baseline,   (design)    [ plan > build > review > retro ]  (baseline,
            criteria)                [ plan > build > review > retro ]   handoff,
                                     (agile sprints live HERE)           retro)
```

**The outside of DMAIC is sequential,** a lot like waterfall. You do not build before you
know the problem, and you do not hand off before you have built. **The inside of Improve
is iterative,** because building is where the surprises are. That is the program rule:
**agile ceremonies live inside Improve.**

This mix is common in real work. Pure versions of either approach are rarer than the
arguments about them suggest.

---

## Worked example 1: a waterfall plan is a list with fixed dates

```python
# Waterfall: every phase happens once, in order, and the dates are set up front.
phases = [
    ("Requirements", "Mon Nov 30", "Tue Dec 1"),
    ("Design", "Wed Dec 2", "Thu Dec 3"),
    ("Build", "Mon Dec 7", "Mon Dec 14"),
    ("Test", "Tue Dec 15", "Wed Dec 16"),
    ("Deliver", "Thu Dec 17", "Thu Dec 17"),
]

for name, start, end in phases:
    print(f"{name:<14}{start} to {end}")
```

Output:

```
Requirements  Mon Nov 30 to Tue Dec 1
Design        Wed Dec 2 to Thu Dec 3
Build         Mon Dec 7 to Mon Dec 14
Test          Tue Dec 15 to Wed Dec 16
Deliver       Thu Dec 17 to Thu Dec 17
```

Look at the Build row. It sits on top of BPA Regional week. Look at the Test row. Testing
starts two days before delivery, which means any defect found in testing has two days to
be fixed. **That is the classic waterfall risk: problems are discovered late, when they
cost the most.**

---

## Worked example 2: an agile backlog, planned one sprint at a time

```python
# Agile: a backlog ordered by value. Each sprint takes the top items that fit.
backlog = [
    (1, "Read the donation log", 2),
    (2, "Total by category", 2),
    (3, "Show what to ask for next", 3),
    (4, "Morning announcement text", 2),
    (5, "Chart of daily totals", 4),
]
capacity = 5   # build blocks this team has in one sprint


def plan_sprint(backlog, capacity):
    """Take items from the top of the backlog while they fit. Returns (taken, blocks used)."""
    taken = []
    used = 0
    for priority, task, blocks in backlog:
        if used + blocks <= capacity:
            taken.append((priority, task, blocks))
            used = used + blocks
    return taken, used


sprint = 1
while len(backlog) > 0:
    taken, used = plan_sprint(backlog, capacity)
    names = []
    for priority, task, blocks in taken:
        backlog.remove((priority, task, blocks))
        names.append(task)
    print(f"Sprint {sprint} ({used} blocks): {', '.join(names)}")
    sprint = sprint + 1
```

Output:

```
Sprint 1 (4 blocks): Read the donation log, Total by category
Sprint 2 (5 blocks): Show what to ask for next, Morning announcement text
Sprint 3 (4 blocks): Chart of daily totals
```

After Sprint 1, the stakeholder can already see real totals from their real log. If the
project stopped there, something useful exists. **That is the agile bet: always have
something working, and put the most valuable work first.**

---

## Worked example 3: the stakeholder changes their mind

```python
# The stakeholder changes their mind after sprint 1. Agile absorbs it at the next planning.
backlog = [
    (3, "Show what to ask for next", 3),
    (4, "Morning announcement text", 2),
    (5, "Chart of daily totals", 4),
]

# New information from the sprint review: bad rows are corrupting the totals.
backlog.append((1, "Refuse negative item counts", 1))
backlog.sort()

print("Next sprint starts with:")
for priority, task, blocks in backlog:
    print(f"  {priority}  {task} ({blocks} blocks)")
```

Output:

```
Next sprint starts with:
  1  Refuse negative item counts (1 blocks)
  3  Show what to ask for next (3 blocks)
  4  Morning announcement text (2 blocks)
  5  Chart of daily totals (4 blocks)
```

The new item goes to the top and nothing else had to be replanned. In the waterfall plan
from example 1, the same discovery during the Test phase means going back to Design with
two days left.

---

## The strongest case for each, honestly

This is a genuine tradeoff. Neither side is the right answer everywhere, and you will
meet professionals who are sure of both.

### The strongest case for waterfall

- **When requirements are fixed and well understood, planning once is cheaper than
  replanning every week.** If you are building the fourth version of a payroll report
  with rules that are set in law, iterating to discover requirements wastes time.
- **Some work must be signed off before the next step legally or physically can start.**
  Hardware, safety-critical systems, and contracts with fixed deliverables often need a
  documented, approved design before anyone builds.
- **Cost and finish date can be predicted up front,** and some stakeholders need exactly that
  to approve the project at all.
- **It produces documentation as a matter of course,** because each phase hands a document
  to the next.
- **It does not depend on a stakeholder being available every week.** Many stakeholders
  are not.

### The strongest case for agile

- **When requirements are uncertain, you find out what is wrong in days instead of at the
  end.** Most software requirements are uncertain, often because the stakeholder does not
  know what they need until they see something.
- **Something working exists early,** so a project that runs out of time still delivers
  value.
- **Testing happens every sprint,** so defects are found while they are small.
- **It absorbs change,** which is the one thing every project has.

### The honest summary

The question is not which is better. **The question is how uncertain the requirements are,
and how expensive a late surprise would be.** Low uncertainty and expensive change: lean
waterfall. High uncertainty and cheap change: lean agile. Most real projects are somewhere
between, which is why the DMAIC frame in this program is sequential outside and iterative
inside.

---

## The wrong version, and what it does instead of an error

A team wants the highest priority work first. Priority 1 is the most important. Somebody
sorts the backlog.

```python
backlog = [
    (1, "Read the donation log", 2),
    (2, "Total by category", 2),
    (3, "Show what to ask for next", 3),
    (4, "Morning announcement text", 2),
    (5, "Chart of daily totals", 4),
]
capacity = 5

# "Highest priority first," so sort with the biggest number on top.
backlog.sort(reverse=True)

used = 0
for priority, task, blocks in backlog:
    if used + blocks <= capacity:
        print(f"Sprint 1 takes: {task}")
        used = used + blocks
```

Output:

```
Sprint 1 takes: Chart of daily totals
```

**No error. No traceback. A confident plan that builds the least valuable feature first.**

The chart takes 4 of the 5 blocks, nothing else fits, and Sprint 1 ends with a chart of
data the program cannot read yet. Python did exactly what it was told. "Highest priority"
meant priority 1 to the team and meant "biggest number" to whoever typed `reverse=True`.

You have seen this shape all semester: `121212` in Week 2, `202` in Week 3, and now a sprint
plan. **The dangerous bugs are the ones that do not crash, and they are not only in code.**
A plan can be one.

---

## Why the wrong version is tempting

**The word "highest" is ambiguous.** Highest number, or highest importance? English does not
say, and both readings are reasonable.

**The output looks like a plan.** It names a real task and prints cleanly. Nobody stops a
plan that looks finished.

**Nobody checks a plan against the goal.** Teams check that a plan exists, not that its first
item is the most valuable one. The fix is a habit: after planning, read the first item aloud
and ask whether the stakeholder would pick that first.

---

## Vocabulary

| Term | What it means |
|---|---|
| **SDLC** | Software development lifecycle: the stages software goes through from idea to retirement. |
| **Waterfall** | Phases done once each, in order, planned up front, each signed off before the next. |
| **Agile** | Work done in short repeated sprints, each producing something working, reordered as you learn. |
| **Sprint** | One fixed-length round of agile work. In this unit, a few class days. |
| **Backlog** | The ordered list of work not yet done. |
| **Sprint planning** | Choosing which backlog items fit in the next sprint. |
| **Stand-up** | A short daily check-in: done, doing, blocked. |
| **Sprint review** | Showing the working piece to the stakeholder at the end of a sprint. |
| **Retrospective** | A team meeting about how to work better next time. |
| **Increment** | The working piece of software produced by a sprint. |
| **DMAIC** | Define, Measure, Analyze, Improve, Control. This program's project frame. |

---

## Self-check

**Question 1.** A team is building a program that calculates overtime pay using rules the
stakeholder has used for fifteen years and will not change. The stakeholder is available
for one meeting at the start and one at the end. Make the strongest case for running this
project closer to waterfall.

**Question 2.** Where in DMAIC do the agile ceremonies go, and why there and not in Define?

**Question 3.** Predict the exact output, then explain in one sentence why this sprint plan
is wrong even though it runs.

```python
backlog = [(2, "Save to file", 3), (1, "Read input", 2), (3, "Color output", 1)]
backlog.sort(reverse=True)
print(backlog[0][1])
```

---

### Answers

**1.** Requirements are fixed and well understood, so the main agile advantage, discovering
requirements by showing working pieces, buys little. The stakeholder cannot attend sprint
reviews, so the feedback loop agile depends on does not exist. Planning once and designing
fully up front is cheaper, and the stakeholder gets a predictable finish date. The risk
waterfall carries, a late surprise, is small when the rules have not changed in fifteen years.

**2.** Inside Improve. Define and Measure are about agreeing on the problem and what success
looks like, and those have to settle before building makes sense. Improve is where the team
builds, and building is where uncertainty lives, so that is where short cycles of plan,
build, review, and retrospective pay off.

**3.** Output:

```
Color output
```

`reverse=True` put the largest priority number first, and priority 3 is the least important
item. The plan starts with color while the program still cannot read input.
