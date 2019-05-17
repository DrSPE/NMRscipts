# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:13:02 2017

@author: steff


"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants
import os
from uncertainties import ufloat
from uncertainties import unumpy

#directory to be used
directory = 'C:\\Users\\steff\\OneDrive for Business\\PhD\\Projects\\solid electrolytes\\LLZO\\analysed NMR data\\5mm_H11281_Z_300n_7Li_se359_20170312\\VT T1\\new\\'


#importing data
tk, t1s, t1err, t11, t11err, lnt11, lnt11err  = np.loadtxt(os.path.join(directory, 't1values.txt'), delimiter = ',', skiprows=1, unpack=True)

#create y and x values
x = 1./tk
y = lnt11

#T1 function to fit data to
def func(x, slope, b):
     return slope * x + b
#data fitting
popt, pcov = curve_fit(func, x, y)

#print slope and standard deviation
#print  '{}+/-{}'.format(popt[0],np.sqrt(np.diag(pcov))[0]) 

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

 # Scatter-Plot using blue color with a line of width 1 (pixels)
plt.scatter(x, y, color="black", linewidth=1.0, linestyle="-")

plt.errorbar(x, y, lnt11err, color="black", linewidth=0.0, linestyle="-")

x2 = np.linspace(0.002,0.0035,10)
y2 = popt[0]*x2+popt[1]

# Line-Plot using blue color with a line of width 1 (pixels)
plt.plot(x2, y2, color="black", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(0.002,0.004)

#save figure
#plt.savefig(os.path.join(directory,'Arrhenius'),dpi=200)

# Show result on screen
plt.show()

