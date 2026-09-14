# Lecture Notes: Requirements and Acceptance Criteria
## 145060 Programming · Unit 6 · Week 13 · Tuesday, December 1

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W13_Requirements.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W13_Requirements.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 5.6.1 (determine requirements specification documentation), 5.6.2
(identify constraints and system processing requirements), 1.2.3 (verbal, nonverbal, and
active listening skills).

---

## Why this exists

A stakeholder never hands you a specification. They hand you a feeling. "Every Monday we
are out of butter." "Things get checked out and never come back." "I want to know what to
ask for next."

If you build from the feeling, you build **your guess about** their problem. You will not
find out whether the guess was right until the demo, and at the demo it is too late.

Requirements turn a feeling into something you can build. Acceptance criteria turn a
requirement into something you can check. Together they are the difference between "I
think it works" and "we agreed on December 4 what working means, and here it is working."

---

## The concept in plain language

A **requirement** says what the program must do, in the stakeholder's terms.

> R2. The program reports progress toward the pantry's total goal.

An **acceptance criterion** says exactly how anyone can tell whether one requirement is
met. It is concrete enough that two people who have never met would agree on pass or fail.

> AC-2.2. Given 50 items collected toward a goal of 150, when progress is calculated, then
> progress is 33.3 percent and 100 items remain.

The **Given, When, Then** shape is a habit, not a law. It forces three things into the
criterion: the situation, the action, and a result you can compare against.

### Three kinds of requirement

| Kind | Question it answers | Example |
|---|---|---|
| **Functional** | What must it do? | Rank categories by how far each is from its goal. |
| **Processing** | What happens to input nobody planned for? | A row with `twelve` in the items column is skipped and reported with its line number. |
| **Constraint** | What limits how it can be built? | Runs on a lab machine with no packages installed. |

Constraints get their own lesson tomorrow. Processing requirements are the ones teams
forget, and they are where most real failures live.

### The first ask is rarely the real need

The reference sprint's stakeholder opened with "I need to count the cans." The club already
counted cans. Two questions later: last year the pantry got hundreds of cans of green
beans and almost no protein. **The real need was knowing what to ask for next.** A program
that counts cans perfectly would have solved nothing.

You find the real need by asking, and by listening to the answer instead of waiting for
your turn to talk.

---

## How to run a stakeholder interview

You get four minutes. Prepare, because four minutes goes fast.

**Questions that find requirements:**

1. "Walk me through how you do this today, step by step." Listen for where it goes wrong.
2. "Tell me about the last time this went badly." A real story beats a general complaint.
3. "Can you show me an example?" Ask for the actual sheet, file, or list.
4. "How will you know this worked?" This is the acceptance criterion question.
5. "What happens when somebody types it wrong?" This finds processing requirements.
6. "What must it never do?" This finds the constraints nobody mentions.

**Active listening, which is competency 1.2.3, used for a reason:**

- **Restate before you write.** "So what you need is to know which category is furthest
  from its goal, not the total count. Is that right?" If they correct you, you saved a week.
- **Watch for the pause.** When a stakeholder hesitates or says "well, mostly," there is a
  requirement hiding in the "mostly." Ask about it.
- **Do not pitch.** "What if it had a chart?" teaches you nothing. The stakeholder will say
  yes to almost any feature, and now you have a requirement nobody needed.
- **Nonverbal counts.** Face the person, not your laptop. One person types. Everyone else
  listens.

---

## Worked example 1: one sentence, two programs

The stakeholder said "Teens get the discount." Two developers each wrote a program.

```python
# The stakeholder said: "Teens get the discount." Two developers, two readings.

def teen_discount_a(age):
    """Developer A: a teen is anyone whose age ends in -teen, 13 through 19."""
    return 13 <= age <= 19


def teen_discount_b(age):
    """Developer B: a teen is a high school student, so 14 through 18."""
    return 14 <= age <= 18


for age in [12, 13, 14, 18, 19]:
    print(f"age {age}:  A says {teen_discount_a(age)},  B says {teen_discount_b(age)}")
```

Output:

```
age 12:  A says False,  B says False
age 13:  A says True,  B says False
age 14:  A says True,  B says True
age 18:  A says True,  B says True
age 19:  A says True,  B says False
```

**Both programs are correct code.** Both developers had a reasonable reading. They disagree
on 13 and 19, and only the stakeholder can say which reading is right. No amount of
programming skill settles it. A question does.

---

## Worked example 2: an acceptance criterion you can run

```python
# A requirement becomes testable when the stakeholder agrees to concrete examples.
# AC-2.1  Given a customer aged 13 through 19, when they buy a ticket, they pay $6.
# AC-2.2  Given a customer aged 12 or 20, when they buy a ticket, they pay $10.

def ticket_price(age):
    """Return the ticket price agreed in AC-2.1 and AC-2.2."""
    if 13 <= age <= 19:
        return 6
    return 10


agreed_examples = [(12, 10), (13, 6), (19, 6), (20, 10)]
for age, expected in agreed_examples:
    actual = ticket_price(age)
    if actual == expected:
        print(f"PASS  age {age}: expected ${expected}, got ${actual}")
    else:
        print(f"FAIL  age {age}: expected ${expected}, got ${actual}")
```

Output:

```
PASS  age 12: expected $10, got $10
PASS  age 13: expected $6, got $6
PASS  age 19: expected $6, got $6
PASS  age 20: expected $10, got $10
```

Look at which ages the stakeholder agreed to: 12, 13, 19, 20. **The edges and one step past
each edge.** Those four examples settle the whole argument from example 1. Thursday's lesson
turns these examples into a full test file.

---

## Worked example 3: a processing requirement

```python
# A processing requirement says what happens to input the stakeholder did not expect.
# R3: "If the age is not a whole number from 0 to 120, refuse it and say why."

def read_age(text):
    """Return (age, None) for a usable age, or (None, reason) for anything else."""
    try:
        age = int(text.strip())
    except ValueError:
        return None, f"'{text}' is not a whole number"
    if age < 0 or age > 120:
        return None, f"{age} is outside 0 to 120"
    return age, None


for typed in ["16", " 16 ", "sixteen", "-3", "16.5"]:
    print(repr(typed), "->", read_age(typed))
```

Output:

```
'16' -> (16, None)
' 16 ' -> (16, None)
'sixteen' -> (None, "'sixteen' is not a whole number")
'-3' -> (None, '-3 is outside 0 to 120')
'16.5' -> (None, "'16.5' is not a whole number")
```

Nobody in the interview said "what if somebody types sixteen." You asked, and the answer
became R3. **Every processing requirement you find in the interview is a crash or a silent
wrong answer you will not ship.**

---

## The wrong version, and what it does instead of an error

The stakeholder said "13 through 19." The developer wrote what felt natural.

```python
# The stakeholder said "13 through 19." The developer typed what felt natural.

def ticket_price(age):
    """Return the teen price for teens, adult price for everyone else."""
    if 13 < age < 19:
        return 6
    return 10


for age in [13, 16, 19]:
    print(f"age {age}: ${ticket_price(age)}")
```

Output:

```
age 13: $10
age 16: $6
age 19: $10
```

**No error. The program runs, looks right on the example everyone tries first (16), and
charges the adult price to every 13-year-old and every 19-year-old.**

"Through" means including both ends. `<` excludes them. The developer tested with 16, saw
`$6`, and moved on. This is Unit 2's boundary defect showing up again, and now it has a
cost: a requirement the stakeholder believes you met, and you did not.

The fix is not better attention. It is an acceptance criterion that names 13 and 19
explicitly, agreed before the code exists.

---

## Why the wrong version is tempting

**The requirement sounded clear.** "13 through 19" is plain English. Nobody thinks a plain
sentence needs a question.

**Everybody tests the middle.** 16 is the obvious teenager. Edges are where the defects are
and edges are the last thing anyone tries.

**Asking feels like admitting you did not understand.** In an interview it feels smarter to
nod. It is not. "When you say through, does that include 19?" is the question a
professional asks, and stakeholders trust people who ask it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Stakeholder** | The person the software is for, who decides whether it meets the need. |
| **Requirement** | What the program must do, in the stakeholder's terms. |
| **Acceptance criterion** | A concrete, checkable condition that shows one requirement is met. |
| **Given, When, Then** | A shape for criteria: the situation, the action, the exact result. |
| **Functional requirement** | What the program does. |
| **Processing requirement** | What the program does with input nobody planned for. |
| **Requirements specification** | The written, agreed set of requirements and criteria. |
| **Sign-off** | The stakeholder's written agreement that the specification is right. |
| **Active listening** | Restating, asking follow-ups, and attending fully before responding. |
| **Real need** | The problem underneath the first thing the stakeholder asked for. |

---

## Self-check

**Question 1.** Rewrite this requirement as two acceptance criteria in Given, When, Then
form: "The locker checkout should handle late returns."

**Question 2.** A stakeholder says "the report should be fast." Why is that not an
acceptance criterion, and what question would you ask to turn it into one?

**Question 3.** Predict the exact output. Then say which ages disagree with the requirement
"members aged 12 to 17 get the youth rate," and what the criterion should have named.

```python
def youth_rate(age):
    return 12 <= age < 17

for age in [11, 12, 16, 17]:
    print(age, youth_rate(age))
```

---

### Answers

**1.** Many answers work. What matters is a concrete situation, an action, and a result
anyone can check. For example:

- AC-1. Given a locker key checked out for 1 day and returned on day 2, when it is
  checked in, then the record is marked late by 1 day.
- AC-2. Given a key returned on the day it was due, when it is checked in, then the record
  is not marked late.

"Handles late returns well" is not a criterion, because nobody can run it.

**2.** "Fast" has no number and no situation, so two people would disagree about whether it
passed. Ask: "Fast with how much data, and how long is too long for you?" An answer like
"under two seconds for the whole year's log of about 2,000 rows" becomes a criterion.

**3.** Output:

```
11 False
12 True
16 True
17 False
```

Age 17 disagrees with the requirement. "12 to 17" most likely includes 17, and `< 17`
excludes it. The criterion should have named 12 and 17 explicitly as ages that get the
youth rate, and 11 and 18 as ages that do not, and confirmed with the stakeholder that
"to" includes 17.
