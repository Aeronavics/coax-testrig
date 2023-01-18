# ================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 21/11/22
# PURPOSE       : Initializing data set from .csv into list format
#              
# ================================================================

# Library Imports
import csv
from colorama import Fore
from typing import Union
from os import abort

EXPECTED_LABEL = "Motor PWM"            # This is the first label you expect to see
                                       
LF = list[float]

def file_open(file_name: str, folder_path: str) -> list[Union[LF, list[str], str]]:
    """ Opens file and returns a 2d list of ALL elements in the file

    Args:
        file_name (str): Name of file to be opened
        folder_path (str): Path to where your csv files are

    Returns:
        2d list with ALL elements in file
    """
    
    raw_data = []
    
    with open(folder_path +  file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
                    
    file.close()
    
    return raw_data    

   
def control_func(file_name: str, folder_path: str) -> list[Union[LF, list[str], str]]:
    """ Handles the Exception cases from the file_open function

    Args:
        file_name (str): Name of file to be opened
        folder_path (str): Path to where your csv files are

    Returns:
        raw_data: 2d list with ALL elements in file
    """
    
    try:
        raw_data = file_open(file_name, folder_path)   
        return raw_data
    
    except FileNotFoundError:
        print(Fore.RED + f"\nERROR\nSomething went wrong when trying to convert {file_name} to a list.")
        print(f"Got FileNotFoundError\nCheck 'FOLDER_PATH' on line 23 and 24 in analysis.py")
        print(f"FOLDER_PATH = {folder_path}\n" + Fore.RESET)
    
    except:
        print(Fore.RED + f"\nERROR\nSomething went wrong when trying to convert {file_name} to a list.")
    
    # Same code as above but will show error message
    input("Press ENTER to see error message: ")
    raw_data = file_open(file_name, folder_path)  
   
    
    