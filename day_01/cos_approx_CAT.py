#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

from math import factorial
from math import pi


def cos_approx(x, accuracy=10):
    """approximates cosine using taylor series
    Args:
        x(float):
            value to take cosine of
        accuracy(int) (optional):
            (default: 10) Number of taylor series coefficients to use
    
    Returns:
        (float): approximate cosine of x
    
    Examples:
        from math import pi
        cos_approx(pi)
        cos_approx(pi, 50)
    """
    #approxed = sum([(-1)**n*x**(2*n)/(factorial(2*n)) for n in range(accuracy)])
    listi = []
    for n in range(accuracy):
        listi.append((-1)** n* x**(2*n)/(factorial(2*n)))
    approxed = sum(listi)    
    return approxed



# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
