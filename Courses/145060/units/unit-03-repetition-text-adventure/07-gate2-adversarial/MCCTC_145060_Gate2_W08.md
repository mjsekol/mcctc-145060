# Gate 2: Adversarial Review · Week 8
## 145060 Programming · Unit 3 · Friday, October 30

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether
it is correct, because the model is what is being reviewed.

The files are in [`gate2-w08-files/`](gate2-w08-files/): `service_hours.py` and `hours_log.txt`. Put
them in the same folder and run the program from that folder.

**This program uses Unit 3 tools only.** There are no functions in it. You learned `def` on
Wednesday, and you may mention where a function would help in your unsure-about entry, but a missing
function is not one of the five defects.

---

## What you are looking at

Somebody gave an AI assistant the requirements in Part A and got the program in Part B. It runs, the
columns line up, and the numbers look reasonable.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It shows or trusts something it should not |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the spec asked for that is missing |

---

## PART A: The requirements

> The Service Club keeps everyone's volunteer hours in one log file on the laptop at the sign-in table.
> Members walk up, type their own member ID, and check their progress. Write `service_hours.py`.
>
> 1. Read **`hours_log.txt`**. It is fixed width: member ID in positions 0-5, event name in positions
>    7-26, hours in positions 27-28. The advisor adds entries through the year.
> 2. A member types their ID, in any capitalization. Show **only that member's** entries, each with
>    its member ID, event, and hours, so the member can confirm the entries are theirs.
> 3. Print the member's total hours and how many more they need to reach **20**, or that they have met
>    the requirement. **If the ID matches no entries, say so** instead of showing a total.
> 4. Include **every** entry in the log for that member.

The log file:

```
SC1042 Food pantry shift    3
SC1007 Park cleanup         2
SC2210 Food pantry shift    3
SC1040 Library book sale    4
SC1042 Park cleanup         2

SC1007 Blood drive setup    2
SC1042 Tutoring night       2
SC2210 Park cleanup         2
SC1042 Blood drive setup    3
SC1040 Tutoring night       1
```

---

## PART B: What the AI produced

Count line numbers from `# service_hours.py` as line 1. Blank lines count.

```python
# service_hours.py
#
# Service hours lookup for the Service Club sign-in table.
# A member types their ID and sees their logged events, their total hours,
# and how many hours they still need this year.
#
# hours_log.txt is fixed width:
#   positions 0-5    member ID, for example SC1042
#   positions 7-26   event name
#   positions 27-28  hours

LOG_FILE = "hours_log.txt"
REQUIRED_HOURS = 20

print("SERVICE HOURS LOOKUP")
print("====================")
member_id = input("Member ID: ")
print()

log_file = open(LOG_FILE)
total_entries = 0

# Read the log one line at a time until readline reaches the end of the file.
line = log_file.readline().strip()
while line != "":
    # IDs are stored in capitals, so normalize what the member typed.
    if member_id.strip().upper() in line:
        event = line[7:27].strip()
        hours = int(line[27:29])
        print(f"  {line[0:6]}  {event:<20} {hours} hr")
        total_entries = total_entries + hours
    line = log_file.readline().strip()

log_file.close()

print("--------------------")
print(f"Total hours: {total_entries}")
if total_entries >= REQUIRED_HOURS:
    print("Requirement met for the year.")
else:
    print(f"Hours still needed: {REQUIRED_HOURS - total_entries}")
```

### A real run

Typing `sc1042`:

```
SERVICE HOURS LOOKUP
====================
Member ID: sc1042

  SC1042  Food pantry shift    3 hr
  SC1042  Park cleanup         2 hr
--------------------
Total hours: 5
Hours still needed: 15
```

**Before you read the code, count member SC1042's entries in the log file and add up their hours.** Then
compare with the run.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real member at the sign-in
table**, **the input that shows it**, and **the fix**. Then one final entry: **what I was unsure about**.
That entry is scored.

### How to spend 35 minutes

- **First 5:** do the count above. If the program and the file disagree, find out exactly where the
  program stops reading.
- **Next 10:** the laptop is shared. Think about what somebody who is **not** a member, or who types
  carelessly, could type at the prompt. Try an ID with a missing digit. Try pressing Enter on nothing.
- **Next 10:** read Part A one requirement at a time and point at the line that satisfies it.
- **Rest:** read every variable name against what it holds, and ask which lines inside the loop do work
  that never changes from one line of the log to the next.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the security
weighting before you start. **Four of five is a strong score.**
