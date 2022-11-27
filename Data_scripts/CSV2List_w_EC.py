# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 21/11/22
# PURPOSE       : Initializing data set from .csv
#                 Also does some basic error checking
# ===================================================

import csv
from colorama import Fore, Back, Style

EXPECTED_LABEL = "Power1"           # This is the first label you expect to see
FILE_NAME = "PROTO-CALIBRATE-0.csv" # TEMP: This is the file you want to convert

def file_open(file_name):
    """Opens the file and puts data into raw list"""
    
    raw_data = []
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
                    
    file.close()
    
    return raw_data
   
def error_check(raw_data):
    """Checks raw data for errors such as non valid floats"""
    processed_data = []
    row_index = 0
    
    for row in raw_data:
        
        add_row = True
        col_index = 0
        
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

   
def control_func(file_name):
    """Controls data flow inside file"""
    raw_data = file_open(file_name)   
    data = error_check(raw_data)
    print(Fore.GREEN + f"{data}")
    print(Style.RESET_ALL)
    
control_func(FILE_NAME)