from scipy.misc import imread, toimage
import numpy

# This file also displays the correct path at
# the end in green, which is pretty useful.
# Now to implement this into my Turtle Maze!

EMPTY   = 0
WALL    = 1
VISITED = 2

BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
GREEN = [  0, 255,   0]
BLUE  = [  0,   0, 255]

# I had to edit the maze so it
# actually worked, because of
# the lossy compression...
# So I made it a bmp.
MAZE_NAME = "13x13.bmp"
maze = imread(MAZE_NAME)

def mazeToArray(maze):
	newmaze = []
	startx, starty, endx, endy = [None, None, None, None]
	for i in range(len(maze)):
		x = []
		for j in range(len(maze[i])):
			if list(maze[i][j]) == BLACK:
				x.append(WALL)
			if list(maze[i][j]) == WHITE:
				x.append(EMPTY)
			if list(maze[i][j]) == GREEN:
				startx, starty = j, i
				x.append(EMPTY)
			if list(maze[i][j]) == BLUE:
				endx, endy = j, i
				x.append(EMPTY)
		newmaze.append(x)
	return newmaze, startx, starty, endx, endy

oldmaze = numpy.copy(maze)
maze, startx, starty, endx, endy = mazeToArray(oldmaze)

def search(x, y):
	global maze, endx, endy, oldmaze

	# Check for win
	if x == endx and y == endy:
		return True # woohoo

	# Check if on visited or wall
	if maze[y][x] in (WALL, VISITED):
		return False

	# Set visited
	maze[y][x] = VISITED

	found = False
	if y < len(maze) - 1:
		if search(x, y + 1):
			found = True
	if y > 0:
		if search(x, y - 1):
			found = True
	if x < len(maze[y]) - 1:
		if search(x + 1, y):
			found = True
	if x > 0:
		if search(x - 1, y):
			found = True
	if found:
		# Colour the correct path
		oldmaze[y][x] = GREEN

	return found

print search(startx, starty)

# Display our path
toimage(oldmaze).show()