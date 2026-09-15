# Lecture Notes: Reading CSV, Cleaning It, and Converting It
## 145060 Programming · Unit 5 · Week 11 · Wednesday, November 18

**Slides for this lesson:** [outline](../04-slides/MCCTC_145060_Slides_W11_CSVAndCleaning.md) · [deck](../04-slides/exports/MCCTC_145060_Slides_W11_CSVAndCleaning.pptx)

If you missed class, you can learn this concept from this file alone. Make the small
`signups.csv` file below first, exactly as shown, including the space before `Theo`.
Every example reads it.

**Every program below was run on Python 3.13.7, on Windows.** The output shown is the
real output. One example behaves differently on Mac and Linux, and it says so.

---

## Why this exists

The club is ordering hoodies. The sign-up sheet has 23 rows, typed by different people,
and nobody typed the same way: `M`, `med`, `Medium`. `11`, `11th`, `Junior`. Someone
pasted the header in a second time halfway down.

The printer needs one number per size by Friday. The treasurer needs to know who has not
paid.

Spreadsheets export data as CSV, and so do forms, school systems, and most apps with an
Export button. It is the most common way real data reaches a program. It almost never
arrives clean, and turning what people typed into what a program can trust is most of the
work in any real data job.

---

## The concept in plain language

**A CSV is text with rules. The `csv` module knows the rules. Cleaning is deciding what
each messy value means, and never guessing silently.**

The rules of CSV, which stands for comma separated values:

- One row per line. Commas between fields.
- The first row is usually a header naming the columns.
- **A field that contains a comma is wrapped in double quotes.** `"Reyes, Ana"` is one
  field.
- **Every value arrives as a string.** Even `11`. The Unit 1 lesson, again.

Three stages you will do every time:

| Stage | What happens |
|---|---|
| **Read** | `csv.DictReader` turns each row into a dictionary keyed by the header. |
| **Clean** | Strip, lower, translate spellings with a dictionary, and send anything unrecognized to a problems list with its line number. |
| **Convert** | Write the clean rows back out, as clean CSV, as JSON, or both, and check nothing was lost. |

---

## The example file

Save this as `signups.csv`:

```
Name,Grade,Size,Paid
Maya R.,11,M,yes
"Reyes, Ana",10,L,Y
 Theo K. ,10th,large,no
Luis M.,9,med,cash
```

---

## The wrong version first: split on commas

It looks like you can split each line on commas. Here is what that does:

```python
sheet = open("signups.csv", encoding="utf-8")
for line in sheet:
    parts = line.strip().split(",")
    print(len(parts), parts[0], "| size:", parts[2])
sheet.close()
```

Output:

```
4 Name | size: Size
4 Maya R. | size: M
5 "Reyes | size: 10
4 Theo K.  | size: large
4 Luis M. | size: med
```

**Look at the third line.** The row for `"Reyes, Ana"` split into **five** pieces. Her
name came out as half a name with a stray quote mark, and her "size" is `10`, which is
her grade. Every field after the comma slid one place right.

**No error.** If this fed the order, Ana gets a hoodie in size 10.

### Why it is tempting

It works on most rows. Four of the five lines above are correct. If nobody in your test
data has a comma in their name, a note, or an address, you will never see this fail until
the real sheet arrives. **It is the bug that does not crash, wearing a spreadsheet.**

---

## Worked example 1: `csv.DictReader` reads the rules for you

```python
import csv

with open("signups.csv", newline="", encoding="utf-8") as sheet:
    reader = csv.DictReader(sheet)
    for row in reader:
        print(reader.line_num, row["Name"], row["Size"])
```

Output:

```
2 Maya R. M
3 Reyes, Ana L
4  Theo K.  large
5 Luis M. med
```

- `DictReader` reads the header row for you and gives you every other row as a
  dictionary: `row["Size"]`, not `row[2]`. If a column moves, your code still works.
- It handles the quotes. `Reyes, Ana` is one name again, and her size is `L`.
- **`newline=""` is required** whenever you open a CSV file, for reading or writing. It
  lets the csv module handle line endings itself. The last example shows what happens
  without it.
- `reader.line_num` is the line of the file you are on, **header included**. Line 2 is
  the first data row. That is the number a person sees when they open the file to fix a
  row. If you count rows yourself starting at 1, you will be off by one, the header.
- Notice ` Theo K. ` still has its spaces. Reading does not clean. You do.

**Everything is a string:**

```python
import csv

with open("signups.csv", newline="", encoding="utf-8") as sheet:
    for row in csv.DictReader(sheet):
        print(repr(row["Grade"]), type(row["Grade"]).__name__)
        break
```

```
'11' str
```

---

## Worked example 2: clean, never guess, then convert

```python
import csv
import json

SIZES = {"s": "S", "m": "M", "med": "M", "l": "L", "large": "L"}
PAID_WORDS = {"yes", "y"}
UNPAID_WORDS = {"no", "n"}

clean = []
problems = []
with open("signups.csv", newline="", encoding="utf-8") as sheet:
    reader = csv.DictReader(sheet)
    for row in reader:
        size = row["Size"].strip().lower()
        paid = row["Paid"].strip().lower()
        if size not in SIZES:
            problems.append(f"line {reader.line_num}: size {repr(row['Size'])}")
            continue
        if paid not in PAID_WORDS and paid not in UNPAID_WORDS:
            problems.append(f"line {reader.line_num}: paid says {repr(row['Paid'])}")
            continue
        clean.append({"name": row["Name"].strip(), "size": SIZES[size], "paid": paid in PAID_WORDS})

for order in clean:
    print(order)
print(problems)

with open("signups.json", "w", encoding="utf-8") as out:
    json.dump(clean, out, indent=2)

# Check the conversion: every clean row made it, and nothing changed on the way.
with open("signups.json", encoding="utf-8") as check_file:
    converted = json.load(check_file)
print(f"rows read: {len(clean) + len(problems)}, converted: {len(converted)}, needs a person: {len(problems)}")
print("identical after the round trip:", converted == clean)
```

Output:

```
{'name': 'Maya R.', 'size': 'M', 'paid': True}
{'name': 'Reyes, Ana', 'size': 'L', 'paid': True}
{'name': 'Theo K.', 'size': 'L', 'paid': False}
["line 5: paid says 'cash'"]
rows read: 4, converted: 3, needs a person: 1
identical after the round trip: True
```

Everything from Week 10 is in this one program:

- **`.strip().lower()` first.** Spaces and capitals stop mattering before you decide
  anything.
- **A dictionary holds the decisions.** `SIZES` translates every spelling people really
  typed into the one the printer needs. A new spelling is one new entry, not a new `if`.
- **A set holds the yes words.** The only question is "is it one of these."
- **Check with `in` before looking up.** `SIZES.get(size, "M")` would quietly order a
  Medium for anyone whose size you did not recognize.
- **Unknown values go to `problems`, with the line number and what was actually typed.**
  Luis wrote `cash`. Maybe that means paid. Maybe it means he will pay in cash later. The
  program does not know, so it does not decide. A person does.

**Converting** means moving data into a new format without losing anything. Look at what
changed between the CSV and the JSON: `paid` went from the text `yes` to a real `true`,
which JSON can store and CSV cannot. That is the reason to convert. The last two lines
**check** the conversion: every row is accounted for, and loading the JSON back gives
exactly the clean data. A conversion you did not check is a hope.

---

## Worked example 3: writing CSV back out

```python
with open("signups_clean.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.DictWriter(out, fieldnames=["name", "size", "paid"])
    writer.writeheader()
    writer.writerows(clean)
```

The file it writes:

```
name,size,paid
Maya R.,M,True
"Reyes, Ana",L,True
Theo K.,L,False
```

`DictWriter` writes a list of dictionaries, one row each, and puts the quotes back around
`Reyes, Ana` for you. Notice `paid` became the text `True`. CSV has no true or false,
only text. In Lab U5-04 you decide what a person opening this in a spreadsheet should read
there instead.

---

## Two more failures to name before you hit them

### Misspelling a column name

```python
import csv

with open("signups.csv", newline="", encoding="utf-8") as sheet:
    for row in csv.DictReader(sheet):
        print(row["name"])
```

```
    print(row["name"])
          ~~~^^^^^^^^
KeyError: 'name'
```

The header says `Name` with a capital N. Keys are exact. This one crashes, which is the
good outcome. Do not "fix" it with `row.get("name")`, which would print `None` for every
row.

### Forgetting `newline=""` when writing (Windows)

```python
import csv

with open("orders.csv", "w", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["name", "size"])
    writer.writerow(["Maya R.", "M"])
    writer.writerow(["Theo K.", "L"])

with open("orders.csv", newline="", encoding="utf-8") as sheet:
    for row in csv.reader(sheet):
        print(row)
```

Output on Windows:

```
['name', 'size']
[]
['Maya R.', 'M']
[]
['Theo K.', 'L']
[]
```

**No error. An empty row after every real row.** The csv module ends each row with its own
line break, and Windows text mode adds another. Open the file in a spreadsheet and there is
a blank line between every order. On Mac and Linux this particular mistake usually does not
show, which is exactly why code written on one computer breaks on another. Add
`newline=""` every time you open a CSV.

---

## Never drop a row silently

This is the rule for every cleaning program you write, including your data pipeline.

| What the row is | What to do |
|---|---|
| A completely blank row | Skip it. Nothing to report. |
| A second copy of the header | Skip it. Nothing to report. |
| A value you cannot read | Leave it out of the clean data **and** list it with its line number and what was typed. |
| An exact duplicate | Count it once **and** say so. |

At the end, report how many rows were read, how many are clean, and how many need a person.
Somebody should be able to add those numbers up and check your work. A row that disappears
without a word is a hoodie somebody paid for and never gets.

---

## Why the wrong versions are tempting

**`split(",")` is one line and you already know it.** The csv module feels like extra
ceremony until the first comma inside a name.

**Guessing feels helpful.** Defaulting an unknown size to `M` means the program always
produces a complete order. It is complete and wrong.

**The blank-row bug only shows on some computers.** You can write it on a laptop at home
and never see it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **CSV** | Comma separated values. Plain text rows, commas between fields. |
| **Header** | The first row, naming the columns. |
| **Quoted field** | A field wrapped in double quotes because it contains a comma or line break. |
| **`csv.DictReader`** | Reads each row as a dictionary keyed by the header. |
| **`csv.DictWriter`** | Writes dictionaries as rows. Call `.writeheader()` first. |
| **`newline=""`** | Required when opening a CSV. Lets the csv module handle line endings. |
| **`reader.line_num`** | The file line most recently read, header included. |
| **Cleaning** | Turning what people typed into consistent values a program can trust. |
| **Normalize** | Put values into one standard form, such as uppercase size codes. |
| **Converting** | Moving data into another format, such as CSV to JSON, without losing anything. |
| **Round trip** | Write data out, read it back, and check it is identical. |

---

## Self-check

**Question 1.** This line is in a CSV. How many fields does `line.split(",")` give, and how
many does the csv module give? What is the third field in each case?

```
"Okafor, Juno",12,XL,"Paid Friday, cash"
```

**Question 2.** A cleaning program reports `Hoodies to order: 21` from a sheet with 23 data
rows and prints nothing else. Name two things that could have happened to the missing rows,
and the one change that would let a person tell which.

**Question 3.** Your sheet has a `Paid` column containing `yes`, `Y`, `no`, blank, `paid`,
and `venmo sent`. Write the two sets, and say what your program should do with each of the
six values.

---

### Answers

**1.** `split(",")` gives **6** fields: `'"Okafor'`, `' Juno"'`, `'12'`, `'XL'`,
`'"Paid Friday'`, `' cash"'`. Its third field is `'12'`, which is really the grade, the
second column. The csv module gives **4** fields: `'Okafor, Juno'`, `'12'`, `'XL'`, and
`'Paid Friday, cash'`. Its third field is `'XL'`, the size, which is correct.

**2.** They could have been skipped as problems, such as an unreadable size, or dropped as
duplicates, or skipped as blank rows or a repeated header. The change: list every row left
out with its line number and the reason, and print the count of each kind, so the numbers
add up to 23.

**3.** `PAID_WORDS = {"yes", "y", "paid"}` and `UNPAID_WORDS = {"no", "n", ""}`, after
`.strip().lower()`. `yes`, `Y`, and `paid` count as paid. `no` and blank count as unpaid.
`venmo sent` matches neither set, so it goes on the needs-a-person list with its line
number. It probably means paid, and a person should confirm that before the program counts
the money.
