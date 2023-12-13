from random import shuffle
import sys
class Card:
    suits = ['♣','♠','♥','♦']
    ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    def __init__(self,s,r):
        self.suit = s
        self.rank = r
    def __int__(self):
        r = self.ranks[self.rank]
        if r == "J" or r == "Q" or r == "K":
            r = 10
        elif r == "A":
            r = 1
        return int(r)

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1,14):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def draw(self):
        if len(self.cards) == 0:
            return 
        return self.cards.pop()

player1 = Deck()
print(player1.draw())
