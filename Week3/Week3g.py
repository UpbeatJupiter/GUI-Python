import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")


label1 = ttk.Label(win, text="Number 1: ")
label2 = ttk.Label(win, text="Number 2: ")
label3 = ttk.Label(win, text="Operator: ")

entry1 = ttk.Entry(win, width=15)
entry2 = ttk.Entry(win, width=15)

operator = tk.StringVar()

combo1 = ttk.Combobox(win, width=12, textvariable=operator, state="readonly")
combo1["values"] = ("Add", "Subtract")

def click_handler():
    selected_operator = operator.get()
    if selected_operator == "Add":
        result = int(entry1.get()) + int(entry2.get())
    else:
        result = int(entry1.get()) - int(entry2.get())
    
    button1.configure(text="The result is" + result)
    entry1.focus_set()



button1 = ttk.Button(win, text="Calculate", command=click_handler)

label1.grid(row=0, column=0, padx= 10, pady= 10)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0, padx= 10, pady= 10)

entry1.grid(row=0, column=1, padx= 10, pady= 10)
entry2.grid(row=1, column=1, padx= 10, pady= 10)
combo1.grid(row=2, column=1, padx=(0, 10))

button1.grid(row=3, column=0, columnspan=2, sticky="we")



win.mainloop()