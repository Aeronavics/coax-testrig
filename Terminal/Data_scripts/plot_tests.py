# ===========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 27/1/23
# PURPOSE       : Plots the test data with a number of combos
#                 of variables
#               
#                 EXECUTE THIS CODE TO SEE TEST PLOTS
#
# ===========================================================

# Library Imports
from typing import Callable

# Module Imports
from plotter_helper import Graph_Labels
from data_sort import give_same_file_list, give_combined_data_dict, raw_data_dict_check
from plotting import general_plotter
from data_functions import give_thrust_list, give_efficiency_list, give_power_list, give_PWM_list


LF =list[float]

# Label settings used for each graph type
PWM_vs_T_Labels = Graph_Labels( "PWM against Thrust", "PWM", "Thurst (kg)", 1000, 50, True, 100, 25, 1, 0.25, 1)
PWM_vs_E_Labels =  Graph_Labels("PWM against Efficiency", "PWM", "Relative Efficiency (Thrust / Power)", 1000, 50, True, 100, 25, 0.5, 0.125, 1)
T_vs_E_Labels =  Graph_Labels( "Thrust against Efficiency", "Thrust (kg)", "Relative Efficiency (Thrust / Power)", 0, 1, True, 1, 0.25, 0.5, 0.125, 0.15)
T_vs_P_Labels = Graph_Labels("Thrust against Power", "Power (W)", "Thrust (kg)", 0, 1, True, 200, 50, 1, 0.25, 0.5)
Compare_plots_Labels = Graph_Labels( "CHECK THE DATA", "Thrust (kg)", "Relative Efficiency (Thrust / Power)", 0, 1, True, 1, 0.25, 0.5, 0.125, 0.15)

# Where desired csv files are located
PATH_SLASHES = "\\"                             # CHANGE IF ON MAC OR LINUX      (MAC's use '/') 
FOLDER_PATH = '..' + PATH_SLASHES + 'Data_scripts' + PATH_SLASHES + 'Data' + PATH_SLASHES  + "Testing 260123.csv" + PATH_SLASHES  #+'Single prop' + PATH_SLASHES + '160 old' + PATH_SLASHES
# Change to what path your folder is in (MACS use '/')


def plot_data_check(file_dict: dict[str, list[LF]]) -> None:
    """ Plots the data from the same test type

    Args:
        file_dict (dict[str, list[LF]]):  Dict containing files of same test type.
                                          Dict where keys are file name and values is the data
    """
    plotting_dict = dict()
    
    for file_name, data in file_dict.items():
        efficiency_list = give_efficiency_list(data)
        thrust_list = give_thrust_list(data)
        plotting_dict[file_name] = [thrust_list, efficiency_list]
      
    general_plotter(plotting_dict, Compare_plots_Labels)
    

def data_check(same_file_list: list) -> None:
    """ Controls data flow for data check between same tests

    Args:
        same_file_list (list): 2d list. Each sublist are files of same test type
    """
    file_dict = raw_data_dict_check(same_file_list, FOLDER_PATH)

    for file in file_dict:
        plot_data_check(file)


def get_ready_plot(file_dict: dict[str, list[LF]], x_func: Callable[[list[LF]], LF], y_func: Callable[[list[LF]], LF], labels: Graph_Labels) -> None:
    """ General way of processing the data for specific graphs without the need of many functions.

    Args:
        file_dict (dict[str, list[LF]]):Dict containing files of same test type.
                                        Dict where keys are file name and values is the data
        x_func (function):  Function that uses data to give the x data point
        y_func (function):  Function that uses data to give the y data point
        labels (Graph_Labels): The graph labels and presets to be used with that graph
    """
    
    plotting_dict = dict()
    
    for file_name, data in file_dict.items():
        x_list = x_func(data)
        y_list = y_func(data)
        
        # needed for Thrust and Efficiency cutoffs making lists not the same len()
        if len(x_list) > len(y_list):
            x_list.pop(0)
            
        plotting_dict[file_name] = [x_list, y_list]
        
    general_plotter(plotting_dict, labels)



def plot_tests():
    """ Main function that calls functions to give the data dict.
        Then plots the data"""
    same_file_list =  give_same_file_list(FOLDER_PATH)
    combined_data_dict = give_combined_data_dict(same_file_list, FOLDER_PATH)
    
    data_check(same_file_list)  
    
    # Comment out graphs you dont want
    # get_ready_plot(combined_data_dict, give_PWM_list, give_thrust_list, PWM_vs_T_Labels)
    # get_ready_plot(combined_data_dict, give_PWM_list, give_efficiency_list, PWM_vs_E_Labels)
    get_ready_plot(combined_data_dict, give_thrust_list, give_efficiency_list, T_vs_E_Labels)
    get_ready_plot(combined_data_dict, give_power_list, give_thrust_list, T_vs_P_Labels)

plot_tests()