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
from common_funcs import ask_user

NEAT_OFFSET = 0.3

    
def general_plotter(plotting_dict: dict, xlabel: str, ylabel: str, x_start: float, xlim_start: float, offset_multiply: float, LoBF: bool) -> None:
    """"Plots the efficiency to thrust multiple file"""
    fig, ax = plt.subplots()
    lim_x = 0
    lim_y = 0
    # LoBF = ask_user("Would you like to plot the line of best fit?")
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
    
        lim_x = max(max(TvsE_data[0]), lim_x)
        lim_y = max(max(TvsE_data[1]), lim_y)
        
        if LoBF == True: 
            plt.scatter(TvsE_data[0],TvsE_data[1], marker='o')
            x = np.linspace(x_start, max(TvsE_data[0]) , 100)
            ax.plot(x, function_sub(coefficients, x))
        else: 
            ax.plot(TvsE_data[0],TvsE_data[1], marker='o')
        
    ax.set_xlim(xlim_start, lim_x + NEAT_OFFSET * offset_multiply)
    ax.set_ylim(0, lim_y  + NEAT_OFFSET)
        
    file_list = give_file_list(plotting_dict, LoBF)
    
    ax.legend(file_list)
    ax.set_title("lol")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid()
    
    plt.show()
    

def test_plotter(plotting_dict: dict, xlabel: str, ylabel: str, x_start: float, xlim_start: float, offset_multiply: float) -> None:
    """"Plots the efficiency to thrust multiple file"""
    fig, ax = plt.subplots()
    lim_x = 0
    lim_y = 0
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
        
        # co = exp_estimate(TvsE_data)
        lim_x = max(max(TvsE_data[0]), lim_x)
        lim_y = max(max(TvsE_data[1]), lim_y)
        
        plt.scatter(TvsE_data[0],TvsE_data[1], marker='o')
        
        x = np.linspace(x_start, max(TvsE_data[0]) , 100)
        # ax.plot(x, exp_calc(co, x))
        
        ax.plot(x, function_sub(coefficients, x))
        
    ax.set_xlim(xlim_start, lim_x + NEAT_OFFSET * offset_multiply)
    ax.set_ylim(0, lim_y  + NEAT_OFFSET)
    
    file_list = list()
    
    for file in plotting_dict.keys():
        print(file)
        file_list.append(file)
        file_list.append("fitted " + file)
    
    ax.legend(file_list)
    ax.set_title("CHECK THE DATA")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid()
    
    plt.show()
