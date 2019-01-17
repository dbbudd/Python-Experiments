#!/usr/bin/env python

import turtle
t = turtle.Pen()

t.speed(100)
length = 30
while length < 450:
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    length = length + 10

turtle.done()