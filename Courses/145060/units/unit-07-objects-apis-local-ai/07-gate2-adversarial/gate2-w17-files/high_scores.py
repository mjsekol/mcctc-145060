# high_scores.py
#
# Shows the arcade high scores for a game, from the score API. Written from the
# spec in the Gate 2 handout. It runs and looks reasonable. Find what is wrong.
#
# Start the fixture first:  python score_server.py
# Then:                     python high_scores.py pixel-racer

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:8060"
API_KEY = "NOT-A-REAL-KEY-arcade-4417"      # sent with every request
TIMEOUT = 5

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def get_scores(game):
    """Fetch the scores for a game. Returns the list, or an empty list on any failure."""
    url = f"{BASE_URL}/api/games/{game}/scores"
    request = urllib.request.Request(url, headers={"X-Key": API_KEY})
    try:
        with DIRECT.open(request, timeout=TIMEOUT) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data["scores"]
    except urllib.error.HTTPError as error:
        if error.code == 404:
            print("That game was not found. Check the name.")
        else:
            print("The score server had a problem. Try again later.")
        return []
    except Exception:
        return []


def top_three(scores):
    # Return the top three scores, highest first.
    ranked = sorted(scores, key=lambda s: s["points"], reverse=True)
    return ranked[:2]


def show(game):
    scores = get_scores(game)
    if not scores:
        print("No scores yet. Be the first.")
        return
    # leaders: the players at the top of the board
    leaders = get_scores(game)
    print(f"{game}: {len(leaders)} scores on record")
    print("Top three:")
    for entry in top_three(scores):
        print(f"  {entry['player']:<12} {entry['points']}")


def main():
    game = sys.argv[1] if len(sys.argv) > 1 else "pixel-racer"
    show(game)


if __name__ == "__main__":
    main()
