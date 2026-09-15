# Project: Data Pipeline
## 145060 Programming · Unit 5 · Due Tuesday, November 24, 2026

**Mode:** solo. **Gate:** 3, full tooling, decision log and AI usage log required.
**Periods:** three Build 2 blocks and one Build 1 block, Wednesday November 18 through
Tuesday November 24, plus flex time.

**Competencies:** 5.3.11 (access data repositories), 5.5.7 (read inputs: data files and a web
source), 5.1.5 (data management: converting data to a new format), 5.5.3 (operating system
calls: creating folders and building paths), 5.5.6 (format output: reports and data files),
5.5.1 (data validation), 5.3.10 (error handling), 5.4.4 and 5.4.5 (test cases),
1.7.13 (respecting a site's terms).

---

## The brief

> I am the treasurer of the Oak Hollow High School Game Club. We sell donated games to pay
> tournament entry fees. The listings are on our website, and the sales go into a spreadsheet
> that three different volunteers type into at the table after school.
>
> Every month the advisor asks me two things: which platforms actually sell, and whether we are
> giving too much away on price. I spend a Sunday copying numbers from the website and the sheet
> into a calculator, and I am not confident in my answer, because the sheet is a mess and I know
> some sales never got typed in.
>
> I do not need an app. I need to run one thing and get numbers I can trust, and I need to know
> which rows I cannot trust so I can go ask the volunteer who typed them.

**That is the brief.** It does not say which numbers "actually sell" means, what "too much away"
means, or what to do with a row that cannot be read. Deciding those is most of the work.

(The club, its website, and the sheet are invented for this course.)

---

## Your data

You choose **one** of two routes by the end of Wednesday's Build 2.

### Route A: the treasurer's data (recommended)

- **The listings:** the Swap Shelf website, `05-labs/fixtures/swap-shelf/`, which you run on your own
  computer exactly as in Lab U5-05. Scrape it; do not copy it by hand.
- **The sales log:** `09-project/data/swap_shelf_sales_messy.csv`, the sheet the volunteers type into.

### Route B: your own messy data, with approval

A dataset you already have that is messy, **contains no personal information about anyone**, and needs
the same four stages. Examples that have been approved before: a team's statistics export, a game's item
list copied from a spreadsheet, a club's inventory sheet with invented names. **Get your instructor's
approval in writing, in your decision log, before the end of Wednesday's Build 2.** A real website is **not**
an approved Route B source for this project. Scraping practice uses the fixture sites only.

---

## Requirements

### The four stages

1. **Ingest.** Read at least one messy source. Route A reads two: the website and the sales log.
   - Scraping follows every Lab U5-05 rule: `robots.txt` read and obeyed, `can_fetch` before every page, at
     least two seconds between requests, a User-Agent naming your program, and a timeout.
   - CSV is read with the `csv` module.
2. **Clean.** Every cleaning rule is written down in your README. Rows that can be fixed by a rule are fixed.
   Rows that cannot are **listed, with the line number or item ID and the reason**, and left out of the
   calculations. **Nothing is dropped without being reported.** Nothing unknown is guessed.
3. **Convert.** Write the clean data to JSON. Load it back and confirm the count matches.
4. **Report.** Print a report and save it to a file. It includes **at least three calculated fields**, at least
   one of them grouped, such as a total per platform, and the list of rows that need a person.

### Engineering

5. **Structures chosen on purpose.** Use at least one list, one dictionary, and one set, each with a comment
   saying why.
6. **Failures handled with a message, not a traceback:** the sales file missing, a required column missing, and,
   for Route A, the site not running.
7. **Outputs go in an `output` folder** your program creates if it is not there, using `os.makedirs` and paths
   built with `os.path.join`.
8. **At least five test cases**, runnable with one command, covering your cleaning rules and at least one
   calculated field **checked against arithmetic you did by hand**. `assert`-based test functions or `unittest`
   like the text adventure's tests are both fine.
9. **Standard library only.** You may reuse `table_reader.py` from the fixture folder, and your own code from Labs
   U5-02, U5-04, and U5-05.

### Repository

```
data-pipeline/
  pipeline.py            or several files, if you split the stages
  test_pipeline.py
  table_reader.py        Route A only, copied from the fixture folder
  data/                  your input files; the sales log for Route A
  output/                created by the program; add it to .gitignore
  README.md
  decision-log.md
  ai-usage-log.md
  .gitignore
```

### README, eight sections

1. **The question.** The treasurer's two questions in your own words, and what you decided each one means as a
   number.
2. **How to run it and how to test it.** Exact commands, including starting the site for Route A.
3. **Data sources.** What each source is, and for Route A a section titled **Why this was allowed** quoting the
   site's `robots.txt` and the terms sentence that permits collecting the listings.
4. **The mess.** Every kind of problem you found in the data, with one example of each.
5. **Rules I chose.** Every cleaning rule, one line each, including what you refused to guess.
6. **A real run.** The report, pasted.
7. **Checked by hand.** At least one calculated field worked out on paper, matching the report.
8. **Known limitations.** At least two, observed.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Scrape any real website | The fixture site exists so nobody practises on someone else's server. Real sites have real owners, real terms, and real people's data. |
| Put personal information in any dataset, test, or README | Your repository is public. Invented names only. |
| Guess a value you cannot read | The treasurer asked specifically to know which rows cannot be trusted. A confident wrong number is worse than a flagged row. |
| Use pandas or any other installed package | Not installed on lab machines, and you have not been taught dependency management. Everything here is standard library. |
| Use classes | Unit 7. `table_reader.py` uses one internally; you do not need to write one. |
| Request a page faster than every two seconds | The site's terms ask for two seconds, and the fixture refuses anything under one. |

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Wed Nov 18, end of Build 2 | Route chosen. The treasurer's two questions rewritten as numbers you will calculate, in `decision-log.md`. |
| **Measure** | Wed Nov 18, end of Build 2 | README section 4, **The mess**, from reading the data, before writing any cleaning code. |
| **Analyze** | Thu Nov 19, end of Build 2 | README section 5, **Rules I chose**, drafted. One calculated field worked by hand from three real rows. |
| **Improve** | Thu Nov 19 to Mon Nov 23 | Ingest, clean, convert, report, in that order, committing after each stage works. |
| **Control** | Tue Nov 24, end of Build 1 | Tests passing, README complete, a paired demo given. **Due at the end of the day.** |

**Analyze is where the treasurer's trust comes from.** If you cannot calculate one row's discount on paper, your
program's answer for 28 rows is a guess.

---

## Milestone schedule, against actual class days

| Day | Block | Goal |
|---|---|---|
| Wed Nov 18 | Build 2 | Define and Measure. Route chosen and approved. The mess listed. |
| Thu Nov 19 | Build 2 | Analyze, then ingest: the listings and the sales log each read into a list of dictionaries. |
| Fri Nov 20 | Flex | Optional. Build 2 is text adventure v3's deadline; pipeline work only if v3 is submitted. |
| Mon Nov 23 | Build 2 | Clean, convert to JSON, and the report with calculated fields. |
| Tue Nov 24 | Build 1 | Tests, README, paired demo, final push. |

**This schedule is tight on purpose.** It is four blocks because most of what you need already exists in your own
labs: the scraper from U5-05, the cleaning pattern from U5-04, and the report pattern from U5-02. Reuse your code and
say so in the decision log.

---

## Three worked scope examples

These are here so you can calibrate. The "about right" example uses Route A, so a Route A project
will resemble it. What makes yours yours is the rules you choose, what you decide the treasurer's
questions mean, and how you explain your numbers.

### Too small

> Reads the sales CSV with `split(",")`, removes dollar signs, adds up the sold prices, and prints the total.

One calculated field, no grouping, no conversion, no listings, and `split` breaks on the first comma in a note. It
answers neither of the treasurer's questions and hides every row it could not read.

### About right

> **Route A.** Scrapes the three shelf pages politely and reads the sales log with `DictReader`. Normalizes item IDs
> so `oh-107` and `OH 109` match the site. Refuses prices like `eight` and lists them with line numbers. Counts a
> duplicate sale once and says so. Writes `listings.json` and `sales.json` and checks both reload. The report shows,
> per platform, items listed, items sold, sell-through percent, and revenue, plus the average discount off the listed
> price, and lists five rows that need a person, including a sale typed with a letter O in the item ID. Seven tests.

Every requirement, and the needs-a-person list answers the treasurer's second worry directly.

### Too big

> Also tracks sales by week using the date column, predicts which donations will sell, emails the advisor a monthly
> summary, and builds a web page to show the report.

The dates in the sheet are typed three different ways, which is a whole project on its own. Prediction is not
reliable with 28 items. Email and web pages are Units 7 and 8. **The calibration question:** can you explain every
number in your report to the treasurer, including how you got it? If a feature makes that harder, cut it.

---

## The five-minute demo

Tuesday, November 24, in pairs. Your partner plays the treasurer.

1. **The question.** The two questions, and what number answers each. (30 seconds)
2. **Run it live.** For Route A, the site's terminal must be visible, so your partner can see the pages requested
   two seconds apart. (60 seconds)
3. **One row that needs a person.** Show it in the report, then open the input file and show the line. Explain why
   your program refused to guess. (60 seconds)
4. **One number, checked.** Point at one calculated field and walk through the arithmetic from the raw data.
   (75 seconds)
5. **One decision.** A cleaning rule or a structure, and what you rejected. (45 seconds)
6. **Questions.** (30 seconds)

**Steps 3 and 4 are the graded part of the demo.** They are the two things the treasurer said mattered most.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | All four stages work on the real data. At least three calculated fields, one grouped. JSON written and reloaded. Missing file, missing column, and site down each handled with a message. |
| **Code Quality** | 20 | List, dictionary, and set each justified in a comment. Cleaning rules in dictionaries and sets, not long `if` chains. No bare `except`. Scraping follows every rule. |
| **Documentation** | 20 | All eight README sections. `Why this was allowed` quotes both documents. `Checked by hand` matches the report. |
| **Process** | 15 | DMAIC checkpoints on time, especially Measure before code. Five or more tests, one checked by hand. Commits after each stage. |
| **Demonstration** | 10 | The demo script, with a flagged row traced to its line and one number explained from raw data. |
| **Polish** | 10 | A report a treasurer reads without asking what a column means. Percentages and money formatted. Problem messages a volunteer could act on. |

**Security is not a separate row here, and it is still the fastest way to lose points.** A scraper that requests a
disallowed page, skips the wait, or runs against a real site loses Code Quality and Functionality credit for those
stages, regardless of how good the report looks.

---

## If you are stuck

**"The item IDs will not match."** Print both lists of IDs next to each other with `repr()`. Look for spaces, case, and
a letter that looks like a digit.

**"My calculated field is a weird decimal."** That is floating point. Round when you display it, not while you calculate.

**"I do not know what sell-through means."** Items sold divided by items listed. Decide whether items marked on hold
count as listed, and write the decision down.

**"The scraper is slow."** It is supposed to be. Three pages at two seconds each is about eight seconds. Develop the
cleaning code against a saved copy of your scraped data so you do not rescrape every run.

**"A row could mean two things."** Then it needs a person. Put it on the list.
