# Lecture Notes: Judging AI Output You Cannot Run
## 145060 Programming · Unit 0 · Week 2 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W02_JudgingAIOutput.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W02_JudgingAIOutput.pptx)

If you missed class, you can learn this concept from this file alone. Keep a terminal
open. Several of the checks below take eight seconds, and doing them is the lesson.

---

## Why this exists

Last week, Python was a referee. Your program either ran or it did not, and the
traceback told you where. You could not argue with it.

An AI assistant gives you paragraphs, explanations, diagrams, and code comments. None
of those crash. A wrong explanation and a right one look identical on the screen, and
both sound sure of themselves. **The confident tone is produced by the same process as
the content**, so it tells you nothing about whether the content is true.

That means you need a different way to check. Not a feeling that something "seems
legit," but a set of specific questions you ask on purpose.

---

## The concept in plain language

The Ohio standard for this (145130 competency 2.14.4) names five criteria. Treat them
as five separate questions.

| Criterion | The question you ask | What it catches |
|---|---|---|
| **Validity** | Is this claim actually correct? | False statements about real things |
| **Relevance** | Does it answer what I asked? | Fluent answers to a different question |
| **Authenticity** | Is it original, or does it belong to somebody? | Copied work, licensing problems |
| **Potential Bias** | Whose view is built in, and who is missing? | Whole groups left out or assumed away |
| **Hallucinations** | Does the thing it describes exist at all? | Invented methods, files, sources |

### The distinction that matters most

**Validity** and **Hallucinations** are the two you will confuse, so learn the line
between them now.

- A **validity** failure is a false claim about **something real**. The thing exists.
  The sentence about it is wrong.
- A **hallucination** is a confident description of **something that does not exist**.

You check them differently. A validity failure you can usually test by running the
real thing. A hallucination you can only catch by going to look and finding nothing
there.

---

## Worked example 1: does the method exist?

An assistant tells you: *"Use `.titlecase()` to capitalize every word in a name."*

Do not argue with it. Ask Python.

```python
print(hasattr("ava ruiz", "title"))
print(hasattr("ava ruiz", "titlecase"))
print("title" in dir(str))
```

Output:

```
True
False
True
```

`hasattr()` asks whether a value has a method with that name. `.title()` exists.
`.titlecase()` does not. **That was a hallucination**: a well-named, sensible-sounding
method that is not real.

---

## Worked example 2: is the claim about a real thing correct?

An assistant tells you: *"`sort()` returns a new sorted list."*

`sort()` is real, so this is not a hallucination. Test the claim.

```python
nums = [3, 1, 2]
result = nums.sort()
print("sort() returned:", result)
print("list is now:", nums)
print("sorted() returns:", sorted([3, 1, 2]))
```

Output:

```
sort() returned: None
list is now: [1, 2, 3]
sorted() returns: [1, 2, 3]
```

`sort()` returns `None` and changes the list in place. The function that returns a
new sorted list is `sorted()`. **That was a validity failure**: a real method, a false
sentence about it.

You have not been taught lists yet. You do not need to understand them to run this
check, and that is the point. **You can verify a claim you do not fully understand**,
as long as the claim is about something you can run.

---

## Worked example 3: a claim you already know how to check

An assistant writes: *"When you give `print()` more than one value, it separates them
with a comma."*

```python
print("Set", "Go")
```

Output:

```
Set Go
```

A space, not a comma. You met this in Week 1. **Validity failure**, and one you could
have caught from memory.

---

## Claims no command can settle

Two of the five criteria do not have a terminal test.

**Potential Bias.** An infographic lists five large tech companies under "who uses
Python" and says "if you want to work at a real tech company, Python is what you
need." Nothing there is technically false. What is wrong is what it leaves out:
hospitals, county government, manufacturers, and small businesses all write software,
and "real tech company" quietly defines their work as not real. You catch this by
asking who is missing, not by running code.

**Authenticity.** A study guide says "all Python code posted online is free to copy
however you want." You check that by reading licenses, which is tomorrow's lesson.

**A statistic with no source is its own problem.** "97 percent of developers say Python
is the simplest language to learn." Who was surveyed, how many, when, and where can you read it?
If all four answers are nothing, you do not have weak evidence. **You have no evidence
with a number attached to it.**

---

## The wrong version, and the exact error

You trust the assistant and put its suggestion straight into your program:

```python
name = "ava ruiz"
print(name.titlecase())
```

```
AttributeError: 'str' object has no attribute 'titlecase'
```

This one at least crashes, so you find out. **The dangerous version is the validity
failure that does not crash.** If you trusted "`sort()` returns a sorted list" and
wrote `result = nums.sort()`, your program would run, `result` would be `None`, and
you would find out three screens later when something printed `None` where a list
should be.

---

## Why the wrong version is tempting

**Fluency looks like knowledge.** In people, confident, organized, well-worded answers
usually come from someone who knows. That shortcut has served you your whole life, and
it does not transfer.

**It is usually right.** Most of what an assistant says about Python is correct, so
spot-checking one or two things and accepting the rest feels reasonable. The errors
hide inside the correct parts, which is exactly why they get through.

**Checking feels slower than it is.** Every check on this page took under ten seconds.
Rewriting a program built on a false claim takes an afternoon.

---

## What this does not mean

It does not mean AI tools are useless. It means **a claim you have not checked is not
something you know.** The course rule that the only way to fail is submitting work you
cannot explain applies directly: if you cannot evaluate an answer, you cannot explain
it, so you cannot submit it.

Both extremes are wrong. Accepting everything is wrong. Refusing to use the tool at all
is also wrong, and it leaves you slower than people who learned to check.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Validity** | Whether a claim about a real thing is correct. |
| **Relevance** | Whether the answer addresses what was actually asked. |
| **Authenticity** | Whether content is original or belongs to somebody. |
| **Potential bias** | Perspectives built in, and groups left out. |
| **Hallucination** | A confident description of something that does not exist. |
| **`hasattr(value, name)`** | Asks whether a value has a method or attribute with that name. |
| **`dir(type)`** | Lists everything a type provides. |
| **Primary source** | The original, such as official documentation, rather than a summary of it. |
| **Verification** | Checking a claim against something that cannot be wrong in the same way. |

---

## Self-check

**1.** An assistant says: *"Python strings have a `.reverse()` method."* Write one line
of Python that settles whether this is true, and say which criterion it tests.

**2.** An assistant says: *"`len()` counts the words in a string."* The function is
real. Which criterion does this claim fail if it is wrong, and how would you check it?

**3.** A guide says: *"Nearly every professional programmer uses Python."* No command
settles this. Name the criterion it most fails and the question you would ask.

---

### Answers

**1.** `print(hasattr("hello", "reverse"))` prints `False`. Strings have no
`.reverse()` method. If the claim is wrong, it is a **hallucination**, because the
method does not exist. (Reversing a string is done with slicing, `"hello"[::-1]`,
which is a later lesson.)

**2.** **Validity**, because `len()` is real and the claim is about what it does. Check
it by running `print(len("hi there"))`. It prints `8`, the number of characters
including the space, not `2` words. The claim is false.

**3.** It fails **Validity** as an unsupported claim, and it has a **Potential Bias**
problem because "professional programmer" is being defined narrowly. The question to
ask is: according to whom, measured how, and who counts as a professional programmer
in that survey? If there is no source, there is no evidence.
