#!/usr/bin/env python

class Card(object):
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Deck(Card):
    def __init__(self):
        self.cards = []
        Card.__init__(self)
        for suit in Card.suit_names:
            for rank in Card.rank_names:
                self.cards.append({"RANK": rank, "SUIT":suit, "VALUE":0})
        
        for card in self.cards:
            if card["RANK"] == "JACK" or card["RANK"] == "Queen" or card["RANK"] == "King":
                card["VALUE"] = 11
            elif card["RANK"] == "10":
                card["VALUE"] = 10
            elif card["RANK"] == "9":
                card["VALUE"] = 9
            elif card["RANK"] == "8":
                card["VALUE"] = 8
            elif card["RANK"] == "7":
                card["VALUE"] = 7
            elif card["RANK"] == "6":
                card["VALUE"] = 6
            elif card["RANK"] == "5":
                card["VALUE"] = 5
            elif card["RANK"] == "4":
                card["VALUE"] = 4
            elif card["RANK"] == "3":
                card["VALUE"] = 3
            elif card["RANK"] == "2":
                card["VALUE"] = 2
            elif card["RANK"] == "Ace":
                card["VALUE"] = 1
    
    def deal(self):
        import random
        random.shuffle(self.cards)
        return self.cards.pop()
    
    def hit(self):
        return self.cards.pop()


class Player(object):
    def __init__(self):
        self.hand = []
    
    def totalHand(self):
        total = 0
        for card in self.hand:
            total = total + card['VALUE']
        return total

#create instance of objects
myDeck = Deck()
Player1 = Player()
Dealer = Player()

#initial deal
Player1.hand.append(myDeck.deal())
Dealer.hand.append(myDeck.deal())

#first hit
Player1.hand.append(myDeck.hit())
Dealer.hand.append(myDeck.hit())

def checkWinner(play, deal):
    PlayerDiff = 0
    DealerDiff = 0
    PlayerDiff = 21 - play
    DealerDiff = 21 - deal
    
    if play > 21:
        print("dealer wins")
    elif deal > 21:
        print("player wins")
    elif PlayerDiff < DealerDiff:
        print("player wins")
    else:
        print("dealer wins")

    print("Player Total: " + str(Player1.totalHand()))
    print("Dealer Total: " + str(Dealer.totalHand()))
    

checkWinner(Player1.totalHand(), Dealer.totalHand())


