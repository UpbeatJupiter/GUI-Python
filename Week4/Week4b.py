import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
#win.iconbitmap("python.ico")

check_state = tk.BooleanVar()

def print_state():
    print(check_state.get())

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0)
file_menu.add_command(label="Open...")
file_menu.add_separator()

sub_menu = tk.Menu(file_menu, tearoff=False)
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")
file_menu.add_cascade(label="Editor", menu=sub_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.destroy)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False, variable=check_state, command=print_state)
help_menu.add_separator()
help_menu.add_command(label="About...")

menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu, underline=0)


win.mainloop()