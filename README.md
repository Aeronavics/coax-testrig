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

*add your naming scheme here Reuben*

### Setup and Use:

*Add your stuff Reuben*


### Trouble Shooting

*Add your stuff Reuben*
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
4. Open 'plot_tests.py' and change the PATH_FOLDER to where the data is. This should be relative to the 'Data_scripts' folder. Example:
    ```python
    PATH FOLDER = 'Data\\Motor Config\\160-160vs160-220\\'   # Change to what path your folder is in (MACS use '/')
    ```
    - If using MAC or Linux you will need to change the '\\\\' to '/ ' for the PATH_SLASHES variable
5. In 'plot_tests.py inside analysis.py comment out the graphs you don't want to plot. Example
    ```python
    do_plot_PWMvsE(combined_data_dict)  # Plots PWM against efficiency
    do_plot_PWMvsT(combined_data_dict)  # Plots PWM against Thrust
    do_plot_TvsE(combined_data_dict)    # Plots Thrust against efficiency
    do_plot_TvsP(combined_data_dict)    # Plots Power against Thrust
6. Compile and execute analysis.py. Example:
   ```bash
   python3 plot_tests.py
    ```
### Trouble Shooting

Firstly if you have collected the data usign the GUI then this is the wrong page for you. Please go to the GUI_final branch.

The most common issue withe analysis scripts is the file path so please **triple check** your data is there and you have named the path correctly.

