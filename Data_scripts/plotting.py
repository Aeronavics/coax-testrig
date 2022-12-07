# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Plots data
#               
# ===================================================


# Library Imports
import numpy as np
import matplotlib.pyplot as plt

NEAT_OFFSET = 0.3

def give_file_list(plotting_dict):
    """Gives file list based onb dict passed to plotting function"""
    file_list = list()
    for file in plotting_dict.keys():
        file = file.split("#")
        file[0] = file[0].rstrip(file[0][-1])
        file_list.append(file[0])
        file_list.append("fitted " + file[0])
    
    return file_list


def least_squares_estimate(data):
    """Find an N degree polynomial fit for teh data""" 
    x = data[0]
    y = data[1]
    coefficients = np.polyfit(x, y, 4)
    
    return np.flip(coefficients)


def function_sub(coefficients, x):
    """subs coefficients into equation"""
    size = len(coefficients)
    y = 0
    for i in range(0, size):
        y += coefficients[i] * (x ** i)
    
    return y
    
    
def efficiency_to_thrust_plot(plotting_dict, title):
    """"Plots the efficiency to thrust multiple file"""
    
    i = 0
    fig, ax = plt.subplots()
    lim_thrust = 0
    lim_E = 0
    
    x = np.linspace(0, 3, 100)
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
        
        
        ax.plot(TvsE_data[0],TvsE_data[1], marker="o")
        ax.plot(x, function_sub(coefficients, x))
        lim_thrust = max(max(TvsE_data[0]), lim_thrust)
        lim_E = max(max(TvsE_data[1]), lim_E)
        
    ax.set_xlim(0, lim_thrust + NEAT_OFFSET)
    ax.set_ylim(0, lim_E  + NEAT_OFFSET)
        
    file_list = give_file_list(plotting_dict)
    
    ax.legend(file_list)
    ax.set_title(title)
    ax.set_xlabel("Thrust (kg)")
    ax.set_ylabel("Relative Efficiency (Thrust / Power)")
    ax.grid()
    
    plt.show()

    