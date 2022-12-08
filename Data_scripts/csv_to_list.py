# ================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 21/11/22
# PURPOSE       : Initializing data set from .csv into list format
#                 Also does some basic error checking such as
#                 Checks if elements are floats
# ================================================================

# Library Imports
import csv
from colorama import Fore

# SET UP FOR WINDOWS
# PATH = '..\\Data_scripts\\put_data_here\\'            
PATH = '..\\Data_scripts\\'

EXPECTED_LABEL = "Motor PWM"            # This is the first label you expect to see
                                       

def file_open(file_name, folder):
    """Opens the file and puts data into raw list"""
    
    raw_data = []
    
    with open(PATH + folder +  file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
                    
    file.close()
    
    return raw_data
   
   
def error_check(raw_data):
    """ Checks raw data for errors such as non valid floats
        This pretty much deletes any rows that are not of type int or float
        with the exception of the header with time and info"""
    processed_data = []
    row_index = 0
    
    for row in raw_data:
        
        add_row = True
        col_index = 0
        
        # Tests for float
        while col_index < len(row) and add_row == True:
            try:
                row[col_index] = float(row[col_index])
            except ValueError:
                add_row = False
        
            col_index += 1
        
        if add_row == True or row[0] == EXPECTED_LABEL or row[0].startswith("Time:"):
            processed_data.append(row)
        
        elif add_row == False and row_index != 0:
            print(Fore.RED + f"\nInvalid value at row {row_index}.\nThis row was removed\n")
            
        row_index += 1
    return processed_data     

   
def control_func(file_name, folder):
    """ LINKER FUNCTION
        Links functions inside this module"""
    raw_data = file_open(file_name, folder)   
    data = error_check(raw_data)
    return data
    