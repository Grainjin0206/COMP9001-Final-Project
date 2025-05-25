import json
import os

SAVE_FILE = "savefile.json"

def save_game(player):

    data = {
        "score": player.score,
        "medals": player.medals,
        "wins": player.wins,
        "losses": player.losses,
        "draws": player.draws
    }
        
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def load_game(player):
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            player.score = data.get("score", 100)
            player.medals = data.get("medals", [])
            player.wins = data.get("wins", 0)
            player.losses = data.get("losses", 0)
            player.draws = data.get("draws", 0)
    else:
        print(" No save file found. Starting a new game.")