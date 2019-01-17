#!/usr/bin/env python

import numpy as np

g = [['1','2','0'],
    ['2','4','5'],
    ['2','5','6']]

grid = np.array(g)



grid[0,0] = "X"
'''
print(grid[0,0]) #A1
print(grid[0,1]) #A2
print(grid[0,2]) #A3

print(grid[1,0]) #B1
print(grid[1,1]) #B2
print(grid[1,2]) #B3

print(grid[2,0]) #C1
print(grid[2,1]) #C2
print(grid[2,2]) #C3
'''

column = 0
#returns specific triangles
print(np.diag(grid, column))

print(np.trace(grid, 1))

