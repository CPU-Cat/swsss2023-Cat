#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":

    dx = 0.25

    # set x with 1 ghost cell on both sides:
    x = np.arange(-dx, 10 + 2 * dx, dx)
    print(x)
    t_lower = 200.0
    t_upper = 1000.0
    nPts = len(x)
    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    #d = np.zeros(nPts)
    Q = np.zeros(nPts)
    x3_index = int(3/dx+dx)
    x7_index = int(7/dx+dx)
    print(x3_index, x7_index)
    Q[x3_index:x7_index]= 100
    lam = 10
    d = Q*dx**2/lam

    # boundary conditions :
    a[0] = 0
    b[0] = 1
    c[0] = -1
    d[0] = 0#t_lower
    # top - floating:
    a[-1] = 1
    b[-1] = -1
    c[-1] = 0
    d[-1] = 0 #t_upper

    # a[nPts/2] = 1
    # b[nPts/2] = 0
    # c[nPts/2] = 0
    d[x7_index+1] = 20000 #t_upper



    # Add a source term:
    
    # solve for Temperature:
    t = solve_tridiagonal(a, b, c, d)

    # plot:
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111)

    ax.plot(x, t)
    plt.xlabel('altitude')
    plt.ylabel('Temp')
    plotfile = 'conduction_v1_floating_with_Q.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)
    plt.show()
    plt.close()
    
    
    
