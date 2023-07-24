import numpy as np
import matplotlib.pyplot as plt
import math
from math import pi

#!/usr/bin/env python
"""
A 3D plot script for spherical coordinates
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

def spherical_to_cartesian(radius, anglephi, angletheta):
    """
    Converts spherical coordinate to cartesian coordinate
    Args:
        radius(float):
            distance from origin
        anglephi(float):
            azimuth angle in radians
        angletheta(float):
            polar angle in radians
      
    Returns:
        x,y,z cartesian coordinates
    
    Examples:
        from math import pi
        spherical_to_cartesian(3.6, pi/2, pi/8)
    """
    x = radius * np.sin(anglephi)*np.cos(angletheta)
    y = radius * np.sin(anglephi)*np.sin(angletheta)
    z = radius * np.cos(anglephi)
    return x,y,z


# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    def checkcoordinatesaresame(rad, phi, theta, x,y,z, error = 1e-4):
        """
        checks if spherical and cartesian coordinates are the same point within error
        Args:
            rad(float):
                distance from origin for spherical point
            phi(float):
                azimuth angle in radians for spherical point
            theta(float):
                polar angle in radians for spherical point
            x (float):
                x coordinate for cartesian point
            y(float):
                y coordinate for cartesian point
            z(float):
                z coordinate for cartesian point
            error (float, default = 1e-4):
                the allowable distance between spherical and cartesian point
       
        Returns:
            True (boolean) if points are within error distance
            False (boolean) if points are not within error distance
        
        Examples:
            checkcoordinatesaresame(1, pi/2, pi/2, 0,1,0)
        """
        cartesianconverted = spherical_to_cartesian(rad,phi,theta)
        distancebetween = math.dist(cartesianconverted, (x,y,z))
        if distancebetween<error:
            output = True
        else:
            output = False
        return output
    #uncomment below print lines to print values to see results
    # print("test should be 1,0,0 output: ", spherical_to_cartesian(1, np.pi/2, 0))
    # print("test should be 0,1,0 output: ", spherical_to_cartesian(1, np.pi/2, np.pi/2))
    # print("test should be 0,0,1 output: ", spherical_to_cartesian(1, 0, 0))
    # print( spherical_to_cartesian(1, np.pi, np.pi))
    # print( spherical_to_cartesian(1, np.pi*2, np.pi*2))
    # print(spherical_to_cartesian(1, -np.pi, -2*np.pi))
    # print(spherical_to_cartesian(1, -2*np.pi, np.pi))

    # putting errors around known values to ensure accuracy of function
    assert checkcoordinatesaresame(1, np.pi/2, 0, 1,0,0) , "Coordinate mismatch! (1, pi/2,0) != (1,0,0) "
    assert checkcoordinatesaresame(1, np.pi/2, pi/2, 0,1,0) , "Coordinate mismatch! (1, pi/2,pi/2) != (0,1,0) "
    assert checkcoordinatesaresame(1, 0, 0, 0,0,1) , "Coordinate mismatch! (1, pi/2,0) != (0,0,1) "
    assert checkcoordinatesaresame(1, np.pi, np.pi, 0,0,-1) , "Coordinate mismatch! (1, np.pi, np.pi) != (0,0,-1) "
    assert checkcoordinatesaresame(1, np.pi*2, np.pi*2,0,0,1) , "Coordinate mismatch! (1,np.pi*2, np.pi*2) != (0,0,1) "
    assert checkcoordinatesaresame(1, -np.pi, -2*np.pi, 0,0,-1) , "Coordinate mismatch! (1,-np.pi, -2*np.pi) != (0,0,-1) "
    assert checkcoordinatesaresame(1, -2*np.pi, np.pi, 0,0,1) , "Coordinate mismatch! (1, -2*np.pi, np.pi) != (0,0,1) "

    #plot 3d spherical coordinates
    fig = plt.figure()
    axes = fig.add_subplot(projection = '3d')
    rvals = np.linspace(0,1)
    phivals = np.linspace(0, 2*np.pi)
    thetavals = np.linspace(0, 2*np.pi)
    xvals,yvals,zvals = spherical_to_cartesian(rvals,phivals,thetavals)
    axes.scatter(xvals,yvals,zvals)
    plt.xlabel('x')
    plt.ylabel('y')
    axes.set_zlabel('z')
    plt.title('Spherical coordinates test plot')

    plt.show()