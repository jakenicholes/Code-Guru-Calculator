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
root.geometry("375x250")

#Create text usage on gui
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#ADD BUTTONS
#add 1 button
digit_1 = tk.Button(root, text="1", command= lambda: add_to_calculation(1), width= 5, font=("Arial", 16))
digit_1.grid(row=2, column=1)

#add 2 butotn
digit_2 = tk.Button(root, text="2", command= lambda: add_to_calculation(2), width= 5, font=("Arial", 16))
digit_2.grid(row=2, column=2)

#add 3 button
digit_3 = tk.Button(root, text="3", command= lambda: add_to_calculation(3), width= 5, font=("Arial", 16))
digit_3.grid(row=2, column=3)

#add 4 button
digit_4 = tk.Button(root, text="4", command= lambda: add_to_calculation(4), width= 5, font=("Arial", 16))
digit_4.grid(row=3, column=1)

#add 5 button
digit_5 = tk.Button(root, text="5", command= lambda: add_to_calculation(5), width= 5, font=("Arial", 16))
digit_5.grid(row=3, column=2)

#add 6 button
digit_6 = tk.Button(root, text="6", command= lambda: add_to_calculation(6), width= 5, font=("Arial", 16))
digit_6.grid(row=3, column=3)

#add 7 button
digit_7 = tk.Button(root, text="7", command= lambda: add_to_calculation(7), width= 5, font=("Arial", 16))
digit_7.grid(row=4, column=1)

#add 8 button
digit_8 = tk.Button(root, text="8", command= lambda: add_to_calculation(8), width= 5, font=("Arial", 16))
digit_8.grid(row=4, column=2)

#add 9 button
digit_9 = tk.Button(root, text="9", command= lambda: add_to_calculation(9), width= 5, font=("Arial", 16))
digit_9.grid(row=4, column=3)

#add 0 button
digit_0 = tk.Button(root, text="0", command= lambda: add_to_calculation(0), width= 5, font=("Arial", 16))
digit_0.grid(row=5, column=2)

#add + button
digit_plus = tk.Button(root, text="+", command= lambda: add_to_calculation("+"), width= 5, font=("Arial", 16))
digit_plus.grid(row=2, column=4)

#add - button
digit_minus = tk.Button(root, text="-", command= lambda: add_to_calculation("-"), width= 5, font=("Arial", 16))
digit_minus.grid(row=2, column=5)

#add * button
digit_multiply = tk.Button(root, text="*", command= lambda: add_to_calculation("*"), width= 5, font=("Arial", 16))
digit_multiply.grid(row=3, column=4)

#add / button
digit_divide = tk.Button(root, text="/", command= lambda: add_to_calculation("/"), width= 5, font=("Arial", 16))
digit_divide.grid(row=3, column=5)

#add = button
digit_equals = tk.Button(root, text="=", command= lambda: evaluate_calculation, width= 5, font=("Arial", 16))
digit_equals.grid(row=4, column=4)

#add CLEAR button
"""
digit_clear = tk.Button(root, text="1", command= lambda: ************, width= 5, font=("Arial", 16))
digit_clear.grid(row=4, column=5)
"""
root.mainloop()