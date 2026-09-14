# Additional Resources · Week 19
## 145060 Programming · January 25-29, 2027
### Topic: deploying, documenting, and versioning

Links marked **Confident** or **[VERIFY]**, same standard as every week. A [VERIFY] link is one the
builder could not confirm is live today; check it before you assign it.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The Twelve-Factor App: Config, and Port binding | Mon | On-level | 15 min |
| 2 | Python documentation: `http.server` | Mon | On-level | 10 min |
| 3 | Python documentation: `os.environ` | Mon | Remediation | 5 min |
| 4 | Render documentation | Mon, Thu | On-level | 15 min |
| 5 | Python Tutor | Mon, Wed | Remediation | 10 min |
| 6 | Semantic Versioning | Wed | On-level | 15 min |
| 7 | Pro Git, Tagging | Wed, Thu | On-level | 15 min |
| 8 | Keep a Changelog | Thu | Extension | 10 min |
| 9 | Diátaxis, a documentation framework | Tue | Extension | 20 min |
| 10 | Python for Everybody, networked programs | Mon | Extension | 30 min |
| 11 | SQ-08 Deploy Something Nobody Asked For | Fri | Extension | 2 blocks |

**No video is listed this week.** No free video under 20 minutes on standard-library Python deployment
could be confirmed live by the builder, and a guessed link costs a class period. If you find one you
trust, add it here.

---

## 1. Industry reading: The Twelve-Factor App

**Factor III, Config** · `https://12factor.net/config` · **Confident** for the site, **[VERIFY]** the page path.
**Factor VII, Port binding** · `https://12factor.net/port-binding` · **[VERIFY]** the page path.

**What it is.** A short, widely referenced set of principles for building apps that deploy to hosting
platforms. Each factor is a page of a few paragraphs.

**Why this one.** Monday's whole lesson, settings from the environment and an app that binds to a port it
is given, is two of these factors. Reading them shows students that `int(os.environ.get("PORT", "8000"))`
is not a classroom trick; it is how deployable software is expected to behave.

**Assign a question, not the pages.** "Find the sentence that explains why config belongs in the
environment and not in the code. What does it say could happen if it is in the code?"

---

## 2. Official documentation: `http.server`

`https://docs.python.org/3/library/http.server.html` · **Confident.**

**Why this one.** It is the module every web app this week is built on, and the page opens with Python's own
warning that `http.server` is not recommended for production. Having students find that warning themselves
is worth more than you saying it. It is also where the EXTENDED Lab U8-01 hint about `HEAD` requests leads.

---

## 3. Official documentation: `os.environ`

`https://docs.python.org/3/library/os.html#os.environ` · **Confident.**

**For the student who is behind.** Read the first paragraph only, then run `import os; print(os.environ.get("PORT"))`
in a terminal before and after `$env:PORT = "10000"`. That thirty-second experiment teaches Monday.

---

## 4. Render documentation

`https://render.com/docs` · **[VERIFY]** before assigning. Specific pages for web services, the free tier,
environment variables, and health checks exist in some form, and their exact paths are not listed here
because they were not confirmed.

**Why this one.** It is the primary source for every **[VERIFY]** marker in this unit. **Teacher use first:**
work the crash course section 4 checklist against it. Point students at it only after you have read the pages
yourself, because platform documentation changes without notice.

---

## 5. Python Tutor

`https://pythontutor.com/` · **Confident.**

Paste in Wednesday's version comparison and watch the strings compare:

```python
installed = "2.9.1"
available = "2.10.0"
print(available > installed)
```

Then exam item 18's disappearing list. Seeing `inventory` created fresh on every call settles scope faster
than any explanation.

---

## 6. Semantic Versioning

`https://semver.org/` · **Confident.**

**What it is.** The specification behind `MAJOR.MINOR.PATCH`. The summary at the top is one paragraph.

**Why this one.** Wednesday teaches the rule; this is the rule's source. **Read only the summary and the FAQ
question about what to do if you accidentally release a breaking change as a minor version.** The rest is
written for library authors and will lose most students.

---

## 7. Pro Git, Tagging

`https://git-scm.com/book/en/v2/Git-Basics-Tagging` · **Confident.**

**What it is.** The chapter section on creating, listing, and pushing tags, in the free official Git book.

**Why this one.** It explains the failure mode students hit Thursday: `git push` does not send tags, and the
section shows how to push them. Annotated versus lightweight tags is the only other idea they need.

---

## 8. Keep a Changelog

`https://keepachangelog.com/` · **Confident.**

**What it is.** A one-page convention for writing `CHANGELOG.md`, with an example.

**Why this one.** The final project requires a changelog, and this page shows a clean format in two minutes.
**Extension:** its categories, such as Added, Changed, and Removed, map neatly onto patch, minor, and major.

---

## 9. Diátaxis

`https://diataxis.fr/` · **[VERIFY]** before assigning.

**What it is.** A framework that sorts documentation into four kinds by what the reader needs: tutorials,
how-to guides, reference, and explanation.

**Why this one.** Tuesday says every document has one reader. Diátaxis is a professional version of that idea.
For the student whose user help and implementation plan keep bleeding into each other, it names the
difference. Extension only.

---

## 10. Python for Everybody, networked programs chapter

`https://www.py4e.com/` · **Confident** for the site. **[VERIFY]** the chapter location before assigning.

**Why this one.** It explains what an HTTP request and response actually are, in plain language, from the
client side. Students who want to know what `send_response` and `end_headers` are writing will find the other
half of the conversation here. Extension, 30 minutes.

---

## 11. Side quest

**SQ-08 · Deploy Something Nobody Asked For** · `Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.
Unlocks Unit 8.

**Why it fits.** "Done when the URL loads from a phone on cell data, not school wifi, and your README explains
what deployment actually did to your code." It is the final project's hardest requirement, done a second time
on something small and personal. Hand it to students who presented Friday and to anyone at `v1.0.0` early
Thursday.

---

## For the student who is behind

1. Resource 3, the thirty-second `os.environ` experiment
2. The Monday lecture notes, typing the four stages of `on_the_air.py`
3. Lab U8-01 SCAFFOLDED

Do not hand out eleven links. A student who is behind in the last week of the semester needs one working
deploy, not a reading list.
