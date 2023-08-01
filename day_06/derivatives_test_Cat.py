#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------

# Take first + second derivative of a function analytically and taylor

# ----------------------------------------------------------------------
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

def first_derivative(f, x):

    """ Function that takes the first derivative ASSUMING EVENLY SPACED X

    Parameters
    ----------
    f - values of a function that is dependent on x -> f(x)
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    dfdx - the first derivative of f(x)

    Notes
    -----
    take the first derivative of f(x) here

    """

    nPts = len(f)
    dfdx = np.zeros(nPts)

    
    dx = x[1]-x[0] #assumes even spacing
    dfdx[1:-1] = [(f[xindex+1]-f[xindex-1])/(2*dx) for xindex in range(1, nPts-1)]
    dfdx[0] = -1*(dfdx[2]-dfdx[1])/(dx)+dfdx[1]
    dfdx[0] = -1*(3*dfdx[2]-2*dfdx[1]-dfdx[3])/(dx)+dfdx[1]
    dfdx[-1] = -1*(dfdx[-3]-dfdx[-2])/(dx)+dfdx[-2]

    return dfdx

# ----------------------------------------------------------------------
# Take second derivative of a function
# ----------------------------------------------------------------------

def second_derivative(f, x):

    """ Function that takes the second derivative

    Parameters
    ----------
    f - values of a function that is dependent on x -> f(x)
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    d2fdx2 - the second derivative of f(x)

    Notes
    -----
    take the second derivative of f(x) here

    """

    nPts = len(f)
    
    d2fdx2 = np.zeros(nPts)

    # do calculation here - need 3 statements:
    #  1. left boundary ( dfdx(0) = ...)
    #  2. central region (using spans, like dfdx(1:nPts-2) = ...)
    #  3. right boundary ( dfdx(nPts-1) = ... )
    
    dx = x[1]-x[0] #assumes even spacing
    d2fdx2[1:-1] = [(f[xindex+1]+f[xindex-1]-2*f[xindex])/(dx**2) for xindex in range(1, nPts-1)]
    d2fdx2[-1] = -1*(d2fdx2[-3]-d2fdx2[-2])/(dx)+d2fdx2[-2]
    d2fdx2[0] = -1*(d2fdx2[2]-d2fdx2[1])/(dx)+d2fdx2[1]


    return d2fdx2

# ----------------------------------------------------------------------
# Get the analytic solution to f(x), dfdx(x) and d2fdx2(x)
# ----------------------------------------------------------------------

def analytic(x):

    """ Function that gets analytic solutions

    Parameters
    ----------
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    f - the function evaluated at x
    dfdx - the first derivative of f(x)
    d2fdx2 - the second derivative of f(x)

    Notes
    -----
    These are analytic solutions!

    """

    f = 0.01*x**6-100*np.cos(x)+50
    dfdx = 0.01*6*x**5-100*(-1)*np.sin(x)
    d2fdx2 = 0.01*6*5*x**4-100*(-1)*np.cos(x)

    return f, dfdx, d2fdx2

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":


    # define dx:
    dx = np.pi / 4
    
    # arange doesn't include last point, so add explicitely:
    x = np.arange(-2.0 * np.pi, 2.0 * np.pi + dx, dx)

    # get analytic solutions:
    f, a_dfdx, a_d2fdx2 = analytic(x)

    # get numeric first derivative:
    n_dfdx = first_derivative(f, x)

    # get numeric first derivative:
    n_d2fdx2 = second_derivative(f, x)

    # plot:
    # get figures:
    fig = plt.figure(figsize = (10,10))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax1.plot(x, f)
    # plot first derivatives:
    error = np.sum(np.abs(n_dfdx - a_dfdx)) / len(n_dfdx)
    sError = ' (Err: %5.1f)' % error
    ax2.plot(x, a_dfdx, color = 'black', label = 'Analytic')
    ax2.plot(x, n_dfdx, color = 'red', label = 'Numeric'+ sError)
    ax2.scatter(x, n_dfdx, color = 'red')
    ax2.legend()
    # plot second derivatives:
    error2 = np.sum(np.abs(n_d2fdx2 - a_d2fdx2)) / len(n_d2fdx2)
    sError2 = ' (Err: %5.1f)' % error2
    ax3.plot(x, a_d2fdx2, color = 'black', label = 'Analytic')
    ax3.plot(x, n_d2fdx2, color = 'red', label = 'Numeric'+ sError2)
    ax3.scatter(x, n_d2fdx2, color = 'red')
    ax3.legend()

    
    plotfile = 'day6_derivtest_plot.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile, dpi = 500)
    plt.show()
    plt.close()
    
