# Messy Sheets: Reading CSV, Cleaning It, and Converting It
---
## Slide 1: Twenty-three rows, and nobody typed the same way
- Sizes typed as M, med, Medium, and m
- Grades typed as 11, 11th, and Junior
- Someone pasted the header in twice
- The printer needs one clean count by size
Speaker notes: The club is ordering hoodies. The sign-up sheet has twenty three rows, filled in by different people, and nobody typed the same way. M, med, Medium. Eleven, eleventh, Junior. Someone pasted a second copy of the header halfway down. The printer needs one number per size by Friday. That gap between what people typed and what a program can use is what cleaning means.
Image: A messy spreadsheet with inconsistent cells highlighted in accent blue.
---
## Slide 2: A CSV is text with rules
- One row per line, commas between fields
- The first row is usually the header
- A field with a comma inside is wrapped in quotes
- Everything arrives as a string
Speaker notes: CSV stands for comma separated values, and every spreadsheet can export it. It looks like you could split each line on commas. The rule that breaks that idea is the third bullet. When a field contains a comma, like a name written last comma first, the whole field is wrapped in double quotes. And every value, even a number, comes in as text, which is the Unit 1 lesson one more time.
Image: A single CSV line with each field boxed and one quoted field containing a comma.
---
## Slide 3: Watch this: split on commas
```python
sheet = open("signups.csv", encoding="utf-8")
for line in sheet:
    parts = line.strip().split(",")
    print(len(parts), parts[0], "| size:", parts[2])
sheet.close()
```
```
4 Name | size: Size
4 Maya R. | size: M
5 "Reyes | size: 10
4 Theo K.  | size: large
4 Luis M. | size: med
```
Speaker notes: Look at the third line of output. The row for Reyes comma Ana split into five pieces, so the name is half a name with a stray quote, and her size came out as ten, which is her grade. No error. Every field after the comma shifted one place. If this fed an order, Ana would get a hoodie in size ten.
Image: None. This slide is code.
---
## Slide 4: The csv module knows the rules
```python
with open("signups.csv", newline="", encoding="utf-8") as sheet:
    reader = csv.DictReader(sheet)
    for row in reader:
        print(reader.line_num, row["Name"], row["Size"])
```
```
2 Maya R. M
3 Reyes, Ana L
4  Theo K.  large
5 Luis M. med
```
Speaker notes: DictReader reads the header for you and gives you each row as a dictionary, keyed by column name. It handles the quotes, so Reyes comma Ana is one name again with the right size. newline equals empty string is required when you open a CSV. line num is the line of the file you are on, header included, which is the number a person will look for when they go to fix a row.
Image: None. This slide is code.
---
## Slide 5: Cleaning is deciding, and a dictionary holds the decisions
```python
SIZES = {"s": "S", "m": "M", "med": "M", "l": "L", "large": "L"}
PAID_WORDS = {"yes", "y"}
UNPAID_WORDS = {"no", "n"}

size = row["Size"].strip().lower()
if size not in SIZES:
    problems.append(f"line {reader.line_num}: size {repr(row['Size'])}")
else:
    clean_size = SIZES[size]
```
Speaker notes: Strip and lower first, so capitals and stray spaces stop mattering. Then a dictionary translates every spelling people really typed into the one the printer needs. A set holds the words that mean paid. And anything you do not recognize goes to a problems list with its line number. Cleaning never guesses. A row you drop without saying so is a hoodie somebody paid for and never gets.
Image: None. This slide is code.
---
## Slide 6: Write it back out, and convert it
```python
with open("signups_clean.csv", "w", newline="", encoding="utf-8") as out:
    writer = csv.DictWriter(out, fieldnames=["name", "size", "paid"])
    writer.writeheader()
    writer.writerows(clean)

with open("signups.json", "w", encoding="utf-8") as out:
    json.dump(clean, out, indent=2)
```
Speaker notes: DictWriter writes your list of dictionaries back to CSV, quoting any field with a comma for you. Then one json dump converts the same clean data to JSON, where paid becomes real true and false instead of text. Moving data from one format to another without losing anything is called converting, and it is one of this unit's competencies.
Image: None. This slide is code.
---
## Slide 7: Forget newline and every other row is blank
```
['name', 'size']
[]
['Maya R.', 'M']
[]
['Theo K.', 'L']
[]
```
- Writing CSV on Windows without newline=""
- Every row ends with an extra line break
- Excel shows a blank row between each order
Speaker notes: This one is specific to Windows, which is what our lab runs. Open a CSV for writing without newline equals empty string, and the csv module's line ending gets doubled. Read the file back and every other row is empty. Open it in a spreadsheet and there is a blank line between every order. Add newline equals empty string every time you open a CSV, reading or writing.
Image: None. The output is the content.
---
## Slide 8: Never drop a row silently
- Blank rows and a pasted header: skip, no report needed
- Unreadable values: list with line number and reason
- Duplicates: count once, and say so
- Report how many rows went where
Speaker notes: Here is the rule for the whole pipeline. Some rows are safe to skip quietly, like a blank line or a second copy of the header. Every other row that does not make it into your clean data gets listed with its line number and a reason a person can act on. At the end, say how many rows were clean and how many need a person. Somebody should be able to check your numbers.
Image: A sorting diagram with three bins labelled clean, skipped, and needs a person.
---
## Slide 9: What you are about to build
- Lab U5-04: the hoodie order cleanup
- Clean 23 messy rows into a printer order
- Convert to clean CSV and JSON
- Build 2: text adventure v3 due, with paired demos
Speaker notes: Build one is the Hoodie Order lab. The real messy sheet, with every problem on slide one and a few more. You produce the printer's count by size and color, the treasurer's paid and unpaid totals, a clean CSV, a JSON file, and a needs a person list with line numbers. Build two is the finish line for text adventure version three. Finish your tests and README, then demo it to a partner and break your save three ways. It is due at the end of the block.
Image: A clean order table beside a short needs a person list, navy and accent blue.
