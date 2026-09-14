# snack_tally.py
#
# Concession stand tally for the robotics club.
# The volunteer enters each sale in whole dollars. Typing "done" ends the shift.
# Sales must be between $1 and $100. Anything else is refused and not counted.
# At the end, the program prints a shift summary, the milestones reached,
# and whether the club hit tonight's fundraising goal from goal.txt.

GOAL_FILE = "goal.txt"
MIN_SALE = 1
MAX_SALE = 50
MILESTONE_STEP = 50

print("SNACK BAR TALLY")
print("===============")
print('Enter each sale in whole dollars. Type "done" to close out the shift.')
print()

sale_count = 0
total = 0
biggest_sale = 0

while True:
    entry = input("Sale amount: ").strip().lower()

    if entry == "done":
        break

    sale = int(entry)

    # Refuse anything outside the allowed range without counting it.
    if sale < MIN_SALE or sale > MAX_SALE:
        print(f"  Refused. Sales must be from ${MIN_SALE} to ${MAX_SALE}.")
        continue

    # Load tonight's goal so the running status stays accurate.
    goal_file = open(GOAL_FILE)
    goal = int(goal_file.read())
    goal_file.close()

    sale_count = sale_count + 1
    total = total + sale
    if sale > biggest_sale:
        biggest_sale = sale

    print(f"  Recorded ${sale}. Running total: ${total} of ${goal}.")

print()
print("SHIFT SUMMARY")
print("-------------")
print(f"Sales recorded: {sale_count}")
print(f"Total collected: ${total}")

# Celebrate every $50 milestone the stand passed tonight.
for milestone in range(MILESTONE_STEP, total, MILESTONE_STEP):
    print(f"Reached ${milestone}")

goal_file = open(GOAL_FILE)
goal = int(goal_file.read())
goal_file.close()

if total >= goal:
    print(f"Goal of ${goal} met. Nice work.")
else:
    print(f"${goal - total} short of the ${goal} goal.")
