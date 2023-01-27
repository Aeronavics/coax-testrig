# ===========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Calls all the data collection modules to 
#                 organize, filter and represent it as a dict
#
# ===========================================================


# Library Imports
from colorama import Fore
import copy

# Module Imports
from average_data import give_average_data
from csv_to_list import control_func
from data_check import error_check
from file_combine import get_file_list, same_files


# Index of where each value in a row of a csv file
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5


# Short hand as this data type is used extensively
LF = list[float]    
      
           
def get_data(filename: str, folder_path: str) -> list[LF]:
    """ Gets data from file and converts to a 2d list. Calls data checks as well

    Args:
        filename (str): Current file name that is to be opened
        folder_path (str): Path where csv data files are located

    Returns:
        good_data (list[LF]): 2d list with data from file. Each new list is the next row.
    """
    
    raw_data =  control_func(filename, folder_path)     
    
    # Format checks
    data = error_check(raw_data, filename)
    
    good_data = give_average_data(data[2:])
    return good_data


def raw_data_dict(file_list: list[list], folder_path: str) -> dict[str, list[LF]]:
    """ Takes each file and if of same test type will call functions to average it
        and will append it to a dict where the key is the file name and data is
        a 2D list where each list element is the averaged result ata specific PWM

    Args:
        file_list (list[str]): 2d list. Each sublist are files of same test type
        folder_path (str): Path where csv data files are located

    Returns:
        dict[str, list[LF]]: Dictionary where each key is the corresponding test_type
        and the value is a 2d list of the data
    """
        
    all_the_data = dict()
    
    for test_types in file_list:
        data = None
        
        for filename in test_types:
            
            if data == None:
                data = get_data(filename, folder_path)
                continue
            else:
                next_data = get_data(filename, folder_path)
                
                for row in next_data:
                    data.append(row)
                    
        data = give_average_data(data)
            
        all_the_data[filename] = data
        
 
    return all_the_data      


def raw_data_dict_check(file_list: list[list[str]], folder_path: str) -> list[dict[str,list[LF]]]:
    """ Creates a dict of all same test type against each other so it can be easily checked for errors

    Args:
        file_list (list[list[str]]): 2d list. Each sublist are files of same test type
        folder_path (str): Path where csv data files are located

    Returns:
        list[dict[str,list[LF]]]: Dict where keys are file name and values is the data
    """
    
    data_list = []
    
    for test_types in file_list:
        data_to_check = dict()
        
        for filename in test_types:  
            data = get_data(filename, folder_path)
            data_to_check[filename] = data
        
        dictcpy = copy.deepcopy(data_to_check)
    
        data_list.append(dictcpy)

    
    return data_list

  
def give_same_file_list(folder_path) -> list[str]:
    """ Returns a 2d list of all csv files found. Each sublist contains
        tests of same type

    Args:
        folder_path (str): Path where csv data files are located

    Returns:
        2d list of files where each sub list contains tests of the same type
    """
    
    file_list = get_file_list(folder_path)
    same_file_list = same_files(file_list)
    
    # Graphs same test against each other for manual error checking
    
    return same_file_list


def give_combined_data_dict(same_file_list, folder_path):
    """ Returns the main data"""
    
    combined_data_dict = raw_data_dict(same_file_list, folder_path)
    return combined_data_dict
    

