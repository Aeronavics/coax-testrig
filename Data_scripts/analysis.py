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
from plotting import efficiency_to_thrust_plot

PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

FILE_NAME_LIST = ["Falcon-15-160-5.5-0-0-0-#1.csv","Xoar-15-160-5-0-0-0-#0.csv", "TMOTOR-18.2-0-160-0-6.1-#0.csv", "Xoar-14-160-5-0-0-0-#0.csv"]

def efficiency_and_thrust_find(data):
    """Finds efficiency to thrust provides"""
    thrust_list = list()
    efficiency_list = list()
    for row in data:
        thrust = row[LOAD_INDEX]
        
        top_motor_power = row[TOP_V_INDEX] * row[TOP_I_INDEX] 
        bottom_motor_power = row[BOTTOM_V_INDEX] * row[BOTTOM_I_INDEX] 
        total_power = top_motor_power #+ bottom_motor_power * 0
        
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

def do_plot_TvsE(file_list):
    """Sets up data to be plotted"""
    total_thrust_list = list()
    total_efficiency_list = list()
    
    title = str(input("\nWhat should the title for this graph be: "))
    
    for filename in file_list:
        data = get_data(filename)
        efficiency_list, thrust_list = efficiency_and_thrust_find(data)
        total_thrust_list.append(thrust_list)
        total_efficiency_list.append(efficiency_list)
        
    efficiency_to_thrust_plot(total_thrust_list, total_efficiency_list, file_list, title)
    


def analysis_main(file_list):
    """main func that will direct all others in analysis"""
    plot_E = ask_user("\nDo you want to plot efficiency against thrust?")
    if plot_E == True:
        do_plot_TvsE(file_list)
    
    
analysis_main(FILE_NAME_LIST)