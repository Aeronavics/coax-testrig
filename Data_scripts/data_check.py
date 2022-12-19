# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 30/11/22
# PURPOSE       : Checks the data is in expected format
#               
# ===================================================


# Library Imports
from colorama import Fore
import os


EXPECTED_HEADER = ['Motor PWM', ' Top Voltage (V)', ' Bottom Voltage (V)', ' Top Current (A)', ' Bottom Current (A)', ' Thrust (kg)']
EXPECTED_ROW_SIZE = 6

LF = list[float]


def header_check(data: list[LF], filename: str) -> None:
    """Checks to ensure headers are in the expected format"""
    header_row = data[1]
    
    try:
        assert(header_row == EXPECTED_HEADER)
        
    except:
        print(Fore.RED + f"\nERROR")
        print(f"Header from {filename} is not in the correct format")
        print(f"Expected: {EXPECTED_HEADER}\nGot: {header_row}\n" + Fore.RESET)
        os.abort()
        
          
def row_check(data: list[LF], filename: str) -> None:
    """Checks to see rows are correct size in case data has 'slipped' in serial transmission"""
    for index, row in enumerate(data[2:]): # Skips header rows
        
        try:
            assert(len(row) == EXPECTED_ROW_SIZE)
            
        except:
            print(Fore.RED + f"\nERROR")
            print(f"Row {index + 3} is not the correct size in file {filename}")
            print(f"Expected: {EXPECTED_ROW_SIZE}\nGot: {len(row)}\nPlease check this this file and row\n" + Fore.RESET)
            
            os.abort()
          
