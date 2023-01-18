![Aeronavics Logo](https://search.therobotreport.com/wp-content/uploads/2020/07/Aeronavics-Droidworx-NZ-334637.png)

# About
Contains all the code used for the investigation of optimizing thrust and efficiency of coaxial propeller systems. This was conducted and created by the 2022 - 2023 interns.

This branch contains the code to conduct each test through the terminal.

## Pre-requisites
[Python3](https://www.python.org/) and [Arduino IDE](https://www.arduino.cc/en/software) as linked. The following modules are also required with their install commands seen below:

<!-- Modules to install -->
```bash
pip install numpy
```

```bash
pip install matplotlib
```

```bash
pip install colorama
```

```bash
pip install pyserial
```

# Sections:
- Data Collection
  - Setup and Use 
  - Trouble Shooting
- Data Analysis 
  - Setup and Use

## Data Collection
All code for the data collection is found in the 'Test Rig Program' folder. Ensure you name the files of the same test the same as each other (with differing test numbers). Example:
```
Pitch2-18-160-6-15-220-5-#1.csv
Pitch2-18-160-6-15-220-5-#2.csv
```

### Setup and Use:
1. Clone this repository. [SSH help](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    ```bash
   git clone git@github.com:Aeronavics/coax-testrig.git
   ```
2. Open the Arduino IDE and connect the Arduino Nano Every
3. Upload 'Test Rig Program.ino' to Arduino using IDE (ensure power sources are off). Make sure the assisting modules such as HX711.h are in the same directory. **Arduino does NOT do this automatically**
4. In 'file_name_make.py' alter the PROP_LIST and KV_LIST so they contain the motors and props you are using. Example:
    ```python
    PROP_LIST = [0, 14, 15, 15.2, 16.2, 17, 18, 18.2, 18.3]    
    KV_LIST = [0, 140, 160, 220, 240]  
    ```
5. In 'Serial_read.py' change the following the "arduino_port" to the port where your Arduino is connected. Example:
    ```python
    arduino_port = 'COM3' # Serial port of Arduino.
    ```
6. Turn power on THEN plug battery in
7. Run the following (or equivalent):
    ```bash
    python3 Serial_read.py
    ```
8. Following the instructions on displayed by the terminal
9.  After test has finished turn off and unplug all power (except USB) and cool motors down
10. For each new test repeat steps 6 - 9

### Trouble Shooting
**Failure to connect to Serial port**\
Message:
> ERROR\
> Access to serial port {chosen port} has been denied.
> This is likely due to another program using the serial monitor\
> Press ENTER to try again:
- Make sure Arduino IDE does not have its Serial port view option open
- Ensure connection to Arduino via USB is solid
- Check the Arudnino is OK. The Arduino NANO EVERY's have a poor schotky diode (K26, top left) that fails easily. If this or one of the Atmel chip is **very hot** it is because it has failed and the board is probably toast. Check there are no shorts to GND
    ![Ardino Nano Every](https://blog.arduino.cc/wp-content/uploads/2019/05/ABX00028_front.jpg)
  
**Connected to Serial port but message never sends**

Message: 
> Press 1 to attempt to connect to arduino and start test:\
> Sending...

and this never changes

- Before every test open and close the Serial monitor in the Arduino IDE
- Turn off all power sources and USB and then re-upload code.

**Interrupt fires unannounced**

- Check that the switch connections
- Check there is enough but no too much capacitance between the switch and GND.
- Is the Arduino resetting itself for any reason?

## Data Analysis

All the code for the data analysis is found in the 'Data_scripts' folder.

### Setup and Use
This assumes you have used the data collection method **without the GUI**. This is the one outlined above.
1. Clone the repository. [SSH help](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
   ```bash
   git clone git@github.com:Aeronavics/coax-testrig.git
   ```
2. Go to 'Data_scripts' directory
3. Add the data you wish to analyze somewhere in the directory of the repository or elsewhere.
4. Open 'analysis.py and change the PATH_FOLDER to where the data is. This should be relative to the 'Data_scripts' folder. Example:
    ```python
    PATH FOLDER = 'Data\\Motor Config\\160-160vs160-220\\'   # Change to what path your folder is in (MACS use '/')
    ```
    - If using MAC or Linux you will need to change the '\\\\' to '/ ' for the PATH_SLASHES variable
5. In analysis_main() inside analysis.py comment out the graphs you don't want to plot. Example
    ```python
    do_plot_PWMvsE(combined_data_dict)  # Plots PWM against efficiency
    do_plot_PWMvsT(combined_data_dict)  # Plots PWM against Thrust
    do_plot_TvsE(combined_data_dict)    # Plots Thrust against efficiency
    do_plot_TvsP(combined_data_dict)    # Plots Power against Thrust
6. Compile and execute analysis.py. Example:
   ```bash
   python3 analysis.py
    ```
### Trouble Shooting

## Contact
