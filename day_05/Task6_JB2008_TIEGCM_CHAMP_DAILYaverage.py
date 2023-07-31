import os 
import pandas as pd
import numpy as np
from scipy.io import loadmat
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt
import h5py


__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'


datalist = []
for file in os.listdir("../Champ_dens_2002"):
    if file.endswith(".txt"):
        datalist.append(os.path.join("../Champ_dens_2002/", file))
sortedChampdata = sorted(datalist) # or sorted(datalist2)

header_labels = []
data_arrays = []

# Density_Eric (kg/m^3),Density_New (kg/m^3),
# Density_HASDM (kg/m^3),Density_JB2008 (kg/m^3) 
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
    accel_dens = data_array['Density_New (kg/m^3)'][::hour] #Density_New (kg/m^3)
    data_arrays.append([gpstime, lst, lat, alt, accel_dens])#, hourtime])

#print(data_arrays[1][4][7200])

localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
JB2008times = 8760 #every hour in a year!


loaded_data = loadmat('../2002_JB2008_density')
JB2008_dens = loaded_data['densityData']

nofAlt_JB2008 = altitudes_JB2008.shape[0]
nofLst_JB2008 = localSolarTimes_JB2008.shape[0]
nofLat_JB2008 = latitudes_JB2008.shape[0]
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008,8760), order='F')

#############################################
loaded_data = h5py.File('../2002_TIEGCM_density.mat')
# This is a HDF5 dataset object, some similarity with a dictionary
tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T # convert from g/cm3 to kg/m3
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]
time_array_JB2008 = np.linspace(0,8759,5, dtype = int)
# We will be using the same time index as before.
time_array_tiegcm = time_array_JB2008
# Each data correspond to the density at a point in 3D space. 
# We can recover the density field by reshaping the array.
# For the dataset that we will be working with today, you will need to reshape them to be lst x lat x altitude
tiegcm_dens_reshaped = np.reshape(tiegcm_dens,(nofLst_tiegcm,nofLat_tiegcm,nofAlt_tiegcm,8760), order='F')

#############################################


champtimes = 50*24-1 #50 days only, 24 hours/day, jb2008 need hour input
JB2008_dens_champs_traj = np.zeros(champtimes)
TIEGCM_dens_champs_traj = np.zeros(champtimes)
# CHAMP_dens= np.zeros(champtimes)

for time_index in range(champtimes): #for each hour, interpolate 3D, use location of champ 
    JBdens_interp = RegularGridInterpolator((localSolarTimes_JB2008, latitudes_JB2008, altitudes_JB2008), JB2008_dens_reshaped[:,:,:,time_index], bounds_error=False, fill_value=None)
    TIEGCM_interp = RegularGridInterpolator((localSolarTimes_tiegcm, latitudes_tiegcm, altitudes_tiegcm), tiegcm_dens_reshaped[:,:,:,time_index], bounds_error=False, fill_value=None)
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
    TIEGCM_dens_champs_traj[time_index] = TIEGCM_interp(trajlocate)
    # CHAMP_dens[time_index] = data_arrays[day][4][og_index]
    # print(CHAMP_dens[time_index])
CHAMP_dens = []
for i in range(50):
    for j in data_arrays[i][4]:
        if (len(CHAMP_dens)<1199):
            CHAMP_dens.append(j)

# print('CHAMP', CHAMP_dens)
times = range(champtimes)
print(len(JB2008_dens_champs_traj), len(TIEGCM_dens_champs_traj))
plt.figure()
plt.plot(times, CHAMP_dens, '--', label = 'CHAMP')
plt.plot(times, JB2008_dens_champs_traj, label = 'JB2008')
plt.plot(times, TIEGCM_dens_champs_traj, label = 'TIEGCM')
plt.title('In Situ and modeled density along champ trajectory')
plt.ylabel('density')
plt.xlabel('hour in 50 days')
plt.legend()

CHAMP_dens_ave = []
JB_dens_ave = []
TIE_dens_ave = []
times_ave = range(50)
for ave_ind in range(len(times)):
    if ave_ind %24 == 0 and ave_ind != 0:
        CHAMP_track = CHAMP_track/24
        JB2008_track = JB2008_track/24
        TIE_track = TIE_track/24
        CHAMP_dens_ave.append(CHAMP_track)
        JB_dens_ave.append(JB2008_track)
        TIE_dens_ave.append(TIE_track)
        CHAMP_track = 0
        JB2008_track = 0
        TIE_track = 0
    CHAMP_track = CHAMP_track +CHAMP_dens[ave_ind]
    JB2008_track = JB2008_track+JB2008_dens_champs_traj[ave_ind]
    TIE_track = TIE_track+ TIEGCM_dens_champs_traj[ave_ind]
    
    


plt.figure()
plt.plot(times, CHAMP_dens_ave, '--', label = 'CHAMP')
plt.plot(times, JB_dens_ave, label = 'JB2008')
plt.plot(times, TIE_dens_ave.append, label = 'TIEGCM')
plt.title('Daily averaged density in situ and models')
plt.ylabel('density')
plt.xlabel('Days')
plt.legend()


plt.show()

