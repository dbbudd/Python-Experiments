#!/usr/bin/env python

from Tkinter import *
import math
def sierpinsky(canvas, x, y, size, level):
    x = float(x)
    y = float(y)
    if (level == 0):
        canvas.create_polygon(x, y,
                              x+size, y,
                              x+size/2, y-size*math.sqrt(3)/2,
                              fill="black")
    else:
        sierpinsky(canvas, x, y, size/2, level-1)
        sierpinsky(canvas, x+size/2, y, size/2, level-1)
        sierpinsky(canvas, x+size/4, y-size*math.sqrt(3)/4, size/2, level-1)

root = Tk()
myCanvas = Canvas(root, width=500, height=500)
myCanvas.pack()
sierpinsky(myCanvas, 100, 400, 300, 2)
root.mainloop()