#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 1 2023

@author: CPU-Cat ckpawu@bu.edu
"""

import numpy as np
import matplotlib.pyplot as plt

# Use Euler's method with different stepsizes to solve the IVP:
# dx/dt = -2*x, with x(0) = 3 over the time-horizon [0,2]
# Compare the numerical approximation of the IVP solution to its analytical
# solution by plotting both solutions in the same figure. 

def analytic(t):

    """ Function that gets analytic solutions

    Parameters
    ----------
    t - the time of the point at which x) is evaluated

    Returns
    -------
    x - the function of x

    Notes
    -----
    These are analytic solutions!

    """
    x =[ 3*np.exp(-2*ti) for ti in t]
    return x

def euler(t, h, x0):

    """ Function that gets euler solutions for specific equation dx/dt = -2*x(t)

    Parameters
    ----------
    t - the time of the point at which x) is evaluated
    h - time step
    x0 = initial condition (x at t=0)
    Returns
    -------
    x - the function values of x euler

    Notes
    -----
    These are euler solutions!

    """
    x = []
    for tindex in range(len(t)):
        if tindex == 0:
            x.append(x0)
        else:
            x.append(x[tindex-1]+h*-2*x[tindex-1])

    return x

if __name__ == "__main__":

    # define dx:
    h = 0.01#0.01
    # arange doesn't include last point, so add explicitely:
    tend = 2
    t = np.arange(0,tend+h, h)
    # get analytic solutions:
    x_analytic = analytic(t)
    # get euler solution:
    x0 = 3
    x_euler = euler(t,h, x0)
    # plot:
    # get figures:
    fig = plt.figure(figsize = (10,10))
    ax1 = fig.add_subplot(111)
    ax1.plot(t, x_analytic, 'x-')
    ax1.plot(t, x_euler, '+--')
    plt.show()