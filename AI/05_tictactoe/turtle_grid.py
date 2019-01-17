#!/usr/bin/env python

import turtle
import math 
import random 

cellSize = 100
turtleWidth =10
gridColor  = 'Black'
xColor = 'Blue'
oColor = 'Red'
winColor = 'green'
drawColor = 'Gray'

winninTriples = ((0,1,2))


def onclick(x, y):
    print (x, y)

turtle.Screen().onscreenclick(onclick)

pen = turtle.Pen()
pen.width(5)
#the grid is here 

def drawGrid(pen, length, xcoor, ycoor):
    startX = [xcoor,xcoor,xcoor+length, xcoor+(2*length)]
    endX = [xcoor+(3*length), xcoor+(3*length), xcoor+(length),xcoor+(2*length)]
    startY = [ycoor+(2*length),ycoor+length, ycoor, ycoor]
    endY = [ycoor+(2*length), ycoor+length, ycoor+(3*length),ycoor+(3*length)]
    for grid in range(4):
        pen.up()
        pen.goto(startX[grid],startY[grid])
        pen.down()
        pen.goto(endX[grid],endY[grid])
    turtle.done()



drawGrid(pen,100,-40,-50)

board = [0,1,2,
          3,4,5,
          6,7,8]


def theWinnner(grid0,grid1,grid2,grid3,grid4,grid5,grid6,grid7,grid8):
    X = 'X wins'
    O = 'O wins'
    No = 'Draw'
    #this was a code that was given, I am supposed to add on to it and I am not sure how it can be modified and what should I put as the parameters when executing it? 

def drawX(t,x,y,size):
   drawLine(t, x + size/4, y + size/4, x - size/4, y - size/4)
   drawLine(t, x - size/4, y + size/4, x + size/4, y - size/4)

def drawO(t,x,y,size):
   t.cirle(size)


def Move():
   y = input("Please choose a row:")
   x = input("Now please choose a column:")
   if x in ['0','1','2']  and y in ['0','1','2']:
      return("Your destination is " + y + " " + "and " + x)
   else:
      return("One or more of your dimensions is out of bounds")