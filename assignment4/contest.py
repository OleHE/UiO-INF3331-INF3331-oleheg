import numpy as np
from numpy_integrator import midpoint_integrate



def f1(x):
    return (1/np.pi)*(np.sin(x)/(x) * np.sin(x/3.)/(x/3.) * np.sin(x/5.)/(x/5.))

def f2(x):
    return f1(x)*(1/np.pi)*(np.sin(x/5.)/(x/5.))

def f3(x):
    return f2(x)*(1/np.pi)*(np.sin(x/7.)/(x/7.))

def f4(x):
    return f3(x)*(1/np.pi)*(np.sin(x/9.)/(x/9.))

def f5(x):
    return f4(x)*(1/np.pi)*(np.sin(x/11.)/(x/11.))

def f6(x):
    return f1(x)*(1/np.pi)*(np.sin(x/13.)/(x/13.))

a = 10**(-20)
b = 1E7
N = 100

print midpoint_integrate(f1,a,b,N)
print midpoint_integrate(f2,a,b,N)
print midpoint_integrate(f3,a,b,N)
print midpoint_integrate(f4,a,b,N)
print midpoint_integrate(f5,a,b,N)
print midpoint_integrate(f6,a,b,N)
