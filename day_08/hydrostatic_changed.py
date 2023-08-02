#!/usr/bin/env python
"""Space Weather Simulation Summer School
"""
__author__ = 'Cat now lol'
__email__ = 'ckpawu@bu.edu'

import numpy as np
import matplotlib.pyplot as plt

# num_pts = 100
# alt_0 = 100
# alt_n = 500
# temp_0 = 200
# temp_n = 1000
# k = 1.38e-23
# radius_e = 6370  # km
# m = 28*1.67e-27 #changes w/ species
# n_0 = 1.e19


def scale_height(temp, gravity, mass):
    """Returns scale height given temperature and accel. due to gravity
    """
    k = 1.38e-23
    return k*temp/mass/gravity

def dens_from_alt( temp, alt,  massm, n0 , radius = 6370.0):
    g = 3.99e14 / ((radius+np.array(alt))*1000)**2
    # print('g \n', g)
    # print('alt \n', alt)
    # print('temp \n', temp)
    # print('mass \n', massm)
    sc_height = scale_height(temp,
                             g, mass=massm)
    # print('sc height \n', sc_height)
    n = [n0]
    for h, t_0, t_1, dz in zip(sc_height,
                               temp[:-1], temp[1:],
                               (alt[1:]-alt[:-1])*1000):
        # print(h, t_0, t_1, dz, n[-1])
        n += [t_0/t_1 * n[-1] * np.exp(-1*dz/h)]
    density = n
    return(density)

# if __name__ == '__main__':
#     # Set up problem
#     alt = np.linspace(alt_0, alt_n, num_pts)
#     temp = np.linspace(temp_0, temp_n, num_pts)
#     g = 3.99e14 / ((radius_e+alt)*1000)**2
#     sc_height = scale_height(temp=(temp[1:]+temp[:-1])/2,
#                              gravity=(g[1:]+g[:-1])/2)

#     # Calculate
#     n = [n_0]
#     for h, t_0, t_1, dz in zip(sc_height,
#                                temp[:-1], temp[1:],
#                                (alt[1:]-alt[:-1])*1000):
#         n += [t_0/t_1 * n[-1] * np.exp(-1*dz/h)]


#     massm = 28*1.67e-27
#     n0 = 1.e19
#     dens = dens_from_alt(temp, alt,  massm, n0)
#     # Plot
#     plt.plot(alt, np.log(n))
#     plt.plot(alt, np.log(dens), '*')
#     plt.xlabel('Altitude [km]')
#     plt.ylabel('Density [$m^{-3}$]')
#     plt.show()
