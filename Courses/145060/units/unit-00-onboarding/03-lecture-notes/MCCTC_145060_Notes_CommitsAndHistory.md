# Lecture Notes: Commits and History
## 145060 Programming · Unit 0 · Week 1 · Wednesday

If you missed class, you can learn this concept from this file alone. Open a
terminal and run every command. Git is a tool you learn with your hands.

---

## Why this exists

Every version of this story is the same story. You had a working project. You
changed something. It stopped working. You changed three more things trying to fix
it. Now you cannot get back to the version that worked, and you cannot remember
what you changed first.

Or: two people worked on the same project, and the newer file overwrote the better
one, and nobody can tell which was which.

The information you lost in both cases is the same information. You could see what
the file looks like **now**. You could not see what it looked like **before**, or
**who** changed it, or **why**. Git is the tool that keeps that.

**Git is not backup.** Backup answers one question: where is my file. Git answers a
different one: what did this look like at every point along the way, and what was
the person trying to do at the time. That second half is why commit messages are
graded work in this course.

---

## The concept in plain language

Here is the mental model. Use these words all semester and do not switch.

**Git does not watch your folder.** It takes photographs when you ask it to.

There are three places a change can be, and a change moves through them in order.

| Place | What it is | How things get there |
|---|---|---|
| Working directory | The files you can see and edit right now | You edit and save them |
| Staging area | The list of changes going into the next photograph | `git add` |
| Repository | The permanent history of every photograph taken | `git commit` |

- `git add` is **choosing what goes in the photograph.**
- `git commit` is **taking the photograph and writing a caption on it.**
- `git status` is **asking what is in the frame right now.**
- `git log` is **flipping through the album.**

**A commit is not a save. A save is a save. A commit is a save you named and can
find again.** Hold onto that sentence. Almost everything that confuses people this
week comes from mixing those two up.

---

## Why there is a staging area at all

This is the first thing students find annoying, and the annoyance is reasonable.
On a file with four lines, `git add` looks like typing for no reason.

The reason: real work changes several files at once, and they are usually not all
part of the same idea. You fixed a bug in one file and started an unrelated feature
in another. Those belong in two different commits with two different messages,
because six months from now you will want to find the bug fix without the
half-finished feature attached to it.

The staging area is where you choose. On a four-line program that choice is
trivially small. Around Unit 4, when your text adventure has real files in it, it
stops being trivial.

---

## Worked example 1: the three commands

Start in a folder that has `status_card.py` in it and no repository yet.

```
git init -b main
```

That creates the repository. The `-b main` names the first branch `main`. Branches
come later in 145065, so for now `main` is the only one you have.

```
git status
```

Real output:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        status_card.py

nothing added to commit but untracked files present (use "git add" to track)
```

Git is telling you three separate things. There is no history yet. There is a file
here Git has never been told about, which is what **untracked** means. And nothing
is lined up to be committed, so committing right now would record nothing.

Notice that Git printed the fix twice, in parentheses, in its own output. Reading
tool output instead of skipping past it is a real skill and this is where it starts.

```
git add status_card.py
git commit -m "Add status card that prints my name and day 1 goal"
git log --oneline
```

Real output of that last command:

```
54ab326 Add status card that prints my name and day 1 goal
```

`54ab326` is the start of the commit's ID. Yours will be different from everyone
else's, including your classmate who typed the identical file. The ID is computed
from the contents, the message, the author, and the time, so no two are the same.

---

## Worked example 2: what `git status` says at each stage

Run `git status --short` after each step and watch the letters change. This is the
fastest way to make the three places real instead of theoretical.

| After you do this | `git status --short` shows | Meaning |
|---|---|---|
| Create a new file | `?? notes.py` | Untracked. Git has never seen it. |
| `git add notes.py` | `A  notes.py` | Added, waiting in the staging area. |
| `git commit -m "..."` | (nothing) | Committed. Working directory matches history. |
| Edit and save `notes.py` | ` M notes.py` | Modified on disk, not staged. |
| `git add notes.py` | `M  notes.py` | Modified and staged. |
| Edit and save it again | `MM notes.py` | One version staged, a newer one on disk. |

Look at rows four and five. The letter is the same and its **position** moved.
The left column is the staging area. The right column is your working directory.
That single space is Git telling you which of the three places your change is
sitting in.

The last row is worth staring at. `MM` means there are now two different versions
of that file in play: the one you staged, and the newer one you have since typed.
A commit right now would record the older of the two. Come back to this row after
you answer self-check question 1.

---

## Worked example 3: a message that is worth writing

Both of these commits contain identical code changes.

```
git commit -m "update"
git commit -m "Fix crash when the player types an exit that does not exist"
```

The first one is worth close to nothing. Six weeks from now you will scroll a list
of forty commits named `update`, `update2`, `fix`, and `fixed it`, and you will
have to open every one to find anything.

Use this test. **A good commit message completes the sentence "This commit
will..."** and says something the diff cannot tell you on its own.

The diff already shows *what* changed. Anyone can read that. Your message is the
only place the *why* is ever recorded.

| Message | Verdict |
|---|---|
| `update` | Worthless. Says nothing. |
| `Changed line 14` | Worthless. The diff already says that, more precisely. |
| `Add .gitignore` | Weak. True, and says nothing about why. |
| `Ignore my personal notes file so it never gets pushed` | Good. |
| `Fix crash when the player types an exit that does not exist` | Good. |

Present tense, and describe the change rather than yourself. Write
`Add status card`, not `I added the status card` and not `Added status card`.
This is a convention, not a law of nature, and it is the one this course uses so
that thirty repositories read the same way.

---

## The wrong version, and the exact error

Here is the mistake almost everyone makes on day two. You write the file, you save
it in VS Code, and you commit.

```
git commit -m "first commit"
```

Real output:

```
On branch main

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        status_card.py

nothing added to commit but untracked files present (use "git add" to track)
```

**Nothing was committed.** The command did not crash, it did not turn red, and it
did not say the word "error" anywhere. It told you calmly that there was nothing to
photograph, because you never handed it anything.

The fix is on the last line of Git's own output: `git add status_card.py` first.

There is a second version of the same mistake that bites later. You commit, then
keep editing, then push, and are surprised the newest changes did not go. The
changes you made after the commit are still sitting in your working directory. A
commit is a photograph of a moment, not a live feed.

---

## Why the wrong version is tempting

It is tempting because **every other program you have ever used works the other
way.** In Google Docs, in Notes, in a game save, saving is the whole operation.
There is one step and it happens automatically. You have twelve years of training
that saving means done.

Git splits it into two steps on purpose, and the payoff for that split does not
arrive until your project is big enough to have unrelated changes in flight at the
same time. In Week 1 you are paying a cost with no visible benefit. That is real,
and it is worth naming instead of pretending.

The second reason it is tempting: Git's message is polite. It does not look like a
failure. A red traceback makes you stop. A calm paragraph makes you assume it
worked. Read the last line of Git output before you move on, every time.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Repository** / **repo** | A project folder plus the full history Git keeps for it. |
| **`git init`** | Creates a new, empty repository in the current folder. |
| **Working directory** | The files as they exist right now, that you can open and edit. |
| **Staging area** | The list of changes selected for the next commit. |
| **`git add`** | Puts a change into the staging area. |
| **Commit** | One saved snapshot in the history, with a message and an author. |
| **`git commit -m "..."`** | Takes the snapshot. `-m` supplies the message. |
| **Commit message** | Your written record of why this change was made. |
| **Untracked** | A file in the folder that Git has never been told about. |
| **Tracked** | A file Git is following. |
| **Modified** | A tracked file that changed since the last commit. |
| **`git status`** | Reports which files are untracked, modified, or staged. |
| **`git log`** | Lists the commit history, newest first. |
| **`--oneline`** | Shows each commit on a single line. |
| **Commit hash** | The unique ID of a commit. Different on every machine. |
| **`main`** | The default name of the first branch. |
| **`.gitignore`** | A file listing things Git should never start tracking. |

---

## Self-check

**Question 1.** You created `budget.py`, ran `git add budget.py`, then edited
`budget.py` again and saved. You have not run any other Git command. Run
`git commit -m "Add budget tool"` in your head. Which version of the file goes into
the commit, the one you added or the one currently on disk. Explain why.

**Question 2.** Here is a commit history. Two of these messages are doing real
work and three are not. Sort them and say what makes the difference.

```
a1b2c3d update
e4f5g6h Add .gitignore before first commit so notes stay out of the repo
i7j8k9l fixed
m0n1o2p Fix crash when the player types an exit that does not exist
q3r4s5t changes
```

**Question 3.** In two sentences, explain to somebody who has never used a terminal
what `git add` does that `git commit` does not.

---

### Answers

**1.** The version you added goes in. `git add` copied that version of the file
into the staging area at the moment you ran it, and your later edit changed only
the working directory. The commit records what is staged, so your most recent edit
is left out, and afterward `git status` will show `budget.py` as modified. This is
the most common surprise in the first two weeks, and the cure is running
`git status` before every commit rather than after.

**2.** `e4f5g6h` and `m0n1o2p` are doing real work. `update`, `fixed`, and
`changes` are not.

The difference is not length. It is that the two good messages tell you something
the diff cannot: **why**. The diff already shows exactly what characters changed.
It cannot tell you that a crash was involved, or that the goal was keeping personal
notes out of the repository. Anything the diff already says is wasted space in a
message.

**3.** `git add` is you choosing which of your changes belong in the next snapshot,
and it is the only step where you have a choice. `git commit` takes the snapshot of
whatever you chose and writes it into the permanent history with your explanation
attached.
