# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 29/11/22
# PURPOSE       : File name set up
# ======================================================================


from colorama import Fore

TEST_TYPES = ["TEST", "CALIBRATE", "DATA"]

def file_name():
    """Defines filename"""
    
    top_prop = str(input(Fore.MAGENTA + f"What is the top prop size: "))
    bottom_prop = str(input("\nWhat is the bottom prop size: "))
    top_KV = str(input("\nWhat is the top motor KV: "))
    bottom_KV  = str(input("\nWhat is the bottom motor KV: "))
    pitch = str(input("\nWhat is the pitch: "))
    
    fileName = """TEST_TYPES[0]""" + "-" + top_prop + "-" + bottom_prop + "-" + top_KV + "-" + bottom_KV + "-" + pitch + ".csv"
    
    return fileName