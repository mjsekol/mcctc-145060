# Judging What You Cannot Run
---
## Slide 1: Last week the computer was the referee
- A program runs or it does not
- The interpreter never argues with you
- Today the referee goes away
- Nothing crashes when prose is wrong
Speaker notes: Last week you learned to read error messages. That worked because Python is a referee. It either accepts your file or it does not, and it cannot be talked out of its answer. Today I am taking that away. When a model writes you a paragraph, an explanation, or a diagram, there is no traceback. Nothing turns red. A wrong answer and a right answer look exactly the same on the screen, and both of them sound sure.
Image: A split panel. Left, a terminal with a red error. Right, a clean page of prose with no marks on it at all.
---
## Slide 2: Fluent is not the same as correct
- The tone is generated the same way the content is
- Confidence carries no information about accuracy
- You have been told it "makes mistakes"
- The real failure mode is worse than that
Speaker notes: Here is the thing people get wrong. You have been told AI makes mistakes, and you hear that as it is sometimes wrong about hard things. That is not the failure mode. It is wrong in exactly the same voice it uses when it is right. The confidence is not a signal, because the confidence is produced by the same process as the content. There is no separate step where it checks a record of what is true.
Image: Two identical-looking paragraphs side by side, one marked correct and one marked wrong, with no visual difference between them.
---
## Slide 3: Five questions, not one feeling
- Validity: is it correct
- Relevance: does it answer what I asked
- Authenticity: does it belong to somebody
- Potential Bias: whose view is built in
- Hallucinations: does this thing exist at all
Speaker notes: The Ohio standard names five criteria and I want you to treat them as five separate questions. Students collapse them into one general feeling of seems legit, and that feeling is what we are replacing. Each of these catches a different failure, and today you are going to apply all five to one document and label every finding with exactly one of them.
Image: Five navy boxes in a row, each with a short label, connected to a single document icon below.
---
## Slide 4: The hard one, and it is worth four minutes
- Validity: a false claim about a real thing
- Hallucination: it invented the thing
- You test the first one
- You have to go look for the second
Speaker notes: This distinction is the one you will get wrong, so let us do it now. If I tell you Python's sort method returns a new sorted list, that is a validity failure. Sort is real. The sentence about it is false. If I tell you to use Python's titlecase method, that is a hallucination, because there is no such method. Notice the difference in how you catch them. You can test the first by running sort. You cannot test the second at all until you go and look, and find nothing there.
Image: Two columns, one headed with a real object described wrongly, one headed with an empty space described confidently.
---
## Slide 5: Watch this live, and I do not know the answer
```
Ask the local model:
"What does git rm --cached do to a file's history?"
```
Speaker notes: I am going to ask it a question right now, in front of you, and I genuinely do not know what it will say. We verified the real answer last week, so we can check it in about ten seconds. I want you to run the five criteria on whatever comes back while I read it out loud. If it gets it right, that is fine. We are still going to check.
Image: None. This slide is code.
---
## Slide 6: The verification, either way
```
git log --oneline -- secrets.txt
```
```
b151592 Stop tracking the settings file
38cc1b2 Add settings file
```
Speaker notes: Here is what we established last week. The key survives git rm cached. It is still in commit 38cc1b2. Now compare that against what the model told us a moment ago. If it matched, notice that I checked anyway, and notice that checking took ten seconds. That is the habit, and the habit is the lesson. The point was never catching it out.
Image: None. This slide is code.
---
## Slide 7: A statistic with no source is not evidence
- "97 percent of developers say Python is simplest"
- No survey named. No year. No sample
- Precision reads as proof and is not
- Ask what would make you believe it
Speaker notes: Numbers are the most persuasive form a false claim takes, because precision looks like somebody counted something. When you see a figure like this, ask four questions. Who was surveyed. How many. When. Where can I read it. If the answer to all four is nothing, you do not have weak evidence. You have no evidence with a number attached to it.
Image: A large percentage figure with a magnifying glass over the space beneath it where a source would be, and nothing there.
---
## Slide 8: Two failures no command can catch
- Whose perspective is built into the list
- Who got left out of it
- Whether the code you copied belongs to somebody
- These need judgment, not a terminal
Speaker notes: Most of what you find today can be settled by typing one command. Two of the defects cannot. One is about who a document assumes its reader is and who it leaves out. The other is about whether something has an owner. Notice while you work which findings you could prove and which you had to argue. That difference matters more than the count.
Image: A terminal on the left with a green check, and on the right a document with a question mark where a source or an author would be.
---
## Slide 9: What you are about to build
- An autopsy of a study guide that looks good
- Six findings minimum, eight is strong
- Quote it, label it, prove it
- Three findings proved by a command you ran
Speaker notes: You are getting a one page Python study guide that was made with AI. It looks fine. It is not. For every defect you find, I want four things: the exact sentence quoted, which of the five criteria it fails, why it is wrong in your words, and how you know. That last one is where the points are. Saying something is wrong is an opinion. Showing how you checked is the assignment.
Image: A polished-looking one-page guide with a magnifying glass over one line, navy and accent blue, no faces.
---
