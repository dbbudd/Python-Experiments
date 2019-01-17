#!/usr/bin/env python
'''This script converts speed from KMH to MPH, which may be handy for calculating speed limits when driving abroad, especially for UK and US drivers.
   The conversion formula for KPH to MPH is: 1 kilometre = 0.621371192 miles'''

kmh = int(raw_input("Enter km/h: "))
mph = 0.6214 * kmh
print "Speed:", kmh, "KM/H = ", mph, "MPH"