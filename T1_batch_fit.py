# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:02:01 2017

@author: steff
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:19:15 2017

@author: se359

!!!check if change tau...has been used!!!

fitting T1 for all temperatures
all files called '*K.txt' in the folder
saving them in a file

"""
# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants
import os
from uncertainties import ufloat
from uncertainties import unumpy

#T1 function to fit data to
def func(x, I0, A, T1):
     return I0*(1-(2*A*np.exp(-x/T1)))


#directory to be used
directory = 'C:\\Users\\steff\\OneDrive for Business\\PhD\\Projects\\solid electrolytes\\LLZO\\VT T1rho\\Al-LLZO\\T2\\new'

#create file to save values to
with open(os.path.join(directory, 't1values.txt'), 'w') as newfile:
 newfile.write('T/K, T1/s, T1_error, T1-1/s-1, T1-1_error, ln(T1-1), lnT1-1_error \n')

#itterate over all data files in folder endwing with K.txt
 for filename in os.listdir(directory):
    if filename.endswith("K.txt"):
        datafile = os.path.join(directory, filename)
                
        #data import
        n, t, I, Ic, diff = np.loadtxt(datafile, skiprows=2, unpack=True)

        #data fitting
        popt, pcov = curve_fit(func, t, I)
        
        #standard deviation
        perr = np.sqrt(np.diag(pcov))
        #print str(perr[-1])
        
        #show temperature/K for T1
        temp = filename.replace("K.txt", "")
       
        
        print('T1({} K) = {:f} +/- {:f}'.format(temp, popt[-1], perr[-1]))
        
       # print ufloat(popt[-1], perr[-1])
        
        print unumpy.nominal_values(ufloat(popt[-1], perr[-1]))
        print unumpy.std_devs(ufloat(popt[-1], perr[-1]))
        
        t1new = (ufloat(popt[-1], perr[-1]))
        t11 = t1new**(-1)
        logt11 = unumpy.log(t11)
        print t11
        print logt11
       
        
        #write values to file
        newfile.write(temp)
        newfile.write('.0, ')
        newfile.write(str(popt[-1]))
        newfile.write(', ')
        newfile.write(str(perr[-1]))
        newfile.write(', ')
        newfile.write(str(unumpy.nominal_values(t11)))
        newfile.write(', ')
        newfile.write(str(unumpy.std_devs(t11)))
        newfile.write(', ')
        newfile.write(str(unumpy.nominal_values(logt11)))
        newfile.write(', ')
        newfile.write(str(unumpy.std_devs(logt11)))
        newfile.write('\n')
        
        # Create a new figure of size 8x6 points, using 100 dots per inch
        plt.figure(figsize=(8,6), dpi=80)

        # Create a new subplot from a grid of 1x1
        plt.subplot(111)


        # Scatter-Plot using blue color with a line of width 1 (pixels)
        plt.scatter(t, I, color="blue", linewidth=1.0, linestyle="-")

        

        plt.plot(np.arange(0, t[-1]+1, 0.01), func(np.arange(0, t[-1]+1, 0.01), *popt), 'g-')
        

        
        # Set x limits
        #plt.xlim(-180.0,180.0)

        # Set x ticks
        #plt.xticks(np.linspace(-4,4,9,endpoint=True))

        # Set y limits
        #plt.ylim(-1.0,1.0)

        # Set y ticks
        #plt.yticks(np.linspace(-1,1,5,endpoint=True))
        
        #create figures directory
        try:
            os.stat(os.path.join(directory, 'figures'))
        except:
            os.mkdir(os.path.join(directory, 'figures'))
        figdirectory = os.path.join(directory, 'figures')
        
        #Save figure using 72 dots per inch
        plt.savefig(os.path.join(figdirectory, temp) ,dpi=72)

        # Show result on screen
        #plt.show()



#plot T1-1 vs 1000K/T
tk, t1s, t1err, t11, t11err, lnt11, lnt11err  = np.loadtxt(os.path.join(directory, 't1values.txt'), delimiter = ',', skiprows=1, unpack=True)

#create y and x values
x = 1./tk
y = lnt11

#t1erro1 = (1000/(tk+t1err)-1000/(tk-t1err))

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

 # Scatter-Plot using blue color with a line of width 1 (pixels)
plt.scatter(x, y, color="black", linewidth=1.0, linestyle="-")

# Show result on screen
plt.show()

