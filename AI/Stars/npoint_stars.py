#!/usr/bin/env python

import turtle
t = turtle.Pen()

def star(points, size, colour):
    t.color(colour)
    t.pencolor(colour)
    t.begin_fill()
    for i in range(points):
        angle = 180.0 - 180.0 / points
        t.forward(size)
        t.right(angle)
        t.forward(size)
    t.end_fill()

star(7, 200, 'blue')
star(5, 200, 'red')

turtle.done()


