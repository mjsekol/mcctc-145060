# Constraints and Timelines
---
## Slide 1: December 16 is too late to find out
- The demo is Friday, December 18
- Two teammates were at Regional all week
- The plan assumed everyone, every day
- Now the only choice is shipping less
Speaker notes: Here is how a sprint dies. Nobody wrote down the limits. The plan assumed four people in the room every day. BPA week happened, which everyone knew about in November, and on December sixteenth the team discovers it has half the time it planned for. At that point there is no decision left, only less. Today you write the limits down while cutting is still a choice.
Image: A calendar page for mid December with one week shaded and a red circle on the eighteenth, navy and blue.
---
## Slide 2: A constraint is a fence, not a feature
- Technical: standard library, lab machines, Python 3.14
- Time: acceptance demo Friday, December 18
- People: known BPA days, known absences
- Legal and ethical: no personal information, ever
- Every constraint comes with why it exists
Speaker notes: A requirement is something the program does. A constraint is a fence around where the program is allowed to exist. Technical limits, time limits, people limits, legal and ethical limits, and whatever the stakeholder cannot bend on. Every one you write down needs a reason next to it. A constraint with a reason can be questioned or confirmed. A constraint without one is a rumor.
Image: A simple fenced rectangle with four labeled fence sides and a small program icon inside, navy and blue.
---
## Slide 3: The language is a constraint too
- Python: reads and validates files, testable, runs here
- Spreadsheet: stakeholder knows it, but breaks silently
- JavaScript page: shareable, but nobody here knows it yet
- Choosing Python is a decision. Log the reason.
Speaker notes: You are building in Python, and I want you to be able to say why, because a stakeholder might ask. Python reads and checks messy files, you can test it, and it runs on these machines. A spreadsheet is what many stakeholders already use, and one dragged formula can break it without a sound. A web page can be shared with one link, and none of you has learned it yet. For this sprint Python wins, and that is a decision with reasons, so it goes in your decision log.
Image: Three columns comparing a terminal icon, a spreadsheet grid icon, and a browser icon, with short plus and minus marks.
---
## Slide 4: Count class days, not calendar days
```python
class_days = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
bpa_days = ["Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Fri Dec 11"]

here = 0
for day in class_days:
    if day not in bpa_days:
        here = here + 1
print("Days a competitor is in the room:", here)
```
Speaker notes: Timelines run on class days, because weekends and winter break do not build software. Here is our sprint as a list. The BPA days are the ones a competitor might miss, worst case. The loop counts the days that are not BPA days. It prints eleven. Fifteen days in the sprint, eleven in the room. Plan for the worst case on paper.
Image: None. This slide is code.
---
## Slide 5: Plan backward from what cannot move
- The demo date is fixed. Start there.
- Baseline two class days before the demo
- First working increment five class days before
- Acceptance tests agreed eleven class days before
Speaker notes: Do not plan forward from today, because forward planning always runs out of days at the end. Start at the date that cannot move, Friday the eighteenth, and count back in class days. Two class days back is Wednesday the sixteenth, the baseline. Five back is Friday the eleventh, the first increment. Eleven back is Thursday the third, which is tomorrow, when your acceptance tests get written.
Image: A horizontal timeline with arrows pointing leftward from a flag on December 18 to three earlier milestones.
---
## Slide 6: Does the work fit
```python
remaining_estimate = 22
days_left = 6
blocks_per_day = 2
people = 3
absences = 4

capacity = days_left * blocks_per_day * people - absences
print("Capacity:", capacity, "Remaining:", remaining_estimate)
if remaining_estimate > capacity:
    print("Cut scope now.")
else:
    print("Fits, with", capacity - remaining_estimate, "blocks of slack.")
```
Speaker notes: Capacity is the build time you really have. Days, times blocks per day, times people, minus the blocks you already know you will lose. Six days, two blocks, three people, minus four for BPA. Thirty two blocks. The work is estimated at twenty two, so it fits with ten blocks of slack. That slack is not wasted. Estimates are guesses and guesses run low. Slack is what absorbs the bug that eats a whole afternoon.
Image: None. This slide is code.
---
## Slide 7: Watch this
```python
# Copied from the BPA schedule email.
bpa_days = ["Mon Dec 07", "Tue Dec 08", "Wed Dec 09", "Fri Dec 11"]

here = 0
for day in class_days:
    if day not in bpa_days:
        here = here + 1
print("Days a competitor is in the room:", here)
```
Speaker notes: Same program. This time a teammate copies the BPA dates straight out of the official schedule email, which writes the dates its own way. Everything else is identical. Predict the number before I run it.
Image: None. This slide is code.
---
## Slide 8: Three days that do not exist
```
Days a competitor is in the room: 14
```
Speaker notes: No error. Fourteen instead of eleven. Mon Dec zero seven and Mon Dec seven are different strings, so not in is True for every BPA day except Friday, which happened to be written the same way. The plan gains three days that do not exist, capacity looks comfortable, and the team promises more than it can build. A comfortable number stops the questions, which is why this bug survives. Print the list of days you excluded and read it.
Image: None. This slide is output.
---
## Slide 9: A milestone you can check
- A date on a class day
- One named owner, plus a backup
- Done when: something a stranger could verify
- Tested checks passing, not percent complete
Speaker notes: Every milestone on your timeline needs three things. A class day. One owner, with the backup from your charter. And a done when that a stranger could check. Tests written and failing is checkable. Eighty percent done is not, because nobody can check a percent. When in doubt, make the done when a number of acceptance checks passing.
Image: A single timeline card with date, owner, backup, and done when fields, navy header and blue labels.
---
## Slide 10: What you are about to build
- Build 1: constraints, each with its reason
- Build 1: a baseline measurement from real sample data
- Build 2: a timeline on class days, including BPA week
- Capacity counted, and what you cut first if it shrinks
Speaker notes: Build one, list every constraint with why it exists, then take a baseline measurement. Count something real in your stakeholder's sample data, like how many rows have a problem nobody would catch today. That number is what Measure means. Build two, your timeline on class days, with BPA week and every known absence in it. Count capacity. Then write down what you will cut first if capacity shrinks, and write it today, while nobody is panicking.
Image: A timeline document with a constraints table above a row of class day milestones, navy and blue.
---
