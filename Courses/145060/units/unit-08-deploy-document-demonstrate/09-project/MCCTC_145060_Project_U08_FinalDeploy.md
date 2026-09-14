# Project: Final Deploy
## 145060 Programming · Unit 8 · Live URL due Thursday, January 28, 2027 · Demos Friday, January 29

**Mode:** solo. **Gate:** 3, full tooling, decision log required. **Periods:** Build 2 on
Monday and Tuesday, the end of Wednesday if the exam finishes early, and Build 2 on Thursday
after the WebXam post-test. Demos fill Friday.

**Competencies:** 5.6.16 (deploy the application), 5.6.8 (implementation plan and user help),
5.6.17 (collect feedback and maintain the application), 5.7.1 (version management and
interface control), 5.7.2 (baseline and lifecycle phases), 5.7.3 (analyze the impact of
changes), 1.2.2 (deliver a formal presentation), 1.2.5 (communicate for an intended audience),
1.2.11 (write professional documents).

**This is the last project of the semester, and it closes Grading Period 2.** There is no
revision window after Friday that can reach this grading period. Plan for that.

---

## The brief

Read this as though a person said it to you. This brief is a composite scenario written for
this course, not a real request from a real person.

> Every January families ask us what students actually built this semester, and every year
> the answer is a screenshot. I am done with screenshots. I want a page of links. A parent
> taps one on their phone in the parking lot and the thing runs.
>
> I do not care how fancy it is. I care that it works the first time, for a stranger, on a
> phone, with nobody standing next to them explaining it. If something is missing, like
> the AI part, it has to say so instead of looking broken.
>
> And when somebody asks the student "why did you build it like that," I want an answer,
> not a shrug.

**That is the whole brief.** Notice what it does not say. It does not name your project, the
host's settings, what counts as "works," or what a stranger needs to read first. Deciding
those is the work.

## Which project you deploy

Pick one. Tell your teacher by the end of Monday's Build 2.

1. **Your text adventure, version 4, as a web app.** The expected choice.
2. **Your Unit 7 API-consuming application, as a web app.** Allowed if it uses an API with
   no key and no account, the same rule as SQ-10.
3. **Another project you built this semester**, approved by your teacher on Monday. It must
   be your own semester work, and it must take input from the person using it.

Whichever you choose, **it is standard library only, like everything else this semester.**

---

## Requirements

### Deployed

1. **A live public URL** on Render, free tier, that loads from a phone on cell data.
2. **It listens where Render can reach it:** host `0.0.0.0`, port read from `PORT` and
   converted to a whole number.
3. **A `/health` route** that answers 200 quickly and never depends on anything optional.
4. **It survives what Render does not have.** No local model exists on Render. If your
   project uses a model or an outside API, a failure falls back to something useful and the
   page says, in plain words, that the fallback happened.
5. **Every visitor gets their own experience.** Two people playing at once must not share one
   game, one score, or one inventory.
6. **Nothing typed by a visitor is placed in the page unescaped**, and input is validated the
   way Unit 7 taught.
7. **No secret, key, or password anywhere in the repository**, including old commits.

### Documented

8. **`README.md`**: what it is, the live URL, how to run it locally, the start command, a real
   run, and known limitations.
9. **`docs/IMPLEMENTATION_PLAN.md`**: what version, numbered steps with what success looks
   like, a settings table, verification commands with expected output, and a contingency
   plan that includes rolling back.
10. **`docs/USER_HELP.md`**: for a player or user, with no technical words. It describes the
    deployed version, not the laptop version.
11. **`docs/DECISION_LOG.md`**: at least five decisions, each with what you chose, what you
    rejected, and why. AI use recorded in the decision it affected. It ends with a
    **Feedback** section: what two people who used your live URL ran into, and what you
    changed or deferred because of it. Tuesday's partner counts as one.
12. **`docs/CHANGE_IMPACT.md`**: one real change you made for the deployed version, analyzed:
    what it touches, what it breaks, what you considered instead, and what version number it
    earned.

### Versioned

13. **A tag, `v1.0.0` or higher, pushed to GitHub**, on the exact commit that is deployed.
14. **`CHANGELOG.md`** with at least that version in it.
15. **Every period ends with a commit.** Same rule as every day this semester.

### Demonstrated

16. **A five-minute demo on Friday** covering what it does, why you built it this way, and what
    you rejected. Script below.

---

## Required repository structure

```
your-project/
  app.py                 (or your own name, as long as README names the start command)
  requirements.txt       (comments only, if nothing needs installing)
  README.md
  CHANGELOG.md
  test_*.py              (your tests, if your project had them; keep them passing)
  docs/
    IMPLEMENTATION_PLAN.md
    USER_HELP.md
    DECISION_LOG.md
    CHANGE_IMPACT.md
  ...                    (the rest of your project's files)
```

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Enter a credit card or payment method anywhere | The program uses free tiers only. If Render asks for one, stop and tell your teacher. |
| Use a commercial AI API or any API that needs a key | Commercial developer APIs require users to be 18 or older, and a key in a public repository is public. |
| Make the lab model server reachable from the internet | That is a district security decision. The fallback is the requirement. |
| Put a last name, student ID, or any personal detail in your service name, pages, or logs | The URL and the page are public. |
| Install packages | Nothing this semester needed one, and a new dependency in the last week adds a way to fail you cannot explain. |
| Add accounts, logins, or a database | Each is a new technology with its own security risks, in four days. Put it in Known limitations as a future version. |
| Submit anything you cannot explain | The one way to fail outright in this program. Friday's demo is where it shows. |

**If your family has asked for an alternative to Render,** you deploy to a lab machine on the
class network instead. Your "live URL" is that machine's address, reachable from another lab
computer, and every other requirement is identical. Your teacher confirms this with you
Monday.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Mon Jan 25, end of Build 2 | Which project, who the user is, and one sentence on what they do with it. First entry in `DECISION_LOG.md`. |
| **Measure** | Mon Jan 25, end of Build 2 | A readiness audit: for your project as it is today, which of requirements 2 through 7 already pass and which fail. Written, before you fix anything. Tag it `v0.9.0`: that is your starting baseline. |
| **Analyze** | Tue Jan 26, end of Build 2 | Implementation plan and user help drafted. The contingency plan names your three likeliest failures. |
| **Improve** | Mon through Thu | Make the readiness fixes, deploy, test from a phone, write the docs. |
| **Control** | Thu Jan 28, end of block | `v1.0.0` tagged and pushed on the deployed commit. Change impact note done. All five of your plan's verification checks run against the live URL. |

**Measure is the checkpoint students skip, and it is the one that saves Thursday.** A readiness
audit on Monday tells you exactly how much work there is, while there is still time to do it.

---

## Milestone schedule, against actual class days

| Day | In class | Your project goal by end of block |
|---|---|---|
| **Mon Jan 25** | Deploying to Render. Lab U8-01. | Project chosen. Readiness audit written, `v0.9.0` tagged. Port, host, and `/health` fixed. Service created on Render, even if the first deploy fails. |
| **Tue Jan 26** | Implementation plans and user help. Lab U8-02 Parts 1-2. | Deploy working. Implementation plan and user help drafted. A partner followed your plan and you fixed what they hit. |
| **Wed Jan 27** | Versions, baselines, change impact. Lab U8-02 Part 3. **GP2 exam** in Build 2. | Decision log has five entries. Change impact note drafted. |
| **Thu Jan 28** | **WebXam post-test** first. Build 2 is project time. | Tag `v1.0.0`, `CHANGELOG.md`, verification checks run on the live URL from a phone, demo rehearsed once with a partner. **Everything due at the end of the block.** |
| **Fri Jan 29** | **Demos.** | Present. Your teacher checks your URL before class starts. |

---

## Three worked scope examples

These are here so you can calibrate. Nobody builds these exact three.

### Too small

> A page that says "Storm Relay by Jordan" with a link to the GitHub repository. Deployed,
> live, health route, README.

It is live and it is not the project. A stranger cannot do anything with it. The brief said
"the thing runs," and the thing is not there. It fails requirements 4, 5, 6, and most of
Documentation, because there is nothing to document.

### About right

> **Storm Relay web.** Text adventure version 4 behind a command box. Each visitor gets their
> own game, tracked by a cookie. No model on Render, so rooms use stored descriptions with a
> one-line note saying so. `save` and `load` answer with a message explaining they are off on
> the web, and that choice is the change impact note. `/health` reports the version. Plan,
> help, decision log, changelog, tag `v1.0.0`.

Every requirement, nothing extra, and every choice has a reason a player would understand.
**The Unit 7 API app version of "about right"** is the same shape: a form, one request to a
no-key API per submission, and a different plain-language message on the page for a 404, a
timeout, and a rate limit.

### Too big

> Storm Relay with player accounts, a high-score table saved in a database, a chat box so
> players can help each other, and a custom domain name.

Accounts mean passwords, which means a security problem you have four days to get right.
A database is a new technology, and on a free tier its terms need checking before anybody
depends on it. A chat box is unescaped user text shown to other users. A custom domain costs
money. Every one of those is a good version 2.0.0 idea. Write them in Known limitations as
future versions, and ship 1.0.0.

**The calibration question:** could a classmate redeploy your project from your implementation
plan alone, on Thursday night, without texting you? If the plan would need more than one page
to make that true, the scope is too big for this week.

---

## The five-minute demo

Friday. **Five minutes, timed, and the timer is strict,** because every demo in the room has to
fit. Your teacher opens your URL before class so a sleeping service is awake.

| Time | You show | You say |
|---|---|---|
| **0:00 to 1:00** | The live URL on the projector | **What it does.** Who it is for, in one sentence. Then use it for real: three actions a new user would take. |
| **1:00 to 2:30** | Your decision log | **Why you built it this way.** Two decisions. For each, what you chose and the reason, in words a player would follow. |
| **2:30 to 3:30** | Your decision log or change impact note | **What you rejected.** One option you seriously considered and did not build, and exactly why. |
| **3:30 to 4:15** | The page, or the log | **What happens when something is missing.** Show the fallback. Say what the page tells the user. |
| **4:15 to 5:00** | Anything | **Questions.** Answer one. |

**The middle two sections are the graded core.** Anybody can click through a web page. A
decision you can defend, and an option you can explain rejecting, is the evidence that you built
it and understand it.

### If your live URL fails during the demo

Stay calm and say what you see. Open your deploy log or your `/health` route, name what you
think happened, and run the demo locally from your repository. **A clear explanation of a
failure earns more Demonstration points than a demo that worked and could not be explained.**
The deployed requirement itself is graded from your URL check, not from demo luck.

### Demo score sheet

Your teacher fills this in during your demo. Each line is observable.

| # | Observed | Points |
|---|---|---|
| 1 | Opened the live URL and used the app as a new user would | 2 |
| 2 | Said who it is for and what it does, in plain words | 1 |
| 3 | Explained two decisions, each with a reason | 2 |
| 4 | Named one rejected option and why it was rejected | 2 |
| 5 | Showed or explained the fallback when something is missing | 1 |
| 6 | Answered a question about any part of the code or the choices | 1 |
| 7 | Finished inside five minutes | 1 |
| | **Demonstration total** | **10** |

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Live URL loads from a phone on cell data. `PORT` and `0.0.0.0` correct. `/health` answers. Fallback works and is labelled. Two visitors never share state. Input escaped and validated. |
| **Code Quality** | 20 | Readable names, comments that explain why, no bare `except`, no secret anywhere in history, tests from earlier versions still passing. |
| **Documentation** | 20 | README, implementation plan, user help, decision log with its Feedback section, and change impact note all present and each written for its reader. The plan's verification steps are real commands. The user help describes the deployed version. |
| **Process** | 15 | DMAIC checkpoints hit on the dates above. `v0.9.0` and `v1.0.0` tags. `CHANGELOG.md`. A commit at the end of every block, spread across the week. |
| **Demonstration** | 10 | The demo score sheet above. |
| **Polish** | 10 | A stranger can use it on a phone without asking anything. Messages are plain. Nothing looks broken when something optional is missing. |

**The fastest way to lose Process points** is one enormous commit Thursday at 10:15 with a tag
on it. Commit at the end of every block.

---

## If you are stuck

**"My deploy failed and I do not know why."** Open the deploy log and read the last ten lines
before changing anything. Then change one thing, push, and read the log again. Changing three
things at once is how an hour disappears.

**"It works on my laptop."** Run it the way Render does: set `PORT` yourself, request it through
your network address, and stop the model. If all three work locally, the problem is almost
always a missed commit or a wrong start command.

**"My project does not have anything to put in a change impact note."** It does. Deploying
changed it. Turning off a feature that cannot work on a shared server, shortening a timeout,
adding a health route, or labelling a fallback are all real changes to a baseline.

**"Render is asking for a credit card."** Stop. Do not enter one. Tell your teacher.

**"My decision log only has three things."** Every requirement above is a decision. How you
track visitors, what the fallback says, what the timeout is, what you left out and why.
