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