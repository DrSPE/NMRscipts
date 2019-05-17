# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:37:05 2017

@author: steff


check if folder is  correct, especially if subfolders were created
"""


import os

replacements = {'n':'e-9', 'm':'e-3', 'u':'e-6', 's':' '}

directory = 'D:\NMR data\Analysis\T1rho\H100_LLZO'


try:
    os.stat(os.path.join(directory, 'new'))
except:
    os.mkdir(os.path.join(directory, 'new'))
 
for filename in os.listdir(directory):
    if filename.endswith("K.txt"): 
        with open(os.path.join(directory, filename),'r') as infile, open(os.path.join(directory, 'new', filename), 'w') as outfile:
            for line in infile:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                outfile.write(line)