# Match the Menu
---
## Slide 1: The snack bar sold you sushi
- The snack bar sells pizza and a daily special
- Today's special is tacos
- You typed sushi
- The program charged you for today's special
Speaker notes: The snack bar program knows two things, pizza and today's special, which is tacos. A student typed sushi to test it, and the program happily charged them two fifty for today's special. No error. The person who wrote it used a brand new Python structure and made the one mistake that structure invites. Today you learn the structure, and you learn to see that mistake coming.
Image: A snack bar menu board with two items and a receipt reading sushi, flat navy and accent blue.
---
## Slide 2: The same question, over and over
```python
if club == "robotics":
    print("Room B114, Tuesdays after school.")
elif club == "band":
    print("Band room, every morning at 7:15.")
elif club == "esports" or club == "gaming":
    print("Lab C, Thursdays. Bring your own headset.")
else:
    print("That club is not on the list. Check the spelling.")
```
Speaker notes: This chain is correct. But look at it. Every condition asks the exact same question about the exact same variable. Which one of these values is it. You typed club double equals four times, and every time is another chance to write Tuesday's or gaming bug. Most languages have a structure built for exactly this. Java and JavaScript call it switch. Python calls it match.
Image: None. This slide is code.
---
## Slide 3: The same program with match
```python
club = input("Which club? ").strip().lower()

match club:
    case "robotics":
        print("Room B114, Tuesdays after school.")
    case "band":
        print("Band room, every morning at 7:15.")
    case "esports" | "gaming":
        print("Lab C, Thursdays. Bring your own headset.")
    case _:
        print("That club is not on the list. Check the spelling.")
```
Speaker notes: Match names the value once. Each case is one option on the menu. The bar symbol means or this one, and it goes between values. Underscore is the catch-all, like else, and it goes last. Python checks cases top to bottom and runs only the first match, same rule as elif. No break statements. It never falls through into the next case.
Image: None. This slide is code.
---
## Slide 4: Three runs
```
Which club? Robotics
Room B114, Tuesdays after school.

Which club? gaming
Lab C, Thursdays. Bring your own headset.

Which club? chess
That club is not on the list. Check the spelling.
```
Speaker notes: Capital R Robotics matched only because we lowered it first. A case compares exactly, character by character, same as double equals. Gaming hit the or pattern. Chess matched nothing and fell to underscore. I also ran the elif version with these three inputs, and it printed the same three lines. Both are correct. The match version reads like a menu.
Image: None. This slide is code.
---
## Slide 5: Match or elif
- match: one variable, exact values, a menu
- elif: ranges with less than or greater than
- elif: conditions about more than one variable
- elif: conditions joined with and or or
Speaker notes: Be honest about the choice. Match is built for exact values. It can do ranges with a guard, case s if s is at least 90, and it is uglier than the elif chain from last Monday. Grade bands, ticket ages, and GPA cutoffs stay elif. Menu choices, commands, and club names become match. Newer is not a reason to rewrite working code.
Image: A two-column comparison card, match on the left with menu icons and elif on the right with a number line.
---
## Slide 6: The wrong way, and no error
```python
TODAYS_SPECIAL = "tacos"
order = input("What do you want? ").strip().lower()

match order:
    case "pizza":
        print("Pizza slice, $3.00")
    case TODAYS_SPECIAL:
        print("Today's special, $2.50")
```
```
What do you want? sushi
Today's special, $2.50
```
Speaker notes: Here is the snack bar. No error, and sushi is today's special. In a case, a value in quotes is compared. A bare name is not compared to anything. It is a capture. It matches whatever the value is and stores it in that name. So this case catches every order that is not pizza, and it overwrites today's special with the word sushi on the way.
Image: None. This slide is code.
---
## Slide 7: Python catches it only sometimes
```python
    case TODAYS_SPECIAL:
        print("Today's special, $2.50")
    case _:
        print("Not on the menu.")
```
```
SyntaxError: name capture 'TODAYS_SPECIAL' makes remaining patterns unreachable
```
Speaker notes: Add a catch-all below the capture and Python refuses to run. The message says this case catches everything, so the one below it can never run. That is the unreachable code from Week 5 Monday, except this time Python warns you. But only when there is a case underneath. On the last slide there was not, so it ran quietly. The fix is to write the value in quotes, case tacos.
Image: None. This slide is code.
---
## Slide 8: Ninth time, same shape
- Tacos passed the test
- Pizza passed the test
- Sushi was never tested
- Always test one input that should match nothing
Speaker notes: Ninth appearance of a bug that does not crash. And the testing lesson is the same one from Tuesday. The two obvious tests pass. The test that finds it is the input that should reach the catch-all. So for every match you write, run one value that should match nothing, and watch it land in underscore. If it lands anywhere else, you have a capture.
Image: A test checklist with tacos and pizza checked and a third row reading nothing should match, circled in accent blue.
---
## Slide 9: Other languages, other words
- switch is Java, JavaScript, and C#
- default is their catch-all
- Both are a SyntaxError in Python
- Python says match and case underscore
Speaker notes: If you have written any Java or JavaScript, your fingers will type switch and default. Python says invalid syntax for both. And one practical warning. Match arrived in Python 3.10. The lab runs 3.14. If you try this on an old computer at home and every match line is a syntax error, check python dash dash version before you check your code.
Image: Two keyboard keycaps labeled switch and default with a small crossed circle, navy and accent blue.
---
## Slide 10: What you are about to build
- Build 1: Lab U02-02 Club Sign-Up Validator
- match picks the club, conditions check eligibility
- Build 2: Problem Drop 1, 40 minutes
- Nobody tells you what to build
Speaker notes: Build 1 is the club sign-up validator. A student picks a club, match routes them, and compound conditions check whether they are eligible for that club. Step six asks you to test one club name that should match nothing. Build 2 is your first Problem Drop. Forty minutes, a real annoyance, and a problem statement that is not quite the real problem. Nobody will tell you what to build. Finding what to build is the assignment.
Image: A club sign-up sheet on a clipboard with several club names, flat navy and accent blue.
---
