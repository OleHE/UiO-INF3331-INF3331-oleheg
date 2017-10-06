from integrator import integrate_time as integrate_time
from numpy_integrator import integrate_time as numpy_integrate_time
from numba_integrator import integrate_time as numba_integrate_time


def f(x):
    return 3*x**2 + 2*x + 1

a = 0
b = 1
N = 10000

print integrate_time(f, a, b, N) +  " Python"
print numpy_integrate_time(f, a, b, N) + " Numpy"
print numba_integrate_time(f, a, b, N) + " Numba"
