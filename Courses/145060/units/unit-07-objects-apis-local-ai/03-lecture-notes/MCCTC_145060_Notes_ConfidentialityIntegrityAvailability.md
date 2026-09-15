# Lecture Notes: Confidentiality, Integrity, Availability
## 145060 Programming · Unit 7 · Week 18 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W18_CIA.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W18_CIA.pptx)

If you missed class, you can learn this concept from this file alone.

---

## Why this exists

You have found and fixed a pile of vulnerabilities. This lesson gives you the three words
that name what all of that protects. Confidentiality, integrity, and availability, called
CIA, are the standard way to say what security is for. When you can name which of the
three a problem breaks, you can talk about security clearly, prioritize honestly, and
answer the exam question. This is a named Ohio competency, 2.1.1.

---

## The concept in plain language

Security protects three things about information:

- **Confidentiality:** who can read it. Broken when someone sees what they should not.
- **Integrity:** whether it is true. Broken when data is changed or faked.
- **Availability:** whether it is there when you need it. Broken when a system is down,
  frozen, or too slow to use.

Every vulnerability breaks at least one of these. Naming which one tells you what you
lost. The order spells CIA, which is how everyone remembers it. The order is not a
ranking. Availability failures are often the most common of the three.

---

## Worked example 1: the three, mapped onto one program

Take the security review lab you finished. Three of its defects, one per letter:

```
Confidentiality  The moderator code and a key were written in the file and put
                 into the prompt. Anyone who read either could see them.

Integrity        The thank command accepted a negative number, so a member could
                 PULL points off another member. The saved file said something false.

Availability     The model call had no timeout, so a hung model froze the whole app
                 for everyone in the room until it was killed.
```

One codebase, all three letters. This is the pattern: a real program has ways to fail on
each of the three, and a review checks for all of them.

---

## Worked example 2: the same three in the projects you built

The text adventure and the API app protect all three on purpose:

```
Confidentiality  No key anywhere in the files. A local model needs none, so there
                 is nothing to leak. A test fails if the source contains "api_key".

Integrity        The keep-phrase check throws away a model reply that dropped a
                 needed fact, so the game never shows a false, unwinnable room.

Availability     Every model and API call has a timeout, and the game stops asking
                 after two failures, so a dead server never freezes the program.
```

The features you wrote were not only conveniences. Each one is protecting a letter of
CIA, whether you named it that way or not.

---

## Worked example 3: naming the letter for a new problem

Practice the move: given a problem, name the letter.

```
A stolen password that lets someone read private messages.   -> Confidentiality
A bug that lets a student change their own grade in a file.   -> Integrity
A denial-of-service attack that takes a website offline.      -> Availability
A tampered save file that says you have 999 lives.            -> Integrity
Verbose errors that print the database address to any user.   -> Confidentiality
A model call with no timeout that hangs the app.              -> Availability
```

The test for each: did someone read what they should not (C), did the data become false
(I), or is the thing not there when needed (A)? Some problems break more than one.
Ransomware that encrypts your files breaks availability and often confidentiality too.

---

## The wrong version, and why the mapping matters

A common mistake is to call everything that "feels bad" an integrity problem, or to call
every leak an integrity problem because a leak is bad. Watch:

```
"A leaked password is an integrity problem."     WRONG. It is confidentiality.
```

A leaked password did not change any data. It exposed it. Nothing became false; something
became readable. That is confidentiality. Getting the letter right is not pedantry. It
tells you what to fix and what you actually lost. A confidentiality fix (stop exposing
it) is different from an integrity fix (stop it being changed).

### Write this down

> Confidentiality is who can read it. Integrity is whether it is true. Availability is
> whether it is there.

---

## Why this framing is worth learning

Without CIA, security is a vague feeling that some code is "unsafe." With it, you can say
exactly what a problem threatens and how much it matters for this program. A game losing
availability for a second is minor. A gradebook losing integrity is serious. The same
vulnerability can matter a lot or a little depending on which letter it breaks and what
the program is for. That judgment is what a real review produces, and it is what the exam
asks you to show.

---

## Vocabulary

| Term | What it means |
|---|---|
| **CIA** | Confidentiality, Integrity, Availability. What security protects. |
| **Confidentiality** | Keeping information readable only to those allowed. |
| **Integrity** | Keeping information true and unchanged by the wrong people. |
| **Availability** | Keeping a system there and usable when needed. |
| **Denial of service** | An attack on availability, making a system unusable. |
| **Tampering** | Changing data without permission, an integrity attack. |

---

## Self-check

**Question 1.** Give the one-line meaning of each letter of CIA.

**Question 2.** Sort these into C, I, or A: a frozen app from a missing timeout; a leaked
key; a save file edited to add points; an error message printing the server address.

**Question 3.** Why is a leaked password a confidentiality problem and not an integrity
problem, even though it feels serious?

---

### Answers

**1.** Confidentiality: who can read it. Integrity: whether it is true. Availability:
whether it is there when you need it.

**2.** Frozen app from a missing timeout: **Availability**. Leaked key: **Confidentiality**.
Save file edited to add points: **Integrity**. Error printing the server address:
**Confidentiality**.

**3.** Because a leaked password exposes information without changing any data. Nothing
became false; something became readable by the wrong person, which is exactly
confidentiality. It feels serious because exposure can lead to worse attacks, but the
letter it breaks is C. An integrity problem would be data that got changed or faked.
