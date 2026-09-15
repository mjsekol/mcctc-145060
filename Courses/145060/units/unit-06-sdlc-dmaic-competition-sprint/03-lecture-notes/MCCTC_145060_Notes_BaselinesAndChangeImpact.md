# Lecture Notes: Baselines, Branches, and the Impact of a Change
## 145060 Programming · Unit 6 · Week 14, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W14_BaselinesAndChange.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W14_BaselinesAndChange.pptx)

If you missed class, you can learn this concept from this file alone. Type and run
every Python example.

**Competencies introduced here, assessed in Unit 8:** 5.7.1 (version management), 5.7.2
(baseline and software lifecycle phases), 5.7.3 (analyze the impact of changes). Also 5.1.8
(version control) from Unit 0, used at a new level.

**This is a first look, on purpose.** Configuration management is 6.67% of the WebXam and it is
taught fully in Unit 8. Today you use it once, for real, on your own sprint, so that Unit 8 has
something to build on.

---

## Why this exists

Yesterday every one of your acceptance checks passed. That version of your program is the one
the stakeholder is going to accept. It is valuable, and right now it is also fragile, because
the next commit anybody makes changes it.

This morning your stakeholder sends a change request. It is small and reasonable. And it is the
most dangerous moment of the sprint, because a small reasonable change to accepted code is how
teams break things that already worked, two days before a demo.

Three ideas protect you:

1. **A baseline:** a named, recorded version you can always get back to and compare against.
2. **A branch:** a separate line of work, so the change does not touch the baseline until it is
   reviewed.
3. **Impact analysis:** working out what a change will affect **before** you make it.

---

## The concept in plain language

### Baseline

A **baseline** is a version of the software that was reviewed and accepted, and is recorded so
that it can be identified exactly later. It is the answer to "what did the stakeholder accept?"
Not "roughly what we had on Tuesday." Exactly.

Baselines line up with **lifecycle phases.** Signed requirements are a baseline for Define and
Measure. The accepted program is a baseline for Improve. The version handed to the stakeholder is
the baseline Control protects. Anything that changes a baseline goes through a change process.

### Tags: naming a baseline in Git

A **tag** is a permanent name on one commit. Unlike a branch, it does not move when you commit
again.

```
git tag -a v1.0 -m "Accepted baseline: all acceptance checks passing"
git push origin v1.0
```

The second line matters. **Tags are not pushed by a normal `git push`.** Without it, your
baseline exists only on the machine you tagged it on.

### Branches: a separate line of work

A **branch** lets you commit a change without changing `main`. You create one, work on it, get it
reviewed, and only then merge it back.

```
git switch -c cr-1-leading-bin      # create the branch and move onto it
# ... edit, run tests, commit as usual ...
git push origin cr-1-leading-bin    # share the branch for review
git diff v1.0 --stat                # which files changed since the baseline
```

After Review 2 approves the change:

```
git switch main
git merge cr-1-leading-bin
git tag -a v1.1 -m "CR-1 merged after review"
git push origin main v1.1
```

**Verification note.** The Git commands in this file were not executed while this lesson was
written, because the authoring rules for this repository do not allow running Git. They are
standard Git commands for Git 2.23 and later. Your instructor confirms their exact output on a lab
machine before this lesson. Every Python example below was executed and its output is real.

**If Git reports a merge conflict,** stop and get your instructor. Resolving conflicts is taught in
145065. Today's changes are small enough that most teams will not hit one.

### Impact analysis

**Impact analysis** is answering, before you touch code: if this changes, what else changes? It
has three columns:

| Changes directly | Uses something that changes | Must NOT change |
|---|---|---|
| The function you will edit | Everything that calls it, and every check that tests them | Everything else, which you prove by rerunning all checks |

The third column is the one teams skip, and it is the one the stakeholder cares about. Their
change request almost always ends with some version of "please do not break anything."

---

## Worked example 1: a baseline you can prove

Git records baselines for you. To see what a baseline really is underneath, this program builds one
by hand: a **fingerprint** of every file's contents.

`baseline.py`:

```python
# baseline.py
# Records a fingerprint of every file in a folder, so you can prove later
# exactly what the accepted version contained.
#
# Usage:  python baseline.py project v1.0

import hashlib
import json
import os
import sys


def fingerprint(path):
    """Return a SHA-256 fingerprint of the file's CONTENTS. One changed byte changes it."""
    with open(path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


def build_manifest(folder):
    """Return a dictionary from each file name in the folder to its fingerprint."""
    manifest = {}
    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            manifest[name] = fingerprint(path)
    return manifest


if __name__ == "__main__":
    folder = sys.argv[1]
    label = sys.argv[2]
    manifest = build_manifest(folder)
    with open(f"baseline_{label}.json", "w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=2)
    for name in manifest:
        print(f"{manifest[name][:12]}  {name}")
    print(f"Baseline {label}: {len(manifest)} files recorded")
```

With a `project` folder holding `README.md`, `orders.csv`, and `points.py`:

```
$ python baseline.py project v1.0
2e7b80ddfbb6  README.md
09f449137d07  orders.csv
064141003ea7  points.py
Baseline v1.0: 3 files recorded
```

**Your fingerprints will be different** unless your files are byte-for-byte identical to these,
including line endings. That is the point. A **SHA-256 fingerprint** is a long code calculated from
a file's contents, and changing a single character produces a completely different code. `hashlib`
is in the standard library. Git uses the same idea to name every commit.

---

## Worked example 2: what changed since the baseline?

`impact.py`:

```python
# impact.py
# Compares a folder to a recorded baseline and reports what changed since.
#
# Usage:  python impact.py project baseline_v1.0.json

import json
import sys

import baseline

folder = sys.argv[1]
with open(sys.argv[2], encoding="utf-8") as file:
    recorded = json.load(file)
current = baseline.build_manifest(folder)

changed = []
for name in recorded:
    if name in current and current[name] != recorded[name]:
        changed.append(name)

print("Changed:", changed)
print("Added:  ", sorted(set(current) - set(recorded)))
print("Removed:", sorted(set(recorded) - set(current)))
```

After editing `points.py` for the change request and adding a new `game_days.txt`:

```
$ python impact.py project baseline_v1.0.json
Changed: ['points.py']
Added:   ['game_days.txt']
Removed: []
```

This is what `git diff v1.0 --stat` tells you, built from parts you already know: a dictionary, a
loop, and set subtraction from Unit 5.

---

## Worked example 3: before the change, map what depends on it

Files are too coarse. The real question is which **behaviors** a change can reach.

```python
# impact_map.py
# Before you change a function, look up everything that depends on it.
depends_on = {
    "points_for": ["receipt line", "end-of-day balances", "AC-2.1", "AC-2.2"],
    "read_orders": ["skipped count", "AC-1.1", "AC-1.2"],
    "receipt": ["register screen", "AC-3.1"],
}

change_request = "CR-2: double points on game days"
functions_touched = ["points_for", "receipt"]

print(change_request)
for name in functions_touched:
    print(f"  {name} affects: {', '.join(depends_on[name])}")
```

Output:

```
CR-2: double points on game days
  points_for affects: receipt line, end-of-day balances, AC-2.1, AC-2.2
  receipt affects: register screen, AC-3.1
```

Now you know which checks must still pass unchanged, which must change, and which new checks the
change needs. **Write that down in `docs/change_impact.md` before editing a single line.**

---

## The wrong version, and what it does instead of an error

A teammate writes the fingerprint function slightly differently.

```python
import hashlib
import os


def fingerprint(path):
    """Return a fingerprint of the file."""
    return hashlib.sha256(path.encode("utf-8")).hexdigest()


before = fingerprint(os.path.join("project", "points.py"))
with open(os.path.join("project", "points.py"), "a", encoding="utf-8") as file:
    file.write("# a change nobody reviewed\n")
after = fingerprint(os.path.join("project", "points.py"))
print("Changed since baseline:", before != after)
```

Output:

```
Changed since baseline: False
```

**No error. The file really did change, and the program says it did not.**

`path.encode("utf-8")` fingerprints the file's **name**, not its contents. The name never changes, so
the fingerprint never changes. The baseline check passes forever, on any edit, including the one that
breaks the demo.

This is the most dangerous shape of silent bug, because it is a **safety check** that does not check.
A test that agrees with the bug. A static checker that reports zero findings on broken code. A
baseline that cannot see changes. Each one produces a reassuring answer and stops people looking.

---

## Why the wrong version is tempting

**Both versions return a long, official-looking code.** Nothing about the output reveals which one you
have.

**The path is right there.** The function receives a path, and hashing the thing you were handed feels
natural. Reading the file is an extra step.

**Nobody tests the tester.** The fix is to prove the safety check can fail: change a file on purpose and
confirm the check notices. If you cannot make a check fail, you do not know that it works.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Configuration management** | Keeping track of exactly which versions of every part make up the software. |
| **Version management** | Recording, naming, and retrieving versions over time. |
| **Baseline** | A reviewed, accepted version recorded so it can be identified exactly. |
| **Tag** | A permanent Git name on one commit, such as `v1.0`. |
| **Branch** | A separate line of commits that does not change `main` until merged. |
| **Merge** | Bringing a branch's commits into another branch. |
| **Change request** | A written request from the stakeholder to change accepted behavior. |
| **Impact analysis** | Working out what a change will affect before making it. |
| **Fingerprint (hash)** | A code calculated from contents. Any change to the contents changes it. |
| **Lifecycle phase** | A stage of the software's life. Each one can end in a baseline. |

---

## Self-check

**Question 1.** Your team tagged `v1.0` on Wednesday morning and pushed `main` but not the tag. Your laptop
dies. What is lost, and what command would have prevented it?

**Question 2.** A change request says: "Show the leading bin in the announcement. Please do not break
anything." Fill in the three impact analysis columns for the reference Food Drive program, using
`announcement()`, `main()`, the test file, and `build_report()`.

**Question 3.** Predict the exact output. Assume `notes.txt` does not exist yet.

```python
import hashlib

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("v1")
first = hashlib.sha256(open("notes.txt", "rb").read()).hexdigest()

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("v1")
second = hashlib.sha256(open("notes.txt", "rb").read()).hexdigest()

print(first == second)
```

---

### Answers

**1.** The name `v1.0` is lost, because tags are not sent by a normal `git push`. The commits themselves
are safe on GitHub, but nobody can say with certainty which commit was the accepted baseline.
`git push origin v1.0` would have prevented it.

**2.**

| Changes directly | Uses something that changes | Must NOT change |
|---|---|---|
| `announcement()`: new sentence, AC-5.1 text, and the 200-character limit in AC-5.2 is at risk | `main()` must pass the bin ranking in. The test file's calls to `announcement()` need the new argument. | `build_report()` and every R1 to R4 and R6 check, proved by rerunning the whole test file |

The full version is `09-project/reference-implementation/docs/change_impact.md`.

**3.** Output: `True`

The file was rewritten, but with the same contents, so the fingerprint is identical. A fingerprint
tracks contents, not activity. Saving a file without changing it is not a change.
