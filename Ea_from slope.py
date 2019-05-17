slope = (7.8367046784210e+03); 	    #without minus
slope_error = (2.8109405753659e+02);

E_a = (slope)*(8.6173303*1e-5);
t1rho_error  = 1/(slope - slope_error)  - 1/(slope +slope_error) ;

# t1rho_ms = t1rho*1e3;
# t1rho_error_ms = t1rho_error*1e3;

print 'E_a in eV'
print E_a  
#print '+/-'
# print t1rho_error



