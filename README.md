# Attendance Calculator-A QuickCheck

# Overview:
Welcome to the Attendance Calculator project! This Python-based tool is crafted to simplify attendance tracking for NMIMS Hyderabad STME students (CSE-DS branch). It offers swift calculations through a terminal-based code and an interactive tkinter interface.

## Key Features:

### 1.Terminal Code

### 2.Interface

### 3.Visualization

## Getting Started:

### Terminal Code:

 1. Directly run the terminal attendance calculator code from terminal code folder.

 2. Choose between Semester Overall Calculator or Month Overall Calculator for your specific needs.

 
    
### Interface Code:
•	Download the attandance_ttk_code.py code along with data(data_att1.txt) text file (contains subjects and semester details) from user interface attendance calculator folder.

•	Install the necessary packages using the following commands :

pip install ttkbootstrap

pip install matplotlib

•	Update lines 19 and 20 in the interface code with the correct file location od data text files:

#### Update the file path

data_file_path = "your/data/file/path.txt"

#### Save as CSV after loading as TXT

values_df = pd.read_csv(data_file_path)

values_df.to_csv('your/data/file/path.csv', index=None)

•	Run the interface code.

### Disclaimer:

While the semester percentage calculator provides accurate results, slight changes may occur in the month percentage due to mid-semester weightage adjustments.

Happy calculating!
