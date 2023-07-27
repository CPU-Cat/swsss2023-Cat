import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np

"""
Takes data from dataset to produce plots including tec
"""

__author__ = 'Cat'
__email__ = 'ckpawu@bu.edu'


def plot_tec(dataset, figsize = (12,6)):
    """Plots TEC from dataset
    Args:
        dataset(variable name):
            dataset retrieved from a ipe05 .nc file or location of file
        figsize(int,int) (optional):
            (default: (12,6)) size of figure to output
    
    Returns:
        figure of tec (must be shown with plt.show() after the function run)
    """
    if isinstance(dataset, str):
        dataset = nc.Dataset(dataset)
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = figsize)
    datax = dataset['lon']
    datay = dataset['lat']
    dataz = dataset['tec']
    pc = ax.pcolormesh(datax, datay, dataz)
    plt.xlabel(r'longitude ['+str(dataset['lon'].units)+']')
    plt.ylabel(r'latitude ['+str(dataset['lat'].units)+']')
    plt.title("Total Electron Counts")
    cbar = fig.colorbar(pc, ax = ax)
    cbar.ax.set_ylabel('TEC  ['+str(dataset['tec'].units)+ ']')
    return fig, ax


def plot_wam_ipe(dataset, key, figsize = (12,6)):
    """Plots key from dataset
    Args:
        dataset(variable name):
            dataset retrieved from a ipe05 .nc file or location of file
        key (string):
            key of the dataset's data want to retrieve
        figsize(int,int) (optional):
            (default: (12,6)) size of figure to output
    
    Returns:
        figure of tec (must be shown with plt.show() after the function run)
    """
    if isinstance(dataset, str):
        dataset = nc.Dataset(dataset)
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = figsize)
    datax = dataset['lon']
    datay = dataset['lat']
    dataz = dataset[key]
    pc = ax.pcolormesh(datax, datay, dataz)
    plt.xlabel(r'longitude ['+str(dataset['lon'].units)+']')
    plt.ylabel(r'latitude ['+str(dataset['lat'].units)+']')
    plt.title(str(key))
    cbar = fig.colorbar(pc, ax = ax)
    cbar.ax.set_ylabel(key+'  ['+str(dataset[key].units)+ ']')
    return fig, ax

def saveplot_wam_ipe(dataset, key, figsize = (12,6)):
    """Plots key from dataset
    Args:
        dataset(str):
            dataset retrieved from a ipe05 .nc file or location of file
        key (string):
            key of the dataset's data want to retrieve
        figsize(int,int) (optional):
            (default: (12,6)) size of figure to output
    
    Returns:
        saves figure of tec (must be shown with plt.show() after the function run)
    """
    if isinstance(dataset, str):
        filename = dataset + '.png'
    else:
        filename = 'unknown_name.png'
    plot_wam_ipe(dataset, key, figsize = (12,6))
    plt.savefig(filename, format = 'png', dpi =500)
    

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    datadata = nc.Dataset("wfs.t06z.ipe05.20230725_120500.nc")
    # plot_tec(datadata)
    datafilename = "wfs.t06z.ipe05.20230725_120500.nc"
    # plot_tec(datafilename)
    # key = 'NmF2'
    key = 'tec'
    # plot_wam_ipe(datadata, key)
    # plot_wam_ipe(datafilename, key)
    saveplot_wam_ipe(datafilename, key)
    saveplot_wam_ipe(datadata, key)
    #plt.show()

    
