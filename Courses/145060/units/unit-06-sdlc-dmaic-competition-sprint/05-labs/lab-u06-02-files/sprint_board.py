# sprint_board.py
#
# Reads the team's task list and prints a stand-up board: what is done, what
# is late, what is blocked, and whether the remaining work fits the days left.
#
# Usage:
#     python sprint_board.py tasks.csv TODAY PEOPLE
#     python sprint_board.py tasks.csv 8 3
#
# This file runs right now. It prints a header and nothing useful.

import csv
import sys

# The sprint runs on class days, not calendar days. Day 1 is Monday Nov 30.
# Weekends and winter break are not in the list, so they cannot be counted.
DAY_LABELS = [
    "Mon Nov 30", "Tue Dec 1", "Wed Dec 2", "Thu Dec 3", "Fri Dec 4",
    "Mon Dec 7", "Tue Dec 8", "Wed Dec 9", "Thu Dec 10", "Fri Dec 11",
    "Mon Dec 14", "Tue Dec 15", "Wed Dec 16", "Thu Dec 17", "Fri Dec 18",
]
LAST_BUILD_DAY = 14      # Day 15 is acceptance demos, not building
BLOCKS_PER_DAY = 2       # Build 1 and Build 2
STATUSES = ["todo", "doing", "blocked", "done"]

# TODO 1: read_tasks(path) returns (tasks, problems). Each task is a dictionary.
# TODO 2: count_by_status(tasks) returns a dictionary from status to count.
# TODO 3: remaining_blocks(tasks) adds up the estimates of tasks not done.
# TODO 4: capacity(today, people) returns build blocks left for the team.
# TODO 5: overdue(tasks, today) lists tasks due before today that are not done.
# TODO 6: remaining_by_role(tasks) totals the remaining estimate per role.


def main():
    """Read the arguments and print the board. Right now it only prints the header."""
    if len(sys.argv) != 4:
        print("Usage: python sprint_board.py tasks.csv TODAY PEOPLE")
        sys.exit(1)

    today = int(sys.argv[2])
    print(f"SPRINT BOARD | Day {today} of {len(DAY_LABELS)} ({DAY_LABELS[today - 1]})")
    print("=" * 52)
    print("Nothing on the board yet.")


if __name__ == "__main__":
    main()
