# Two Readers: Implementation Plans and User Help
---
## Slide 1: Your laptop dies Thursday night
- Your app is live and your demo is Friday
- A classmate has to redeploy it without you
- A player opens your link knowing nothing
- Neither of them can ask you anything
Speaker notes: Picture it. Thursday night your laptop will not turn on. Your app needs a fix before Friday and a classmate offers to redeploy it. Meanwhile somebody opens your link and has never played a text adventure in their life. Neither person can text you a question. Everything they know comes from what you wrote down. That is what documentation is. You, answering questions before anybody asks them.
Image: A dark laptop on a desk beside a phone showing a web page, deep navy and accent blue.
---
## Slide 2: One document, one reader
- Implementation plan: the person who deploys and maintains it
- User help: the person who uses it
- Different questions, different words
- Write for them, never for yourself
Speaker notes: Every document has exactly one reader. The implementation plan is for whoever deploys and maintains the app, and that might be you in three months, which is basically a stranger. User help is for the person playing, who does not know what Python is and should never have to. Same project. Two readers. Two completely different documents.
Image: Two simple silhouettes, one at a terminal and one holding a phone, each with its own document icon.
---
## Slide 3: What the implementation plan must answer
- What version, from which tag, to which URL
- Numbered steps, each saying what success looks like
- Settings table: the data dictionary
- How to prove it worked, with real commands
- What to do if it breaks: the contingency plan
Speaker notes: Five questions. Which exact version is going out, and from which Git tag. Numbered steps, and every step tells the reader what they should see when it worked. A table of every setting, which is your data dictionary. A verification section with real commands and real expected output. And a contingency plan, which mostly means how to roll back to the version that worked yesterday. Ohio names all four document types, and you are writing all of them today.
Image: A numbered checklist with a small table beneath it, navy lines, accent blue numbers.
---
## Slide 4: A verification step is a real command
```
curl.exe -s http://127.0.0.1:10000/health
{"status": "ok", "version": "1.0.0", "narrator": "not asked yet"}

curl.exe -s http://127.0.0.1:10000/health
{"status": "ok", "version": "1.0.0", "narrator": "not answering"}
```
Speaker notes: Here is the difference between check that it works and a step somebody can follow. Run this command, expect this output. Nothing to interpret. The second line is from after one page loaded, and it says not answering, because there is no model. On Render that is the correct result, and the plan says so in writing, so nobody panics about an outage that is not one.
Image: None. This slide is code.
---
## Slide 5: A plan written by someone who already knows
```
1. Open a terminal.
2. Run python playlist_namer.py
3. Open http://127.0.0.1:8000 and type a mood.
```
Speaker notes: This plan was written by somebody who knows the project well. It looks complete. Three steps, each one short. I am going to follow it exactly as written, the way a classmate would, starting with step one, open a terminal. Watch what happens at step two. Do not help me.
Image: None. This slide is code.
---
## Slide 6: The wrong way, and the real error
```
python playlist_namer.py

C:\Python313\python.exe: can't open file
'C:\\Users\\...\\playlist_namer.py': [Errno 2] No such file or directory
```
Speaker notes: A new terminal does not open in the app's folder. The writer never noticed, because their terminal was already in the right place. That is one of the most common documentation failures. The missing step is always the one you do without thinking, and nobody writes down what they do automatically. The part before the colon is where Python lives on this machine, so yours will look a little different.
Image: None. This slide is code.
---
## Slide 7: The fix is a tester, not more care
- Hand your plan to someone else
- Watch them follow it without helping
- Every time you say "oh, you have to" write it down
- Rereading your own plan does not work
Speaker notes: You cannot find this bug by rereading, because your brain fills the gap every time, the same way it did when you wrote it. The fix is a tester. Somebody else follows your plan while you sit on your hands. Each time you want to say oh, you have to, that is a missing step, and it goes in the plan. It is uncomfortable, and it works every time.
Image: Two students at one screen, one typing, one with hands folded and a notepad, navy and accent blue.
---
## Slide 8: User help makes promises too
```
Help page:  Type save at any time to keep your progress.

> save
Saving is turned off on the web version. Every visitor shares one server,
and it forgets everything when it restarts.
```
Speaker notes: This help text was copied from the laptop version of the game, where it was true. The web version deliberately turns saving off. So the help page promised something the app will not do. The player believed it, lost their game, and now believes nothing else on that page. Deploying a program changes it, and the help has to describe the version people actually use.
Image: None. This slide is code.
---
## Slide 9: Same fact, two readers
- Plan: model requests fail, log says model failed
- Plan: this is expected on Render, do not fix it
- Help: descriptions here are written by hand
- Help: the game plays the same either way
Speaker notes: One fact. There is no model on Render. For the deployer, you name the log line and the health output, and you say plainly that it is expected, so nobody opens a lab machine to the internet trying to fix it. For the player, no log, no model, no Render. Descriptions here are written by hand. Same truth, and not one word in common.
Image: A single fact card splitting into two cards, one technical in navy, one plain in accent blue.
---
## Slide 10: What you are about to build
- Build 1: Lab U8-02, your own project's plan and help
- Push, then a partner clones and follows your plan
- You may not speak while they follow it
- Build 2: Gate 2, the last one of the semester
Speaker notes: Build one is Lab U8 two, parts one and two, and it is not practice. You write the implementation plan and the user help for your own final project, because those are due Thursday. Then you push, a partner clones your repository into a fresh folder and follows your plan exactly as written, and you sit on your hands. A fresh clone only has what you committed, which is exactly what Render gets. Build two is Gate 2, the last one this semester, and one of its defects only shows up the way Render runs code.
Image: Two students at one screen, one following a printed plan, one silent with a notepad, navy and accent blue.
---
