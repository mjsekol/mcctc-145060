# Lecture Notes: Implementation Plans and User Help
## 145060 Programming · Unit 8 · Week 18, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W18_DocsForTwoReaders.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W18_DocsForTwoReaders.pptx)

If you missed class, you can learn this concept from this file alone. Run the commands.
Documentation is the one part of a project people assume they can write without testing,
and this file shows you why that assumption fails.

---

## Why this exists

On Friday you are not the only person who touches your project. A classmate might have to
redeploy it if your laptop dies. A player opens your link and has never seen a text
adventure. Your teacher grades it without you in the room.

None of them can ask you a question. **Documentation is you answering their questions
before they ask.** When it is missing, they guess. When it is wrong, they trust it and
then they are stuck, which is worse.

---

## The concept in plain language

**Every document has one reader, and you write for that reader, not for yourself.** A
software project needs at least two, because it has at least two kinds of people.

| | Implementation plan | User help |
|---|---|---|
| **Reader** | The person who deploys and maintains the app. Maybe you in three months. Maybe a classmate tonight. | The person who uses the app. Knows nothing about Python, Render, or ports. |
| **Question it answers** | "How do I put this online, prove it worked, and undo it if it broke?" | "How do I use this, and what does it mean when something odd happens?" |
| **Vocabulary** | Commands, settings, versions, logs | Buttons, words on the screen, what to do next |
| **Tested by** | Somebody following it step by step on a clean machine | Somebody who has never seen the app reading it and then playing |

Ohio's software lifecycle standard names four kinds of documentation: an implementation
plan, a contingency plan, a data dictionary, and user help. This week you write all four,
and you fold the smaller two into the implementation plan, where their reader is.

- The **contingency plan** is the "if this goes wrong, do this" part of the implementation
  plan. A rollback is the most important contingency.
- The **data dictionary** is the table that names every setting and every data field,
  what type it holds, and what it means.

### The rule that makes documentation honest

> **A document is a set of claims about your program. Claims can be tested.**

"Run `python app.py`" is a claim. "Type `save` to keep your progress" is a claim.
Either one can be checked in thirty seconds, and if you did not check it, you do not know
it is true.

---

## What goes in an implementation plan

Use these headings. Every one of them answers a question the deployer will have.

1. **What is being deployed.** App name, version number, and the Git tag it comes from.
2. **Where it goes.** The hosting service, the service name, and the public URL.
3. **Before you start.** What must already be true: accounts, a pushed repository, tests
   passing.
4. **Steps.** Numbered. One action each. Each step says what you should see when it
   worked.
5. **Settings.** The data dictionary for configuration: every environment variable, its
   type, its default, and what it controls.
6. **How to verify it worked.** Real commands with the expected output.
7. **If it goes wrong.** The contingency plan: the likely failures, how you recognize
   each one in the log, and how to roll back to the last version that worked.
8. **Known limits.** What the deployed version does not do, on purpose.

## What goes in user help

Shorter, and written with no technical words at all.

1. **What this is**, in one or two sentences.
2. **How to use it.** The first three things to try.
3. **What you will see**, including anything that looks like a problem and is not.
4. **What does not work here**, said plainly.
5. **What to do when something goes wrong.**

---

## Worked example 1: a verification step that is a real command

Weak verification steps say "check that it works." A deployer cannot follow that. A strong
one gives the command and the exact output, so there is nothing to interpret.

From the Storm Relay web implementation plan. On your own machine, start the app the way
Render does:

```
$env:PORT = "10000"
python app.py
```

```
Storm Relay web 1.0.0 listening on 0.0.0.0:10000
```

In a second terminal, check health before anyone has played:

```
curl.exe -s http://127.0.0.1:10000/health
```

```
{"status": "ok", "version": "1.0.0", "narrator": "not asked yet"}
```

Load the game page once, then check again:

```
curl.exe -s http://127.0.0.1:10000/health
```

```
{"status": "ok", "version": "1.0.0", "narrator": "not answering"}
```

That second line is what a correct deploy looks like on Render. The app is running, it is
the version you meant to ship, and the narrator is not answering because there is no model.
**The plan says so in writing**, so the deployer does not treat an expected result as an
outage at 11pm.

---

## Worked example 2: the step you skipped because you never need it

Here is a plan for the Playlist Namer lab app, written by someone who knows the project
well:

> 1. Open a terminal.
> 2. Run `python playlist_namer.py`.
> 3. Open http://127.0.0.1:8000 and type a mood.

A classmate follows it exactly. They open a terminal, which starts in their home folder or
the repository root, not the folder with the app in it. Step 2:

```
C:\Python313\python.exe: can't open file 'C:\\Users\\...\\playlist_namer.py': [Errno 2] No such file or directory
```

The part before the colon is the path to Python on that machine, so it will look different
on yours. The rest is the same.

**The writer never needed step 1.5, because their terminal was already in the right
folder.** That is one of the most common documentation failures: the missing step is the
one you do without thinking. Nobody writes down what they do automatically.

The fixed plan:

> 1. Open a terminal **in the folder that contains `playlist_namer.py`**. In VS Code, right
>    click the folder and choose Open in Integrated Terminal.
> 2. Run `python playlist_namer.py`. You should see `Playlist Namer listening on 0.0.0.0:8000`.
> 3. Open http://127.0.0.1:8000. You should see a box labelled with a question about mood.

Every step now names its starting point and what success looks like.

**The defense is not being more careful. It is handing your plan to someone else and
watching them follow it without helping.** Every time you want to say "oh, you have to..."
you have found a missing step.

---

## Worked example 3: user help that makes a promise the app does not keep

A first draft of Storm Relay web user help, copied from the version 4 README:

> Type `save` at any time to keep your progress, and `load` to pick up where you left off.

That was true for the version on your laptop. Here is what the web version actually does
when a player types `save`:

```
> save
Saving is turned off on the web version. Every visitor shares one server, and it forgets everything when it restarts.
```

The help page promised something the deployed app deliberately does not do. The player
trusted the help, lost their game, and now trusts nothing else it says.

The fixed user help:

> **Save and load do not work here.** The web version forgets games when the server
> restarts. A game is short, about 20 moves.

**Deploying a program changes it.** The same code in a different place can behave
differently, and the documentation has to describe the version people actually use.

### The same fact, written twice

The model is missing on Render. Here is that one fact for each reader.

**Implementation plan:** "`ADVENTURE_MODEL_URL` is not set on Render. Every model request
fails, the log shows `model failed`, and `/health` reports `narrator: not answering`.
This is expected. Do not open the lab model server to the internet to change it."

**User help:** "The room descriptions on this site are written by hand. On a lab computer,
a language model can retell them in its own words. The game plays the same either way."

Same truth. Different words, because different people need different things from it.

---

## Why the weak versions are tempting

**You are the worst tester of your own documentation.** You already know every missing
step, so you read right past the gap. Your brain fills it in.

**Copying is fast and it looks finished.** Pasting the README from the laptop version
produces a complete-looking page. It is complete. It describes a different program.

**"Check that it works" feels like a step.** It has a verb. It sounds like an instruction.
It is not one, because it does not say what "works" looks like.

**Technical words feel precise to you.** "The narrator falls back when the model endpoint
is unreachable" is exact to a programmer and meaningless to a player.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Implementation plan** | The document that tells a deployer how to put a version online, prove it worked, and undo it |
| **Contingency plan** | The part that says what to do when a step fails. A rollback is the main one |
| **Rollback** | Putting the last working version back online |
| **Data dictionary** | A table naming every setting or data field, its type, default, and meaning |
| **User help** | Documentation for the person using the app, in their words |
| **Verification step** | A command with its expected output that proves a step worked |
| **Audience** | The one reader a document is written for |

---

## Self-check

**Question 1.** Sort each sentence into implementation plan or user help, and rewrite the
one that is in the wrong voice for its reader.

- "If the page takes a while to load the first time, wait. The site was asleep."
- "Set the Start Command to `python app.py`."
- "The app degrades gracefully when the Ollama endpoint returns a non-200 status."

**Question 2.** A classmate's verification step says "Make sure the deploy worked." Rewrite
it as a step someone else can follow, for an app whose health route returns
`{"status": "ok"}`.

**Question 3.** Why is "the missing step is the one you do without thinking" a reason to
have someone else test your plan, rather than a reason to reread it more carefully?

---

### Answers

**1.** The first sentence is user help and is already in the right voice. The second is
implementation plan and is in the right voice. The third is true, but no user can read it,
and it is too vague for a deployer. For user help: "Room descriptions are written by hand
on this site. On a lab computer, a language model can retell them." For the implementation
plan: "When the model server does not answer, the log shows `model failed` and players see
the stored descriptions. This is expected on Render."

**2.** "Run `curl.exe -s https://your-service-name.onrender.com/health`. You should see
`{"status": "ok"}`. If nothing comes back for a long time, wait and run it once more,
because a free service may have been asleep **[VERIFY]**." The address is a placeholder:
use your own service's URL.

**3.** Rereading does not help, because you fill in the gap automatically every time you
read it, the same way you did when you wrote it. Someone without your knowledge cannot fill
the gap, so they hit it, and that is the only reliable way to find it.
