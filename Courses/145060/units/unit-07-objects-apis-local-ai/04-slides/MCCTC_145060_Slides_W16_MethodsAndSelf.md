# Methods and self
---
## Slide 1: How does a method know which object
- You have two gear objects
- You call check_out on one of them
- How does it change that one, not both
- The answer is one small word
Speaker notes: Here is today's puzzle. You have two gear objects. You call check_out on one. Somehow it changes that one and leaves the other alone. How does the method know which object it belongs to. The answer is self, and by the end of class it will make sense.
Image: Two gear objects side by side, one highlighted, a method arrow pointing only at it.
---
## Slide 2: A method is a function on a class
- Its first parameter is always self
- self is the object it was called on
- You never type self at the call
- Python fills it in from before the dot
Speaker notes: A method is a function that lives on a class. Its first parameter is self. When you call pad dot check_out, Python takes pad, the object before the dot, and hands it to the method as self. You never type it yourself. Python fills it in from whatever is before the dot.
Image: pad.check_out("NovaFox") with an arrow showing pad becoming self.
---
## Slide 3: A method that changes its object
```python
class Gear:
    def __init__(self, tag):
        self.tag = tag
        self.borrower = None

    def check_out(self, borrower):
        if self.borrower is not None:
            return f"{self.tag} is already out with {self.borrower}."
        self.borrower = borrower
        return f"{self.tag} is now out with {borrower}."
```
Speaker notes: Read the method. It reads self dot borrower to check the rule, then writes self dot borrower to record the loan. Everything about the object is reached through self. The rule about being already loaned lives right here, next to the data it protects.
Image: None. This slide is code.
---
## Slide 4: Two objects prove what self is
```python
first = Gear("CTRL-01")
second = Gear("CTRL-02")
first.check_out("NovaFox")
print(first.borrower)     # NovaFox
print(second.borrower)    # None
```
Speaker notes: This is the example that makes self click. I called check_out on first, so self was first, so only first changed. Second was never touched. The same method on second would change second instead. That is the entire meaning of self, the specific object before the dot.
Image: None. This slide is code.
---
## Slide 5: Some methods only report
- Not every method changes the object
- Some only answer a question
- is_available reads, does not write
- Still takes self, to see its own data
Speaker notes: Methods do not have to change anything. is_available only reads the object's own state and returns True or False. It still takes self, because it needs to see the object's own data. Two objects, two different answers, from one method.
Image: A gear answering "available?" with True, another answering False.
---
## Slide 6: The trap, forget self
```python
class Gear:
    def __init__(self, tag):
        self.tag = tag
    def label():               # WRONG: no self
        return "gear"

Gear("CTRL-01").label()
```
Speaker notes: This method does not use the object, so it feels like it should not need self. Watch what Python says when I call it. The error is going to talk about arguments, and the number will be confusing until you see why.
Image: None. This slide is code.
---
## Slide 7: takes 0 but got 1
```
TypeError: Gear.label() takes 0 positional arguments but 1 was given
```
Speaker notes: The one argument I supposedly gave is the object itself. Python always hands the object to the method, and label had no parameter to catch it because I left out self. The fix is def label with self in the parentheses. Every method's first parameter is self, even when the method ignores it.
Image: None. This slide is code.
---
## Slide 8: Why forgetting self is tempting
- label does not use the object
- So self feels unnecessary
- But Python passes it anyway
- Every method must accept it
Speaker notes: The trap is tempting because label never touches the object, so self looks like clutter. But Python does not know that. It passes the object to every method, used or not, so every definition needs self first. A method that ignores its object still has to accept it.
Image: An arrow always delivering the object to a method, whether the method uses it.
---
## Slide 9: Reading a call out loud
- locker.check_out("CTRL-01", "NovaFox")
- self is locker, before the dot
- tag is "CTRL-01"
- borrower is "NovaFox"
Speaker notes: Practice reading a call. Locker dot check_out with two strings. Self is locker, the object before the dot. The two strings become tag and borrower, the parameters after self. Being able to say this for any call is the whole skill for today.
Image: The call with three arrows labeled self, tag, borrower.
---
## Slide 10: What you are about to build
- Write is_available and check_out
- Write check_in and label
- Prove self with two objects
- Pass the Part 2 tests
Speaker notes: Build one is writing the four methods on Gear. Build two proves self with two objects and finishes the broken-gear and already-out cases. Run the Part 2 tests until all six pass. Tomorrow the locker holds these gears.
Image: A test runner with six green Part 2 tests, navy and accent blue.
