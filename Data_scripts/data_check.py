# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 30/11/22
# PURPOSE       : Data analysis of data
#               
# ===================================================


from colorama import Fore
import os

from csv_to_list import control_func


EXPECTED_HEADER = ['Motor PWM', ' Top Voltage (V)', ' Bottom Voltage (V)', ' Top Current (A)', ' Bottom Current (A)', ' Thrust (kg)']
EXPECTED_ROW_SIZE = 6

FILE_NAME = "TEST-0-0-0-0-1-#0.csv"     # TEMP: will be automated from outside func

DATA = control_func(FILE_NAME)          # TEMP


def header_check(data):
    """Checks to ensure headers are in the expected format"""
    # header_row = 
    header_row = data[0]
    
    try:
        assert(header_row == EXPECTED_HEADER)
    except:
        print(Fore.RED + f"\nERROR")
        print("Header is not in the correct format")
        print(f"Expected: {EXPECTED_HEADER}\nGot: {header_row}\n" + Fore.RESET)
        os.abort()
        
          
def row_check(data):
    """Checks to see rows are correct size in case data has 'slipped' in serial transmission"""
    for row in data[1:]:
        try:
            assert(len(row) == EXPECTED_ROW_SIZE)
        except:
            print(Fore.RED + f"\nERROR")
            print("Rows are not the correct size")
            print(f"Expected: {EXPECTED_ROW_SIZE}\nGot: {len(row)}\n" + Fore.RESET)
            os.abort()
          

def leader_func():
    """Function that directs others in this module"""
    data = DATA
    header_check(data)
    row_check(data)
    
    
leader_func()
    