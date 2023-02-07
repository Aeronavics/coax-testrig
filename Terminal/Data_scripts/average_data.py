# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Averages the data based on the PWM
#                 sent to the ESC
# ===================================================

# Library Imports
from colorama import Fore

# Index of where each value in a row of a csv file
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

LF = list[float]


def summing_data(data: list[LF]) -> list[LF]:
    """ Sums data based on the PWM into ESC

    Args:
        data (list[LF]): 2d list of all processed data

    Returns:
        list[LF]: 2d list of data but all elements with the same PWM have been summed
    """
    # Variable declaration
    data.sort()
    combined_data = list()
    last_PWM = 0
    pwm_num = -1
    num_occurrences = 0
    occurrence_list = list()
    
    for row in data:
        temp_data = [0,0,0,0,0,0]
        # If data with this PWM has been averaged in previously
        if row[PWM_INDEX] == last_PWM:
            combined_data[pwm_num][TOP_V_INDEX] += row[TOP_V_INDEX]
            combined_data[pwm_num][BOTTOM_V_INDEX] += row[BOTTOM_V_INDEX]
            combined_data[pwm_num][TOP_I_INDEX] += row[TOP_I_INDEX]
            combined_data[pwm_num][BOTTOM_I_INDEX] += row[BOTTOM_I_INDEX]
            combined_data[pwm_num][LOAD_INDEX] += row[LOAD_INDEX]
            
            num_occurrences += 1
        
        # If data of this PWM has not been averaged previously
        elif row[PWM_INDEX] != last_PWM:
            if pwm_num >= 0:
                occurrence_list.append(num_occurrences) # Adds the occurrence of previous PWM signal
            
            pwm_num += 1
            
            last_PWM = row[PWM_INDEX]
            temp_data[PWM_INDEX] = last_PWM
            temp_data[TOP_V_INDEX] = row[TOP_V_INDEX]
            temp_data[BOTTOM_V_INDEX] = row[BOTTOM_V_INDEX]
            temp_data[TOP_I_INDEX] = row[TOP_I_INDEX]
            temp_data[BOTTOM_I_INDEX] = row[BOTTOM_I_INDEX]
            temp_data[LOAD_INDEX] = row[LOAD_INDEX]
            
            num_occurrences = 1
                
            combined_data.append(temp_data)
            
    occurrence_list.append(num_occurrences)
                
    return combined_data, occurrence_list


def divide_by_occurrence(row_data: list[LF], occurrence_num: list[int]) -> LF:
    """ Divides all elements except PWM by the num of occurrences

    Args:
        row_data (list[LF]): _description_
        occurrence_num (list[int]): _description_

    Returns:
        LF: row data that has been averaged
    """
    
    for i in range(1, len(row_data)):
        row_data[i] /= occurrence_num
        
    return row_data
        
    
def avg_data_func(combined_data: list[LF], occurrence_list: list[int]) -> list[LF]:
    """ The function that averages the data and returns the 2d list

    Args:
        combined_data (list[LF]): Summed data based on PWM
        occurrence_list (list[int]): Number of times each PWM was in data set

    Returns:
        list[LF]: The averaged data
    """
    
    avg_data = list()
    i = 0
    
    while i in range(0, len(combined_data)):
        avg_row = divide_by_occurrence(combined_data[i], occurrence_list[i])
        avg_data.append(avg_row)
        i += 1
    
    return avg_data
        

def give_average_data(data: list[LF]) -> list[LF]:
    """ Error handling and will send the averaged data to other modules

    Args:
        data (list[LF]): Un averaged data
    Returns:
        list[LF]: The averaged data
    """
        
    try:
        combined_data, occurrence_list = summing_data(data)
        avg_data = avg_data_func(combined_data, occurrence_list)
    
    except:
        print(Fore.RED + f"ERROR\nSomething went wrong inside of average_data.py")
        print(f"This doesn't usually happen")
        
    else: 
        return avg_data
    
    input(f"Press ENTER to view error message: " + Fore.RESET)
    combined_data, occurrence_list = summing_data(data)
    avg_data = avg_data_func(combined_data, occurrence_list)
