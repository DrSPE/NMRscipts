# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:19:15 2017

@author: se359
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

#data import
n, I, f, delta = np.loadtxt('nmr.txt', skiprows=1, delimiter=',', unpack=True)


# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

# Plot using blue color with a continuous line of width 1 (pixels)
plt.plot(delta, I, color="blue", linewidth=1.0, linestyle="-")


# Set x limits
#plt.xlim(-180.0,180.0)

# Set x ticks
#plt.xticks(np.linspace(-4,4,9,endpoint=True))

# Set y limits
#plt.ylim(-1.0,1.0)

# Set y ticks
#plt.yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
# savefig("../figures/exercice_2.png",dpi=72)

# Show result on screen
plt.show()