from integrator import integrate as integrate
from numpy_integrator import integrate as numpy_integrate

def test_integral_of_constant_function():
    def f(x):
        return 2
    for i in range(1,4):
        assert integrate(f,0,1,10**i) - 2  < 1E20

def test_integral_of_linear_function():
    def f(x):
        return 2*x
    for i in range(1,4):
        assert integrate(f,0,1,10**i) - 2 < 1E20

def test_numpy_integral_of_constant_function():
    def f(x):
        return 2
    for i in range(1,4):
        assert numpy_integrate(f,0,1,10**i) - 2  < 1E20

def test_numpy_integral_of_linear_function():
    def f(x):
        return 2*x
    for i in range(1,4):
        assert numpy_integrate(f,0,1,10**i) - 2  < 1E20
