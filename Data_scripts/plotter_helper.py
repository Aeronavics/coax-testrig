# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 9/12/22
# PURPOSE       : File with plotting helper functions
# ======================================================================

# Library Imports
import numpy as np


def ask_title():
    """ Asks user for a title to their graph"""
    title = str(input("\nWhat should the title for this graph be: "))
    return title

   
def give_file_list(plotting_dict, LoBF):
    """Gives file list based onb dict passed to plotting function"""
    file_list = list()
    
    for file in plotting_dict.keys():
        file = file.split("#")
        file[0] = file[0].rstrip(file[0][-1])
        
        file_list.append(file[0])
        
        if LoBF == True: file_list.append("fitted " + file[0])
    
    return file_list


def least_squares_estimate(data):
    """ Returns the coefficients for the polynomial that fits the function""" 
    x = data[0]
    y = data[1]
    
    coefficients = np.polyfit(x, y, 3)
    
    return np.flip(coefficients)


def function_sub(coefficients, x):
    """subs coefficients into equation"""
    size = len(coefficients)
    y = 0
    for i in range(0, size):
        y += coefficients[i] * (x ** i)
    
    return y


def exp_estimate(data):
    """exp model least squares estimate (redundant)"""
    x = data[0]
    y = data[1]
    x = np.asarray(x).T
    y = np.asarray(np.log(y)).T
    
    A = np.column_stack((np.ones_like(x), x))
    Q, R = np.linalg.qr(A)
    ln_a_b = np.linalg.solve(R, Q.T @ y)
    lna, lnb = ln_a_b[0], ln_a_b[1]
    
    co = [lna, lnb] 
    
    return co

    
def exp_calc(co, x):
    a = co[0]
    b = co[1]
    y = np.exp(a + b * x)
    return y      