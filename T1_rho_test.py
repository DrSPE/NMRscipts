slope = (2.5623334091319e+03); 	    #without minus
slope_error = (1.0441082995245e+02);

t1rho = 1/(slope);
t1rho_error  = 1/(slope - slope_error)  - 1/(slope +slope_error) ;

t1rho_ms = t1rho*1e3;
t1rho_error_ms = t1rho_error*1e3;

print 'T1rho in ms'
print t1rho_ms  
print '+/-'
print t1rho_error_ms

