# Tables in Code: Lists of Dictionaries and Calculated Fields
---
## Slide 1: The coach wants points per game, not points
- The stat sheet has games and total points
- Nobody typed points per game
- The coach wants it for every player
- And totals for each position
Speaker notes: The JV coach has a season of stats. Games played, total points, rebounds. What the coach actually wants is points per game, and the totals for guards against forwards. Nobody typed those numbers anywhere. Your program has to calculate them. A number you compute from other columns is called a calculated field, and every real report is full of them.
Image: A simple stat sheet with one empty highlighted column labelled per game.
---
## Slide 2: A list of dictionaries is a table
- Each dictionary is one row
- Each key is a column name
- The list holds the rows in order
- players[1]["name"] reads row 1, column name
Speaker notes: Put the last two days together. One player is a dictionary, because you look up their points by the name points. The team is a list of those dictionaries, because the roster has an order. That shape is a table. Row by position, column by name. It is exactly what a spreadsheet, a CSV file, and a website table turn into when a program reads them.
Image: A spreadsheet grid with one row outlined as a dictionary and the whole grid outlined as a list.
---
## Slide 3: Calculated fields in a loop
```python
players = [
    {"name": "Jaylen", "position": "Guard", "games": 12, "points": 138},
    {"name": "Sofia", "position": "Forward", "games": 12, "points": 101},
    {"name": "Dev", "position": "Center", "games": 11, "points": 92},
    {"name": "Hannah", "position": "Guard", "games": 12, "points": 77},
]

total_points = 0
for player in players:
    player["ppg"] = player["points"] / player["games"]
    total_points += player["points"]
    print(f"{player['name']:<8} {player['ppg']:.1f} points per game")
print("Team points:", total_points)
```
Speaker notes: One loop does two jobs. It adds a new key, ppg, to each player, which is the calculated field. And it adds each player's points to a running total, which is the accumulator you have written since Unit 3. The f string formats the result to one decimal place.
Image: None. This slide is code.
---
## Slide 4: What it prints
```
Jaylen   11.5 points per game
Sofia    8.4 points per game
Dev      8.4 points per game
Hannah   6.4 points per game
Team points: 408
```
Speaker notes: Check one by hand before you trust any of them. Jaylen, one hundred thirty eight points over twelve games, is eleven and a half. The total, four hundred eight, is the four point totals added up. A report you have not checked by hand at least once is a guess with nice formatting.
Image: None. This slide is code.
---
## Slide 5: Group rows into a dictionary of lists
```python
by_position = {}
for player in players:
    if player["position"] not in by_position:
        by_position[player["position"]] = []
    by_position[player["position"]].append(player["name"])

print(by_position)
# {'Guard': ['Jaylen', 'Hannah'], 'Forward': ['Sofia'], 'Center': ['Dev']}
```
Speaker notes: Grouping is the counting pattern with a list instead of a number. If the position has no list yet, start an empty one. Then append the player to it. The result is a dictionary where each key holds a list. The version 3 text adventure stores the items left in each room exactly this way.
Image: None. This slide is code.
---
## Slide 6: Watch this: a report with one row per player
```python
report = []
row = {}
for player in players:
    row["name"] = player["name"]
    row["ppg"] = round(player["points"] / player["games"], 1)
    report.append(row)

for line in report:
    print(line)
```
Speaker notes: I want a separate report list with only the name and points per game. I will make a row dictionary, fill it in for each player, and append it. Read it once. It looks reasonable. Predict what the three lines will say.
Image: None. This slide is code.
---
## Slide 7: Every row is Dev
```
{'name': 'Dev', 'ppg': 8.4}
{'name': 'Dev', 'ppg': 8.4}
{'name': 'Dev', 'ppg': 8.4}
```
- One dictionary was made, above the loop
- The list holds that same dictionary three times
- Each pass overwrote it
- Fix: row = {} goes inside the loop
Speaker notes: Three rows, all Dev. There was only ever one dictionary. Appending it did not copy it. The list got three references to the same dictionary, and every pass through the loop wrote over it, so at the end all three show the last player. No error. This is the name tag idea from Unit 1 coming back: two names can point at one thing. Move row equals empty braces inside the loop so each pass makes a brand new dictionary.
Image: Three arrows from three list slots all pointing at one single dictionary box.
---
## Slide 8: Guard the calculation, not the report
- A player with 0 games crashes the division
- ZeroDivisionError stops the whole report
- Check games before dividing
- Decide what the report should say instead
Speaker notes: One more failure to name before you hit it. An injured player with zero games makes points divided by games crash with ZeroDivisionError, and one player takes down the whole report. Put the check inside the function that divides, and decide on purpose what that player's line should show. Zero is one choice. Not played is another. Either is fine if you chose it.
Image: A report with one row reading not played, the rest filled in.
---
## Slide 9: What you are about to build
- Lab U5-02: the JV season report
- Points and rebounds per game, shooting percent
- Totals by position, top scorer
- Build 2: v3 state as one dictionary
Speaker notes: Build one is the Team Report lab. Ten players, three calculated fields each, team totals, a top scorer, and a by-position summary, printed in lined-up columns. Step five makes you write the shared dictionary bug on purpose and record what the report showed. Build two moves your text adventure's game state into one dictionary, with a dictionary of lists for the items left in each room.
Image: A lined-up terminal report with a highlighted calculated column, navy and accent blue.
