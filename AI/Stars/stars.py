#!/usr/bin/env python
import turtle
turtle.setup(600,400)
myWindow = turtle.Screen()
myWindow.bgcolor("blue")
t = turtle.Pen()
t.speed(100)

def drawstar():
    t.up()
    t.fillcolor("yellow")
    t.color("yellow")
    t.down()
    t.forward(30)
    t.right(162)
    t.begin_fill()
    for i in range(5):
        t.forward(22)
        t.left(72)
        t.forward(22)
        t.right(144)
    t.end_fill()
    t.left(162)

drawstar()

myWindow.exitonclick()