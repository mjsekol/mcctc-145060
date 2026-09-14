# Turning Disagreement into Decisions
---
## Slide 1: Three days arguing about a zero
- Should zero items be refused or allowed
- The Test Lead flipped the check one way
- The Integration Lead flipped it back
- Nobody said a word at stand-up
Speaker notes: This is a composite, built from things that happen on student teams all the time. During BPA week, one teammate made a check refuse zero items. Another teammate changed it back to allow zero, because an empty bin is real data. Neither said anything. By Monday the check had flipped twice and both people were annoyed. Three days gone, whichever answer was right. Teams rarely sink on code. They sink when they cannot decide and stick to it.
Image: A single toggle switch drawn twice, pointing opposite ways, with a calendar showing three days crossed out.
---
## Slide 2: Roles are accountability. Leadership is behavior.
- A role answers: whose job was that
- Leadership: making sure the quiet person is heard
- Naming a problem out loud at stand-up
- Proposing a way to decide when stuck
- Any member can lead. Good teams have several.
Speaker notes: Your roles are assigned. Facilitator, liaison, test lead, integration lead. A role tells us whose job something was. Leadership is not a role. It is a set of behaviors anyone on the team can do. Making sure the quietest person speaks before the decision, not after. Saying the problem out loud at stand up. Keeping a commitment or saying early that you cannot. Offering a way to decide when everyone is stuck.
Image: Four role badges in a row, with small light bursts appearing above two different badges, navy and blue.
---
## Slide 3: Three kinds of conflict
- Task: what to build. Useful if resolved.
- Process: how and when to work. Useful if quick.
- Relationship: who someone is. Rarely useful.
- The goal is not zero conflict
Speaker notes: Not all conflict is bad. Task conflict, should zero be refused, surfaces real questions. Process conflict, should we fix findings before building the change, is useful if you settle it fast. Relationship conflict, you never listen, almost never helps, because it stops the other two from getting solved. A team with no task conflict at all is usually a team where someone stopped talking.
Image: Three labeled boxes, the first two with green outlines, the third with a red outline, navy text.
---
## Slide 4: Positions versus interests
- Position: zero must be refused
- Interest: a typo should never silently count
- Position: zero must be allowed
- Interest: an empty checked bin should be visible
- Both interests can be served at once
Speaker notes: A position is what someone says they want. An interest is why. Refuse zero, because a typo should not count. Allow zero, because a volunteer checked an empty bin and that should show. The positions collide. The interests do not. Keep refusing zero in the log and record empty bins some other way. You only find that by asking why do you want that, and restating the answer back.
Image: Two arrows colliding head on labeled positions, and beneath them two parallel arrows labeled interests.
---
## Slide 5: Fist to five
```python
votes = {"Facilitator": 4, "Stakeholder Liaison": 5,
         "Test Lead": 1, "Integration Lead": 3}

concerns = []
for role in votes:
    if votes[role] <= 1:
        concerns.append(role)

if len(concerns) > 0:
    print("Not decided yet. Hear from:", ", ".join(concerns))
else:
    print("Decided. Record it in the decision log.")
```
Speaker notes: Fist to five. Everyone shows zero to five fingers on a proposal. Our working agreement says any zero or one gets heard before we decide. Three people like this proposal and the average is above three. The rule still stops, and prints hear from Test Lead. That one might know something nobody else does. Hearing it takes two minutes. Missing it can take two days.
Image: None. This slide is code.
---
## Slide 6: A decision rule agreed in advance
```python
def decide(votes, minutes_spent, timebox_minutes):
    lowest = min(votes.values())
    if lowest >= 3:
        return "consensus: adopt it"
    if minutes_spent < timebox_minutes:
        return "keep talking: hear the concerns first"
    return "timebox over: facilitator decides and logs the reason"

print(decide({"A": 4, "B": 1, "C": 5}, 10, 10))
```
Speaker notes: Your working agreement already has a decision rule, and here it is as code so the branches cannot be fudged. Everyone at three or above, adopt it. Someone low and time left, keep talking. Someone low and the timebox is over, the facilitator decides and writes down why, and the team commits. That last line prints here. The rule has to exist before the argument, because a rule invented during an argument always looks like it was invented to win.
Image: None. This slide is code.
---
## Slide 7: Watch this
```python
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
Speaker notes: Dot voting on which review findings to fix first. Nine dots from a shared form, typed by four different people. Count how many dots validate item counts really got, then predict what the program picks.
Image: None. This slide is code.
---
## Slide 8: The vote nobody actually cast
```
The team chose: announcement text with 3 dots
```
Speaker notes: No error. Validate item counts got five dots, spelled five different ways, so the dictionary saw five different options with one vote each. The team spends the afternoon on the announcement and the fix most people wanted never happens. The fix is one line from Unit 1. Strip and lower each label before counting. When a decision surprises the people who voted, check the tally before you check each other.
Image: None. This slide is output.
---
## Slide 9: When the argument will not end
- Separate the people from the problem
- Restate each interest until the person agrees
- Check the objective standard: the signed criteria
- Find an option that serves both interests
- Still stuck: the decision rule, then commit
Speaker notes: Here is the sequence when a disagreement will not end. Talk about the problem, not the person. Restate each side's interest until that person says yes, that is it. Check the objective standard, and on a software team the strongest one is the acceptance criteria your stakeholder signed. Look for an option that serves both interests. If you are still stuck, use the rule, and then commit to the result as if it were your idea.
Image: A five-step vertical ladder with short labels on each rung, navy and blue.
---
## Slide 10: What you are about to build
- Build 1: Gate 2 W15, on your own
- Build 2: triage yesterday's review findings as a team
- Dot vote to rank, fist to five on the top item
- Record accepted, rejected, deferred, and why
- Fix the must-fix findings. Every check passes.
Speaker notes: Build one is Gate 2 for this week, individually. Build two is your team's response to yesterday's review. Dot vote to rank the findings, then fist to five on the top one. Clean the labels before you count. Every finding gets accepted, rejected, or deferred, with a reason, in your review response. Fix the must fix findings first. By the end of Build two, every acceptance check passes, because tomorrow we tag that version as the baseline.
Image: A review response table with accepted, rejected, and deferred columns filling in, navy and blue.
---
