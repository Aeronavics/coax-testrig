# =========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 30/11/22
# PURPOSE       : Checks the data is in expected format and
#                 removes non int and float data
#               
# ========================================================


# Library Imports
from colorama import Fore
import os
from typing import Union

EXPECTED_LABEL = "Motor PWM"            # This is the first expected label


EXPECTED_HEADER = ['Motor PWM', ' Top Voltage (V)', ' Bottom Voltage (V)', ' Top Current (A)', ' Bottom Current (A)', ' Thrust (kg)']
EXPECTED_ROW_SIZE = 6

LF = list[float]

def error_check(raw_data: list[Union[LF, list[str], str]], filename: str) -> list[Union[LF, list[str], str]]:
    """ Removes all non int or float data except the header and time data

    Args:
        raw_data (list[Union[LF, list[str], str]]): All elements from original file in 2d list
        filename (str): Name of the file the data belongs to

    Returns:
        list[Union[LF, list[str], str]]: 2d list of processed data
    """
    
    processed_data = []
    row_index = 0
    
    for row in raw_data:
        add_row = True
        col_index = 0
        
        # Tests for float
        while col_index < len(row) and add_row == True:
            try:
                row[col_index] = float(row[col_index])
                
            except:
                add_row = False
        
            col_index += 1
            
        
        if add_row == True:
            processed_data.append(row)
        
        elif add_row == False and (row[0] != EXPECTED_LABEL or row[0].startswith("Time:")) and row_index != 0:
            print(Fore.RED + f"\nInvalid value at row {row_index + 1}.\nThis row was removed inside {filename}\n" + Fore.RESET)
            
        elif row[0] == EXPECTED_LABEL or row[0].startswith("Time:"):
            processed_data.append(row)
            
        row_index += 1
        
    return processed_data


def header_check(data: list[LF], filename: str) -> None:
    """ Will display error message if header is not in the correct format

    Args:
        data (list[LF]): 2d list of proceeded data
        filename (str): Name of current file
    """
    header_row = data[1]
    
    try:
        assert(header_row == EXPECTED_HEADER)
        
    except:
        print(Fore.RED + f"\nERROR")
        print(f"Header from {filename} is not in the correct format")
        print(f"Expected: {EXPECTED_HEADER}\nGot: {header_row}\n" + Fore.RESET)
        os.abort()
        
          
def row_check(data: list[LF], filename: str) -> None:
    """ If rows are not of teh expected size then will display an error message

    Args:
        data (list[LF]): 2d list of proceeded data
        filename (str): Name of current file
    """
    for index, row in enumerate(data[2:]): # Skips header rows
        
        try:
            assert(len(row) == EXPECTED_ROW_SIZE)
            
        except:
            print(Fore.RED + f"\nERROR")
            print(f"Row {index + 3} is not the correct size in file {filename}")
            print(f"Expected: {EXPECTED_ROW_SIZE}\nGot: {len(row)}\nPlease check this this file and row\n" + Fore.RESET)
            
            os.abort()
          