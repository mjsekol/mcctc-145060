# Every Character Is a Number
---
## Slide 1: A computer cannot store the letter A
- It stores switches, on or off
- So how does it store your name
- Somebody made an agreement
- Today you read the agreement
Speaker notes: Yesterday we established that everything in the machine is switches. So here is the problem. Your name is letters. There is no switch position called A. So how does your name get stored at all? The answer is that a group of people agreed on a number for every character, and every computer follows that agreement. Today you learn to read it.
Image: The letter A beside a row of eight switches, with a question mark between them.
---
## Slide 2: A character is a number by agreement
- ASCII gave numbers to 128 characters
- Unicode extended it to almost every writing system
- A is 65 in both
- The agreement is the only reason text works
Speaker notes: ASCII was the first widely used agreement and it covered one hundred twenty eight characters, which was enough for English letters, digits, and punctuation. It was not enough for the rest of the world. Unicode extended the agreement to essentially every writing system, plus emoji. The first one hundred twenty eight Unicode numbers match ASCII exactly, so A is sixty five in both.
Image: A small ASCII table region beside a much larger Unicode grid, the overlap highlighted.
---
## Slide 3: Asking Python for the number
```python
print(ord("A"))    # 65
print(ord("a"))    # 97
print(ord("0"))    # 48
print(ord(" "))    # 32

print(chr(65))     # A
print(chr(97))     # a
```
Speaker notes: ord gives you the number for a character. chr gives you the character for a number. Notice the third line. The character zero is forty eight, not zero. The digit you type on the keyboard and the number zero are completely different values. You met this exact idea in week two with the string twelve and the number twelve.
Image: None. This slide is code.
---
## Slide 4: The alphabet is arithmetic
```python
print(ord("B"))            # 66
print(chr(ord("A") + 25))  # Z
print(ord("a") - ord("A")) # 32
```
Speaker notes: Because the alphabet is stored in order, letters are arithmetic. B is one more than A. Twenty five past A is Z. And look at the last line. Uppercase and lowercase are exactly thirty two apart, and thirty two is two to the fifth power, which is one single switch. The people who designed ASCII did that on purpose so a machine could change case by flipping one bit.
Image: None. This slide is code.
---
## Slide 5: Unicode goes much further
- An e with an accent is 233
- An emoji is a number too
- len counts characters, not bytes
- Some characters need more storage than others
Speaker notes: Unicode numbers go far past two fifty five. An e with an accent mark is two thirty three. A fire emoji is one hundred twenty eight thousand two hundred ninety three. And len still counts characters, so the word cafe with an accent is four characters long, the same as without one, even though storing the accented version takes more space. How much space is a question for later.
Image: A few characters with their code points underneath, including an accented letter and a simple emoji outline.
---
## Slide 6: Now it breaks, and it is not your fault
```python
print(chr(128293))
```
```
UnicodeEncodeError: 'charmap' codec can't encode character '\U0001f525' in position 0: character maps to <undefined>
```
Speaker notes: This is going to crash on most of these machines, and I want you to read the error slowly. Your program is correct. Nothing you wrote is wrong. The terminal is set to an older agreement that can only show two hundred fifty six characters, and the one you asked for is not among them. This is the first failure you have met that is not in your code at all.
Image: None. This slide is code.
---
## Slide 7: Checking what your terminal can show
```python
import sys
print(sys.stdout.encoding)    # cp1252
```
Speaker notes: This line tells you which agreement your terminal is using. On a default Windows terminal it says c p twelve fifty two, which is the older, smaller one. Set it to U T F eight and the same program prints the emoji fine. The fix is in the environment, not in the program. Learning to tell those two apart will save you hours for the rest of your career.
Image: None. This slide is code.
---
## Slide 8: Two kinds of broken
- My program is wrong: fix the code
- My environment cannot do what I asked
- The error message tells you which
- Changing correct code to dodge it makes it worse
Speaker notes: When something fails, ask this before you touch anything. Is my program wrong, or can my environment not do what my program asked? If you rewrite correct code to avoid an environment problem, you have now broken working code and the environment is still wrong. The words charmap and encode in that error are the clue that this is about the output destination, not your logic.
Image: A split panel, a code file on one side and a terminal settings icon on the other, with a divider between them.
---
## Slide 9: What you are about to build
- Print the code point of every character in your name
- Find one character your terminal cannot show
- Record the exact error message
- Explain the case gap as a power of two
Speaker notes: Build one is detective work on yourself. Get the number for every character in your own name. Then find a character this terminal cannot display, and copy the exact error into your notes. Then work out the gap between uppercase and lowercase and explain it in terms of binary. Build two is the CLI Toolsmith, where today you write the input section.
Image: A name broken into letters with a number under each, navy and accent blue.
---
