# Baselines: The Version You Can Always Come Back To
---
## Slide 1: Six small changes and a broken game
- Your app went live Monday
- Since then: a typo fix, a rename, four more tweaks
- Friday morning, nobody can type a command
- Which change did it? What did working look like?
Speaker notes: Here is Thursday night for somebody in this room. The app works Monday. Then a typo fix, a variable rename that seemed tidy, and four other little things. Friday morning, the day of your demo, the game will not accept a single command. Which of the six broke it? What exactly was running when it worked? If you cannot answer both questions in under a minute, you have a configuration management problem, and today you fix it before you have it.
Image: A timeline of six small commit dots with the last one marked in red, navy line, accent blue dots.
---
## Slide 2: Three ideas that are really one
- Version management: every release has a name
- Interface control: know what depends on you
- Baseline: an agreed version you can return to
- Change impact: check what breaks before changing
Speaker notes: Ohio calls this configuration management, and it is on your WebXam tomorrow. It sounds like a big company thing. It is a Thursday night thing. Every release gets a name. You know which parts of your app other things depend on. You keep one agreed version you can always go back to. And before you change anything, you list what it touches. Four bullets, one habit.
Image: Four connected tiles arranged in a loop, navy and accent blue.
---
## Slide 3: Every release has a name
```
MAJOR.MINOR.PATCH

1.4.2  ->  1.4.3   a fix nobody depends on changing
1.4.2  ->  1.5.0   a new feature, everything old still works
1.4.2  ->  2.0.0   something someone depends on breaks

git tag -a v1.0.0 -m "Storm Relay web 1.0.0: first public release"
git push origin v1.0.0
```
Speaker notes: Three numbers. Patch for a fix. Minor for a feature that breaks nothing. Major when something somebody depends on stops working. In Git, a tag pins that name to one exact commit. And here is the failure mode that catches people. Plain git push does not send tags. Your commits reach GitHub and your tag stays on your laptop. Push the tag by name.
Image: None. This slide is code.
---
## Slide 4: Version numbers are not strings
```python
print("1.10.0" > "1.9.0")
print(max(["1.2.5", "1.10.0", "1.9.0"]))

False
1.9.0
```
Speaker notes: Predict before I run it. Is version one point ten newer than version one point nine? Python says no. And the biggest of these three is one point nine. No error, wrong answer, twice. Strings compare one character at a time, and the character one comes before nine. Split the version and convert each part with int before you compare. This is our running thread again. The dangerous bugs are the ones that do not crash.
Image: None. This slide is code.
---
## Slide 5: An interface is anything that depends on you
- URL paths, like /health and /command
- Form field names, like command
- Environment variable names, like PORT
- Save file keys, like room
- Change these on purpose, never in a cleanup
Speaker notes: Your code has an inside and an outside. Renaming a variable inside a function is housekeeping. Renaming something on the outside is a change somebody else feels. Paths other people bookmarked. The name of a form field. The PORT variable the host sets. The keys in save files already sitting on someone's disk. Interface control means those only change deliberately, with a version number and a note.
Image: A box labelled app with arrows coming in from a browser, a host, and a save file, navy and accent blue.
---
## Slide 6: Baselines and lifecycle phases
- Requirements, design, development, testing, deployment, maintenance
- A baseline can be set when a phase ends
- Yours: the tagged release your client accepted
- Maintenance starts the second your app is live
Speaker notes: Software moves through phases. Requirements, design, development, testing, deployment, maintenance. When a phase ends and people agree on the result, that result can become a baseline, a line you measure every later change against. For you, the baseline is the tagged version your teacher or client accepted. And notice the last phase. The moment your app goes live Monday, you are in maintenance, which is the longest phase any real software lives in.
Image: Six phase boxes in a row with a flag planted after deployment, accent blue flag.
---
## Slide 7: The wrong way: a one-word cleanup
```html
<input type="text" id="command" name="cmd" maxlength="40">
```
```
> 
Type a command. Type help to see the list.
```
Speaker notes: Somebody decides cmd is tidier than command. They change the form and forget the server, which still reads command. Now a player types north, the browser sends cmd equals north, and the server finds no command at all. Every command, every player, the same reply. The page loads. The server answers normally. Nothing in the log. The game is unplayable, and nobody got an error message.
Image: None. This slide is code.
---
## Slide 8: One test caught it
```
python -m unittest test_app

FAIL: test_the_form_sends_the_field_the_handler_reads
AssertionError: 'name="command"' not found in '...the whole page...'
Ran 46 tests in 24.191s
FAILED (failures=1, skipped=1)
```
Speaker notes: I shortened the error line, because it prints the entire page. Forty four tests passed. One failed, and it is the only test that checks the form and the handler use the same name. Every other test sends command straight to the server, so without this one test, that change sails through the whole suite. The form and the handler are two halves of one interface. Tests written for each half separately cannot see the gap between them.
Image: None. This slide is code.
---
## Slide 9: Change impact analysis, before you touch it
- Code: which files change together
- Tests and docs: what must be updated
- Host settings and stored data: what breaks
- People: who notices, and what version number
- Decide: patch, minor, major, or reject it
Speaker notes: Here is the right way. Before touching anything, list what the change touches. Code, tests, documentation, settings on the host, data already stored, and the people who use it. Then decide the version number. For our cmd rename, the answer is reject it. Nothing gets better for a player. Rejecting a change is a real, respectable outcome of an impact analysis, and often it is the best one.
Image: A checklist with the final row reading reject, circled in accent blue.
---
## Slide 10: What you are about to build
- Build 1: Lab U8-02 Part 3, one real change request
- Predict what breaks, then make it and check
- Build 2: GP2 exam, 50 minutes
- Tomorrow: WebXam post-test, then tag your release
Speaker notes: Build one is Lab U8 two, part three. You get one real change request for Playlist Namer. You write the impact analysis first, predicting what breaks. Then you make the change on a branch, run the checker, and compare what broke with what you predicted. Comparing the two is the point of the lab. Build two today is the grading period exam. Tomorrow you take the WebXam post-test first, then you tag your release and write your change impact note.
Image: A two-column sheet labelled predicted and actual, navy and accent blue.
---
