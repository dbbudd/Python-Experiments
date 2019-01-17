#!/usr/bin/env python

import matplotlib.pyplot as plt



class Dice(object):
    def __init__(self, value = 1):
        self.value = value

class Player(Dice):
    def __init__(self):
        Dice.__init__(self)
        self.tally = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    
    def rollDice(self):
        import random
        #change the value of the dice
        Dice.value = random.randint(1,6)
        print(Dice.value)
    
    def runTest(self, n):
        self.n = n
        for i in range(n):
            self.rollDice()
            self.tally[Dice.value] = self.tally[Dice.value] + 1
        print(self.tally)
        
    def plotTally(self):
        import matplotlib.pyplot as plt
        #plot the frequencies
        plt.bar(range(len(self.tally)), self.tally.values(), align='center', color='red')
        plt.show()
        
    def realtimeTally(self, n, colour):

        
        import time
        
        #set the axis and draw the initial graph
        plt.axis([0, 6, 0, 100])
        plt.ion()
        plt.show()
        
        for i in range(n):
            
            #roll the Dice and record the value in the tally
            self.rollDice()
            self.tally[Dice.value] = self.tally[Dice.value] + 1
            
            plt.bar(range(len(self.tally)), self.tally.values(), align='center', color=colour)
            plt.draw()
            time.sleep(0.05)

Player1 = Player()
Player2 = Player()

Player1.realtimeTally(50, "red")
Player2.realtimeTally(50, "blue")

