# Same Number, Three Ways to Write It
---
## Slide 1: Eight light switches
- Each switch is on or off
- How many arrangements can eight make
- Work it out, do not guess
- The answer explains half of computing
Speaker notes: Before we touch Python today, answer the bell ringer question out loud. Eight switches, each on or off. One switch gives two arrangements. Two give four. Each new switch doubles it. Eight switches give two hundred fifty six. That number is not arbitrary. It is a byte, and every limit you have ever seen that says 255 or 256 comes from counting switches. Today you learn to read the switches directly.
Image: A row of eight simple toggle switches, some up and some down, navy and accent blue.
---
## Slide 2: A written number is a value plus a base
- The value is the quantity
- The base is how many digits you get
- Decimal has ten. Binary has two
- 13 and 1101 are the same value
Speaker notes: This is the one idea for today. A number written on a page is two things at once: how much, and which counting system you used to write it down. Thirteen and one one zero one are not similar numbers. They are the same number. The way thirteen and trece are the same word in two languages. If you keep that straight, conversion stops being magic and becomes bookkeeping.
Image: The quantity thirteen shown as thirteen dots, with the labels 13 and 1101 both pointing at the same group.
---
## Slide 3: Place value in decimal, which you already know
```
    1      3
   10s    1s

 1 x 10  +  3 x 1  =  13
```
Speaker notes: You have done this since second grade without calling it anything. The one on the left is not worth one. It is in the tens place, so it is worth ten. Each place is worth ten times the place to its right. Binary uses exactly the same idea with one change, and that change is the whole lesson.
Image: None. This slide is code.
---
## Slide 4: Place value in binary
```
    1      1      0      1
    8s     4s     2s     1s

    8  +   4  +   0  +   1  =  13
```
Speaker notes: Same idea, but each place is worth two times the place to its right instead of ten. Ones, twos, fours, eights. Wherever there is a one, add that place's value. Wherever there is a zero, skip it. Eight plus four plus one is thirteen. That is the entire technique for binary to decimal and there is nothing else to it.
Image: None. This slide is code.
---
## Slide 5: Now I break it on purpose
- 1101 to decimal
- Add the digits: 1 + 1 + 0 + 1
- That gives 3
- Tell me why that is wrong
Speaker notes: I am going to do what somebody always does. Add up the digits. One plus one plus zero plus one is three. Somebody in here is already objecting. Good. Adding the digits throws away place value, which is the entire idea. The one on the far left is not worth one. It is sitting in the eights place. Three is not a rounding error. It is a completely different number.
Image: The digits 1101 with a large crossed-out plus sign between them, and the place values written underneath.
---
## Slide 6: Decimal to binary, biggest place first
```
42    fits in 32?  yes   remaining 10    digit 1
      fits in 16?  no                    digit 0
      fits in  8?  yes   remaining  2    digit 1
      fits in  4?  no                    digit 0
      fits in  2?  yes   remaining  0    digit 1
      fits in  1?  no                    digit 0

42 in binary is 101010
```
Speaker notes: Going the other way, start from the biggest power of two that fits. Thirty two fits in forty two, write a one, ten left over. Sixteen does not fit in ten, write a zero. Eight fits, write a one, two left. Four does not fit, zero. Two fits, one, nothing left. One does not fit, zero. Read the digits down the right side. One zero one zero one zero.
Image: None. This slide is code.
---
## Slide 7: Why hexadecimal exists
- Base 16: digits 0 to 9, then a to f
- Four binary digits are one hex digit
- Always, exactly
- 1111 1111 is ff, which is 255
Speaker notes: Binary is honest and unreadable. Nobody wants to read thirty two ones and zeros. Hex fixes that, because four binary digits always make exactly one hex digit, so you can translate in chunks. That is why colours on the web look like pound five seven A one E B. Three pairs of hex digits, each pair one byte, each byte a number from zero to two fifty five. That is our course colour, Launch Blue.
Image: A 16-row table of decimal, binary, and hex side by side, the rows 10 through 15 highlighted.
---
## Slide 8: Checking your hand work with Python
```python
print(bin(13))          # 0b1101
print(hex(13))          # 0xd
print(int("1101", 2))   # 13
print(int("d", 16))     # 13
print(f"{13:08b}")      # 00001101
```
Speaker notes: Python can do all of this in one call. Use these to check your work, not to replace it. The WebXam asks you to convert by hand, so the skill has to live in your head before it lives in a function. The zero b and zero x at the front are Python labelling which base it is showing you. They are not part of the number.
Image: None. This slide is code.
---
## Slide 9: What you are about to build
- Twelve conversions on paper, no computer
- Show the place values every time
- Then check all twelve with Python
- Count how many you got right
Speaker notes: Build one is paper and pencil. Four decimal to binary, four binary to decimal, four involving hex. Show the place value arithmetic every time, because the arithmetic is what I am grading, not the answer. Then open a terminal and check all twelve with bin and int. Count your matches. Build two opens the CLI Toolsmith project, and today is planning only, no code.
Image: A worksheet with place value columns and a terminal window beside it, navy and accent blue.
---
