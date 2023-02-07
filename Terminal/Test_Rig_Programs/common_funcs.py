# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : Module with common functions
# ======================================================================


# Library Imports
from colorama import Fore

def print_list(list: list) -> None:
    """ Prints all items in list

    Args:
        list (list): A list
    """
    
    for item in list:
        print(Fore.RESET + f"{item}")
        

def list_check(user_input: str, list_used: list, data_type: type) -> bool:
    """ Checks if user input is an item inside a given list

    Args:
        user_input (str): The users input
        list_used (list): The List used as reference
        data_type (type): The data type

    Returns:
        bool: T or F if in list
    """
    
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
    """ Asks the user a bool question (yes or no) adn will return the corresponding bool

    Args:
        question (str): The question to be asked

    Returns:
        bool: Result from question
    """
    
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
        