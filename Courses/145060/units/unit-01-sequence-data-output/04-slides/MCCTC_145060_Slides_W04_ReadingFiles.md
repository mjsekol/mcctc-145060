# Reading Data Out of a File
---
## Slide 1: You cannot type in three hundred members
- Every program so far asked a person
- That works for four values
- It does not work for a roster
- And the data vanishes when the program ends
Speaker notes: Look at everything you have built. Every value came from somebody typing. That is fine for a calculator with four questions. It is absurd for a club roster with three hundred members. And when the program ends, everything anyone typed is gone. Real data lives in files. Today your program learns to read one.
Image: A long printed roster list next to a single keyboard, with a crossed-out arrow between them.
---
## Slide 2: Three steps, always in this order
- Open the file and get a handle
- Read from the handle
- Close it
- The handle is not the contents
Speaker notes: Opening a file does not give you the words in it. It gives you a handle, which is an object that knows how to read the file. Then you ask the handle for the text. Then you close it, which gives the file back to the operating system. On a four line program forgetting to close does nothing you will notice. On a real system it causes problems that are miserable to track down.
Image: Three numbered boxes, open, read, close, connected left to right.
---
## Slide 3: read gives you everything as one string
```python
roster_file = open("roster.txt")
contents = roster_file.read()
roster_file.close()

print(len(contents))          # 102
print(repr(contents[0:40]))
```
```
'Ava Ruiz            ROBO-2026-114\nMarcus'
```
Speaker notes: read hands you the entire file as one big string. Look at the repr output. Right after the member code there is a backslash n. That is the line break, and it is an ordinary character sitting inside the string, the same as a letter. The file size of one hundred two is three lines of thirty three characters plus one newline each.
Image: None. This slide is code.
---
## Slide 4: readline gives you one line, with its newline
```python
roster_file = open("roster.txt")
first = roster_file.readline()
roster_file.close()

print(repr(first))
print(repr(first.strip()))
```
```
'Ava Ruiz            ROBO-2026-114\n'
'Ava Ruiz            ROBO-2026-114'
```
Speaker notes: readline gives you one line at a time, and look at the end of it. The newline is included. That is why strip follows readline almost everywhere you will ever see it. If you forget, the newline is invisible until it lands somewhere it should not, like the middle of a sentence or the end of a column.
Image: None. This slide is code.
---
## Slide 5: A fixed-width file is built for slicing
- Every line has the same layout
- Name in positions 0 to 19
- Code in positions 20 to 32
- Week 3 slicing reads it directly
Speaker notes: The roster file uses a format called fixed width. Every field starts at the same position on every line, and short names are padded with spaces to fill their field. Plenty of older systems still export data this way. And it means you can read it with nothing but the slicing you learned last week. Slice the name, strip the padding, slice the code.
Image: Three roster lines stacked with a column ruler above and vertical guides at positions 0, 20, and 33.
---
## Slide 6: Now I break it on purpose
```python
roster_file = open("rooster.txt")
```
```
FileNotFoundError: [Errno 2] No such file or directory: 'rooster.txt'
```
Speaker notes: One letter wrong and Python tells you exactly what happened and exactly which name it looked for. That one is friendly. The next one is not, and it is the one that costs students real hours. I am going to run this same program from a different folder, spelled correctly, with the file sitting right there in the sidebar.
Image: None. This slide is code.
---
## Slide 7: The file is right there and Python cannot find it
- The name is looked up from where you ran the program
- Not from where the program file lives
- The error message prints the path it tried
- Compare that path to where the file really is
Speaker notes: This is the one. You can see the file in the editor two inches from the error that says it does not exist. Everything in front of you says the file is present. The one thing that matters, which folder your terminal is sitting in, is not visible anywhere on screen. Read the path in the error. It tells you exactly where Python looked. That path is the answer.
Image: An editor sidebar showing roster.txt next to a terminal whose prompt shows a different folder.
---
## Slide 8: Reading past the end does not crash
```python
roster_file = open("roster.txt")
roster_file.readline()
roster_file.readline()
roster_file.readline()
extra = roster_file.readline()
roster_file.close()

print(repr(extra))             # ''
print(repr(extra[0:20]))       # ''
```
Speaker notes: The file has three lines and I asked for a fourth. No error. readline hands back an empty string at the end of a file, and every slice of an empty string is another empty string. Your report would print a blank member and keep going. That is the fourth time this course has shown you the bug that does not crash, and it will not be the last.
Image: None. This slide is code.
---
## Slide 9: What you are about to build
- Lab U1-03, the Roster Reader
- Read the file, report its size
- Slice each member apart, strip the padding
- Record what a fourth readline gives you
Speaker notes: Build one is the Roster Reader lab. Read the file and report its size, then read each line and pull out the name, the season year, and the member number by position. You will copy the same block three times, and I want you to notice how that feels, because that feeling is why loops exist. Step eight asks you to read a line that is not there and write down what happened. Build two is the CLI Toolsmith.
Image: A clean three-line aligned roster report in a terminal, navy and accent blue.
---
