# Commits and History
---
## Slide 1: The group project that went wrong
- Somebody had the file, somebody had a newer one
- One was named final underscore FINAL underscore v2
- Work got overwritten and nobody could prove it
- You lost information about time
Speaker notes: Every one of you has lived this. A group project, two versions, nobody can tell which is newer, and somebody's work is gone. I want you to notice what you actually lost, because it was not the file. You could see what the file was now. You could not see what it was before, who changed it, or why they did. That missing information has a name and a tool, and you are getting both today.
Image: Two document icons side by side with confusingly similar filenames, a question mark between them.
---
## Slide 2: Git is not backup
- Backup answers one question: where is my file
- Git answers: what did it look like before
- And who changed it, and why
- The why is the half you write yourself
Speaker notes: Get this distinction now and the rest of the week goes smoothly. Backup is a copy of the current thing. Git keeps every version, plus who made it and when, plus one thing no tool can generate for you: what you were trying to do at the time. That last part is the commit message. It is the reason commit messages are graded work in this class and not a formality.
Image: Left side one document labeled now. Right side a stack of documents on a timeline.
---
## Slide 3: Git does not watch your folder
- It takes photographs when you ask
- git add chooses what is in the photo
- git commit takes it and captions it
- Three places, and changes move in order
Speaker notes: This is the sentence to memorize. Git does not watch your folder. It is not Google Docs and it is not a save button. It takes a photograph when you ask it to, and you choose what is in the frame. I am going to draw three boxes and we are staying with these three all week. There is a fourth place, and you get it tomorrow, not today.
Image: Three navy boxes left to right labeled working directory, staging area, repository, with accent blue arrows labeled git add and git commit.
---
## Slide 4: The three commands
```
git init -b main
git status
git add status_card.py
git commit -m "Add status card that prints my name and day 1 goal"
git log --oneline
```
Speaker notes: Five lines, three of which do real work. Init creates the repository. Add chooses. Commit takes the photograph. Status and log are you asking questions, and they never change anything, which means you can run them as often as you want and you should. I run status more than any other Git command and so will you.
Image: None. This slide is code.
---
## Slide 5: Read what the tool tells you
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        status_card.py

nothing added to commit but untracked files present (use "git add" to track)
```
Speaker notes: Look at how much is in here. No history yet. There is a file Git has never been told about, which is what untracked means. And nothing is lined up to commit. Now find something else. Git printed the fix twice, in parentheses, in its own output. You are going to spend this year not reading output like this, and I am asking you to start reading it today instead.
Image: None. This slide is code.
---
## Slide 6: Now I break it on purpose
- I write the file. I save it in VS Code
- I run git commit with a message
- Nothing turns red. Nothing says error
- Nothing gets committed either
Speaker notes: Watch this. I am doing exactly what feels correct. I wrote the file, I saved it, and I am committing it with a real message. This is what almost every one of you will do tomorrow morning without thinking about it. It does not crash. It does not turn red. And nothing happens. Read the last line with me.
Image: A terminal window with a calm-looking multi-line Git message, no red text anywhere.
---
## Slide 7: A commit is not a save
- A save is a save. Nothing more
- A commit is a save you named and can find
- Saving puts changes on disk
- Git is not watching the disk
Speaker notes: Here is the whole misconception in one line. You have twelve years of training that saving means done, because in every other program you have used, it does. Git splits it into two steps on purpose. The cost of that split is real and it lands this week. The payoff does not arrive until Unit 4, when your project has enough files that unrelated changes are in flight at the same time. I am not going to pretend the cost is not there.
Image: Left panel a floppy or save icon. Right panel a photograph with a handwritten caption underneath.
---
## Slide 8: Why there is a staging area
- Real work changes five files at once
- Two of them belong to a different idea
- Staging is where you choose
- Trivial today. Not trivial by Unit 4
Speaker notes: You fixed a bug in one file and started an unrelated feature in another. Those belong in two commits with two messages, because in six weeks you will want to find the bug fix without dragging the half-finished feature along with it. On a four line program, that choice is meaningless and typing git add feels like busywork. You are not wrong about that today. Ask me again in October.
Image: A diagram showing five changed files with two selected and moving into a commit box.
---
## Slide 9: Messages that are worth writing
- update, fixed, changes: worth nothing
- The diff already shows what changed
- Your message is the only record of why
- Complete this: "This commit will..."
Speaker notes: Both of these commits contain identical code. One says update. One says fix crash when the player types an exit that does not exist. Six weeks from now you scroll forty commits named update and you have to open every single one. Here is the test. A good message completes the sentence this commit will, and it says something the diff cannot say on its own. The diff already shows what characters changed. Only you know why.
Image: A commit list, three greyed-out vague messages and two in accent blue that are specific.
---
## Slide 10: What you are about to build
- Rebuild your repo in the right order
- gitignore written before the first commit
- Two commits minimum, real messages on both
- Then lab U0-01, steps one through six
Speaker notes: Two blocks. First you rebuild the repository properly, and the order matters: gitignore gets committed first, before anything else exists. You will find out tomorrow why that ordering is not a style preference. Then you start the lab. The bar for done today is that git log oneline shows at least two commits and not one of the messages is update, stuff, fixed, or your own name. At close, somebody's log goes on the projector and we read it out loud.
Image: A terminal showing a clean two-line git log oneline output with descriptive messages.
---

