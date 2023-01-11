# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 2/12/22
# PURPOSE       : Combines csv files of same test     
# ===================================================


# Library Imports
import os


def splited_files_list(file_list: list) -> list[list]:
    """ Returns a list of files that have been split by '-' char"""
    
    split_file_list = list()
    
    for file in file_list:
        split_file_list.append(file.split("-"))
    
    return split_file_list


def two_d_list_init(file_list: list) -> list[list]:
    """ Inits a 2d list of the size of the the len(files)"""
    rows, cols = (len(file_list), 0)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    return arr


def same_files(file_list: list) -> list[list]:
    """ Returns a 2d list that contains lists of files that are of the same test
        FILE MUST BE ORDERED"""
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
    same_file_list = [x for x in same_file_list if x != []]
        
    # print(f"This is the sorted file list:\n{same_file_list}")
    return same_file_list

        
def get_file_list(FOLDER: str) -> list:
    """Gets all the files from the directory"""
    file_list = list()

    with os.scandir(".\\" + FOLDER + "\\") as entries:
        print("\nFiles found:")
        
        for entry in entries:
            if entry.name.endswith(".csv"):
                file_list.append(entry.name)
                print(entry.name)
            
    return file_list
