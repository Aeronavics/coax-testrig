# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 2/12/22
# PURPOSE       : Combines csv files of same test
#                 
# ===================================================


# Library Imports
import os

def same_file_test(file_list, previous_file):
    """"""
    file_list = file_list.split("-")
    previous_file = previous_file.split("-")
    
    if file_list[1:7] == previous_file[1:7]:
        return True
    else:
        return False
    
    
def get_file_list():
    """Gets all the files from the directory"""
    file_list = list()

    with os.scandir(".\put_data_here\\") as entries:
        print("\nFiles found:\n")
        
        for entry in entries:
            if entry.name.endswith(".csv"):
                file_list.append(entry.name)
                print(entry.name)
            
    return file_list
