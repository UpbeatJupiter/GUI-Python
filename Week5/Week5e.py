import tkinter as tk
from tkinter import ttk

def key_press(event):
    label1["text"] = event.keysym

def focus_gained(event):
    label1["text"] = "Focus gained"

def focus_lost(event):
    label1["text"] = "Focus lost"

def return_key(event):
    label1["text"] = entry1.get().upper()

win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

entry1 = ttk.Entry(win)
button1 = ttk.Button(win, text="Button 1")
label1 = ttk.Label(win, text="", font=("Consoloas", 16))

entry1.pack(pady=20)
button1.pack(pady=(0,20))
label1.pack()

entry1.bind("<KeyPress>", key_press)
entry1.bind("<FocusIn>", focus_gained)
entry1.bind("<FocusOut>", focus_lost)
entry1.bind("<Return>", return_key)

win.mainloop()