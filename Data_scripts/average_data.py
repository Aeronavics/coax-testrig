# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Averages the data based on the PWM
#                 sent to ESC
# ===================================================


#  Data Index's
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5


def summing_data(data):
    """ Sums data based on the PWM into ESC and returns list of summed data
        the number of times each PWM data set was summed"""
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
    """ LINKER FUNCTION
        Function that directs all others in this module"""
    combined_data, occurrence_list = summing_data(data)
    avg_data = avg_data_func(combined_data, occurrence_list)
    
    return avg_data
