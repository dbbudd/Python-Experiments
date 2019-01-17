#!/usr/bin/env python



class Dice(object):
    def __init__(self):
        import random
        #run any time dice() is used
        self.player = random.randrange(6)
        self.computer = random.randrange(6)
    
    def compare(self):
        print(self.player)
        print(self.computer)
        
        if self.player == self.computer:
            print("you win")
        else:
            print("you lose")
    
myDice = Dice()
myDice.compare()