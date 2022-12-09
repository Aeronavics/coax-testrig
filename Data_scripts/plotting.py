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

NEAT_OFFSET = 0.3

    
def efficiency_to_thrust_plot(plotting_dict, LoBF):
    """"Plots the efficiency to thrust multiple file"""
    fig, ax = plt.subplots()
    lim_thrust = 0
    lim_E = 0
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
        
        # co = exp_estimate(TvsE_data)
        lim_thrust = max(max(TvsE_data[0]), lim_thrust)
        lim_E = max(max(TvsE_data[1]), lim_E)
        
        plt.scatter(TvsE_data[0],TvsE_data[1], marker='o')
        
        x = np.linspace(0, max(TvsE_data[0]) , 100)
        # ax.plot(x, exp_calc(co, x))
        if LoBF == True: ax.plot(x, function_sub(coefficients, x))
        
    ax.set_xlim(0, lim_thrust + NEAT_OFFSET)
    ax.set_ylim(0, lim_E  + NEAT_OFFSET)
        
    file_list = give_file_list(plotting_dict, LoBF)
    
    ax.legend(file_list)
    ax.set_title(ask_title())
    ax.set_xlabel("Thrust (kg)")
    ax.set_ylabel("Relative Efficiency (Thrust / Power)")
    ax.grid()
    
    plt.show()


