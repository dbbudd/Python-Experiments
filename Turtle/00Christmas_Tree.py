#!/usr/bin/env python
import turtle
n = 200

t = turtle.Pen()
t.speed(0)
t.left(90)
t.forward(3*n)
t.color("orange", "yellow")
t.begin_fill()
t.left(126)
for i in range(5):
    t.forward(n/5)
    t.right(144)
    t.forward(n/5)
    t.left(72)
t.end_fill()
t.right(126)

t.color("dark green")
t.backward(n*4.8)

def tree(d, s):
    if d <= 0: return
    t.forward(s)
    tree(d-1, s*.8)
    t.right(120)
    tree(d-3, s*.5)
    t.right(120)
    tree(d-3, s*.5)
    t.right(120)
    t.backward(s)
tree(15, n)
t.backward(n/2)


turtle.done()

