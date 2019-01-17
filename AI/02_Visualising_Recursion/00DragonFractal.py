#!/usr/bin/env python

import turtle
def initialize (color='blue'):
    '''prepare to draw'''
    turtle.clear()
    # values for speed are 'fastest' (no delay), 'fast', (delay 5ms),
    # default = 'normal' (delay 10ms), 'slow' (delay 15ms),
    # 'slowest' (delay 20ms)
    turtle.speed('slow')
    # lift turtle pen to move without drawing
    turtle.up()
    # start at 120 units to the left of center
    turtle.goto(-120, 0)
    # initial heading 0 --> east
    turtle.setheading(0)
    # initial color of pen
    turtle.color(color)
    # turtle pen ready to draw
    turtle.down()
def dragon_right(max_len, min_len):
    '''draw lines favoring right'''
    # optionally draw this part in red
    turtle.color ('red')
    if max_len <= min_len:
        turtle.forward(max_len)
    else :
        max_len /= 2.0
        #print(max_len)  # test
        dragon_right(max_len, min_len)
        turtle.right(90)
        dragon_left(max_len, min_len)
def dragon_left(max_len, min_len):
    '''draw lines favoring left'''
    # optionally draw this part in blue
    turtle.color('blue')
    if max_len <= min_len:
        turtle.forward(max_len)
    else :
        max_len /= 2.0
        #print(max_len)  # test
        dragon_right(max_len, min_len)
        turtle.left(90)
        dragon_left(max_len, min_len)
def dragon_curve(max_len, min_len, color):
    initialize(color)
    dragon_right(max_len, min_len)
if __name__ == '__main__' :
    turtle.title("dragon curve fractal")
    # experiment with max and min length
    max_len = 4000
    min_len = 30
    dragon_curve(max_len, min_len, 'purple')
    # show finished result until corner x is clicked
    turtle.done()