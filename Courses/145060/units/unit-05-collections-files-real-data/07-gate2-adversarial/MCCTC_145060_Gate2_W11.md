# Gate 2: Adversarial Review · Week 11
## 145060 Programming · Unit 5 · Week 11, Friday

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether
it is correct, because the model is what is being reviewed.

The program is in `gate2-w11-files/price_watch.py`, with a copy of `table_reader.py` next to
it. It runs against the Swap Shelf fixture site from Thursday's lab.

---

## How to run it

**Terminal 1:** start the site, and keep this terminal where you can see it.

```
cd 05-labs/fixtures/swap-shelf
python serve_site.py
```

**Terminal 2:** run the program from its own folder.

```
cd 07-gate2-adversarial/gate2-w11-files
python price_watch.py
```

It takes about fifteen seconds, because it waits between requests. It creates
`last_prices.json` in the folder you run it from. Delete that file to simulate a first run.

**Stop the site with Ctrl+C in Terminal 1 when you finish.**

---

## What you are looking at

A club member asked an AI assistant for a price watcher and got the program in Part B. It
reads `robots.txt`, uses the crawl delay, identifies itself, saves JSON, and handles a
missing file. It looks like it learned everything from this week.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It reads, exposes, or trusts something it should not, or ignores rules it should obey |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing, or something nobody asked for |

---

## PART A: The requirements

> Write `price_watch.py` for the Oak Hollow Game Club Swap Shelf.
>
> 1. Read the site's `robots.txt` first, and **never request a page it disallows**.
> 2. Wait at least two seconds between requests, or longer if `robots.txt` asks. Identify the
>    program in the User-Agent header.
> 3. Find listings by exploring the site from the home page, so a new shelf page is found
>    without changing the code.
> 4. Remember each available item's price between runs in `last_prices.json`. On the first run,
>    when there is no file, report no drops and count every available item as new.
> 5. **If `last_prices.json` is damaged, stop without changing it**, so a person can look at it.
> 6. Print every available item whose price went **down** since the last run, with the old price,
>    the new price, and the percent off. Ignore items marked SOLD.
> 7. Print how many available items are new since the last run.
> 8. Save today's prices for available items, replacing the previous file.

---

## PART B: What the AI produced

Count line numbers from `# price_watch.py` as line 1. Blank lines count.

```python
# price_watch.py
#
# Watches the Oak Hollow Game Club Swap Shelf for price drops.
# Run it once to remember today's prices. Run it again later to see what
# got cheaper since last time.
#
# Start the site first, in another terminal:  python serve_site.py

import json
import sys
import time
import urllib.parse
import urllib.request
import urllib.robotparser

from table_reader import read_links, read_tables

BASE_URL = "http://127.0.0.1:8000"
START_PAGE = BASE_URL + "/index.html"
USER_AGENT = "SwapShelfPriceWatch/1.0 (MCCTC 145060 student project)"
PRICES_FILE = "last_prices.json"
WAIT_MS = 2


def read_robots():
    """Download the site's robots.txt so the crawler can follow its rules."""
    robots = urllib.robotparser.RobotFileParser(BASE_URL + "/robots.txt")
    robots.read()
    return robots


def fetch(url):
    """Download one page, identifying this program, and return its text."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=10) as response:
        return response.read().decode("utf-8")


def parse_price(text):
    """Turn '$18.00' or '18' into 18.0. Return None for 'Make an offer'."""
    cleaned = text.strip().lstrip("$")
    try:
        return float(cleaned)
    except ValueError:
        return None


def crawl_listings(robots):
    """Visit every page on the site once and collect the rows of every listing table."""
    # Respect the site's requested crawl delay, falling back to our own.
    delay = robots.crawl_delay(USER_AGENT) or WAIT_MS
    to_visit = [START_PAGE]
    visited = set()
    listings = []
    while to_visit:
        url = to_visit.pop(0)
        if url in visited:
            continue
        visited.add(url)
        time.sleep(delay)
        page_text = fetch(url)

        for table in read_tables(page_text):
            header = table[0]
            if header[0] != "Item ID":
                continue
            for cells in table[1:]:
                listing = {}
                for position in range(len(header)):
                    listing[header[position]] = cells[position]
                listings.append(listing)

        # Queue every link that stays on this site.
        for link in read_links(page_text):
            next_url = urllib.parse.urljoin(url, link["href"])
            if next_url.startswith(BASE_URL) and next_url not in visited:
                to_visit.append(next_url)
    return listings


def load_previous():
    """Return the prices saved by the last run as a dictionary of item ID to price."""
    try:
        with open(PRICES_FILE, encoding="utf-8") as prices_file:
            return json.load(prices_file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def report_changes(listings):
    """Print price drops and new items. Return today's prices to save."""
    current = {}
    drops = 0
    new_items = 0
    for listing in listings:
        if listing["Status"].upper() == "SOLD":
            continue
        previous = load_previous()
        item_id = listing["Item ID"]
        price = parse_price(listing["Price"])
        current[item_id] = price
        if item_id not in previous:
            new_items += 1
            continue
        # Match IDs without case, so "oh-101" and "OH-101" count as the same item.
        old_price = previous.get(item_id.lower())
        if old_price is not None and price is not None and price < old_price:
            percent = (old_price - price) / old_price * 100
            print(f"  {item_id} {listing['Title']}: ${old_price:.2f} -> ${price:.2f} ({percent:.0f}% off)")
            drops += 1
    if drops == 0:
        print("  No price drops since last run.")
    print(f"  New since last run: {new_items}")
    return current


def save_prices(prices):
    with open(PRICES_FILE, "w", encoding="utf-8") as prices_file:
        json.dump(prices, prices_file, indent=2)


def main():
    robots = read_robots()
    listings = crawl_listings(robots)
    print(f"PRICE WATCH: {len(listings)} listings found")
    prices = report_changes(listings)
    save_prices(prices)
    print(f"Saved {len(prices)} prices to {PRICES_FILE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### A real run

Terminal 2, the first run, with no `last_prices.json`:

```
PRICE WATCH: 28 listings found
  No price drops since last run.
  New since last run: 17
Saved 17 prices to last_prices.json.
```

Terminal 2, the second run, straight after the first:

```
PRICE WATCH: 28 listings found
  No price drops since last run.
  New since last run: 0
Saved 17 prices to last_prices.json.
```

Both runs look exactly right. **The fixture site's prices never change, so to test requirement
6 you have to change the saved file.** Open `last_prices.json` after a run, raise one saved price,
save it, and run again.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**, and **the
fix**. Then one final entry: **what I was unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 10:** run it twice with Terminal 1 visible. Read **every** line Terminal 1 prints, and
  compare the paths to the site's `robots.txt`.
- **Next 10:** test requirement 6 by raising a saved price. Then test requirement 5: put the words
  `not json` in `last_prices.json` and run it. Open the file afterwards.
- **Next 5:** read Part A one requirement at a time and point at the line that satisfies it.
- **Rest:** read every name and comment against what the code does. Count how many times a file is
  opened.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the security
weighting before you start. **Four of five is a strong score.**
