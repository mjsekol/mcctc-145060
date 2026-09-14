# test_concessions.py
#
# Acceptance tests for concessions.py. You write these from the stakeholder's
# acceptance criteria in the lab handout, NOT from reading the code. If you
# read the code first, your tests will agree with whatever it does.
#
# Run:  python test_concessions.py
#
# This file runs right now. It checks one thing.

import concessions

# One True or False per check, so the summary can count them.
results = []


def check(label, actual, expected):
    """Print PASS or FAIL for one check and remember the result."""
    if actual == expected:
        results.append(True)
        print(f"PASS  {label}")
    else:
        results.append(False)
        print(f"FAIL  {label}")
        print(f"        expected: {expected!r}")
        print(f"        actual:   {actual!r}")


def refused(item, quantity):
    """Return 'ValueError' if line_total refuses this line, or the total if it does not."""
    try:
        return concessions.line_total(item, quantity)
    except ValueError:
        return "ValueError"


# AC-1: every item costs its listed price.
check("AC-1 three pretzels", concessions.line_total("pretzel", 3), 10.5)

# TODO AC-2: quantities 1 through 20 are allowed. Test both edges and one step past each.

# TODO AC-3: an item the stand does not sell is refused.

# TODO AC-4: every hot dog paired with ANY drink is a combo.

# TODO AC-5: members get 10 percent off AFTER combo savings.

# TODO AC-6: totals are rounded to cents.

# TODO AC-7: an empty order costs nothing.

print()
print(f"{results.count(True)} passed, {results.count(False)} failed")
