# ===============================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 21/11/22
# PURPOSE       : Initializing data set
# ===============================

import matplotlib.pyplot as pyplot
import numpy as np
import csv
from colorama import Fore, Back, Style

def file_open(file_name):
    """Opens the file and puts data into raw list"""
    
    raw_data = []
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            raw_data.append(row)
                    
    file.close()
    
    return raw_data
   
def error_check(file_name):
    """Checks raw data for errors such as non valid floats"""
    
    raw_data = file_open(file_name)
    
    processed_data = []
    row_index = 1
    
    for row in raw_data:
        
        add_row = True
        col_index = 0
        
        while col_index < len(row) and add_row == True:
            try:
                row[col_index] = float(row[col_index])
            except ValueError:
                add_row = False
        
            col_index += 1
        
        if add_row == True:
            processed_data.append(row)
        
        elif add_row == False and row_index != 1:
            print(Fore.RED + f"\nInvalid value at row {row_index} which is at time {row[0]}s.\nThis row was removed\n")
            
        row_index += 1
    return processed_data        
    
data = error_check("proto-0")
print(Fore.GREEN + f"{data}")
print(Style.RESET_ALL)