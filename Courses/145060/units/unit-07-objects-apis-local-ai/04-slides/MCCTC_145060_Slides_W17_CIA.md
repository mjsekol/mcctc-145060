# Three Words for What Security Protects
---
## Slide 1: You fixed a pile of bugs, now name them
- You found leaks, fakes, and freezes
- What do all of those have in common
- Security protects three things
- They spell CIA
Speaker notes: You have found and fixed a pile of vulnerabilities. Leaks, fakes, and freezes. What do they have in common. Security protects three things about information, and the three spell CIA. Once you can name which one a problem breaks, you can talk about security clearly and answer the exam question.
Image: Three shields labeled C, I, A over a program.
---
## Slide 2: The three, one line each
- Confidentiality, who can read it
- Integrity, whether it is true
- Availability, whether it is there
- Every vulnerability breaks at least one
Speaker notes: Confidentiality is who can read it, broken when someone sees what they should not. Integrity is whether it is true, broken when data is changed or faked. Availability is whether it is there when you need it, broken when a system is down or frozen. Every vulnerability breaks at least one of these.
Image: Three columns, C, I, A, each with its one-line meaning.
---
## Slide 3: All three in one codebase
```
Confidentiality  The moderator code and a key sat in the file and the prompt.
Integrity        thank() accepted a negative number, so points could be pulled.
Availability     The model call had no timeout, so it froze the whole app.
```
Speaker notes: Take the security lab you finished. The moderator code in the file is confidentiality, anyone reading it could see it. The negative thank is integrity, the saved file said something false. The missing timeout is availability, a hung model froze the app for everyone. One codebase, all three letters.
Image: None. This slide is code.
---
## Slide 4: Your own projects protect all three
```
Confidentiality  No key anywhere. A local model needs none. A test enforces it.
Integrity        The keep-phrase check rejects a reply that dropped a needed fact.
Availability     Every call has a timeout; the game stops asking after two failures.
```
Speaker notes: The features you wrote were not only conveniences. No key means nothing to leak, that is confidentiality. The keep-phrase check means the game never shows a false, unwinnable room, that is integrity. The timeouts mean a dead server never freezes the program, that is availability. You were protecting CIA without naming it.
Image: None. This slide is code.
---
## Slide 5: Name the letter, fast
- A stolen password reads private messages
- A save file edited to add lives
- A site taken offline by an attack
- Which letter for each
Speaker notes: Practice the move. A stolen password that reads private messages is confidentiality. A save file edited to add lives is integrity. A site taken offline is availability. The test for each, did someone read what they should not, did the data become false, or is the thing not there when needed.
Image: Three scenarios, each with a blank waiting for C, I, or A.
---
## Slide 6: The trap, everything feels like integrity
- A leaked password feels serious
- So students call it integrity
- But nothing was changed
- Something was read, that is confidentiality
Speaker notes: Here is the common mistake. A leaked password feels serious, so people call it an integrity problem. But a leaked password did not change any data. It exposed it. Nothing became false, something became readable. That is confidentiality. Feeling bad is not a category.
Image: A password being read, not changed, tagged confidentiality.
---
## Slide 7: Why the right letter matters
- The fix depends on the letter
- Confidentiality, stop exposing it
- Integrity, stop it being changed
- Availability, keep it running
Speaker notes: Getting the letter right is not pedantry. It tells you what to fix. A confidentiality fix is stop exposing it. An integrity fix is stop it being changed. An availability fix is keep it running. Name the wrong letter and you reach for the wrong fix. Name the right one and the fix is obvious.
Image: Each letter paired with the kind of fix it points to.
---
## Slide 8: The same bug can matter a lot or a little
- A game frozen for a second, minor
- A gradebook made false, serious
- Depends on the letter and the program
- That judgment is the review
Speaker notes: The same vulnerability can matter a lot or a little depending on which letter it breaks and what the program is for. A game losing availability for a second is minor. A gradebook losing integrity is serious. That judgment, not only a list, is what a real security review produces.
Image: A dial from minor to serious, the same bug placed differently for two programs.
---
## Slide 9: CIA connects to the whole unit
- The API app protects availability with timeouts
- The model code protects integrity with checks
- The no-key rule protects confidentiality
- Three weeks, one idea
Speaker notes: CIA ties the whole unit together. The API app's timeouts protect availability. The model code's checks protect integrity. The no-key rule protects confidentiality. Objects, APIs, and security were not three separate topics. They were three angles on building something you can trust.
Image: The three unit topics converging on the three CIA letters.
---
## Slide 10: What you are about to build
- Map every lab defect to a CIA letter
- Write a one-line reason for each
- Then a timed 5.3 review set
- The heaviest outcome on the exam
Speaker notes: Build one completes the CIA column of your review template, every defect mapped to a letter with a one-line reason. Build two is a timed review set weighted to outcome 5.3, the heaviest on the WebXam, to start getting ready for the post-test. Name the letters, then sharpen the fundamentals.
Image: A completed review template beside a review question set, navy and accent blue.
