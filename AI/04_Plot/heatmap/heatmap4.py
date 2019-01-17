#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.cm
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import csv

dat = np.loadtxt('xy.csv', delimiter = ",")
x, y = dat[:,0], dat[:,1]

#heatmap
'''
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)  
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]  
plt.clf()  
plt.imshow(heatmap, extent=extent)
plt.colorbar()
'''

#gameboard
fig = plt.figure()
ax = fig.add_subplot(111, xlim = (0,3), ylim = (0,3))
rec = plt.Rectangle([0,0], 3, 3, facecolor='none')
ax.add_patch(rec)
rec.set_picker(True)

def draw_shape(xCoord, yCoord):
    rectangle = plt.Rectangle((xCoord,yCoord), 1,1, facecolor="green")
    ax.add_patch(rectangle)
    fig.canvas.draw()
    
def onclick(event):
    #round value down to nearest coordinate
    x = math.trunc(event.xdata)
    y = math.trunc(event.ydata)
    draw_shape(x,y)
    
plt.suptitle("Game Board", size = 20)
fig.canvas.mpl_connect('button_press_event', onclick)


plt.show() 