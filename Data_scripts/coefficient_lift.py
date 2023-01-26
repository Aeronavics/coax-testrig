import numpy as np
import matplotlib.pyplot as plt

from plotter_helper import give_file_list
from data_functions import give_PWM_list, give_current_offset
from analysis import give_same_file_list, give_combined_data_dict

INCH_TO_MM_C = 39.37
ACCEL_GRAVITY = 9.81
ROW = 1.293
EFFICIENCY = 0.8
I_OFFSET = 0.25
LOAD_CUTOFF = 0.1

# Indexs
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

LF = list[float]


def inch_to_m(inches: float) -> float:
    """ Converts inch to mm"""
    return inches / INCH_TO_MM_C

def A_CS_find(radius_inch):
    """ Finds the cross sectional area"""
    radius_m = inch_to_m(radius_inch)
    return np.pi * (radius_m ** 2)

def calc_power(voltage: float, current: float) -> float:
    """ Calculates power via P = VI"""
    return voltage * current


def CL_find(F_T, V, I, radius_inch, current_offset):
    """ Finds the coefficient of lift"""
    A_CS = A_CS_find(radius_inch)
    power = calc_power(V, I - current_offset)
    top = 2 * ((F_T * ACCEL_GRAVITY) ** 3)
    bottom = (power ** 2) * (EFFICIENCY ** 2) * ROW * A_CS
    return top / bottom
    

def CL_sort(data, radius):
    """ sorts data for CL"""
    CL_list = list()
    current_offset = give_current_offset(data, TOP_I_INDEX)

    for row in data[1:]:
        F_T, V, I = row[LOAD_INDEX], row[TOP_V_INDEX], row[TOP_I_INDEX]
        CL = CL_find(F_T, V, I, radius, current_offset)
        CL_list.append(CL)
    
    return CL_list


def plot_s(plot_dict):
    """ Plots the data"""
    fig, ax = plt.subplots()
    
    for data in plot_dict.values():
        ax.plot(data[0], data[1], marker='o')
        
    file_list = give_file_list(plot_dict, False)
    ax.legend(file_list)
    
    ax.grid()
    ax.set_title("CL against PWM")
    ax.set_xlabel("PWM")
    ax.set_ylabel("CL")
    plt.show()


def prop_r_find(file_name):
    """finds radius of prop with relation to the file name"""
    splitted = file_name.split("-")
    radius_s = splitted[1]
    return float(radius_s) / 2


def PWMvsCL(combined_data_dict):
    """"""
    
    plotting_dict = dict()
    
    for file_name, data in combined_data_dict.items():
        radius = prop_r_find(file_name)
        PWM_list = give_PWM_list(data)
        CL_list = CL_sort(data, radius)
        
        # needed for Thrust and Efficiency cutoffs making lists not the same len()
        if len(PWM_list) > len(CL_list):
            PWM_list.pop(0)
            
        plotting_dict[file_name] = [PWM_list, CL_list]
        
    plot_s(plotting_dict)
    
    
def CL_director():
    """ Directs all functions in this module"""
    same_file_list = give_same_file_list()
    combined_data_dict = give_combined_data_dict(same_file_list)
    PWMvsCL(combined_data_dict)
    
CL_director()
    
    
