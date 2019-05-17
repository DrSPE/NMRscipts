# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:19:15 2017

@author: se359
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#T1 function to fit data to
def func(x, I0, A, T1):
     return I0*(1-(2*A*np.exp(-x/T1)))

 

#data import
n, t, I, Ic, diff = np.loadtxt('C:\\Users\\steff\\OneDrive for Business\\PhD\\Projects\\solid electrolytes\\LLZO\\VT T1rho\\Al-LLZO\\T1rho\\new\\390K.txt', skiprows=2, unpack=True)


# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)


# Scatter-Plot using blue color with a line of width 1 (pixels)
plt.scatter(t, I, color="blue", linewidth=1.0, linestyle="-")

popt, pcov = curve_fit(func, t, I)

plt.plot(np.arange(0, t[-1]+1, 0.01), func(np.arange(0, t[-1]+1, 0.01), *popt), 'g-')
print('T1 = {} s'.format(popt[-1]))


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