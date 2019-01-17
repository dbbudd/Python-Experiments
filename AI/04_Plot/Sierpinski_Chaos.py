#!/usr/bin/env python

%matplotlib inline #!
import random
import numpy as np
import time
import pylab as pl #!
from IPython import display #!
import numpy as np

pylab.rcParams['figure.figsize'] = (10.0, 8.0)


def Sierpinski_Chaos(gp=None, n=None):
    """This Choase game shows how randomness can lead to structure:
        1. 3 points have to be drawn in the plane
        2. Mark a triangle with these points with pl.plot
        3. draw a random point outside this triangle - this is the fiest 'Game-Point' (gp)
        
        Repeat til n:
        4. Choose a randomly a base-point out of three corner points
        5. Build the vector between the 'Game-Point' and the randomly chosen base-point and make a point (scatter) half way to the base-point
    """
    
    #1,2.
    pl.plot([0,4,2,0],[0,0,4,0])
    pl.xlim(0,4)
    pl.ylim(0,4)
    base_points = [[0,0],[4,0],[2,4]]
    if gp==None:
        gp = np.array([5,5]) #starting game_point
    if n==None:
        n = 500 #number of interactions
    for n in range(500):
        gp_log = gp.copy()
        pl.scatter(gp[0], gp[1], lw='O', s=20) #3
        pl.xlim(0,4) #!
        pl.ylim(0,4) #!
        pl.draw() #!
        display.clear_output(wait=True) #!
        display.display(pl.gcf()) #!
        time.sleep(0.0000005) #!
        
        #4
        fort_wheel = random.choice(base_points)
        rand_base = np.array(fort_wheel)
        
        #5
        gp = gp - 1.0 / 2 * (gp-rand_base)
        gp_log = np.concatenate((gp_log, gp))
        
        # (gp-rand_base) is "direction-vector" starting from the gp and just walking half way leads to new gp
    return gp_log

build_hipster = Sierpinski_Chaos(n=1500)
    