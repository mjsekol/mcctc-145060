# Cleaning Up What People Typed
---
## Slide 1: Three people, one name, three spellings
- ava ruiz
- AVA RUIZ
- (two spaces) Ava Ruiz (two spaces)
- Same person. Three different values
Speaker notes: Your club sign-in sheet has all three of these on it and they are the same human being. To you that is obvious. To a computer these are three completely unrelated strings that happen to share some letters. Today you learn the tools that fix that, and then you learn where those tools stop working, which is the more useful half.
Image: Three text fields with the same name typed three different ways, a question mark between them.
---
## Slide 2: A method is something a value does to itself
```python
raw = "  ava RUIZ  "

print(repr(raw.strip()))            # 'ava RUIZ'
print(repr(raw.strip().title()))    # 'Ava Ruiz'
print(raw)                          # '  ava RUIZ  '
```
Speaker notes: You call a method with a dot after the value. Strip removes whitespace from the two ends. Title capitalises the first letter of each word. And you can chain them, which is line two. Now look at line three, because that is the part that catches people.
Image: None. This slide is code.
---
## Slide 3: Methods hand back a copy
- raw is exactly what it always was
- strip did not change it
- It handed you a new string
- If you want to keep it, store it
Speaker notes: This is the single most common mistake of the day. You call dot strip, you print the variable, and the spaces are still there, and you conclude that strip is broken. Strip is not broken. Strip made you a clean copy and you threw it away. Nothing in Python changes a string in place, ever. You have to catch what comes back with a name and an equals sign.
Image: A box labelled raw unchanged, with an arrow producing a second separate box labelled clean.
---
## Slide 4: Why I keep wrapping things in repr
```python
print("  Ava  ".strip())          # Ava
print(repr("  Ava  ".strip()))    # 'Ava'
```
Speaker notes: The first line proves nothing at all. Trailing spaces are invisible on a terminal, so you cannot tell whether strip did anything or whether it did nothing. Repr shows you the quote marks so you can see exactly where the string starts and stops. Whenever whitespace is the thing you are checking, wrap it in repr or you are only trusting it.
Image: None. This slide is code.
---
## Slide 5: The ones worth knowing
- strip: whitespace off both ends
- title, upper, lower: capitalisation
- replace: swap one piece of text for another
- in: is this text inside that text, True or False
Speaker notes: Four tools and a fifth thing. The word in is not a method, it is an operator, and it hands you back True or False, which is the bool type from week two showing up for a reason. You will use in constantly starting in Unit Two when conditions arrive. For today it is enough to know it answers a yes or no question about text.
Image: A five-row reference card, navy headers, monospace method names.
---
## Slide 6: strip does not do what its name suggests
```python
print(repr("  Ava  Ruiz  ".strip()))
```
```
'Ava  Ruiz'
```
Speaker notes: Read the name of that method and then read the output. The two spaces in the middle are still there. Strip removes whitespace from the two ends and nothing else. An AI assistant told a student this week that strip removes all the spaces and gave an example output of Ava Ruiz jammed together. That was wrong, and one line in a terminal settles it in eight seconds.
Image: None. This slide is code.
---
## Slide 7: Now I break it on purpose
```python
code = "MCCTC"
print(code[5])
```
```
IndexError: string index out of range
```
Speaker notes: Yesterday I told you a slice never crashes. An index does. Position five does not exist in a five character string, because the positions are zero through four. This is the friendly failure. It stops immediately and tells you exactly where. Compare that with yesterday's year that quietly lost a digit and said nothing.
Image: None. This slide is code.
---
## Slide 8: Where these tools stop working
```python
print("mcdonald".title())        # Mcdonald
print("o'brien".title())         # O'Brien
print("van der berg".title())    # Van Der Berg
```
Speaker notes: The first one is wrong. The second one happens to be right, by luck. The third is wrong for almost everybody who has that name. There is no method that gets all of these right and there is not going to be one. Names are one of the genuinely hard problems in software, and people whose names break systems deal with this constantly, at the doctor, at the bank, on every form.
Image: None. This slide is code.
---
## Slide 9: The professional habit is not a better method
- No cleaning rule handles every name
- You will not find one. Stop looking
- Know where yours fails
- Write it down where the next person sees it
Speaker notes: Here is what a working developer actually does. Not find a perfect solution, because there is not one. They find out where their thing breaks, they write it down honestly in the documentation, and the next person is warned. That is why every lab this week asks you to name one input your program gets wrong. It is not busywork and it is not you admitting failure. It is the deliverable.
Image: A README section headed Known limitations with a specific entry written under it.
---
## Slide 10: What you are about to build
- A cleaner that handles spaces and capitals
- Prove it with repr, do not trust it
- Then lab U1-02, steps eleven through fourteen
- Step thirteen finds where your cleaner breaks
Speaker notes: Build one is the cleaner, tested on three specific messy inputs. Use repr at least once so you are checking rather than hoping. Then finish the lab. Step thirteen has you run your program on mcdonald, o brien, and van der berg, and record which one it mangles in your README under Known limitations. Do not fix it. Naming it is the grade.
Image: A terminal showing a messy name going in and a clean badge coming out, navy and accent blue.
---
