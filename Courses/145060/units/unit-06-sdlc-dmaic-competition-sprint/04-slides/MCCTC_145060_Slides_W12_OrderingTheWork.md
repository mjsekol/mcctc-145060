# Ordering the Work
---
## Slide 1: Four people, one week, nothing fits together
- Everyone on the team worked hard
- Nobody's piece connects to anybody else's
- The stakeholder sees nothing on Friday
- The problem was never effort. It was order.
Speaker notes: Picture a group project where all four of you really did work. One person built the input, one built the report, one wrote a README, one made slides. On Friday none of it connects, because nobody agreed on what order the work happens in. Starting today you are on a team, building for somebody who is not you, with a week in the middle where I am not here. Today is about the order of work.
Image: Four puzzle pieces on a navy background that clearly do not fit together, accent blue edges.
---
## Slide 2: Waterfall, every phase once
- Requirements, then design, then build, then test, then deliver
- Each phase signed off before the next starts
- The whole schedule is planned on day one
Speaker notes: The first answer is called waterfall, because work flows downhill and does not flow back up. You finish requirements, get them signed, then design, then build, then test, then deliver. It sounds orderly, and for some projects it is exactly right. Watch what happens when we put it on our real calendar.
Image: A simple five-step staircase diagram flowing downward left to right, navy steps, blue arrows.
---
## Slide 3: Waterfall on our calendar
```python
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
Speaker notes: Here is a waterfall plan as a list. Look at two rows before I run it. Build sits right on top of BPA Regional week. Test starts two days before delivery. Anything testing finds has two days to be fixed. That is the classic waterfall risk. Problems show up late, when they cost the most.
Image: None. This slide is code.
---
## Slide 4: Agile, small working slices
- Build a small piece that works end to end
- Show it to the stakeholder, learn something
- Reorder the backlog, plan the next sprint
- Always have something that runs
Speaker notes: The second answer is agile. Instead of one long build, you build a small slice that works all the way through, show it, learn, and plan the next slice. The list of work not yet done is the backlog, ordered by value. Each round is a sprint. Four meetings repeat every sprint: planning, a daily stand-up, a review with the stakeholder, and a retrospective about how the team worked.
Image: A circular loop of four labeled arcs, plan, build, review, retro, navy with blue arrows.
---
## Slide 5: A backlog, one sprint at a time
```python
backlog = [
    (1, "Read the donation log", 2),
    (2, "Total by category", 2),
    (3, "Show what to ask for next", 3),
    (4, "Morning announcement text", 2),
    (5, "Chart of daily totals", 4),
]
capacity = 5
used = 0
for priority, task, blocks in backlog:
    if used + blocks <= capacity:
        print("Sprint 1 takes:", task)
        used = used + blocks
```
Speaker notes: Here is a backlog. Priority, task, and how many build blocks it needs. The team has five blocks this sprint. The loop takes items from the top while they fit. Run it and you get reading the log and totals by category. After one sprint the stakeholder sees real totals from real data. If the project stopped there, something useful exists.
Image: None. This slide is code.
---
## Slide 6: Where each one lives in DMAIC
- Define, Measure, Analyze: sequential, like waterfall
- Improve: agile sprints, planning, stand-ups, review, retro
- Control: baseline, handoff, retrospective
- Outside is ordered. Inside Improve is iterative.
Speaker notes: You have used DMAIC since Week 4, and it is not a third competitor. It is the frame around everything. The outside runs in order, because you do not build before you know the problem. The inside of Improve runs in sprints, because building is where the surprises live. That is the program rule. Agile ceremonies live inside Improve.
Image: A horizontal five-box DMAIC bar with the Improve box expanded into a small loop, navy and blue.
---
## Slide 7: The strongest case for each
- Waterfall: fixed rules, fixed contract, predictable date
- Waterfall: works when the stakeholder is rarely available
- Agile: uncertain requirements get discovered early
- Agile: defects found while small, something always works
- The real question: how uncertain, and how costly is change
Speaker notes: This is a real tradeoff and I am not going to pretend one side wins. If the rules are fixed by law or contract and the stakeholder can meet twice all project, waterfall is cheaper and more predictable. If nobody really knows what they need until they see something, agile finds out in days instead of at the end. Most real projects are in between, which is why our frame is ordered outside and iterative inside.
Image: A balance scale with two labeled pans, predictability on one side and adaptability on the other.
---
## Slide 8: Watch this
```python
# "Highest priority first," so put the biggest number on top.
backlog.sort(reverse=True)

used = 0
for priority, task, blocks in backlog:
    if used + blocks <= capacity:
        print("Sprint 1 takes:", task)
        used = used + blocks
```
Speaker notes: Same backlog. A teammate wants the highest priority first, so they sort with reverse equals True. Priority one is our most important item. Predict what Sprint 1 takes before I run it.
Image: None. This slide is code.
---
## Slide 9: A confident plan for the wrong thing
```
Sprint 1 takes: Chart of daily totals
```
Speaker notes: No error. No traceback. The chart eats four of the five blocks, nothing else fits, and Sprint 1 ends with a chart of data the program cannot read yet. Highest priority meant priority one to the team and meant the biggest number to whoever typed reverse. You have seen this shape all semester. One two one two one two, then two oh two, now a sprint plan. The dangerous bugs do not crash, and a plan can be one.
Image: None. This slide is output.
---
## Slide 10: What you are about to build
- Build 1: your team, your roles, your backups for BPA week
- A working agreement with a decision rule, before any disagreement
- Build 2: Define, a project charter draft
- Problem statement names what hurts, not what to build
Speaker notes: Build one, you meet your team, pick roles, and name a backup for every role, because some of you compete at Regional next week. You write a working agreement, including how you will decide when you disagree, and you write it now while nobody is disagreeing. Build two is Define. A charter draft. Your problem statement says what hurts for your stakeholder, not what you plan to build. Read the first line of your plan out loud before you leave and ask whether your stakeholder would pick it first.
Image: A blank project charter page with four role boxes and a backup box under each, navy and blue.
---
