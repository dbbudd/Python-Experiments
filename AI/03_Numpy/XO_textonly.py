#!/usr/bin/env python
import numpy as np
import itertools


#player 1 puts a "X", player 2 puts a "O"
g = [['.','.','.'],
    ['.','.','.'],
    ['.','.','.']]

isComplete = False
turn = True

grid = np.array(g)

X_Win = [['X'], ['X'], ['X']]
Y_Win = [['O'], ['O'], ['O']]

def complete(grid):
    for row in grid:
        for cell in row:
            if cell == ".":
                pass
            else:
                print("draw")

def checkColumns(grid, X, O, isComplete):
    length = len(grid)
    if isComplete == False:
        for column in range(0, length):
            the_column = grid[:, column]
            if (the_column == X).all():
                print("X Wins")
                isComplete = True
            elif (the_column == O).all():
                print("O Wins")
                isComplete = True
            else:
                complete(grid, isComplete)


def checkRows(grid, X, O, isComplete):    
    length = len(grid)
    if isComplete == False:
        for row in range(0,length):
            the_row = grid[row, :]
            if (the_row == X).all():
                print("X Wins")
                isComplete = True
            elif (the_row == O).all():
                print("O Wins")
                isComplete = True
            else:
                complete(grid)

def checkDiag(grid, X, O, isComplete):
    if isComplete == False:
        if (grid.diagonal(0) == X).all() or (np.flipud(grid).diagonal(0) == X).all():
            print("X Wins")
            isComplete = True
        elif (grid.diagonal(0) == O).all() or (np.flipud(grid).diagonal(0) == O).all():
            print("O Wins")
            isComplete = True
        else:
            complete(grid, isComplete)

print(grid)



def Play(turn):
    player = input("Enter grid reference: ")
    if turn == True:
        grid[player[0],player[1]] = "X"
        turn = False
        print(grid)
        checkDiag(grid, X_Win, Y_Win, isComplete)
        checkRows(grid, X_Win, Y_Win, isComplete)
        checkColumns(grid, X_Win, Y_Win, isComplete)
        Play(turn)
    elif player == "Q":
        print("end")
    else:
        grid[player[0], player[1]] = "O"
        turn = True
        print(grid)
        checkDiag(grid, X_Win, Y_Win, isComplete)
        checkRows(grid, X_Win, Y_Win, isComplete)
        checkColumns(grid, X_Win, Y_Win, isComplete)
        Play(turn)

#Play(turn)

