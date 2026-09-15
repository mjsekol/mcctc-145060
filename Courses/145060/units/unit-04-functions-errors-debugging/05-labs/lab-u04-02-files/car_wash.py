# car_wash.py
#
# Tally for the band's Saturday car wash. The volunteer at the sign types the
# kind of vehicle after every wash, then the tip, and the program keeps a
# running total and a progress bar toward the goal in goal.txt.
#
# Written with Unit 3 tools only: one loop, no functions. It works. Your job
# is to change its shape without changing what it does.
#
# Usage:  python car_wash.py

GOAL_FILE = "goal.txt"
CAR_PRICE = 10
SUV_PRICE = 15
TRUCK_PRICE = 20
MAX_TIP = 50        # bigger tips go in the donation jar, not the tally
BAR_WIDTH = 20

goal_file = open(GOAL_FILE)
goal = int(goal_file.readline())
goal_file.close()

washes = 0
raised = 0

print("CAR WASH TALLY")
print("==============")
print(f"Goal: ${goal}")
print("After each wash, type car, suv, or truck. Type done to finish.")

tallying = True
while tallying:
    command = input("> ").strip().lower()

    if command == "car":
        while True:
            tip_text = input(f"Tip in whole dollars, 0 to {MAX_TIP}: ").strip()
            if not tip_text.isdecimal():
                print("Type a whole number of dollars, like 5.")
            elif int(tip_text) > MAX_TIP:
                print(f"Tips over ${MAX_TIP} go in the donation jar, not the tally.")
            else:
                break
        tip = int(tip_text)
        washes = washes + 1
        raised = raised + CAR_PRICE + tip
        filled = raised * BAR_WIDTH // goal
        if filled > BAR_WIDTH:
            filled = BAR_WIDTH
        bar = ""
        for block in range(BAR_WIDTH):
            if block < filled:
                bar = bar + "#"
            else:
                bar = bar + "-"
        print(f"Car ${CAR_PRICE} + tip ${tip}. Raised ${raised} [{bar}]")

    elif command == "suv":
        while True:
            tip_text = input(f"Tip in whole dollars, 0 to {MAX_TIP}: ").strip()
            if not tip_text.isdecimal():
                print("Type a whole number of dollars, like 5.")
            elif int(tip_text) > MAX_TIP:
                print(f"Tips over ${MAX_TIP} go in the donation jar, not the tally.")
            else:
                break
        tip = int(tip_text)
        washes = washes + 1
        raised = raised + SUV_PRICE + tip
        filled = raised * BAR_WIDTH // goal
        if filled > BAR_WIDTH:
            filled = BAR_WIDTH
        bar = ""
        for block in range(BAR_WIDTH):
            if block < filled:
                bar = bar + "#"
            else:
                bar = bar + "-"
        print(f"SUV ${SUV_PRICE} + tip ${tip}. Raised ${raised} [{bar}]")

    elif command == "truck":
        while True:
            tip_text = input(f"Tip in whole dollars, 0 to {MAX_TIP}: ").strip()
            if not tip_text.isdecimal():
                print("Type a whole number of dollars, like 5.")
            elif int(tip_text) > MAX_TIP:
                print(f"Tips over ${MAX_TIP} go in the donation jar, not the tally.")
            else:
                break
        tip = int(tip_text)
        washes = washes + 1
        raised = raised + TRUCK_PRICE + tip
        filled = raised * BAR_WIDTH // goal
        if filled > BAR_WIDTH:
            filled = BAR_WIDTH
        bar = ""
        for block in range(BAR_WIDTH):
            if block < filled:
                bar = bar + "#"
            else:
                bar = bar + "-"
        print(f"Truck ${TRUCK_PRICE} + tip ${tip}. Raised ${raised} [{bar}]")

    elif command == "done":
        tallying = False

    elif command == "":
        print("Type car, suv, truck, or done.")

    else:
        print(f"'{command}' is not a vehicle. Type car, suv, truck, or done.")

print()
print(f"Washes: {washes}")
print(f"Raised: ${raised}")
if raised >= goal:
    print("Goal reached. Thank you.")
else:
    print(f"Still needed: ${goal - raised}")
