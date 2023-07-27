import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
"""
Making function out of day 2 getting and plotting omni data
"""
__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'


def read_ascii_file_my(filename,index, header = False):
    "This reads an ascii file of omni data"
    #input = filename and index of data wanted and output = data as dictionary
    # define data (for example, a dictionary) to store variables
    #data = {'date':(), 'symh':() }
        
    with open(filename) as f:
        data = {'time': [], 'symh':[] }
        if header:
            header = f.readline()
            vars = header.split()
        for line in f:
            tmp = line.split()
            data['symh'].append(float(tmp[index]))
            datetime_ofline = dt.datetime(int(tmp[0]), 1, 1, int(tmp[2]), int(tmp[3])) + dt.timedelta(days = int(tmp[1])-1)
            data['time'].append(datetime_ofline)

    # read the ascii file
    # 1. do we need to skip any lines? No skipping lines needed
    # 2. read line by line (readline, split, convert data format, etc)
    # 3. how to construct datetime
    return data


def read_ascii_file_fordates(filename, timestart, timeend, index, header = False):
    "This reads an ascii file of omni data"
    #input = filename and index and datestart dateend wanted and output = data as dictionary
    #datestart needs to be datetime.datetime(2013, 3, 20, 23, 20) format
    # define data (for example, a dictionary) to store variables
    #data = {'date':(), 'symh':() }
    data = {'time': [], 'indexedvalue':[] }
    #get datestart --> day, hour, minute
    with open(filename) as f:
        if header:
            header = f.readline()
            vars = header.split()
        for line in f:
            tmp = line.split()
            datetime_ofline = dt.datetime(int(tmp[0]), 1, 1, int(tmp[2]), int(tmp[3])) + dt.timedelta(days = int(tmp[1])-1)
            data['indexedvalue'].append(float(tmp[index]))
            data['time'].append(datetime_ofline)
    timefull = np.array(data['time'])
    maskfortimecareabout = (timefull>timestart) & (timefull<timeend)
    selectedtime = timefull[maskfortimecareabout]
    datafull = np.array(data['indexedvalue'])
    selecteddata = datafull[maskfortimecareabout]
    data['indexedvalue'] = selecteddata
    data['time'] =selectedtime
    return data




#--- This is the main code ----------------
if __name__ == '__main__':
    # file_data0 =(read_ascii_file_my('day_02/omni_min_def_eMyN4ZWsFs.lst',4))
    # fig = plt.figure()
    # plt.plot(file_data0['time'], file_data0['symh'])
    # plt.xlabel("time")
    # plt.ylabel("SYMH")

    # datestart1 = dt.datetime(2013, 3, 16, 20, 19)
    # dateend1 = dt.datetime(2013, 3, 19, 1, 56)
    # file_data =(read_ascii_file_fordates('day_02/omni_min_def_eMyN4ZWsFs.lst',datestart1, dateend1, 4))
    
    # fig = plt.figure()
    # plt.plot(file_data['time'], file_data['indexedvalue'])
    # plt.xlabel("time")
    # plt.ylabel("indexedvalue")

    # fig = plt.figure()
    # plt.plot(file_data0['time'], file_data0['symh'])
    # plt.plot(file_data['time'], file_data['indexedvalue'])
    # plt.xlabel("time")
    # plt.ylabel("indexedvalue")
    # 
    
    #find all places where data symh<100nT -->~14ish
    file_data2003 =(read_ascii_file_my('day_03/omni_min_h7Fc7_Lo3A.lst',4))
    storms2023 = []
    stormstart = []
    stormend = []
    stormstartindex = []
    stormendindex = []
    for datapoints_index in range(len(file_data2003['symh'])-1):
        if file_data2003['symh'][datapoints_index] > -100 and file_data2003['symh'][datapoints_index+1] <=-100:
            stormstart.append(file_data2003['time'][datapoints_index])
            stormstartindex.append(datapoints_index)
        if file_data2003['symh'][datapoints_index] <= -100 and file_data2003['symh'][datapoints_index+1] >-100:
            stormend.append(file_data2003['time'][datapoints_index])
            stormendindex.append(datapoints_index)
    # print("starts: ",stormstart)
    # print("ends: ",stormend)
    print("number of times stormstarts and ends: ", len(stormstart), len(stormend))
    print(stormstart[0], stormend[0])


    fig = plt.figure()
    plt.plot(file_data2003['time'], file_data2003['symh'], 'b-')
    for storms_index in range(len(stormend)):
        plt.plot(stormend[storms_index], file_data2003['symh'][stormendindex[storms_index]], 'co')
    for storms_index in range(len(stormstart)):
        plt.plot(stormstart[storms_index], file_data2003['symh'][stormstartindex[storms_index]], 'go')
        #print('storm')
        # stormdata = read_ascii_file_fordates('day_03/omni_min_h7Fc7_Lo3A.lst',stormstart[storms_index], stormend[storms_index], 4)
        # if len(stormdata['time'])>0:
        #     stormtime = stormdata['time'][0]
        #     stormmag = stormdata['indexedvalue'][0]
        #     plt.plot(stormtime, stormmag, 'co')
    plt.xlabel("time")
    plt.ylabel("indexedvalue")

    # #TIME LIMITED!!!! must be 12 hours apart
    # storms2023 = []
    # stormstart = []
    # stormend = []
    # stormstartindex = []
    # stormendindex = []
    # for datapoints_index in range(len(file_data2003['symh'])-1):
    #     #check that time of this is more than 12 hours since then
    #     if file_data2003['symh'][datapoints_index] > -100 and file_data2003['symh'][datapoints_index+1] <=-100:
    #         stormstart.append(file_data2003['time'][datapoints_index])
    #         stormstartindex.append(datapoints_index)
    #     if file_data2003['symh'][datapoints_index] <= -100 and file_data2003['symh'][datapoints_index+1] >-100:
    #         stormend.append(file_data2003['time'][datapoints_index])
    #         stormendindex.append(datapoints_index)
    # print("number of times stormstarts and ends: ", len(stormstart), len(stormend))
    # print(stormstart[0], stormend[0])
    plt.show()