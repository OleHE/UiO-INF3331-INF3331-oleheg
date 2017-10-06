import matplotlib.pyplot as plt
import numpy as np
import time

def integrate(f, a, b, N):
    x = np.linspace(a, b, N+1)
    x = x[1:]
    dx = x[1]-x[0]  # dx = float(b-a)/N
    return np.sum(f(x))*dx

def midpoint_integrate(f, a, b, N):
    x = np.linspace(a, b, N+1)
    # dx = float(b-a)/(N-1)
    dx = x[1]-x[0]
    x += dx/2
    x = x[:-1]
    return np.sum(f(x))*dx

def integrate_time(f, a, b, N):
    start = time.clock()
    integrate(f,a,b,N)
    stop = time.clock()
    return "Time = %s -- N = %s" % (stop-start, N)
