#!/usr/bin/env python

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(grid)

#print rows
print(grid[0])
print(grid[1])
print(grid[2])


#print columns
for i in range(0,3):
    print(grid[i][0])


#print individual cell
print(grid[2][2])



#create a function to print any column
def column(matrix, i):
    return[row[i] for row in matrix]


print(column(grid, 1))

