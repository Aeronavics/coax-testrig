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
from file_combine import same_file_test, get_file_list

FOLDER = '\\\Coax_pre\\' 

PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.1

TOP_I_OFFSET = 0.11
BOTTOM_I_OFFSET = 0.18

def get_file_list():
    """Gets all the files from the directory"""
    file_list = list()

    with os.scandir("." + FOLDER) as entries:
        print("\nFiles found:\n")
        
        for entry in entries:
            if entry.name.endswith(".csv"):
                file_list.append(entry.name)
                print(entry.name)
            
    return file_list


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
        bottom_motor_power = row[BOTTOM_V_INDEX] * (row[BOTTOM_I_INDEX] - BOTTOM_I_OFFSET) 
        total_power = top_motor_power + bottom_motor_power 
        
        if total_power == 0:
            continue
        
        efficiency = SCALE_FACTOR * thrust / total_power
        
        if efficiency < EFFICIENCY_CUTOFF:
            continue
        
        thrust_list.append(thrust)
        efficiency_list.append(efficiency)
        
    return efficiency_list, thrust_list


def data_combine(file_list):
    """"""
    all_the_data = dict()
    previous_file = ""
    previous_data = list()
    
    for filename in file_list:
        data = get_data(filename)
        bool_same_file_type = same_file_test(filename, previous_file)
        
        if bool_same_file_type == True:
            
            for row in data:
                previous_data.append(row)
                
            previous_data.sort()
            previous_data = give_average_data(previous_data)
            all_the_data[previous_file] = previous_data
            
        else:
            all_the_data[filename] = data
            previous_data = data
            previous_file = filename
            
            
    return all_the_data
        

def do_plot_TvsE(file_dict):
    """Sets up data to be plotted for thrust against efficiency"""
    total_thrust_list = list()
    total_efficiency_list = list()
    
    title = str(input("\nWhat should the title for this graph be: "))
    
    
    for test in file_dict.items():
        
        efficiency_list, thrust_list = efficiency_and_thrust_find(test[1])
        total_thrust_list.append(thrust_list)
        total_efficiency_list.append(efficiency_list)
        
    efficiency_to_thrust_plot(total_thrust_list, total_efficiency_list, file_dict, title)
    

def analysis_main():
    """main func that will direct all others in analysis"""
    file_list = get_file_list()
    combined_data_dict = data_combine(file_list)
    print(f"\n\n{combined_data_dict.keys()}\n\n")
  
    plot_E = ask_user("\nDo you want to plot efficiency against thrust?")
    if plot_E == True:
        do_plot_TvsE(combined_data_dict)
    
    
analysis_main()
