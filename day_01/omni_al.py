import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from swmfpy.web import get_omni_data

#!/usr/bin/env python
"""Space 477: Python: II

Use OMNI data from swmfpy.web to plot auroral electrojet index Cat's birthday plotting
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'

#start at birthday and go until next day so when grab data, it covers 24hours
start_time = datetime(1997, 6, 12) 
end_time = datetime(1997, 6,13) 
data = get_omni_data(start_time, end_time) #data = dictionary with information from OMNI from start_time to end_time
timerange = data['times'] #timerange from start_time to end_time that matches rest of data in OMNI
AL_data = data['al'] #auroral electroject index corresponding to timerange

#plot data of time and ALdata with axes and title 
plt.figure()
plt.plot(timerange, AL_data)
plt.xlabel(r'time [month-day hour UTC]')
plt.ylabel(r'AL [nT]')
plt.title("Cat's Birthday's OMNI auroral electrojet index")
plt.show()