# gear_locker.py  ·  Lab U7-01 starter
#
# The esports club lends controllers and headsets. Right now the loan list is
# a pile of dictionaries, and it has already lied to somebody. By Thursday this
# file holds two classes:
#
#   Gear         one controller or headset
#   GearLocker   the whole cabinet
#
# This file runs right now. It does not do anything useful yet.
#
# Borrowers are gamer tags, never real names. The loan list goes on the
# projector at club meetings.

CONDITIONS = ["good", "worn", "broken"]


# ----- The way the club tracks gear today -----
# Read this, run it, and look hard at the last line it prints.

def make_gear_dict(tag, kind, condition="good"):
    return {"tag": tag, "kind": kind, "condition": condition, "borrower": None}


def lend_dict(gear, borrower):
    gear["borrower"] = borrower


def is_available_dict(gear):
    # Somebody typed this line in a hurry.
    return gear.get("borower") is None and gear["condition"] != "broken"


def show_the_old_way():
    old_pad = make_gear_dict("CTRL-01", "controller")
    lend_dict(old_pad, "NovaFox")
    print("Dictionary version says CTRL-01 is available:", is_available_dict(old_pad))


# ----- Part 1, Tuesday: the Gear class -----
# TODO 1: Write class Gear with an __init__ that takes tag, kind, and a
#         condition that defaults to "good". Store all three on self, plus
#         borrower (None) and times_loaned (0).
# TODO 2: Refuse a condition that is not in CONDITIONS by raising ValueError.


# ----- Part 2, Wednesday: methods -----
# TODO 3: is_available(), check_out(borrower), check_in(condition), label()


# ----- Part 3, Thursday: GearLocker -----
# TODO 4: class GearLocker with add, find, check_out, check_in, available, report
# TODO 5: def build_locker() returning the club's four pieces of gear


if __name__ == "__main__":
    show_the_old_way()
    print("Nothing is tracked by a class yet.")
