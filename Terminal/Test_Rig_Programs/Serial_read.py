# =====================================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 25/11/22
# PURPOSE       : Reads data From Serial monitor and puts it 
#                 into csv format
# =====================================================================


# Library Imports
import serial
import os
import csv
from colorama import Fore
from time import time, ctime, sleep

# Module Imports
from file_name_make import file_name

LF = list[float]


SAMPLES = 55                # Make sure this is big enough
TIME_OUT = 2                # This needs to be > 1 for good readings otherwise may skip rows
SLEEP_TIME = 3
SHORT_SLEEP = 0.55
MAX_SERIAL_SEND_ATTEMPTS = 50

CSV = ".csv"

# Arduino related setup
arduino_port = 'COM3'       # Serial port of Arduino. CHANGE TO WHAT YOURS IS
baud = 9600                 # Arduino nano every runs at 9600 baud (can change but doesn't significantly effect speed)         

t = time()

DONT_APPEND = ['Waiting for Authorization', 'Turing Power On!', 'Finished', '', 'Waiting...']



def serialread(fileName: str) -> list[LF]:
    """ This function sends a 1 to the serial port specified by 'arduino_port'.
        The Arduino should send a message back that when read by this function will
        begin reading the serial output from the Arduino

    Args:
        fileName (str): Name for the file to be created

    Returns:
        list: 2d list of data read
    """
        
    with serial.Serial(arduino_port, baud, timeout=TIME_OUT) as ser:
        print(Fore.GREEN + "\nConnected to port: " + arduino_port)
    
        line = 0                # start at 0 because our header is 0 (not real data)
        sensor_data = []        # store raw data
        
        ser.flush()             # clear serial 
        send = str(input("Press 1 to attempt to connect to arduino and start test: "))
        
        if send != '1':
            print(Fore.RED + f"\n1 was not pressed\nExiting program" + Fore.RESET)
            os.abort()
            
        ser.write(bytes(send, 'utf-8'))
        
        print("Sending...")
        
        # This loop will attempt to connect to arduino until it responds
        counter = 0
        
        while counter < MAX_SERIAL_SEND_ATTEMPTS:
            ser.write(bytes(send, 'utf-8'))
            
            if ser.readline().decode('utf-8')[0:][:-2] == "Turing Power On!":   # Ignores the last 2 bits as they are stop bits
                print("Sent")
                print("Connection Established")
                break
            
            else:
                sleep(SHORT_SLEEP)
                counter += 1
                
        print("Start up sequence initiated")
        sleep(SHORT_SLEEP)      # sleep to allow Arduino to get ready to send data
            
        # collect the samples
        while line <= SAMPLES:
            if send == '2': break
            getData=ser.readline()
            dataString = getData.decode('utf-8')
            data=dataString[0:][:-2]
            
            # Filters samples
            
            if data.startswith("Time:"): data = data + ctime()
            
            if warning_message(data) == True:
                break

            readings = data.split(",")
            
            if readings[0] not in DONT_APPEND: sensor_data.append(readings) # doesn't include messages from Arduino
            
            print(Fore.RESET + f"{fileName} data:\n{sensor_data}")  # prints data as its collected

            line = line + 1
    
    return sensor_data


def warning_message(data) -> bool:
    """ Prints message if either temperature or current go over max limit
        Also triggered if interrupt is triggered which is good for debugging

    Args:
        data (_type_): Current row of data

    Returns:
        bool: Returns True if this warning message is in the row and prints it has occurred
    """
        
    if data.startswith("MAX CURRENT"):
        print(Fore.RED + f"\nCurrent has exceeded the max limit!!!")
        print(f"Shutting down" + Fore. RESET)
        return True
        
    elif data.startswith("MAX TEMP"):
        print(Fore.RED + f"\nTemperature has exceeded the max limit!!!")
        print(f"Shutting down" + Fore. RESET)
        return True
    
    elif data.startswith("INTERRUPT"):
        print(Fore.RED + f"\Interrupt has been triggered!!!")
        print(f"Shutting down" + Fore. RESET)
        return True
    
    else:
        return False
    
    
def csv_make(fileName: str, sensor_data: list) -> None:
    """ Creates the csv file from the list provided. Each sub list is a row

    Args:
        fileName (str): Filename
        sensor_data (list): 2d list with the data
    """
    
    file = open(fileName, "a")
    
    print(Fore.GREEN + f"\nCreated file")
        
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)

    print(Fore.GREEN + f"Data collection complete for: {fileName}")
    
    file.close()
    
    
def serial_error() -> None:
    """ Prints error message if failing to connect with Arduino"""

    print(Fore.RED + f"\nERROR")
    print(f"Access to serial port {arduino_port} has been denied.")
    print("This is likely due to another program using the serial monitor.")
    print("Ex: Arduino serial monitor is open.\n" + Fore.RESET)
    input("Press ENTER to try again: ")     


def control_func() -> None:
    """ LINKER FUNCTION. In a try loop until data is successfully collected"""
    fileName = file_name()

    attempt = 0
    
    while attempt < 10:
        try:
            data = serialread(fileName)
            
        except serial.serialutil.SerialException:
            serial_error()
            attempt += 1
            
        else:    
            csv_make(fileName + CSV, data)
            print(Fore.LIGHTGREEN_EX+ f"\nData collection complete!")
            print(f"Test was carried out at {ctime(t)}\n" + Fore.RESET)
            break
            
control_func()
