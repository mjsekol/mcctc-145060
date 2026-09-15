# Gate 2: Adversarial Review · Week 10
## 145060 Programming · Unit 5 · Friday, November 13

**35 minutes.** Individual. You may and should run the code. You may not ask a model whether
it is correct, because the model is what is being reviewed.

The program is in `gate2-w10-files/tryout_checkin.py`. Run it from that folder.

---

## What you are looking at

A soccer coach gave an AI assistant the requirements in Part A and got the program in Part B.
It runs. It uses a list of dictionaries, the report is lined up, and it looks finished.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It reads, exposes, or trusts something it should not |
| **Readability** | A name or comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be, or the wrong structure for the job |
| **Requirements Fit** | Something the spec asked for that is missing, or something nobody asked for |

---

## PART A: The requirements

> Write `tryout_checkin.py` for the tryout coaches.
>
> 1. Registered players are in a list at the top of the file. Each has a bib number, name, age
>    group, 40-yard sprint time in seconds, and a medical note.
> 2. As each player arrives, the coach types their bib number. Confirm with the player's name
>    and age group.
> 3. A bib number that is not registered prints a warning and is not checked in.
> 4. A player whose bib is typed twice is only checked in once.
> 5. A blank line ends check-in. Then, for each age group, print the players who checked in, in
>    the order they arrived, followed by the group's **average** sprint time and its
>    **fastest** sprint time, counting only players who checked in.
> 6. Print the names of registered players who did not show up, so the coaches can call their
>    families.
> 7. **Medical notes are for the athletic trainer only. This program must never print them.**
> 8. Registration allows up to 50 players, so looking up a bib should not get slower and slower
>    as the list grows.

---

## PART B: What the AI produced

Count line numbers from `# tryout_checkin.py` as line 1. Blank lines count.

```python
# tryout_checkin.py
#
# Checks players in at soccer tryouts and prints a report for the coaches.
# Coaches type each player's bib number as the player arrives. A blank line
# ends check-in and prints the report.

REGISTERED = [
    {"bib": "3", "name": "Lena Ortiz", "age_group": "U15", "sprint_seconds": 6.8, "medical_note": "none"},
    {"bib": "7", "name": "Caleb Park", "age_group": "U15", "sprint_seconds": 7.4, "medical_note": "inhaler in bag"},
    {"bib": "12", "name": "Imani Wright", "age_group": "U17", "sprint_seconds": 6.5, "medical_note": "none"},
    {"bib": "15", "name": "Diego Alvarez", "age_group": "U17", "sprint_seconds": 6.9, "medical_note": "knee brace, cleared by doctor"},
    {"bib": "21", "name": "Ruby Chen", "age_group": "U15", "sprint_seconds": 7.1, "medical_note": "none"},
    {"bib": "24", "name": "Owen Murphy", "age_group": "U17", "sprint_seconds": 7.0, "medical_note": "peanut allergy, EpiPen with trainer"},
    {"bib": "30", "name": "Nadia Haddad", "age_group": "U17", "sprint_seconds": 6.6, "medical_note": "none"},
]

AGE_GROUPS = ["U15", "U17"]


def find_player(bib):
    """Return the registered player with this bib number, or None."""
    for player in REGISTERED:
        if player["bib"] == bib:
            return player
    return None


def check_in_players():
    """Read bib numbers until a blank line. Return the bibs in arrival order."""
    checked_in = []
    bib = input("Bib number (blank to finish): ").strip()
    while bib != "":
        player = find_player(bib)
        if player is None:
            print(f"  Bib {bib} is not registered. Send them to the registration table.")
        elif bib in checked_in:
            print(f"  Already checked in: {player}")
        else:
            checked_in.append(bib)
            print(f"  Checked in {find_player(bib)['name']} ({find_player(bib)['age_group']})")
        bib = input("Bib number (blank to finish): ").strip()
    return checked_in


def group_report(group, checked_in):
    """Print the checked-in players in one age group and the group's average sprint."""
    print(f"\n{group}")
    total_seconds = 0
    group_size = 0
    for player in REGISTERED:
        if player["age_group"] == group:
            group_size += 1
    for bib in checked_in:
        player = find_player(bib)
        if player["age_group"] == group:
            print(f"  #{bib:<3} {player['name']:<16} {player['sprint_seconds']:.1f} s")
            total_seconds += player["sprint_seconds"]
    if group_size > 0:
        # Average sprint time for the group, rounded to a tenth of a second.
        print(f"  Average sprint: {total_seconds / group_size:.1f} s")


def count_no_shows(checked_in):
    """Work out which registered players did not arrive."""
    missing = []
    for player in REGISTERED:
        if player["bib"] not in checked_in:
            missing.append(player["name"])
    return missing


def main():
    print("TRYOUT CHECK-IN")
    checked_in = check_in_players()
    print(f"\nChecked in: {len(checked_in)} of {len(REGISTERED)}")
    for group in AGE_GROUPS:
        group_report(group, checked_in)
    no_shows = count_no_shows(checked_in)
    print(f"\nDid not show: {', '.join(no_shows)}")


main()
```

### A real run

The coach typed `12`, `3`, `7`, `99`, `15`, `21`, `30`, then a blank line. (Input was piped in,
so the typed numbers do not appear after the prompts.)

```
TRYOUT CHECK-IN
Bib number (blank to finish):   Checked in Imani Wright (U17)
Bib number (blank to finish):   Checked in Lena Ortiz (U15)
Bib number (blank to finish):   Checked in Caleb Park (U15)
Bib number (blank to finish):   Bib 99 is not registered. Send them to the registration table.
Bib number (blank to finish):   Checked in Diego Alvarez (U17)
Bib number (blank to finish):   Checked in Ruby Chen (U15)
Bib number (blank to finish):   Checked in Nadia Haddad (U17)
Bib number (blank to finish): 
Checked in: 6 of 7

U15
  #3   Lena Ortiz       6.8 s
  #7   Caleb Park       7.4 s
  #21  Ruby Chen        7.1 s
  Average sprint: 7.1 s

U17
  #12  Imani Wright     6.5 s
  #15  Diego Alvarez    6.9 s
  #30  Nadia Haddad     6.6 s
  Average sprint: 5.0 s

Did not show: Owen Murphy
```

**Check every number in that output against the list at the top of the program before you read
any function.** One number is impossible.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**, and **the
fix**. Then one final entry: **what I was unsure about**. That entry is scored.

### How to spend 35 minutes

- **First 5:** run it with the same bibs as the real run. Check each average by hand.
- **Next 10:** test requirement 4. Type the same bib twice. Read everything the program prints
  and ask who is allowed to see it.
- **Next 10:** read Part A one requirement at a time and point at the line that satisfies it.
- **Rest:** read every function name and comment against what the code actually does and
  returns, and count how many times the program searches the whole list.

**To pipe input in, use a Git Bash terminal:** `printf '12\n3\n\n' | python tryout_checkin.py`.
PowerShell's pipe can add an invisible character to the first line, which makes the first bib
look unregistered. Typing the bibs by hand works in any terminal.

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start. **Four of five is a strong score.**
