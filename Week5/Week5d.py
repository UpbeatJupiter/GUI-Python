import tkinter as tk
from tkinter import ttk

def click_event(event):
    if event.num == 1:
        button = "Left"
    elif event.num == 2:
        button = "Middle"
    else :
        button = "Right"

    message = button + " clicked to " + event.widget["text"]
    ttk.Label(win, text=message).pack()

def mouse_enter(event):
    event.widget.configure(text="Mouse entered.")

def mouse_move(event):
    win.title(f"{event.x}, {event.y}")

def mouse_leave(event):
    event.widget["text"]="Mouse left."

win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

btn1 = ttk.Button(win, text="Button 1")
btn2 = ttk.Button(win, text="Button 2")

btn1.pack(pady = (20,0))
btn2.pack(pady=20)

btn1.bind("<Button-1>", click_event)
btn2.bind("<Double-3>", click_event)
btn1.bind("<Enter>", mouse_enter)
btn1.bind("<Leave>", mouse_leave)
win.bind("<Motion>", mouse_move)

win.mainloop()