# City_Weather_Comparison

## To view the final project
1. Clone GitHub repository to a local machine.

2. Open the 'City_Weather_Comparison.ipynb' file.

### Description of Notebook
This Jupyter Notebook contains daily weather data for Cincinnati OH/Northern KY, Louisville KY, New York City NY, and Los Angeles CA, from January 2022 to December 2022. Analysis of daily temperature highs, lows, and averages, as well as snowfall and precipitation will show which months are the hottest and coldest, including the months with the most precipitation and snowfall. Then group and compare the weather data between the four cities. 

## Required Programs
### The following programs must be installed in order to run this project
Download the latest version of python from https://www.python.org/downloads/ and follow the recommended steps. 

Follow the steps below to install the Jupyter Notebook package on macOS using pip:

Step 1: Install the latest Python3 in MacOS.

Step 2: Check if pip3 and Python3 are correctly installed. python3 --version pip3 --version

Step 3: Upgrade your pip to avoid errors during installation. pip3 install --upgrade pip

Step 4: Enter the following command to install Jupyter Notebook using pip3. pip3 install jupyter

Step 5: Enter the command Jupyter Notebook in your terminal to start up Jupyter Notebook. 

### Alternate Method
Jupyter notebook can be downloaded and used via Visual Studio Code extension.

Step 1: Download Visual Studio Code from https://code.visualstudio.com and click on the Download icon.

Step 2: Select the version that corresponds to your operating system.

Step 3: Follow the instalation instructions.

Step 4: Once Visual Studio Code is installed click the Extensions icon, type in Jupyter Notebook.

Step 5: Once the desired package is selected, click Install.

### Windows Instructions
To install Jupyter Notebook, Pandas, and Matplotlib using pip on Windows, fist make sure pip is updated in the Windows system.
Use the following command to update pip: 

python -m pip install --upgrade pip python -m pip install jupyter pip install pandas pip install matplotlib

## Required Packages
Use pip3 to install Pandas:
pip3 install pandas

Use pip3 to install Matplotlib:
pip3 install matplotlib

Numpy and DateTime should come with python, if not, use the following instructions to install each package:

Use pip3 to install DateTime:
pip3 install DateTime

Use pip3 to install Numpy:
pip3 install numpy

### If using a virtual environment or conda environment

Use pip3 to install ipykernel:
pip3 install ipykernel

### To generate a requirements.txt file
Open terminal, once inside, type, pip3 instal pigar, then press enter.

Next, type, pigar generate, then press enter.

## Features Required for Project by CodeKY
Feature 1: Read in local csv file using Pandas read_function.

Feature 2: Use built in Pandas functions to remove unnecessary columns, change column names, fill NaN values with 0, change dates to DateTime, concatinate and groupby data.

Feature 3: Use Pandas to perform calculations on each csv dataset. Use mean(), max(), min(), sum(), and round() functions.

Feature 4: Create plot and bar graphs with Matplotlib.

Feature 5: Add Markdwons on JupyterNotebook and description of data analysis.
