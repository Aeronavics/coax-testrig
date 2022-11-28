# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 25/11/22
# PURPOSE       : Reads data From Serial monitor and puts it into csv
# ======================================================================

import serial
import csv
from colorama import Fore
from time import time, ctime, sleep


# CHANGE THESE FOR DIFFERENT FILE NAMES
TEST_TYPE = "PROTO"
TEST_NAME = "CALIBRATE"
RUN_NUM = 0

SAMPLES = 20
TIME_OUT = 1.1              # This needs to be > 1
SLEEP_TIME = 3

# Arduino related setup
arduino_port = 'COM3'       # serial port of Arduino
baud = 9600                # arduino nano every runs at 9600 baud          

t = time()

invalid_list = ['Waiting for Authorization', 'Turing Power On!', 'Finished', '']

def file_name(test_type, test_name, RUN_NUM):
    """Defines filename"""
    fileName = test_type + "-" + test_name + "-" + str(RUN_NUM)  + ".csv"
    return fileName

def serialread(fileName, samples, timeout1):
    """Reads serial data"""
    
    with serial.Serial(arduino_port, baud, timeout=timeout1) as ser:
        print(Fore.GREEN + "Connected to Arduino port: " + arduino_port)
    
        line = 0 #start at 0 because our header is 0 (not real data)
        sensor_data = [] #store data
        
        ser.flush()
        send = str(input("Press 1 to start test: "))
        ser.write(bytes(send, 'utf-8'))
        print("Sending...")
        sleep(SLEEP_TIME)
        print("Sent")
        
        # collect the samples
        while line <= samples:
            getData=ser.readline()
            dataString = getData.decode('utf-8')
            data=dataString[0:][:-2]
            
            if data == "Time:":
                data = data+ctime()

            readings = data.split(",")
            
            if readings[0] not in invalid_list:
                sensor_data.append(readings)
            print(Fore.WHITE + f"{fileName} data:\n{sensor_data}")

            line = line + 1
            
    
    return sensor_data
        
        
def csv_make(fileName, sensor_data):
    """Creates csv file with data"""
    file = open(fileName, "a")
    print(Fore.GREEN + f"Created file")
        
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)

    print(Fore.GREEN + f"Data collection complete for: {fileName}")
    file.close()


def control_func():
    """Function that controls other functions"""
  
    fileName = file_name(TEST_TYPE, TEST_NAME, str(RUN_NUM))
    data = serialread(fileName, SAMPLES, TIME_OUT)
    csv_make(fileName, data)
    
    print(Fore.LIGHTGREEN_EX+ f"\nData collection complete!")
    print(f"Test was carried out at {ctime(t)}\n" + Fore.RESET)

control_func()