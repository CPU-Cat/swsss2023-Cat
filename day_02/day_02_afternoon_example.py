import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt

"""
Some magic day 2 getting and plotting omni data
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

f = open("day_02/omni_test.lst")   # Please note the directory of the file
line = f.readline()                 # read one line 
f.close()                           # remember to close the file!

nLines = 3
with open("day_02/omni_test.lst") as f:
    # for line in f:
    #     print(line)
    year = []
    day = []
    hour = []
    minute = []
    symh = []
    times = []
    for i in range(nLines):
        print(f.readline()) #read first nlines and print but do nothing else
    header = f.readline() #read the header and assign it to header
    vars = header.split() #split header into list of strings
    # print(vars)
    
    for line in f:
        tmp = line.split()
        # print(tmp)
        year.append(int(tmp[0]))
        day.append(int(tmp[1]))
        hour.append(int(tmp[2]))
        minute.append(int(tmp[3]))
        symh.append(float(tmp[4]))

        datetime1 = dt.datetime(int(tmp[0]), 1, 1, int(tmp[2]), int(tmp[3])) + dt.timedelta(days = int(tmp[1])-1)
        print("datetime: ",datetime1)
        times.append(datetime1)
print(symh)
print(hour)
print(minute)

# time1 = dt.datetime(2013,1,3, 10,12,30)
# time2 = dt.datetime(2013,1,1,10,12,30) + dt.timedelta(days = 2)


fig = plt.figure()
plt.plot(times, symh, 'rx--')
plt.xlabel("time")
plt.ylabel("SYMH")


nLines = 0
with open("day_02/omni_min_def_eMyN4ZWsFs.lst") as f:
    # for line in f:
    #     print(line)
    year = []
    day = []
    hour = []
    minute = []
    symh = []
    times = []
    for i in range(nLines):
        print(f.readline()) #read first nlines and print but do nothing else
    header = f.readline() #read the header and assign it to header
    vars = header.split() #split header into list of strings
    # print(vars)
    
    for line in f:
        tmp = line.split()
        # print(tmp)
        year.append(int(tmp[0]))
        day.append(int(tmp[1]))
        hour.append(int(tmp[2]))
        minute.append(int(tmp[3]))
        symh.append(float(tmp[4]))

        datetime1 = dt.datetime(int(tmp[0]), 1, 1, int(tmp[2]), int(tmp[3])) + dt.timedelta(days = int(tmp[1])-1)
        # print("datetime: ",datetime1)
        times.append(datetime1)
# print(symh)
# print(hour)
# print(minute)

fig = plt.figure()
plt.plot(times, symh)
plt.xlabel("time")
plt.ylabel("SYMH")

plt.show()