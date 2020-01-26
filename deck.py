from card import Card
from constants import SUITS, RANKS

class Deck:
    def __init__(self):
        self.Cards = []
        self.InitializeDeck()
        self.Shuffle()

    def InitializeDeck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.Cards.append(Card(suit, rank))

    def Shuffle(self):
        import random
        return random.shuffle(self.Cards)

    def Deal(self):
        return self.Cards.pop()

    def RemainingCards(self):
        return len(self.Cards)
