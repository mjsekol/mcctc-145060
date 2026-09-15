# Getting Data Off a Website, Responsibly
---
## Slide 1: The data is right there on the page
- The game club lists 28 games on its site
- No download button, no data feed
- Copying by hand takes an hour and has typos
- A program could do it in ten seconds
Speaker notes: The game club's swap shelf website lists every donated game with its price and condition. You want that data in a spreadsheet. There is no download button. You could copy it by hand for an hour, or write a program that reads the pages for you. That is called scraping. It is powerful, and it is the one skill in this unit where doing it badly affects someone else's website.
Image: A web page table with an arrow pointing to a clean spreadsheet.
---
## Slide 2: Six rules before a single request
- Read robots.txt first, and obey it
- Read the terms of use, and quote them
- Wait between requests, at least what they ask
- Never scrape anything behind a login
- Never collect personal information, and use an API if offered
Speaker notes: These are not suggestions. robots dot txt is the site telling programs where they may go. The terms of use are what the owner allows. Waiting between requests keeps your program from hammering a small site that a club pays for. A login page means the data is private. Personal information is off limits no matter how simple it is to reach. And if the site offers an API or a data feed, use it instead, because it is what they built for you.
Image: A six-item checklist on a clipboard, no people.
---
## Slide 3: robots.txt is a public note to programs
```
User-agent: *
Crawl-delay: 2
Disallow: /members/
Disallow: /drafts/
```
Speaker notes: This is the real robots dot txt from the swap shelf site you will run on your own computer. User agent star means every program. Crawl delay two means wait two seconds between requests. Disallow means do not go into the members area or the drafts. Nothing stops you. The members page will load if you ask for it. robots dot txt is a request, and respecting it is your decision.
Image: None. This slide is code.
---
## Slide 4: Ask Python to read the rules for you
```python
robots = urllib.robotparser.RobotFileParser(BASE_URL + "/robots.txt")
print("Before read():", robots.can_fetch(USER_AGENT, BASE_URL + "/shelf/page-1.html"))
robots.read()
print("Shelf allowed:  ", robots.can_fetch(USER_AGENT, BASE_URL + "/shelf/page-1.html"))
print("Members allowed:", robots.can_fetch(USER_AGENT, BASE_URL + "/members/index.html"))
print("Crawl-delay:    ", robots.crawl_delay(USER_AGENT))
```
```
Before read(): False
Shelf allowed:   True
Members allowed: False
Crawl-delay:     2
```
Speaker notes: The standard library reads robots dot txt for you. can fetch answers whether a URL is allowed. Look at the first line of output. Before read runs, can fetch says False for everything, because it has not seen the rules yet. Forget to call read and your scraper decides nothing is allowed and collects nothing, with no error.
Image: None. This slide is code.
---
## Slide 5: Ask slowly, and say who you are
```python
time.sleep(2)
request = urllib.request.Request(BASE_URL + "/shelf/page-1.html",
                                 headers={"User-Agent": USER_AGENT})
with urllib.request.urlopen(request, timeout=10) as response:
    page_text = response.read().decode("utf-8")

rows = read_tables(page_text)[0]
print(rows[1])
# ['OH-101', 'Moss Knight Chronicles', 'Switch', 'Like New', '$18.00', 'Available']
```
Speaker notes: sleep two before every request is the rate limit. The User Agent header tells the site what program is asking, which the terms require. timeout ten means a site that never answers cannot freeze your program. Then read tables, a helper that uses Python's own HTML parser, turns the page's table into rows of cells.
Image: None. This slide is code.
---
## Slide 6: Watch this: skip the parser, split on td
```python
prices = []
for chunk in page_text.split("<td>")[1:]:
    cell = chunk.split("</td>")[0]
    if cell.startswith("$"):
        prices.append(cell)
print(f"Prices found: {len(prices)}")
```
```
Prices found: 0
```
Speaker notes: It is tempting to treat HTML as plain text and split on the cell tag. Page one has ten prices. This found zero, and it did not crash. The price cells are written as td class equals price, so the text you split on never appears in front of a price. HTML has attributes, line breaks, and codes like amp in places plain splitting does not expect. That is why you use a parser.
Image: None. This slide is code.
---
## Slide 7: Skip the wait and the site says no
```
urllib.error.HTTPError: HTTP Error 429: Too Many Requests
```
- Three pages requested back to back
- The first worked, the second was refused
- 429 means you are asking too fast
- Many real sites also block you after this
Speaker notes: This is what the fixture site does when requests arrive less than a second apart, and plenty of real sites behave the same way. Status four twenty nine, too many requests. Your program crashed, and that is the lucky outcome, because you found out immediately. The fix is not a retry loop that asks faster. The fix is the sleep you left out.
Image: None. The error is the content.
---
## Slide 8: Watch the server count your manners
```
[14:24:07] GET /robots.txt -> 200  (first request)
[14:24:09] GET /shelf/page-1.html -> 200  (2.1 s after the previous request)
[14:24:11] GET /shelf/page-2.html -> 200  (2.0 s after the previous request)
[14:24:13] GET /shelf/page-3.html -> 200  (2.0 s after the previous request)
[14:24:15] GET /shelf/page-4.html -> 404  (2.0 s after the previous request)
```
Speaker notes: This is the log from the site's terminal during a polite run, with the User Agent trimmed off the end of each line so it fits. robots dot txt first. Every request two seconds apart. And page four answers 404, not found, which is how the scraper knows it has run out of pages. When you run your lab, keep this terminal where you can see it. It shows you exactly how your program treats someone else's server.
Image: None. The log is the content.
---
## Slide 9: Allowed by robots.txt is not the same as allowed
- robots.txt covers where programs may go
- Terms of use can forbid more than robots.txt does
- A page can be reachable and still private
- Deciding not to scrape is a valid result
Speaker notes: Here is the judgment part. robots dot txt and the terms of use are two different documents, and you have to pass both. A site can leave a page open in robots dot txt and forbid copying it in its terms. And a student who reads the rules and decides a site should not be scraped, then writes down why, has done the skill correctly. Side quest thirteen is built around exactly that decision.
Image: Two separate gates in a row, both of which must be open.
---
## Slide 10: What you are about to build
- Lab U5-05: scrape the Swap Shelf, politely
- Run the site yourself in its own terminal
- robots.txt, a two-second wait, a User-Agent
- Build 2: the data pipeline opens
Speaker notes: Build one is the Swap Shelf Scraper lab. You start the club's website on your own computer, read its robots dot txt and terms, collect all three pages with a two second wait, and write the listings to a CSV. Step seven has you remove the wait on purpose and record the 429. Nobody in this class scrapes a real website for this lab. Keep the shelf dot CSV file your scraper writes. Build two opens the data pipeline project. Choose your route, write down every kind of mess in the data before any code, and read both sources into lists of dictionaries.
Image: Two terminals side by side, a server log on the left and a scraper on the right.
