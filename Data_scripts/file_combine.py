# ============================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 2/12/22
# PURPOSE       : Identifies files that are the testing based
#                 on the file name. This also means that files
#                 MUST be ordered. Eg files of teh same test
#                 should be next to each other when ordered
#                 alphabetically.
# ============================================================

# Library Imports
import os


def splited_files_list(file_list: list) -> list[list]:
    """ Returns a list of files that have been split by '-' char

    Args:
        file_list (list): List of all csv files found in directory specified

    Returns:
        list[list]: returns a 2d list where each sub list is the file name that
                    has been split by the '-' char
    """
    
    split_file_list = list()
    
    for file in file_list:
        split_file_list.append(file.split("-"))
    
    return split_file_list


def two_d_list_init(file_list: list) -> list[list]:
    """ Initializes an empty 2d list that is the same size as the file

    Args:
        file_list (list): List of all csv files found in directory specified

    Returns:
        list[list]: Empty 2d list that is the same size as the file
    """
    rows, cols = (len(file_list), 0)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    return arr


def same_files(file_list: list) -> list[list]:
    """ Goes through each file name to determine if they are of the same test 

    Args:
        file_list (list): List of all csv files found in directory specified

    Returns:
        list[list]: 2d list where all elements in each sub list are tests of the same type
    """
    split_file_list = splited_files_list(file_list)
    same_file_list = two_d_list_init(file_list)
    
    special_index = 0
    
    for index, sfile in enumerate(split_file_list):
        i = index
        
        if file_list[i] not in same_file_list[special_index]:
            same_file_list[special_index].append(file_list[i])
        
        try:   
            if split_file_list[i][1:7] != split_file_list[i + 1][1:7]:
                special_index += 1
                
        except IndexError:
            continue
        
        while i < len(file_list):
            
            if sfile[1:7] == split_file_list[i][1:7] and sfile != split_file_list[i] and file_list[i] not in same_file_list[special_index]:
                same_file_list[special_index].append(file_list[i])
                
            i += 1
    
    # removes empty lists elements 
    same_file_list = [index for index in same_file_list if index != []]
        
    return same_file_list

        
def get_file_list(FOLDER: str) -> list:
    """ Gets all scv files from the specified directory

    Args:
        FOLDER (str): Specified folder

    Returns:
        list: list of all csv files found
    """
    file_list = list()

    with os.scandir(".\\" + FOLDER + "\\") as entries:
        print("\nFiles found:")
        
        for entry in entries:
            if entry.name.endswith(".csv"):
                file_list.append(entry.name)
                print(entry.name)
            
    return file_list
