# Lecture Notes: Who Owns the Code, and What You May Do With It
## 145060 Programming · Unit 0 · Week 2 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W02_OwnershipAndLicensing.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W02_OwnershipAndLicensing.pptx)

If you missed class, you can learn this concept from this file alone.

**An honest warning before you start.** Part of today's topic is genuinely unsettled
law. Nobody in this building is a lawyer, and nothing here is legal advice. What this
file gives you is the part that is **not** unsettled: which documents govern your
situation, and how to read them.

---

## Why this exists

In October some of you submit to the Congressional App Challenge. In senior year you
build a capstone for somebody outside this school. A submission is not only code. It
is a claim that the work is yours and that you are allowed to use everything in it.

Between now and then you will use AI tools, because this course asks you to, and you
will find code online that does what you need. **Each of those comes with conditions,
and the conditions are written down.**

---

## The concept in plain language

Three documents decide what you may do. Read them in this order.

1. **The terms of service of the AI tool you used.** Different tools say different
   things about who owns what they produce and what you may do with it. The version
   that applies is the one in force when you used the tool.
2. **The license on any code you included.** Open-source licenses are not contested.
   They impose real obligations, and they differ from each other.
3. **The rules of whoever receives your work.** A competition, a class, a client. This
   one governs in practice, because they are the ones judging you.

**Whatever the law eventually says, you will be judged by somebody who already wrote
down what they expect.** Read what they wrote.

### The three licenses you will meet most

| License | In one sentence | What it asks of you |
|---|---|---|
| **MIT** | Use it for almost anything. | Keep the copyright and license notice with the code. |
| **Apache 2.0** | Use it for almost anything, with patent terms. | Keep the notice, state significant changes, and respect its patent clause. |
| **GPL** | Use it, and share alike. | If you distribute a program that includes it, you must make your own source available under the GPL too. |

**No license at all does not mean free.** Code posted publicly with no license means
nobody granted you permission. Visible is not the same as permitted.

For precise comparisons, `https://choosealicense.com/` is maintained by GitHub and
written in plain language. Read the actual license text before shipping anything.

---

## Worked example 1: find the license in a project

Every project on GitHub that grants permission has a license file at the top level,
usually named `LICENSE`. You can read its first line the same way you read any file:

```python
f = open("LICENSE")
print(repr(f.readline().strip()))
f.close()
```

With a typical MIT license file, output:

```
'MIT License'
```

Eight seconds, and you know which set of obligations applies.

---

## Worked example 2: the license can be inside the code file

Many projects mark each source file with a short standard tag near the top:

```python
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Example Contributors
"""A tiny helper module somebody shared online."""

def shout(text):
    return text.upper()
```

Read the first line and check for the license name:

```python
f = open("sample_module.py")
first = f.readline()
f.close()
print(repr(first))
print("MIT" in first)
```

Output:

```
'# SPDX-License-Identifier: MIT\n'
True
```

`SPDX-License-Identifier` is a standard way of labeling a file's license so tools and
people can find it quickly. If you copy a file with this line, **you keep the line.**

---

## Worked example 3: the check that comes back empty

You found code you want. You look for the license:

```python
f = open("LICENSE_missing")
```

```
FileNotFoundError: [Errno 2] No such file or directory: 'LICENSE_missing'
```

No license file, and no tag in the source. **That is not permission. That is the
absence of permission.** The safe reading is that you may not use it. Write your own,
or find a project that does grant permission.

---

## The contested question, presented as contested

> **Does the person who wrote the prompt own what the AI produced?**

**The strongest case that they do.** They chose the problem, wrote the input, judged
the result, revised it, and put it into their own work. That is authorship in the
ordinary sense, and the tool is a tool, the way a camera is.

**The strongest case that they do not.** The output was assembled from patterns in
other people's work, and those people did not agree to it. The prompt writer supplied
a sentence and the system supplied the rest. Pressing a button that produces a
thousand lines is not self-evidently the same act as writing a thousand lines.

**Nobody in this room can settle this, and the law is still being written.** What is
settled is the course rule, and it holds whichever way the law goes: **log what you
used and what you changed, and be able to explain every line you submit.**

---

## The wrong version

A study guide claims:

> "All Python code posted publicly online is free to copy and use in your own projects
> however you want. That is the whole point of open source."

**Every part of that is wrong.** Public is not permitted. Code with no license grants
nothing. Open-source code comes with a license, and the license is the whole point of
open source: it states the permission and its conditions. A GPL project copied into a
program you distribute brings real obligations with it.

---

## Why the wrong version is tempting

**You can see it, so it feels available.** Everything else you find online, videos,
images, answers, you can view for free, and the jump from "I can view it" to "I can
use it" feels natural. It is not how licensing works.

**Nobody seems to get in trouble.** Most copying is never noticed. The cost shows up
later and unevenly: a disqualified competition entry, a takedown, a client who cannot
use what you built.

**The honest answer is "it depends,"** and that is unsatisfying, so people reach for a
simple rule. The simple rule that is actually safe is the opposite one: **no license
found means no permission given.**

---

## Vocabulary

| Term | What it means |
|---|---|
| **Terms of service** | The conditions a tool's provider sets for using it. |
| **License** | The document granting permission to use code, and its conditions. |
| **Open source** | Code published under a license that permits use and modification. |
| **MIT** | A permissive license. Keep the notice. |
| **Apache 2.0** | A permissive license with patent terms. |
| **GPL** | A copyleft license. Share alike when you distribute. |
| **Copyleft** | Licensing that requires derived work to carry the same license. |
| **SPDX identifier** | A standard short label for a license inside a file. |
| **Intellectual property** | Creations the law protects: copyright, patent, trademark, trade secret. |
| **Attribution** | Crediting the source you used. |

---

## Self-check

**1.** You find a helpful function in a public repository with no `LICENSE` file and no
license tag in the source. May you copy it into your Congressional App Challenge
entry? Explain in two sentences.

**2.** You use an MIT-licensed file in your project. What is the one thing the MIT
license requires you to keep?

**3.** Your teammate says the AI-written half of your project is "definitely yours
because you wrote the prompt." Give the strongest argument against that position in
two sentences, and then state the course rule that applies regardless.

---

### Answers

**1.** No, not safely. A public repository with no license grants no permission to use
the code, so copying it means using work you were never given the right to use, and a
competition that requires original work may disqualify the entry.

**2.** The copyright notice and the license text must stay with the code.

**3.** The output was assembled from patterns in other people's work, and writing a
prompt is not self-evidently the same act as writing the code, so authorship is at
least contested. Regardless of how that is settled, the course rule applies: log what
you used and what you changed, and be able to explain every line you submit.
