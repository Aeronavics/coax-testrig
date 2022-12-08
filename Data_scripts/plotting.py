# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Plots data
#               
# ===================================================


# Library Imports
import numpy as np
import matplotlib.pyplot as plt

NEAT_OFFSET = 0.3

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
    """exp model"""
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
    
    
def efficiency_to_thrust_plot(plotting_dict, title, LoBF):
    """"Plots the efficiency to thrust multiple file"""
    fig, ax = plt.subplots()
    lim_thrust = 0
    lim_E = 0
    
    for TvsE_data in plotting_dict.values():
        coefficients = least_squares_estimate(TvsE_data)
        
        # co = exp_estimate(TvsE_data)
        lim_thrust = max(max(TvsE_data[0]), lim_thrust)
        lim_E = max(max(TvsE_data[1]), lim_E)
        
        plt.scatter(TvsE_data[0],TvsE_data[1], marker='o')
        
        x = np.linspace(0, max(TvsE_data[0]) , 100)
        # ax.plot(x, exp_calc(co, x))
        if LoBF == True: ax.plot(x, function_sub(coefficients, x))
        
    ax.set_xlim(0, lim_thrust + NEAT_OFFSET)
    ax.set_ylim(0, lim_E  + NEAT_OFFSET)
        
    file_list = give_file_list(plotting_dict, LoBF)
    
    ax.legend(file_list)
    ax.set_title(title)
    ax.set_xlabel("Thrust (kg)")
    ax.set_ylabel("Relative Efficiency (Thrust / Power)")
    ax.grid()
    
    plt.show()
