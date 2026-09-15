# Additional Resources · Week 11
## 145060 Programming · November 16-20, 2026
### Topics: JSON, saving and loading, CSV, and responsible scraping

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
invented card shop website, and it is built so that following robots.txt alone is not enough. ★★★, two blocks.

**SQ-09 The Automation That Saves You Ten Minutes** also unlocks this week, per the catalog. A student who wants a
smaller, personal version of Wednesday's cleaning program, pulling numbers out of their own non-personal spreadsheet,
fits it well.

---

## For the student who is behind

1. The Tuesday lecture notes' first example, run by hand, with the half-written file opened afterwards
2. json.org's diagrams, for anyone still writing single quotes
3. Gate 1 Reps 11, 13, and 15

## For the student who is ahead

- Lab U5-03 EXTENDED (safe saving with `os.replace`), Lab U5-04 EXTENDED (`difflib`), Lab U5-05 EXTENDED (following links)
- SQ-13
