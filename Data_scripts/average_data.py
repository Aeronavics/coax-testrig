# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Averages the
#               
# ===================================================

from colorama import Fore

from csv_to_list import control_func
from data_check import header_check, row_check

#  Index's
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

FILE_NAME = "TEST-0-0-0-0-1-#0.csv"     # TEMP: will be automated from outside func     

def combing_data(data):
    """Averages data"""
    combined_data = list()
    last_PWM = 0
    pwm_num = -1
    num_occurrences = 0
    occurrence_list = list()
    
    
    for row in data[2:]:
        temp_data = [0,0,0,0,0,0]
        if row[PWM_INDEX] == last_PWM:
            combined_data[pwm_num][TOP_V_INDEX] += row[TOP_V_INDEX]
            combined_data[pwm_num][BOTTOM_V_INDEX] += row[BOTTOM_V_INDEX]
            combined_data[pwm_num][TOP_I_INDEX] += row[TOP_I_INDEX]
            combined_data[pwm_num][BOTTOM_I_INDEX] += row[BOTTOM_I_INDEX]
            combined_data[pwm_num][LOAD_INDEX] += row[LOAD_INDEX]
            
            num_occurrences += 1
            
        elif row[PWM_INDEX] != last_PWM:
            if pwm_num >= 0:
                occurrence_list.append(num_occurrences)
            
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

def divide_by_occurrence(row_data, occurrence_num):
    """Divides all elements except PWM by the num of occurrences"""
    for i in range(1, len(row_data)):
        row_data[i] /= occurrence_num
    return row_data
        
    
def avg_data_func(combined_data, occurrence_list):
    """Divides the avg data by num of occurrence's to get the actual average of the data"""
    avg_data = list()
    i = 0
    while i in range(0, len(combined_data)):
        avg_row = divide_by_occurrence(combined_data[i], occurrence_list[i])
        avg_data.append(avg_row)
        i += 1
        
    return avg_data
        
    

def give_average_data(data):
    """Function that directs all others in this module"""
    
    # Format checks
    header_check(data)
    row_check(data)
    combined_data, occurrence_list = combing_data(data)
    avg_data = avg_data_func(combined_data, occurrence_list)
    
    return avg_data


