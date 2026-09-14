# Practice Interview Transcript
## 145060 Programming · Unit 6 · Week 13 · Tuesday, December 1 · Build 1

**Why this exists.** In Build 2 you get four minutes with your real stakeholder, and four minutes goes fast.
Practice pulling requirements out of a conversation first, on one where nobody is waiting for you.

**The people in this transcript are a composite.** The band director and the student team are invented.

---

## The transcript

A student team interviewed the marching band director about the uniform room. Read it twice. The second time,
underline every sentence that contains a requirement, a constraint, or a hint about the real need.

> **Student:** Thanks for meeting with us. Can you walk us through how the uniform room works today?
>
> **Director:** Sure. We have about ninety uniforms. Jacket, pants, and a hat for each. They live on racks in the
> band room. At the start of the season everybody gets fitted and signs one out. I have a spreadsheet of what we own.
>
> **Student:** And what goes wrong?
>
> **Director:** Honestly, all I need is a list of the uniforms.
>
> **Student:** You have the spreadsheet already, though. Can you tell us about the last time the uniforms caused a
> problem?
>
> **Director:** Oh. The holiday parade, last year. The Tuesday before, we found out we had no jackets left in small.
> None. Four freshmen marched in jackets down to their knees. And two jackets we thought were fine had broken zippers,
> which we found out that morning.
>
> **Student:** So you found out too late.
>
> **Director:** Right. If I had known two weeks ahead, I could have ordered, or had them fixed. The parent volunteers
> do repairs, but they need time.
>
> **Student:** How do sizes get written in the spreadsheet?
>
> **Director:** Whoever enters them. S, small, sm. Medium, M, med. It is a mess, mostly.
>
> **Student:** Mostly?
>
> **Director:** Well, some rows have no size at all. Those are the old uniforms from before I started.
>
> **Student:** What about damaged ones?
>
> **Director:** There is a condition column. "Good," "needs repair," or blank. Blank usually means nobody checked.
>
> **Student:** How will you know if a tool like this worked?
>
> **Director:** If two weeks before the parade I can see, for each size, how many good jackets I have compared to how many
> kids need that size. And a list of what needs repair, so I can hand it to the parent volunteers.
>
> **Student:** Is there anything it must never do?
>
> **Director:** It cannot need the internet. The band room computer is not on the school network. And please do not put the
> kids' names in it. I track who has what on paper.

---

## Your task

Work with your team. Write answers in `docs/question_log.md` under a heading `Practice interview`.

1. **The real need, in one sentence.** Not what the director first asked for.
2. **Three requirements**, each with at least one acceptance criterion in Given, When, Then form. At least one must be a
   processing requirement: what happens to input nobody planned for.
3. **Two constraints**, each with the reason it exists.
4. **One question you would ask next**, because the transcript did not answer it, and the assumption you would make until you
   got an answer.

**Done when:** all four are written, and a teammate who has not read the transcript could check each of your acceptance criteria.

---

## What to notice before your real interview

- The director's first answer was a solution, not a problem. The student did not argue. The student asked about the last time
  it went badly.
- The student asked "mostly?" out loud. That one word found the rows with no size.
- The best acceptance criterion question was "how will you know if a tool like this worked?" The director's answer is nearly a
  criterion already.
- Nobody pitched a feature.
