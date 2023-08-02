#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import solve_tridiagonal
import hydrostatic as hs

def fac(time):
    factorval = -1*np.cos(time/24*2*np.pi)
    if factorval <0:
        factorval = 0
    return(factorval)


# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------
if __name__ == "__main__":
    #add tides 
    AmpDi = 50
    AmpSd = 25
    PhaseDi = np.pi/2
    PhaseSd = 3*np.pi/2

    dalt = 4
    alt_real = 100+np.arange(-dalt, 400+2*dalt, dalt)
    print(alt_real)
    nPts = len(alt_real)

    # set default coefficients for the solver:
    a = np.zeros(nPts) - 1
    b = np.zeros(nPts) + 2
    c = np.zeros(nPts) - 1
    #d = np.zeros(nPts)

    #time dependence
    nDays = 27 #days
    dt = 1 #hours
    times = np.arange (0, nDays*24, dt)
    #solar cycle and rotate periodicity
    f107 = 100+(50/(24*365))*times + 25*np.sin(times/(27*24)*2*np.pi)
    lon = 0.0
    temp_contf = np.zeros((len(times), nPts))
    for hour in range(len(times)):
        UT = times[hour]%24
        localtime = lon/15+UT #greenwich time

        # Add a source term:
        Qbkg = np.zeros(nPts)
        xstart_index = int(200/dalt+dalt) #x = 200km --> index is int(200/dx+dx)
        xend_index =  int(400/dalt+dalt) #x = 400km
        Qbkg[xstart_index:xend_index]= 0.4 #100-->0.4 to get km to work

        QEUV = np.zeros(nPts)
        factor = fac(localtime)
        sunheat = 0.4 *f107[hour]/100
        QEUV[xstart_index:xend_index] = sunheat*factor

        lam = 80
        d = (Qbkg+QEUV)*dalt**2/lam


        t_lower = 200.0 +AmpDi*np.sin(localtime/24*2*np.pi+PhaseDi) + AmpSd*np.sin(localtime/24*2*np.pi*2+PhaseSd)

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


    timedays = times/24
    time_contf, alt_contf = np.meshgrid(timedays, alt_real)
    #levels = np.linspace(np.min(temp_contf), np.max(temp_contf), num = 15)
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(111)
    cs = ax.contourf(time_contf, alt_contf, temp_contf.T)#, levels)
    cbar = fig.colorbar(cs)
    cbar.ax.set_ylabel('temperature [K]')
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.xlabel('time [days]')
    plt.ylabel('altitude [km]')
    plotfile = 'conduction_v1_contour_km_TIDES.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)


    plt.show()
    plt.close()
    
    
    
