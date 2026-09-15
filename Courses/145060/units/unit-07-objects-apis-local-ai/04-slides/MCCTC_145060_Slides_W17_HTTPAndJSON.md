# Asking Another Program for Data
---
## Slide 1: Where does a bus app get the next arrival
- You open the app, a number appears
- Your phone did not know that number
- It asked a server, over the network
- Today your program does the asking
Speaker notes: When you open a bus app and see the next arrival, your phone did not know that. It asked a transit server and got the number back. Today your program becomes the one asking. It sends a request to another program and gets data in return.
Image: A phone sending a request arrow to a server, a number coming back.
---
## Slide 2: Three steps, three types
- open the URL, get a response
- read the body, get bytes
- decode, get text
- parse as JSON, get Python data
Speaker notes: There are three steps between asking and having data you can use. Open the URL and get a response. Read the body and get raw bytes. Decode the bytes to text, then parse the text as JSON, which gives you a dictionary or a list. Watch the type change at each step.
Image: A pipeline: response, then bytes, then text, then a dict, each labeled.
---
## Slide 3: The three steps in code
```python
import json, urllib.request
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
with opener.open("http://127.0.0.1:8070/api/v1/stations", timeout=5) as response:
    raw = response.read()
print(type(raw))                      # <class 'bytes'>
data = json.loads(raw.decode("utf-8"))
print(type(data))                     # <class 'dict'>
```
Speaker notes: Read it top to bottom. We skip proxies, because a school proxy cannot reach 127.0.0.1. We open with a timeout, always. Read gives bytes. Decode gives text. json dot loads gives a dictionary. Miss a step and you get an error.
Image: None. This slide is code.
---
## Slide 4: Now it is ordinary Python
```python
with opener.open(url + "/stations/north-field/observations", timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))
print(data["name"])                          # North Practice Field
print(data["observations"][0]["gust_mph"])   # 19
```
Speaker notes: Once it is a dictionary, it is data you already know how to handle from Unit 5. A JSON object becomes a dictionary. A JSON array becomes a list. You reach in with keys and indexes, exactly like a save file. The network part is over. The rest is Unit 5.
Image: None. This slide is code.
---
## Slide 5: Always set a timeout
- A dead server can hang forever
- A missing timeout freezes your program
- timeout=5 means give up after five seconds
- This is an availability problem
Speaker notes: The timeout is not optional. Without it, a slow or dead server can freeze your program with no way out, and a person waiting on it is stuck. That is an availability problem, a term you will name next week. Set a timeout on every request, every time.
Image: A spinner that never stops, crossed out, next to timeout=5.
---
## Slide 6: The trap, a page that is not JSON
```python
with opener.open("http://127.0.0.1:8070/api/stations", timeout=5) as response:
    data = json.loads(response.read().decode("utf-8"))
```
Speaker notes: This old address returns an HTML page for old bookmarks, not JSON. The request succeeds. Read returns something. It feels like it worked. Predict what json dot loads does with an HTML page before the next slide.
Image: None. This slide is code.
---
## Slide 7: Expecting value, column 1
```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
Speaker notes: The reply started with a less-than sign, the start of HTML, and json dot loads cannot read that. Column one, character zero, the very first character. The request succeeded and the data was still wrong. Getting a reply is not the same as getting the data you asked for.
Image: None. This slide is code.
---
## Slide 8: Reply is not the same as data
- Getting a reply is not getting your data
- A wrong address returns a real reply
- A login page returns a real reply
- Check what you got, do not assume
Speaker notes: This is the running thread wearing a network costume. The server answered, but a wrong address, a redirect, or an old endpoint all return a real response that is not your data. The crash here is the friendly case. Next week you handle the quiet failures too.
Image: Three different "successful" replies, only one of which is the data you wanted.
---
## Slide 9: Standard library only
- urllib.request sends the request
- json parses the reply
- Nothing to install
- Works on any lab machine
Speaker notes: Everything today is in Python already. urllib dot request for the request, json for the reply. No packages, no install, nothing that can be missing on a lab machine. The same two modules carry you through the whole week, including talking to the local model.
Image: Two standard-library modules labeled, a checkmark for "already installed".
---
## Slide 10: What you are about to build
- Start the weather station fixture
- Write get_json and read the stations
- Write decide for a calm and a windy reading
- Pass the Part 1 tests
Speaker notes: Build one starts the fixture server in one terminal and writes get_json to read the station list. Build two writes decide, the rule that says whether practice is on. Run the Part 1 tests until they pass. Tomorrow you handle everything that can go wrong.
Image: A terminal running the fixture next to a terminal running the client, navy and accent blue.
