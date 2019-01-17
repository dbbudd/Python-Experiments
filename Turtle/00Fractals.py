#!/usr/bin/env python

import turtle

t = turtle.Turtle()

def leaf():
    t.fillcolor("green")
    t.begin_fill()
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.right(120)
    t.end_fill()


def tree(branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15)
        t.left(40)
        tree(branchLen - 15)
        t.right(20)
        t.backward(branchLen)
    else:
        leaf()
   
t.setheading(90)
t.color("green")
tree(75)

turtle.done()

