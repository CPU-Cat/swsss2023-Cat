import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1)
plt.plot(x, np.exp(x), 'mo-')
plt.xlabel(r'$0 \leq x < 1$')
plt.ylabel(r'$e^x$')
plt.title('Exponential function')

plt.show()