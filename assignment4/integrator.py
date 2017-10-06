import matplotlib.pyplot as plt
import time

def integrate(f, a, b, N):
    dx = float(b-a)/N
    integral = 0
    for i in range(1,N+1):
        integral += f(i*dx)*dx
    return integral

def midpoint_integrate(f, a, b, N):
    dx = float(b-a)/N
    half_step = dx/2
    integral = 0
    for i in range(0,N):
        integral += f(i*dx + half_step)*dx
    return integral

def integrate_time(f,a,b,N):
    start = time.clock()
    integrate(f, a, b, N)
    stop = time.clock()
    return "Time = %s -- N = %s" % (stop-start, N)


if __name__ == '__main__':
    def f(x):
        return x**2

    error = []
    N = [i for i in range(1,100)]
    for n in N:
        error.append(abs(integrate(f,0,1,n) - 1./3))

    plt.plot(N,error)
    plt.xlabel('N')
    plt.ylabel('Error')
    plt.savefig('quadratic error.png')
    plt.show()
