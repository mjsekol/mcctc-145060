# Lab U0-02: Infographic Autopsy
## 145060 Programming · Unit 0 · Week 2 · Monday, September 14

**Gate:** 2 (adversarial). **Duration:** two blocks, 35 and 40 minutes.
**Competencies:** PRIMARY 1.2.1 (extract relevant, valid information and cite
sources). LATENT 145130 2.14.4 (evaluate an AI result on validity, relevance,
authenticity, potential bias, hallucinations), 2.14.6 (critically analyze scenarios
involving AI usage).

---

## About this artifact, before you start

**The infographic below was constructed for this class.** It is not a real one
found circulating online. Every error in it was planted on purpose and every one of
them is checkable.

You are being told this because the alternative is worse. A real infographic gets
corrected or taken down, and thirty students picking apart a findable person's work
is a different exercise than the one intended here. What is real is the **shape**:
every error below is a mistake that generated content actually makes, presented the
way it actually gets presented, which is confidently and attractively.

Treat it as though you found it pinned to a wall.

---

## The scenario

Somebody in your school made a study guide with an AI assistant and posted it. It
looks good. It is laid out well, the tone is confident, and about half the people
who read it will believe all of it.

Your job is to be the person who checks.

## What you will build

A written autopsy: every defect you can find, quoted exactly, labeled with which of
the five criteria it fails, and where possible, proved with a command you ran.

---

## The five criteria

Every finding gets exactly one of these labels. Choosing the label is part of the
work.

| Criterion | The question it asks |
|---|---|
| **Validity** | Is it correct? A false claim about something real. |
| **Relevance** | Does it answer what was asked, or something else? |
| **Authenticity** | Is it original, or does it belong to somebody? |
| **Potential Bias** | Whose perspective is built in, and who is missing? |
| **Hallucinations** | Does it confidently describe something that does not exist? |

**The hardest call is Validity against Hallucinations,** and you will have to make
it more than once today.

- **Validity** is a wrong claim about a real thing. The thing exists; the statement
  about it is false.
- **Hallucination** invents the thing itself.

You can catch a validity failure by testing the real thing. You can only catch a
hallucination by going to look and finding nothing there.

---

# THE ARTIFACT

> ## PYTHON IN 60 SECONDS
> ### Everything a beginner needs to know, in one page
>
> ---
>
> **WHAT IS PYTHON?**
>
> Python is the world's easiest and fastest programming language. **97% of
> developers say Python is the simplest language to learn.** If you are starting
> out, Python is the correct choice for everyone.
>
> ---
>
> **VARIABLES**
>
> Every variable must be declared with the `var` keyword before you use it:
>
> ```python
> var hours = 5
> ```
>
> Once declared, the variable is locked to that type for the rest of the program.
>
> ---
>
> **PRINTING**
>
> The `print()` function displays text on screen. When you give it more than one
> value, it separates them with a comma:
>
> ```python
> print("Set", "Go")     # displays: Set,Go
> ```
>
> ---
>
> **GETTING INPUT**
>
> Use `input()` to ask the user a question. **If the user types digits, `input()`
> returns a number, so you can do math with it right away:**
>
> ```python
> age = input("Your age: ")
> print(age + 5)          # works fine
> ```
>
> ---
>
> **CONVERTING**
>
> `int()` converts anything to a whole number. It handles decimals by rounding
> down, so `int("11.5")` returns `11`.
>
> ---
>
> **USEFUL STRING METHODS**
>
> | Method | What it does |
> |---|---|
> | `.upper()` | Makes everything uppercase |
> | `.lower()` | Makes everything lowercase |
> | `.titlecase()` | Capitalizes the first letter of every word |
>
> ---
>
> **WHO USES PYTHON**
>
> Google. Meta. Netflix. Amazon. Microsoft. If you want to work at a real tech
> company, Python is what you need.
>
> ---
>
> **USING CODE YOU FIND**
>
> All Python code posted publicly online is free to copy and use in your own
> projects however you want. That is the whole point of open source.
>
> ---
>
> *Generated with AI. Share freely.*

---

# Your work

## Part 1 (35 minutes, individual)

Find defects. For each one, write an entry with all four parts:

1. **The exact claim, quoted.** Copy it word for word.
2. **Which criterion it fails.** One label per finding.
3. **Why it is wrong.** In your own words.
4. **How you know.** Best: a command you ran and what it printed. Acceptable: a
   documentation page you checked, named specifically. Not acceptable: "I could
   tell" or "it seems wrong."

**There are at least eight defects.** Six findings is a passing autopsy. Eight is
strong.

### Acceptance criteria, Part 1

1. At least six findings, each with all four parts
2. Each finding labeled with exactly one of the five criteria
3. At least three findings proved by a command you ran, with the output pasted
4. At least one finding labeled Hallucinations and one labeled Validity, and you
   can say why each is not the other

## Part 2 (40 minutes)

**First 10 minutes:** trade with one partner. Read theirs. Add anything they found
that you missed, **marked clearly as theirs.**

**Next 20 minutes:** write the summary section of your autopsy. It answers:

- Which defect would fool the most people, and why?
- Which criterion did you find hardest to apply, and what made it hard?
- One defect required you to go and look rather than reason from what you knew.
  Which one, and what did you have to do?
- If you had read this page a week ago, how many of these would you have caught?
  Answer honestly. Nobody is graded on the number.

**Last 10 minutes:** commit and push.

### Acceptance criteria, full lab

- [ ] Six or more findings with all four parts each
- [ ] Your partner's additions are present and marked as theirs
- [ ] At least three commands run and output pasted
- [ ] Summary answers all four questions
- [ ] Committed and pushed to your repository
- [ ] AI usage log entry if you used a model at any point today

---

## How to actually check things

You have a terminal. Use it. Most of the technical claims on this page can be
settled in under ten seconds.

To test a claim about a method, try it:

```
python -c "print('ava ruiz'.title())"
```

To test what a function returns, ask:

```
python -c "v = input(); print(type(v).__name__)"
```

**A claim you cannot test with a command needs a different kind of checking.** Some
of the defects on this page are not about Python at all, and no command will settle
them. Notice which ones, because that difference matters.

---

## If you get stuck

**"It all looks fine to me."** You are reading at the paragraph level. Read one
sentence at a time and ask of each: what would I have to do to prove this? If the
answer is "run one command," run it.

**"I found three and I am out."** Go section by section rather than skimming for
what feels wrong. There is at least one defect in most sections.

**"I cannot tell if this is Validity or Hallucination."** Ask whether the thing
being described exists at all. If it does not exist, it is a Hallucination. If it
exists and the sentence about it is false, it is Validity. Write down which one you
picked and why. Showing the reasoning earns the credit even if the label is wrong.

**"Two of these are not really about Python."** Correct. Keep going, and pay
attention to why those two are harder to prove than the rest.

---

## Submission checklist

- [ ] `autopsy.md` is in your repository
- [ ] Six or more findings, each with claim, criterion, why, and how you know
- [ ] Three or more pasted command outputs
- [ ] Partner additions marked
- [ ] Summary section complete
- [ ] Pushed
