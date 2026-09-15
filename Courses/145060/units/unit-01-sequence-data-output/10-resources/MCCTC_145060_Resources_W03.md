# Additional Resources · Week 3
## 145060 Programming · Week 3
### Topic: strings, formatting, and slicing

Links marked **Confident** or **[VERIFY]**, same standard as every week.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff, strings chapter | Tue-Thu | On-level | 35 min |
| 2 | Think Python 3e, strings chapter | Wed | On-level | 25 min |
| 3 | Python Tutor | Wed | Remediation | 15 min |
| 4 | Official docs: string methods | Thu | On-level | 15 min |
| 5 | Official docs: f-string format spec | Tue | Extension | 20 min |
| 6 | Falsehoods about names | Thu | Extension | 15 min |
| 7 | SQ-02 The Regex Wrangler | Fri | Required-ish | 2 blocks |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, the chapter on manipulating strings** ·
`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the
third-edition chapter path.

**Why this one.** It covers indexing, slicing, `in`, and the common methods in one
place, with examples that are about text people actually have rather than alphabet
strings.

**Skip:** anything about the clipboard or `pyperclip`. Not this course, not this week.

---

## 2. Second reading, more precise

**Think Python, 3rd edition, the strings chapter** ·
`https://allendowney.github.io/ThinkPython/` · **Confident.**

**Why this one.** Downey is careful about the difference between an index and a
slice, and about strings being immutable. Assign it to any student who asks why they
cannot change one character.

---

## 3. Interactive practice

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Paste in Wednesday's off-by-one and step through it:

```python
code = "ROBO-2026-114"
year = code[5:8]
print(year)
```

Seeing the slice highlighted against the string does more for the counting
misconception than any explanation.

---

## 4. Official documentation, string methods

`https://docs.python.org/3/library/stdtypes.html#string-methods` · **Confident.**

**Assign a question, not the page.** The page is long and intimidating on purpose.

> Find `str.strip()`. Read what it says about which characters it removes and from
> where. Then answer in one sentence: does it touch the middle of the string?

That question settles Thursday's bell ringer from the primary source, which is the
habit being built.

---

## 5. Format specifiers, for the student who wants columns

`https://docs.python.org/3/library/string.html#format-specification-mini-language` ·
**Confident.**

**Warning worth passing on:** this page is dense and reads like a specification,
because it is one. Tell students to look only for the alignment characters `<`, `>`,
`^` and the `.2f` precision form. Everything else can wait.

**Time.** 20 minutes and only for students who asked. **Level.** Extension.

---

## 6. Why name cleaning is genuinely hard

Search for the widely circulated article **"Falsehoods Programmers Believe About
Names."** · **[VERIFY]** the URL before assigning, since it has been reposted in many
places and the original may have moved.

**Why this one.** Thursday ends by admitting that `.title()` gets real names wrong.
This is the canonical list of everything else that goes wrong, and it reframes a
frustration as a known hard problem rather than a personal failure.

**If you cannot verify a live copy, do not assign a link.** Instead run the exercise
live: have students type names from their own families into a `.title()` call and
report what breaks. That is better than the article anyway, because it is theirs.

---

## 7. Side quest

**SQ-02 The Regex Wrangler** unlocks Friday. It is named in the 145060 syllabus as a
Unit 1 deliverable. Full description in
`Courses/Misc/MCCTC_Side_Quest_Catalog_2026-2027.md`.

**Why it fits here.** Slicing works when you know exactly where things are. Regular
expressions are what you reach for when you do not. A student who spent Wednesday
counting positions is ready to want something better.

---

## For the student who is behind

1. Python Tutor with the off-by-one example, stepped one line at a time
2. The lecture notes Part 2 only, with a terminal open, typing every example
3. Rewrite Lab U1-02 Part 2 from an empty file without looking at their old one

Do not assign all seven resources. A student who is behind and gets seven links reads
none of them.
