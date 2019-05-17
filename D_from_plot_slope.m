%script to convert the slope from the linear fit in the ln(I/I0) vs G² plot
%using lnI instead of ln(I/I0) has (as expected) no influence on the slope

%defining variables/constants:
gamma = 2*pi*1654.7; %gyro 7Li in rad/(s·G)

%define small delta in s
sd = 1.2*1e-3;

%define big delta in s
bd =  5*1e-3;

%enter slope from fit
slope =  -2.4713187609138e-06 ; 
slope_error = 2.0791875886933e-07;


%start calculation

D_cm = -(slope)/((gamma^2*sd^2)*((bd-sd)/3)) %D in cm²/s

D_m  = D_cm*1e-4                              %D in m²/s


%calculate error

D_error = -(slope-slope_error)/((gamma^2*sd^2)*((bd-sd)/3))...
--(slope+slope_error)/((gamma^2*sd^2)*((bd-sd)/3))

%calculate msd

