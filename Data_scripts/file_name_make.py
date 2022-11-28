# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File name set up with naming Scheme
# ======================================================================


from colorama import Fore

TEST_TYPES = ["TEST", "CALIBRATE", "DATA"]
PROP_LIST = [15.2, 16.2, 18.2]              # ADD PROP SIZES YOU ARE USING
    
    
def file_name():
    """Defines filename with naming scheme"""
    test_type = str(test_type_ask())
    
    top_prop = str(prop_input("top"))
    bottom_prop = str(prop_input("bottom"))
    
    top_KV = str(input("\nWhat is the top motor KV: "))
    bottom_KV  = str(input("\nWhat is the bottom motor KV: "))
    
    pitch = str(input("\nWhat is the pitch: "))
    
    fileName = test_type + "-" + top_prop + "-" + bottom_prop + "-" + top_KV + "-" + bottom_KV + "-" + pitch + ".csv"
    
    return fileName

def test_type_ask():
    """Asks user for test type"""
    valid_input = False
    
    print(f"\nWhat is the type of test being performed\n")
    
    while valid_input == False:
        i = 0
        
        for test in TEST_TYPES:
            
            print(f"{i}: {test}")
            i += 1
        
        test_input = input(Fore.RESET + f"\nPress one with the corresponding number: ")
        
        # Tests user input
        try:
           test_type = TEST_TYPES[int(test_input)]
        except:
            print(Fore.RED + f"\nPlease enter a valid input.\nIt Should be of type int in the range of 0 to {i - 1}\n" + Fore.RESET)
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



def print_list(list):
    """Prints elements in list"""
    
    for item in list:
        print(Fore.RESET + f"{item}")
        

def list_check(user_input, list_used, data_type):
    """Returns the prop size in list"""
    try:
        if data_type(user_input) in list_used:
            return True
        else:
            print(Fore.RED + f"\nThat is not one of the options")
            print("Try again\n")
            return False
    except:
        print(Fore.RED + f"\nThat is not a {str(data_type)} data type")
        print("Try again\n")
        return False
   