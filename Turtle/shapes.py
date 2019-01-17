#!/usr/bin/env python
import turtle

t = turtle.Pen()


def square():
    count = 0
    while count <= 4:
        t.forward(100)
        t.right(90)
        count += 1
    
def triangle():
    count = 0
    while count <= 3:
        t.forward(100)
        t.right(120)
        count += 1
