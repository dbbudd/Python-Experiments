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
turn = "P1"

grid = [['.','.','.'],
    ['.','.','.'],
    ['.','.','.']]

board = np.array(grid)





#fig, ax = plt.subplots(1, figsize=(6,6))
fig = plt.figure()
ax = fig.add_subplot(111, xlim = (0,3), ylim = (0,3), xticks = (1,2,3), yticks = (1,2,3))

def draw_shape(xCoord, yCoord, colour):
    rectangle = plt.Rectangle((xCoord,yCoord), 1,1, facecolor=colour)
    ax.add_patch(rectangle)
    rectangle.set_picker(True)

draw_shape(0,0,'none')
draw_shape(0,1,'none')
draw_shape(0,2,'none')

draw_shape(1,0,'none')
draw_shape(1,1,'none')
draw_shape(1,2,'none')

draw_shape(2,0,'none')
draw_shape(2,1,'none')
draw_shape(2,2,'none')



def on_pick(event):
    event.artist.set_facecolor('green')
    fig.canvas.draw()
    
def onclick(event):
    if event.xdata < 1 and event.ydata < 1:
        board[0,0] = "X"
    elif event.xdata < 1 and event.ydata < 2:
        board[0,1] = "X"
    elif event.xdata < 1 and event.ydata < 3:
        board[0,2] = "X"
    #NEXT ROW
    elif event.xdata < 2 and event.ydata < 1:
        board[1,0] = "X"
    elif event.xdata < 2 and event.ydata < 2:
        board[1,1] = "X"
    elif event.xdata < 2 and event.ydata < 3:
        board[1,2] = "X"
    elif event.xdata < 3 and event.ydata < 1:
        board[2,0] = "X"
    elif event.xdata < 3 and event.ydata < 2:
        board[2,1] = "X"
    elif event.xdata < 3 and event.ydata < 3:
        board[2,2] = "X"
    else:
        print("")
    
    

plt.suptitle("Game Board", size = 20)

fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

print(board)



