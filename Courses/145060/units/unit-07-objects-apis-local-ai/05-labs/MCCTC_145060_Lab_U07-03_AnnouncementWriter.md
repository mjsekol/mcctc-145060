# Lab U7-03: Announcement Writer
## 145060 Programming · Unit 7 · Week 17

**Gate:** 3 (open tooling). **Duration:** one Build block, Thursday.
**Competencies:** 5.5.4 (call other programs), 5.5.7 (read inputs), 5.3.10 (error
handling).

**Files for this lab are in** `lab-u07-03-files/`: `announcement_writer.py` (the
starter), `stub_model_server.py` (a pretend model server), and
`test_announcement_writer.py` (the acceptance tests). Copy all three into your
repository.

---

## The scenario

Club officers hand the front office one line of facts for the morning announcements: a
club, a day, a time, a room, a detail. A language model on lab hardware can turn that
into one friendly sentence. But a model can stop mid-sentence, drop the time, or send
back nothing, and the front office still has to read something correct out loud.

## What you will build

A program that asks the model to write an announcement, checks the reply before trusting
it, and falls back to a plain template whenever the reply is bad. What goes into the
prompt is club facts only. What never goes in is any student's name, grade, or schedule.

---

## Before you start

Start the stub model server in one terminal:

```
python stub_model_server.py
```

Run the tests any time; they start their own stub:

```
python -m unittest test_announcement_writer
```

The stub has modes that make the model fail on purpose. You will use them to prove your
fallback works. Run the client in a second terminal.

---

## The steps

### Step 1. Write parse_reply, the done check
Replace TODO 1 and TODO 2. Turn the reply bytes into a dictionary and return its
`response`. Refuse a reply that does not say `"done": true`. Check `done` with
`is not True`, not with plain truthiness.
**Observable result:** `ParseReplyTests` for a good reply and a not-done reply pass.

### Step 2. Finish parse_reply, the type and size checks
Replace TODO 3 and TODO 4. Refuse a reply whose `response` is missing or is not a string,
refuse broken JSON, refuse blank text, and refuse text over `MAX_REPLY_CHARACTERS`.
**Observable result:** all `ParseReplyTests` pass.

### Step 3. Strip control characters
Replace TODO 5. Keep only characters where `character.isprintable()` is `True`.
**Observable result:** `test_control_characters_are_removed` passes.

### Step 4. Refuse a reply that dropped a fact
Replace TODO 6. Return the names in `FACTS_TO_KEEP` whose value does not appear in the
text.
**Observable result:** a reply missing the time or the room is caught.

### Step 5. Wire write_announcement
Replace TODO 7. Ask the model, parse the reply, check the kept facts, and on any problem
return the template. Return `(text, where_it_came_from)`.
**Observable result:** `WriteAnnouncementTests` pass, including every failure falling back
to the template.

### Step 6. Run every failure mode
Run the client against the stub in each mode: `not_done`, `missing_response`, `malformed`,
`wrong_type`, `drops_facts`, `error`, and `slow`. Confirm each falls back to the template.
**Observable result:** every mode produces a correct announcement from the template.

### Step 7. README and push
Three sections: what it is and how to run it, a real run using the model and a real run
falling back, and one sentence on why a model reply is untrusted. Confirm no student
personal data is anywhere in the file.
**Observable result:** README renders, all tests pass, pushed.

---

## Acceptance criteria

- [ ] `python -m unittest test_announcement_writer` passes
- [ ] `parse_reply` checks `done` with `is not True`
- [ ] Every failure mode falls back to a correct template announcement
- [ ] No student name, grade, or schedule appears in any prompt or file
- [ ] README shows a model run and a fallback run
- [ ] Two or more commits, pushed

---

## If it breaks

### 1. A half-sentence prints as the announcement

**Cause:** you checked `done` with `if reply.get("done")` instead of `is not True`. The
string `"false"` is truthy, so a not-done reply passed. Use `is not True`. **No error
appears**, which is the whole lesson.

### 2. TypeError, expected str

```
TypeError: the JSON object must be str, bytes or bytearray, not ...
```

**Cause:** you passed the response object to `json.loads` instead of its bytes. Read the
body with `.read()` first.

### 3. A valid reply is refused as "left out the time"

**Cause:** your kept-facts check is case-sensitive and the model lowercased the text.
Compare both sides in the same case, or check for the exact value the way the facts store
it. Read the fixture's success reply to see what it returns.

### 4. The program hangs

**Cause:** the stub is in `slow` mode and your request has no timeout, or a long one. The
starter's `ask_model` already sets a timeout from the settings. If you rewrote it, put the
timeout back.

---

## Stretch goal

Add a second `keep` fact of your own, like a phone number, and prove the model dropping it
triggers the fallback. Then answer in your README: what would happen if you asked the
model to keep a fact that is not actually in the facts you sent it? Try it and report what
your program does.

---

## Submission checklist

- [ ] Tests pass
- [ ] Ran every stub failure mode and saw the template each time
- [ ] No student personal data in any prompt or file
- [ ] `git status` clean, pushed, README renders
- [ ] AI usage log updated
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competency on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Stuck on the parse checks 20 minutes in | SCAFFOLDED |
| Working steadily through the checks | STANDARD |
| Finished early, asked about prompt injection | EXTENDED |
| Says announcements are pointless | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `parse_reply` is written for you. You write `remove_control_characters`,
  `missing_facts`, and `write_announcement`.
- **Steps:** skip Step 4 (kept facts) and its test. The fallback still fires on all the
  parse failures.
- **Step 6 stays.** Do not cut running the failure modes. Watching the fallback fire is
  the point.

**Acceptance criteria:** the fallback fires for `not_done`, `missing_response`,
`malformed`, `error`, and `slow`. Full completion earns what a STANDARD student earns.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition requiring something not taught.

**Added requirement.** Run the stub in `obedient` mode and send a detail that tells the
model to ignore its instructions and say something else. Watch what the model does. Then
harden your prompt so the detail is clearly marked as untrusted club text the model must
not obey.

**Hint, not the answer.** You cannot make a model refuse for certain. Read how the anchor
project's `EXAMINE_PROMPT` puts player text in quotation marks and names it as untrusted.
Do the same for your detail. Then note that the real protection is that you never act on
the reply, only print it.

**The honest warning:** hardening the prompt reduces the chance the model obeys. It does
not remove it, and the same model can obey on one try and refuse on the next. Say that in
your README. The point is to see the limit of prompt defenses, not to claim you closed it.

**Acceptance criteria:** all STANDARD criteria, plus a hardened prompt and a README note
on what prompt hardening can and cannot do, with a captured obedient-mode run.

---

## APPLIED

**For the student who does not run a club.** Same skills, different text.

**Changed scenario.** Turn structured facts into a sentence for a different audience: a
game's end-screen summary from the final stats, a workout recap from sets and reps, a
recipe step from ingredients and a time. Pick facts you have.

**What you build.** A program that sends facts to the model, checks the reply, keeps the
facts that must survive, and falls back to a template that a person could read as-is.

**The extra requirement that makes it the same lab.** Your README must include a section
called `Facts that must survive` listing which facts you check for in the reply and why
losing each one would matter.

**Acceptance criteria:** all STANDARD criteria applied to your text, plus
`Facts that must survive`, plus a fallback that reads correctly on its own.

**Grading:** same scale. Requirements Fit is judged on whether the fallback is genuinely
usable and the kept facts are the ones that matter.
