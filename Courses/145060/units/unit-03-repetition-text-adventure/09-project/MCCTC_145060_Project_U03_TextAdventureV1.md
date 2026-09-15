# Project: Text Adventure v1
## 145060 Programming · Unit 3 · Due end of block, Week 8, Tuesday

**Mode:** solo. **Gate:** 3, full tooling, decision log required. **Periods:** Build 2 every day
from Monday of Week 7 through Tuesday of Week 8. The modeling practice on Wednesday of Week 6 and the
`while` loop skeleton on Thursday of Week 6 are the warm-up.

**Competencies:** 5.3.6 (repetition control structures), 5.3.8 (nested structures), 5.1.3
(model the solution with flowcharts, IPO charts, decision trees, and pseudocode), 5.1.2
(algorithms and data structures in information processing), 5.4.7 (debug logic errors), 5.5.7
(read inputs), 5.5.5 (naming and comments).

**This is version 1 of four.** The same game grows in Unit 4 (functions and error handling), Unit 5
(data files and save games), and Unit 7 (a local language model writes room descriptions). Build a
world you will still want to work on at the end of the semester.

---

## The brief

Read this as though a person said it to you.

> I run Teen Game Night at the public library on Friday evenings. We have six old laptops that
> cannot run anything modern, and a lot of kids who show up early and have nothing to do until the
> tables open. I want short games they can play in a terminal while they wait.
>
> Here is what keeps going wrong with the ones people have given me. Some never end, so the kid walks
> away and the next kid sits down in the middle of somebody else's game. Some you cannot lose, so
> nobody cares. Some crash the second a nine-year-old mashes the keyboard, and then I am the one who has
> to figure out how to restart it. And some are so confusing that nobody gets past the first room.
>
> I do not care what the game is about. A spooky one would be a hit with some kids,
> but plenty of kids hate scary stuff, so do not make every game a haunted house. It has to be something
> I would put in front of an eleven-year-old.
>
> It should take about ten minutes to finish if you know what you are doing. And I need to be able to tell
> whether it works without playing it for an hour.

**That is the whole brief.** Notice what it does not say. It does not say how many rooms, what the commands
are, how you win, or how you lose. Those are yours to decide, and deciding them is most of the work.

**The library and its game night are a composite scenario** written for this project. The problems in it are
the real problems text games have.

---

## Your setting

**You choose it.** A spaceship with failing oxygen. The school after the last bell. A theme park after closing.
A shipwreck. A normal Tuesday that stops being normal. A haunted house is allowed and so is anything else. Nobody
is required to write horror.

Three rules for every setting:

- **Appropriate for an eleven-year-old.** Tense is fine. Gore is not.
- **No real people.** No classmates, teachers, celebrities, or anybody's actual house.
- **Invented places only,** or places so generic nobody could be identified, such as "a gas station."

---

## Requirements

### Design, before any code

These are a syllabus deliverable: **flowchart and pseudocode produced before any code is written.**

1. **An IPO chart** with a State section listing every value your game remembers between turns.
2. **A flowchart** of your game loop: every kind of command, every ending, and the report after the loop, using the
   four shapes from the Modeling Before Code notes. Paper photographed, a drawing tool, or typed. All are fine.
3. **Pseudocode** precise enough that a classmate could turn it into Python without asking you a question.
4. **A room map** showing every room and every exit.
5. **All four committed before `adventure.py` exists in your repository.** Your commit history is the evidence. A design
   commit that comes after your first code commit does not count, and redrawing the flowchart from finished code is not
   modeling.

### Technical

1. **At least 4 rooms.** Winning must require the player to visit at least 3 of them.
2. **A game loop.** A `while` loop controlled by a flag, where every turn shows the state, reads one command, updates the
   state, and checks for an ending.
3. **At least one win state and at least one lose state** that a player can reach by playing. Quitting is not a lose state.
4. **At least one state variable besides the room and a move counter** that changes what the player can do, such as an item,
   a switch, or a door that opens.
5. **A report after the loop** that prints the right ending for every way the game can end.
6. **Input handling.**
   - Commands work in any capitalization and with extra spaces
   - An empty line gets a helpful message
   - An unknown command gets a message that names what was typed
   - A move with no exit gets a message and costs nothing
   - A `help` command lists every command
   - **Nothing the player types crashes the game.** Any number the game asks for is checked with a validation loop or a check
     before it is converted
7. **At least one `for` loop that does real work** in the game.
8. **Constants** for room names and for every number that controls the game, such as a move limit.
9. **Test scripts.** A `win.txt` that wins the game, and one script for each lose state, each reaching its ending when run with
   `python adventure.py < test-scripts/win.txt`.

### Repository

```
text-adventure/
  design/
    ipo-chart.md
    flowchart.png        (or .jpg, .pdf, or .md)
    pseudocode.md
    room-map.md          (or an image)
  test-scripts/
    win.txt
    lose-<name>.txt      (one per lose state)
  adventure.py
  README.md
  decision-log.md        (daily goal and result lines, and why you made each big choice)
  AI-usage-log.md
  .gitignore
```

### README, six sections

1. **The game.** Two sentences: the setting and the goal.
2. **How to play.** The command to run it and the list of commands.
3. **How to test it.** The exact commands to run each test script, and which ending each one reaches.
4. **The map.** Your room map, or a link to it in `design/`.
5. **The algorithm.** In one paragraph: describe your game loop as an algorithm, name the state variables it processes, and say which
   kind of loop you used for which job and why. This is outcome 5.1.2 in your own words.
6. **Known limitations.** What you know does not work or is awkward, observed, not guessed. At minimum: what happens when a test script
   runs out of commands before the game ends. Run it and paste what happened.

---

## Constraints, and why each one exists

| You may not | Why |
|---|---|
| Use `def`, lists, dictionaries, `try`, `import`, or classes | Version 1 is built from Unit 3 tools. Version 2 rebuilds it with functions, and you need to feel what is awkward without them to understand what they fix. Code you cannot explain fails the course standard. |
| Write any code before your design is committed | The syllabus requires the model first. A flowchart drawn after the code documents what you built. It does not catch what you missed. |
| Copy a text adventure from the internet or from a model and change the words | The brief asks for a game you can test and explain. You cannot explain a structure you did not design. |
| Put a real person, a classmate, or anybody's personal information in the game | It goes in a public repository and in front of other people's kids. |
| Make a game that cannot be finished in about ten minutes by someone who knows the route | The client's laptops are shared. A game has to end. |

**On AI:** this is Gate 3. You may use a model for ideas, room descriptions, or debugging, and every use goes in `AI-usage-log.md`: the prompt,
the response, what you changed, and why. No personal information goes into any prompt. You must be able to explain every line in your file.

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 7 Mon, first 10 minutes of Build 2 | Setting, goal, how you win, and how you lose, in four sentences |
| **Measure** | Week 7 Mon, Build 2 | Room map and IPO chart with State |
| **Analyze** | Week 7 Mon, end of Build 2 | Flowchart and pseudocode **committed and pushed**. No `adventure.py` yet. If you run out of time, finish before you write any code on Tuesday |
| **Improve** | Week 7 Tue to Week 8 Mon | Build it. One daily goal per block, a commit at the end of every block, a classmate playtest Friday |
| **Control** | Week 8 Mon to Week 8 Tue | Test scripts passing, README complete, known limitations observed |

You practiced all four models on the class world, Storm Relay, on Wednesday of Week 6. Monday you do the same four for **your** world, and you
already know how.

**Agile lives inside Improve.** Each Build 2 starts with one sentence in your decision log: today's goal. It ends with a commit and one sentence: what
got done and what did not. That is a sprint, one day long.

**Analyze is the phase students skip and it is the one that saves them.** The most common v1 failure is a game with a room nobody can reach or a lose state
that never fires. Both are visible on a flowchart in ten minutes.

---

## Milestone schedule, against actual class days

| Day | Build 2 goal |
|---|---|
| Week 6 Wed | Modeling practice on Storm Relay. This brief is handed out. Start thinking about your setting. |
| Week 6 Thu | `while` loops, and a Storm Relay loop skeleton. Start narrowing down your setting. |
| Week 6 Fri | No new content. Gate 2 in Build 1. Pick your setting before Monday, and catch up on anything from this week. |
| Week 7 Mon | Define, Measure, Analyze for **your** game: four sentences, room map, IPO chart, flowchart, pseudocode. Committed and pushed. **No code.** |
| Week 7 Tue | First code, after the game loop lesson. Constants, state variables, intro, a `while playing` loop that shows every room, movement for every exit, your win state, and the report after the loop. |
| Week 7 Wed | Input handling. Empty, unknown, capitals, blocked moves, `help`, and a validation loop for any number the game asks for. |
| Week 7 Thu | Lose states, the extra state variable, and a `for` loop doing real work. |
| Week 7 Fri | Playtest swap. A classmate plays your game with no help from you and writes down every place they got stuck or it broke. |
| Week 8 Mon | Test scripts for every ending. Fix what the playtest found. README draft. |
| Week 8 Tue | README complete, known limitations, final commit and push **by the end of the block. Due.** |
| Week 8 Fri | Demos. |

**Congressional App Challenge teams:** the CAC deadline usually falls in Week 8. Your instructor will confirm this year's date and time from the official
site. Your v1 is still due Tuesday of Week 8. Talk to your instructor during Week 7, not on the deadline day.

---

## Three worked scope examples

These are here so you can calibrate. **Do not build any of these three.** They are occupied.

### Too small

> **Hallway.** Two rooms. You start in one, type `north`, and you win.

One room short of the minimum, no lose state, nothing to remember, no decisions. It is a `while` loop around one `if`. It meets almost none
of the technical requirements and nobody would play it twice.

### About right

> **Last Bus Home.** You fell asleep on a city bus and woke up at the end of the line after dark, with 15 minutes until the last bus back.
> Five locations: the empty bus, the depot, a closed diner, a vending machine alcove, and the ticket booth. You need a transfer ticket from
> the booth, and the booth attendant will not sell one without exact change, which you get by buying a drink at the vending machine. The
> vending machine asks for a two-digit item code, validated in a loop. Lose if the 15 minutes run out, or if you leave the depot fence and
> get lost. The route home announces each of the stops with a `for` loop when you win.

Five rooms, two lose states, two items that change what is possible, one validated number, a real `for` loop, and a win that needs four of
the five rooms. Ten minutes to finish if you know the route. A spooky version of the same shape, a lighthouse during a storm or a museum after
closing, is exactly as good.

### Too big

> **The Academy.** Twenty rooms across three floors, twelve collectable items with an inventory screen, characters you can talk to with dialogue
> choices, a save and load system, and a random map every game.

An inventory of twelve items needs lists, which is Unit 5. Save and load is file writing, also Unit 5. Dialogue choices with many characters turn into
hundreds of `elif` branches without functions and data structures. Random maps need modules you have not been taught. **Every one of those is a real
feature of a later version of this same project.** Write them in your README under a heading called `Later versions`, and build the four-room core now.

**The calibration question:** can you draw your whole flowchart on one sheet of paper and your whole room map on half of another? If not, it is too big
for v1.

---

## The five-minute demo

Week 8, Friday. Some of you present, everybody submits.

1. **The game, in two sentences.** Setting and goal. (20 seconds)
2. **Show your flowchart and one line of your commit history** proving it came before the code. (40 seconds)
3. **Run the win script live,** then one lose script. (90 seconds)
4. **Type something ridiculous at your game,** chosen by the audience. It must not crash. (30 seconds)
5. **One decision you made and why.** A room you cut, a lose state you changed after the playtest, a `for` versus `while` choice. (90 seconds)
6. **Questions.** Your instructor will point at one line of your code and ask what it does. (30 seconds)

**Item 5 is the graded part** of Demonstration. **Item 6 is the course standard:** the only way to fail outright is to submit work you cannot explain.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Runs clean. At least 4 rooms, a flag-controlled game loop, every win and lose state reachable and reported correctly. Nothing typed crashes it. Every test script reaches its ending. |
| **Code Quality** | 20 | Constants for rooms and numbers. State variables named for what they hold. Comments explain why. A real `for` loop. Blocked moves cost nothing. Unit 3 tools only. |
| **Documentation** | 20 | IPO chart, flowchart, pseudocode, and room map complete and matching the game. Six README sections, with the algorithm paragraph in your own words and limitations actually observed. AI usage log complete. |
| **Process** | 15 | Design committed before `adventure.py`. DMAIC checkpoints on time. A commit at the end of every Build 2. Daily goal and result lines in the decision log. Playtest notes acted on. |
| **Demonstration** | 10 | Runs the scripts live, survives the audience's input, explains a real decision and any line pointed at. |
| **Polish** | 10 | A stranger can start playing without asking a question. Clear room descriptions and exits. Messages that tell the player what to do next. |

**The fastest way to lose Process points** is a history where `adventure.py` and `design/flowchart.png` arrive in the same commit, or the flowchart arrives
after the code. **The fastest way to lose Functionality points** is a win script that has never been run.

---

## If you are stuck

**"I cannot think of a setting."** Look at your Problem Inventory for a place you spend too much time waiting. Waiting rooms make good games, because the
player wants out.

**"My game is too simple."** Read the "about right" example again and count: rooms, lose states, items, one validated number, one `for` loop. Add a lose
state before you add a room. A second way to lose makes a game more interesting than a fifth room does.

**"My test script ends with `EOFError: EOF when reading a line`."** The script ran out of commands while the game was still waiting for one. Your game did
not crash on its own. Play the script by hand against your map and find where the player is when it runs out.

**"In PowerShell, my script's first command is not a command."** Windows PowerShell can add an invisible character to the start of piped input. Use
`cmd /c "python adventure.py < test-scripts\win.txt"` instead, or run it from Git Bash.

**"I want to use a function."** Not in v1. Write it in your README under `Later versions`, and build it in two weeks when version 2 asks you to.
