# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File with common functions
# ======================================================================


# Library Imports
from colorama import Fore

def print_list(list: list) -> None:
    """Prints elements in list"""
    
    for item in list:
        print(Fore.RESET + f"{item}")
        

def list_check(user_input: str, list_used: list, data_type: type) -> bool:
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
    
    
def ask_user(question: str) -> bool:
    """Asks a user a question and returns bool dependant on answer"""
    print(question)
    user_input = str(input("Type yes or no: "))
    while True:
        try:
            if user_input.lower() == "yes":
                return True
            else:
                return False
            
        except:
                print("That was not a valid input.\n")
                print("Type yes or no: ")
        