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
