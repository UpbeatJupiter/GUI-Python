import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog as fd

win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap("python.ico")

check_state = tk.BooleanVar()

def print_state():
    print(check_state.get())

def exit_app():
    dialog_result = msg.askyesno(title="Exit", message="Are you sure you want to exit?")
    if dialog_result:
        win.destroy()


def open_file():
    file_filter = (
        ('All files', '*.*'),
        ('Text files', '*.txt'),
        ('PDF files', '*.pdf')
    )
    selected_file = fd.askopenfilename(filetypes=file_filter)
    ttk.Label(win, text=selected_file).pack()

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(label="New", accelerator="Ctrl+N", underline=0,
                      command=lambda: msg.showwarning(title="Warning", message="All unsaved progress will be lost!"))
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_separator()

sub_menu = tk.Menu(file_menu, tearoff=False)
sub_menu.add_command(label="Zoom in")
sub_menu.add_command(label="Zoom out")
file_menu.add_cascade(label="Editor", menu=sub_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

help_menu = tk.Menu(menubar, tearoff=False)
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False, variable=check_state, command=print_state)
help_menu.add_separator()
help_menu.add_command(label="About...", 
                      command=lambda:msg.showinfo(title="About",
                                                  message="SEN4017 - Introduction to GUI Programming \nFall2023"))


menubar.add_cascade(label="File", menu=file_menu, underline=0)
menubar.add_cascade(label="Help", menu=help_menu, underline=0)


win.mainloop()