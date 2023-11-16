import tkinter as tk
from tkinter import ttk


win = tk.Tk() #a window
win.title("SEN4017")

#win.state(newstate="zoomed") #to start the window full screen

win.geometry("300x200+600+300") #300x200 saize of the window and padding are right:600 and top:300 to open it on the stable location

#win.resizable(False,False) #keep the window at the same size

#ttk.Label(win, text="A label").grid(column=0, row=0) #puts the label to the specified column and row

label1 = ttk.Label(win, text="A Label")
label1.grid(column=0, row=1)  #there is no change, it overlaps the earlier cells 


def click_handler():
    button1.configure(text="User clicked")
    label1.configure(foreground="red")
    label1.configure(text="A red label")

button1 = ttk.Button(win, text="A Button", command=click_handler) #clickable button
#button1 = ttk.Button(win, text="A Button")
button1.grid(column=1, row=1)  #after the label, the button will be added next to it


win.mainloop() #to stay the window open even it has nothing to work ----> keeps the application running



