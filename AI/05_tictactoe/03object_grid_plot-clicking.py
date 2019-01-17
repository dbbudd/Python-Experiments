#!/usr/bin/env python

import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class gameboard(object):
    
    def __init__(self):
        #player 1 puts a "X", player 2 puts a "O"
        self.g = [[0,0,0],[0,0,0],[0,0,0]]
        self.grid = np.array(self.g)
        self.turn = True
        self.state = True
        print(self.grid)    
    
    def drawGrid(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, xlim=(0,3), ylim = (0,3))
        
        self.myCells = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        for i in self.myCells:
            if self.grid[i] == 1:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="red")
                ax.add_patch(cell)
                cell.set_picker(True)
            elif self.grid[i] == 2:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="blue")
                ax.add_patch(cell)
                cell.set_picker(True)
            else:
                cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="none")
                ax.add_patch(cell)
                cell.set_picker(True)
        
        
        
        def setMarker():
            x = 0
            if self.turn == True:
                x = 1
                self.turn = False
            else:
                x = 2
                self.turn = True
            return x
        
        def onclick(event):
            marker = setMarker()
            if event.xdata <1 and event.ydata <1:
                marker = setMarker()
                self.grid[0,0] = marker
            elif event.xdata <1 and event.ydata <2:
                marker = setMarker()
                self.grid[0,1] = marker
            elif event.xdata < 1 and event.ydata < 3:
                marker = setMarker()
                self.grid[0,2] = marker
            elif event.xdata < 2 and event.ydata < 1:
                marker = setMarker()
                self.grid[1,0] = marker
            elif event.xdata < 2 and event.ydata < 2:
                marker = setMarker()
                self.grid[1,1] = marker
            elif event.xdata < 2 and event.ydata < 3:
                marker = setMarker()
                self.grid[1,2] = marker
            elif event.xdata < 3 and event.ydata < 1:
                marker = setMarker()
                self.grid[2,0] = marker
            elif event.xdata < 3 and event.ydata < 2:
                marker = setMarker()
                self.grid[2,1] = marker
            elif event.xdata < 3 and event.ydata < 3:
                marker = setMarker()
                self.grid[2,2] = marker
            else:
                print("")
            
        def on_pick(event):
            self.myCells = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
            for i in self.myCells:
                if self.grid[i] == 1:
                    cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="red")
                    ax.add_patch(cell)
                    cell.set_picker(True)
                elif self.grid[i] == 2:
                    cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="blue")
                    ax.add_patch(cell)
                    cell.set_picker(True)
                else:
                    cell = mpatches.Rectangle((i), 1, 1, alpha=1, facecolor="none")
                    ax.add_patch(cell)
                cell.set_picker(True)
            
            '''
            colour = "blue"
            event.artist.set_facecolor(colour)
            '''
            fig.canvas.draw()
            
        fig.canvas.mpl_connect('pick_event', on_pick)
        fig.canvas.mpl_connect('button_press_event', onclick)
        
        plt.show()

board = gameboard()
board.drawGrid()
#board.gamestate(board.turn)
print(board.grid)