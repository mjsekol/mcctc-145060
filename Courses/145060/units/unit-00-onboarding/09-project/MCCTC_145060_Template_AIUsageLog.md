# AI Usage Log · Template
## 145060 Programming · Use this for every project, starting Week 1

Copy this file into your repository as `ai-usage-log.md` and add to it as you work.
Do not write it at the end from memory. A log reconstructed afterward is a guess,
and it reads like one.

---

## Why this exists

Two reasons, and the second is the one that matters to you.

The first is the course policy: AI is permitted on Gate 2 and Gate 3 work and
prohibited on Gate 1 reps, and every project includes a log of what you asked, what
came back, and what you changed. That is in the syllabus and in the Lab Acceptable
Use and Safety Agreement you signed.

The second is that **the only way to fail outright in this course is to submit work
you cannot explain.** The log is how you avoid that, and it works because writing
down what you changed and why forces you to have actually changed something for a
reason. A student who keeps a real log cannot end up in front of a demo unable to
explain their own project. That is not a threat, it is the mechanism.

There is a third reason worth knowing. In your senior capstone you will have a
stakeholder who asks how something was built. "I do not remember" is an answer you
do not want to give to somebody outside this building.

---

## The rules

1. **Every model interaction that affected a submitted artifact gets an entry.**
   That includes commit messages, README wording, and error-message explanations.
   If it changed something you turned in, it goes in the log.

2. **No personal information goes into any AI tool.** No real names, no student
   data, no photographs, no grades, no addresses. Ever, on any assignment.

3. **Local models only.** Commercial developer APIs require users to be 18 or older,
   so this course uses locally hosted models on lab hardware. Record which one you
   used.

4. **Nothing goes in from a Gate 1 rep.** Gate 1 is closed. If a Gate 1 rep appears
   in this log, it is a violation, not a disclosure.

5. **"I used AI and changed nothing" is a legitimate entry.** It is also the entry
   that gets asked about at demo time, so be ready to explain the output you
   accepted. Accepting output is a decision and you own it.

---

## Entry format

Copy this block for each interaction.

```markdown
### Entry N · <date> · <artifact this affected>

**Model used:**

**What I asked:**

> paste the prompt exactly as you sent it

**What came back, in summary:**

**What I kept:**

**What I changed, and why:**

**How I verified it:**
```

**The last two fields are the graded ones.** "What I changed and why" and "How I
verified it" are where the thinking is. The first three fields are record keeping.

---

## Worked example

This is what a real entry looks like. Note that the student did not accept the
output as given, and note the verification step.

```markdown
### Entry 3 · September 10 2026 · README.md for event-card

**Model used:** local model on lab machine 7

**What I asked:**

> Write a README for a small Python program that prints the time, place, and what
> to bring for a club meeting. Keep it under 200 words.

**What came back, in summary:**

Four sections: a title, a description, an installation section, and a usage
section. The description was two sentences and read well. The installation section
told the reader to run `pip install -r requirements.txt`.

**What I kept:**

The four-section structure and the ordering. Also the phrase "no internet connection
required," which was better than what I had written.

**What I changed, and why:**

I deleted the entire installation section. My program has no dependencies and there
is no `requirements.txt` in my repository, so that instruction would fail for anyone
who tried it. I think it appeared because most Python projects have one, not because
anything about my project suggested it.

I also rewrote the first sentence. The model described it as "a utility for
displaying event information," which is true and tells a stranger nothing. I changed
it to name the actual club and the actual problem.

**How I verified it:**

I checked my folder and confirmed there is no `requirements.txt`. Then I followed my
own README from the top on a machine where I had not been working, and it ran.
```

That entry takes four minutes to write and it is the difference between explaining
your project and hoping nobody asks.

---

## What a weak entry looks like

```markdown
### Entry 1 · Sept 10 · README

**Model used:** the local one
**What I asked:** to write a readme
**What came back:** a readme
**What I kept:** all of it
**What I changed, and why:** nothing
**How I verified it:** it looked right
```

This entry is honest, which is worth something, and it is failing on the two fields
that matter. "It looked right" is not verification. Neither is "it ran," on its own,
for a README.

**If your entry looks like this, the problem is usually not the log.** It is that
you accepted output without checking it. The log did its job by showing you that.

---

## Where this gets graded

Under **Written & Documentation**, 20 percent of your course grade, and inside the
**Process** dimension of the 100-point project rubric.

When your log is evaluated against the Ohio AI output standard, these five are the
criteria, and they are the same five used in every AI evaluation in this program:

| Criterion | The question it asks |
|---|---|
| **Validity** | Is the output actually correct? |
| **Relevance** | Does it address what was asked, or something adjacent? |
| **Authenticity** | Is it original, or reproduced from somewhere with an owner? |
| **Potential Bias** | Whose perspective is baked in, and who is left out? |
| **Hallucinations** | Does it confidently state things that are not true? |

The `requirements.txt` in the worked example above is a hallucination. It is
specific, correctly formatted, plausible, and refers to a file that does not exist.
That is the most common form the failure takes, and it is why the verification field
is required.
