import turtle, math, random, sys

turtle.setup(600, 600)
myWindow = turtle.Screen()
myWindow.bgcolor("white")
myWindow.title("Noughts and Crosses v1.0")

t = turtle.Pen()

def fadein():
    t.shape("turtle")
    t.shapesize(random.randint(1, 10), random.randint(1, 10))
    
def fadeout():
    t.shape("classic")
    t.shapesize(1, 1)

class Grid:
    def __init__(self, grid):
        """
        Initialises the Grid object.
        """
        for i in range(2): # Vertical
            t.penup()
            t.goto(-100 + 200 * i, 300)
            t.pendown()
            t.goto(-100 + 200 * i, -300)
        for i in range(2): # Horizontal
            t.penup()
            t.goto(-300, 100 - 200 * i)
            t.pendown()
            t.goto(300, 100 - 200 * i)
        self.grid = grid
        self.currentMove = 1 # Nought
        self.oldGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.updateGrid()
        
    def updateGrid(self):
        """
        Updates the screen display according to the grid.
        Also checks if the game has been won, via checkForWin, and if so,
        calls renderWin and returns True.
        """
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] != self.oldGrid[i][j]: # Prevent redrawing
                    t.setheading(0)
                    t.penup()
                    t.goto(-200 + j * 200, 200 - i * 200) # Go to location
                    t.pendown()
                    if self.grid[i][j] == 1: # Nought
                        t.color("black")
                        t.penup()
                        t.goto(t.xcor(), t.ycor() - 50)
                        t.pendown()
                        t.circle(50)
                    elif self.grid[i][j] == 2: # Cross
                        t.color("black")
                        t.setheading(45)
                        for k in range(4):
                            t.forward(math.sqrt(5000) )
                            t.forward(-math.sqrt(5000))
                            t.right(90)
                    else: # You what?
                        continue
                    # Because self.oldGrid = self.grid yields a pointer
                    self.oldGrid[i][j] = self.grid[i][j]
        winCheck = self.checkForWin()
        if len(winCheck) != 1: # The game is won
            print(["Noughts", "Crosses"][winCheck[0] - 1], "won this time!")
            self.renderWin(winCheck[1]) # The coordinates
            myWindow.onclick(self.exitGame, btn = 1) # Left click again to exit
        elif winCheck[0] == False:
            print ("It's a draw.")
            myWindow.onclick(self.exitGame, btn = 1)
        else:
            return # Ignore
        
    def getClick(self, x, y):
        """
        Updates the grid according to the location of click.
    
        """
        currentX = math.floor((x + 300) / 200)
        currentY = 2 - math.floor((y + 300) / 200)
        
        if (self.grid[currentY][currentX] == 0):
            self.grid[currentY][currentX] = self.currentMove
            self.currentMove = self.currentMove % 2 + 1
            self.updateGrid()
        else: # Oh dear, it's been clicked on.
            for i in range(2, 50): # Make the turtle spaz to say "You did a bad thing!"
                t.shapesize(math.floor(i / 2), math.floor(i))
                t.setheading(random.randint(-i, i))
            t.setheading(0)
            t.shapesize(1, 1)
            
    def checkForWin(self):
        """
        Returns a list.
        Returns [True] if neither have won yet.
        Returns [False] if it is impossible to win.
        Otherwise:
          First element:
            1 if the game of Noughts and Crosses has been won by Noughts;
            2 if the game was won by Crosses;
          Second element:
            [[beginX, beginY], [endX, endY]] - The beginning and end
            coordinates of the win.
        A win is defined as a player getting three Noughts or
        Crosses in a row or diagonal.
        """
        # The != 0 is to ensure that we don't see any lines of blanks.
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return [self.grid[0][i], [[0, i], [2, i]]]
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                return [self.grid[i][0], [[i, 0], [i, 2]]]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            return [self.grid[0][0], [[0, 0], [2, 2]]]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            return [self.grid[0][2], [[0, 2], [2, 0]]]
        
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return [True] # A not-won-yet, as there are still places left
        return [False] # A draw
    
    def renderWin(self, lineCoords):
        """
        Draws a stroke through the winning player's winning line.
        """
        t.penup()
        # Go to location 1
        t.goto(-200 + lineCoords[0][1] * 200, 200 - lineCoords[0][0] * 200)
        t.pendown()
        t.goto(-200 + lineCoords[1][1] * 200, 200 - lineCoords[1][0] * 200)
            
            
    def exitGame(self, x, y): # Dummy
        """
        Exits the game. A dummy function for the left click after game.
        """
        sys.exit(0)
        
t.speed(0) # Fast

grid = Grid([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

myWindow.listen()
myWindow.onclick(grid.getClick, btn = 1) # Left mouse button clicked
myWindow.onkeypress(fadein, "Up")
myWindow.onkeyrelease(fadeout, "Up")

turtle.done()