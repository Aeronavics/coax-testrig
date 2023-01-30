# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Plots data
#               
# ===================================================


# Library Imports
import numpy as np
import matplotlib.pyplot as plt

# Module Imports
from plotter_helper import *

LINE_WIDTH = 0.7

    
def general_plotter(plotting_dict: dict, labels: Graph_Labels) -> None:
    """ Plots 2 variables against each other cased on the data in the dict passed to it.
        matplotlib graph values are given by the labels.

    Args:
        plotting_dict (dict): Values that will be plotted against each other
        labels (Graph_Labels): Preset values to make the graph look nice
    """
    
    fig, ax = plt.subplots()
    lim_x = 0
    lim_y = 0
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
    
        lim_x = max(max(TvsE_data[0]), lim_x)
        lim_y = max(max(TvsE_data[1]), lim_y)
        
        if labels.LoBF == True: 
            plt.scatter(TvsE_data[0],TvsE_data[1], marker='o')
            x = np.linspace(labels.xstart, max(TvsE_data[0]) , 100)
            ax.plot(x, function_sub(coefficients, x))
            
        else: 
            ax.plot(TvsE_data[0],TvsE_data[1], marker='o')
        
    # Gets files names for legends   
    file_list = give_file_list(plotting_dict, labels.LoBF)
    ax.legend(file_list)
    
    # Sets titles and labels
    ax.set_title(labels.title)
    ax.set_xlabel(labels.xlabel)
    ax.set_ylabel(labels.ylabel)
    
    # Sets graph min and max values that will be shown
    ax.set_xlim(labels.xstart, labels.max_ytick(lim_x, labels.offset))
    ax.set_ylim(0, labels.max_ytick(lim_y, labels.offset))
    
    # Sets the grid lines and ticks for x and y
    xmajor_ticks = np.arange(labels.xstart, labels.max_xtick(lim_x, labels.offset), labels.Mxticks)
    xminor_ticks = np.arange(labels.xstart, labels.max_xtick(lim_x, labels.offset), labels.mxticks)
    
    ymajor_ticks = np.arange(0, labels.max_ytick(lim_y, labels.offset), labels.Myticks)
    yminor_ticks = np.arange(0, labels.max_ytick(lim_y, labels.offset), labels.myticks)
    
    ax.set_xticks(xmajor_ticks)
    ax.set_xticks(xminor_ticks, minor=True)
    
    ax.set_yticks(ymajor_ticks)
    ax.set_yticks(yminor_ticks, minor=True)
    
    # Specify more info about the grid lines
    ax.grid(which='minor', linewidth=LINE_WIDTH)
    ax.grid(which='major', linewidth=LINE_WIDTH, color ='#252b39')
    
    plt.show()
    