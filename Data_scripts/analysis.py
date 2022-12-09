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

PATH = '..\\Data_scripts\\'     # Change to what path your folder is in (MACS use '/')
FOLDER = 'Coax_pre\\'           # Change to what folder your data is in

PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.1


def get_data(filename):
    """Gets data and gets it error checked"""
    data =  control_func(filename, PATH, FOLDER)          
    
    # Format checks
    header_check(data)
    row_check(data)
    
    good_data = give_average_data(data[2:])
    return good_data


def efficiency_and_thrust_find(data):
    """Finds relative efficiency and thrust"""
    print(Fore.GREEN + f"{data}" + Fore.RESET)
    thrust_list = list()
    efficiency_list = list()
    
    top_I_offset = data[0][TOP_I_INDEX]
    bottom_I_offset = data[0][BOTTOM_I_INDEX]
    
    for row in data:
        thrust = row[LOAD_INDEX]
        
        top_motor_power = row[TOP_V_INDEX] * (row[TOP_I_INDEX] - top_I_offset)
        bottom_motor_power = row[BOTTOM_V_INDEX] * (row[BOTTOM_I_INDEX] - bottom_I_offset) # edit out for single prop
        total_power = top_motor_power + bottom_motor_power 
        
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
            
        all_the_data[filename] = data
            
    return all_the_data


def ask_plot_TvsE(combined_data_dict):
    """Asks the user to plot Thrust vs Efficiency"""
    plot_E = ask_user("\nDo you want to plot efficiency against thrust?")
    
    if plot_E == True:
        do_plot_TvsE(combined_data_dict)  
        

def do_plot_TvsE(file_dict):
    """Sets up data to be plotted for thrust against efficiency"""
    plotting_dict = dict()
    print(Fore.RED + f"{file_dict}" + Fore.RESET)
    
    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        plotting_dict[file_name] = [thrust_list, efficiency_list]
      
    efficiency_to_thrust_plot(plotting_dict, "Thrust (kg)", "Relative Efficiency (Thrust / Power)", 0, 0, 1)

        
def ask_plot_PWMvsE(combined_data_dict):
    """Asks the user to plot Thrust vs Efficiency"""
    plot_E = ask_user("\nDo you want to plot efficiency against PWM?")
    
    if plot_E == True:
        do_plot_PWMvsE(combined_data_dict)        
              

def do_plot_PWMvsE(file_dict):
    """ Sets up data to be plotted for PWM against E""" 
    plotting_dict = dict()
    
    
    for file_name, data in file_dict.items():
        efficiency_list, dw = efficiency_and_thrust_find(data)
        PWM_list = []
        for row in data:
            PWM_list.append(row[0])
        plotting_dict[file_name] = [PWM_list, efficiency_list]
        PWM_list.pop(0)
    
    
        
    efficiency_to_thrust_plot(plotting_dict, "PWM", "Relative Efficiency (Thrust / Power)", 1000, 1000, 50)  
    
def ask_plot_PWMvsT(combined_data_dict):
    """Asks the user to plot Thrust vs PWM"""
    plot_E = ask_user("\nDo you want to plot Thrust against PWM?")
    
    if plot_E == True:
        do_plot_PWMvsT(combined_data_dict)        
              

def do_plot_PWMvsT(file_dict):
    """ Sets up data to be plotted for PWM against Thrust""" 
    plotting_dict = dict()
    
    
    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        PWM_list = []
        for row in data:
            PWM_list.append(row[0])
        plotting_dict[file_name] = [PWM_list, thrust_list]
        PWM_list.pop(0)
    
    
        
    efficiency_to_thrust_plot(plotting_dict, "PWM", "Thrust (kg)", 1000, 1000, 50)  

    

def analysis_main():
    """main func that will direct all others in analysis"""
    file_list = get_file_list(FOLDER)
    same_file_list = same_files(file_list)

    combined_data_dict = raw_data_dict(same_file_list)
    print(f"\n\n{combined_data_dict.keys()}\n\n")
  
    ask_plot_TvsE(combined_data_dict)
    ask_plot_PWMvsE(combined_data_dict)
    ask_plot_PWMvsT(combined_data_dict)
    
analysis_main()
