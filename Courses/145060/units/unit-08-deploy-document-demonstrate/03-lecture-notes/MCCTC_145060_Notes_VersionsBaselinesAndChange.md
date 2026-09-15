# Lecture Notes: Versions, Baselines, and the Impact of Change
## 145060 Programming · Unit 8 · Week 18, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W18_BaselinesAndChange.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W18_BaselinesAndChange.pptx)

If you missed class, you can learn this concept from this file alone. This concept is on
the WebXam, and it is the last new idea of the semester. **Outcome 5.7, Configuration
Management, is 6.67% of the exam and this is the only full lesson on it.** You met pieces
of it in the Unit 6 sprint. Today it gets its names.

**About the Git commands in this file.** They are standard Git. Their printed output is
not reproduced here, because it was not captured when these notes were written. Your
teacher runs them before class. Run them yourself and read what Git says.

---

## Why this exists

Your app is live. On Thursday you notice a typo on the help page and fix it. On Thursday
night you rename a variable to make the code cleaner. Friday morning the game does not
accept commands, and you have no idea which of your six small changes did it, or what the
working version looked like.

That is what happens without configuration management. It is not a big-company problem.
It is a Thursday-night problem, and every project that is used by anybody has it.

---

## The concept in plain language

**Configuration management is knowing exactly what version is running, having a named
version you can always return to, and checking what a change will break before you make
it.**

Three ideas, and they are one idea seen from three angles.

### 1. Version management: every release has a name

A **version** is a specific, frozen state of your project with a name. The name most
software uses has three numbers, `MAJOR.MINOR.PATCH`, a convention called semantic
versioning:

| Change | Which number goes up | Example from 1.4.2 |
|---|---|---|
| A fix that changes nothing anyone depends on | PATCH | 1.4.3 |
| A new feature, and everything old still works | MINOR, and PATCH resets | 1.5.0 |
| Anything that breaks what someone depends on | MAJOR, and the rest reset | 2.0.0 |

In Git, a **tag** attaches a version name to one exact commit:

```
git tag -a v1.0.0 -m "Storm Relay web 1.0.0: first public release"
git push origin v1.0.0
```

**Failure mode: `git push` alone does not send tags.** Your commits reach GitHub and your
tag stays on your laptop. Push the tag by name, then check the repository's tags on
GitHub **[VERIFY: where GitHub lists tags]**.

### 2. Interface control: know what other things depend on

An **interface** is anything outside your code that relies on your code staying the same.
For a web app that includes more than you would guess:

| Interface | Who depends on it |
|---|---|
| The URL paths, like `/health` and `/command` | The host's health check, bookmarks, links people shared |
| Form field names, like `command` | The page's own form, and anything that submits to it |
| The shape of `/health` output | Whoever reads it, including a deployer's verification step |
| Environment variable names, like `PORT` | The host, and every deploy setting |
| Save file keys, like `"room"` | Every save file already on somebody's disk |

**Interface control** means you change those things deliberately, with a new version
number and a written note, never by accident in a cleanup.

### 3. Baselines and lifecycle phases: a line you can come back to

A **baseline** is a version that has been reviewed and agreed on, and becomes the reference
point. Every later change is measured against it, and you can always go back to it. In a
class project, your baseline is the tagged version your teacher or stakeholder accepted.

Software moves through **lifecycle phases**. The names vary a little by team, and this is
the common set:

| Phase | What happens | A baseline you might set at the end |
|---|---|---|
| Requirements | Decide what it must do | The approved requirements |
| Design | Decide how it will do it | The approved design |
| Development | Build it | |
| Testing | Prove it does what the requirements say | The version that passed |
| Deployment | Put it where users can reach it | The released version, tagged |
| Maintenance | Fix, improve, and respond to feedback | Each later release |

Maintenance is the longest phase for any software people use. It is where you are the
moment your app goes live, and it is why the other two ideas matter.

### Change impact analysis: think before you change a baseline

**Change impact analysis** is listing everything a change touches before you make it:
code, tests, documentation, settings on the host, stored data, and the people who use it.
Then you decide whether it is a patch, a minor change, or a breaking one.

---

## Worked example 1: version numbers are not strings

You want to know whether a new release is newer than the one running. Obvious approach:

```python
current = "1.9.0"
new = "1.10.0"
print(new > current)
print(max(["1.2.5", "1.10.0", "1.9.0"]))
```

```
False
1.9.0
```

**No error. Wrong answer twice.** Strings compare one character at a time, and at the
third character `"1"` comes before `"9"`, so `"1.10.0"` sorts as smaller. Version ten
looks older than version nine.

Compare the numbers, not the text:

```python
def as_numbers(version):
    numbers = []
    for part in version.split("."):
        numbers.append(int(part))
    return numbers


print(as_numbers("1.10.0"))
print(as_numbers("1.10.0") > as_numbers("1.9.0"))
print("1.10.0".split(".") > "1.9.0".split("."))
```

```
[1, 10, 0]
True
False
```

The last line is the trap one level down. Splitting gives a list of **strings**, and the
comparison is still text. The dangerous bugs are the ones that do not crash, and this one
reads as correct to almost anyone skimming it.

---

## Worked example 2: working out the next version number

```python
def bump_version(version, change):
    """Return the next version. change is "major", "minor", or "patch"."""
    parts = version.split(".")
    major = int(parts[0])
    minor = int(parts[1])
    patch = int(parts[2])
    if change == "major":
        return f"{major + 1}.0.0"
    if change == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


print(bump_version("1.4.2", "patch"))
print(bump_version("1.4.2", "minor"))
print(bump_version("1.4.2", "major"))
```

```
1.4.3
1.5.0
2.0.0
```

The code is the small half. **The hard half is deciding which word to pass in**, and that
decision is the change impact analysis.

---

## Worked example 3: a one-word change that breaks every player

Storm Relay web 1.0.0 is tagged and live. Its game page has a form:

```html
<input type="text" id="command" name="command" maxlength="40">
```

and the server reads that field:

```python
command = form.get("command", [""])[0]
```

Somebody decides `cmd` is a tidier name, changes it in the form, and forgets the server.
It looks like a one-word cleanup. It is a change to an interface.

**The wrong way: no impact analysis.** A player types `north` and presses Go. The browser
sends `cmd=north`. The server looks for `command`, finds nothing, and treats it as an empty
command. The page shows:

```
>
Type a command. Type help to see the list.
```

Every command. Every player. **No crash and no error in the log.** The page loads, the
server answers 200 and 303 like normal, and the game is unplayable.

Run the test suite and one test catches it:

```
python -m unittest test_app
```

```
FAIL: test_the_form_sends_the_field_the_handler_reads (test_app.RouteTests.test_the_form_sends_the_field_the_handler_reads)
AssertionError: 'name="command"' not found in '<!doctype html>...
Ran 46 tests in 24.191s
FAILED (failures=1, skipped=1)
```

That output is shortened with `...` where the page text runs long. The skipped test only
runs in the teacher's copy of the course files. Forty-four tests passed. **Every other test sends `command` directly, so without that one test, this change
passes the whole suite.** The form and the handler are two halves of one interface, and
only one test was checking that the halves match.

**The right way: the analysis first.** Before touching anything, list what depends on the
name `command`:

| Touches | Impact |
|---|---|
| Code | The form in `render_game_page` and the handler in `handle_post` must change together |
| Tests | Every test that posts `command` must change, plus the form-field test |
| Documentation | None: user help never names the field |
| Host settings | None |
| Stored data | None: nothing saves the field name |
| People | Anything that submits a form to `/command` directly breaks |
| Version | Breaking for direct submitters: 2.0.0. Or accept both names and ship 1.1.0 |
| Worth it? | No. Nothing gets better for a player. Reject the change. |

**Rejecting a change is a legitimate result of an impact analysis.** Often it is the best
one.

---

## Rolling back to the baseline

When a release breaks and you do not know why, go back to the baseline first and
investigate second. Players get a working game while you think.

```
git log --oneline
git revert <commit that broke it>
git push
```

`git revert` makes a new commit that undoes an old one, so history stays honest and nothing
is lost. Whether your host redeploys automatically when you push is a host setting
**[VERIFY: Render auto-deploy on push]**. Then run your implementation plan's verification
step, exactly as written.

Avoid `git reset --hard` followed by a forced push on a shared repository. It rewrites
history other people may already have.

---

## Why the wrong versions are tempting

**Cleanup feels safe.** Renaming for readability is good practice inside a function. The
same rename on something outside the function, like a form field or a save key, is a
different act, and the editor makes them feel identical.

**Tests passing feels like proof.** Tests check what somebody thought to check. A change
that crosses two files can slip between tests written for each file separately.

**Version numbers feel like decoration.** Until you need to know what is running, and
"the latest one" turns out to mean three different commits on three different machines.

**Strings look like numbers.** `"1.10.0"` reads as a number to you. It is text to Python.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Configuration management** | Controlling exactly which version exists, what it contains, and how it changes |
| **Version** | A specific, frozen, named state of a project |
| **Semantic versioning** | `MAJOR.MINOR.PATCH`: breaking, feature, fix |
| **Tag** | A Git name attached to one exact commit, like `v1.0.0` |
| **Interface** | Anything outside your code that depends on it staying the same |
| **Interface control** | Changing interfaces only on purpose, with a version and a note |
| **Baseline** | A reviewed, agreed version that later changes are measured against |
| **Lifecycle phases** | Requirements, design, development, testing, deployment, maintenance |
| **Change impact analysis** | Listing everything a change touches before making it |
| **Breaking change** | A change that makes something that depended on the old version stop working |
| **Backward compatible** | A change after which everything that worked before still works |
| **Rollback** | Returning the running system to an earlier version |
| **Changelog** | A file listing what changed in each version, newest first |

---

## Self-check

**Question 1.** Storm Relay web is at `1.2.0`. Give the next version number for each
change, alone, and say why.

- The help page had a spelling mistake.
- A new `hint` command is added. Every old command still works.
- The save file key `"room"` is renamed to `"location"`, and old save files no longer load.

**Question 2.** Write the exact output.

```python
releases = ["2.0.0", "10.0.0", "9.1.0"]
print(max(releases))
```

**Question 3.** Your team tagged `v1.0.0` Monday after the client approved it. Since then
you have pushed four commits, and Thursday the app is broken. In three sentences: what is
the baseline, what should you do first, and why that order?

---

### Answers

**1.** Spelling fix: `1.2.1`, a patch, because nothing anyone depends on changes. New
`hint` command: `1.3.0`, a minor version, because it adds a feature and everything old
still works. Renamed save key: `2.0.0`, a major version, because every existing save file
stops loading, which breaks something people depend on. The better plan is to read both
keys so old saves still load, and ship it as `1.3.0` instead.

**2.**

```
9.1.0
```

Text comparison, one character at a time. `"9"` is greater than `"2"` and greater than
`"1"`, so `"9.1.0"` wins, even though version 10 is the newest.

**3.** The baseline is `v1.0.0`, the version the client approved and you tagged. First, get
a working version back in front of users by rolling back to that baseline, for example by
reverting the four commits and redeploying. Then find which change broke it, because users
get a working app during the investigation instead of waiting for you to finish it.
