class Player:
    def __init__(self, name="Player", score=100):
        self.name = name
        self.hand = []
        self.score = score
        self.medals = []
        self.current_bet = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def add_card(self, card):
        self.hand.append(card)

    def get_total(self):
        total = 0
        for card in self.hand:
            total += card.get_value()
        return total

    def clear_hand(self):
        self.hand = []

    def __str__(self):
        return f"{self.name} | Hand: {[str(c) for c in self.hand]} | Total: {self.get_total()} | Score: {self.score}"