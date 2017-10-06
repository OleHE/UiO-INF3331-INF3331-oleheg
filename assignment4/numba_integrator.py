from numba import jit
import time


@jit
def integrate(f, a, b, N):
    dx = float(b-a)/N
    integral = 0
    for i in range(1,N+1):
        integral += f(i*dx)*dx
    return integral

@jit
def midpoint_integrate(f, a, b, N):
    dx = float(b-a)/N
    half_step = dx/2
    integral = 0
    for i in range(0,N):
        integral += f(i*dx + half_step)*dx
    return integral

@jit
def integrate_time(f,a,b,N):
    start = time.clock()
    integrate(f,a,b,N)
    stop = time.clock()
    return "Time = %s -- N = %s" % (stop-start, N)
