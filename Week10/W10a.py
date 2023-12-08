# I18N
import tkinter as tk
from tkinter import ttk
import langpack

class W10a:
    def __init__(self):
        self.win = tk.Tk()
        self.i18n = langpack.I18N("en")
        self.win.geometry("330x165+710+290")
        self.win.title(self.i18n.title)
        self.win.iconbitmap("python.ico")
        self.win.resizable(False, False)

        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()

        self.create_widgets()
        self.txt_fname.focus_set()
        self.win.protocol("WM_DELETE_WINDOW", self.close_window)

    def update_values(self):
        pass

    def create_widgets(self):
        self.lbl_fname = ttk.Label(self.win, text=self.i18n.fname, width=10, anchor="center")
        self.lbl_fname.grid(column=0, row=0, padx=15, pady=15)

        self.lbl_lname = ttk.Label(self.win, text=self.i18n.lname, width=10, anchor="center")
        self.lbl_lname.grid(column=0, row=1, padx=15, pady=(0, 15))

        self.lbl_grade = ttk.Label(self.win, text=self.i18n.grade, width=10, anchor="center")
        self.lbl_grade.grid(column=0, row=2, padx=15, pady=(0, 15))

        self.txt_fname = ttk.Entry(self.win, textvariable=self.fname, width=35)
        self.txt_fname.grid(column=1, row=0, padx=(0, 15), pady=15)

        self.txt_lname = ttk.Entry(self.win, textvariable=self.lname, width=35)
        self.txt_lname.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        
        self.txt_grade = ttk.Entry(self.win, textvariable=self.grade, width=35)
        self.txt_grade.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.btn_update = ttk.Button(self.win, text=self.i18n.update, command=self.update_values)
        self.btn_update.grid(column=0, row=3, columnspan=2, pady=(0, 15))

    def close_window(self):
        self.win.destroy()


app = W10a()
app.win.mainloop()
