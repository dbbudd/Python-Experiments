import random


class Dealer():
    def __init__(self):
        self.cards = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
        print(self.cards)
    
    def shuffleDeck(self):
        random.shuffle(self.cards)
        #print(self.cards)
        print("The Deck has been shuffled")
        
    def dealCard(self):
        card = self.cards.pop()
        return card
    
    def countDeck(self):
        length = len(self.cards)
        return length

class Player():
    def __init__(self):
        #run any time dice() is used
        self.cards = []
        
    def hit(self, deck):
        print("Hit me!")
        self.cards.append(deck)
    
    def showHand(self):
        print(self.cards)
    
    def sumCards(self):
        self.total = sum(self.cards)
        return self.total
    
 
def prob(sumHand, cards):
    count = 0
    for item in cards:
        if item <= (21-sumHand):
            count +=1
    length = len(cards) 
    probability = "Probability of getting 21 is " + str(100.0 * count / length) + " %"
    return probability


myDealer = Dealer()
Player1 = Player()
Player2 = Player()
House = Player()


myDealer.shuffleDeck()

House.hit(myDealer.dealCard())
Player1.hit(myDealer.dealCard())
Player2.hit(myDealer.dealCard())

print(myDealer.countDeck())


sumHand = Player1.sumCards()
cards = myDealer.cards

print(sumHand)
print(cards)

print(prob(sumHand, cards))

