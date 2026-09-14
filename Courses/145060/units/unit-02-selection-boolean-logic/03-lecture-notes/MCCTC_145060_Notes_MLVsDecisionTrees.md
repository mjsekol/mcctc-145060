# Lecture Notes: How Machine Learning Differs from a Decision Tree You Write
## 145060 Programming · Unit 2 · Week 6 · Tuesday, October 13

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W06_MLVsDecisionTrees.md) ·
[deck](../04-slides/exports/MCCTC_145060_Slides_W06_MLVsDecisionTrees.pptx)

If you missed class, you can learn this concept from this file alone. There is less code in
this file than in any other Unit 2 note, and more thinking. Run the three programs anyway,
because the numbers are the argument.

**A note on honesty before you start.** Machine learning is surrounded by hype, in both
directions. Some people describe it as magic. Some describe it as fancy autocomplete that
understands nothing. This file does not make claims about how smart any real product is, and
it does not quote statistics. It explains the **mechanism**, which is the part you can check.

---

## Why this exists

For two weeks you have written decisions. Your Decision Engine project sorts input into
categories with nested `if` statements that **you** chose.

Plenty of software makes the same kind of decision without anybody writing the rules. A photo
app sorts pictures by who is in them. An email service guesses which messages are spam. A music
app guesses what you want to hear next. Those are usually described as machine learning.

The WebXam for your senior AI course asks you to **describe how machine learning and neural
networks operate differently than standard decision trees.** You can answer that today, because
you now know exactly what a decision tree is. You have been writing them.

---

## The concept in plain language

### A decision tree you write

A person chooses **which questions to ask, in what order, and where every cutoff goes.** The
program follows those choices exactly.

```python
# A decision tree a person wrote by hand.
tempo = int(input("Tempo in beats per minute: "))
energy = int(input("Energy, 1 to 10: "))

if tempo >= 120:
    if energy >= 6:
        playlist = "Workout"
    else:
        playlist = "Chill"
else:
    playlist = "Chill"

print("Playlist:", playlist)
```

```
Tempo in beats per minute: 128
Energy, 1 to 10: 7
Playlist: Workout
```

```
Tempo in beats per minute: 100
Energy, 1 to 10: 9
Playlist: Chill
```

Why did 120 become the cutoff? Because the person who wrote it picked 120. If that person is
wrong about what makes a workout song, the program is wrong in exactly the same way, every time,
and you can point at the line.

### Machine learning

The person does **not** write the rules. Instead:

1. Somebody collects **examples** where the right answer is already known. Songs, each one
   labeled Workout or Chill by a listener. The labels are called **labeled data**.
2. A **training** program adjusts the model so its answers match the labels as often as it can.
3. The adjusted model is then used on new songs nobody labeled.

**The rules are an output of training, not something a person typed.**

### The honest complication

A decision tree can **also** be built by machine learning. A training program can look at labeled
examples and choose the questions and the cutoffs itself. So "decision tree" and "machine learning"
are not opposites.

The real difference the WebXam is asking about is this:

| | A decision tree you write | Machine learning |
|---|---|---|
| **Who chooses the rules** | A person | A training process, from examples |
| **What it needs** | Somebody who understands the problem | Many labeled examples |
| **Can you read why it decided** | Yes, line by line | Sometimes for a learned tree; rarely for a neural network |
| **When it is wrong** | The person's rule was wrong | The examples, or the training, led somewhere wrong |
| **A case nobody thought of** | Falls to whatever branch catches it | Gets a guess based on similar examples |

### A neural network

A neural network is a kind of model that contains **no questions at all.** It is made of many small
units. Each unit takes some numbers in, multiplies each one by a **weight**, adds them up, and passes
a result on to the next units. Training adjusts the weights.

The name comes from a loose resemblance to neurons in a brain. It is a resemblance, not a copy, and a
neural network is not a brain.

Here is **one** unit, the smallest possible piece:

```python
# One artificial neuron. No questions, no branches in the rule itself.
# It multiplies each input by a weight, adds them up, and compares to a threshold.
tempo = int(input("Tempo in beats per minute: "))
energy = int(input("Energy, 1 to 10: "))

tempo_weight = 0.05
energy_weight = 0.2
threshold = 8.0

score = tempo * tempo_weight + energy * energy_weight

if score >= threshold:
    playlist = "Workout"
else:
    playlist = "Chill"

print(f"Score: {score:.2f}")
print("Playlist:", playlist)
```

```
Tempo in beats per minute: 128
Energy, 1 to 10: 7
Score: 7.80
Playlist: Chill
```

Notice three things.

**There is no "if tempo is at least 120."** Tempo and energy are blended into one number. A very
energetic slow song and a calm fast song can land on the same score.

**The weights are not meaningful to a person.** Why 0.05 and not 0.06? No reason yet. These are
starting values, and this neuron has not been trained, which is why it put a 128 beats per minute
song in Chill.

**The one `if` at the end is not a rule about songs.** It turns a score into a label. The knowledge,
such as it is, lives in the weights.

A real neural network has many of these units in layers, and many weights. That is exactly why its
decisions are hard to explain: the "reason" for any one answer is spread across all of those numbers
at once.

---

## Worked example: one training step, by hand

Real training repeats a small adjustment over many examples, which needs loops. Thursday gives you
loops. Today you do **one** step by hand, so you can see every number move.

The example is a loud, slow song. The listener labeled it Workout, written as `1`. The untrained
neuron scores it 6.80 and says Chill, written as `0`. It is wrong.

```python
# One training step, done by hand so you can see every number.
# The example: a loud, slow song. The listener labeled it Workout (1).
tempo = 100
energy = 9
label = 1

tempo_weight = 0.05
energy_weight = 0.2
threshold = 8.0
learning_rate = 0.0005

score = tempo * tempo_weight + energy * energy_weight
if score >= threshold:
    prediction = 1
else:
    prediction = 0
print(f"Before: score {score:.2f}, prediction {prediction}, label {label}")

# The error is how wrong the prediction was: 1 means "should have said Workout".
error = label - prediction

# Nudge each weight in the direction that would have helped, in proportion to its input.
tempo_weight = tempo_weight + learning_rate * error * tempo
energy_weight = energy_weight + learning_rate * error * energy
print(f"New weights: tempo {tempo_weight:.4f}, energy {energy_weight:.4f}")

score = tempo * tempo_weight + energy * energy_weight
print(f"After: score {score:.2f}")

# Check a song the old weights already got right: slow and quiet, labeled Chill (0).
chill_score = 70 * tempo_weight + 2 * energy_weight
print(f"Slow quiet song now scores {chill_score:.2f} against threshold {threshold}")
```

```
Before: score 6.80, prediction 0, label 1
New weights: tempo 0.1000, energy 0.2045
After: score 11.84
Slow quiet song now scores 7.41 against threshold 8.0
```

The loud slow song now scores 11.84, above the threshold, so the neuron now says Workout. The slow
quiet song still scores under 8.0, so it is still Chill. **Nobody typed a new rule.** Two numbers
moved, and the behavior changed.

This update rule is one of the oldest and simplest ways to train a single unit, often taught as the
**perceptron** rule. Modern neural networks are trained with more sophisticated methods, but the core
idea is the same: measure how wrong the output was, and adjust the weights to be less wrong.

---

## The wrong version: a step that is too big

Change one number, the learning rate, from `0.0005` to `0.001`. Nothing else changes.

```
Before: score 6.80, prediction 0, label 1
New weights: tempo 0.1500, energy 0.2090
After: score 16.88
Slow quiet song now scores 10.92 against threshold 8.0
```

**No error. The slow quiet song is now a workout song.**

The neuron fixed the example it was shown and broke one it already had right. It moved too far. The
program ran perfectly and the model got worse.

This is the tenth time this course has shown you a result that runs cleanly and is wrong, and it is
the most important version yet, because **in machine learning, there is no line to point at.** In your
Decision Engine, a wrong answer traces back to a condition you wrote. Here, the wrong answer comes from
a number chosen during training, and the only way to find out it is wrong is to test the model on
examples it was not adjusted on.

That is why people who build machine learning systems keep some labeled examples aside and never train
on them. They are the test.

### The mistake that does crash

```python
tempo = int(input("Tempo in beats per minute: "))
energy = input("Energy, 1 to 10: ")

tempo_weight = 0.05
energy_weight = 0.2

score = tempo * tempo_weight + energy * energy_weight
```

Typing `128` and `7`:

```
    score = tempo * tempo_weight + energy * energy_weight
                                   ~~~~~~~^~~~~~~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'float'
```

Week 2's lesson, still true inside a neuron. `energy` was never converted, so it is the text `"7"`.
Python can repeat text a whole number of times, but not 0.2 times.

---

## Why "it learned it, so it must be right" is tempting

**Training sounds objective.** "The computer figured out the rule from data" sounds more trustworthy than
"a person guessed." But the model can only learn what is in the examples. If every example was labeled
by one person with unusual taste, the model learns that person's taste. If the examples leave out a whole
kind of song, the model has never seen it. **Patterns in the data, including unfair ones, become patterns
in the model.** This is what "potential bias" means on the AI evaluation rubric you used in Week 2.

**It works on the examples.** A model that matches its training examples can still be wrong on new input,
exactly like the too-big step above.

**Hand-written rules feel old-fashioned.** They are not worse by default. When a decision has to be
explained, defended, or audited, a rule a person can read is often the right choice. When the rules are too
complicated for anyone to write down, and good labeled examples exist, learning can be the right choice.
**Knowing which situation you are in is the skill.**

### Where people honestly disagree

**The case for hand-written rules:** you can read every decision, you can explain it to the person it
affected, you can fix a wrong rule on a specific line, and it needs no data at all.

**The case for learned models:** some problems, such as recognizing a face in a photo, have no rule anyone
can write down, and a model trained on good examples can handle them. A learned model can also be retrained
when the world changes, without somebody rewriting hundreds of conditions.

Both cases are real. The strongest programmers can argue either side for a specific problem.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Decision tree** | A structure where each answer decides which question comes next. Can be written by a person or learned from data. |
| **Machine learning** | Building a model by adjusting it to match examples, instead of writing its rules by hand. |
| **Labeled data** | Examples where the correct answer is already known. |
| **Training** | The process that adjusts a model to match labeled data. |
| **Model** | The thing that produces an answer: a set of rules, a learned tree, or a set of weights. |
| **Neural network** | A model made of many units that each weight and add their inputs, with the weights set by training. |
| **Weight** | A number that says how much one input counts. Adjusted during training. |
| **Threshold** | The score where the output flips from one label to the other. |
| **Learning rate** | How far each training step moves the weights. Too big breaks things that were right. |
| **Explainability** | How well a person can say why a model gave a particular answer. |
| **Bias (in data)** | A pattern in the examples, including an unfair one, that the model learns as if it were a rule. |

---

## Self-check

**Question 1.** In two sentences, describe how a machine learning model and a decision tree you wrote
yourself differ in **where the rules come from**. Do not use the word "smart."

**Question 2.** A classmate says, "Decision trees are old, and machine learning replaced them." Give one
fact that makes that statement wrong.

**Question 3.** A school wants a program that decides which students get a limited number of parking
passes. Give the strongest argument for writing the rules by hand instead of training a model, in two or
three sentences.

---

### Answers

**1.** In a decision tree you write, a person chooses every question, its order, and every cutoff, and the
program follows those choices. In machine learning, a training process adjusts the model, whether that is a
learned tree or a set of weights, until its answers match labeled examples, so the rules come out of the data
rather than out of a person's head.

**2.** Decision trees can themselves be built by machine learning, where a training program chooses the
questions and cutoffs from labeled examples. A hand-written tree also remains the sensible choice whenever a
decision must be readable line by line, which learning did not change. Either point is enough.

**3.** Full credit for any argument built on explainability, fairness, or data. A strong answer: every student
who is denied a pass deserves to know exactly why, and a hand-written rule can be read, explained, and
challenged line by line. A trained model would learn from past pass decisions, so any unfairness in who got
passes before would become part of the model, and nobody could point to the line that caused it.
