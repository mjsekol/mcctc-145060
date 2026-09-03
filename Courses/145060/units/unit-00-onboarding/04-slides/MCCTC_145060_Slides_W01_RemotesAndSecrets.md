# Remotes, and the Mistake You Cannot Undo
---
## Slide 1: Your laptop is not a plan
- One spilled drink and the repository is gone
- You cannot hand the project to anyone
- You cannot open it on another machine
- Today it gets a second home
Speaker notes: Right now your entire semester exists in one folder on one machine. If that machine dies tonight, everything you did this week is gone, and the version history you built yesterday goes with it. Today we fix that. And in the middle of fixing it, I am going to show you the one mistake this course can teach you that you genuinely cannot take back.
Image: A single laptop icon with a fracture line through it, navy on light background.
---
## Slide 2: A remote is a fourth place
- Working directory, staging area, repository
- Now: a copy of your history on GitHub
- git push sends commits to it
- Push sends commits, not your folder
Speaker notes: Yesterday we had three boxes and I told you there was a fourth one coming. Here it is. A remote is a copy of your history living on another machine. Ours live on GitHub. Read that fourth bullet twice, because it costs people about two weeks. Push sends commits. If you edited a file and did not commit it, pushing sends nothing new, and you will stand there wondering why GitHub looks out of date.
Image: The three navy boxes from yesterday with a fourth box added, connected by an arrow labeled git push.
---
## Slide 3: Connecting and pushing
```
git remote add origin https://github.com/aruiz/trip-budget.git
git push -u origin main
git remote -v
```
Speaker notes: Two commands you run once, and one you run whenever you want to check. Origin is a nickname, not a keyword. It is what everybody calls their main remote and you could call it anything. The dash u means remember this pairing, so every push after today is git push with nothing after it. Somebody will ask what dash u does and that is the answer.
Image: None. This slide is code.
---
## Slide 4: Pushing is publishing
- The instant you push, you handed over a copy
- You cannot reach into someone else's clone
- GitHub scans public repos for leaked credentials
- Your signed lab agreement, section 2
Speaker notes: This is the part I want you awake for. Push is not save. Push is publish. The moment you push, a copy exists somewhere you do not control, and depending on your settings, possibly a copy everyone can read. This happens to working professionals often enough that GitHub runs an automated service that scans public repositories for credentials and tells the companies that issued them. The agreement you and a parent signed says it in section 2. Credentials never go in a repository. In four minutes you will see why that rule exists.
Image: One repository icon with arrows branching out to several anonymous machine icons, one-way arrows only.
---
## Slide 5: Watch me make the mistake
```
OPENAI_API_KEY=sk-not-a-real-key-1234567890
```
```
git add secrets.txt
git commit -m "Add settings file"
```
Speaker notes: This key is fake. I am typing it by hand and it opens nothing. But I am doing exactly what a student in a hurry does at eight fifty on a Thursday. I have a file with a credential in it and I am committing it without looking. Nothing is going to stop me. Git will not warn me. Watch.
Image: None. This slide is code.
---
## Slide 6: Now I fix it the way everybody fixes it
```
echo secrets.txt > .gitignore
git add .gitignore
git commit -m "Add gitignore"
```
```
On branch main
Changes not staged for commit:
        modified:   secrets.txt
```
Speaker notes: I realized the mistake. So I did the thing every single person does first: I added it to gitignore and committed. Status is clean. The filename is in the file. Every visible signal says handled. Now watch what happens when I edit that secrets file and check status. Git is still tracking it. The gitignore did nothing.
Image: None. This slide is code.
---
## Slide 7: The rule nobody tells you first
- gitignore controls files Git is not yet tracking
- It has no effect on a file already tracked
- Status looked clean. It was not
- Absence of an error is not success
Speaker notes: There it is. Gitignore governs whether Git starts tracking something. Once a file is in the history, gitignore is talking about a decision that was already made. Say that back to me before we move on, because the next two minutes only make sense if this one landed. And notice the second half. Nothing turned red. Nothing said error. You have to know what to check.
Image: A gate with new files being turned away and one file already inside the fence, unaffected.
---
## Slide 8: So stop tracking it. Did that work
```
git rm --cached secrets.txt
git commit -m "Stop tracking the settings file"
git log --oneline -- secrets.txt
```
```
b151592 Stop tracking the settings file
38cc1b2 Add settings file
```
Speaker notes: Git rm cached does work. It stops the tracking, and future changes are ignored. So I ask the only question that matters. Is the key gone. Look at the bottom of the screen. Commit 38cc1b2 still contains it. Anyone who clones this repository reads that key in about four seconds. And if I had pushed before I noticed, other people already have their own copy that nothing I type can reach.
Image: None. This slide is code.
---
## Slide 9: Nothing on this list fixes it
- gitignore: nothing, the file was already tracked
- Delete and commit: old commit still has it
- rm cached: old commit still has it
- Make it private: existing clones still have it
Speaker notes: Read that list. Not one of those works, and those are the four things people try. The only action that resolves this is changing the secret. Revoke the key, get a new one, update everywhere that used it, and treat the old one as public from now on, because it is. Sit with how unsatisfying that is. Almost every mistake you make this year is undoable. This one is not, and that is exactly why the habit matters more than the recovery.
Image: A four-row table, every row marked with the same grey cross, navy header.
---
## Slide 10: Which is why gitignore comes first
- Write gitignore before the first commit
- Not after the mistake. Before
- git add dot is fast, and stages everything
- That includes what you did not mean to add
Speaker notes: Now yesterday's ordering rule makes sense. Gitignore is commit number one, before there is anything to protect, because after is too late. And a warning about the command you are all going to find on the internet tonight. Git add dot stages everything in the folder. It is fast, it is convenient, and it is how most leaked credentials get staged. There is a safe way to use it. It needs a gitignore written first and a status read every time, and both of those are doing real work.
Image: A timeline with gitignore as the first commit, then other commits after it, accent blue.
---
## Slide 11: What you are about to build
- Create the GitHub repo, connect it, push
- Write a README a stranger can actually use
- Finish lab U0-01, steps seven through twelve
- Nothing in your repo contains a key or password
Speaker notes: Three things. Get your repository on GitHub and confirm your log matches. Write a README that names what the program is rather than what assignment it was, and includes the exact command that runs it. Then finish the lab, which completes SQ-01, and SQ-01 has to be done before anything else you turn in gets graded. At close you are reading somebody else's README and telling them one thing you could not figure out from it.
Image: A GitHub repository page with a rendered README, navy and accent blue, no faces.
---

