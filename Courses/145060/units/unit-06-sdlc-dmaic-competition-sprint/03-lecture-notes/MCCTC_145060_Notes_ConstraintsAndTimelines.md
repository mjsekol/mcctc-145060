# Lecture Notes: Constraints and Timelines
## 145060 Programming · Unit 6 · Week 13 · Wednesday, December 2

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W13_ConstraintsAndTimelines.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W13_ConstraintsAndTimelines.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 5.6.2 (identify constraints and system processing requirements), 5.6.3
(develop and adhere to timelines), 1.8.2 (select and organize resources to develop a
product), 5.1.6 (strengths and weaknesses of different languages for a specific problem,
introduced).

---

## Why this exists

Yesterday you found out what the stakeholder needs. Today you find out what is standing in
the way.

Every project has limits it cannot argue with. The lab machines will not install packages.
The demo is December 18 and the building closes for winter break on December 21. Some of
your teammates will be at BPA Regional next week and your instructor will be with them.

A team that ignores those limits does not make them go away. It discovers them on
December 16, when the only option left is to ship less than it promised. A team that
writes them down on December 2 gets to decide what to cut while cutting is still a choice.

---

## The concept in plain language

A **constraint** is a limit on how a project can be built or delivered. It is not a thing
the program does. It is a fence around the space where the program is allowed to exist.

| Kind | Example from this unit | What it rules out |
|---|---|---|
| **Technical** | Standard library only, lab machines, Python 3.14 | Charting packages, a database server |
| **Time** | Acceptance demo Friday, December 18 | Anything that cannot be tested by Thursday |
| **People** | Two teammates compete at Regional on known days | A plan where one person holds the only copy of the knowledge |
| **Legal and ethical** | No personal information in a public repository | Tracking who donated or who checked out a part |
| **Stakeholder** | The announcement must fit a 200-character card | Long sentences and lists |

Every constraint should come with **why it exists.** A constraint with a reason can be
questioned, negotiated, or confirmed. A constraint with no reason is a rumor.

### The language is a constraint too

You are building in Python, and it is worth knowing why, because the choice has real
tradeoffs. That comparison is competency 5.1.6.

| Option | Strength for these stakeholder problems | Weakness |
|---|---|---|
| **Python script** | Reads CSV and JSON with the standard library, validates every row, repeatable, testable | The stakeholder needs a terminal. No built-in window or web page. |
| **A spreadsheet with formulas** | The stakeholder already knows it, and they can see every number | Hard to validate messy rows, hard to test, and one dragged formula breaks silently |
| **A web page in JavaScript** | Runs in any browser, and sharing it is one link | Reading local files is limited by the browser, and nobody on the team has learned it yet |

For this sprint, Python wins on the constraints that matter most: the team knows it, it
runs on the lab machines, and it can be tested. **That is a decision, not a default,** and a
stakeholder who lives in spreadsheets might reasonably want the second row. Write the
decision and its reason in your decision log.

### A timeline runs on class days

A **timeline** is a list of milestones, each with a date, an owner, and a "done when" that
someone could check. It is built on **class days**, not calendar days, because weekends,
winter break, and no-school days do not build software.

Two habits make timelines honest:

1. **Plan backward from the date that cannot move.** The demo is fixed. Everything else is
   placed before it.
2. **Count capacity before committing to scope.** Capacity is the build time your team really
   has: days, times blocks per day, times people, minus known absences.

---

## Worked example 1: class days, and a teammate at Regional

```python
# Timelines run on class days, not calendar days. Weekends are not in the list.
class_days = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
bpa_days = ["Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Fri Dec 11"]

# A teammate competing at Regional misses the BPA days.
days_for_competitor = 0
for day in class_days:
    if day not in bpa_days:
        days_for_competitor = days_for_competitor + 1

print("Class days in the sprint:", len(class_days))
print("Days a competitor is in the room:", days_for_competitor)
print("Build blocks for that competitor:", days_for_competitor * 2)
```

Output:

```
Class days in the sprint: 15
Days a competitor is in the room: 11
Build blocks for that competitor: 22
```

This is the worst case, a competitor out on every event day. Most competitors will miss
fewer. **Plan for the worst case on paper, and be pleasantly surprised in real life.**

---

## Worked example 2: plan backward from the date that will not move

```python
# Plan backward from a date that will not move.
class_days = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
demo_index = class_days.index("Fri Dec 18")

# Each milestone is due a number of class days before the demo.
milestones = [
    ("Acceptance tests agreed", 11),
    ("First working increment", 5),
    ("Baseline v1.0 tagged", 2),
    ("Stakeholder demo", 0),
]
for name, days_before in milestones:
    print(f"{class_days[demo_index - days_before]:<12}{name}")
```

Output:

```
Thu Dec 3   Acceptance tests agreed
Fri Dec 11  First working increment
Wed Dec 16  Baseline v1.0 tagged
Fri Dec 18  Stakeholder demo
```

Counting in class days means "five class days before the demo" lands on Friday, December 11,
not on a Sunday. The list does the skipping for you, which is the point of building a
timeline on class days.

---

## Worked example 3: does the work fit?

```python
# A constraint check: does the work fit the time that is actually left?
remaining_estimate = 22        # build blocks the unfinished tasks need
days_left = 6                  # class days of building left
blocks_per_day = 2
people = 3
absences = 4                   # blocks lost to BPA events and appointments

capacity = days_left * blocks_per_day * people - absences
print("Capacity:", capacity, "blocks")
print("Remaining:", remaining_estimate, "blocks")
if remaining_estimate > capacity:
    print("Cut scope now. Decide what the stakeholder can live without.")
else:
    print("It fits, with", capacity - remaining_estimate, "blocks of slack.")
```

Output:

```
Capacity: 32 blocks
Remaining: 22 blocks
It fits, with 10 blocks of slack.
```

**Slack is not wasted time.** Estimates are guesses, and guesses are usually low. Ten blocks
of slack is what absorbs the bug that takes a whole afternoon.

---

## The wrong version, and what it does instead of an error

A team copies the BPA dates out of an email that writes dates its own way.

```python
class_days = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
# Copied from the BPA schedule email, which writes dates its own way.
bpa_days = ["Mon Dec 07", "Tue Dec 08", "Wed Dec 09", "Fri Dec 11"]

days_for_competitor = 0
for day in class_days:
    if day not in bpa_days:
        days_for_competitor = days_for_competitor + 1

print("Days a competitor is in the room:", days_for_competitor)
```

Output:

```
Days a competitor is in the room: 14
```

**No error. The plan now says the competitor is in the room 14 days instead of 11.**

`"Mon Dec 07"` and `"Mon Dec 7"` are different strings, so `not in` is true for every BPA
day except Friday, which happened to be written the same way. The timeline gains three days
that do not exist, the capacity number looks comfortable, and the team commits to scope it
cannot deliver.

Same shape as every silent bug this semester. `121212`. `202`. A `.get()` default that
hides a typo. **The program did exactly what it was told, and what it was told was wrong.**

---

## Why the wrong version is tempting

**Copying is faster than retyping.** The dates came from an official email, so they feel
trustworthy. Nobody checks official dates.

**Membership tests fail quietly.** `in` and `not in` never raise an error. They answer
`False` and move on, and `False` looks like a perfectly normal answer.

**A comfortable number stops the questions.** If capacity had come out too low, somebody
would have checked. When the plan says everything fits, nobody looks for the bug that made
it fit.

The defense: **print the list of excluded days and read it.** If you expected four BPA days
removed and the output shows one, you find the bug in ten seconds.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Constraint** | A limit on how the project can be built or delivered. |
| **Processing requirement** | What the program must do with input nobody planned for. |
| **Timeline** | Milestones with dates, owners, and a checkable "done when." |
| **Milestone** | A point in the timeline where something specific is finished. |
| **Class day** | A day school is in session. The only kind of day that builds software here. |
| **Capacity** | Build time really available: days times blocks times people, minus absences. |
| **Estimate** | A guess at how much time a task needs. Usually low. |
| **Slack** | Capacity left over after the estimate. It absorbs surprises. |
| **Backward planning** | Placing milestones by counting back from a date that cannot move. |
| **Scope** | What the project will deliver. The thing you cut when capacity runs out. |

---

## Self-check

**Question 1.** For each item, say whether it is a requirement or a constraint, and why.

- The program ranks food categories by how far each is from its goal.
- The program must run on a lab machine without installing anything.
- The stakeholder cannot meet with the team during the week of December 7.
- A row with a blank bin is reported with its line number.

**Question 2.** A team of four has 5 class days of building left, 2 blocks per day. Two
members will miss one day each. Their remaining tasks are estimated at 38 blocks. What is
their capacity, and what should they do today?

**Question 3.** Predict the exact output, and explain the bug in one sentence.

```python
week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
off = ["mon", "Fri"]
working = 0
for day in week:
    if day not in off:
        working = working + 1
print(working)
```

---

### Answers

**1.**

- **Requirement**, functional. It is something the program does.
- **Constraint**, technical. It limits how the program can be built, not what it does.
- **Constraint**, people and time. It limits the schedule, and it means questions that week
  go into the question log.
- **Requirement**, processing. It is what the program does with bad input.

**2.** Capacity is 5 days times 2 blocks times 4 people, which is 40, minus 2 absent days
times 2 blocks, which is 4. **Capacity is 36 blocks.** The work is 38 blocks, so it does not
fit even if every estimate is right, and estimates are usually low. **Today** they should
choose what to cut with the stakeholder's agreement and record the decision, not hope to
work faster.

**3.** Output: `4`

`"mon"` is lowercase and the week list says `"Mon"`, so Monday is not recognized as a day
off. Only Friday is excluded. The count should be 3.
