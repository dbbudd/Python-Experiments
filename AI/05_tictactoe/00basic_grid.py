#!/usr/bin/env python

import numpy as np
import itertools


#player 1 puts a "X", player 2 puts a "O"
g = [[0,2,0],
    [0,0,0],
    [0,0,0]]

grid = np.array(g)
print(grid)

print(grid[0,1])