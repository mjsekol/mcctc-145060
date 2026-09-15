# Requirements You Can Check
---
## Slide 1: You built exactly what they said
- The stakeholder said teens get the discount
- You built it, tested it, it works
- They are furious at the demo
- Nobody lied. Nobody made a coding mistake.
Speaker notes: Here is a story that happens to professionals every week. The stakeholder said teens get the discount. You built it, you tested it with a sixteen year old, it works. At the demo the stakeholder asks why their thirteen year old paid full price. Nobody lied and nobody wrote bad code. The requirement was never pinned down, and today you learn how to pin one down before you build.
Image: A demo screen with a green checkmark on one side and a frowning stakeholder silhouette on the other, navy and blue.
---
## Slide 2: Requirement versus acceptance criterion
- Requirement: what it must do, in their words
- Criterion: exactly how anyone can tell it passed
- Given a situation, when an action, then a result
- Two strangers must agree on pass or fail
Speaker notes: A requirement says what the program must do in the stakeholder's words. Report progress toward the goal. An acceptance criterion says exactly how anyone could check it. Given fifty items toward a goal of one fifty, progress is thirty three point three percent. The test for a good criterion is this. Two people who have never met could run it and agree whether it passed.
Image: Two stacked cards, the top labeled requirement in plain words, the bottom labeled criterion with given, when, then lines.
---
## Slide 3: One sentence, two programs
```python
def teen_discount_a(age):
    return 13 <= age <= 19

def teen_discount_b(age):
    return 14 <= age <= 18

for age in [12, 13, 14, 18, 19]:
    print(age, teen_discount_a(age), teen_discount_b(age))
```
Speaker notes: Two developers heard teens get the discount. Developer A says thirteen through nineteen. Developer B says high school, fourteen through eighteen. Both are correct code. Both are reasonable readings. They disagree at thirteen and nineteen, and no amount of programming skill settles that. Only a question to the stakeholder does.
Image: None. This slide is code.
---
## Slide 4: Questions that find requirements
- Walk me through how you do this today
- Tell me about the last time it went badly
- Can you show me an actual example
- How will you know this worked
- What happens when somebody types it wrong
Speaker notes: You get four minutes with your stakeholder tomorrow, so these are the questions worth your minutes. The walkthrough finds where their process breaks. The bad story finds the real problem. The example gets you real data. How will you know it worked is the acceptance criterion question. And what happens when somebody types it wrong finds processing requirements, the ones every team forgets.
Image: A clipboard with five short question lines and a pencil, flat navy style.
---
## Slide 5: Listen like it costs you something
- Restate before you write it down
- A pause or a mostly hides a requirement
- Do not pitch features during the interview
- Face the person. One teammate types.
Speaker notes: Active listening is a competency, and here it has a real payoff. Restate what you heard. So you need to know which category is furthest from its goal, not the total, is that right. If they correct you, you saved a week. When a stakeholder says well, mostly, there is a requirement inside the mostly, so ask. Do not pitch. They will say yes to any feature you suggest, and now you owe them a feature nobody needed.
Image: Two simple figures facing each other across a table, one with a speech bubble echoing the other's words.
---
## Slide 6: Examples the stakeholder agreed to
```python
def ticket_price(age):
    if 13 <= age <= 19:
        return 6
    return 10

agreed = [(12, 10), (13, 6), (19, 6), (20, 10)]
for age, expected in agreed:
    print(age, ticket_price(age) == expected)
```
Speaker notes: Here is what settles the argument. The stakeholder agreed to four examples. Twelve pays ten, thirteen pays six, nineteen pays six, twenty pays ten. Look at which ages those are. The edges, and one step past each edge. Run it and all four print True. Thursday we turn examples like these into a full test file.
Image: None. This slide is code.
---
## Slide 7: Watch this
```python
# The stakeholder said "13 through 19."
def ticket_price(age):
    if 13 < age < 19:
        return 6
    return 10

for age in [13, 16, 19]:
    print(age, ticket_price(age))
```
Speaker notes: The stakeholder said thirteen through nineteen. The developer typed what felt natural and tested with sixteen, the most obvious teenager there is. Predict all three lines before I run it.
Image: None. This slide is code.
---
## Slide 8: Every edge charged the adult price
```
13 10
16 6
19 10
```
Speaker notes: No error. It looks right on sixteen, which is the only age anyone tried. Every thirteen year old and every nineteen year old pays the adult price. Through means including both ends, and less than excludes them. You met this boundary in Unit 2. Now it has a cost. The stakeholder believes you met the requirement, and you did not. The fix is not trying harder. It is a criterion that names thirteen and nineteen before any code exists.
Image: None. This slide is output.
---
## Slide 9: The first ask is rarely the real need
- First ask: I need to count the cans
- The club already counts cans
- Real need: know what to ask for next
- A perfect can counter solves nothing
Speaker notes: The sample stakeholder in our reference sprint opened with I need to count the cans. Two questions later the real story came out. Last year the pantry got hundreds of cans of green beans and almost no protein. The real need was knowing what to ask for next. A program that counts cans perfectly would have solved nothing. You only find that by asking and listening.
Image: A shelf of identical green cans with one empty labeled space where protein should be, navy and blue.
---
## Slide 10: What you are about to build
- Build 1: write your interview questions, practice on a transcript
- Build 2: four minutes with your stakeholder
- Then requirements, each with Given, When, Then criteria
- Name the edges. Log every question you could not ask.
Speaker notes: Build one, your team writes interview questions and practices pulling requirements out of a written transcript. Build two, I become your stakeholder for four minutes per team, so be ready when I get to you. Then write requirements version one, and every requirement gets at least one criterion in given, when, then form. Name the edges explicitly. Anything you ran out of time to ask goes in the question log with the assumption you are making until you get an answer.
Image: A requirements document with numbered R1 and R2 headings and indented criteria lines, navy and blue.
---
