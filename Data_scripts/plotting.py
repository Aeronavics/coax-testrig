# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Plots data
#               
# ===================================================


# Library Imports
import matplotlib.pyplot as plt

NEAT_OFFSET = 0.2


def efficiency_to_thrust_plot(total_thrust_list, total_efficiency_list, file_list, title):
    """"Plots the efficiency to thrust multiple file"""
    i = 0
    fig, ax = plt.subplots()
    lim_thrust = max(max(total_thrust_list))
    lim_E = max(max(total_efficiency_list))
    
    while i in range(0, len(file_list)):
        ax.set_xlim(0, lim_thrust + NEAT_OFFSET)
        ax.set_ylim(min(total_efficiency_list[i]) - NEAT_OFFSET, lim_E  + NEAT_OFFSET)
        ax.plot(total_thrust_list[i], total_efficiency_list[i], marker="o")
        
        i+=1
    
    ax.legend(file_list)
    ax.set_title(title)
    ax.set_xlabel("Thrust (kg)")
    ax.set_ylabel("Relative Efficiency (Thrust / Power)")
    ax.grid()
    
    plt.show()

    