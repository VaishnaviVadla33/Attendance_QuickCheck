from tkinter import *
import ttkbootstrap as tb
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
import math

# Creating a window
root = tb.Window(themename="solar")
root.title("ATTENDANCE CALCULATOR")

# Creating a notebook
my_notebook = tb.Notebook(root, bootstyle="success", width=1600, height=900)
my_notebook.pack(pady=20)

# Load the entire CSV file
values_df = pd.read_csv("D:/Projects_python/attendace_calculator/data_att1.txt")
values_df.to_csv('D:/Projects_python/attendace_calculator/data_att1.csv', index=None)

def clear_frame_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def calculate_percentage_s():
    try:
        subject_name = sub_combo_s1.get()
        total_count_t = int(total_count_t_entry_s1.get())
        present_count_t = int(entry_present_count_t_s1.get())
        total_count_p = int(total_count_p_entry_s1.get())
        present_count_p = int(entry_present_count_p_s1.get())
        xt = int(theory_var_s1.get())
        xp = int(practical_var_s1.get())

        if (total_count_t < present_count_t) or (total_count_p < present_count_p):
            raise ValueError("Present count can't be greater than Total count.")
        
        if total_count_t == 0:
            x1=0
        else:
            x1 = (present_count_t * 100) / total_count_t
        
        if total_count_p == 0:
            x2=0
        else:
            x2 = (present_count_p * 100) / total_count_p

        # Weightage calculation
        t = xt / (xt + xp)
        p = xp / (xt + xp)
        result = (x1 * t) + (x2 * p)

        messagebox.showinfo(f"RESULT", f"Your percentage in {subject_name} is:\n{result:.2f}%")
        # Display the result in a bar graph
        plot_percentage_bar_graph_s(result)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def plot_percentage_bar_graph_s(percentage):
    # Clear existing widgets in the graph frame
    clear_frame_widgets(graph_frame_s)

    fig, ax = plt.subplots(figsize=(4, 4))
    bars = ax.bar(["Percentage"], [percentage], color='blue', width=0.2)
    ax.set_ylabel('Percentage')
    ax.set_title('Attendance Percentage in semester')

    # Add labels inside the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{percentage:.2f}%', ha='center', va='bottom')

    # Customize x-axis and y-axis with ticks
    ax.set_xticks([])
    ax.set_yticks(range(0, 101, 10))
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 100)

    # Adjust layout and add padding
    fig.tight_layout(pad=4)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame_s)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()



# Adding our frames to the notebook
# Page 1
tab1 = tb.Frame(my_notebook)
my_notebook.add(tab1, text="Semester attendance")

my_label1 = tb.Label(tab1, text="Semester attendance", font=("Helvetica", 30)).pack(pady=30)

# Inside tab1 (the first page of the notebook)
s_percent_frame = tb.Frame(tab1, bootstyle="dark")
s_percent_frame.pack(side='left', pady=20)

tb.Label(s_percent_frame, text="Want to check your percentage", bootstyle="white", font=("Helvetica", 20)).pack(pady=40)

def update_subjects_s1(event):
    semester = sem_combo_s1.get()
    subjects_df = values_df[values_df['sem'] == semester]
    sub_combo_s1["values"] = subjects_df['subject'].tolist()

sem_label = tb.Label(s_percent_frame, text="Semester:", bootstyle="default")
sem_label.pack()

sem_combo_s1 = tb.Combobox(s_percent_frame, values=["sem 1", "sem 2", "sem 3", "sem 4", "sem 5"], state="readonly",width=40)
sem_combo_s1.pack()
sem_combo_s1.bind("<<ComboboxSelected>>", update_subjects_s1)

# Update the entries based on the selected subject
def update_entries_s1(event):
    values_df_lower = values_df.apply(lambda x: x.astype(str).str.lower())
    subject = sub_combo_s1.get()
    semester = sem_combo_s1.get()
    selected_row = values_df_lower[(values_df_lower['subject'] == subject.lower()) & (values_df_lower['sem'] == semester.lower())]
    if semester == "sem 5":
        theory_var_s1.set(0)
        practical_var_s1.set(0)
    else:
        # update the values of the entries
        theory_var_s1.set(int(selected_row["theory count in week"].values[0]))
        practical_var_s1.set(int(selected_row["practical count in week"].values[0]))

# GUI elements
sub_label_s1 = tb.Label(s_percent_frame, text="Subject:", bootstyle="default")
sub_label_s1.pack()

sub_combo_s1 = tb.Combobox(s_percent_frame, values=[], state="readonly",width=40)
sub_combo_s1.pack()
sub_combo_s1.bind("<<ComboboxSelected>>", update_entries_s1)

#total_count_t_var = tk.IntVar()
theory_var_s1 = tk.IntVar()
practical_var_s1 = tk.IntVar()

total_count_t_label_s1 = tb.Label(s_percent_frame, text="Total count in theory:", bootstyle="warning")
total_count_t_label_s1.pack()
total_count_t_entry_s1 = tb.Entry(s_percent_frame, state="write")
total_count_t_entry_s1.pack()

entry_present_count_t_s1 =tb.Label(s_percent_frame, text="Enter Attended classes count in theory:",bootstyle="warning")
entry_present_count_t_s1 .pack()
entry_present_count_t_s1 =tb.Entry(s_percent_frame, state="write")
entry_present_count_t_s1.pack()

total_count_p_label_s1 = tb.Label(s_percent_frame, text="Total count in practical", bootstyle="danger")
total_count_p_label_s1.pack()
total_count_p_entry_s1 = tb.Entry(s_percent_frame, state="write")
total_count_p_entry_s1.pack()

entry_present_count_p_s1=tb.Label(s_percent_frame, text="Enter Attended classes count in practical:",bootstyle="danger")
entry_present_count_p_s1.pack()
entry_present_count_p_s1 =tb.Entry(s_percent_frame, state="write")
entry_present_count_p_s1.pack()

theory_label_s1 = tb.Label(s_percent_frame, text="Theory count in week:", bootstyle="success")
theory_label_s1.pack()
theory_entry_s1 = tb.Entry(s_percent_frame, textvariable=theory_var_s1, state="write")
theory_entry_s1.pack()

practical_label_s1 = tb.Label(s_percent_frame, text="Practical count in week:", bootstyle="success")
practical_label_s1.pack()
practical_entry_s1 = tb.Entry(s_percent_frame, textvariable=practical_var_s1, state="write")
practical_entry_s1.pack()

tb.Button(s_percent_frame, text="Calculate Percentage", bootstyle="primary-outline", command=calculate_percentage_s).pack()


####################################################################################
# Subframe for semester estimations
s_estimate_frame = tb.Frame(tab1, bootstyle="dark")  # Subframe for semester percentage 
s_estimate_frame.pack(side='right', pady=20)

# Add widgets for estimation within the subtract_frame
tb.Label(s_estimate_frame, text="Estimate absents to be taken", bootstyle="white",font=("Helvetica",20)).pack(pady=40)


def calculate_estimation_s():
    # Get values from entry3 and entry4, perform subtraction, and display result
    try:
        subject_name = sub_combo_s2.get()
        total_count = int(entry_total_count_s2.get())
        xt = int(theory_entry_s2.get())
        xp = int(practical_entry_s2.get())
        default_percent = int(entry_default_percent_s.get())

        if total_count == 0:
            raise ValueError("Total count cannot be zero.")
        weeks = total_count // xt
        total_theory_classes = weeks * xt
        total_practical_classes = weeks * xp

        classes_to_attended_theory = ((default_percent * total_theory_classes) / 100)
        if classes_to_attended_theory % 1 != 0:
            classes_to_attended_theory = ((default_percent * total_theory_classes) // 100) + 1
        else:
            classes_to_attended_theory = ((default_percent * total_theory_classes) / 100)

        absents_to_take1 = (total_theory_classes) - (classes_to_attended_theory)

        classes_to_attended_practical = ((default_percent * total_practical_classes) / 100)
        if classes_to_attended_practical % 1 != 0:
            classes_to_attended_practical = ((default_percent * total_practical_classes) // 100) + 1
        else:
            classes_to_attended_practical = ((default_percent * total_practical_classes) / 100)

        absents_to_take2 = (total_practical_classes) - (classes_to_attended_practical)

        result = (absents_to_take1 + absents_to_take2)

        
        messagebox.showinfo(f"RESULT", f"<---   IN {subject_name}:   ---> \n IN THEORY \nClasses to attend : {classes_to_attended_theory} \nAbsents to take: {absents_to_take1} \nIN PRACTICAL: \nClasses to attend : {classes_to_attended_practical} \nAbsents to take : {absents_to_take2} \n<-----------------------------> \nTOTAL LEAVE OF: {result} ")
        # Display the result in a pie chart
        plot_estimation_pie_chart_s(absents_to_take1, absents_to_take2)

    except ValueError as e:
        messagebox.showerror("Error", str(e))



def plot_estimation_pie_chart_s(absents_theory, absents_practical):
    # Clear existing widgets in the graph frame
    clear_frame_widgets(graph_frame_s)

    labels = ['Theory Classes', 'Practical Classes']
    sizes = [absents_theory, absents_practical]

    fig, ax = plt.subplots(figsize=(4, 4))
    # Check for zero sum to avoid division by zero
    if sum(sizes) != 0:
        autopct_func = lambda p: '{:.0f}'.format(p * sum(sizes) / 100)
    else:
        autopct_func = lambda p: ''

    ax.pie(sizes, labels=labels, startangle=90, colors=['blue', 'green'], autopct=autopct_func)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.


    ax.set_title('Attendance Estimation in semester')

    # Adjust layout and add padding
    fig.tight_layout(pad=3)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame_s)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

#````````````````````````````````````````````````````````````````````````````````````````````````````
def update_subjects_s2(event):
    semester_s2 = sem_combo_s2.get()
    subjects_df_s2 = values_df[values_df['sem'] == semester_s2]
    sub_combo_s2["values"] = subjects_df_s2['subject'].tolist()

sem_label_est = tb.Label(s_estimate_frame, text="Semester:", bootstyle="default")
sem_label_est.pack()

sem_combo_s2 = tb.Combobox(s_estimate_frame, values=["sem 1", "sem 2", "sem 3", "sem 4", "sem 5"], state="readonly",width=40)
sem_combo_s2.pack()
sem_combo_s2.bind("<<ComboboxSelected>>", update_subjects_s2)



# Update the entries based on the selected subject
def update_entries_s2(event):
    values_df_lower_s2 = values_df.apply(lambda x: x.astype(str).str.lower())
    subject_s2 = sub_combo_s2.get()
    semester_s2 = sem_combo_s2.get()
    selected_row_s2 = values_df_lower_s2[(values_df_lower_s2['subject'] == subject_s2.lower()) & (values_df_lower_s2['sem'] == semester_s2.lower())]
    if semester_s2 == "sem 5":
        total_count_t_var_s2.set(0)
        theory_var_s2.set(0)
        practical_var_s2.set(0)
    else:
        # update the values of the entries
        total_count_t_var_s2.set(int(selected_row_s2["total count"].values[0]))
        theory_var_s2.set(int(selected_row_s2["theory count in week"].values[0]))
        practical_var_s2.set(int(selected_row_s2["practical count in week"].values[0]))

# GUI elements
sub_label_s2 = tb.Label(s_estimate_frame, text="Subject:", bootstyle="default")
sub_label_s2.pack()

sub_combo_s2 = tb.Combobox(s_estimate_frame, values=[], state="readonly",width=40)
sub_combo_s2.pack()
sub_combo_s2.bind("<<ComboboxSelected>>", update_entries_s2)

total_count_t_var_s2 = tk.IntVar()
theory_var_s2 = tk.IntVar()
practical_var_s2 = tk.IntVar()


label_total_count_s2 = tb.Label(s_estimate_frame, text="Total classes count(as per course policy)", bootstyle="warning")
label_total_count_s2.pack()
entry_total_count_s2 = tb.Entry(s_estimate_frame, textvariable=total_count_t_var_s2, state="write")
entry_total_count_s2.pack()

theory_label_s2 = tb.Label(s_estimate_frame, text="Theory count in week:", bootstyle="danger")
theory_label_s2.pack()
theory_entry_s2 = tb.Entry(s_estimate_frame, textvariable=theory_var_s2, state="write")
theory_entry_s2.pack()

practical_label_s2 = tb.Label(s_estimate_frame, text="Practical count in week:", bootstyle="danger")
practical_label_s2.pack()
practical_entry_s2 = tb.Entry(s_estimate_frame, textvariable=practical_var_s2, state="write")
practical_entry_s2.pack()

entry_default_percent_s=tb.Label(s_estimate_frame, text="Enter Default percentage", bootstyle="success")
entry_default_percent_s.pack()
entry_default_percent_s = Entry(s_estimate_frame)
entry_default_percent_s.insert(0, "80")  # Set default value to 80
entry_default_percent_s.pack()


tb.Button(s_estimate_frame, text="Estimate Leaves",bootstyle="primary-outline", command=calculate_estimation_s).pack()




#adding our frames to the notebook
###########################################################################################################################################
#page 2


tab2=tb.Frame(my_notebook)
my_notebook.add(tab2, text="Monthly attendance")

my_label2 = tb.Label(tab2, text="Monthly attendance", font=("Helvetica", 30)).pack(pady=30)

def calculate_percentage_m():
    try:
        subject_name = sub_combo_m1.get()
        total_count_t = int(total_count_t_entry_m1.get())
        present_count_t = int(entry_present_count_t_m1.get())
        total_count_p = int(total_count_p_entry_m1.get())
        present_count_p = int(entry_present_count_p_m1.get())
        xt = int(theory_var_m1.get())
        xp = int(practical_var_m1.get())


        if  (present_count_t > total_count_t) or (present_count_p > total_count_p) :
            raise ValueError("Present count can't be greater than Total count.")

        if total_count_t == 0:
            x1=0
        else:
            x1 = (present_count_t * 100) / total_count_t
        
        if total_count_p == 0:
            x2=0
        else:
            x2 = (present_count_p * 100) / total_count_p

        # Weightage calculation
        t = xt / (xt + xp)
        p = xp / (xt + xp)
        result = (x1 * t) + (x2 * p)

        messagebox.showinfo(f"RESULT", f"Your percentage in {subject_name} is:\n{result:.2f}%")
        # Display the result in a bar graph
        plot_percentage_bar_graph_m(result)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def plot_percentage_bar_graph_m(percentage):
    # Clear existing widgets in the graph frame
    clear_frame_widgets(graph_frame_m)

    fig, ax = plt.subplots(figsize=(4, 4))
    bars = ax.bar(["Percentage"], [percentage], color='blue', width=0.2)
    ax.set_ylabel('Percentage')
    ax.set_title('Monthly Attendance Percentage')

    # Add labels inside the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, f'{percentage:.2f}%', ha='center', va='bottom')

    # Customize x-axis and y-axis with ticks
    ax.set_xticks([])
    ax.set_yticks(range(0, 101, 10))
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 100)

    # Adjust layout and add padding
    fig.tight_layout(pad=4)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame_m)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()


# Inside tab1 (the first page of the notebook)
m_percent_frame = tb.Frame(tab2, bootstyle="dark")
m_percent_frame.pack(side='left', pady=20)

tb.Label(m_percent_frame, text="Confirm your percentage", bootstyle="white", font=("Helvetica", 20)).pack(pady=40)

def update_subjects_m1(event):
    semester = sem_combo_m1.get()
    subjects_df = values_df[values_df['sem'] == semester]
    sub_combo_m1["values"] = subjects_df['subject'].tolist()

sem_label_m1 = tb.Label(m_percent_frame, text="month:", bootstyle="default")
sem_label_m1.pack()

sem_combo_m1 = tb.Combobox(m_percent_frame, values=["sem 1", "sem 2", "sem 3", "sem 4", "sem 5"], state="readonly",width=40)
sem_combo_m1.pack()
sem_combo_m1.bind("<<ComboboxSelected>>", update_subjects_m1)


# Update the entries based on the selected subject
def update_entries_m1(event):
    values_df_lower = values_df.apply(lambda x: x.astype(str).str.lower())
    subject = sub_combo_m1.get()
    semester = sem_combo_m1.get()
    selected_row = values_df_lower[(values_df_lower['subject'] == subject.lower()) & (values_df_lower['sem'] == semester.lower())]
    if semester == "sem 5":
        theory_var_m1.set(0)
        practical_var_m1.set(0)
    else:
        # update the values of the entries
        theory_var_m1.set(int(selected_row["theory count in week"].values[0]))
        practical_var_m1.set(int(selected_row["practical count in week"].values[0]))

# GUI elements
sub_label_m1 = tb.Label(m_percent_frame, text="Subject:", bootstyle="default")
sub_label_m1.pack()

sub_combo_m1 = tb.Combobox(m_percent_frame, values=[], state="readonly",width=40)
sub_combo_m1.pack()
sub_combo_m1.bind("<<ComboboxSelected>>", update_entries_m1)

theory_var_m1 = tk.IntVar()
practical_var_m1 = tk.IntVar()

total_count_t_label_m1 = tb.Label(m_percent_frame, text="Total count in theory:", bootstyle="warning")
total_count_t_label_m1.pack()
total_count_t_entry_m1 = tb.Entry(m_percent_frame, state="write")
total_count_t_entry_m1.pack()

entry_present_count_t_m1=tb.Label(m_percent_frame, text="Enter Attended classes count in theory:",bootstyle="warning")
entry_present_count_t_m1.pack()
entry_present_count_t_m1 = tb.Entry(m_percent_frame, state="write")
entry_present_count_t_m1.pack()

total_count_p_label_m1 = tb.Label(m_percent_frame, text="Total count in practical", bootstyle="danger")
total_count_p_label_m1.pack()
total_count_p_entry_m1 = tb.Entry(m_percent_frame, state="write")
total_count_p_entry_m1.pack()

entry_present_count_p_m1=tb.Label(m_percent_frame, text="Enter Attended classes count in practical:",bootstyle="danger")
entry_present_count_p_m1.pack()
entry_present_count_p_m1 = tb.Entry(m_percent_frame, state="write")
entry_present_count_p_m1.pack()

theory_label_m1 = tb.Label(m_percent_frame, text="Theory count in week:", bootstyle="success")
theory_label_m1.pack()
theory_entry_m1 = tb.Entry(m_percent_frame, textvariable=theory_var_m1, state="write")
theory_entry_m1.pack()

practical_label_m1 = tb.Label(m_percent_frame, text="Practical count in week:", bootstyle="success")
practical_label_m1.pack()
practical_entry_m1 = tb.Entry(m_percent_frame, textvariable=practical_var_m1, state="write")
practical_entry_m1.pack()

tb.Button(m_percent_frame, text="Calculate Percentage", bootstyle="primary-outline", command=calculate_percentage_m).pack()

####################################################################################
# Subframe for monthly estimations
m_estimate_frame = tb.Frame(tab2, bootstyle="dark")  # Subframe for semester percentage 
m_estimate_frame.pack(side='right', pady=20)

# Add widgets for month widgets
tb.Label(m_estimate_frame, text="Estimate absents in midst of Semester", bootstyle="white",font=("Helvetica",20)).pack(pady=40)


def calculate_estimation_m():
    # Get values from entry3 and entry4, perform subtraction, and display result
    try:
        subject_name = sub_combo_m2.get()
        total_count = int(total_count_t_var_m2.get())
        xt = int(theory_var_m2.get())
        xp = int(practical_var_m2.get())
        #default_percent=int(entry_default_percent_m.get())
        default_percent = float(entry_default_percent_m.get())  # Convert to float

        if math.isnan(default_percent):
            raise ValueError("Default percentage cannot be NaN.")

        if total_count == 0:
            raise ValueError("Total count cannot be zero.")
        total_classes_theory_month = int(entry_total_classes_theory_month.get())
        present_classes_theory_month = int(entry_present_classes_theory_month.get())
        total_classes_practical_month = int(entry_total_classes_practical_month.get())
        present_classes_practical_month = int(entry_present_classes_practical_month.get())

        weeks=total_count//xt
        total_theory_classes=weeks*xt
        total_practical_classes=weeks*xp

        if present_classes_theory_month > total_classes_theory_month or present_classes_practical_month > total_classes_practical_month:
            raise ValueError("Present count can't be greater than Total count.")

        classes_to_attended_theory = ((default_percent * total_theory_classes) / 100)
        if classes_to_attended_theory % 1 != 0:
            classes_to_attended_theory = ((default_percent * total_theory_classes) // 100) + 1
        else:
            classes_to_attended_theory = ((default_percent * total_theory_classes) / 100)
        balance_t = (total_classes_theory_month) - (present_classes_theory_month)
        absents_to_take1 = (total_theory_classes) - (classes_to_attended_theory)
        absents_to_take11 = (total_theory_classes) - (classes_to_attended_theory) - (balance_t)


        classes_to_attended_practical = ((default_percent * total_practical_classes) / 100)
        if classes_to_attended_practical % 1 != 0:
            classes_to_attended_practical = ((default_percent * total_practical_classes) // 100) + 1
        else:
            classes_to_attended_practical = ((default_percent * total_practical_classes) / 100)

        balance_p = (total_classes_practical_month) - (present_classes_practical_month)
        absents_to_take2 = (total_practical_classes) - (classes_to_attended_practical)
        absents_to_take22 = (total_practical_classes) - (classes_to_attended_practical) - (balance_p)

        result = (absents_to_take11 + absents_to_take22) 

        if ((balance_t <= absents_to_take1) and (balance_p <= absents_to_take2)): 
            messagebox.showinfo(f"RESULT", f"YOU CAN TAKE {absents_to_take11} LEAVES in theory classes \nYOU CAN TAKE {absents_to_take22} LEAVES in practical classes \nTOTAL YOU CAN TAKE LEAVE OF: {result}")
        elif (balance_t > absents_to_take1) and (balance_p > absents_to_take2):
            messagebox.showinfo(f"RESULT", f"You are in defaulter list \n cause maximum leaves can be taken in {subject_name} theory classes is : {absents_to_take1} and \nmaximum leaves can be taken in {subject_name} practical classes is : {absents_to_take2}\n")
        elif (balance_t > absents_to_take1):
            messagebox.showinfo(f"RESULT", f"You are in defaulter list, cause maximum leaves can be taken in  {subject_name} theory classes is : {absents_to_take1}")
        elif (balance_p > absents_to_take2):
            messagebox.showinfo(f"RESULT", f"You are in defaulter list, cause maximum leaves can be taken in {subject_name} practical classes is : {absents_to_take2}")
        

        # Display the result in a pie chart
        plot_estimation_pie_chart_m(absents_to_take11, absents_to_take22)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Function to plot estimation pie chart
def plot_estimation_pie_chart_m(absents_theory, absents_practical):
    # Clear existing widgets in the graph frame
    clear_frame_widgets(graph_frame_m)
    labels = ['Theory Classes', 'Practical Classes']
    sizes = [absents_theory, absents_practical]

    fig, ax = plt.subplots(figsize=(4, 4))

    # Check for zero sum to avoid division by zero
    if sum(sizes) != 0:
        autopct_func = lambda p: '{:.0f}'.format(p * sum(sizes) / 100)
    else:
        autopct_func = lambda p: ''

    ax.pie(sizes, labels=labels, startangle=90, colors=['blue', 'green'], autopct=autopct_func)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

    ax.set_title('Monthly Attendance Estimation')

    # Adjust layout and add padding
    fig.tight_layout(pad=3)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame_m)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

def update_subjects_m2(event):
    semester_m2 = sem_combo_m2.get()
    subjects_df_m2 = values_df[values_df['sem'] == semester_m2]
    sub_combo_m2["values"] = subjects_df_m2['subject'].tolist()

sem_label_est_m2 = tb.Label(m_estimate_frame, text="Semester:", bootstyle="default")
sem_label_est_m2.pack()

sem_combo_m2 = tb.Combobox(m_estimate_frame, values=["sem 1", "sem 2", "sem 3", "sem 4", "sem 5"], state="readonly",width=40)
sem_combo_m2.pack()
sem_combo_m2.bind("<<ComboboxSelected>>", update_subjects_m2)

# Update the entries based on the selected subject
def update_entries_m2(event):
    values_df_lower_m2 = values_df.apply(lambda x: x.astype(str).str.lower())
    subject_m2 = sub_combo_m2.get()
    semester_m2 = sem_combo_m2.get()
    selected_row_m2 = values_df_lower_m2[(values_df_lower_m2['subject'] == subject_m2.lower()) & (values_df_lower_m2['sem'] == semester_m2.lower())]
    if semester_m2 == "sem 5":
        total_count_t_var_m2.set(0)
        theory_var_m2.set(0)
        practical_var_m2.set(0)
        #total_count_p_var.set(0)  # Set total_count_p to 0 for sem 3
    else:
        # update the values of the entries
        total_count_t_var_m2.set(int(selected_row_m2["total count"].values[0]))
        theory_var_m2.set(int(selected_row_m2["theory count in week"].values[0]))
        practical_var_m2.set(int(selected_row_m2["practical count in week"].values[0]))

       
# GUI elements

sub_label_m2 = tb.Label(m_estimate_frame, text="Subject:", bootstyle="default")
sub_label_m2.pack()

sub_combo_m2 = tb.Combobox(m_estimate_frame, values=[], state="readonly",width=40)
sub_combo_m2.pack()
sub_combo_m2.bind("<<ComboboxSelected>>", update_entries_m2)

total_count_t_var_m2 = tk.IntVar()
theory_var_m2 = tk.IntVar()
practical_var_m2 = tk.IntVar()


label_total_count_m2 = tb.Label(m_estimate_frame, text="Total classes count(as per course policy)", bootstyle="warning")
label_total_count_m2.pack()
entry_total_count_m2 = tb.Entry(m_estimate_frame, textvariable=total_count_t_var_m2, state="write")
entry_total_count_m2.pack()

theory_label_m2 = tb.Label(m_estimate_frame, text="Theory count in week:", bootstyle="danger")
theory_label_m2.pack()
theory_entry_m2 = tb.Entry(m_estimate_frame, textvariable=theory_var_m2, state="write")
theory_entry_m2.pack()

practical_label_m2 = tb.Label(m_estimate_frame, text="Practical count in week:", bootstyle="danger")
practical_label_m2.pack()
practical_entry_m2 = tb.Entry(m_estimate_frame, textvariable=practical_var_m2, state="write")
practical_entry_m2.pack()

entry_default_percent_m=tb.Label(m_estimate_frame, text="Enter Default percentage", bootstyle="success")
entry_default_percent_m.pack()
entry_default_percent_m = tb.Entry(m_estimate_frame)
entry_default_percent_m.insert(0,"80")
entry_default_percent_m.pack()

entry_total_classes_theory_month=tb.Label(m_estimate_frame, text="Enter total theory classes till this month:", bootstyle="secondary")
entry_total_classes_theory_month.pack()
entry_total_classes_theory_month = tb.Entry(m_estimate_frame,state="write")
entry_total_classes_theory_month.pack()

entry_present_classes_theory_month=tb.Label(m_estimate_frame, text="Enter present theory classes till this month:", bootstyle="secondary")
entry_present_classes_theory_month.pack()
entry_present_classes_theory_month = tb.Entry(m_estimate_frame,state="write")
entry_present_classes_theory_month.pack()

entry_total_classes_practical_month=tb.Label(m_estimate_frame, text="Enter total practical classes till this month:", bootstyle="info")
entry_total_classes_practical_month.pack()
entry_total_classes_practical_month = tb.Entry(m_estimate_frame,state="write")
entry_total_classes_practical_month.pack()

entry_present_classes_practical_month=tb.Label(m_estimate_frame, text="Enter present practical classes till this month:", bootstyle="info")
entry_present_classes_practical_month.pack()
entry_present_classes_practical_month = tb.Entry(m_estimate_frame,state="write")
entry_present_classes_practical_month.pack()


tb.Button(m_estimate_frame, text="Estimate Leaves",bootstyle="primary-outline", command=calculate_estimation_m).pack()


# Create a frame within each tab for displaying the graphs
graph_frame_s = tb.Frame(tab1)
graph_frame_s.pack(side='bottom')


graph_frame_m = tb.Frame(tab2)
graph_frame_m.pack(side='bottom')


# success colored default scrollbar style
tb.Scrollbar(my_notebook)

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()