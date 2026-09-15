# Problem Drop #4
## 145060 Programming · Unit 7 · Week 17 · Friday, January 15

**75 minutes. Individual.** Full tooling. This is not a lab with steps. You get a real,
messy annoyance, and you decide what to build.

**What you may use:** everything through Unit 7. Classes, files and JSON, dictionaries and
lists, functions, error handling, input validation. You will not finish everything. You
have to choose.

---

## The situation

The library runs a cart of 30 laptops that students borrow during study hall and return by
the end of the period. The librarian is frustrated:

> Every single day I get students telling me the laptops are dead. Half the cart is
> useless by third period. I have asked for money for more chargers, and even for a whole
> second cart, but the answer is always no. I only need the laptops to be charged when
> students need them. Can you build something that tells me which laptops need charging so
> I can plug them in before the next class? That is all I want, a list of the dead ones.

The librarian hands you what they have: a text file, `cart_log.txt`, where students are
supposed to write their name and the laptop number when they take one and when they bring
it back. It is filled in by hand and it is a mess. Some lines have a return, some do not.
Some laptop numbers appear twice with no return in between.

You have the period. Build something that helps.

---

## What hurts

- Laptops are dead when students need them.
- The librarian cannot get money for more chargers or a second cart.
- The log is filled in by hand and is incomplete.
- The librarian asked for one specific thing: a list of the dead laptops.

**Notice that last point.** The librarian told you what to build. Part of this drop is
deciding whether that is actually the thing that would help.

---

## What to hand in

By the end of the period, commit and push:

1. **A short problem statement**, three or four sentences, in a file `PROBLEM.md`. Say
   what you think the real problem is, which may or may not be the one the librarian named.
2. **A working artifact.** A program that runs and does something useful with the log, even
   if it is small. It does not have to solve everything. It has to run and help.
3. **A `README.md`** with how to run it, a real sample run, and one thing it does not do
   that you would build next.

The `cart_log.txt` fixture is in `09-project/problem-drop-04-files/`. Copy it into your
repository.

---

## The rule about scope

**You cannot solve this completely in 75 minutes, and you are not supposed to.** A good
submission does one real thing well and is honest about what it left out. A submission that
tries to do everything and finishes nothing scores worse than a small thing that works.

---

## What your instructor will ask you

At some point while you work, your instructor will stop at your desk and ask you one
question. You will have 60 seconds to answer. Think about it while you build.

You will not be told the question in advance. It is about a tradeoff you made.

---

## Grading, 30 points

| Dimension | Points | What earns it |
|---|---|---|
| **Problem Identification** | 15 | You found the real problem under the stated one, and said so clearly. |
| **Working Artifact** | 10 | Something runs and does something useful with the real log. |
| **Tradeoff** | 5 | You can name a choice you made, what you gave up, and why, in 60 seconds. |

**The largest share is Problem Identification.** Building the exact thing the librarian
asked for, with no thought about whether it helps, earns the Working Artifact points and
little of the rest.
