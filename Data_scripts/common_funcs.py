# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File with common functions
# ======================================================================

from colorama import Fore

def print_list(list):
    """Prints elements in list"""
    
    for item in list:
        print(Fore.RESET + f"{item}")
        

def list_check(user_input, list_used, data_type):
    """Returns bool if element is in list"""
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
    
def ask_user(question):
    """Asks a user a question and returns bool"""
    print(question)
    user_input = str(input("Type yes or no: "))
    
    if user_input.lower() == "yes":
        return True
    else:
        return False