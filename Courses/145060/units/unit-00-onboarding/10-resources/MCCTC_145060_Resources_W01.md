# Additional Resources · Week 1
## 145060 Programming · Unit 0 · Week 1
### Topic: running a program, and version control

**About the links.** Every URL below is marked with how confident this file is that
it currently exists. Broken links cost a class period, so the marking is honest
rather than optimistic.

- **Confident** means the resource and that address are well established.
- **[VERIFY]** means the resource exists but the exact address or section number
  should be clicked once before assigning it. Two minutes of checking.

---

## The week at a glance

| # | Resource | Level | Time |
|---|---|---|---|
| 1 | Automate the Boring Stuff, Chapter 1 | Remediation / on-level | 30 min |
| 2 | Pro Git, sections 1.3 and 2.2 | On-level | 25 min |
| 3 | Python Tutor | Remediation | 15 min |
| 4 | Official docs: `print` | On-level | 10 min |
| 5 | GitHub secret scanning documentation | Extension | 15 min |
| 6 | Video: Git basics | Remediation | Under 20 min |
| 7 | Side quest: SQ-01 | Required | 80 min |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, 3rd edition · Chapter 1, "Python Basics"**
`https://automatetheboringstuff.com/` · **Confident** for the site.
**[VERIFY]** the exact third-edition chapter path before you post the link. The site
hosts the full text of multiple editions free to read, and the chapter numbering
shifted between editions.

**What it is.** The opening chapter of the most widely used free Python book. It
covers the interactive shell, expressions, and writing a first program in a file.

**Why this one.** It is the only free introductory book that treats "get the thing
installed and run a file" as a real topic rather than a footnote, which is exactly
Monday. It also uses the interactive shell heavily, which this course does not,
so tell students to read for the file-based section and skip the shell material for
now.

**Time.** 30 minutes. **Level.** Remediation for anyone shaky after Monday, and
on-level reinforcement for everyone else.

### Alternates, both confident

- **Think Python, 3rd edition** · `https://allendowney.github.io/ThinkPython/` ·
  Chapter 1. Denser and more precise. Better for the student who found Monday
  slow and wants the vocabulary nailed down.
- **Python for Everybody** · `https://www.py4e.com/` · Chapter 1. Gentler pacing
  and a strong "why programming" framing. The best choice for a student who is not
  sure they belong in this course yet.

---

## 2. Version control reading

**Pro Git, 2nd edition** · `https://git-scm.com/book/en/v2` · **Confident.**

Read two sections, not the whole book.

- **1.3 What is Git?** Explains snapshots against differences. This is the reading
  that makes the photograph metaphor from Tuesday click.
- **2.2 Recording Changes to the Repository** Covers the three states directly.

**Why this one.** It is the official book, free in full, and it is what a working
developer actually reaches for. Assigning primary sources in Week 1 sets the
expectation for the next two years.

**Warning worth passing on.** Chapter 3 is about branching, which this course does
not reach until 145065. A student who reads ahead into it will come back confused
and convinced they missed something. They did not.

**Time.** 25 minutes for both sections. **Level.** On-level.

---

## 3. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

**What it is.** You paste in code and it steps through execution one line at a time,
showing you what the machine is doing at each step.

**Why this one.** Week 1's whole concept is "the interpreter reads your file top to
bottom." Python Tutor makes that visible instead of theoretical. Paste in the
five-line `event_card.py` and press Next five times.

**Time.** 15 minutes. **Level.** Remediation, and genuinely useful for anyone who
did not believe the top-to-bottom claim.

**Alternate for practice volume:** Exercism's Python track ·
`https://exercism.org/tracks/python` · **Confident.** Free, and the early exercises
are appropriately small. Better for Week 2 onward than for Week 1, since most of it
assumes variables.

---

## 4. Official documentation

**The `print` function** ·
`https://docs.python.org/3/library/functions.html#print` · **Confident.**

**Why this one.** Students will find this page intimidating and that is the point.
Give them one specific question to answer from it rather than telling them to read
it: **what is the default value of `sep`, and what does it do.**

That single question explains why `print("Ava", "Ruiz")` puts a space between the
two words, which is Gate 1 Rep 05, Rep 16, and bell ringer W01-04. A student who
finds that answer on an official reference page has done something more valuable
than the answer itself.

**Time.** 10 minutes. **Level.** On-level. Assign the question, not the page.

---

## 5. Connecting to real industry work

**GitHub documentation on secret scanning** ·
`https://docs.github.com/en/code-security/secret-scanning` · **[VERIFY].** GitHub
documents this feature and the section exists, but the exact URL path has moved
between documentation reorganizations. Click it once.

**What it is.** GitHub's own documentation for the service that scans repositories
for credentials and notifies the provider that issued them.

**Why this one.** Wednesday's lesson can read like a classroom rule. This is the
platform itself documenting a feature it built because the mistake is common enough
at professional scale to require automated defense. That reframes the lesson from
"my teacher said not to" to "this is a known industry failure mode with tooling
built around it."

**Time.** 15 minutes. **Level.** Extension.

**On the "current article" slot.** This resource pack does not include a link to a
current news article about a credential leak, and that is deliberate. Article URLs
go stale and this file cannot confirm which ones are live today. If you want one,
search for `hardcoded credentials public repository` limited to the last twelve
months and pick one yourself. A story from this month lands harder than any link
written in advance, and you can confirm it loads before class.

---

## 6. Video

**Git basics, official short videos** · `https://git-scm.com/videos` · **[VERIFY].**
The Git project hosts a short introductory video series and this address has been
stable, but confirm it plays through district filtering before assigning it.

**Honest note.** This pack does not name a specific YouTube video. There are several
excellent free Git introductions on YouTube under twenty minutes, and a specific
video ID written into a file today is a link that may not resolve later.
Rather than guess at one, pick a video yourself, watch the first three minutes, and
confirm two things: it uses `main` rather than `master` as the default branch name,
and it does not open with GitHub Desktop or another graphical client. Both of those
will contradict what students did in class this week.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 7. Side quest

**SQ-01 Hello, Version Control** is this week's required side quest and is delivered
as Lab U0-01. It is the prerequisite for grading anything else in this course.

**Also available now:** `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`. The
quest that pairs with Week 1 is **SQ-03 The Terminal Is Not Scary**, one block,
which is the right hand-out for a student whose Week 1 friction was the terminal
rather than the concepts.

**An extension for a student who finished everything.** Have them clone a
classmate's repository, run it without asking any questions, and write down every
point at which they had to guess. Hand that list back to the repository's owner.
This is a code review before students know the term, it takes 20 minutes, and it
teaches more about READMEs than any reading on this page.

---

## For the student who is behind

In this order, and no more than two of them:

1. Python Tutor with their own `event_card.py`, stepping one line at a time
2. Automate the Boring Stuff Chapter 1, the file-based section only
3. Pro Git section 2.2, read slowly, with a terminal open next to it

Do not assign all seven resources to a struggling student. A student who is behind
and receives a list of seven links reads zero of them.
