# MyFirstPythonProject.py
# by Justin Larsen, started 4/6/2025
#
# An experimental project for the beginning of my python learning journey while
# creating a windows GUI application.

import tkinter
from idlelib.multicall import MC_ENTER

import customtkinter

#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Justin's first Python Experiment")

def get_double_value():
    try:
        value_str = field1.get()
        value_float = float(value_str)
        result1.configure(text = f"Divided by Two: {value_float / 2}")
        print(f"The value as float is: {value_float}")
    except ValueError:
        print("Please enter a valid number.")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Welcome to my Python Experiment!")
title.pack(pady = 5)
author = customtkinter.CTkLabel(app, text = "by Justin Larsen")
author.pack(pady = 0)
instruct1 = customtkinter.CTkLabel(app, text = "Enter a number:")
instruct1.pack(pady = 5)

string_var = tkinter.StringVar()
field1 = customtkinter.CTkEntry(app, width=50, height=20, textvariable=string_var)
field1.pack()
button1 = customtkinter.CTkButton(app, text = "Calculate", command=get_double_value)
button1.pack()
result1 = customtkinter.CTkLabel(app,text = "")
result1.pack()

#Run App
app.mainloop()