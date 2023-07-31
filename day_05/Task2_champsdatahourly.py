import os 
import pandas as pd

datalist = []
for file in os.listdir("../Champ_dens_2002"):
    if file.endswith(".txt"):
        datalist.append(os.path.join("../Champ_dens_2002/", file))
sortedChampdata = sorted(datalist) # or sorted(datalist2)

# The following code reads the first file in the sortedChampdata list.
header_label = ['GPS Time (sec)','Geodetic Altitude (km)','Geodetic Latitude (deg)','Geodetic Longitude (deg)','Local Solar Time (hours)','Velocity Magnitude (m/s)','Surface Temperature (K)','Free Stream Temperature (K)','Yaw (rad)','Pitch (rad)','Proj_Area_Eric (m^2)','CD_Eric (~)','Density_Eric (kg/m^3)','Proj_Area_New (m^2)','CD_New (~)','Density_New (kg/m^3)','Density_HASDM (kg/m^3)','Density_JB2008 (kg/m^3)' ]
df=pd.read_csv(sortedChampdata[0], delim_whitespace=True, header=None, skiprows=1)
df.columns = header_label
# df.head()


