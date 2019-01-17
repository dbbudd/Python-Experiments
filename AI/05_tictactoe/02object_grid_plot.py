#!/usr/bin/env python

import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class gameboard(object):    
    def __init__(self):
        #player 1 puts a "X", player 2 puts a "O"
        self.g = [[1,0,1],[0,0,2],[0,2,0]]
        self.grid = np.array(self.g)
        print(self.grid)
    
    def drawGrid(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, xlim=(0,3), ylim = (0,3))
        
        self.myCells = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        for i in self.myCells:
            if self.grid[i] == 1:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="red")
                ax.add_patch(cell)
            elif self.grid[i] == 2:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="blue")
                ax.add_patch(cell)
            else:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="none")
                ax.add_patch(cell)
        
        plt.show()


board = gameboard()
board.drawGrid()