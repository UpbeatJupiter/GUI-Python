import tkinter as tk
from tkinter import ttk

def open_second_window():
    win2 = tk.Toplevel()
    win2.title("Second Window")
    win2.geometry("300x200")

    ttk.Label(win2, text="Second Window").pack(pady=(20,0))
    ttk.Button(win2, text="Close", command=win2.destroy).pack(pady=(20,0))

win = tk.Tk()
win.title("SEN4017 - Week 6")
win.iconbitmap("python.ico")
win.geometry("300x300")

btn1 = ttk.Button(win, text="Open Second Window", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20,0))
btn2.pack(pady=(20,0))

win.mainloop()