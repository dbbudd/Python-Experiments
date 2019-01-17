#!/usr/bin/env python

import numpy as np
import random
import matplotlib.pyplot as plt

# Make the board
# Set some basic parameters

#create a 3x3 grid
board_x = 3
board_y = 3
trials = 10000


board = np.zeros((board_y, board_x), dtype=int)
print(board)


gs1 = plt.GridSpec(3,3)
gs1.update(left=0.55, right=0.98, hspace=0.05)


ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])

ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

ax7 = plt.subplot(gs1[2,0])
ax8 = plt.subplot(gs1[2,1])
ax9 = plt.subplot(gs1[2,2])



plt.suptitle("An overall title", size = 20)

plt.show()