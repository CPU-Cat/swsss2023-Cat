import numpy as np

# #times, x
nDays = 3
dt = 1 #hours
times = np.arange (0, nDays*24, dt)
dx = 0.25
# # set x with 1 ghost cell on both sides:
x = np.arange(-dx, 10 + 2 * dx, dx)
nPts = len(x)
# dt_days = (3-0)/(len(times))
timedays = times/24
# print(times)
# print(timedays)
alt_real = 40*x+100
time_contf, alt_contf = np.meshgrid(timedays, alt_real)

print(x, '\n')
print('\n', alt_real)