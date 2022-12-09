# =========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : This module pulls from all other modules
#                 to do some data analysis such as finding
#                 thrust to relative efficiency
# =========================================================


# Library Imports
import os
from colorama import Fore

# Module Imports
from common_funcs import ask_user
from average_data import give_average_data
from csv_to_list import control_func
from data_check import header_check, row_check
from plotting import efficiency_to_thrust_plot
from file_combine import get_file_list, same_files

FOLDER = 'put_data_here\\' 

PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.1

TOP_I_OFFSET = 0
BOTTOM_I_OFFSET = 0


def get_data(filename):
    """Gets data and gets it error checked"""
    data =  control_func(filename, FOLDER)          
    
    # Format checks
    header_check(data)
    row_check(data)
    
    good_data = give_average_data(data[2:])
    return good_data


def efficiency_and_thrust_find(data):
    """Finds relative efficiency and thrust"""
    thrust_list = list()
    efficiency_list = list()
    

    
    for row in data:
        thrust = row[LOAD_INDEX]
        
        top_motor_power = row[TOP_V_INDEX] * (row[TOP_I_INDEX] - TOP_I_OFFSET)
        # bottom_motor_power = row[BOTTOM_V_INDEX] * (row[BOTTOM_I_INDEX] - BOTTOM_I_OFFSET) # edit for single prop
        total_power = top_motor_power #+ bottom_motor_power 
        
        if total_power == 0:
            continue
        
        # efficiency = total_power
        efficiency = SCALE_FACTOR * thrust / total_power
        
        if efficiency < EFFICIENCY_CUTOFF or efficiency > 2.5:
            continue
        
        thrust_list.append(thrust)
        efficiency_list.append(efficiency)
          
    return efficiency_list, thrust_list


def raw_data_dict(same_file_list):
    """"""
    print(same_file_list)
    all_the_data = dict()
    
    for test_types in same_file_list:
        data = None
        
        for filename in test_types:
            
            if data == None:
                data = get_data(filename)
                continue
            else:
                next_data = get_data(filename)
                
                for row in next_data:
                    data.append(row)
                    
                    
        print(Fore.CYAN + f"{data}" + Fore.RESET)
        data = give_average_data(data)
        
        print(filename)
        print(f"{data}\n")
        
            
        all_the_data[filename] = data
            
    return all_the_data
        
        
def do_plot_TvsE(file_dict, LoBF):
    """Sets up data to be plotted for thrust against efficiency"""
    plotting_dict = dict()
    
    title = str(input("\nWhat should the title for this graph be: "))
    
    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        plotting_dict[file_name] = [thrust_list, efficiency_list]
        print(data)
        
    print(f"\n{plotting_dict}\n")
        
    efficiency_to_thrust_plot(plotting_dict, title, LoBF)
    

def analysis_main():
    """main func that will direct all others in analysis"""
    file_list = get_file_list()
    same_file_list = same_files(file_list)

    combined_data_dict = raw_data_dict(same_file_list)
    print(f"\n\n{combined_data_dict.keys()}\n\n")
  
    plot_E = ask_user("\nDo you want to plot efficiency against thrust?")
    
    if plot_E == True:
        LoBF = ask_user("\nDo you want to plot the lines of best fit too?")
        do_plot_TvsE(combined_data_dict, LoBF)
    
    
analysis_main()
