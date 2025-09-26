"""
Name:   Code-Guru_Wk_6.py
Author: Jake Nicholes
Date:   9/25/2025
"""

#start by importing tkinter so we can build as a GUI
import tkinter as tk

#declare calculation variable
calculation = ""

#create addition function
def add_to_calculation(symbol):
    global calculation
    #Make calculation calculate based on string so that symbols can be used in the calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#create evaluate function
def evaluate_calculation():
    #Eval is risky, people can inject code into it. Use caution when using this function
    global calculation
    #attempt to calculate using the eval py function
    try:
        calculation= str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    
    #Handle exceptions
    except:
        clear_field()
        text_result.insert(1.0, "error")
        pass

#create clear function
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    pass

#begin creation of GUI
root = tk.Tk()
root.geometry("500x350")

#Create text usage on gui
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

root.mainloop()