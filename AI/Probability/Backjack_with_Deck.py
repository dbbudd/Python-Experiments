#!/usr/bin/env python

#!/usr/bin/env python
import random

class Card(object):
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "|Suit: %s Rank: %s|" % (self.suit, self.rank)

    def __repr__(self):
        return "%s(%s %s)" % (self.__class__, self.suit, self.rank)
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Deck(Card):
    def __init__(self):
        self.cards = []
        Card.__init__(self)
        for suit in Card.suit_names:
            for rank in Card.rank_names:
                self.cards.append(Card(suit,rank))

    def deal(self):
        random.shuffle(self.cards)
        return self.cards.pop()

    def hit(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Player(object):

    def __init__(self, isDealer):
        self.hand1 = []
        self.hand2 = []
        self.xy = "cat"
        self.twoHands = False
        self.value = 0
        self.value2 = 0
        self.hasLost = False
        self.isDealer = isDealer
        
    def initalCards(self, cards):
        if self.isDealer == False: print("These are your staring cards:", cards[0], cards[1])
        if cards[0].rank == cards[1].rank and self.isDealer == False:
            print("\nYou got two cards of the same rank!!")
            print("You can play them as two seperate hands or just one.")
            if input("Do you want to play with two hands?(y,n)>>").lower() == "y":
                self.twoHands = True
                self.hand1.append(cards[0])
                self.value = self.valueOfCard(cards[0], self.isDealer)

                self.hand2.append(cards[1])
                self.value2 = self.valueOfCard(cards[1], self.isDealer)
                
            else:
                self.hand1 += cards
                self.value = self.valueOfCard(cards[0], self.isDealer)
                self.value = self.valueOfCard(cards[1], self.isDealer)
                self.checkLost()
        else:
            self.hand1 += cards
            self.value += self.valueOfCard(cards[0], self.isDealer)
            self.value += self.valueOfCard(cards[1], self.isDealer)
            self.checkLost()

    def addCard(self, card):
        if self.twoHands:
            print("\nWhich hand do you want to add your cards to?")
            if input("Hand 1(1) Hand 2(2)>>") == '1':
                self.hand1.append(card)
                self.value += self.valueOfCard(card, self.isDealer)
            else:
                self.hand2.append(card)
                self.value2 += self.valueOfCard(card, self.isDealer)
        else:
            self.hand1.append(card)
            self.value += self.valueOfCard(card, self.isDealer)
            self.checkLost()

    def checkLost(self):
        if self.value > 21 or self.value2 > 21:
                self.hasLost = True

    def valueOfCard(self, card, isDealer=True):
        value = 0
        if card.rank == self.rank_names[0]:
            #ace check with player
            if isDealer:
                value = 1
            else:
                inputInt = int(input("\nYou got an ace, do you want an 11 or a 1?(11,1)>>"))
                if inputInt == 1 or inputInt == 11:
                    value = inputInt
                else:
                    value = 1
        elif card.rank in self.rank_names[-4:]:
            value = 10
        elif card.rank in self.rank_names[1:-4]:
            value = self.rank_names.index(card.rank) + 1
        else:
            value = 0
        return value

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class BlackjackGame(Deck):
    def __init__(self):
        Deck.__init__(self)
        self.shuffle()
        self.player = Player(False)
        self.dealer = Player(True)
        self.roundNum = 0

    def hitGame(self, isDealer=True):
        if isDealer:
            self.dealer.addCard(self.hit())
        else:
            self.player.addCard(self.hit())

    def nextTurn(self, stand=True):
        self.roundNum += 1
        
        self.hitGame(True)#dealer play
        if self.dealer.hasLost:
            self.printScores()
            print("\n<><><><><><>\nPlayer Wins\n<><><><><><>\n")
            return True
        else:
            if stand:
                None
            else:
                self.hitGame(False)
                if self.player.hasLost:
                    self.printScores()
                    print("\n<><><><><><>\nDealer Wins\n<><><><><><>\n")
                    return True
            self.printScores()

    def runGame(self):
        self.dealer.initalCards([self.hit(),self.hit()])
        self.player.initalCards([self.hit(),self.hit()])
        while True:
            self.printOdds()
            standChoice = input("Do you want to stand?(y,n)").lower()
            if game.nextTurn(standChoice=='y'): break

    def printScores(self):
        print("\n Round:", self.roundNum, "Dealer:",self.dealer.value,end + " ")
        if self.player.twoHands:
            print("Player Hand 1:",self.player.value,"Player Hand 2:",self.player.value2)
        else:
            print("Player:",self.player.value)

    def printOdds(self):
        print("\n")
        print("<><><><><>Odds<><><><><>")
        for rank in self.rank_names[:-4]:
            tempCard = Card(self.suit_names[0], rank)
            print(tempCard.rank, "%" + str(calculateOdds(1, (self.player.hand1 + self.player.hand2 + self.dealer.hand1), tempCard)))

        tempCard = Card(self.suit_names[0], self.rank_names[9])
        print(tempCard.rank, "%" + str(calculateOdds(1, (self.player.hand1 + self.player.hand2 + self.dealer.hand1), tempCard)))
        
        print("<><><><><>Odds<><><><><>")
        print("\n")

def calculateOdds(numDecks, playedCards, targetCard):
    #finding num of target
    tempDeck = Deck()
    numOfTarget = 0
    for i in playedCards:
        if i.rank == targetCard.rank:
            numOfTarget += 1
    
    if targetCard.rank in tempDeck.rank_names[-4:]:
        #p = (16*numDeck-numOfTargetPlayed)/(52*numDeck-len(playedCards)) if x = 10
        return ((16*numDecks)-numOfTarget)/((52*numDecks)-len(playedCards))*100
    else:
        #p = (4*numDeck-numOfTargetPlayed)/(52*numDeck-len(playedCards)) if x =/= 10
        return ((4*numDecks)-numOfTarget)/((52*numDecks)-len(playedCards))*100

game = BlackjackGame()
game.runGame()