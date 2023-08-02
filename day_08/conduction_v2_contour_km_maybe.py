#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------
def fac(time):
    factorval = -1*np.cos(time/24*2*np.pi)
    if factorval <0:
        factorval = 0
    return(factorval)


if __name__ == "__main__":

    dx = 0.25
    # set x with 1 ghost cell on both sides:
    x = np.arange(-dx, 10 + 2 * dx, dx)
    nPts = len(x)
    # print(x)
    t_lower = 200.0
    # t_upper = 1000.0
    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    #d = np.zeros(nPts)

    #time dependence
    nDays = 3 #days
    dt = 1 #hours
    times = np.arange (0, nDays*24, dt)
    lon = 0.0
    temp_contf = np.zeros((len(times), nPts))
    for hour in range(len(times)):
        UT = times[hour]%24
        localtime = lon/15+UT #grenich time
        # Add a source term:
        Qbkg = np.zeros(nPts)
        xstart_index = int(3/dx+dx) #x = 3 --> index is int(3/dx+dx)
        xend_index = int(7/dx+dx) #x = 7
        Qbkg[xstart_index:xend_index]= 100
        QEUV = np.zeros(nPts)
        # localtime = 12
        factor = fac(localtime)
        sunheat = 100
        QEUV[xstart_index:xend_index] = sunheat*factor
        #confirm fac working
        # times = np.linspace(0,24)
        # plt.figure()
        # plt.plot(times, [fac(time_in) for time_in in times])
        lam = 10
        d = (Qbkg+QEUV)*dx**2/lam

        # boundary conditions (bottom - fixed):
        a[0] = 0
        b[0] = 1
        c[0] = 0
        d[0] = t_lower
        # top - floating:
        a[-1] = 1
        b[-1] = -1
        c[-1] = 0
        d[-1] = 0 #t_upper
        
        # solve for Temperature:
        t = solve_tridiagonal(a, b, c, d)
        temp_contf[hour] = t


    # #times, x
    # #     dt = 1 #hours
    # # times = np.arange (0, nDays*24, dt)
    #     dx = 0.25
    # # set x with 1 ghost cell on both sides:
    # x = np.arange(-dx, 10 + 2 * dx, dx)
    # nPts = len(x)
    # dt_days = (3-0)/(len(times))
    timedays = times/24
    alt_real = 40*x+100
    time_contf, alt_contf = np.meshgrid(timedays, alt_real)

    levels = np.linspace(np.min(temp_contf), np.max(temp_contf), num = 15)
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111)
    cs = ax.contourf(time_contf, alt_contf, temp_contf.T, levels)
    cbar = fig.colorbar(cs)
    cbar.ax.set_ylabel('temperature [K]')
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.xlabel('time [days]')
    plt.ylabel('altitude [km]')
    plotfile = 'conduction_v1_contour.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)


    plt.show()
    plt.close()
    
    
    
