# Problem Drop #3
## 145060 Programming · Unit 6 · Week 14, Thursday · Build 2

**40 minutes. Individual. Gate 3:** full tooling, AI allowed with a usage log entry.
**30 points,** Lab & Practice.

**Files:** `09-project/problem-drop-03-files/participants.csv`, `last_year.csv`, and `this_year_draft.csv`.

---

## How a problem drop works

Nobody is going to tell you what to build. You get a real situation from a real kind of person,
written the way people actually describe their problems: out of order, with some opinions mixed in,
and with the thing they ask for not quite matching the thing that hurts.

You have 40 minutes. You cannot solve all of it. **Deciding what to solve is part of the grade.**

Your instructor will stop by in the last 15 minutes and ask you one question about a choice you made.
It takes about a minute.

This one should feel familiar. You spent three weeks learning that the first ask is rarely the real need.

---

## The situation

This is a message Marisol sent to a cousin who "is taking a programming class." Marisol and her
family are a composite, invented for this drop.

> ok so our family gift exchange is a disaster every single year and I need help
>
> My mom runs it. Everybody calls her Aunt Rosa, even me at this point. Everybody's name goes in a
> bowl and everybody draws one. Every year
> somebody draws their own name and we have to redo it. Last year we redid it THREE times, and by the
> third time everybody had seen who got who the first two times, so the whole secret part was ruined.
>
> Also Kayla and Brandon are brother and sister and live in the same house, and last year Kayla drew
> Brandon. Which is pointless, their parents buy their stuff anyway. My mom says that's allowed. Grandpa
> Joe says it's not. And Uncle Dev drew Theo two years in a row and Theo said it was rigged, as a joke,
> except not really a joke.
>
> My mom already did this year's drawing in a spreadsheet so she wouldn't have to use the bowl. I put
> it in the files. I think something is wrong with it but I honestly can't tell who is allowed to have
> who, so I can't prove it.
>
> The party is Saturday. Can you make something that does the drawing actually random so nobody can
> say it's rigged??

The files, as Marisol sent them:

`participants.csv`, where a household letter means those people live together:

```
name,household
Aunt Rosa,A
Uncle Dev,A
Marisol,A
Grandpa Joe,B
Kayla,C
Brandon,C
Nia,D
Theo,E
```

`last_year.csv` and `this_year_draft.csv` both have the columns `giver,receiver`. Open them to see the
pairs.

---

## What you hand in

A new folder in your repository, `problem-drop-03/`, containing:

### 1. `DROP.md`, with these four headings

- **The real problem.** In two or three sentences. Not what Marisol asked for. What is actually causing
  the fight.
- **Who uses what I built, and when.** One or two sentences.
- **What my program does.** One or two sentences.
- **What I chose not to do, and why.** At least two things.

### 2. A working program

Whatever you decided to build, using only what you know from Units 0 through 5: functions, `try` and
`except`, lists, dictionaries, sets, CSV, JSON, and files. It must run with no traceback, and you must
paste at least one real run at the bottom of `DROP.md`.

### 3. A commit

Committed and pushed before the block ends.

---

## How to spend 40 minutes

| Minutes | Do this |
|---|---|
| 0-8 | Read the message twice. Write **The real problem** in `DROP.md` before you open a Python file. |
| 8-33 | Build the smallest thing that fixes the real problem. Run it on Marisol's files. |
| 33-38 | Paste your run. Write the other three headings. |
| 38-40 | Commit and push. |

**If you are still writing code at minute 34, stop.** A program that handles less, with an honest
`DROP.md`, scores higher than a bigger program with no explanation.

---

## Scoring, 30 points

| Dimension | Points |
|---|---|
| **Problem Identification** | 15 |
| **Working Artifact** | 10 |
| **Tradeoff** | 5 |

Half the points are for seeing the problem clearly. That is on purpose.
