# Project: Text Adventure v4
## 145060 Programming · Unit 7 · Objects and a Local Narrator

**Mode:** solo, building on your own version 3. **Gate:** 3, full tooling.
**Periods:** across Weeks 15 and 16, with milestones on real class days below.

**Competencies:** 5.3.12 (classes, objects, methods), 5.5.4 (call other programs),
5.5.7 (read inputs from an API), 9.3.3 (input validation), 2.1.1 (CIA in your design).

---

## The brief

Read this as though a person said it to you, because a person did.

> Your text adventure works. I have played it. The rooms always read the same, though,
> and after two runs I have them memorized. I want the rooms to feel alive, described a
> little differently each time, without you writing a hundred descriptions by hand. I
> heard we have a language model running on the lab machines. Use it to narrate the
> rooms. But it cannot break the game. If the model is slow, or down, or says something
> that leaves out the clue I need to win, the game still has to be playable and winnable.
> I should never be stuck because the narrator got creative.

**That is the whole brief.** Notice what it demands: the model improves the game when it
works, and never breaks it when it does not. Both halves are the assignment.

## Where the project comes from

**Your own version 3, from Unit 5.** You are not starting over. You are reorganizing your
v3 into classes and adding a narrator. Same world, same rooms, same win condition. If your
v3 is incomplete, finish it first; a narrator on a broken game is a broken game.

---

## Requirements

### Technical

1. **Three classes.** A `Room` class, a `Player` class, and a `Game` class. The room knows
   its own description and exits. The player knows where it is and what it carries. The
   game holds the rooms and the player and runs the rules.
2. **`Game.handle(line)` returns text and never calls `input` or `print`.** All input and
   output stay in a small `adventure.py` that connects the game to the keyboard. This is
   what lets Unit 8 put the same game behind a web page.
3. **A local model narrates rooms** through an Ollama-compatible `/api/generate` endpoint,
   with a timeout, using only the standard library.
4. **The reply is checked before it is used:** valid JSON, `done` is `True`, a non-empty
   string response, under a length cap. Any failure falls back to the stored description.
5. **Facts that must survive are kept.** A room that carries a clue you need to win, like
   the emergency frequency, rejects a narration that dropped it.
6. **No credentials anywhere.** A local model needs none.
7. **Player input that reaches a prompt is validated:** capped in length and limited in
   characters before it is used, echoed, or sent.
8. **A bundled stub model server** so the game runs and can be tested with no real model.
9. **A test suite** that runs without a real model or the internet.

### Repository

```
text-adventure/v4/
  adventure.py          connects the game to the keyboard, no game logic
  game.py               Room, Player, Game, and the rules
  local_model.py        the model client, with the reply checks
  stub_model_server.py  a stand-in model server for running and testing
  world.json            the world data, your v3 world plus keep lists
  test_adventure.py     the test suite
  README.md
```

### README, four sections

1. **What it is and how to run it**, with and without the stub.
2. **How the narrator decides what you see**, the cache, the checks, the fallback.
3. **A real run** against the stub, showing a narrated room.
4. **What is untrusted and how you handle it**, both your input and the model's reply.

---

## Constraints, and why each exists

| You may not | Why |
|---|---|
| Use any package outside the standard library | The lab machines have only the standard library, and a model needs no package to reach over HTTP. |
| Put an API key anywhere | A local model needs none, and a committed key is a public key. |
| Let the model change exits, items, or rules | The model narrates only. A model that could open a door could break the game. |
| Let `Game.handle` call `input` or `print` | Unit 8 puts this class behind a web page. Input and output belong in `adventure.py`. |
| Ship a game that needs a live model to be winnable | The brief requires it plays and wins with no model. The stored descriptions must be enough. |

---

## DMAIC checkpoints

| Phase | Due | What you hand in |
|---|---|---|
| **Define** | Week 15 Tue, end of Build 2 | One sentence on what the narrator adds, and the one rule it must never break |
| **Measure** | Week 15 Wed, end of Build 2 | A list of every room, and for each, the clue (if any) that must survive narration |
| **Analyze** | Week 15 Thu, end of Build 2 | On paper: the three classes and what each knows and does, drawn from your v3 |
| **Improve** | Week 15 Thu to Week 16 Wed | Build it: classes first, then the model client, then the checks |
| **Control** | Week 16 Wed, end of Build 2 | Tests pass, README complete, three runs recorded: success, fallback, rejected reply |

**Analyze is the one students skip and the one that saves them.** Draw the three classes
before you write them. Half the projects that go wrong go wrong because the student started
typing `Game` before deciding what `Room` and `Player` each own.

---

## Milestone schedule, against actual class days

| Day | Goal |
|---|---|
| Week 15 Thu | v3 reorganized into `Room`, `Player`, `Game`. Same game, now in classes. Tests pass. |
| Week 15 Fri | Optional flex: start `local_model.py` skeleton |
| Week 16 Mon | Model client sends a request and reads a reply |
| Week 16 Tue | The reply checks and the fallback |
| Week 16 Wed | Keep-phrases, input validation on `examine`, README, three recorded runs |

---

## Three worked scope examples

These calibrate you. Do not build any of these three; they are occupied.

### Too small
> Keep v3 exactly as it is, and print "the model would narrate here" instead of calling
> one.

No classes, no real model call, no checks. It meets none of the technical requirements and
does not do what the brief asked.

### About right
> The three classes, a working narrator on the stub, the four reply checks, a fallback to
> the stored description, one keep-phrase (the frequency) enforced, and `examine` capped
> and filtered. Plays and wins with no model. Tests pass.

Every technical requirement, at a size one person can finish and explain. This is the bar.

### Too big
> Add a second model that scores your choices, a save format that stores narrations,
> streaming replies, and a settings menu.

Streaming and a second model are beyond the unit, and a settings menu is polish that is not
the assignment. This is a good Unit 8 or personal-project idea. It is too big for now.

**The calibration question:** can you explain, in three sentences, what happens when the
model is down? If not, your fallback is not designed yet, and that is the heart of the
project.

---

## The five-minute demo

1. **What it does, in one sentence.** The narrator, and the one rule it never breaks. (30s)
2. **Run it with the stub.** Show a narrated room. (60s)
3. **Break the model on purpose.** Slow mode or no server. Show the game fall back and
   still play. (90s)
4. **One decision you made and why.** A check, the cache, the keep-phrase, the input cap.
   (90s)
5. **Questions.** (30s)

**Item 3 is the graded part.** Anybody can show a working narrator. Showing it fail safely
is the evidence you understood the brief.

---

## Grading, standard 100-point project rubric

| Dimension | Points | What earns it |
|---|---|---|
| **Functionality** | 25 | Three classes. Narrator works on the stub. Plays and wins with no model. Reply checks and fallback all work. |
| **Code Quality** | 20 | `Game.handle` does no I/O. Attributes in `__init__`. Readable names. No credentials. Comments explain why. |
| **Documentation** | 20 | Four README sections. The narrator logic explained. Three runs recorded. |
| **Process** | 15 | DMAIC checkpoints on time. Commits spread across days, not one lump. |
| **Demonstration** | 10 | Can explain any line. Shows the model failing safely. |
| **Polish** | 10 | The game reads well. The fallback note is clear. Narration is a real improvement when the model works. |

**The fastest way to lose Functionality points** is a game that needs the model to be
winnable. Test it with no model before you call it done.

---

## If you are stuck

**"I do not know what goes in which class."** Room knows its description, exits, and items.
Player knows its location, inventory, and moves. Game holds both and runs the rules. If a
piece of data changes as you play and belongs to one thing, it is that thing's attribute.

**"My narrator works but the game breaks when the model is down."** That is the whole
project, and you are halfway. Every model call must fall back to the stored description on
any failure. Wrap it and return the stored text when anything goes wrong.

**"The model keeps dropping the frequency."** That is the keep-phrase check doing its job.
The room shows the stored description when the reply drops a clue. That is correct
behaviour, not a bug.

**"I want to add more."** Write it in the README under "What I would add next" and build it
in a personal project. The brief is specific. Meet it first.

---

## The reference implementation

A complete, verified v4 is documented in
`09-project/reference-implementation/text-adventure-v4/README.md`, which points at the
canonical anchor build. Do not copy the anchor code. Build your own from your own v3. The
reference is there so the instructor can compare behaviour, not so you can transcribe it.
