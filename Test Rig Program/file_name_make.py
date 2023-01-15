# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File name set up with naming scheme
# ======================================================================

# Library Imports
from colorama import Fore
from typing import Union

# Module Imports
from common_funcs import list_check, print_list

# Lists of set parameters
PROP_LIST = [0, 14, 15, 15.2, 16.2, 17, 18, 18.2, 18.3]     # ADD PROP SIZES YOU ARE USING
KV_LIST = [0, 140, 160, 220, 240]                           # ADD MOTOR KVs YOU ARE USING
    
    
def file_name() -> str:
    """ Module director. Asks user for all the parameters of test to be used as the file name.
        Only accepts pre selected parameter's

    Returns:
        str: Filename
    """
    test_type = str(input("Whats some useful info about test.\nEg brand of prop?\nEnsure it is similar for same test.\nInput here: "))
    
    top_prop = str(prop_input("top"))
    top_KV = str(KV_input("top"))
    top_pitch = str(input("\nWhat is the pitch of top: "))
    
    bottom_prop = str(prop_input("bottom"))
    bottom_KV  = str(KV_input("bottom"))
    bottom_pitch = str(input("\nWhat is the pitch of bottom: "))
    
    test_num = str(input("\nWhat is the test num: "))
    
    fileName = test_type + "-" + top_prop + "-" +  top_KV + "-" + top_pitch + "-" + bottom_prop + "-" + bottom_KV + "-" + bottom_pitch + "-#" + test_num
    
    return fileName


def prop_input(position: str) -> str:
    """ Gets the prop size from user

    Args:
        position (str): The position of the prop

    Returns:
        str: Prop size
    """
    
    print(f"\nEnter {position} propeller size (inch) from the following list\n")
    print_list(PROP_LIST)
    
    prop_input = input("\nEnter Propeller size: ")
    
    valid = list_check(prop_input, PROP_LIST, float)
    
    # Checks to see if user input is one in predefined list
    while valid == False:
        print_list(PROP_LIST)    
        prop_input = input(Fore.RESET + f"\nEnter {position} Propeller size: ")
        valid = list_check(prop_input, PROP_LIST, float)
        
    return prop_input


def KV_input(position: str) -> str:
    """ Gets the motor kV from the user

    Args:
        position (str): The position of the motor in question

    Returns:
        str: Motor kV
    """
    
    print(f"\nEnter {position} motor KV from the following list\n")
    print_list(KV_LIST)
    
    motor_input = input(f"\nEnter {position} motor KV: ")
    
    # Checks to see if user input is one in predefined list
    valid = list_check(motor_input, KV_LIST, int)
    while valid == False:
        print_list(KV_LIST)    
        motor_input = input(Fore.RESET + f"\nEnter {position} motor KV: ")
        valid = list_check(motor_input, KV_LIST, int)
        
    return motor_input



   