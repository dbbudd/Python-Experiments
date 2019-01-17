#!/usr/bin/env python

import numpy as np
import random
import math

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches

# Make the board
# Set some basic parameters

#create a 3x3 grid
board_x = 3
board_y = 3
turn = "P1"

grid = [['.','.','.'],
    ['.','.','.'],
    ['.','.','.']]

board = np.array(grid)





#fig, ax = plt.subplots(1, figsize=(6,6))
fig = plt.figure()
ax = fig.add_subplot(111, xlim = (0,3), ylim = (0,3), xticks = (1,2,3), yticks = (1,2,3))
rec = plt.Rectangle([0,0], 3, 3, facecolor='none')
ax.add_patch(rec)
rec.set_picker(True)



def draw_shape(xCoord, yCoord):
    rectangle = plt.Rectangle((xCoord,yCoord), 1,1, facecolor="green")
    ax.add_patch(rectangle)
    fig.canvas.draw()


    
def onclick(event):
    #round value down to nearest coordinate
    x = math.trunc(event.xdata)
    y = math.trunc(event.ydata)
    
    draw_shape(x,y)
    board[x,y] = "X"
    

plt.suptitle("Game Board", size = 20)

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

print(board)



