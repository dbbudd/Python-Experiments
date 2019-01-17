#!/usr/bin/env python

"""
Hypothesis is that the centre rows and columns are better because the aircraft carier must be there somehwere, because it's so long.
Human intuition about placement is obviously a factor too, but we'll worry about that later
"""


import numpy as np
import random
import matplotlib

import matplotlib.pyplot as plt

# Make the board
# Set some basic parameters
boats = [2,3,3,4,5]
board_x = 10
board_y = 10
trials = 10000


board = np.zeros((board_y, board_x), dtype=int)
print(board)


# Make some boats
def make_board():
    board = np.zeros((board_y, board_x), dtype=int)
    for boat in boats:
        # Decide a direction, True is N-S, False is E-W
        #direction = np.random.choice([True, False])
        direction = np.random.sample([True, False])
        
        #Decide a position, accounting for the length of boat
        if direction == True: #then N-S
            while True:
                endpoint_row = np.random.randint(board_y - boat + 1)
                endpoint_col = np.random.randint(board_x)
                
                if np.sum(board[endpoint_row:endpoint_row + boat, endpoint_col]) > 0:
                    continue
                else:
                    for i in range(boat):
                        board[endpoint_row + i, endpoint_col] = 1
                    break
        else: #then E-W
            while True:
                endpoint_row = np.random.randint(board_y)
                endpoint_col = np.random.randint(board_x - boat + 1)
                
                if np.sum(board[endpoint_row, endpoint_col:endpoint_col + boat]) > 0:
                    continue
                else:
                    for i in range(boat):
                        board[endpoint_row, endpoint_col + i] = 1
                    break
    return board

print (make_board())


#Do it lots of times
'''
Make the board lots of times, and simply add up the ship position over time.  Then we can normalise to the number of tirals for probabilities
'''

all_boards = np.zeros((board_y, board_x), dtype=float)
for i in range(trials):
    all_boards += make_board()
print(all_boards)


# Graphically display results

plt.imshow(all_boards)
plt.show()

# We'll normalise to the number of trials to get probabilities
np.set_printoptions(precision=2)
probs = np.zeros((board_y, board_x), dtype=float)
probs = all_boards / trials
print(probs)

# W can also finesse the plot a bit, e.g. with different colourmap,a dn without interpolation (to see each square)

plt.figure(figsize=(8,8))
plt.imshow(probs, cmap=plt.get_cmap('autumn_r'), interpolation='nearest')
plt.colorbar(shrink=0.75)
plt.title('Battleship Probabilities', size=18)
plt.yticks(range(board_y), [chr(65 + x) for x in xrange(board_y)])
plt.xticks(range(board_x), [x + 1 for x in range(board_x)])
plt.show()
