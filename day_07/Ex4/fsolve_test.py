from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)-4*x
x0 = 2
x = fsolve(f, x0)
print(x)
xval = np.linspace(-5,5)
print(xval)
fval = f(xval)
plt.figure()
plt.plot(xval, fval)
plt.show()
