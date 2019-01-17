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

def drawring():
    t.up()
    t.goto(0,0)
    t.left(90)
    for i in range(0,360,30):
        t.right(i)
        t.up()
        t.forward(130)
        t.left(i)
        drawstar()
        t.up()
        t.goto(0,0)
        t.down()
        
    
drawring()

myWindow.exitonclick()
