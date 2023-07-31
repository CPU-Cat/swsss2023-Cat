import os 
import pandas as pd
import numpy as np
from scipy.io import loadmat
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt


__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'


datalist = []
for file in os.listdir("../Champ_dens_2002"):
    if file.endswith(".txt"):
        datalist.append(os.path.join("../Champ_dens_2002/", file))
sortedChampdata = sorted(datalist) # or sorted(datalist2)

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
    #hourtime = np.array(data_array['GPS Time (sec)'][::hour])/(60*60)+fileindex*24
    data_arrays.append([gpstime, lst, lat, alt])#, hourtime])
# print(data_arrays)


loaded_data = loadmat('../2002_JB2008_density')
# print (loaded_data)
# Uses key to extract our data of interest
JB2008_dens = loaded_data['densityData']
localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
nofAlt_JB2008 = altitudes_JB2008.shape[0]
nofLst_JB2008 = localSolarTimes_JB2008.shape[0]
nofLat_JB2008 = latitudes_JB2008.shape[0]
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008,8760), order='F')
JB2008times = 8760 #every hour in a year!
champtimes = 50*24-1 #50 days only, 24 hours/day, jb2008 need hour input
JB2008_dens_champs_traj = np.zeros(champtimes)
for time_index in range(champtimes): #for each hour, interpolate 3D, use location of champ 
    JBdens_interp = RegularGridInterpolator((localSolarTimes_JB2008, latitudes_JB2008, altitudes_JB2008), JB2008_dens_reshaped[:,:,:,time_index], bounds_error=False, fill_value=None)
    #time_index is every hour of champtime 50 days
    #[day][gpstime lst lat alt list][og index is key]
    day = int(champtimes/24)
    mod_hour = champtimes % 24
    og_index = int(mod_hour*60*60/10)
    lst = data_arrays[day][1][og_index]
    lat = data_arrays[day][2][og_index]
    alt = data_arrays[day][3][og_index]
    trajlocate = (lst,lat,alt )#location of champ at time of jb2008
    JB2008_dens_champs_traj[time_index] = JBdens_interp(trajlocate)

times = range(champtimes)
density = JB2008_dens_champs_traj
print(len(density))
plt.figure()
plt.plot(times, density)
plt.title('JB2008 model 2002 champ trajectory')
plt.ylabel('density')
plt.xlabel('hour in 50 days')
plt.show()
