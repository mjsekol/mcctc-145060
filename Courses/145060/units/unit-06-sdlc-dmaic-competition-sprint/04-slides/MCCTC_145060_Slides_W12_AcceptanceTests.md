# Tests the Stakeholder Signs
---
## Slide 1: Every test passed. The program was wrong.
- Twelve checks, twelve green PASS lines
- The stakeholder runs it on real data
- The totals are off by a little, everywhere
- The tests agreed with the bug
Speaker notes: Here is the worst demo there is. Your test file prints twelve passes. You feel great. The stakeholder runs the program on their own data and every total is off by a little. How did twelve tests miss it? Because somebody ran the program, saw the numbers, and typed those numbers into the tests as the right answers. The tests agreed with the bug. Today is about tests that cannot be fooled that way.
Image: A terminal of green pass lines next to a spreadsheet with small red circles on several totals, navy and blue.
---
## Slide 2: Unit test versus acceptance test
- Unit test: does my code do what I intended
- Acceptance test: does it do what they need
- Expected values come from the stakeholder
- Written before the code, failing at first
Speaker notes: In Unit 4 your tests asked whether your code does what you meant. An acceptance test asks the stakeholder's question instead. Does it do what I need. So the expected value in every check comes from the criterion they signed, or from arithmetic you did by hand. Never from your own program. And you write them before the code, which means today they fail. A failing test today is a promise waiting to be kept.
Image: Two labeled magnifying glasses, one pointed at code, one pointed at a stakeholder's sticky note.
---
## Slide 3: The check helper
```python
results = []

def check(label, actual, expected):
    if actual == expected:
        results.append(True)
        print("PASS", label)
    else:
        results.append(False)
        print("FAIL", label, "expected", expected, "got", actual)

check("AC-2 uneven split rounds up", split_bill(1000, 3), 334)
print(results.count(True), "passed,", results.count(False), "failed")
```
Speaker notes: Here is the helper every test file uses this unit. Classes are Unit 7, so we are not using the unittest module, which needs them. A check takes a label, the actual value, and the expected value. The label starts with the criterion number, so when something fails you know which promise broke. Where did three thirty four come from? Ten dollars split three ways is three thirty three and a third, and rounding up makes three thirty four. A person did that by hand.
Image: None. This slide is code.
---
## Slide 4: Both sides of every boundary
- Rule: 1 to 12 people
- Check 0: refused
- Check 1 and 12: allowed
- Check 13: refused
- Four checks, both edges, one step past each
Speaker notes: A boundary has two edges and each edge has two sides. For one to twelve people, you check zero, which must be refused, one and twelve, which must be allowed, and thirteen, which must be refused. Four checks. If a boundary in your requirements has fewer than four checks around it, the gap is where the bug will live, because edges are the last thing anyone tries by hand.
Image: A number line from 0 to 13 with filled dots at 1 and 12 and hollow dots at 0 and 13.
---
## Slide 5: Testing a refusal
```python
def outcome(total_cents, people):
    try:
        return split_bill(total_cents, people)
    except ValueError:
        return "refused"

check("AC-4 zero people refused", outcome(2400, 0), "refused")
check("AC-4 thirteen people refused", outcome(2400, 13), "refused")
check("AC-4 twelve people allowed", outcome(2400, 12), 200)
```
Speaker notes: A refusal raises ValueError, and a raised error would crash your test file instead of being checked by it. So outcome catches it and turns it into a plain value, the word refused. Now check can compare it like anything else. Twelve people on a twenty four dollar bill is two dollars each, two hundred cents, and zero and thirteen both come back refused.
Image: None. This slide is code.
---
## Slide 6: Watch this
```python
def split_bill(total_cents, people):
    return round(total_cents / people)

share = split_bill(1000, 3)
expected = split_bill(1000, 3)
if share == expected:
    print("PASS uneven split:", share)
else:
    print("FAIL uneven split:", share)
print("Collected:", share * 3, "cents for a 1000 cent bill")
```
Speaker notes: This split bill has a real defect. It rounds to the nearest cent instead of rounding up. And somebody wrote a test for it. Look at where the expected value comes from. It comes from calling split bill. Predict what prints.
Image: None. This slide is code.
---
## Slide 7: A pass that proves nothing
```
PASS uneven split: 333
Collected: 999 cents for a 1000 cent bill
```
Speaker notes: It passed. On broken code. It compared the function's answer to the function's answer, so it would pass if split bill returned seven, or negative forty. It cannot fail, so it proves nothing. The group is one cent short. The sneaky version of this is not calling the function twice. It is running the program, seeing three thirty three, and typing three thirty three into the check. Same result. A test that agrees with the bug.
Image: None. This slide is output.
---
## Slide 8: Find the criteria with no test
```python
criteria = {"AC-1", "AC-2", "AC-3", "AC-4", "AC-5"}
checks = {
    "even split": "AC-1",
    "uneven split rounds up": "AC-2",
    "bill is covered": "AC-3",
    "zero people refused": "AC-4",
}
tested = set()
for label in checks:
    tested.add(checks[label])
print("No test:", sorted(criteria - tested))
```
Speaker notes: Your test plan maps every criterion to at least one check. Sets from Unit 5 find the gaps. Every criterion, minus the ones that have a check, leaves the ones nobody is verifying. This prints AC five. A criterion with no check is a promise nobody will keep an eye on, and that list has to be empty before your stakeholder signs tomorrow.
Image: None. This slide is code.
---
## Slide 9: Agreed means they saw it
- Friday: stakeholder reads your criteria and check labels
- Changing a check Friday costs one line
- Changing it in Week 14 costs the demo
- Later they run it on real data: user acceptance
Speaker notes: Agreed with stakeholders means they actually read your criteria and your check labels, and signed. That is tomorrow. It is also the cheapest moment in the whole project to find a misunderstanding. One line to fix on Friday. The whole demo if you wait until Week 14. And when the stakeholder finally runs your program on their own real data to see if it works for them, that is user acceptance testing, the classroom version of what industry calls beta testing.
Image: A requirements page with a signature line and a checkmark column beside each criterion, navy and blue.
---
## Slide 10: What you are about to build
- Build 1: Lab U06-01, tests for code you did not write
- Write from the spec, not from reading the code
- Build 2: your team's acceptance tests, all failing
- A test plan: every criterion, every check, every source
Speaker notes: Build one is Lab U06-01. Somebody else wrote a concession stand program, and you test it from the stakeholder's criteria without reading the code first. If you read the code first, your tests will agree with whatever it does. Expect some checks to fail, because there are real defects in it. Build two, your team writes its own acceptance tests, every one of them failing today, plus a test plan that says where every expected value came from.
Image: A terminal showing a mix of pass and fail lines above a small test plan table, navy and blue.
---
