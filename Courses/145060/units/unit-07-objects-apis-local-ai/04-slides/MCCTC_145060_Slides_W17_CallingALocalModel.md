# Putting a Model Inside Your Program
---
## Slide 1: A model can write the boring part for you
- Your room has dry stored facts
- A model can turn them into a scene
- It speaks HTTP, like the weather feed
- But its reply is text it made up
Speaker notes: A language model on lab hardware can turn dry facts into readable prose. A room's stored facts into a narrated scene. You call it the same way you called the weather feed, because it speaks HTTP. The new part is that its reply is text a model invented, so you cannot trust it blindly.
Image: A plain list of facts on the left, a narrated paragraph on the right, a model between.
---
## Slide 2: Be honest about what a model is
- It generates plausible text
- Plausible is not the same as correct
- It can drop facts and stop early
- It does not know anything
Speaker notes: Say this plainly. A model generates plausible text. Plausible is not correct. It can reword a number, drop a fact, or stop mid-sentence, and it does not know anything. Your program has to treat every reply as untrusted until it has checked it. That is the whole lesson today.
Image: A speech bubble labeled "plausible" next to one labeled "correct", not equal sign between.
---
## Slide 3: The request is a POST
```python
payload = json.dumps({"model": "llama3.2", "prompt": "Say hello.", "stream": False})
request = urllib.request.Request(base + "/api/generate",
                                 data=payload.encode("utf-8"),
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
with opener.open(request, timeout=20) as response:
    reply = json.loads(response.read().decode("utf-8"))
```
Speaker notes: This is a POST, because you are sending data, the prompt. stream false asks for one whole reply instead of a stream of pieces. Otherwise it is the same urllib and json you already know. The reply comes back as JSON with two fields you care about, response and done.
Image: None. This slide is code.
---
## Slide 4: Check before you trust
```python
def usable_text(reply):
    if reply.get("done") is not True:
        return None
    text = reply.get("response")
    if not isinstance(text, str) or text.strip() == "":
        return None
    return text.strip()
```
Speaker notes: Status 200 is not enough. Check done is exactly True. Check response is a string and not empty. Only then return the text. Each bad reply returns None, which tells the caller to fall back. This is the running thread on the model, in one small function.
Image: None. This slide is code.
---
## Slide 5: Fall back to something you control
- A bad reply is not a dead end
- Use the description or template you wrote
- The person always gets something correct
- A bad model never breaks the feature
Speaker notes: When a reply fails a check, you do not show nothing. You fall back to the stored description or the plain template your own code holds. The person reading the announcements still gets a correct, complete sentence. A missing or broken model only means they see the plain version.
Image: A path splitting: good reply used, bad reply falling back to a template.
---
## Slide 6: The trap, skip the done check
```python
reply = {"response": "The dials glow amber. Type broadcast to", "done": False}
print(reply["response"])
```
Speaker notes: Here is the reply from a model that got cut off. done is False, but nothing checked it. Predict what prints. The JSON is valid, the status was 200, and the response field has text in it. Every sign says it worked. Watch.
Image: None. This slide is code.
---
## Slide 7: A half sentence, printed as truth
```
The dials glow amber. Type broadcast to
```
Speaker notes: No error. A half-sentence printed as if it were finished. In the text adventure, a description that loses broadcast on 1470 could make the game unwinnable. The reply was valid JSON with status 200, so no exception fired. Only your own done check catches this.
Image: None. This slide is code.
---
## Slide 8: Check done with is not True
- Do not write if reply.get("done")
- The string "false" is truthy
- A lazy check passes a bad reply
- Require the real boolean, is not True
Speaker notes: One more trap inside the trap. Do not check done with plain truthiness. The string false, spelled f a l s e, is truthy, so if reply dot get done would pass a reply that is not done. Write is not True to require the actual boolean. This exact thing bites people.
Image: A comparison of "if reply.get(done)" failing on "false" versus "is not True" catching it.
---
## Slide 9: Keep the facts you need
- A reply can be done and still wrong
- It might reword 1470 as fourteen seventy
- After the other checks, confirm the fact appears
- If it dropped it, throw it away
Speaker notes: A reply can pass every check and still be wrong for you, because a model rewords things. If it turns 1470 into fourteen seventy, the player cannot win, with no error to warn anyone. After the other checks, confirm the required fact still appears in the text, and reject the reply if it does not.
Image: A reply missing "1470" being rejected in favor of the stored text.
---
## Slide 10: What you are about to build
- Write parse_reply with the three checks
- Strip control characters from the reply
- Fall back to the template on any failure
- Pass the announcement tests
Speaker notes: Build one writes parse_reply with the done, type, and empty checks, and strips control characters from the reply. Build two wires write_announcement to use the model when the reply is good and the template when it is not. Run the tests, and try the stub in not_done mode to see the fallback.
Image: A terminal showing an announcement, one from the model and one from the template, navy and accent blue.
