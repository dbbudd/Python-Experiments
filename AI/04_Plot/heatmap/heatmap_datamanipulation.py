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

data = []
output = ""

#HEATMAP DATA
dat = np.loadtxt('xy.csv', delimiter = ",")
x, y = dat[:,0], dat[:,1]

#DRAWING THE GRID
fig = plt.figure()
ax = fig.add_subplot(111)

#DRAW A HEATMAP
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
plt.clf()
plt.imshow(heatmap, extent=extent)

#DRAW RECTANGLE TO RECORD CLICKS
rec = plt.Rectangle([0,0], 3, 3, facecolor='none')
#plt.grid(True, which="major", ls="-", linewidth=0.4, color="#ffffff", alpha=0.5)






def onclick(event):
    coord = float(event.xdata), float(event.ydata)
    data.append(coord)

fig.canvas.mpl_connect("button_press_event", onclick)

#draw your own grid
plt.axis("off")
plt.axhline(y=1, xmin=0, xmax=3, linewidth=2, color='#ffffff')
plt.axhline(y=2, xmin=0, xmax=3, linewidth=2, color='#ffffff')
plt.axvline(x=1, ymin=0, ymax=3, linewidth=2, color='#ffffff')
plt.axvline(x=2, ymin=0, ymax=3, linewidth=2, color='#ffffff')

plt.show()
plt.close()

# OUTPUT USER CLICKS TO CSV
def record_clicks(data, output):
    file = open("xy.csv", "a")
    for row in data:
        output = output + str(row[0]) + "," + str(row[1]) + "\n"
    
    file.write(output)
    file.close()

record_clicks(data, output)