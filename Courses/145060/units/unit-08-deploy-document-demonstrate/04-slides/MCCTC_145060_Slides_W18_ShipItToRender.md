# Ship It: Your App on a Public Address
---
## Slide 1: It works on my machine
- Your text adventure runs for exactly one person
- Friday, five people open your link on their phones
- Nobody is sitting at your keyboard
- What has to change?
Speaker notes: Everything you built this semester runs on one computer, yours. On Friday you stand up and give people a link, and they open it on their phones. Your laptop is not involved. Today is about the gap between works on my machine and works. Everybody underestimates that gap exactly once, and I would rather you do it today, with me here, than Thursday night alone.
Image: A laptop on the left and three phones on the right with a broken dotted line between them, deep navy and accent blue.
---
## Slide 2: Two settings decide who can reach you
- Host: which connections your app accepts
- 127.0.0.1 means this machine only
- 0.0.0.0 means every connection, including Render's
- Port: the numbered door your app answers
- Render picks the port and tells you in PORT
Speaker notes: Think of a building. The host is which entrances are unlocked. One two seven zero zero one locks every door except the one from inside the building. Zero zero zero zero unlocks them all. The port is the apartment number. Render walks up and knocks on the apartment number it gave you. Wrong apartment, or locked front door, and nobody answers. Render screens change, so anything I say about Render menus today is something I confirmed this week.
Image: A simple building with numbered doors, one door highlighted in accent blue, a locked front entrance marked in navy.
---
## Slide 3: The smallest deployable web app
```python
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000

class OnTheAir(BaseHTTPRequestHandler):
    def do_GET(self):
        body = "Kestrel Ridge relay is on the air.".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = HTTPServer((HOST, PORT), OnTheAir)
server.serve_forever()
```
Speaker notes: This is the whole app. It is the standard library, the same http dot server module the Unit 7 stub model used, so there is nothing to install. do GET runs every time a browser asks for a page. We send a status, a length, and the body. I am going to run it and ask for the page with curl dot exe, and it is going to work. Watch what happens next.
Image: None. This slide is code.
---
## Slide 4: Same app, same machine, different door
```
curl.exe -s http://127.0.0.1:8000
Kestrel Ridge relay is on the air.

curl.exe -s -S http://10.200.57.157:8000
curl: (7) Failed to connect to 10.200.57.157:8000 after 2055 ms: Could not connect to server
```
Speaker notes: First request, through one two seven zero zero one, works. Second request, to this machine's own network address, which I got from ipconfig, is refused. Same machine. Same app. Same port. The app was told to accept connections from this machine talking to itself, and nothing else. Render's router is something else. Change one line, the host, to zero zero zero zero, and the second request works.
Image: None. This slide is code.
---
## Slide 5: The fix that passes every test on your laptop
```python
import os

HOST = "0.0.0.0"
PORT = os.environ.get("PORT", 8000)
```
Speaker notes: Render tells us the port through an environment variable called PORT. So we read it, with a sensible default of eight thousand for our laptop. I run it. It says listening on eight thousand. The page loads. Every test I can think of passes. Before I deploy, I am going to do one thing Render does that my laptop never does. I am going to set PORT myself.
Image: None. This slide is code.
---
## Slide 6: The wrong way, and the real error
```
$env:PORT = "10000"
python on_the_air.py

    server = HTTPServer((HOST, PORT), OnTheAir)
  ...
TypeError: 'str' object cannot be interpreted as an integer
```
Speaker notes: There it is. With PORT unset, get hands back my default, the number eight thousand. With PORT set, get hands back what the environment holds, the text one zero zero zero zero. Environment variables are always text. You have seen this bug before. Week two, twelve times three gave you one two one two one two. Same bug, and this time it only crashes on the one computer you cannot sit at.
Image: None. This slide is code.
---
## Slide 7: Convert at the moment you read
```python
PORT = int(os.environ.get("PORT", "8000"))
```
Speaker notes: Same habit as int around input. Convert at the moment you read the value, so an unconverted port never exists. Notice the default is now the text eight thousand in quotes. That means both paths, laptop and Render, go through int every time, and your laptop is finally testing the path Render uses. Then I add a health route that answers ok, and that is a deployable app.
Image: None. This slide is code.
---
## Slide 8: There is no model on Render
- Your model runs on lab hardware inside the building
- Render cannot reach it, and must not
- Every model call on Render fails
- Your app falls back and says so on the page
- Health checks never depend on the model
Speaker notes: Read this slide twice. The model you called in Unit 7 lives on lab hardware. Render cannot reach it, and opening a lab machine to the internet is not a class project decision. So on Render every model call fails, every single time. Version four of the text adventure already catches that and shows the stored description. That is why it can be deployed. Label the fallback, so nobody thinks a model wrote text it did not write. And never make your health route ask the model, or a healthy app looks dead forever.
Image: A school building with a model server inside and a cloud outside, a closed gate between them, navy and accent blue.
---
## Slide 9: What Render needs from your repository
- Code pushed to GitHub, because Render builds from there
- requirements.txt, even if it only holds a comment
- A start command that works from your repository folder
- PORT read, converted, and bound on 0.0.0.0
- A /health route that answers fast
Speaker notes: Render only sees what you pushed. Not your laptop, not the file you forgot to commit. Your requirements file can be a single comment, because the standard library needs nothing installed, and pip finishes cleanly on a file with no packages in it. The start command is exactly what you type in a terminal to start the app. If it does not work from your repository folder on your machine, it will not work on Render.
Image: A checklist on a clipboard next to a repository folder icon, accent blue checkmarks.
---
## Slide 10: What you are about to build
- Build 1: Lab U8-01, make Playlist Namer deploy-ready
- Run check_ready.py until all nine checks pass
- Build 2: the same five changes in your final project
- Commit, push, then create your Render service
Speaker notes: Build one is Lab U8 one. You get a small web app that works on your machine and is not ready to deploy. Five changes, and a checker that starts your app the way Render does and tells you exactly what is still wrong. Do not skip the checker, and do not argue with it. Build two, you make the same changes in your own final project, push, and create your Render service. If your deploy fails, read the log before you change anything, and change one thing at a time.
Image: A terminal showing a column of PASS lines, navy background with accent blue text.
---
