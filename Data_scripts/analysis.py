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

# Module Imports
from average_data import give_average_data
from csv_to_list import control_func
from data_check import header_check, row_check, error_check
from plotting import general_plotter, test_plotter
from plotter_helper import Graph_Labels
from file_combine import get_file_list, same_files

# Where desired csv files are located
PATH = '..\\Data_scripts\\'     # DOne change this!!!! (MAC's use '/')
FOLDER = 'Data\\Motor Config\\160-160vs160-220\\'   # Change to what path your folder is in (MACS use '/')

# Index of where each value in a row of a csv file
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

# Constants
SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.1

# Label settings used for each graph type
PWM_vs_T_Labels = Graph_Labels("PWM", "Thurst (kg)", 1000, 50, True, 100, 25, 1, 0.25)
PWM_vs_E_Labels =  Graph_Labels("PWM", "Relative Efficiency (Thrust / Power)", 1000, 50, True, 100, 25, 0.5, 0.125)
T_vs_E_Labels =  Graph_Labels("Thrust (kg)", "Relative Efficiency (Thrust / Power)", 0, 1, True, 1, 0.25, 0.5, 0.125)
T_vs_P_Labels = Graph_Labels("Thrust (kg)", "Power (W)", 0, 1, True, 1, 0.25, 200, 50)

# Short hand as this data type is used extensively
LF = list[float]    
    

def get_data(filename: str) -> list[LF]:
    """ Gets data from file and converts to a 2d list. Calls data checks as well

    Args:
        filename (str): Current file name that is to be opened

    Returns:
        good_data (list[LF]): 2d list with data from file. Each new list is the next row.
    """
    
    raw_data =  control_func(filename, PATH, FOLDER)     
    
    # Format checks
    data = error_check(raw_data)
    header_check(data, filename)
    row_check(data, filename)
    
    good_data = give_average_data(data[2:])
    return good_data

def power_find(data: list[LF]) -> list[LF]:
    """Finds relative efficiency and thrust"""
    power_list = list()
    
    top_I_offset = data[0][TOP_I_INDEX]
    bottom_I_offset = data[0][BOTTOM_I_INDEX]

    
    for row in data:
        top_motor_power = row[TOP_V_INDEX] * (row[TOP_I_INDEX] - top_I_offset)
        bottom_motor_power = row[BOTTOM_V_INDEX] * (row[BOTTOM_I_INDEX] - bottom_I_offset) # edit out for single prop
        total_power = top_motor_power + bottom_motor_power
        
        if total_power == 0:
            continue
        
        power_list.append(total_power)
        
    return power_list


def efficiency_and_thrust_find(data: list[LF]) -> tuple[LF, LF]:
    """ Calculates the relative efficient with the corresponding thrust output.
    
        Note: If you are doing single prop testing you may want to only include
        motor you are using as part of your calculations. This means only including
        the motor you are using foe the total power variable.

    Args:
        data (list[LF]): The data ready to be used

    Returns:
        tuple[LF, LF]: Relative efficient with the corresponding thrust output
    """
    
    thrust_list = list()
    efficiency_list = list()
    
    top_I_offset = data[0][TOP_I_INDEX]
    bottom_I_offset = data[0][BOTTOM_I_INDEX]

    
    for row in data:
        thrust = row[LOAD_INDEX]
        
        top_motor_power = row[TOP_V_INDEX] * (row[TOP_I_INDEX] - top_I_offset)
        bottom_motor_power = row[BOTTOM_V_INDEX] * (row[BOTTOM_I_INDEX] - bottom_I_offset) # edit out for single prop
        total_power = top_motor_power + bottom_motor_power
        
        # total_power = bottom_motor_power
        
        if total_power == 0:
            continue
        
        efficiency = SCALE_FACTOR * (thrust / total_power)
        
        if efficiency < EFFICIENCY_CUTOFF or efficiency > 2.5:
            continue
        
        thrust_list.append(thrust)
        efficiency_list.append(efficiency)
          
    return efficiency_list, thrust_list


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
        
        print(all_the_data)
 
    return all_the_data      
              

def do_plot_PWMvsE(file_dict: dict[str, list[LF]]) -> None:
    """ Collects the necessary data to plot PWM against efficiency

    Args:
        file_dict (dict[str, list[LF]]): Dictionary where each key is the corresponding test_type
                                         and the value is a 2d list of the data
    """
    
    plotting_dict = dict()
    
    for file_name, data in file_dict.items():
        efficiency_list, dw = efficiency_and_thrust_find(data)
        PWM_list = []
        
        for row in data:
            PWM_list.append(row[0])
        plotting_dict[file_name] = [PWM_list, efficiency_list]
        PWM_list.pop(0) # DANGER LINE. Assuming the first value will not be included

    general_plotter(plotting_dict,PWM_vs_E_Labels)  
    

def do_plot_PWMvsT(file_dict: dict[str, list[LF]]) -> None:
    """ Collects the necessary data to plot PWM against Thrust

    Args:
        file_dict (dict[str, list[LF]]): Dictionary where each key is the corresponding test_type
                                         and the value is a 2d list of the data
    """
     
    plotting_dict = dict()
    
    
    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        PWM_list = []
        
        for row in data:
            PWM_list.append(row[0])
            
            
        plotting_dict[file_name] = [PWM_list, thrust_list]
        PWM_list.pop(0) # DANGER LINE. Assuming the first value will not be included
        
    general_plotter(plotting_dict, PWM_vs_T_Labels)  
 
    
def do_plot_TvsE(file_dict: dict[str, list[LF]]) -> None:
    """ Collects the necessary data to plot Thrust against Efficiency

    Args:
        file_dict (dict[str, list[LF]]): Dictionary where each key is the corresponding test_type
                                         and the value is a 2d list of the data
    """
    
    plotting_dict = dict()

    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        plotting_dict[file_name] = [thrust_list, efficiency_list]
        
      
    general_plotter(plotting_dict, T_vs_E_Labels)


def do_plot_TvsP(file_dict: dict[str, list[LF]]) -> None:
    """ Collects the necessary data to plot Thrust against Power

    Args:
        file_dict (dict[str, list[LF]]): Dictionary where each key is the corresponding test_type
                                         and the value is a 2d list of the data
    """
    
    plotting_dict = dict()

    for file_name, data in file_dict.items():
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        power_list = power_find(data)
        plotting_dict[file_name] = [thrust_list, power_list]
        
      
    general_plotter(plotting_dict, T_vs_P_Labels)


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
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
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

    
def analysis_main() -> None:
    """ Main func that will direct all others in this module"""
    file_list = get_file_list(FOLDER)
    same_file_list = same_files(file_list)
    
    combined_data_dict = raw_data_dict(same_file_list)
    
    data_check(same_file_list)  # Remove if confident in data

    do_plot_PWMvsE(combined_data_dict)
    do_plot_PWMvsT(combined_data_dict)
    do_plot_TvsE(combined_data_dict)
    do_plot_TvsP(combined_data_dict)
    
analysis_main()
