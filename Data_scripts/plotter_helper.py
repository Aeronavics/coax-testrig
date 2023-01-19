# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 9/12/22
# PURPOSE       : File with plotting helper functions
# ======================================================================

# Library Imports
import numpy as np

LF = list[float]


class Do_plot:
    """ Class that allows to plot different things"""
    
    def __init__(self, file_dict: dict[str, list[LF]]) -> None:
        self.file_dict = file_dict

class Graph_Labels:
    """ Class that has all the labels and graph values for graphing to make it look pretty"""
    
    def __init__(self, xlabel: str, ylabel: str, xstart: int, offset_multiply: float, LoBF: bool, Mxticks: float, mxticks: float, Myticks: float, myticks: float):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xstart = xstart
        self.offset_multiply = offset_multiply
        self.LoBF = LoBF
        self.Mxticks = Mxticks
        self.mxticks = mxticks
        self.Myticks = Myticks
        self.myticks = myticks
        
        
    def max_xtick(self, lim_x: int, NEAT_OFFSET: float) -> float:
        """ Returns the maximum x value that should be displayed of the graph"""
        return lim_x + NEAT_OFFSET * self.offset_multiply
    
    def max_ytick(self, lim_y: int, NEAT_OFFSET: float) -> float:
        """ Returns the maximum y value that should be displayed of the graph"""
        return lim_y + NEAT_OFFSET
           

def ask_title() -> None:
    """ Asks user for a title to their graph"""
    title = str(input("\nWhat should the title for this graph be: "))
    return title

   
def give_file_list(plotting_dict: dict[str, list[LF]], LoBF: bool) -> list[str]:
    """_summary_

    Args:
        plotting_dict (dict[str, list[LF]]): _description_
        LoBF (bool): _description_

    Returns:
        list[str]: List of files 
    """
    file_list = list()
    
    for file in plotting_dict.keys():
        file = file.split("#")
        file[0] = file[0].rstrip(file[0][-1])
        
        file_list.append(file[0])
        
        if LoBF == True: file_list.append("fitted " + file[0])
    
    return file_list


def least_squares_estimate(data: list) -> np.ndarray:
    """ Returns the coefficients for the polynomial that fits the function""" 
    x = data[0]
    y = data[1]
    
    coefficients = np.polyfit(x, y, 4)
    
    return np.flip(coefficients)


def function_sub(coefficients: np.ndarray, x: float) -> float:
    """subs coefficients into equation"""
    size = len(coefficients)
    y = 0
    for i in range(0, size):
        y += coefficients[i] * (x ** i)
    
    return y


def exp_estimate(data: LF) -> np.ndarray:
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