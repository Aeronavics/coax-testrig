# =========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : This module pulls from all other modules
#                 to do some data analysis such as finding
#                 thrust to relative efficiency.
#                 Calls plotting module to then plot the
#                 results
#
#               CODE IS EXECUTED FROM HERE!!!
# =========================================================


# Library Imports
from colorama import Fore
import copy
from typing import Callable

# Module Imports
from average_data import give_average_data
from csv_to_list import control_func
from data_check import header_check, row_check, error_check
from plotting import general_plotter, test_plotter
from plotter_helper import Graph_Labels
from file_combine import get_file_list, same_files
from data_functions import give_power_list, give_thrust_list, give_efficiency_list, give_PWM_list

# Where desired csv files are located
PATH_SLASHES = "\\"                             # CHANGE IF ON MAC OR LINUX      (MAC's use '/') 
FOLDER_PATH = '..' + PATH_SLASHES + 'Data_scripts' + PATH_SLASHES + 'Data' + PATH_SLASHES + 'Prop Config' + PATH_SLASHES + "Single prop" + PATH_SLASHES + '160' + PATH_SLASHES
# Change to what path your folder is in (MACS use '/')

# Index of where each value in a row of a csv file
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

# Constants
SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.08
LOAD_CUTOFF = 0.2

# Label settings used for each graph type
PWM_vs_T_Labels = Graph_Labels( "PWM against Thrust", "PWM", "Thurst (kg)", 1000, 50, True, 100, 25, 1, 0.25)
PWM_vs_E_Labels =  Graph_Labels("PWM against Efficiency", "PWM", "Relative Efficiency (Thrust / Power)", 1000, 50, True, 100, 25, 0.5, 0.125)
T_vs_E_Labels =  Graph_Labels( "Thrust against Efficiency", "Thrust (kg)", "Relative Efficiency (Thrust / Power)", 0, 1, True, 1, 0.25, 0.5, 0.125)
T_vs_P_Labels = Graph_Labels("Thrust against Power", "Power (W)", "Thrust (kg)", 0, 1, True, 200, 50, 1, 0.25)

# Short hand as this data type is used extensively
LF = list[float]    
      
           
def get_data(filename: str) -> list[LF]:
    """ Gets data from file and converts to a 2d list. Calls data checks as well

    Args:
        filename (str): Current file name that is to be opened

    Returns:
        good_data (list[LF]): 2d list with data from file. Each new list is the next row.
    """
    
    raw_data =  control_func(filename, FOLDER_PATH)     
    
    # Format checks
    data = error_check(raw_data, filename)
    
    good_data = give_average_data(data[2:])
    return good_data


def raw_data_dict(file_list: list[list]) -> dict[str, list[LF]]:
    """ Takes each file and if of same test type will call functions to average it
        and will append it to a dict where the key is the file name and data is
        a 2D list where each list element is the averaged result ata specific PWM

    Args:
        file_list (list[str]): 2d list. Each sublist are files of same test type

    Returns:
        dict[str, list[LF]]: Dictionary where each key is the corresponding test_type
        and the value is a 2d list of the data
    """
        
    all_the_data = dict()
    
    for test_types in file_list:
        data = None
        
        for filename in test_types:
            
            if data == None:
                data = get_data(filename)
                continue
            else:
                next_data = get_data(filename)
                
                for row in next_data:
                    data.append(row)
                    
        data = give_average_data(data)
            
        all_the_data[filename] = data
        
 
    return all_the_data      


def raw_data_dict_check(file_list: list[list[str]]) -> list[dict[str,list[LF]]]:
    """ Creates a dict of all same test type against each other so it can be easily checked for errors

    Args:
        file_list (list[list[str]]): 2d list. Each sublist are files of same test type

    Returns:
        list[dict[str,list[LF]]]: Dict where keys are file name and values is the data
    """
    
    data_list = []
    
    for test_types in file_list:
        data_to_check = dict()
        
        for filename in test_types:  
            data = get_data(filename)
            data_to_check[filename] = data
        
        dictcpy = copy.deepcopy(data_to_check)
    
        data_list.append(dictcpy)

    
    return data_list


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
      
    test_plotter(plotting_dict, T_vs_E_Labels)
    

def data_check(same_file_list: list) -> None:
    """ Controls data flow for data check between same tests

    Args:
        same_file_list (list): 2d list. Each sublist are files of same test type
    """
    file_dict = raw_data_dict_check(same_file_list)

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
        
        
def give_same_file_list() -> None:
    """ Main func that will direct all others in this module"""
    file_list = get_file_list(FOLDER_PATH)
    same_file_list = same_files(file_list)
    
    # Graphs same test against each other for manual error checking
    
    return same_file_list


def give_combined_data_dict(same_file_list):
    """ Returns the main data"""
    
    combined_data_dict = raw_data_dict(same_file_list)
    return combined_data_dict
    

def plot_tests():
    """ Plots the data"""
    same_file_list =  give_same_file_list()
    combined_data_dict = give_combined_data_dict(same_file_list)
    
    data_check(same_file_list)  
    
    # Comment out graphs you dont want
    get_ready_plot(combined_data_dict, give_PWM_list, give_thrust_list, PWM_vs_T_Labels)
    get_ready_plot(combined_data_dict, give_PWM_list, give_efficiency_list, PWM_vs_E_Labels)
    get_ready_plot(combined_data_dict, give_thrust_list, give_efficiency_list, T_vs_E_Labels)
    get_ready_plot(combined_data_dict, give_power_list, give_thrust_list, T_vs_P_Labels)

# plot_tests()
