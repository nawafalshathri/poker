# This is the implementation of the deck and cards including some
# methods that help out.

import random


class Card:

    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
    def __str__(self):
        return str(self.suit) + " of " + str(self.num)
    def getRank(self):
        royals = ["King", "Queen", "Jack"]
        if self.suit in royals:
            if self.suit == "King":
                return "K"
            elif self.suit == "Queen":
                return "Q"
            elif self.suit == "Jack":
                return "J"
        elif self.suit == "Ace":
            return "A"
        elif self.suit == 10:
            return "T"
        else:
            return "" + str(self.suit)

    def getSuit(self):
        suits = ["Heart", "Spade", "Diamond", "Club"]
        if self.num == suits[0] + '\'s':
            return 'h'
        if self.num == suits[1] + '\'s':
            return 's'
        if self.num == suits[2] + '\'s':
            return 'd'
        if self.num == suits[3] + '\'s':
            return 'c'
    def getID(self):
        return self.getRank() + self.getSuit()


class Deck:

    decks = []
    fullDeck = []

    def __init__(self):
        suits = ["Heart", "Spade", "Diamond", "Club"]
        royals = ["King", "Queen", "Jack"]
        num_of_suits = 13

        for i in range(len(suits)):
            self.decks.append(Card("Ace", suits[i] + '\'s'))
            for j in range(2, 1+num_of_suits):
                if 1 < j <= 10:
                    self.decks.append(Card(j, suits[i] + '\'s'))
                else:
                    self.decks.append(Card(royals[j % 3],suits[i] + '\'s'))
        self.fullDeck = self.decks[:]


    def __str__(self):
        string = ""
        for i in range(52):
            string += self.decks[i] + " "
        return string

    def shuffle(self):
        tempdeck = self.decks[:]
        random.shuffle(tempdeck)
        self.decks = tempdeck

    def refill(self):
        self.decks = self.fullDeck[:]