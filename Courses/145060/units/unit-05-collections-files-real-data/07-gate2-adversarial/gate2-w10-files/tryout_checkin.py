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
