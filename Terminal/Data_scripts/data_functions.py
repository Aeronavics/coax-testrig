# =========================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 19/1/23
# PURPOSE       : This module contains math functions for
#                 the data
#
# =========================================================

# Library imports
from colorama import Fore

# Index of where each value in a row of a csv file
PWM_INDEX = 0
TOP_V_INDEX, BOTTOM_V_INDEX = 1, 2
TOP_I_INDEX, BOTTOM_I_INDEX = 3, 4,
LOAD_INDEX = 5

# Constants
SCALE_FACTOR = 100
EFFICIENCY_CUTOFF = 0.08
LOAD_CUTOFF = 0.1
IDLE_I = 0.18

LF = list[float]

def calc_power(voltage: float, current: float) -> float:
    """ Calculates power via P = VI
    
        returns power as a float
    """
    
    return voltage * current


def give_current_offset(data: list[LF], index: int) -> float:
    """ Gives the current offset

    Args:
        data (list[LF]): 2d lost of data ready to be used_
        index (int): desired index for columns of data where current is

    Returns:
        float: current offset
    """
    
    current_offset_list = list()
    
    for row in data:
        if row[LOAD_INDEX] < LOAD_CUTOFF:
            current_offset_list.append(row[index])
    
    current_offset = (sum(current_offset_list) / len(current_offset_list)) / 2
    
    return current_offset
        
        

def give_power_list(data: list[LF]) -> list[LF]:
    """ Calculates the electrical power used

    Args:
        data (list[LF]): The combined processed data from the data dict

    Returns:
        list[LF]: 2d list of power values where each sublist is a specific test type
    """
    power_list = list()
    
    top_I_offset = give_current_offset(data, TOP_I_INDEX)
    bottom_I_offset = give_current_offset(data, BOTTOM_I_INDEX)
    
    for row in data[1:]:
        top_motor_power = calc_power(row[TOP_V_INDEX], (row[TOP_I_INDEX] - top_I_offset))
        bottom_motor_power = calc_power(row[BOTTOM_V_INDEX], (row[BOTTOM_I_INDEX] - bottom_I_offset))
        total_power = top_motor_power + bottom_motor_power
        
        if total_power <= 0.18:
            continue
        
        power_list.append(total_power)
        
    return power_list


def give_efficiency_list(data: list[LF]) -> LF:
    """ Calculates the relative efficiency.
    
        Note: If you are doing single prop testing you may want to only include
        motor you are using as part of your calculations. This means only including
        the motor you are using foe the total power variable.

    Args:
        data (list[LF]): 2d list of data ready to be used

    Returns:
        LF: Returns a list of valid efficiency's
    """
    
    efficiency_list = list()
    
    power_list = give_power_list(data)
    thrust_list = give_thrust_list(data)
     
    try:
        assert(len(power_list) == len(thrust_list))
    
    except AssertionError:
        print(Fore.RED + f"ERROR\nPower list and Thrust list are not the same length")
        
    for i in range(0, len(thrust_list)):
        efficiency = SCALE_FACTOR * (thrust_list[i] / power_list[i])
        efficiency_list.append(efficiency)
          
    return efficiency_list


def give_thrust_list(data: list[LF]) -> LF:
    """ Returns a list of thrusts

    Args:
        data (list[LF]): 2d list of data ready to be used

    Returns:
        LF: Returns a list of valid thrusts
    """
    
    thrust_list = list()
    
    for row in data:
        thrust = row[LOAD_INDEX]
        
        if thrust > LOAD_CUTOFF:
            thrust_list.append(thrust)
            
    return thrust_list


def give_PWM_list(data: list[LF]) -> LF:
    """ Returns a list of PWMs

    Args:
        data (list[LF]): 2d list of data ready to be used

    Returns:
        LF: Returns a list of valid PWMs
    """

    PWM_list = []
        
    for row in data:
        PWM_list.append(row[PWM_INDEX])
    
    return PWM_list
