# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 1/12/22
# PURPOSE       : Plots data
#               
# ===================================================

import matplotlib.pyplot as plt


def efficiency_to_thrust_single(thrust_list, efficiency_list):
    """"Plots the efficiency to thrust"""
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(thrust_list) + 0.5)
    ax.set_ylim(min(efficiency_list) - 0.2, 1)
    ax.plot(thrust_list, efficiency_list, marker="o")
    
    ax.set_title("Test")
    ax.set_xlabel("Thrust (kg)")
    ax.set_ylabel("Efficiency")
    ax.grid()
    
    plt.show()
    