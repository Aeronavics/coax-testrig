![Aeronavics Logo](https://search.therobotreport.com/wp-content/uploads/2020/07/Aeronavics-Droidworx-NZ-334637.png)

# About
Contains all the code used for the investigation of optimizing thrust and efficiency of coaxial propeller systems. This was conducted and created by the 2022 - 2023 interns.

This branch contains the code to conduct each test through the **GUI**.

## Pre-requisites
[Python3](https://www.python.org/) and [Arduino IDE](https://www.arduino.cc/en/software) as linked. The following libraries are also required with their install commands seen below:

<!-- Libraries to install -->
```bash
pip install numpy
```

```bash
pip install matplotlib
```

```bash
pip install colorama
```

# Sections:
- Data Collection
  - Setup and Use 
  - Trouble Shooting
- Data Analysis 
  - Setup and Use

## Data Collection
All code for the data collection is found in the 'Test Rig Program' folder. Ensure you name the files of the same test the same as each other (with differing test numbers). Example:

18in 160kv 15in 220kv T1

### Setup and Use:

- Program Arduino with code
- Connect sensors according to wiring diagram
- Select com port and press connect
- Press START button under "Ramp test" to start automatic test
  - Warning: STOP button will not stop motors spinning instantaneously, shut off main power in emergency
  - Ramp test min and max speed as well as increment can be changed at top in arduino code
  - Data can be saved with download button or directly copied
  - Clear data table before performing another test, if data table fills up the application will crash
- Press motor buttons to enable/disable motors, green is on
- To set speed manually, press arm, move throttle slider, press send to set throttle
  - If motors do not spin when armed, press disarm, then arm again

- If any issues, restart app, restart arduino with button

- Visual studio free trial ended before contant stats readout at top was implemented, this is not supposed to work

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
4. Open 'plot_tests.py' and change the FOLDER_PATH to where the data is. Example:
    ```python
    FOLDER_PATH = '..\\Data\\Motor Config\\160-160vs160-220\\'  
    ```
    - If using MAC or Linux you will need to change the '\\\\' to '/ ' for the PATH_SLASHES variable
5. In plot_tests() inside plot_tests.py comment out the graphs you don't want to plot. Example
    ```python
    do_plot_PWMvsE(combined_data_dict)  # Plots PWM against efficiency
    do_plot_PWMvsT(combined_data_dict)  # Plots PWM against Thrust
    do_plot_TvsE(combined_data_dict)    # Plots Thrust against efficiency
    do_plot_TvsP(combined_data_dict)    # Plots Power against Thrust
6. Compile and execute plot_tests.py. Example:
   ```bash
   python3 plot_tests.py
    ```
### Trouble Shooting

Firstly if you have collected the data usign the GUI then this is the wrong page for you. Please go to the GUI_final branch.

The most common issue withe analysis scripts is the file path so please **triple check** your data is there and you have named the path correctly.

