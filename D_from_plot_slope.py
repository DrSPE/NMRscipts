

#script to convert the slope from the linear fit in the ln(I/I0) vs G² plot
#using lnI instead of ln(I/I0) has (as expected) no influence on the slope

#defining variables/constants:

gamma = 2*3.14*4257.8 #last number=gyro (7Li=1654.7, 1H=4257.8) in rad/(s·G)

#define small delta in s
sd = 530*1e-6

#define big delta in s
bd =  40*1e-3

#enter slope from fit
slope =  -9.93332e-08
slope_error = 1.22935e-8


#start calculation

D_cm = -(slope)/((gamma^2*sd^2)*((bd-sd)/3)) #D in cm²/s

#D_m  = D_cm*1e-4                              %D in m²/s


#calculate error

D_error = -(slope-slope_error)/((gamma^2*sd^2)*((bd-sd)/3))--(slope+slope_error)/((gamma^2*sd^2)*((bd-sd)/3))

#calculate msd

