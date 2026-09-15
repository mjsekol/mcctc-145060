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
