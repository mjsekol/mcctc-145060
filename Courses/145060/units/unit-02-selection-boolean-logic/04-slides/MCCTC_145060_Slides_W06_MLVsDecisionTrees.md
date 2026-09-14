# Who Wrote the Rules
---
## Slide 1: Your music app never asked you a question
- Your Decision Engine asks questions you chose
- A music app guesses what you want next
- Nobody wrote an if statement about your taste
- So where did its rules come from
Speaker notes: For two weeks you have written decisions. Every question your Decision Engine asks, you chose. Every cutoff, you typed. Now think about the app that picks your next song. Nobody at that company wrote an if statement about you. Today is not about which one is smarter. It is about a mechanism you can check. Where do the rules come from, and what happens when they are wrong.
Image: A phone music player next to a hand-drawn decision tree on paper, flat navy and accent blue.
---
## Slide 2: A tree a person wrote
```python
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
Speaker notes: This is the kind of program you have been writing. Why is the cutoff 120? Because I picked 120. If I am wrong about what makes a workout song, the program is wrong in exactly the same way every time, and you can point at the line. A loud slow rock song at 100 beats per minute with energy 9 goes to Chill, because my rule said so.
Image: None. This slide is code.
---
## Slide 3: Machine learning flips who writes the rules
- Collect examples with known answers: labeled data
- A training process adjusts the model to match
- The rules are an output, not something typed
- A decision tree can also be learned this way
Speaker notes: In machine learning, a person does not write the rules. Somebody collects songs a listener already labeled workout or chill. A training process adjusts the model until its answers match those labels as often as it can. Here is the honest complication. A training process can build a decision tree too. So the difference is not the shape. The difference is who chose the questions and the cutoffs, a person or a process working from examples.
Image: A pile of labeled song cards flowing into a box marked training, and a finished model coming out.
---
## Slide 4: One artificial neuron
```python
score = tempo * tempo_weight + energy * energy_weight

if score >= threshold:
    playlist = "Workout"
else:
    playlist = "Chill"
```
```
Tempo in beats per minute: 128
Energy, 1 to 10: 7
Score: 7.80
Playlist: Chill
```
Speaker notes: A neural network has no questions in it at all. It is made of small units like this one. Multiply each input by a weight, add them up, compare to a threshold. Tempo weight is 0.05, energy weight is 0.2, threshold is 8. There is no rule about 120 beats per minute anywhere. This neuron is untrained, which is why it put a fast energetic song in Chill.
Image: None. This slide is code.
---
## Slide 5: Where the knowledge lives
- No readable rule about tempo
- Inputs are blended into one score
- The weights mean nothing to a person
- Real networks: many units, many weights
- That is why they are hard to explain
Speaker notes: Look at what is missing. There is no line that says fast songs are workout songs. The inputs are blended, so a calm fast song and a wild slow song can land on the same score. And the weights are not meaningful to a person. A real neural network has many of these units in layers. The reason for any single answer is spread across all of those numbers at once, which is exactly why it is hard to say why it decided anything.
Image: A small diagram of two inputs feeding one unit through two weighted lines, and a larger faded network behind it.
---
## Slide 6: One training step
```python
error = label - prediction

tempo_weight = tempo_weight + learning_rate * error * tempo
energy_weight = energy_weight + learning_rate * error * energy
```
```
Before: score 6.80, prediction 0, label 1
New weights: tempo 0.1000, energy 0.2045
After: score 11.84
Slow quiet song now scores 7.41 against threshold 8.0
```
Speaker notes: Here is training, one step, by hand. The loud slow song was labeled workout, which we write as 1. The neuron said 0. The error is 1. Nudge each weight a little in the direction that would have helped. Now that song scores above 8 and becomes workout, and the slow quiet song we already had right is still under 8. Nobody typed a rule. Two numbers moved. Real training repeats this over many examples, which needs loops, and loops are Thursday.
Image: None. This slide is code.
---
## Slide 7: The wrong way, and no error
```
learning_rate = 0.001

Before: score 6.80, prediction 0, label 1
New weights: tempo 0.1500, energy 0.2090
After: score 16.88
Slow quiet song now scores 10.92 against threshold 8.0
```
Speaker notes: I changed one number, the learning rate, from 0.0005 to 0.001. No error. The slow quiet song is now a workout song. The step was too big, so the neuron fixed the example it was shown and broke one it already had right. Tenth time you have seen a program run cleanly and be wrong. And this time there is no line to point at. The only way to catch it is to test the model on examples it was never trained on.
Image: None. This slide is code.
---
## Slide 8: Learned does not mean right
- A model learns what is in the examples
- One labeler's taste becomes the model's taste
- Unfair patterns in data become patterns in the model
- That is potential bias from your AI rubric
Speaker notes: Training sounds objective. The computer figured it out from the data. But a model can only learn what the examples contain. If one person with unusual taste labeled every song, the model learned that person. If the examples left out a whole kind of music, the model has never met it. You used the AI evaluation rubric in Week 2. Potential bias is exactly this, and now you know the mechanism behind it.
Image: A funnel of example cards that are all one color producing a model that only recognizes that color.
---
## Slide 9: When to write rules, when to learn them
- Write rules: decisions must be explained and audited
- Write rules: you have no labeled examples
- Learn: nobody can write the rule down
- Learn: good labeled examples exist
Speaker notes: This is a real disagreement and both sides are strong. Hand-written rules can be read, explained to the person affected, and fixed on a specific line, and they need no data. Learned models can handle problems nobody can write rules for, like recognizing a face, and can be retrained when the world changes. Knowing which situation you are in is the skill. Your quiz today will not ask which is better. It will ask how they differ.
Image: A two-column comparison card with a pencil icon on one side and a stack of labeled examples on the other.
---
## Slide 10: What you are about to build
- Build 1: the Unit 2 quiz, 30 minutes
- Build 2: Decision Engine, final build and demos
- Add one README paragraph to your engine
- Explain why your engine is not machine learning
Speaker notes: Build 1 is the Unit 2 quiz. Build 2 is the last block for the Decision Engine. Finish, push, and demo in your circle. One addition to your README before you push. Write a paragraph called How this differs from machine learning. Say who chose your rules, what a training process would need instead, and one thing your engine can do that a trained model would struggle with. That paragraph is part of your Documentation score.
Image: A README file in an editor with a highlighted heading reading How this differs from machine learning.
---
