# Lecture Notes: Remotes, READMEs, and Why Secrets Never Go In
## 145060 Programming · Unit 0 · Week 1 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W01_RemotesAndSecrets.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W01_RemotesAndSecrets.pptx)

If you missed class, you can learn this concept from this file alone. The
demonstration in the middle of this file is the most important five minutes of
Week 1. Run it yourself in a throwaway folder rather than reading it.

---

## Why this exists

Two reasons, and the second one is the one people learn the hard way.

**The first reason is that your laptop is not a plan.** A repository that exists on
one machine is one spilled drink away from not existing. Pushing to GitHub gives
the history a second home, and it is the only reason you can hand a project to
somebody else or pick it up on a different computer.

**The second reason is that pushing is publishing.** The instant you push, you have
handed a copy to a service, and depending on the repository's settings, possibly to
everyone. You cannot take that back. This is where credentials leak, and it happens
to professionals often enough that GitHub runs an automated service that scans
public repositories for credentials and notifies the companies that issued them.

The Lab Acceptable Use and Safety Agreement you signed says it directly in section
2: passwords, API keys, tokens, and credentials are never committed to a
repository, shared, or posted. Today is the day you find out what that rule is
protecting you from, and why the fix you will reach for first does not work.

---

## The concept in plain language

Yesterday you had three places: your working directory, the staging area, and the
repository. Today there is a fourth.

**A remote is a copy of your history living on another machine.** GitHub is where
ours live. The remote is not a folder full of your files. It is a copy of the
history, made of the commits you sent it.

- `git remote add origin <url>` tells your repository where that other copy lives.
  `origin` is the conventional name for it, not a keyword.
- `git push` sends commits from your repository to the remote.
- `git clone <url>` makes a new local repository from a remote one, history and all.

**Push sends commits. It does not send your folder.** If you edited a file and did
not commit, pushing sends nothing new. This trips people up for about two weeks and
then never again.

Extend the photo album metaphor. `git commit` takes the photograph.
`git push` mails a copy of the album to someone else. Once it is mailed, it is
theirs. There is no command that reaches into someone else's mailbox.

---

## Worked example 1: connecting and pushing

You have a local repository with commits in it, and you have created an empty
repository on GitHub.

```
git remote add origin https://github.com/aruiz/trip-budget.git
git push -u origin main
```

`-u` sets the upstream, which means "remember that my `main` goes to `origin`'s
`main`." You do it once. Every push after that is `git push` with nothing after it.

Check what you connected to:

```
git remote -v
```

If you skip the remote step and push anyway, Git says so plainly:

```
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>
```

Again, the tool tells you the fix in its own output.

---

## Worked example 2: a README a stranger can use

Your README is the front page of the repository. Assume the reader is a stranger,
because at a CTAG review, a BPA judge, or an internship interview, that is exactly
who it is.

A README that earns full credit in this course answers four questions, in this
order:

1. **What is this.** One or two sentences. Not the assignment name, the thing.
2. **How do I run it.** The exact command, copyable, and what you need installed.
3. **What does it do when it works.** Show the actual output.
4. **What did you learn or decide.** The part that is yours.

```markdown
# Trip Budget

A command-line tool that prints what a weekend trip to Cedar Point costs per person
once gas, tickets, and food are split across everyone going.

## Running it

Requires Python 3.14.

    python trip_budget.py

## What it looks like

    Gas: 40 dollars
    Tickets: 55 dollars each
    Per person total: 68 dollars

## Notes

I started by hardcoding four people, then pulled the number out so the same file
works for any group size. The gas estimate assumes one round trip and does not
account for the second car we usually end up taking.
```

The single most common failure is a README that names the assignment instead of the
program. "Unit 0 Lab" tells a stranger nothing. Write the second sentence of that
example and you are ahead of most repositories on GitHub.

---

## The demonstration: the `.gitignore` trap

Run this yourself, in a throwaway folder, in exactly this order. Type the fake key
by hand. It is not a key to anything.

**Step 1.** Create a file called `secrets.txt` containing one line:

```
OPENAI_API_KEY=sk-not-a-real-key-1234567890
```

**Step 2.** Commit it, the way somebody in a hurry would.

```
git add secrets.txt
git commit -m "Add settings file"
```

**Step 3.** Realize the mistake and do the thing everybody does first. Create
`.gitignore` containing `secrets.txt`, and commit that.

```
git add .gitignore
git commit -m "Add gitignore"
```

**Step 4.** Now edit `secrets.txt` and check the status.

Real output:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   secrets.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

**Git is still tracking it.** The `.gitignore` did nothing to this file.

Here is the rule that explains it, and it is the whole lesson:

> **`.gitignore` controls whether Git *starts* tracking a file. It has no effect on
> a file Git is already tracking.**

**Step 5.** So stop the tracking.

```
git rm --cached secrets.txt
git commit -m "Stop tracking the settings file"
```

That works. `git ls-files` no longer lists it, and future changes are ignored. Now
ask the real question:

```
git log --oneline -- secrets.txt
```

Real output:

```
b151592 Stop tracking the settings file
38cc1b2 Add settings file
```

**The key is still in the history.** Commit `38cc1b2` contains it, permanently, and
anyone who clones the repository can read it in about four seconds. If you pushed
before you noticed, other people may already have that clone.

---

## What actually fixes it

There is no command in this list that fixes it, and that is the point.

| What people try | What it actually does |
|---|---|
| Add it to `.gitignore` | Nothing. The file is already tracked. |
| Delete the file and commit | Removes it going forward. The old commit still has it. |
| `git rm --cached` | Stops tracking it. The old commit still has it. |
| Make the repository private | Reduces who can reach it. Anyone who already cloned still has it. |
| Rewrite the history | Possible, difficult, and does not touch existing clones. |

**The only action that resolves it is changing the secret.** Revoke the key, issue
a new one, update everywhere that used it, and treat the old one as public from now
on, because it is.

Sit with how unsatisfying that is. Almost every other mistake you make this year is
undoable. This one is not, and that is exactly why the habit matters more than the
recovery procedure.

**Which is why `.gitignore` gets written before the first commit.** Not after the
mistake. That ordering is a graded requirement in this week's lab, and now you know
what it is protecting.

---

## Why the wrong version is tempting

Three reasons, and they stack.

**Undo is everywhere else.** Every tool you have used has undo. Ctrl-Z, trash,
version history in Docs. You have been trained that mistakes are reversible, and
almost all of yours have been. This is one of the first tools you will use where
the damage happens the instant you press enter and no button takes it back.

**The obvious action feels like it worked.** After step 3, `git status` is clean and
`.gitignore` has the filename in it. Every visible signal says handled. Nothing
turns red. The absence of an error message is not evidence of success, and this is
the week to learn that.

**`git add .` is fast.** It stages everything at once, and it is how most leaked
credentials get staged. There is a defensible version of using it: on a small
repository, with a `.gitignore` written first, and with `git status` read before
every commit. Each of those conditions is doing real work. Take one away and it is
the least safe command in this file.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Remote** | A copy of your repository's history on another machine. |
| **`origin`** | The conventional name for your main remote. Not a keyword. |
| **`git remote add`** | Tells your repository where a remote lives. |
| **`git push`** | Sends commits from your repository to the remote. |
| **`-u` / `--set-upstream`** | Remembers the pairing so later pushes need no arguments. |
| **`git clone`** | Creates a local repository from a remote one, history included. |
| **`git ls-files`** | Lists every file Git is currently tracking. |
| **`git rm --cached`** | Stops tracking a file without deleting it from your folder. |
| **`.gitignore`** | Lists things Git should never start tracking. |
| **README** | The front page of a repository, written for a stranger. |
| **Markdown** | The plain-text formatting used in `.md` files, including this one. |
| **Credential** | A password, API key, token, or anything else that proves you are you. |
| **API key** | A credential that identifies your program to an outside service. |
| **Revoke** | To cancel a credential so it stops working. |
| **Public repository** | One anybody on the internet can read. |

---

## Self-check

**Question 1.** You committed three times today and pushed once, after the first
commit. A classmate clones your repository right now. How many of your three
commits do they get, and why.

**Question 2.** A student pushed a file containing their real GitHub password on
Tuesday. On Thursday they ran `git rm --cached passwords.txt`, added the file to
`.gitignore`, committed, and pushed. They tell you it is handled. Write the four
sentences you would say back: whether they are right, what `.gitignore` controls,
what is true about the password right now, and the one action that resolves it.

**Question 3.** Your README says only this: `Unit 0 Lab. Run the python file.`
Name three specific things a stranger cannot do because of what is missing, and
write a replacement first line.

---

### Answers

**1.** They get one commit. Push sends commits to the remote, and you have pushed
only once, so commits two and three exist on your machine and nowhere else. This is
also the answer to "why does my GitHub page look out of date," which you will ask
at some point in the next two weeks.

**2.** They are not right. `.gitignore` controls whether Git starts tracking files
it is not already tracking, and `git rm --cached` stops the tracking going forward,
so neither one touches a commit that already exists. The password is sitting in
Tuesday's commit, that commit is on GitHub, and anyone who cloned the repository
since Tuesday has their own copy that no command of yours can reach. The one action
that resolves it is changing the password itself, everywhere it is used, and
treating the old one as public.

**3.** Three things a stranger cannot do:

- They cannot tell what the program is for, so they cannot tell whether it is worth
  running.
- They cannot run it, because "the python file" does not name a file and no command
  is given. In a repository with four `.py` files, this is a dead end.
- They cannot tell whether it worked, because no expected output is shown.

A replacement first line names the thing rather than the assignment, for example:

```
A command-line tool that prints how much a weekend trip costs per person once gas,
tickets, and food are split across everyone going.
```
