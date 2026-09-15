# Lab U5-04: Hoodie Order Cleanup
## 145060 Programming · Unit 5 · Week 11

**Gate:** 3 (open tooling). **Duration:** one Build 1 block, Wednesday, 35 minutes, with the
report and README finishing in Friday flex time if needed. **Competencies:** 5.3.11 (access
data repositories), 5.5.7 (read inputs from a data file), 5.1.5 (data management:
converting a data file to a new format), 5.5.1 (data validation), 5.5.6 (format output).

---

## The scenario

The club is ordering hoodies, and the sign-up sheet was exported from a shared spreadsheet
that everyone typed into differently. The printer needs an exact count by color and size by
Friday, and the treasurer needs to know how much has been collected and how much is still
owed. If the program guesses wrong, somebody gets the wrong size or pays for a hoodie that
never gets ordered.

## What you will build

A program that reads the messy CSV with the `csv` module, cleans every row it can with
rules, lists every row it cannot with the line number and reason, removes duplicates,
converts the clean orders to both CSV and JSON, and prints the printer's and the
treasurer's numbers.

---

## Files you need

Copy `05-labs/fixtures/hoodie_order_messy.csv` into your lab folder. **The names are
invented.** Open it in the editor, not a spreadsheet program, so you see exactly what is in
it.

---

## Starter code

Create `hoodie_cleanup.py`. It runs. It does nothing useful.

```python
# hoodie_cleanup.py
# Cleans the club hoodie sign-up sheet, converts it to JSON, and prints the
# order that the printer and the treasurer each need.
#
# This file runs right now. It does not do anything useful yet.

import csv
import json

MESSY_FILE = "hoodie_order_messy.csv"
CLEAN_CSV = "hoodie_order_clean.csv"
CLEAN_JSON = "hoodie_order.json"
PRICE = 32   # dollars per hoodie

# TODO: dictionaries that translate messy spellings into clean ones.
# TODO: sets of the words that mean paid and unpaid.


def read_and_clean(filename, problems):
    """TODO: return a list of clean order dictionaries.

    Add a sentence to problems for every row that is left out.
    """
    orders = []
    with open(filename, newline="", encoding="utf-8") as sheet:
        reader = csv.DictReader(sheet)
        for raw in reader:
            pass   # every row is ignored for now
    return orders


problems = []
orders = read_and_clean(MESSY_FILE, problems)
print(f"Clean orders: {len(orders)}")
print(f"Rows that need a person: {len(problems)}")
```

Running it produces:

```
Clean orders: 0
Rows that need a person: 0
```

---

## Steps

### Step 1. Starter running and committed
**Observable result:** the two lines above, and a commit.

### Step 2. Measure the mess before you write code
In your README, under `The mess`, list every kind of problem you can find in the file by
reading it. Give the line number of one example of each.
**Observable result:** at least seven kinds. If you found fewer, read the Size, Grade, and
Paid columns again, and look at lines 11 through 14.

### Step 3. Watch `split` get it wrong
In a scratch file, read the lines of the CSV and `split(",")` line 11. Print how many parts
it has, and the name, size, and paid values you would get by position.
**Observable result:** 7 parts instead of 6, a name of `"Reyes`, a size of `10`, and a paid
value of `Navy`. **No error.** Record it under `What I learned`. Delete the scratch file.

### Step 4. Read it properly
In `read_and_clean`, count the rows `csv.DictReader` gives you and print `reader.line_num`,
`raw["Name"]`, and `raw["Size"]` for lines 11, 13, and 14.
**Observable result:** 23 data rows. Line 11 is `'Reyes, Ana'` with size `'L'`. Line 13 is
blank. Line 14 is the header pasted in again.

### Step 5. Skip what is safe to skip
Skip a completely blank row and a repeated header row, without reporting them.

### Step 6. Translate spellings with dictionaries
Create `SIZES`, `COLORS`, and `GRADE_WORDS` dictionaries that map every spelling in the file,
after `.strip().lower()`, to one clean value. Sizes become `S`, `M`, `L`, `XL`, `2XL`. Colors
become `Navy` or `Gray`. Grades become the numbers 9 through 12, including `11th` and
`Junior`. Create `PAID_WORDS` and `UNPAID_WORDS` sets.
**Observable result:** `SIZES["x-large"]` is `"XL"`. `GRADE_WORDS["junior"]` is `11`.

### Step 7. Find problems, never guess
Write `find_problem(raw)` that returns a sentence describing why a row cannot be used, or an
empty string. A size, color, grade, or paid value you do not recognize is a problem. **Do not
default an unknown size to anything.** Rows with a problem go into `problems` as
`line N, Name: reason`.
**Observable result:** three problems: Marcus D. has no size, Emily C. picked a color that is
not offered, and Ravi P.'s paid column says `cash`.

### Step 8. Build clean rows, and catch duplicates with a set
For every row without a problem, build a clean dictionary with `name`, `grade`, `size`,
`color`, `paid` as `True` or `False`, and `notes`. Keep a set of keys made from the clean
name, size, and color. A row whose key is already in the set is a duplicate: report it and
leave it out.
**Observable result:** `Clean orders: 16` and `Rows that need a person: 5`. The two new
problems are Maya R. on lines 9 and 21.

### Step 9. The printer's and the treasurer's numbers
Print a count for every color and size, sizes in the order S, M, L, XL, 2XL. Then print how
many hoodies to order, how much has been collected at $32 each, and how much is still owed.
Then print every problem.
**Observable result:**

```
Navy   S 1  M 2  L 4  XL 2  2XL 1
Gray   S 3  M 2  L 0  XL 0  2XL 1
```

16 hoodies, $352 collected, $160 owed.

### Step 10. Convert, twice, and check
Write the clean orders to `hoodie_order_clean.csv` with `csv.DictWriter`, with `paid` written
as `yes` or `no` so a person reading the spreadsheet understands it. Write the same orders to
`hoodie_order.json` with `json.dump`, where `paid` stays `true` or `false`. Then load the JSON
back and confirm it has 16 orders.
**Observable result:** `"Reyes, Ana"` is quoted in the clean CSV. The JSON has `"grade": 10`
as a number, not `"10"`.

### Step 11. README and push
Add `Rules I chose`: every cleaning rule, one line each, including what you did with `cash`
and why. Push.

---

## Acceptance criteria

- [ ] Uses `csv.DictReader` and `csv.DictWriter`, with `newline=""` on every CSV `open`
- [ ] 16 clean orders and 5 problems, every problem with a line number matching the file
- [ ] No unknown value is guessed or defaulted
- [ ] Printer counts and money totals match step 9
- [ ] `hoodie_order_clean.csv` and `hoodie_order.json` written; the JSON loads back with 16 orders
- [ ] README has `The mess`, `What I learned`, and `Rules I chose`
- [ ] Commits with messages that say why, pushed

---

## If it breaks

### 1. A column name that does not match the header

```
KeyError: 'size'
```

**Cause:** the header says `Size` with a capital S. `DictReader` keys are exactly the header
text.

### 2. Converting a grade that has letters in it

```
ValueError: invalid literal for int() with base 10: '11th'
```

**Cause:** `int()` on text like `11th`. Remove the `th` first, check `.isdigit()`, and look up
words like `junior` in a dictionary.

### 3. Writing a key the writer does not know about

```
ValueError: dict contains fields not in fieldnames: 'paid'
```

**Cause:** the dictionary you passed to `writerow` has a key that is not in `fieldnames`. Make
the list of field names match the keys of your clean rows exactly.

### 4. A blank row after every order in the clean CSV

**Not an error message, and it only shows on Windows.** **Cause:** the output file was opened
without `newline=""`.

### Not an error: Reyes, Ana is split in half, or her size is 10

**Cause:** you used `split(",")` instead of the `csv` module. That is step 3.

---

## Stretch goal

A second export arrives with `Maya R` typed without the period. Your duplicate check treats
her as a new person. Decide whether your program should catch that, write down the risk of
catching too much (two different students named Maya R.), and either implement a check that
flags it for a person or explain in the README why you did not.

---

## Submission checklist

- [ ] Runs from the lab folder with no traceback
- [ ] Numbers match steps 8 and 9
- [ ] Both output files open and look right
- [ ] `git status` clean, pushed
- [ ] AI usage log updated if a model was used at any point
- [ ] Repository URL submitted

---

# Extended Lab Options

All four assess the same competencies on the same 100-point five-dimension scale.

## Which version to hand a student

| What you observe | Hand them |
|---|---|
| Ten minutes in, still using `split(",")` or `readlines()` to get fields | SCAFFOLDED |
| `DictReader` working, building the translation dictionaries | STANDARD |
| Clean counts correct before Build 1 is half over | EXTENDED |
| "I will never order hoodies" or "where does cleaning data happen in a job" | APPLIED |

---

## SCAFFOLDED

**Changed sections:**
- **Starter:** `SIZES`, `COLORS`, `GRADE_WORDS`, and the two paid sets are provided.
- **Steps:** step 2 needs four kinds of mess, not seven. Step 8's duplicate check is removed,
  so the expected result is 18 clean orders, with Maya counted three times, and the student
  writes one sentence explaining why that number is wrong.
- **Step 3 stays.**
- **Checkpoints:** show you after steps 4, 7, and 9.

**Acceptance criteria:** `DictReader` used; the three value problems reported with correct line
numbers; printer counts produced; JSON written; step 3 recorded.

**Grading:** same scale, Requirements Fit judged against this list.

---

## STANDARD

The base lab above, unchanged.

---

## EXTENDED

Everything in STANDARD, plus the stretch goal done properly.

**Added requirement.** Flag possible near-duplicates, such as `Maya R` and `Maya R.`, or `Theo K`
and `Theo K.`, for a person to check. Do not remove them automatically.

**Hint, not the answer.** The standard library module `difflib` compares strings for
similarity. Read about `get_close_matches` in its documentation,
`https://docs.python.org/3/library/difflib.html`, and pay attention to what the `cutoff`
argument does.

**How to test it.** Add two test rows to a **copy** of the CSV: `Maya R` and `Theo K`, with the
same sizes and colors as the originals.

**Added README question.** What `cutoff` did you choose, and give one pair of different real
people whose names your check would wrongly flag.

**Acceptance criteria:** all STANDARD criteria, near-duplicates flagged not removed, the test rows
caught, and the question answered.

---

## APPLIED

**For the student who asks where cleaning data happens in a job.** Everywhere data is typed by
people. Here, a school store buys back used textbooks.

**Changed scenario.** Create `buyback_messy.csv` with at least 15 rows and columns `Title`,
`ISBN`, `Condition`, `Offer`. Put real kinds of mess in it on purpose: ISBNs typed with and
without dashes, conditions written `good`, `Good`, `gd`, `like new`, and `LN`, offers written
`$12`, `12.00`, and `twelve`, one repeated row, one blank row. Invent the book titles.

**What you build.** The same program: clean with dictionaries and sets, report problems with line
numbers, remove duplicates, convert to clean CSV and JSON, and print the total the store will pay
and the count by condition.

**The extra requirement that makes it the same lab.** Your README's `The mess` section must list
every problem you planted, and your program's problem list must catch every one that should not be
guessed. Step 3's `split` test repeated on a title with a comma in it.

**Grading:** same scale and dimensions. Requirements Fit is judged on whether the program catches the
mess the student planted and says so.
