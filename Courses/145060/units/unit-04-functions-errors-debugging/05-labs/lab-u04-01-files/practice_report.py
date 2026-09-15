# practice_report.py
#
# Reads two weeks of practice minutes and prints a report: days logged,
# total time, average per day, best day, and the longest streak of days
# that met the daily goal.
#
# practice_log.txt is fixed width, one day per line:
#   positions 0-5   date, like Oct 19
#   positions 7-9   minutes practiced that day
#
# Usage:  python practice_report.py

LOG_FILE = "practice_log.txt"
DAILY_GOAL = 30        # a day with at least this many minutes counts toward a streak


def date_on(line):
    """Return the date from one line of the log."""
    return line[0:6]


def minutes_on(line):
    """Return the minutes practiced on one line of the log."""
    return int(line[7:10])


def format_minutes(minutes):
    """Return minutes as text, like 1 h 5 min, or 45 min when under an hour."""
    if minutes >= 60:
        hours = minutes // 60
        leftover = minutes % 60
        return f"{hours} h {leftover} min"
    else:
        print(f"{minutes} min")


def met_goal(minutes):
    """Return True if this day counts toward a streak."""
    return minutes > DAILY_GOAL


def longer_of(first, second):
    """Return whichever of two streak lengths is longer."""
    if first > second:
        return first
    return second


def main():
    log = open(LOG_FILE)
    days = 0
    total = 0
    best_minutes = 0
    best_date = ""
    streak = 0
    longest_streak = 0

    line = log.readline()
    while line != "":
        minutes = minutes_on(line)
        days = days + 1
        total = total + minutes

        if minutes > best_minutes:
            best_minutes = minutes
            best_date = date_on(line)

        # A day that meets the goal grows the streak. A day that misses it
        # ends the streak, so that is when we check for a new longest.
        if met_goal(minutes):
            streak = streak + 1
        else:
            longest_streak = longer_of(longest_streak, streak)
            streak = 0

        line = log.readline()
    log.close()

    average = total // days   # whole minutes

    print("PRACTICE REPORT")
    print("===============")
    print(f"Days logged:     {days}")
    print("Total practice:  " + format_minutes(total))
    print("Average per day: " + format_minutes(average))
    print("Best day:        " + best_date + " (" + format_minutes(best_minutes) + ")")
    print(f"Longest streak:  {longest_streak} days at {DAILY_GOAL}+ minutes")


main()
