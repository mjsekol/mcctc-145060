# The Fair Workplace
---
## Slide 1: The script threw out the two best applicants
- A café owner wants to hire two students
- A cleanup script sorts the applications first
- The two highest scores never reach a person
- Nobody meant it. Nobody noticed.
Speaker notes: This scenario is a composite. A café owner loved a student team's scheduling tool and wants to hire two students for next summer. Before reading applications, the owner runs a small cleanup script a model suggested. The two strongest applicants in the pool never reach a human being. Nobody decided to do that and nobody noticed. Today is about the laws that shape hiring and work, and about how bias gets into decisions, including decisions made by code.
Image: A stack of application cards with two cards sliding off the side into shadow, navy and blue.
---
## Slide 2: I am not a lawyer, and this is not legal advice
- These laws explained at the level of purpose
- No wage amounts, hour limits, or cutoffs here
- Those change, and federal and Ohio can differ
- Look them up: U.S. Department of Labor
- Ohio Bureau of Wage and Hour Administration, and the EEOC
Speaker notes: Same rule as Unit 0. I am not a lawyer and this is not legal advice. I am going to tell you what these laws are for, so you can recognize when one applies. I am deliberately not giving you wage amounts or hour limits or age cutoffs, because they change and federal and Ohio rules can differ. When you need a number, you go to the source. The Department of Labor, Ohio's Bureau of Wage and Hour Administration, and the EEOC. That is the professional move.
Image: A simple bookshelf with three labeled binders, federal, Ohio, and EEOC, navy spines with blue labels.
---
## Slide 3: Pay, hours, and workers under 18
- FLSA: minimum wage, overtime, records, youth employment
- Younger teens: limits on hours and times of day
- Under 18: no jobs classified as hazardous
- Federal and Ohio both apply: follow the more protective rule
- Responsibility for youth rules falls on the employer
Speaker notes: The Fair Labor Standards Act is the federal law behind minimum wage, overtime, recordkeeping, and youth employment. Youth rules limit when and how much younger teens can work, especially on school days, and keep anyone under eighteen out of jobs the Department of Labor classifies as hazardous. Ohio has its own minor labor law too, and when both apply, the employer follows whichever protects the worker more. The café wants a sixteen year old closing at midnight and running a meat slicer. Those are exactly the details to look up before anyone is hired.
Image: A clock and a kitchen slicer icon side by side, each with a small magnifying glass over it, navy and blue.
---
## Slide 4: Discrimination, disability, and harassment
- EEOC enforces laws against discrimination and retaliation
- Race, color, religion, sex, national origin, disability
- Age 40 or older, and genetic information
- ADA: reasonable accommodations for qualified workers
- Harassment is discrimination when it becomes a job condition
Speaker notes: The EEOC is the federal agency that enforces laws against employment discrimination. Hiring, firing, pay, assignments, promotions, training. The protected characteristics are race, color, religion, sex including pregnancy, national origin, age forty or older, disability, and genetic information. Punishing someone for reporting discrimination is also illegal. The ADA requires reasonable accommodations for qualified people with disabilities unless it would cause undue hardship. And harassment based on those characteristics is illegal when enduring it becomes a condition of the job or it creates a hostile environment.
Image: A row of simple balanced scales in a line, navy outlines, one blue highlight.
---
## Slide 5: Fix the café's interview questions
- How old are you: ask which shifts they can work
- What church do you go to: ask about the schedule
- Any health problems: ask if they can do the duties
- Planning to have kids: delete it entirely
- Ask about the job, never the person's traits
Speaker notes: The owner drafted interview questions, and almost all of them ask about a protected characteristic. That creates legal risk, because those traits cannot be the basis of the decision, and asking suggests they were. So ask about the job. Instead of how old are you, this role closes at nine on Fridays, can you work that shift. Instead of health problems, the job means standing four hours and lifting boxes, can you do that with or without an accommodation. The pregnancy question has no job version. It goes.
Image: A two-column list, crossed-out questions on the left, rewritten job questions on the right, navy and blue.
---
## Slide 6: A structured interview
```python
questions = ["explains a bug clearly", "handles a rush calmly", "asks about the task"]
scores = {
    "Applicant 1": [4, 3, 5],
    "Applicant 2": [5, 4, 4],
    "Applicant 3": [3, 5, 3],
}
for applicant in scores:
    total = 0
    for score in scores[applicant]:
        total = total + score
    print(f"{applicant}: {total} of {len(questions) * 5}")
```
Speaker notes: One practice that reduces bias is a structured interview. Same job related questions for everybody, written before anyone applied, scored on the same scale. Look at the structure. How old are you has nowhere to fit in it. That is part of why it works. Affinity bias, liking people who seem like us, has less room when everyone answers the same questions and gets the same scoring.
Image: None. This slide is code.
---
## Slide 7: Watch this
```python
applicants = [
    {"name": "Maya Johnson", "sample_score": 8},
    {"name": "José Ramírez", "sample_score": 9},
    {"name": "Liam O'Connor", "sample_score": 6},
    {"name": "Zoë Adams", "sample_score": 9},
    {"name": "Dmitri Volkov", "sample_score": 7},
]
# "Remove records with corrupted characters in the name field."
clean = []
for person in applicants:
    if person["name"].isascii():
        clean.append(person)
print("Applicants reviewed:", len(clean), "of", len(applicants))
```
Speaker notes: Here is the cleanup step the model suggested. Every applicant is invented. Remove records with corrupted characters in the name. isascii is True only when every character is basic English. Predict the number before I run it, and then tell me whose applications are gone.
Image: None. This slide is code.
---
## Slide 8: Bias with no one deciding
```
Applicants reviewed: 3 of 5
```
Speaker notes: No error. Three of five. José and Zoë are gone, and they had the two highest scores in the pool. An accent is not corruption. It is an ordinary letter in millions of names. That is bias turning into a productivity cost, because the café hires weaker applicants, and into legal risk, because filtering people by traits tied to national origin is exactly what discrimination law is about. And nobody on a team of similar people would ever type José into a test.
Image: None. This slide is output.
---
## Slide 9: What a multicultural team catches
```python
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
typed = "03/04/2026"
first, second, year = typed.split("/")
print("Month first:", MONTHS[int(first) - 1], int(second), year)
print("Day first:  ", MONTHS[int(second) - 1], int(first), year)
```
Speaker notes: In the United States this date is March fourth. In much of the world it is April third. A team where everybody writes month first will never think to ask. The teammate who grew up writing day first catches it in two seconds. You have seen this before. title mangled O'Brien in Unit 1, and Unicode exists because English letters are not the only letters. Global products need teams that notice.
Image: None. This slide is code.
---
## Slide 10: Do diverse teams perform better
- For: more perspectives, more requirements, fewer blind spots
- For: global products need people who know other users
- Caution: diversity alone does not guarantee better results
- Caution: different norms can slow early decisions
- The benefit depends on whether every voice is heard
Speaker notes: People say diverse teams perform better, and this is genuinely argued, so here is the strongest case on each side. For: more perspectives surface more requirements and catch more blind spots, and a global product needs people who understand other users. For caution: diversity by itself guarantees nothing, and teams with different norms can have more misunderstandings early on. What decides it is inclusion, whether those perspectives actually reach the product. That is what Tuesday's decision rules are for.
Image: A balance scale with a group of varied figure outlines on one side and a speech bubble icon on the other.
---
## Slide 11: What you are about to build
- Build 1: Peer Code Review 2, on another team's change branch
- Merge only after the review, then tag v1.1
- Build 2: Problem Drop 3, on your own, 40 minutes
- Tonight is the banquet. Push before you leave.
Speaker notes: Build one is Peer Code Review two. You review another team's change branch against their v one point oh baseline before it touches main. Ask the change questions, especially what the change removed. After the review, merge and tag v one point one. Build two is Problem Drop three, individually, forty minutes. The stated problem is not the real problem, so read it twice. And tonight is the banquet, so push everything before you leave this room.
Image: A branch merging into a main line at a flag labeled v1.1, next to a small stopwatch, navy and blue.
---
