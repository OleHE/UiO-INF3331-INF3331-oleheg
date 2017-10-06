from integrator import midpoint_integrate as midpoint_integrate
from integrator import integrate as integrate
from numpy_integrator import midpoint_integrate as numpy_midpoint_integrate
from numba_integrator import midpoint_integrate as numba_midpoint_integrate
import numpy as np



def step_checker(integrate):
    def f(x):
        return np.sin(x)

    a = 0
    b = np.pi
    eps = 10**(-10)
    exact_solution = 2.0

    N = 0
    while True:
        N += 100
        error = abs(integrate(f, a, b, N) - exact_solution)
        if error < eps:
            break

    print N
    print integrate(f, a, b, N)

step_checker(integrate)
step_checker(midpoint_integrate)
step_checker(numpy_midpoint_integrate)
step_checker(numba_midpoint_integrate)
