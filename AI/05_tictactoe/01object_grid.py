#!/usr/bin/env python

import numpy as np
import itertools

class gameboard(object):    
    def __init__(self):
        #player 1 puts a "X", player 2 puts a "O"
        self.g = [[0,0,0],[0,0,0],[0,0,0]]
        self.grid = np.array(self.g)
        print(self.grid)
    
    def checkWin(self):
        if ((self.grid.diagonal(0) == 1).all()) or ((np.flipud(self.grid).diagonal(0) == 1).all()):
            print("X Wins")
        elif ((self.grid.diagonal(0) == 2).all()) or ((np.flipud(self.grid).diagonal(0) == 2).all()):
            print("0 Wins")
        else:
            for i in range(0,len(self.grid)):
                self.column = self.grid [:, i]
                self.row = self.grid [i, :]
                if (self.row.all() == 1) or (self.column.all() == 1):
                    print("X Wins")
                elif (self.row.all() == 2) or (self.column.all() == 2):
                    print("O Wins")
                else:
                    continue
            print("Keep Playing!")


board = gameboard()
board.checkWin()