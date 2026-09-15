# When the Request Goes Wrong
---
## Slide 1: The request will fail, plan for it
- Yesterday you handled the happy path
- Most days are not the happy path
- The stop id is wrong, the server is slow
- You are asking too fast
Speaker notes: Yesterday you got data on the happy path. Today you plan for the days it does not go right, because most days something does. The stop id is wrong. The server is slow. You are asking too fast. Each one means something different, and a good program says which.
Image: Three broken paths from a phone to a server, each labeled with a different failure.
---
## Slide 2: Three failures, three meanings
- 404 the thing does not exist
- Timeout the server is too slow now
- 429 you are asking too fast
- Each needs a different message
Speaker notes: A 404 means the thing does not exist, and retrying will never help. A timeout means the server is there but too slow right now, and later might work. A 429 means slow down, wait the requested time. Three failures, three different things for the user to do.
Image: A table with 404, timeout, 429 and a one-line action for each.
---
## Slide 3: The ordering rule
- HTTPError is a kind of URLError
- Python runs the first match
- So catch HTTPError first
- Reversed, a 404 looks like no connection
Speaker notes: Here is the one rule you must get right. HTTPError is a kind of URLError, and Python runs the first except clause that matches. So HTTPError has to come first. If URLError came first, it would catch a 404 too, and report it as cannot connect, which is wrong.
Image: Two except clauses stacked, HTTPError above URLError, an arrow "specific first".
---
## Slide 4: Each failure, its own branch
```python
try:
    with opener.open(url, timeout=t) as response:
        return json.loads(response.read().decode("utf-8")), None
except urllib.error.HTTPError as error:
    error.close()
    if error.code == 404:
        return None, "NOT FOUND. Check the id. Retrying will not help."
    if error.code == 429:
        return None, "RATE LIMITED. Wait, then try again."
    return None, f"SERVER ERROR. HTTP {error.code}. Try later."
```
Speaker notes: HTTPError first, and inside it the status code tells 404 from 429 from 500. Each returns its own message that says what to do. The caller gets either the data or a sentence a person can act on. Nothing is hidden, nothing is guessed.
Image: None. This slide is code.
---
## Slide 5: Timeout and no connection
```python
except urllib.error.URLError as error:
    if isinstance(error.reason, TimeoutError):
        return None, "TIMED OUT. Try again in a minute."
    return None, f"CANNOT CONNECT. Is the server running? ({error.reason})"
except TimeoutError:
    return None, "TIMED OUT. Try again in a minute."
```
Speaker notes: A timeout can arrive inside a URLError or on its own, so we check both. A refused connection is a URLError whose reason is not a timeout. Two different situations, two different messages. The server being slow and the server being gone are not the same, and the user should not be told they are.
Image: None. This slide is code.
---
## Slide 6: The trap, one message for all
```python
try:
    data = fetch(url, 5)
except Exception:
    print("Error")
```
Speaker notes: This is the tempting shortcut. Catch everything, print Error, no more red text. Predict what a user does after seeing the word Error. They cannot tell if the id is wrong, the server is slow, or they are asking too fast. Watch why this is worse than a crash.
Image: None. This slide is code.
---
## Slide 7: One word helps no one
- No traceback, no crash, no information
- 404, timeout, 429 all say Error
- Each has a different fix
- All three are hidden
Speaker notes: There is no crash, and there is no information. A 404, a timeout, and a 429 all print Error. The person cannot tell which happened, and each has a different fix. This is both a Requirements Fit failure and a Security failure, because swallowing errors hides real problems.
Image: Three different failures all funneling into one word, Error.
---
## Slide 8: Retry-After tells you the wait
- A 429 usually carries a header
- Retry-After says how many seconds
- Read it, do not guess
- Then wait, or tell the user
Speaker notes: A 429 usually includes a header called Retry-After with the exact seconds to wait. Read it instead of guessing. Then you decide, wait that long and retry once if it is short, or tell the user to come back if it is long. That decision is a real design choice.
Image: A 429 reply with a Retry-After header highlighted.
---
## Slide 9: Why the shortcut is tempting
- It makes the red text go away
- It is one line
- Not crashing feels safe
- But it silences the reason
Speaker notes: Catch-all print Error is tempting because it silences the crash in one line, and not crashing feels safe. But not crashing is a low bar. The job of error handling is to turn a failure into an honest message a person can act on, not to hide it. Name each failure you expect.
Image: A single catch-all next to a set of named handlers, the named set favored.
---
## Slide 10: What you are about to build
- Write fetch with a branch per failure
- 404, timeout, feed error, bad page
- Add the empty-readings case
- Pass the Part 2 tests
Speaker notes: Build one writes fetch so a 404, a feed error, a bad web page, and a timeout each get their own message. Build two adds the empty-readings case, where no readings does not mean calm weather, and the unreachable-server case. Pass every Part 2 test.
Image: A test runner with the Part 2 failure tests green, navy and accent blue.
