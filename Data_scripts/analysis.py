# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Data Analysis
#               
# ===================================================


from common_funcs import ask_user
from average_data import give_average_data
from csv_to_list import control_func
from data_check import header_check, row_check
from plotting import efficiency_to_thrust_single

PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

FILE_NAME = "TEST-0-0-0-0-1-#0.csv"

def efficiency_and_thrust_find(data):
    """Finds efficiency to thrust provides"""
    thrust_list = list()
    efficiency_list = list()
    for row in data:
        thrust = row[LOAD_INDEX]
        
        top_motor_power = row[TOP_V_INDEX] * row[TOP_I_INDEX] 
        bottom_motor_power = row[BOTTOM_V_INDEX] * row[BOTTOM_I_INDEX] 
        total_power = top_motor_power + bottom_motor_power
        
        efficiency = 100 * thrust / total_power
        
        if efficiency < 0.1:
            continue
        
        
        thrust_list.append(thrust)
        efficiency_list.append(efficiency)
        
    return efficiency_list, thrust_list
        

def get_data(filename):
    """Gets data and gets it error checked"""
    data =  control_func(filename)          
    # Format checks
    header_check(data)
    row_check(data)
    
    good_data = give_average_data(data)
    return good_data


def analysis_main(filename):
    """main func that will direct all others in analysis"""
    data = get_data(filename)
    
    plot_E = ask_user("Do you want to plot efficiency against thrust?")
    
    if plot_E == True:
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        efficiency_to_thrust_single(thrust_list, efficiency_list)
    
    
analysis_main(FILE_NAME)