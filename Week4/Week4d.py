import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog as fd

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap("python.ico")

def click_handler():
    ttk.Label(win, text=spin_value.get()).pack()

spin_value = tk.StringVar(value="3")
spin_values = tuple(range(1, 20, 3))
spinbox1 = ttk.Spinbox(win, values=spin_values, wrap=True, 
                       state="readonly", textvariable=spin_value, 
                       command=click_handler)

spinbox1.pack()


win.mainloop()