# Protect What Already Works
---
## Slide 1: A small change, two days before the demo
- Every acceptance check passed yesterday
- The stakeholder asks for one small addition
- You make it straight on main
- Tomorrow three old checks fail and nobody knows why
Speaker notes: Yesterday every acceptance check passed. That version is the one your stakeholder is about to accept. This morning they ask for one small reasonable change. The fastest thing is to type it straight into main. And that is how teams break things that already worked, two days before a demo. Today you learn three things that protect accepted code: a baseline, a branch, and an impact analysis.
Image: A finished tower of blocks with one hand reaching in to swap a block near the bottom, navy and blue.
---
## Slide 2: A baseline is what they accepted, exactly
- Reviewed and accepted, then recorded
- Not roughly what we had on Tuesday
- You can always return to it and compare
- Every lifecycle phase can end in one
Speaker notes: A baseline is a version that was reviewed and accepted, and recorded so it can be identified exactly later. Not roughly what we had Tuesday. Exactly. Your signed requirements were a baseline for Define and Measure. The program with every check passing is the baseline for Improve. Anything that changes a baseline goes through a change process, and today you run that process once for real.
Image: A single commit dot on a timeline with a flag labeled v1.0 planted on it, navy line and blue flag.
---
## Slide 3: Name it, then share the name
```
git tag -a v1.0 -m "Accepted baseline: all acceptance checks passing"
git push origin v1.0
```
Speaker notes: In Git, a tag is a permanent name on one commit. Unlike a branch, it does not move when you commit again. The second line is the one people forget. A normal git push does not send tags. Without git push origin v one point oh, your baseline only exists on the laptop you tagged it on, and if that laptop dies, nobody can say which commit was accepted.
Image: None. This slide is code.
---
## Slide 4: Change on a branch, not on main
```
git switch -c cr-1-leading-bin
git push origin cr-1-leading-bin
git diff v1.0 --stat

git switch main
git merge cr-1-leading-bin
git tag -a v1.1 -m "CR-1 merged after review"
git push origin main v1.1
```
Speaker notes: A branch is a separate line of commits that does not touch main until you merge it. Create the branch, build the change there, and push it so another team can review it tomorrow. git diff against v one point oh shows exactly which files changed since the baseline. Only after the review approves it do you switch back to main, merge, tag v one point one, and push both. If Git ever reports a merge conflict today, stop and get me.
Image: None. This slide is code.
---
## Slide 5: Impact analysis, before any code
- Changes directly: the function you will edit
- Uses something that changes: every caller, every check
- Must NOT change: everything else
- Prove column three by rerunning every check
- Write it down before editing a line
Speaker notes: Impact analysis answers one question before you touch anything. If this changes, what else changes. Column one is the function you will edit. Column two is everything that calls it and every check that tests those. Column three is everything that must not change, and that is the column the stakeholder cares about most, because their request always ends with please do not break anything. You prove column three by rerunning every check.
Image: A three-column table with the third column highlighted, headers only, navy and blue.
---
## Slide 6: A baseline you can prove
```python
import hashlib

def fingerprint(path):
    """Fingerprint the file's CONTENTS. One changed byte changes it."""
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()

print(fingerprint("points.py")[:12])
```
Speaker notes: Git does this for you, but here is what a baseline is underneath. A fingerprint is a long code calculated from a file's contents. Change one character and you get a completely different code. hashlib is in the standard library, and Git uses the same idea to name every commit. Record a fingerprint for every file at the baseline, and later you can prove exactly which files changed.
Image: None. This slide is code.
---
## Slide 7: Watch this
```python
import hashlib

def fingerprint(path):
    """Return a fingerprint of the file."""
    return hashlib.sha256(path.encode("utf-8")).hexdigest()

before = fingerprint("project/points.py")
with open("project/points.py", "a", encoding="utf-8") as file:
    file.write("# a change nobody reviewed\n")
after = fingerprint("project/points.py")
if before == after:
    print("Changed since baseline: False")
else:
    print("Changed since baseline: True")
```
Speaker notes: A teammate writes fingerprint a little differently. Then the program appends a line to points dot py, a real change, and compares the fingerprints from before and after. Predict the output.
Image: None. This slide is code.
---
## Slide 8: A safety check that cannot see
```
Changed since baseline: False
```
Speaker notes: No error. The file really changed and the program says it did not. path dot encode fingerprints the file's name, not its contents. The name never changes, so the check passes forever, on any edit, including the one that breaks your demo. This is the worst kind of silent bug, a safety check that does not check. A test that agrees with the bug. A checker with zero findings on broken code. Always prove a safety check can fail.
Image: None. This slide is output.
---
## Slide 9: Map what a change can reach
```python
depends_on = {
    "points_for": ["receipt line", "end-of-day balances", "AC-2.1", "AC-2.2"],
    "read_orders": ["skipped count", "AC-1.1", "AC-1.2"],
    "receipt": ["register screen", "AC-3.1"],
}
functions_touched = ["points_for", "receipt"]
for name in functions_touched:
    print(name, "affects:", ", ".join(depends_on[name]))
```
Speaker notes: Files are too coarse. The real question is which behaviors a change can reach. Before editing, list the functions you will touch and look up what depends on each one. Now you know which checks must still pass unchanged, which ones have to change, and which new checks the change needs. That list becomes your change impact record.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: tag v1.0 and push the tag
- The change request arrives. Impact record first.
- Then create your change branch
- Build 2: build the change on the branch, checks passing
- Tomorrow another team reviews it before you merge
Speaker notes: Build one. Confirm every check passes, tag v one point oh, and push the tag. Then I hand out your stakeholder's change request. Before a single line of code, fill in the change impact record, all three columns. Then create your branch. Build two, build the change on that branch. Every old check still passes, and the change gets new checks. Tomorrow another team reviews your branch against the baseline before anything touches main.
Image: A branch line splitting from a tagged main line and rejoining later at a second tag, navy and blue.
---
