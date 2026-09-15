# Lab U5-05: Swap Shelf Scraper
## 145060 Programming · Unit 5 · Week 11

**Gate:** 3 (open tooling). **Duration:** one Build 1 block, Thursday, 35 minutes.
**Competencies:** 5.3.11 (access data repositories), 5.5.7 (read inputs, including a web
source), 5.5.2 (reuse libraries), 5.3.10 (error handling), 1.7.13 (protect intellectual
property: respecting a site's terms).

**No real website is used in this lab.** You run the site yourself, on your own computer.

---

## The scenario

The Oak Hollow High School Game Club sells donated games to pay tournament entry fees, and
lists them on a three-page website with no download button. The club treasurer wants the
listings in a spreadsheet to see what is still on the shelf. You will collect them with a
program, and because it is someone else's site, you will do it the way the site asks: rules
first, slowly, and identified. (The club and its site are invented.)

## What you will build

A scraper that reads the site's `robots.txt`, fetches every shelf page with a pause before
each request and a User-Agent header, turns each page's table into dictionaries, stops
cleanly when it runs out of pages, and writes the listings to `shelf.csv`.

---

## Files you need

Everything is in `05-labs/fixtures/swap-shelf/`:

- `serve_site.py`, which runs the site on your computer
- `site/`, the site's pages, `robots.txt`, and terms of use
- `table_reader.py`, a helper that turns HTML tables into rows

**Leave `serve_site.py` and `site/` where they are.** Copy **only** `table_reader.py` into the
folder where your scraper will live.

---

## Two terminals

**Terminal 1** runs the site. **Terminal 2** runs your program. Keep both visible, because
Terminal 1 prints every request your program makes and how long after the previous one it
arrived.

**Terminal 1:**

```
cd 05-labs/fixtures/swap-shelf
python serve_site.py
```

```
Swap Shelf running at http://127.0.0.1:8000/
Press Ctrl+C to stop.
```

If it says port 8000 is in use, run `python serve_site.py 8001` and use `8001` in your program.

**When you are done with the lab, click in Terminal 1 and press Ctrl+C to stop the site.**

---

## Starter code

In your own lab folder, next to your copy of `table_reader.py`, create `shelf_scraper.py`. It
runs. It does nothing useful.

```python
# shelf_scraper.py
# Collects the Oak Hollow Game Club Swap Shelf listings into shelf.csv,
# politely: robots.txt first, a pause before every request, and a
# User-Agent that says who is asking.
#
# This file runs right now. It does not do anything useful yet.
#
# Start the site first, in its own terminal:  python serve_site.py
# Then run this in a second terminal:          python shelf_scraper.py

import csv
import time
import urllib.error
import urllib.request
import urllib.robotparser

from table_reader import read_tables

BASE_URL = "http://127.0.0.1:8000"
USER_AGENT = "TODO: name your program and say why it exists"
MINIMUM_DELAY = 2   # the site's terms ask for at least two seconds
OUTPUT_FILE = "shelf.csv"


def main():
    # TODO: read robots.txt and print what it allows.
    # TODO: fetch each shelf page politely until one answers 404.
    # TODO: turn each table into dictionaries and write shelf.csv.
    print("Nothing collected yet.")


main()
```

Running it produces:

```
Nothing collected yet.
```

---

## Steps

### Step 1. Read the rules like a person first
With the site running, open `http://127.0.0.1:8000/` in a browser. Click through the shelf.
Then open `http://127.0.0.1:8000/robots.txt` and `http://127.0.0.1:8000/terms.html`. In your
README, start a section called `Why this was allowed`. Copy in the `robots.txt` rules and
quote the sentence from the terms that allows collecting the listings.
**Observable result:** your browser's requests appear in Terminal 1, and your README quotes
both documents.

### Step 2. Starter running and committed
Name your program in `USER_AGENT`: what it is and that it is a class project.
**Observable result:** `Nothing collected yet.` and a commit.

### Step 3. Ask robots.txt
Create a `RobotFileParser` for `BASE_URL + "/robots.txt"`, call `.read()`, and print whether
`/shelf/page-1.html`, `/members/index.html`, and `/drafts/new-donations.html` are allowed for
your user agent. Print the crawl delay. Use the larger of your `MINIMUM_DELAY` and the site's
crawl delay as your delay.
**Observable result:** the shelf is allowed, members and drafts are not, and the crawl delay
is 2. Terminal 1 shows one request, for `/robots.txt`.

### Step 4. Fetch one page, identified
Write `fetch(url)` that builds a `urllib.request.Request` with your User-Agent header, opens
it with `timeout=10`, and returns the decoded text. Sleep for your delay, then fetch page 1
and print how many rows `read_tables(page_text)[0]` has.
**Observable result:** 11 rows: the header and 10 listings. Terminal 1 shows the page request
about two seconds after `robots.txt`, **with your User-Agent in the log line**.

### Step 5. Rows into dictionaries
Write `rows_to_dicts(rows)` that uses the first row as the keys and returns one dictionary per
remaining row.
**Observable result:** the first dictionary has `'Item ID': 'OH-101'` and
`'Title': 'Moss Knight Chronicles'`.

### Step 6. Every page, until there are no more
Loop over page numbers starting at 1. Before each request: check `can_fetch`, then sleep. Catch
`urllib.error.HTTPError`. A 404 means you are out of pages, so stop. Any other status, print
it and stop. Add every listing to one list.
**Observable result:** 10, 10, and 8 listings from pages 1 to 3. Terminal 1 shows requests two
seconds apart, and a 404 for page 4.

### Step 7. Remove the wait, on purpose
Comment out the `time.sleep` line and run the scraper again.
**Observable result:** Terminal 1 shows page 1 answered with **429** about a tenth of a second
after `robots.txt`, and your program reports the 429 and collects nothing. Copy both into your
README under `What I learned`. Put the sleep back.

### Step 8. Write the CSV
Write every listing to `shelf.csv` with `csv.DictWriter`, using the keys of the first
dictionary as the field names. Print how many listings you wrote and how many are marked
`SOLD`.
**Observable result:** `Wrote 28 listings to shelf.csv. Marked sold: 11.` Open `shelf.csv` and
find `Wireless controller, blue` wrapped in quotes.

### Step 9. The site is down
Stop the site with Ctrl+C in Terminal 1. Run your scraper.
**Observable result:** instead of a long traceback, your program prints one line saying it could
not reach the site and asking whether `serve_site.py` is running. Catch
`urllib.error.URLError` around `robots.read()` to get there. Start the site again.

### Step 10. README, stop the site, push
Finish `Why this was allowed` with one more sentence: why you did not collect anything from
`/members/`, even though it loads in a browser. Stop the site. Push.

---

## Acceptance criteria

- [ ] `robots.txt` read before any page, and `can_fetch` checked before every page
- [ ] A delay of at least two seconds before every page request, visible in Terminal 1
- [ ] A User-Agent naming your program, visible in Terminal 1
- [ ] `timeout` set on every request
- [ ] 404 stops the loop; other statuses are reported
- [ ] `shelf.csv` has 28 listings; the summary line matches step 8
- [ ] No request to `/members/` or `/drafts/` ever appears in Terminal 1
- [ ] README has `Why this was allowed` (steps 1 and 10) and `What I learned` (step 7)
- [ ] The site was stopped when you finished
- [ ] Pushed

---

## If it breaks

### 1. The helper is not next to your program

```
ModuleNotFoundError: No module named 'table_reader'
```

**Cause:** `table_reader.py` must be in the same folder as `shelf_scraper.py`. Copy it there.

### 2. The site is not running

```
urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>
```

**Cause:** Terminal 1 is not running `serve_site.py`, or it is on a different port from
`BASE_URL`.

### 3. Too fast

```
urllib.error.HTTPError: HTTP Error 429: Too Many Requests
```

**Cause:** two requests arrived less than a second apart, often because the sleep is after the
request instead of before it, or robots.txt and page 1 went out back to back.

### 4. A page with no table

```
IndexError: list index out of range
```

**Cause:** `read_tables(page_text)[0]` on a page with no tables, which returns an empty list.
Usually you fetched the wrong URL, such as the home page. Print the URL you fetched.

### Not an error: nothing is allowed and nothing is collected

**Cause:** you called `can_fetch` before `robots.read()`. Until the rules are read, `can_fetch`
answers `False` for every URL.

---

## Stretch goal

Instead of guessing page numbers until a 404, follow the `Next page` link on each page. You will
need `read_links` from `table_reader.py` and `urllib.parse.urljoin` to turn `page-2.html` into a
full address. Keep a set of pages already visited so a link back to page 1 cannot send your
scraper in a circle. Your program should then make no request that answers 404.

---

## Submission checklist

- [ ] Terminal 1 log for a full polite run pasted into the README
- [ ] `shelf.csv` committed, or listed in `.gitignore` with a sentence saying why
- [ ] The site stopped
- [ ] `git status` clean, pushed
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Ten minutes in and the site is still not running, or both programs are in one terminal | SCAFFOLDED |
| Site running, working through the fetch loop | STANDARD |
| CSV written with a polite log before 20 minutes, or asks how `table_reader.py` works | EXTENDED |
| "Why not copy and paste," or asks where scraping is used for real | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `fetch` and `rows_to_dicts` are provided complete.
- **Steps:** step 6 fetches the three pages from a list of three URLs instead of looping until 404.
  Step 9 is removed.
- **Steps 1 and 7 stay.** Reading the rules and seeing the 429 are the lesson.
- **Checkpoints:** show you Terminal 1 after steps 3, 6, and 7.

**Acceptance criteria:** rules quoted, robots.txt read, a sleep before each page, a User-Agent,
28 listings in `shelf.csv`, step 7 recorded.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus two additions that need things not taught.

**Added requirement 1.** Do the stretch goal: follow `Next page` links with a visited set, so your
scraper makes no 404 request.

**Added requirement 2.** Read `table_reader.py` and explain, in your README, how it knows it is
inside a table cell, and why `&amp;` in the page source arrives in your data as `&`.

**Hint, not the answer.** The helper is built on `html.parser.HTMLParser`. Read the example at the
top of its documentation, `https://docs.python.org/3/library/html.parser.html`, and look at which
methods the example overrides and when each one is called. Then look up what `convert_charrefs`
does on the same page.

**Acceptance criteria:** all STANDARD criteria, zero 404s in Terminal 1, and an accurate explanation
of the helper in your own words.

---

## APPLIED

**For the student who asks where this is used for real.** Price comparison, research datasets,
monitoring a page for changes. The same rules apply everywhere, and deciding not to scrape is a
real outcome.

**Changed scenario.** Side Quest 13, The Scraper, uses a second invented site, a card shop, with a
data feed for its events and a price guide its terms forbid copying. Complete SQ-13's first
checkpoint instead of this lab's steps 4 to 8: run that site, read its `robots.txt` and terms, and
write a `Why this was allowed` section that names which parts you **may** collect, which you may
not, and which part you must get from the feed instead. Then collect only the allowed pages.

**The extra requirement that makes it the same lab.** Step 7's deliberate 429, done against the
card shop, and Terminal 1's log of your polite run pasted into the README.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether the student collected
exactly what the rules allow, no more and no less.
