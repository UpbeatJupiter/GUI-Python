import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text= "Enter your name")
label2 = tk.Label(win, text="")
entry1 = ttk.Entry(win, width=30)

def click_handler():
    if len(entry1.get()) > 0 :
        label2.configure(text="Hello " + entry1.get())
        entry1.delete(0,"end")
    entry1.focus_set()


button1 = tk.Button(win, text="Send", command=click_handler)

label1.pack()
entry1.pack()
button1.pack()
label2.pack()



win.mainloop()