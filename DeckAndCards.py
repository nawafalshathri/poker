# This is the implementation of the deck and cards including some
# methods that help out.

import random


class Card:

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
    def __str__(self):
        return self.suit + " of " + str(self.num)

class Deck:

    decks = []

    def __init__(self):
        suits = ["Heart", "Spade", "Diamond", "Club", "Star"]
        num_of_suits = 16

        for i in range(len(suits)):
            for j in range(1, 1+num_of_suits):
                self.decks.append(Card(suits[i], j).__str__())

    def __str__(self):
        string = ""
        for i in range(52):
            string += self.decks[i] + " "
        return string

    def shuffle(self):
        tempdeck = self.decks[:]
        random.shuffle(tempdeck)
        self.decks = tempdeck



