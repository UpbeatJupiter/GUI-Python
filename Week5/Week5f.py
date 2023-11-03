import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_date_time():
    labels.append(ttk.Label(text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"),font=("Arial", 16)))
    labels[-1].pack(pady=(10,0))

def clear():
    for label in labels:
        label.destroy()
    labels.clear()

def show_context_menu(event):
    context_menu.tk_popup(x=event.x_root, y=event.y_root)


win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

labels = []

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date_time)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu)

win.mainloop()