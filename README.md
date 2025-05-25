# Blackjack Royale – A Terminal-Based Card Game in Python

This is a simple Blackjack (21-point) game I built using Python. It runs entirely in the terminal. The rules are based on the classic casino version: you play against a dealer and try to get as close to 21 as possible without busting. To make things more fun, I added a scoring system, betting, medal achievements, and even autosaving.

##  What can you do?

- You start with 100 points. Before each round, you place a bet.
- Win the round → gain your bet amount. Lose → subtract it.
- Reach 200, 300, or 500 points and you’ll unlock medals.
- You can play as many rounds as you want in one session.
- Your score, medals, 和 win/loss record are saved automatically, so you can pick up where you left off next time.

## 📁 Project structure
  ├── card.py        # A single card
  ├── deck.py        # Full deck logic
  ├── player.py      # Hand, score, medals
  ├── game.py        # Core gameplay flow
  ├── storage.py     # Save/load logic
  ├── main.py        # Run this to start
  └── savefile.json  # Save file
