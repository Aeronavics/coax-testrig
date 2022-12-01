# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File name set up with naming Scheme
# ======================================================================


from colorama import Fore

from common_funcs import list_check, print_list

# Lists of parameters
TEST_TYPES = ["TEST", "CALIBRATE", "DATA"]
PROP_LIST = [0, 15, 15.2, 16.2, 17, 18.2]              # ADD PROP SIZES YOU ARE USING
KV_LIST = [0, 140, 160, 220, 240]              # ADD MOTOR KVs YOU ARE USING
    
    
def file_name():
    """Defines filename with naming scheme"""
    test_type = str(test_type_ask())
    
    top_prop = str(prop_input("top"))
    top_KV = str(KV_input("top"))
    top_pitch = str(input("\nWhat is the pitch of top: "))
    
    bottom_prop = str(prop_input("bottom"))
    bottom_KV  = str(KV_input("bottom"))
    bottom_pitch = str(input("\nWhat is the pitch of bottom: "))
    
    fileName = test_type + "-" + top_prop + "-" +  top_KV + "-" + top_pitch + "-" + bottom_prop + "-" + bottom_KV + "-" + bottom_pitch
    
    return fileName


def test_type_ask():
    """Asks user for test type"""
    valid_input = False
    
    print(f"\nWhat is the type of test being performed\n")
    
    while valid_input == False:
        index = 0
        
        for test in TEST_TYPES:
            
            print(f"{index}: {test}")
            index += 1
        
        test_input = input(Fore.RESET + f"\nPress one with the corresponding number: ")
        
        # Tests user input
        try:
           test_type = TEST_TYPES[int(test_input)]
        except:
            print(Fore.RED + f"\nPlease enter a valid input.\nIt Should be of type int in the range of 0 to {index - 1}\n" + Fore.RESET)
        else:
            valid_input = True
            
    return test_type


def prop_input(position):
    """Gets prop input form user"""
    
    print(f"\nEnter {position} propeller size (inch) from the following list\n")
    print_list(PROP_LIST)
    
    prop_input = input("\nEnter Propeller size: ")
    
    valid = list_check(prop_input, PROP_LIST, float)
    while valid == False:
        print_list(PROP_LIST)    
        prop_input = input(Fore.RESET + f"\nEnter {position} Propeller size: ")
        valid = list_check(prop_input, PROP_LIST, float)
        
    return prop_input


def KV_input(position):
    """Gets motor KV input form user"""
    
    print(f"\nEnter {position} motor KV from the following list\n")
    print_list(KV_LIST)
    
    motor_input = input(f"\nEnter {position} motor KV: ")
    
    valid = list_check(motor_input, KV_LIST, int)
    while valid == False:
        print_list(KV_LIST)    
        motor_input = input(Fore.RESET + f"\nEnter {position} motor KV: ")
        valid = list_check(motor_input, KV_LIST, int)
        
    return motor_input



   