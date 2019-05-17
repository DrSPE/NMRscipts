# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:28:27 2017

@author: steff

replaces u with e-6, m with e-3 and removes s to convert all tau values into seconds
"""

replacements = {'m':'e-3', 'u':'e-6', 's':''}



with open('C:\\Users\\steff\\OneDrive for Business\\PhD\\Projects\\solid electrolytes\\LLZO\\analysed NMR data\\5mm_H11281_Z_300n_7Li_se359_20170312\\test.txt','r') as infile, open('C:\\Users\\steff\\OneDrive for Business\\PhD\\Projects\\solid electrolytes\\LLZO\\analysed NMR data\\5mm_H11281_Z_300n_7Li_se359_20170312\\test2.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)