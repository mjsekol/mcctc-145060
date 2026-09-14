# Keep Asking Until It Makes Sense
---
## Slide 1: Somebody will type loud
- Your game asks for a frequency
- A player types loud
- Another types 2000
- Another presses Enter on nothing
- Right now your program crashes or shrugs
Speaker notes: Players type anything. Your job is not to hope they type the right thing. Your job is to keep asking until the answer is usable, and to tell them what went wrong each time. Every form, every kiosk, and every game you have ever used does this. Today you get the two keywords that make it clean, break and continue, and the loop that uses them.
Image: A game prompt with three bad answers stacked beneath it, flat navy and accent blue.
---
## Slide 2: Two words that change a loop from inside
- break ends the loop right now
- The program continues after the loop
- continue ends this pass right now
- The program goes back to the top for the next pass
- Both apply to the loop they are directly inside
Speaker notes: Break means we are done with this loop. Jump to the first line after it. Continue means we are done with this pass. Go back to the top and start the next one. Remember the last bullet. It sounds like a detail today and it becomes the whole point tomorrow, when loops go inside loops.
Image: Two loop diagrams, one with an arrow leaving the loop and one with an arrow jumping back to the top.
---
## Slide 3: The validation loop pattern
```python
MAX_TICKETS = 8

while True:
    tickets_text = input(f"How many tickets, 1 to {MAX_TICKETS}? ").strip()
    if not tickets_text.isdecimal():
        print("Type a whole number, like 2.")
    elif int(tickets_text) < 1 or int(tickets_text) > MAX_TICKETS:
        print(f"You can buy between 1 and {MAX_TICKETS} tickets.")
    else:
        break

tickets = int(tickets_text)
print(f"Ordering {tickets} tickets at $12 each: ${tickets * 12}")
```
Speaker notes: While True has no condition that ever turns False on its own, so the only way out is the break, and the only way to reach the break is an answer that passed every check. Order matters. isdecimal is checked before int ever touches the text. If int ran first on the word two, the program would crash and never get to ask again. Check that it can convert, then convert.
Image: None. This slide is code.
---
## Slide 4: Guards with continue
```python
while True:
    frequency_text = input("Frequency in kHz: ").strip()
    if not frequency_text.isdecimal():
        print("The dial takes whole numbers only, like 880.")
        continue
    frequency = int(frequency_text)
    if frequency < LOWEST_FREQUENCY or frequency > HIGHEST_FREQUENCY:
        print(f"The dial only runs from {LOWEST_FREQUENCY} to {HIGHEST_FREQUENCY} kHz.")
        continue
    break
```
```
Frequency in kHz: loud
The dial takes whole numbers only, like 880.
Frequency in kHz: 2000
The dial only runs from 530 to 1700 kHz.
Frequency in kHz: 1470
```
Speaker notes: When there are several checks, continue keeps them flat. Read it as a gate with two guards. Each guard either sends the input back to the top, or lets it through. The break at the bottom is only reachable by input that got past both guards. This is the Storm Relay frequency dial.
Image: None. This slide is code.
---
## Slide 5: break as a search, continue as a skip
- Save $45 a week for $140 shoes: break on enough
- Nobody knows the week in advance, so while True
- Rest on day 4 of a 7-day plan: continue
- In a while, update the counter BEFORE continue
- Otherwise the skipped pass skips the update, forever
Speaker notes: Break is also how a loop stops the moment it has an answer. Forty five, ninety, one thirty five are short, one eighty is enough, so week four. Continue skips one pass, like a rest day. But there is a trap in a while loop. A for gets its next value from range automatically. A while only moves on if the update line runs. Put the update below a continue, and on the skipped day the counter never changes, and the program hangs with no error.
Image: A savings bar filling in four steps, with the fourth step crossing a price line.
---
## Slide 6: Watch this: play again
```python
answer = input("Play again? (yes/no) ").strip().lower()
while not answer == "yes" or not answer == "no":
    print("Please type yes or no.")
    answer = input("Play again? (yes/no) ").strip().lower()
print(f"You chose {answer}.")
```
Speaker notes: Here is a validation loop written with a condition instead of break. Keep asking while the answer is not yes or not no. That sentence sounds perfect. In the lecture notes this line uses the not equals operator, which does exactly the same thing. I am going to type maybe, and then yes. Predict what happens when I type yes.
Image: None. This slide is code.
---
## Slide 7: The wrong way: nothing gets through
```
Play again? (yes/no) maybe
Please type yes or no.
Play again? (yes/no) yes
Please type yes or no.
Play again? (yes/no) no
Please type yes or no.
Play again? (yes/no)
```
Speaker notes: It refuses yes. It refuses no. It refuses everything, forever, and there is no error. Ctrl C to get out. The dangerous bugs are the ones that do not crash, and this one also does not stop. And notice how you would miss it. Most people test validation by typing garbage. The test that catches this is typing a valid answer.
Image: None. This slide is code.
---
## Slide 8: The truth table says why
- yes: not yes is False, not no is True. or gives True
- no: not yes is True, not no is False. or gives True
- maybe: both True. or gives True
- The condition is True for every possible word
- Fix: change or to and
Speaker notes: Build the truth table, the way you did in Unit 2. Any single word is always different from at least one of yes and no. So the or is True for every input, and the loop can never end. In English, not yes or no means neither. Neither is and. This is De Morgan's law showing up somewhere that getting it wrong freezes a program.
Image: A three-row truth table with the or column highlighted True in every row.
---
## Slide 9: break or a flag
- break: the exit sits exactly where the decision is
- A flag: the while line says how the loop ends
- One exit reads more clearly than three breaks
- Short validation loops in this course: break
- Game loops in this course: a playing flag
Speaker notes: Reasonable programmers disagree about this, and both sides have a point. Break puts the exit right at the decision and needs no extra variable. A flag puts the ending in the while line, where a reader looks first, and gives you one exit. Our rule for this course. Short validation loops use break. Game loops use a flag, because a game loop is long, has several endings, and has to report which one happened.
Image: Two short loops side by side, one ending with break, one with a flag.
---
## Slide 10: What you are about to build
- Build 1: Lab U03-02 Locked Out, Part 2
- The lockbox keypad: 4 digits, cancel, 3 tries
- A badly typed code never counts as a guess
- Build 2: v1 input handling for every command
- Empty, unknown, and shouting commands all get a message
Speaker notes: Build one finishes Locked Out. You add a keypad validation loop that accepts exactly four digits or the word cancel, and a wrong but well formed code costs one of three tries. A typo like one two does not cost a try. Build two is your own game. Every possible thing a player types must get a sensible response, including an empty line, a word that is not a command, and a command in capitals. Test with a valid answer, not only garbage.
Image: A keypad with four digit slots and a cancel key, navy and accent blue.
---
