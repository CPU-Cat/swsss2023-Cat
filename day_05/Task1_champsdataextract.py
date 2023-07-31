import os 
import pandas as pd
import numpy as np
"""function to open txt champ dens files from txt files given name of location
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

# def champ_dens_extraction(filename):
#     datalist = []
#     for file in os.listdir(filename):#"../Champ_dens_2002"):
#         if file.endswith(".txt"):
#             datalist.append(os.path.join(filename+'/'))#"../Champ_dens_2002/", file))
#     sortedChampdata = sorted(datalist) # or sorted(datalist2)

#     # The following code reads the first file in the sortedChampdata list.
#     header_label = ['GPS Time (sec)','Geodetic Altitude (km)','Geodetic Latitude (deg)','Geodetic Longitude (deg)','Local Solar Time (hours)','Velocity Magnitude (m/s)','Surface Temperature (K)','Free Stream Temperature (K)','Yaw (rad)','Pitch (rad)','Proj_Area_Eric (m^2)','CD_Eric (~)','Density_Eric (kg/m^3)','Proj_Area_New (m^2)','CD_New (~)','Density_New (kg/m^3)','Density_HASDM (kg/m^3)','Density_JB2008 (kg/m^3)' ]
#     df=pd.read_csv(sortedChampdata[0], delim_whitespace=True, header=None, skiprows=1)
#     df.columns = header_label
#     return df 

#print(champ_dens_extraction("../Champ_dens_2002"))


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
    lst = data_array['Local Solar Time (hours)']#find colum with lst so that find data with lst
    lat = data_array['Geodetic Latitude (deg)']
    alt = data_array['Geodetic Altitude (km)']
    gpstime = data_array['GPS Time (sec)']
    data_arrays.append([gpstime, lst, lat, alt])


# Read the trajectory data (local solar time, latitude, and altitude)
print(data_arrays)
#,Geodetic Altitude (km),Geodetic Latitude (deg),Local Solar Time (hours)