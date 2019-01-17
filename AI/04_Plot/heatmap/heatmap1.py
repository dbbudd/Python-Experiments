#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches
import matplotlib.cm

import pylab as pl
data = pl.random((25,25)) # 25x25 matrix of values

fig = plt.figure()
ax = fig.add_subplot(111, xlim = (0,3), ylim = (0,3))
pl.pcolor(data)
pl.colorbar()
pl.show()