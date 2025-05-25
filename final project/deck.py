import random
from card import Card

class Deck:
    def __init__(self):
    
        self.cards = []
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

        self.shuffle()

    def shuffle(self):
   
        random.shuffle(self.cards)

    def deal_card(self):
 
        if len(self.cards) == 0:
            return None
        return self.cards.pop()