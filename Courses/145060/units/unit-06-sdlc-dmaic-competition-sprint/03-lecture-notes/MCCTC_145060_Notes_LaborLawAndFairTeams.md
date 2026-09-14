# Lecture Notes: The Fair Workplace: Labor Law, Bias, and Multicultural Teams
## 145060 Programming · Unit 6 · Week 15 · Thursday, December 17

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W15_FairWorkplace.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W15_FairWorkplace.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every example.

**Competencies:** 1.3.7 (identify the labor laws that affect employment and the consequences of
noncompliance for both employee and employer), 1.5.5 (how bias and discrimination influence
productivity and profitability), 1.5.8 (how multicultural teaming and globalization foster new and
improved products).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** It explains what these laws
are for, at the level of the competency, so you can recognize when they apply. It deliberately does
**not** state wage amounts, hour limits, age cutoffs for specific jobs, or employer size thresholds.
Those numbers change, some differ between federal and Ohio law, and a wrong number in a lesson is
worse than no number.

When you need a number, or when a real situation affects you or someone you know, go to the source
that governs it. That is the correct professional response, and it is the same one Unit 0 modeled
for copyright:

- **U.S. Department of Labor, Wage and Hour Division**, for federal minimum wage, overtime, and youth
  employment rules. Its youth employment information is at
  `https://www.dol.gov/agencies/whd/youthrules` **[VERIFY]**, which loaded when this lesson was
  written. Check it again before class, because government pages move.
- **Ohio Bureau of Wage and Hour Administration**, for Ohio's minimum wage and minor labor rules. Find
  it through the State of Ohio's official website, `https://ohio.gov` **[VERIFY]**, and confirm you are on
  a `.gov` page.
- **U.S. Equal Employment Opportunity Commission**, `https://www.eeoc.gov` **[VERIFY]**, for
  discrimination, harassment, and the ADA in employment.

---

## Why this exists

Your sprint team is a small workplace. It has roles, deadlines, a stakeholder, and people who have to
work together whether or not they would have picked each other.

Many of you already have part-time jobs, and more of you will soon. Some of you will be hired, and some
day some of you will do the hiring. Every one of those situations is shaped by laws that exist because
people were once treated badly at work, and by biases that nobody chooses and everyone has.

There is a programming reason too. Software makes hiring and scheduling decisions at scale now. A
biased rule typed into a screening script does not affect one applicant. It affects every applicant, the
same way, silently.

---

## A composite scenario for the whole lesson

*This scenario is a composite, invented for this lesson. The café and the people in it are not real.*

A team built a scheduling tool for a small neighborhood café. The owner loves it and wants to hire two
students part-time for next summer: one to keep the tool running, one to work the counter and the
kitchen. The owner asks your team to help write the job posting, the interview questions, and a small
script to sort the applications.

Here is what the owner drafted:

> **Posting.** Looking for young, energetic students, ages 16 to 20. Must be a native English speaker.
> Kitchen helper will run the meat slicer.
>
> **Interview questions.** How old are you? What church do you go to? Do you have any health problems?
> Are you planning to have kids soon? Can you close at midnight on school nights?

Almost every line of that draft touches a law in this lesson. Keep it in mind as you read.

---

## The laws, at the level of the competency

### Fair Labor Standards Act (FLSA)

A federal law that sets standards for **minimum wage, overtime pay, recordkeeping, and youth
employment** for many jobs in the United States. It is enforced by the U.S. Department of Labor's
Wage and Hour Division.

### Minor labor laws

Laws that protect workers under 18. Under federal youth employment rules, **younger teens have limits on
how many hours and at what times of day they may work, especially on school days, and workers under 18
may not do jobs the Department of Labor classifies as hazardous.** Ohio has its own minor labor law as
well.

When federal and state rules both apply, **the employer must follow whichever rule protects the worker
more.** That is why "look it up" means checking both.

In the café scenario: closing at midnight on school nights and running a commercial slicer are exactly
the kind of details to check against the youth employment rules before anyone is hired. Look up the
current limits for the applicant's age. Do not guess.

### Equal Employment Opportunity Commission (EEOC)

The federal agency that enforces federal laws making it illegal to discriminate against a job applicant
or employee because of **race, color, religion, sex (including pregnancy), national origin, age (40 or
older), disability, or genetic information.** It is also illegal to retaliate against someone who
complains about discrimination or takes part in an investigation. These laws cover hiring, firing, pay,
job assignments, promotions, training, and harassment. Which employers they cover depends on things like
the employer's size, which is one of the details to look up.

### Americans with Disabilities Act (ADA)

A federal law that, in employment, prohibits discrimination against qualified people with disabilities
and requires employers to provide **reasonable accommodations** so a qualified person can do the job,
unless the accommodation would cause the employer undue hardship.

### Harassment

Harassment based on a protected characteristic is a form of discrimination. It becomes illegal when
putting up with it becomes a condition of keeping the job, or when it is severe or pervasive enough to
create a work environment a reasonable person would find hostile or abusive. Employers are expected to
prevent it and to act when it is reported.

### Interviews and testing

- **Interview questions about protected characteristics create legal risk.** Age, religion, disability,
  national origin, and pregnancy plans cannot lawfully be the basis of a hiring decision, and asking about
  them suggests they were. Ask about the job instead: "This role closes at 9 on Fridays. Can you work
  that shift?"
- **Pre-employment tests should measure what the job really requires.** A test or screening rule that
  filters out a protected group, and is not truly needed for the job, can be discriminatory even if nobody
  meant it to be.

### Consequences of noncompliance, for both sides

| For the employer | For the employee |
|---|---|
| Government investigations | A worker who harasses others can be disciplined or fired |
| Back pay owed to workers who were underpaid | Lying about age or eligibility on an application can cost the job |
| Fines and civil penalties | A minor working prohibited hours or hazardous jobs risks injury, and the job can end |
| Lawsuits and damages | Workers who report violations are protected from retaliation, which matters if you ever need to report one |
| Being ordered to change hiring or pay practices | |
| Losing good workers and a damaged reputation | |

For youth employment rules in particular, **the legal responsibility to follow them falls on the
employer**, which is one reason a careful employer checks age and schedules before the first shift.

---

## Bias, productivity, and profitability

**Bias** is a tendency to favor or disfavor people based on something other than the job. Much of it is
unconscious. A common kind in hiring is **affinity bias**: preferring people who seem like us, who went
where we went, who talk the way we talk.

Bias costs a business in ways you can name without any statistics:

- **Lost talent.** The best applicant is filtered out and hired by a competitor.
- **Lost ideas.** A team member who is interrupted or ignored stops contributing, and the team loses what
  they knew.
- **Turnover.** People leave workplaces where they are treated unfairly, and replacing them costs time and
  money.
- **Products that fail customers.** A team that shares one set of assumptions builds for itself and misses
  the people who are not like it.
- **Legal costs,** when bias becomes discrimination.

Two practices reduce bias in hiring, and both are small enough to try on your own team: a **structured
interview** with the same job-related questions and the same scoring for everyone, and a **blind first
review** that removes information the job does not need.

---

## Multicultural teams and globalization

Software is used across the world, and it is built by teams spread across countries and time zones. A
team whose members grew up with different languages, date formats, names, and customs catches assumptions
that a team of similar people never notices, because to them the assumption is not an assumption.

You have already met examples. `.title()` in Unit 1 mangled names like `O'Brien` and `van der Berg`.
Unicode in Week 4 exists because English letters are not the only letters. Last week's written stand-ups
were a small version of how distributed global teams work across time zones.

### A question with more than one strong side

People often say "diverse teams perform better." Here is the strongest case on each side, because this is
genuinely argued.

**The strongest case for:** a team with more perspectives surfaces more requirements, catches more blind
spots in testing, and understands more customers. For global products that is not a bonus. It is the job.

**The strongest case for caution:** diversity by itself does not guarantee better results. Teams whose
members have different norms can have more misunderstandings and slower decisions at first. Whether
different perspectives actually improve the product depends on whether those perspectives are heard,
which is an inclusion question, not a headcount question.

**Where that leaves you:** the benefit is real when the team's process lets every member's knowledge reach
the product. That is what Tuesday's decision rules and today's structured practices are for.

---

## Worked example 1: one date, two readings

```python
# One date, two readings. A teammate who grew up writing day/month catches it.
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

typed = "03/04/2026"
first, second, year = typed.split("/")

print("Month first:", MONTHS[int(first) - 1], int(second), year)
print("Day first:  ", MONTHS[int(second) - 1], int(first), year)
```

Output:

```
Month first: Mar 4 2026
Day first:   Apr 3 2026
```

In the United States this is March 4. In much of the world it is April 3. A team where everyone writes
month first will never think to ask. A requirement like "dates must be written YYYY-MM-DD" often comes from
the teammate who noticed.

---

## Worked example 2: a structured interview

```python
# A structured interview: same questions, same scale, for every applicant.
# Scores are about the job, and the questions were written before anyone applied.
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

Output:

```
Applicant 1: 12 of 15
Applicant 2: 13 of 15
Applicant 3: 11 of 15
```

Every question is about the job. Every applicant is scored the same way. **"How old are you" and "what
church do you go to" have nowhere to fit in this structure,** which is part of why structure helps.

---

## Worked example 3: a blind first review

```python
# Blind the first review: keep only the fields the job actually needs.
JOB_FIELDS = ["availability", "sample_score"]

application = {
    "name": "Zoë Adams",
    "birth_year": 2009,
    "home_language": "English and French",
    "availability": "weekends",
    "sample_score": 9,
}

reviewed = {}
for field in JOB_FIELDS:
    reviewed[field] = application[field]

print("Reviewer sees:", reviewed)
```

Output:

```
Reviewer sees: {'availability': 'weekends', 'sample_score': 9}
```

The applicant is invented. The reviewer cannot be influenced by a name, an age, or a home language, because
the reviewer never sees them in the first pass. This is also data minimization: a program that never
touches information it does not need cannot leak it or misuse it.

---

## The wrong version, and what it does instead of an error

The owner asks a model for a "cleanup step" before reviewing applications. It suggests removing records
with "corrupted characters" in the name. Every applicant below is invented.

```python
# screen.py: an AI-suggested "cleanup" step before the café reviews applications.
# Invented applicants. Every name here is made up.
applicants = [
    {"name": "Maya Johnson", "availability": "weekends", "sample_score": 8},
    {"name": "José Ramírez", "availability": "weekends", "sample_score": 9},
    {"name": "Liam O'Connor", "availability": "evenings", "sample_score": 6},
    {"name": "Zoë Adams", "availability": "weekends", "sample_score": 9},
    {"name": "Dmitri Volkov", "availability": "weekends", "sample_score": 7},
]

# "Remove records with corrupted characters in the name field."
clean = []
for person in applicants:
    if person["name"].isascii():
        clean.append(person)

print("Applicants reviewed:", len(clean), "of", len(applicants))
for person in clean:
    print(" ", person["name"], person["sample_score"])
```

Output:

```
Applicants reviewed: 3 of 5
  Maya Johnson 8
  Liam O'Connor 6
  Dmitri Volkov 7
```

**No error. The two highest scores in the pool, both 9s, never reach a human.**

`.isascii()` is `True` only when every character is in the basic English character set. `é` and `ë` are
ordinary letters in millions of names, and the filter treated them as corruption. Nobody intended to
screen out applicants by the language of their name. The script did it anyway, to every applicant with an
accent, every time, silently.

That is bias becoming a **productivity** cost, because the café hires weaker applicants, and a **legal**
risk, because a rule that filters people by characteristics tied to national origin is the kind of
practice discrimination law is concerned with. It is also a Gate 2 defect you would recognize: a Security
and Correctness problem wearing a data-cleaning costume.

---

## Why the wrong version is tempting

**It sounds technical and neutral.** "Corrupted characters" sounds like a data problem, not a people
problem. Bias in code rarely announces itself.

**The output looks reasonable.** Three applicants, real-looking names, real scores. Nothing on the screen
says "two people were removed for their names."

**The people it hurts are not in the room.** Nobody on a similar team would type `José` into a test, so
nobody would see it fail. **This is exactly where a multicultural team, or a test fixture with varied
names, pays for itself.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **FLSA** | Federal law setting minimum wage, overtime, recordkeeping, and youth employment standards. |
| **Minor labor laws** | Federal and state rules protecting workers under 18, including hour limits and hazardous job bans. |
| **EEOC** | Federal agency enforcing laws against employment discrimination and retaliation. |
| **ADA** | Federal law protecting qualified people with disabilities, including reasonable accommodations at work. |
| **Protected characteristic** | A trait such as race, religion, sex, national origin, age 40 or older, or disability that employment decisions may not be based on. |
| **Harassment** | Unwelcome conduct based on a protected characteristic, illegal when it becomes a job condition or creates a hostile environment. |
| **Retaliation** | Punishing someone for reporting discrimination or taking part in an investigation. Also illegal. |
| **Reasonable accommodation** | A change that lets a qualified person with a disability do the job. |
| **Bias** | Favoring or disfavoring people based on something other than the job. Often unconscious. |
| **Affinity bias** | Preferring people who seem similar to you. |
| **Structured interview** | Same job-related questions, same scoring, for every applicant. |
| **Multicultural team** | A team whose members bring different cultural backgrounds, languages, and norms. |
| **Globalization** | Products, companies, and teams operating across many countries. |

---

## Self-check

**Question 1.** Rewrite two of the café owner's interview questions so they ask about the job instead of a
protected characteristic, and name which law or agency each original question relates to.

**Question 2.** The café owner wants a 16-year-old to run the meat slicer and close at midnight on school
nights. Without stating any numbers, explain what the owner must check, where they would look, and who
bears the legal responsibility if the rules are broken.

**Question 3.** Predict the exact output, then explain in one sentence the business cost of this filter.

```python
applicants = ["Ana Lucía Ortiz", "Ben Carter", "Chloé Martin", "Sam Lee"]
kept = []
for name in applicants:
    if name.isascii():
        kept.append(name)
print(len(kept), kept)
```

---

### Answers

**1.** Many answers work. Examples:

- "How old are you?" relates to age discrimination rules enforced by the EEOC, and for minors it is often
  asked because of youth employment rules. Better: "This job has shifts that end at 9 p.m. and uses kitchen
  equipment. We will confirm with each hire that the schedule and duties follow the rules for their age.
  Which of these shifts can you work?" Checking that a hire meets the age rules for a job is legitimate.
  Do it the same way for every applicant, and look up the Department of Labor and EEOC guidance on how,
  rather than guessing.
- "What church do you go to?" relates to religious discrimination, enforced by the EEOC. Better: "This role
  works Saturday and Sunday mornings. Can you work that schedule?" If a religious practice affects the
  schedule, that becomes an accommodation conversation.
- "Do you have any health problems?" relates to the ADA. Better: "The counter job involves standing for a
  four-hour shift and lifting boxes. Can you perform those duties, with or without an accommodation?"

**2.** The owner must check the youth employment rules for the applicant's age: whether that equipment is
classified as hazardous for workers under 18, and what hours and times of day a worker that age may work on
school days. They would check the U.S. Department of Labor's youth employment rules and Ohio's minor labor
rules, and follow whichever protects the worker more. The legal responsibility for following youth
employment rules falls on the **employer**.

**3.** Output:

```
2 ['Ben Carter', 'Sam Lee']
```

Half the applicants are removed because their names contain `í` and `é`, so the café may lose its best
candidates to a competitor and take on legal risk, all without anyone deciding to do that.
