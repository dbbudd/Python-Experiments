#!/usr/bin/env python

import turtle
t = turtle.Pen()

def rectangle(colour, width, length):
    t.pencolor(colour)
    t.fillcolor(colour)
    t.begin_fill()
    t.pendown()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.goto(100,-100)
t.setheading(45)
t.heading()
rectangle("red", 30, 300)

t.goto(100,100)
t.right(90)
rectangle("red", 30, 300)

t.goto(0,-200)
t.setheading(90)
t.heading()
rectangle("white", 400, 100)

turtle.done()