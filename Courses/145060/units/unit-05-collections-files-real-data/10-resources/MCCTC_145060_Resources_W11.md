# Additional Resources · Week 11
## 145060 Programming · Week 11
### Topics: JSON, saving and loading, CSV, responsible scraping, and the Unit 5 close

Links marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed live and must
be clicked before it is assigned.

**No resource this week asks a student to scrape a real website.** Every scraping exercise uses the
local fixture sites.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | Automate the Boring Stuff: CSV and JSON chapter | Mon, Wed | On-level | 35 min |
| 2 | Official docs: `json` module | Mon-Tue | On-level | 15 min |
| 3 | Official docs: `csv` module | Wed | On-level | 15 min |
| 4 | Official docs: `urllib.robotparser` and `html.parser` | Thu | Extension | 20 min |
| 5 | The JSON format, json.org | Mon | Remediation | 10 min |
| 6 | RFC 9309, the Robots Exclusion Protocol | Thu | Extension | 20 min |
| 7 | RFC 4180, the CSV format | Wed | Extension | 15 min |
| 8 | Python Tutor | Tue | Remediation | 15 min |
| 9 | A free video on JSON or CSV in Python | Any | Remediation | under 20 min |
| 10 | SQ-13 The Scraper and SQ-09 The Automation That Saves You Ten Minutes | Fri | Extension | 1-2 blocks |
| 11 | This unit's lecture notes, self-check sections | Before Friday's quiz | Review | 20 min |
| 12 | Gate 1 Collections bank, Reps 12-20 | Before Friday's quiz | Review | 10 min each |
| 13 | Official docs: `os.makedirs` and `os.path.join` | Thu-Fri | On-level | 10 min |
| 14 | Official tutorial: Errors and Exceptions | Before Friday's quiz | Remediation | 15 min |
| 15 | Data pipeline reference numbers, for self-checking | Thu-Fri | On-level | 5 min |

---

## 1. Primary reading

**Automate the Boring Stuff with Python, the chapter on working with CSV files and JSON data** ·
`https://automatetheboringstuff.com/` · **Confident** for the site, **[VERIFY]** the third edition's
chapter number and path.

**Why this one.** It covers `csv.reader`, `DictReader`, `DictWriter`, and `json.loads` and `json.dumps` in
one place, with the `newline=""` explanation this week's Windows blank-row bug depends on.

**Skip for now:** any section that calls a web API with a key. Unit 7 covers APIs, and this course never
requires a key.

**Time.** 35 minutes. **Level.** On-level.

**The web scraping chapter in the same book** is excellent on the technical side and uses third-party
packages this course does not install. If a student reads it, point out that its scraping must still follow
this week's six rules, and that the course practises only on fixture sites.

---

## 2. The `json` module

`https://docs.python.org/3/library/json.html` · **Confident.**

**Assign a question, not the page:** *Find the conversion table between Python and JSON. Which Python types
are missing from it, and what does that mean for a set?*

**Time.** 15 minutes. **Level.** On-level.

---

## 3. The `csv` module

`https://docs.python.org/3/library/csv.html` · **Confident.**

**Assign a question:** *Find what the documentation says about opening a CSV file with `newline=''`. What
does it say goes wrong without it?* That is Wednesday's blank-row bug in the official words.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. The scraping modules

`https://docs.python.org/3/library/urllib.robotparser.html` · **Confident.**
`https://docs.python.org/3/library/html.parser.html` · **Confident.**

**Why these.** The robot parser page is short and lists `can_fetch` and `crawl_delay`. The HTML parser page's
example is the pattern `table_reader.py` is built on, which is Lab U5-05's EXTENDED option.

**Time.** 20 minutes. **Level.** Extension.

---

## 5. The JSON format itself

`https://www.json.org/` · **Confident.**

**Why this one.** The diagrams on the front page show exactly where quotes and commas are allowed. A student who
keeps writing single quotes or trailing commas sees in thirty seconds that the grammar has no place for them.

**Time.** 10 minutes. **Level.** Remediation.

---

## 6. How robots.txt is defined

**RFC 9309, Robots Exclusion Protocol** · `https://www.rfc-editor.org/rfc/rfc9309` · **[VERIFY]** before
assigning.

**Why this one.** It is the standards document behind `robots.txt`, and it is readable. Ask a student to find
whether it defines `Crawl-delay`. The honest discussion that follows, about conventions crawlers use that a
standard does not define, is exactly the nuance Thursday's lesson points at.

**Time.** 20 minutes. **Level.** Extension.

---

## 7. How CSV is defined

**RFC 4180, Common Format and MIME Type for CSV Files** · `https://www.rfc-editor.org/rfc/rfc4180` ·
**[VERIFY]** before assigning.

**Why this one.** This is the industry connection for the week: the short document that describes the quoting
rule `split(",")` breaks. It also states plainly that many programs do not follow it exactly, which is why real
exports are messy.

**Time.** 15 minutes. **Level.** Extension.

---

## 8. Python Tutor, for the half-written save

**Python Tutor** · `https://pythontutor.com/` · **Confident.**

Step through Tuesday's `load_game` with a missing file and watch `state` stay the same when the function raises.
The picture of "the assignment never happened" makes the all-or-nothing rule concrete. (Python Tutor cannot read
real files; have the student replace the `open` with a line that raises `FileNotFoundError` directly.)

**A second use, for quiz item 12.** Step through Gate 1 Rep 18. Python Tutor draws both calls pointing at the one list
created with the `def`. It is the fastest way to see the mutable default argument, which is also the subtle defect in
the spare Gate 2.

**Time.** 15 minutes. **Level.** Remediation.

---

## 9. A free video

**[VERIFY]** No specific video is linked. Python for Everybody, `https://www.py4e.com/`, **Confident** for the site,
publishes free lecture videos, including material on reading files and on JSON. Find one under 20 minutes that
matches Monday or Wednesday, and watch it yourself before assigning it.

**Level.** Remediation.

---

## 10. Side quests

**SQ-13 The Scraper** unlocks Friday. Bundle: `Courses/Misc/side-quests/SQ-13-The-Scraper/`. It runs against its own
invented card shop website, and it is built so that following robots.txt alone is not enough. ★★★, two blocks. It
runs entirely on your own computer, with no network needed. Remember to stop the site when you are done.

**SQ-09 The Automation That Saves You Ten Minutes** also unlocks this week, per the catalog. A student who wants a
smaller, personal version of Wednesday's cleaning program, pulling numbers out of their own non-personal spreadsheet,
fits it well.

---

## 11. The self-checks you already have

Every Unit 5 lecture note ends with three self-check questions and worked answers, in `03-lecture-notes/`.
**Before Friday's quiz, a student should be able to answer all 24 without reading the answers first.** The ones most
worth the time: Lists question 2, Dictionaries question 2, Tables question 1, Save and Load question 1, and CSV
question 1.

**Level.** Review.

---

## 12. Gate 1 reps for quiz review

The later reps in the Collections bank are the best short review for the quiz: Rep 12 (JSON types), Rep 13 (except
order), Rep 16 (the Windows blank row), Rep 18 (the mutable default), and Rep 20 (choosing a structure). Your
instructor assigns them from the instructor copy.

**Level.** Review.

---

## 13. Files and folders

`https://docs.python.org/3/library/os.html#os.makedirs` · **Confident.**
`https://docs.python.org/3/library/os.path.html#os.path.join` · **Confident.**

**Why these.** The pipeline creates an `output` folder and builds paths with `os.path.join`. **Assign a question:**
*What does `exist_ok` do in `os.makedirs`?* It is quiz item 9.

**Time.** 10 minutes. **Level.** On-level.

---

## 14. Errors and exceptions, for the except-order question

**The Python Tutorial, section 8, Errors and Exceptions** · `https://docs.python.org/3/tutorial/errors.html` ·
**Confident.**

**Assign a question:** *When a `try` has several `except` clauses, how many of them run?* That settles the except-order
misconception from Tuesday.

**Time.** 15 minutes. **Level.** Remediation.

---

## 15. Checking your pipeline against known numbers

For **Route A** students only. If your pipeline reads the Swap Shelf listings and the provided sales log with rules like the
project's "about right" example, these are numbers you can compare with. **Your numbers can differ if your rules differ.
If they do, your README must explain which rule causes the difference.**

- Listings on the shelf: 28, across 3 pages
- Listings marked sold on the site: 11
- Sales log data rows: 16, including one blank row and one repeated header

The rest is your analysis to do, not a key to copy.

---

## For the student who is behind

1. The Tuesday lecture notes' first example, run by hand, with the half-written file opened afterwards
2. json.org's diagrams, for anyone still writing single quotes
3. Gate 1 Reps 11, 13, and 15
4. Before Friday's quiz: the Save and Load notes, the CSV notes, and nothing else new

## For the student who is ahead

- Lab U5-03 EXTENDED (safe saving with `os.replace`), Lab U5-04 EXTENDED (`difflib`), Lab U5-05 EXTENDED (following links)
- SQ-13
