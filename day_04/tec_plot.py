from wam_ipe_plotter import plot_tec, plot_wam_ipe, saveplot_wam_ipe
import sys

filename = sys.argv[0]
dataset = sys.argv[1]
key = 'tec'
saveplot_wam_ipe(dataset, key)