#!/usr/bin/env python

import turtle

myWin = turtle.Screen()
myWin.setup(600,600)
myWin.bgcolor("white")

t = turtle.Pen()
t.hideturtle()
t.width(5)
t.speed(1000)


def drawVertical():
    t.penup()
    t.goto(0,0)
    t.goto(100,600)
    t.setheading(270) #south
    t.heading()
    t.pendown()
    t.forward(1200)
    t.penup()
    t.penup()
    t.goto(-100,600)
    t.pendown()
    t.forward(1200)
    t.penup()


def drawHorizontal():
    t.penup()
    t.goto(0,0)
    t.goto(600,100)
    t.pendown()
    t.setheading(180) #west
    t.heading()
    t.forward(1200)
    t.penup()
    t.penup()
    t.goto(600,-100)
    t.pendown()
    t.forward(1200)
    t.penup()
    
drawVertical()
drawHorizontal()

'''
A1 = {"topleft":(-300,300), "topright":(-100,300), "bottleft":(-300,100), "bottright":(-100,100)}
B1 = {"topleft":(-300,100), "topright":(-100,100), "bottleft":(-300,-100), "bottright":(-100,-100)}
C1 = {"topleft":(-300,-100), "topright":(-100,-100), "bottleft":(-300,-300), "bottright":(-100,-300)}

A2 = {"topleft":(-100,300), "topright":(100,300), "bottleft":(-100,100), "bottright":(100,100)}
B2 = {"topleft":(-100,100), "topright":(100,100), "bottleft":(-100,-100), "bottright":(100,-100)}
C2 = {"topleft":(-100,-100), "topright":(100,-100), "bottleft":(-100,-300), "bottright":(300,-300)}

A3 = {"topleft":(100,300), "topright":(300,300), "bottleft":(100,100), "bottright":(300,100)}
B3 = {"topleft":(100,100), "topright":(300,100), "bottleft":(100,-100), "bottright":(300,-100)}
C3 = {"topleft":(100,-100), "topright":(300,-100), "bottleft":(100,-300), "bottright":(300,-300)}

t.penup()


s = turtle.Shape("compound")

A1_square = (A1['topleft'],A1['topright'],A1['bottright'], A1['bottleft'])
s.addcomponent(A1_square, "red", "blue")
A2_square = (A2['topleft'],A2['topright'],A2['bottright'], A2['bottleft'])
s.addcomponent(A2_square, "red", "blue")
A3_square = (A3['topleft'],A3['topright'],A3['bottright'], A3['bottleft'])
s.addcomponent(A3_square, "red", "blue")

B1_square = (B1['topleft'],B1['topright'],B1['bottright'], B1['bottleft'])
s.addcomponent(B1_square, "red", "blue")
B2_square = (B2['topleft'],B2['topright'],B2['bottright'], B2['bottleft'])
s.addcomponent(B2_square, "red", "blue")
B3_square = (B3['topleft'],B3['topright'],B3['bottright'], B3['bottleft'])
s.addcomponent(B3_square, "red", "blue")

C1_square = (C1['topleft'],C1['topright'],C1['bottright'], C1['bottleft'])
s.addcomponent(C1_square, "red", "blue")
C2_square = (C2['topleft'],C2['topright'],C2['bottright'], C2['bottleft'])
s.addcomponent(C2_square, "red", "blue")
C3_square = (C3['topleft'],C3['topright'],C3['bottright'], C3['bottleft'])
s.addcomponent(C3_square, "red", "blue")

turtle.register_shape("myshape", s)
turtle.shape("myshape")
'''



def gotoandprint(x, y):
    gotoresult = t.goto(x, y)
    print(t.xcor(), t.ycor())
    return gotoresult

myWin.onscreenclick(gotoandprint)

myWin.onrelease(fun, btn=1, add=None)



turtle.getscreen()._root.mainloop()