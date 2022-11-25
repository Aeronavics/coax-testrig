# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 25/11/22
# PURPOSE       : Reads data From Serial monitor and puts it into csv
# ======================================================================

import serial
import csv
from colorama import Fore

# CHANGE THESE FOR DIFFERENT FILE NAMES
SAMPLES = 50
TIME_OUT = 0.1
TEST_TYPE = "PROTO"
TEST_NAME = "CALIBRATE"

# Arduino related setup
arduino_port = 'COM3'       # serial port of Arduino
baud = 9600                 # arduino nano every runs at 9600 baud          


def file_name(test_type, test_name, run_num):
    """Defines filename"""
    fileName = test_type + "-" + test_name + "-" + run_num + ".csv"
    return fileName

def serialread(fileName, samples, timeout1):
    """Reads serial data"""

    with serial.Serial(arduino_port, baud, timeout=timeout1) as ser:
        print(Fore.GREEN + "Connected to Arduino port: " + arduino_port)
        
        line = 0 #start at 0 because our header is 0 (not real data)
        sensor_data = [] #store data

        # collect the samples
        while line <= samples:
            getData=ser.readline()
            dataString = getData.decode('utf-8')
            data=dataString[0:][:-2]

            readings = data.split(",")
            
            sensor_data.append(readings)
            print(Fore.WHITE + f"{sensor_data}")

            line = line+1
    return sensor_data
        
        
def csv_make(fileName, sensor_data):
    """Creates csv file with data"""
    file = open(fileName, "a")
    print(Fore.GREEN + f"Created file")
        
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)

    print(Fore.GREEN + f"Data collection complete for!{fileName}")
    file.close()
    
def do_test():
    """takes user input to do test"""
    run_test = str(input(Fore.MAGENTA + f"\nPress ENTER to carry out test\nPress any other key to stop:\n"))
    return True if run_test == "" else False


def control_func():
    """Function that controls other functions"""
    run_test = True
    run_num = 0
    
    while run_num < 100 and run_test == True:
        fileName = file_name(TEST_TYPE, TEST_NAME, str(run_num))
        data = serialread(fileName, SAMPLES, TIME_OUT)
        csv_make(fileName, data)
        run_test = do_test()
        run_num += 1
    
    print(Fore.LIGHTGREEN_EX+ f"\nData collection complete!")
    print(f"A total of {run_num} tests were carried out\n" + Fore.RESET)

control_func()