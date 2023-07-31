import os 
import pandas as pd
import numpy as np

__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'


datalist = []
for file in os.listdir("../Champ_dens_2002"):
    if file.endswith(".txt"):
        datalist.append(os.path.join("../Champ_dens_2002/", file))
sortedChampdata = sorted(datalist) # or sorted(datalist2)
print(len(sortedChampdata))
header_labels = []
data_arrays = []

for fileindex in range(len(sortedChampdata)):
    header = pd.read_csv(sortedChampdata[fileindex],  nrows=0).columns.tolist() #index_col=0,
    # header_labels.append(header)
    # print(header)
    data_array = pd.read_csv(sortedChampdata[fileindex], delim_whitespace=True, header=None, skiprows=1)
    # print('\n',data_array)
    data_array.columns = header
    # print('\n', data_array)
    hour = int(60*60/10) #every 10 seconds, want to get every hour, 60 sec per min, 60 min per hour
    lst = data_array['Local Solar Time (hours)'][::hour]#find colum with lst so that find data with lst
    lat = data_array['Geodetic Latitude (deg)'][::hour]
    alt = data_array['Geodetic Altitude (km)'][::hour]
    gpstime = data_array['GPS Time (sec)'][::hour]
    data_arrays.append([gpstime, lst, lat, alt])
     
# print(data_arrays)

print('single arrays')
print(data_arrays[49][1][360]) #[day][gpstime lst lat alt list][og index is key]
print("day 40, hour 5, hour yearly and og index")
print(40*24, 5*60*60/10, 40*24+5)
#960, 1800, 965
print(int(965/24), 965%24, 60*60/10*(965%24))