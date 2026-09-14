# Lab U6-03: Structured Peer Review
## 145060 Programming · Unit 6 · Week 15

**Gate:** 3 (open tooling). **Duration:** Build 1, Monday, December 14, 35 minutes. Pairs.
**Competencies:** 5.6.13 (perform code reviews: peer walkthrough, static analysis), 5.6.9 (review by peer
walkthrough), 1.2.3 (verbal, nonverbal, and active listening).

**Files:** `05-labs/lab-u06-03-files/cart_checkout.py` and `review_check.py`. Copy both into one folder.
**Also open:** `09-project/MCCTC_145060_PeerReview_Protocol.md` and
`09-project/MCCTC_145060_PeerReview_ScoringForm.md`.

---

## The scenario

Room 214 has a cart of 24 laptops, and another team wrote the program that tracks which seat has which
laptop. The teacher who uses it says laptops "disappear from the report" and nobody can explain why. In 40
minutes today, your own team's code gets exactly this kind of review, so this is the rehearsal.

## What you will build

A complete peer review of `cart_checkout.py` on the five-dimension scoring form, using both static analysis
and a requirement-by-requirement walkthrough, and a short comparison of what each method found.

**You are not fixing the code.** A reviewer's job is findings that the author can act on.

---

## The requirements the other team was given

> `cart_checkout.py` tracks the Room 214 laptop cart.
>
> 1. The cart holds laptops numbered **1 to 24**. The state is saved in `cart.json`, a dictionary from laptop
>    number (as text) to the seat code that has it, or `""` when the laptop is on the cart.
> 2. `out LAPTOP SEAT` checks a laptop out. It refuses a laptop number outside 1 to 24, refuses a laptop that is
>    already out, and refuses a seat code that is not in the form `R3-S2` with **row 1 to 6 and seat 1 to 5**.
> 3. `in LAPTOP` returns a laptop. It refuses a laptop that is not checked out.
> 4. `report` prints every laptop still out **in laptop number order** with its seat, and **how many laptops are on
>    the cart.**
> 5. `reset CODE` puts every laptop back on the cart. It requires the teacher's reset code, which must **never be
>    written in the code**. It is read from `reset_code.txt`, a file that is never committed.
> 6. Every change is saved to `cart.json`. **A failed save must be reported.**

---

## The code under review

Line numbers count from `# cart_checkout.py` as line 1.

```python
# cart_checkout.py
#
# Laptop cart checkout for Room 214. Written by another team for review.
#
# The cart holds laptops numbered 1 to 24. A laptop is checked out to a seat
# code such as R3-S2 (row 3, seat 2), never to a name.
#
# Usage:
#     python cart_checkout.py out 7 R2-S4
#     python cart_checkout.py in 7
#     python cart_checkout.py report
#     python cart_checkout.py reset <code>

import json
import sys

CART_FILE = "cart.json"
CART_SIZE = 24
RESET_PIN = "4471"


def new_cart():
    """Return a cart with every laptop on it. An empty seat code means on the cart."""
    cart = {}
    for laptop in range(1, CART_SIZE + 1):
        cart[str(laptop)] = ""
    return cart


def load_cart(path):
    """Read the cart from its JSON file, or start a fresh cart if there is none."""
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return new_cart()


def save_cart(cart, path):
    """Write the cart back to its JSON file."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(cart, file, indent=2)
    except:
        pass


def chk(c, n):
    return c[str(n)] != ""


def valid_laptop(laptop):
    """Return True when the laptop number exists on this cart."""
    if laptop < 1 or laptop >= CART_SIZE:
        return False
    return True


def checkout(cart, laptop, seat):
    """Check a laptop out to a seat. Returns a message for the person at the cart."""
    if not valid_laptop(laptop):
        return f"There is no laptop {laptop} on this cart."
    if chk(cart, laptop):
        return f"Laptop {laptop} is already out to {cart[str(laptop)]}."
    # Seat codes are row 1-5, seat 1-6, written like R3-S2.
    cart[str(laptop)] = seat
    return f"Laptop {laptop} checked out to {seat}."


def checkin(cart, laptop):
    """Return a laptop to the cart. Returns a message for the person at the cart."""
    if not valid_laptop(laptop):
        return f"There is no laptop {laptop} on this cart."
    cart[str(laptop)] = ""
    return f"Laptop {laptop} is back on the cart."


def report(path):
    """Print every laptop still out at the end of the period, in laptop order."""
    still_out = []
    for laptop in range(1, CART_SIZE + 1):
        with open(path, encoding="utf-8") as file:
            cart = json.load(file)
        if cart[str(laptop)] != "":
            still_out.append(str(laptop))
    still_out.sort()
    print("STILL OUT AT END OF PERIOD")
    for laptop in still_out:
        print(f"  Laptop {laptop:>2}  {cart[laptop]}")


def main():
    """Run one cart command from the command line."""
    if len(sys.argv) < 2:
        print("Usage: python cart_checkout.py out|in|report|reset ...")
        return

    command = sys.argv[1]
    cart = load_cart(CART_FILE)

    if command == "out" and len(sys.argv) == 4:
        print(checkout(cart, int(sys.argv[2]), sys.argv[3]))
    elif command == "in" and len(sys.argv) == 3:
        print(checkin(cart, int(sys.argv[2])))
    elif command == "report":
        save_cart(cart, CART_FILE)
        report(CART_FILE)
        return
    elif command == "reset" and len(sys.argv) == 3:
        if sys.argv[2] == RESET_PIN:
            cart = new_cart()
            print("Cart reset. Every laptop is on the cart.")
        else:
            print("Wrong reset code.")
    else:
        print("Usage: python cart_checkout.py out|in|report|reset ...")
        return

    save_cart(cart, CART_FILE)


if __name__ == "__main__":
    main()
```

**Running the program creates `cart.json` in the folder.** To start over with every laptop on the cart, delete
`cart.json`.

---

## Roles

One partner is the **reader**, who keeps the review moving through the requirements and the checklist. The other
is the **recorder**, who writes every finding on the form as it is found. **Swap roles at step 5.** There is no
author in the room today, so where the protocol says "the author points at the lines," the reader points instead.

---

## Steps

### Step 1. Static analysis first · 4 minutes
Run both tools and paste both outputs into section 1 of a new scoring form, `review_practice.md`:

```
python -m py_compile cart_checkout.py
python review_check.py cart_checkout.py
```

**Observable result:** `py_compile` prints nothing. `review_check.py` prints a numbered list of findings and a count.

### Step 2. Judge every static finding · 3 minutes
For each line the checker printed, decide together: a real problem, or a false alarm? Write which, and why, in section 1.
**Observable result:** every static finding marked real or false alarm, with a reason.

### Step 3. Run it the way a teacher would · 5 minutes
Check out three or four laptops, including **laptop 24** and **laptop 10**, check one in, and run `report`. Read the report
against requirement 4.
**Observable result:** your terminal shows each command and its message. Write down anything that disagrees with a
requirement.

### Step 4. Walk through requirement by requirement · 12 minutes
The reader reads requirement 1 aloud. Together, point at the lines that satisfy it. Then ask: **what input would break
this?** Try it. The recorder writes each finding with all four parts: where, dimension, consequence, fix. Repeat for
requirements 2 through 6.

You may test one function directly, without the command line, like this:

```
python -c "import cart_checkout as c; cart = c.new_cart(); print(c.checkout(cart, 3, 'R2-S1'))"
```

**Observable result:** at least one finding per requirement you could not point at.

### Step 5. Swap roles, run the checklist · 5 minutes
The new reader reads the five-dimension checklist from the protocol aloud. Anything new goes on the form.
**Observable result:** at least one finding the walkthrough missed, or a written "checked, nothing new" under each dimension.

### Step 6. Score and compare · 6 minutes
Score all five dimensions on the form, with finding numbers as evidence. Then add a section to `review_practice.md`:

```markdown
## Tool against person
Found by review_check.py only:
Found by a person only:
The finding I think matters most, and why:
```

**Observable result:** a complete form, and the comparison. Commit and push.

---

## Acceptance criteria

1. Both static outputs are pasted, and every static finding is marked real or false alarm with a reason
2. At least **six** findings in the findings table, each with where, dimension, consequence, and fix
3. At least **three** of those findings came from a person, not from `review_check.py`
4. All five dimensions scored with evidence, and the "tool against person" section complete

---

## If it breaks

### 1. A word where a number goes

```
ValueError: invalid literal for int() with base 10: 'seven'
```

**Cause:** `python cart_checkout.py out seven R1-S1`. The program converts the laptop number without checking it. That is a
finding. Write it down.

### 2. A damaged cart file

```
json.decoder.JSONDecodeError: Expecting value: line 2 column 1 (char 7)
```

**Cause:** `cart.json` was edited by hand or cut off. Delete `cart.json` to start fresh. Whether the program should handle this
more gracefully is a fair finding.

### 3. Your earlier tests are still in the cart

**Cause:** `cart.json` remembers every run. If a laptop "is already out" when you expect it on the cart, delete `cart.json`.

### 4. The checker cannot find the file

```
Cannot open cart_checkout.py
```

**Cause:** `review_check.py` and `cart_checkout.py` are not in the same folder you are running from. Copy both into one folder.

### Not an error: the command-line test for a blank seat

A command like `python cart_checkout.py out 3 ""` behaves differently in PowerShell and in other terminals, because PowerShell
can drop an empty argument. Use the `python -c` form from step 4 for anything involving an empty seat code.

---

## Stretch goal

Pick the one finding you believe would cause the most real harm in Room 214, and write the three-sentence message you would send
the authoring team about it. Use the protocol's rules: point at the line, state the consequence, suggest a fix, and write nothing
that would still make sense with a person's name in it.

---

## Submission checklist

- [ ] `review_practice.md` committed, with both static outputs
- [ ] Six or more findings with all four parts
- [ ] Three or more person-found findings
- [ ] Five dimensions scored with evidence
- [ ] "Tool against person" section complete
- [ ] `cart_checkout.py` unchanged
- [ ] Pushed

---

# Extended Lab Options

All four assess 5.6.13 on the same 100-point five-dimension scale.

## Which version to hand a pair

| What you observe | Hand them |
|---|---|
| At 10 minutes, still at step 2, or treating every static finding as automatically real | SCAFFOLDED |
| Moving through the requirements and writing four-part findings | STANDARD |
| Six findings by minute 20, or asking how `review_check.py` works inside | EXTENDED |
| Says reviewing code is "the teacher's job" | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Step 2:** use this table. Fill in the right column only.

| Static finding | Real or false alarm, and why |
|---|---|
| line 19 `RESET_PIN` | |
| line 44, both findings | |
| line 48, three findings | |
| line 82 | |

- **Step 4:** walk through requirements **1, 2, and 4 only.** For requirement 4, check out laptops 2 and 10 before you run `report`.
- **Acceptance criteria changed:** at least **four** findings, at least **two** from a person.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus one addition that needs something not taught.

**Added requirement.** Add a seventh check to a copy of `review_check.py`: flag any comparison to `None` written with `==` or `!=`
instead of `is` or `is not`. Map it to Readability. Test it on a three-line file you write that contains one of each.

**Hint, not the answer.** Read the `ast` module documentation at `https://docs.python.org/3/library/ast.html` and find the node for a
**comparison**. It stores the operators and the right-hand values in two separate lists, because Python allows chains like
`0 < x < 10`. Also find which node class represents a constant value such as `None`.

**Acceptance criteria:** all STANDARD criteria, plus the new check flags `== None` and `!= None` and does not flag `is None`, shown by a
pasted run.

---

## APPLIED

**For the pair who says reviewing code is the teacher's job.** In a real job, nobody's code reaches users without a colleague reviewing it.

**Changed scenario.** Review a program neither of you wrote that you both use or understand: a pair's text adventure from Unit 5, with that
pair's permission, or the reference `food_drive.py` your instructor can share.

**What you build.** The same scoring form, with the same six-finding and three-by-a-person minimums. The requirements come from that
program's README or project spec.

**The extra requirement that makes it the same lab.** Deliver one finding to the author out loud, following the protocol's "giving a
finding" rules, and write one sentence about how they received it.

**Grading:** same scale.
