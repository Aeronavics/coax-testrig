# ======================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 25/11/22
# PURPOSE       : Reads data From Serial monitor and puts it into csv
# ======================================================================

import serial
import csv
from colorama import Fore
from time import time, ctime, sleep

from file_name_make import file_name


SAMPLES = 100
TIME_OUT = 1.2              # This needs to be > 1
SLEEP_TIME = 3
SHORT_SLEEP = 0.5

CSV = ".csv"

# Arduino related setup
arduino_port = 'COM3'       # serial port of Arduino
baud = 9600                 # arduino nano every runs at 9600 baud          

t = time()

invalid_list = ['Waiting for Authorization', 'Turing Power On!', 'Finished', '']


def serialread(fileName):
    """Reads serial data"""
    with serial.Serial(arduino_port, baud, timeout=TIME_OUT) as ser:
        print(Fore.GREEN + "\nConnected to port: " + arduino_port)
    
        line = 0 #start at 0 because our header is 0 (not real data)
        sensor_data = [] #store data
        
        ser.flush()
        send = str(input("Press 1 to attempt to connect to arduino and start test: "))
        ser.write(bytes(send, 'utf-8'))
        
        print("Sending...")
        
        while True:
            if ser.readline().decode('utf-8')[0:][:-2] == "Turing Power On!":   
                print("Sent")
                print("Connection Established")
                break
            else:
                sleep(SHORT_SLEEP)
                
        print("Start up sequence initiated")
        sleep(SHORT_SLEEP)
            
        # collect the samples
        while line <= SAMPLES:
            getData=ser.readline()
            dataString = getData.decode('utf-8')
            data=dataString[0:][:-2]
            
            # Filters samples
            if data.startswith("Time:"):
                data = data + ctime()

            readings = data.split(",")
            
            if readings[0] not in invalid_list:
                sensor_data.append(readings)
                
            print(Fore.RESET + f"{fileName} data:\n{sensor_data}")

            line = line + 1
            
    
    return sensor_data



        
        
def csv_make(fileName, sensor_data):
    """Creates csv file with data"""
    
    file = open(fileName, "a")
    
    print(Fore.GREEN + f"\nCreated file")
        
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)

    print(Fore.GREEN + f"Data collection complete for: {fileName}")
    
    file.close()
    
def serial_error():
    """Error loop that gives user chance to fix error with serial port"""
    print(Fore.RED + f"\nERROR")
    print(f"Access to serial port {arduino_port} has been denied.")
    print("This is likely due to another program using the serial monitor.")
    print("Ex: Arduino serial monitor is open.\n" + Fore.RESET)
    input("Press ENTER to try again: ")

    
def repeat():
    """Allows user to repeat test"""
    do_test = str(input("Press 1 to repeat test: "))
    
    if do_test == "1":
        return True
    else:
        return False


def control_func():
    """Function that controls other functions"""
    it_num = 0
    it_tag = "-#" +  str(it_num)
    fileName = file_name()
    do_test = True
    
    while do_test == True:
    
        it_tag = "-#" +  str(it_num)
        
        try:
            data = serialread(fileName)
            
        except serial.serialutil.SerialException:
            serial_error()
            
        else:    
            csv_make(fileName + it_tag + CSV, data)
            print(Fore.LIGHTGREEN_EX+ f"\nData collection complete!")
            print(f"Test was carried out at {ctime(t)}\n" + Fore.RESET)
            do_test = repeat()
            it_num += 1
            

control_func()