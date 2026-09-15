# Lecture Notes: Getting Data Off a Website, Responsibly
## 145060 Programming · Unit 5 · Week 11, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W11_ResponsibleScraping.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W11_ResponsibleScraping.pptx)

If you missed class, you can learn this concept from this file alone. You need the
fixture site from `05-labs/fixtures/swap-shelf/`, which runs on your own computer.
**Nothing in this lesson, the lab, or the project touches a real website.**

**Every program below was run on Python 3.13.7, on Windows, against the fixture site.**
The output shown is the real output. Times in the server log will be different when you
run it.

---

## Why this exists

The Oak Hollow High School Game Club sells donated games to pay tournament fees. Its
website lists 28 of them across three pages, with prices and conditions. There is no
download button and no data feed. (The club is invented, and so is its website. You run
it yourself.)

You want that list in a spreadsheet. You could copy it by hand for an hour and make
typos, or write a program that reads the pages. Reading data out of web pages with a
program is called **scraping**.

Scraping is the one skill in this unit where doing it carelessly affects **somebody
else**. A program can send hundreds of requests a second to a small site that a club or a
family business pays for. It can reach pages the owner never meant to share. It can
collect information about people who never agreed to it. So this lesson starts with the
rules, and the code comes second.

---

## The rules, before a single request

| Rule | Why |
|---|---|
| **Read `robots.txt` first, and obey it.** | It is the site telling programs where they may go and how fast. |
| **Read the terms of use, and quote the sentence that allows you.** | The owner decides what may be copied. robots.txt does not cover everything. |
| **Rate limit yourself.** At least what the site asks, and never faster than one request every two seconds in this course. | A small site can be slowed or knocked over by a fast loop. |
| **Never scrape anything behind a login.** | A sign-in page means the data is private. |
| **Never collect personal information about anybody.** | Names, contact details, and photos of real people are not yours to gather, however reachable they are. |
| **If the site offers an API or a data feed, use that instead.** | It is what the owner built for programs, and it will not break when they redesign a page. |

**Deciding not to scrape a site, and writing down why, is a correct result.** Side Quest
13 is built around exactly that decision.

---

## Running the fixture site

You need **two terminals**.

**Terminal 1, the website:**

```
cd 05-labs/fixtures/swap-shelf
python serve_site.py
```

```
Swap Shelf running at http://127.0.0.1:8000/
Press Ctrl+C to stop.
```

Leave it running. Open `http://127.0.0.1:8000/` in a browser to look at the site the way
a person would. Every request, from your browser or your program, prints a line in this
terminal with the time since the one before.

**Terminal 2, your program.** Copy `table_reader.py` from the same folder into the folder
where your scraper lives, then run your scraper there.

When you are done, go back to Terminal 1 and press **Ctrl+C**.

If port 8000 is busy, the server says so. Run `python serve_site.py 8001` and change your
program's address to match.

---

## The concept in plain language

**Ask the site's rules first. Then ask slowly, say who you are, and use a parser.**

1. **Rules.** Download `robots.txt` and ask it whether each page is allowed.
2. **Slowly.** `time.sleep()` before every request.
3. **Say who you are.** Send a `User-Agent` header naming your program.
4. **Parse.** Turn the HTML into rows with a parser, not with `split`.
5. **Stop cleanly.** A page that answers 404 Not Found means you have run out of pages.

---

## Worked example 1: what robots.txt says

This is the fixture site's `robots.txt`:

```
# robots.txt for the Oak Hollow Game Club Swap Shelf
# Automated visitors: read this before you request anything else.

User-agent: *
Crawl-delay: 2
Disallow: /members/
Disallow: /drafts/
```

- `User-agent: *` means these rules apply to every program.
- `Crawl-delay: 2` asks for two seconds between requests.
- `Disallow: /members/` means do not request anything whose path starts with `/members/`.

**robots.txt is a request, not a lock.** Nothing stops a program from asking for
`/members/index.html`, and the server will send it. Whether you obey is your decision, and
it is the decision this lesson is about.

---

## Worked example 2: let Python read the rules, then fetch one page

```python
# Thursday Week 11 live-code: ask the site's rules first, then ask slowly.
import sys
import time
import urllib.request
import urllib.robotparser

from table_reader import read_tables

BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"
USER_AGENT = "OakHollowShelfReader/1.0 (MCCTC 145060 class project)"

robots = urllib.robotparser.RobotFileParser(BASE_URL + "/robots.txt")
print("Before read():", robots.can_fetch(USER_AGENT, BASE_URL + "/shelf/page-1.html"))
robots.read()
print("Shelf allowed:  ", robots.can_fetch(USER_AGENT, BASE_URL + "/shelf/page-1.html"))
print("Members allowed:", robots.can_fetch(USER_AGENT, BASE_URL + "/members/index.html"))
print("Crawl-delay:    ", robots.crawl_delay(USER_AGENT))

time.sleep(2)
request = urllib.request.Request(BASE_URL + "/shelf/page-1.html", headers={"User-Agent": USER_AGENT})
with urllib.request.urlopen(request, timeout=10) as response:
    page_text = response.read().decode("utf-8")

rows = read_tables(page_text)[0]
print(rows[0])
print(rows[1])
print(len(rows) - 1, "listings on page 1")
```

(The first `BASE_URL` line lets the same file run against a different port if you type
one after the file name. `python thu_scrape.py` uses port 8000.)

Output:

```
Before read(): False
Shelf allowed:   True
Members allowed: False
Crawl-delay:     2
['Item ID', 'Title', 'Platform', 'Condition', 'Price', 'Status']
['OH-101', 'Moss Knight Chronicles', 'Switch', 'Like New', '$18.00', 'Available']
10 listings on page 1
```

And the site's terminal:

```
[14:47:40] GET /robots.txt -> 200  (first request)  User-Agent: Python-urllib/3.13
[14:47:42] GET /shelf/page-1.html -> 200  (2.1 s after the previous request)  User-Agent: OakHollowShelfReader/1.0 (MCCTC 145060 class project)
```

Read it piece by piece:

- **`RobotFileParser`** holds the rules. **`.read()`** downloads them. **`.can_fetch()`**
  answers whether a URL is allowed for your user agent. **`.crawl_delay()`** returns the
  delay the site asked for, or `None` if it did not ask.
- **Look at the first line of output.** Before `.read()`, `can_fetch` says `False` for
  everything, because it has not seen the rules. Forget to call `.read()` and your scraper
  decides nothing is allowed and collects nothing, with no error.
- **`urllib.request.Request`** lets you attach headers. The site's terms ask programs to
  identify themselves, so the `User-Agent` names the program and why it exists. Notice in
  the log that `robots.read()` did not send your User-Agent. It uses Python's default.
- **`timeout=10`** means a site that never answers raises an error after ten seconds
  instead of freezing your program forever.
- **`response.read()`** gives bytes. **`.decode("utf-8")`** turns them into text.
- **`read_tables()`** comes from `table_reader.py`, a helper in the fixture folder. It uses
  Python's own HTML parser, `html.parser`, and gives you each table as a list of rows, each
  row a list of cell strings. It uses a class inside, which is Unit 7. You may use it the
  same way you use `json` without reading its source.

---

## Worked example 3: every page, politely, into a CSV

The full version is the Lab U5-05 solution. The loop at its heart:

```python
listings = []
page_number = 1
while True:
    url = f"{BASE_URL}/shelf/page-{page_number}.html"
    if not robots.can_fetch(USER_AGENT, url):
        print(f"Stopping: robots.txt does not allow {url}")
        break
    time.sleep(delay)
    try:
        page_text = fetch(url)
    except urllib.error.HTTPError as error:
        # 404 means we have run out of pages. Anything else is a real problem.
        if error.code == 404:
            break
        print(f"Stopping: {url} answered {error.code} {error.reason}")
        break
    tables = read_tables(page_text)
    records = rows_to_dicts(tables[0])
    print(f"Page {page_number}: {len(records)} listings")
    for record in records:
        listings.append(record)
    page_number += 1
```

`rows_to_dicts` turns the header row and the rows under it into a list of dictionaries,
the same table shape you built on Thursday of Week 10. From there, `csv.DictWriter` writes
it out.

Output of the lab solution:

```
robots.txt: /shelf/page-1.html is allowed
robots.txt: /members/index.html is NOT allowed
robots.txt: /drafts/new-donations.html is NOT allowed
Waiting 2 seconds before each request.
Page 1: 10 listings
Page 2: 10 listings
Page 3: 8 listings
Wrote 28 listings to shelf.csv. Marked sold: 11.
```

The site's terminal:

```
[14:24:07] GET /robots.txt -> 200  (first request)  User-Agent: Python-urllib/3.13
[14:24:09] GET /shelf/page-1.html -> 200  (2.1 s after the previous request)  User-Agent: OakHollowShelfReader/1.0 (MCCTC 145060 class project)
[14:24:11] GET /shelf/page-2.html -> 200  (2.0 s after the previous request)  User-Agent: OakHollowShelfReader/1.0 (MCCTC 145060 class project)
[14:24:13] GET /shelf/page-3.html -> 200  (2.0 s after the previous request)  User-Agent: OakHollowShelfReader/1.0 (MCCTC 145060 class project)
[14:24:15] GET /shelf/page-4.html -> 404  (2.0 s after the previous request)  User-Agent: OakHollowShelfReader/1.0 (MCCTC 145060 class project)
```

`HTTPError` is how `urllib` reports a status code that is not a success. **404** means
not found. `error.code` holds the number, so you can treat "out of pages" differently from
a real failure.

---

## The wrong version: treat HTML as plain text

It is tempting to skip the parser and split the page on the cell tag:

```python
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    page_text = response.read().decode("utf-8")

prices = []
for chunk in page_text.split("<td>")[1:]:
    cell = chunk.split("</td>")[0]
    if cell.startswith("$"):
        prices.append(cell)
print(f"Prices found: {len(prices)}")
print(prices)
```

Run against page 1:

```
Prices found: 0
[]
```

**Page 1 has ten prices. This found zero, and it did not crash.** The page source writes
every price cell as `<td class="price">$18.00</td>`. The text `<td>` never appears in front
of a price, so every price is skipped.

Real HTML is full of this. Attributes inside tags. Line breaks inside cells: page 1 writes
one title across three lines. Codes like `&amp;` in place of `&`. A parser reads the page
the way a browser does. `split` reads it the way you hoped it was written.

---

## The other wrong version: no waiting

```python
import sys
import urllib.request

base = sys.argv[1]
for number in [1, 2, 3]:
    url = f"{base}/shelf/page-{number}.html"
    with urllib.request.urlopen(url, timeout=10) as response:
        print(number, response.status)
```

Output:

```
1 200
Traceback (most recent call last):
  ...
urllib.error.HTTPError: HTTP Error 429: Too Many Requests
```

And the site's terminal:

```
[14:24:45] GET /shelf/page-1.html -> 200  (first request)  User-Agent: Python-urllib/3.13
[14:24:45] GET /shelf/page-2.html -> 429  (0.1 s after the previous request)  User-Agent: Python-urllib/3.13
```

**429 Too Many Requests** means you are asking too fast. The fixture site refuses any
request less than one second after the one before, and many real sites do something
similar, or block your address outright. This one crashed, which is the lucky outcome. The
fix is not a loop that retries faster. The fix is the `time.sleep()` you left out.

---

## Two surprises worth knowing

**If your program cannot reach the site at all,** you get this on Windows:

```
urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>
```

It almost always means `serve_site.py` is not running, or is running on a different port.

**If `robots.txt` itself answers 429, Python treats the site as having no rules.** We
tested this: a program requested the home page, then immediately asked for `robots.txt`,
which the fixture refused with 429. Afterwards `can_fetch` answered `True` for the shelf.
Python's robot parser treats most 400-range errors on `robots.txt` as "no robots.txt, so
everything is allowed." So slow down **before** you request `robots.txt` too, and if the
rules did not load cleanly, stop rather than assume.

---

## Allowed by robots.txt is not the same as allowed

`robots.txt` and the terms of use are **two different documents, and you must pass both.**

- A site can leave a page open in `robots.txt` and forbid copying it in its terms.
- A page can be reachable and still private. `/members/` on the fixture site loads if you
  ask. Its own text says it holds a member contact list.
- The Swap Shelf's terms say: "You may copy the item listings on the shelf pages for
  personal or school projects that are not commercial." That is the sentence you quote in
  your README.

When you finish a scraper, you should be able to write a short section called **Why this
was allowed** that quotes `robots.txt` and the terms. If you cannot write that section, you
should not run the scraper.

---

## Why the wrong versions are tempting

**Splitting works on the first page you test by hand.** Paste a simple table into a string
and `split` handles it. The real page has attributes you never looked at.

**Waiting feels like wasted time.** Three pages with two-second gaps takes about eight
seconds. Removing the sleep takes it to a fraction of a second, right up until the site
refuses you, or quietly blocks you.

**"It is on a public page" feels like permission.** Public means reachable. Permission comes
from the owner, in writing, in the terms.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Scraping** | Using a program to extract data from web pages. |
| **`robots.txt`** | A file at a site's root telling programs which paths to avoid and how fast to go. |
| **Terms of use** | The owner's written rules for using the site and its content. |
| **Rate limit** | A maximum request speed. Yours, or the site's. |
| **Crawl-delay** | The seconds between requests a site asks for in `robots.txt`. |
| **User-Agent** | A request header naming the program making the request. |
| **HTTP status code** | The server's answer: 200 OK, 404 Not Found, 429 Too Many Requests. |
| **`HTTPError`** | Raised by `urllib` for a status that is not a success. Has `.code`. |
| **`URLError`** | Raised when the server cannot be reached at all. |
| **Parser** | A program that reads HTML the way a browser does. |
| **API** or **data feed** | A way a site offers its data to programs directly. Preferred over scraping. |

---

## Self-check

**Question 1.** A site's `robots.txt` says `Disallow: /events/`. The events page has no
login, and it loads fine in a browser. May your scraper collect it? Explain in two
sentences.

**Question 2.** Write exactly what these three lines print for the fixture site, and say
why the first one surprises people.

```python
robots = urllib.robotparser.RobotFileParser("http://127.0.0.1:8000/robots.txt")
print(robots.can_fetch("MyBot", "http://127.0.0.1:8000/shelf/page-1.html"))
robots.read()
print(robots.can_fetch("MyBot", "http://127.0.0.1:8000/shelf/page-1.html"))
print(robots.can_fetch("MyBot", "http://127.0.0.1:8000/drafts/new-donations.html"))
```

**Question 3.** A classmate's scraper prints `Found 0 listings` against a page you can see
has 28. It did not crash. Name two different causes this lesson showed you, and how to tell
them apart.

---

### Answers

**1.** No. `robots.txt` asks programs to stay out of `/events/`, and a page loading in a
browser only shows it is reachable, not that the owner allows programs to collect it. If the
site offers an events feed, that is the thing to use; otherwise, leave it alone.

**2.**

```
False
True
False
```

The first is `False` because `can_fetch` returns `False` for everything until `.read()` has
loaded the rules. People expect it to mean the page is forbidden. The drafts page is
`False` because `robots.txt` disallows `/drafts/`.

**3.** Cause one: the parsing is wrong, such as splitting on `<td>` when cells carry
attributes, so rows are skipped without an error. Cause two: `can_fetch` was called before
`robots.read()`, so the scraper decided every page was forbidden and fetched nothing. Tell
them apart with the server's terminal: if the pages were requested and answered 200, the
parsing is wrong; if they were never requested at all, the scraper never fetched them.
