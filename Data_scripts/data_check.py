# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 30/11/22
# PURPOSE       : Checks the data is in expected format
#               
# ===================================================


from colorama import Fore
import os


EXPECTED_HEADER = ['Motor PWM', ' Top Voltage (V)', ' Bottom Voltage (V)', ' Top Current (A)', ' Bottom Current (A)', ' Thrust (kg)']
EXPECTED_ROW_SIZE = 6


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
          


    
    