# Lecture Notes: Team Roles, Leadership, and Conflict
## 145060 Programming · Unit 6 · Week 14, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W14_TeamsAndConflict.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W14_TeamsAndConflict.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 1.2.10 (use interpersonal skills to provide group leadership, promote
collaboration, and work in a team), 1.2.4 (negotiation and conflict-resolution skills),
1.2.7 (problem-solving and consensus-building techniques), 1.2.3 (verbal, nonverbal, and
active listening).

---

## Why this exists

Last week your team worked without an instructor in the room. Some of you had a teammate at
Regional. Some of you disagreed about something, and some of those disagreements are still
not settled. Yesterday another team told you what was wrong with your code, and today you
have to decide together which findings to fix first.

That is every real software team. The code is rarely what sinks a project. **Teams sink when
they cannot make a decision and stick to it.** A team that argues for three days about whether
a zero should be allowed has lost three days, whichever answer was right.

This lesson is about the skills that turn a disagreement into a decision, and they are skills,
not personality traits. You can get better at them on purpose.

---

## The concept in plain language

### Roles are accountability. Leadership is behavior.

Your team has four **roles**: Facilitator, Stakeholder Liaison, Test Lead, Integration Lead. A
role answers "whose job was that." It is assigned.

**Leadership** is not a role. It is a set of behaviors any member can do, and on good teams
several members do:

- Making sure the quiet person's view is heard before the decision, not after
- Naming a problem out loud at stand-up instead of hoping it goes away
- Keeping a commitment, or saying early that you cannot
- Proposing a way to decide when the team is stuck
- Giving credit specifically: "Priya's fixture is why that check caught the bug"

### Three kinds of conflict

| Kind | About | Example | Usually |
|---|---|---|---|
| **Task** | What to build | "Should zero items be refused?" | Useful, if resolved. It surfaces real questions. |
| **Process** | How and when to work | "We should fix review findings before building the change." | Useful, if resolved quickly. |
| **Relationship** | Who someone is | "You never listen." | Rarely useful. It stops the other two from getting solved. |

**The goal is not zero conflict.** A team that never disagrees about the task is usually a team
where somebody stopped speaking up. The goal is keeping conflict about the task and the process,
and resolving it.

### Negotiation: positions versus interests

A **position** is what someone says they want. An **interest** is why they want it.

- Position: "Zero items must be refused."
  Interest: "A zero is usually a typo, and a typo should not silently count."
- Position: "Zero items must be allowed."
  Interest: "A volunteer checked an empty bin, and the sheet should show that it was checked."

Positions conflict directly. Interests often do not. **Both interests above can be served**:
refuse zero in the donation log, and record "bin checked, empty" somewhere else. You only find
that option by asking "why do you want that" and restating the answer.

When interests genuinely conflict, use an **objective standard** instead of whoever argues
longest. For a software team, the strongest objective standard is the signed acceptance
criteria. If AC-1.2 says "a whole number above zero," the argument is over, and a new
requirement goes to the stakeholder as a question.

### Consensus-building techniques

| Technique | How it works | Use it when |
|---|---|---|
| **Fist to five** | Everyone shows 0 to 5 fingers. Any 0 or 1 must be heard before deciding. | Checking whether a proposal has real support |
| **Dot voting** | Each person gets a few votes to spread over options | Choosing between many options, like which review findings to fix first |
| **Timebox** | Discussion gets a fixed number of minutes | Every discussion, so nothing runs for three days |
| **Disagree and commit** | After the decision, everyone works on it as if it were their choice | After a real hearing. It does not mean "stop talking." |

**The decision rule must be agreed before the conflict.** Your working agreement already has one.
A rule invented in the middle of an argument always looks like it was invented to win.

---

## Worked example 1: fist to five

```python
# Fist to five: everyone shows 0 to 5 fingers on a proposal.
# The team's working agreement says: any 0 or 1 must be heard before deciding.
proposal = "Cut the chart feature and finish input validation first"
votes = {"Facilitator": 4, "Stakeholder Liaison": 5, "Test Lead": 1, "Integration Lead": 3}

concerns = []
for role in votes:
    if votes[role] <= 1:
        concerns.append(role)

print("Proposal:", proposal)
if len(concerns) > 0:
    print("Not decided yet. Hear from:", ", ".join(concerns))
else:
    print("Decided. Record it in the decision log.")
```

Output:

```
Proposal: Cut the chart feature and finish input validation first
Not decided yet. Hear from: Test Lead
```

Three members like the proposal and the average is above 3. **The rule still stops.** A 1 means
someone has a reason, and the Test Lead might know something the others do not, such as a
check that depends on the chart. Hearing it takes two minutes. Missing it can take two days.

---

## Worked example 2: dot voting on review findings

```python
# Dot voting: each person spends 3 dots on the fixes that matter most.
dots = [
    "validate item counts", "validate item counts", "announcement text",
    "validate item counts", "sort the report", "announcement text",
    "sort the report", "validate item counts", "announcement text",
]

tally = {}
for choice in dots:
    tally[choice] = tally.get(choice, 0) + 1

# Most dots first: sort (negative count, name) pairs.
ranked = []
for choice in tally:
    ranked.append((-tally[choice], choice))
ranked.sort()
for negative_count, choice in ranked:
    print(f"{-negative_count} dots  {choice}")
```

Output:

```
4 dots  validate item counts
3 dots  announcement text
2 dots  sort the report
```

Dot voting is fast and it makes priorities visible. It is **not** the same as consensus: it shows
what most people want, and it can bury one person's strong objection. Use it to rank, then use fist
to five on the top item if anyone looks uneasy.

---

## Worked example 3: a decision rule in code

```python
# The decision rule is agreed BEFORE the conflict, so nobody invents one mid-argument.
def decide(votes, minutes_spent, timebox_minutes):
    """Apply the team's working agreement to one proposal."""
    lowest = min(votes.values())
    if lowest >= 3:
        return "consensus: adopt it"
    if minutes_spent < timebox_minutes:
        return "keep talking: hear the concerns first"
    return "timebox over: facilitator decides and logs the reason"


print(decide({"A": 4, "B": 3, "C": 5}, 3, 10))
print(decide({"A": 4, "B": 1, "C": 5}, 3, 10))
print(decide({"A": 4, "B": 1, "C": 5}, 10, 10))
```

Output:

```
consensus: adopt it
keep talking: hear the concerns first
timebox over: facilitator decides and logs the reason
```

Writing the rule as a function makes its three branches impossible to fudge. Real teams do not run
Python to decide, but they do benefit from rules this clear. **The third branch is the leadership
one:** after a fair hearing and a fixed time, somebody decides, writes down why, and the team
commits.

---

## The wrong version, and what it does instead of an error

The team runs the same dot vote through a shared form, and four people type the options their own way.

```python
# The same kind of dot vote, typed into a shared form by four different people.
dots = [
    "Validate item counts", "validate item counts ", "announcement text",
    "validate item counts", "announcement text", "Validate Item Counts",
    "sort the report", "VALIDATE ITEM COUNTS", "announcement text",
]

tally = {}
for choice in dots:
    tally[choice] = tally.get(choice, 0) + 1

winner = ""
for choice in tally:
    if winner == "" or tally[choice] > tally[winner]:
        winner = choice

print("The team chose:", winner, "with", tally[winner], "dots")
```

Output:

```
The team chose: announcement text with 3 dots
```

**No error. The team spends its afternoon on the announcement, and the fix that five of nine dots
wanted never happens.**

"Validate item counts" got five votes, spelled five different ways, so the dictionary counted five
different options with one vote each. The fix is one line, the same cleaning you did in Unit 1:

```python
    label = choice.strip().lower()     # one spelling per idea
    tally[label] = tally.get(label, 0) + 1
```

```
The team chose: validate item counts with 5 dots
```

A process can have a silent bug too. When a decision tool produces a result that surprises the
people who voted, **check the tally before you check each other.**

---

## Why the wrong version is tempting

**The result looks official.** It came out of a program, so nobody questions it, and the person who
wanted validation assumes they were outvoted.

**Nobody wants to reopen a decision.** Asking "are we sure about that count?" can feel like a sore
loser move. It is not. It is checking the data, which is exactly what you do with code.

**Conflict avoidance.** It is more comfortable to accept a wrong result quietly than to say "I do
not think that is what we voted for." Saying it calmly, with the evidence, is a leadership behavior.

---

## A composite scenario to work through

*This scenario is a composite. It is built from situations common on student teams, not a real
team.*

During BPA week, a team's Test Lead writes a check that refuses `0` items. The Integration Lead
changes the check to allow zero, because "an empty bin is real data." Neither tells the other.
On Monday the check has been flipped twice and both are annoyed.

A resolution using this lesson:

1. **Separate the people from the problem.** The problem is the requirement, not who changed what.
2. **Restate interests.** Test Lead: typos should not count. Integration Lead: checked-but-empty
   bins should be visible.
3. **Check the objective standard.** AC-1.2, signed on Friday of Week 12, says "whole number above zero."
4. **Find the option that serves both.** Keep refusing zero. Log a question to the stakeholder about
   recording empty bins.
5. **Fix the process conflict too.** Add to the working agreement: nobody changes a check another
   member owns without writing it in the stand-up log first.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Role** | An assigned area of accountability on the team. |
| **Leadership** | Behaviors that help the team decide and act, available to any member. |
| **Task conflict** | Disagreement about what to build. |
| **Process conflict** | Disagreement about how or when to work. |
| **Relationship conflict** | Conflict about the people. Rarely productive. |
| **Position** | What someone says they want. |
| **Interest** | Why they want it. |
| **Objective standard** | A shared reference that settles a dispute, such as signed acceptance criteria. |
| **Consensus** | A decision everyone can support, even if it was not their first choice. |
| **Fist to five** | A quick show of support from 0 to 5 fingers. |
| **Dot voting** | Spreading a few votes across options to rank them. |
| **Timebox** | A fixed amount of time for a discussion. |
| **Disagree and commit** | Supporting a decision fully after being genuinely heard. |

---

## Self-check

**Question 1.** Sort each into task, process, or relationship conflict:

- "We should tag v1.0 before building the change, not after."
- "The report should list bins alphabetically."
- "You always take the short tasks and leave us the hard ones."

**Question 2.** Two teammates are stuck. One wants to spend Build 2 fixing every review finding.
The other wants to spend it building the missing requirement. Write one question that uncovers
each person's interest, and one option that might serve both.

**Question 3.** Predict the exact output.

```python
votes = {"Ava": 3, "Ben": 4, "Chloe": 0, "Dev": 5}
concerns = []
for name in votes:
    if votes[name] <= 1:
        concerns.append(name)
print(len(concerns), concerns)
print(sum(votes.values()) / len(votes))
```

---

### Answers

**1.** Process. Task. Relationship. The relationship one should be restated as a task or process
issue before anything else: "Can we look at how tasks got assigned this sprint?"

**2.** Many answers work. Questions: "What happens at the demo if we skip the findings?" and "What
happens at the demo if that requirement is missing?" An option: fix only the must-fix findings,
which usually touch Correctness and Security, then build the requirement, and defer the rest with
written reasons. That serves both interests: nothing dangerous ships, and nothing required is
missing.

**3.** Output:

```
1 ['Chloe']
3.0
```

The average is 3.0, which looks like solid support. Chloe's 0 is the reason the rule looks for
low votes instead of the average.
