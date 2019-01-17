#!/usr/bin/env python

import numpy as np
import random

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches

# Make the board
# Set some basic parameters

#create a 3x3 grid
board_x = 3
board_y = 3


board = np.zeros((board_y, board_x), dtype=int)
print(board)


fig, ax = plt.subplots(1, figsize=(6,6))

def draw_shape(xCoord, yCoord, colour):
    art = mpatches.Rectangle((xCoord, yCoord), 1, 1, alpha = 1, facecolor=colour)
    ax.add_patch(art)



draw_shape(0,0,'none')
draw_shape(0,1,'none')
draw_shape(0,2,'none')

draw_shape(1,0,'none')
draw_shape(1,1,'none')
draw_shape(1,2,'none')

draw_shape(2,0,'none')
draw_shape(2,1,'none')
draw_shape(2,2,'none')


#set the limit of the axes to 0,3 both on x and y
ax.set_xlim(0,3)
ax.set_ylim(0,3)
ax.set_xticks([1,2,3])
ax.set_yticks([1,2,3])


plt.suptitle("Game Board", size = 20)
plt.show()





