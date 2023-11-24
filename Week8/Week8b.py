# GUI for inserting new records into database.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3


class W8b:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Week 8")
        self.win.geometry("330x165+710+290")
        self.win.resizable(False, False)
        self.fname = tk.StringVar()
        self.lname = tk.StringVar()
        self.grade = tk.IntVar()
        self.create_widgets()
        self.txt_fname.focus_set()

    @staticmethod
    def get_connection():
        return sqlite3.connect("gradebook.db")

    def save_grade(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("insert into GradeBook(fname, lname, grade) values(:first, :last, :grade)",
                    {"first": self.fname.get(),
                     "last": self.lname.get(),
                     "grade": self.grade.get()})
        conn.commit()
        conn.close()
        msg.showinfo("Done", "Grade saved.")
        self.clear_text_boxes()
        self.txt_fname.focus_set()

    def clear_text_boxes(self):
        self.txt_fname.delete(0, "end")
        self.txt_lname.delete(0, "end")
        self.txt_grade.delete(0, "end")

    def create_widgets(self):
        self.lbl_fname = ttk.Label(self.win, text="First Name")
        self.lbl_fname.grid(column=0, row=0, padx=15, pady=15)
        self.lbl_lname = ttk.Label(self.win, text="Last Name")
        self.lbl_lname.grid(column=0, row=1, padx=15, pady=(0, 15))
        self.lbl_grade = ttk.Label(self.win, text="Grade")
        self.lbl_grade.grid(column=0, row=2, padx=15, pady=(0, 15))

        self.txt_fname = ttk.Entry(self.win, textvariable=self.fname, width=35)
        self.txt_fname.grid(column=1, row=0, padx=(0, 15), pady=15)
        self.txt_lname = ttk.Entry(self.win, textvariable=self.lname, width=35)
        self.txt_lname.grid(column=1, row=1, padx=(0, 15), pady=(0, 15))
        self.txt_grade = ttk.Entry(self.win, textvariable=self.grade, width=35)
        self.txt_grade.grid(column=1, row=2, padx=(0, 15), pady=(0, 15))

        self.btn_save = ttk.Button(self.win, text="Save Grade", command=self.save_grade)
        self.btn_save.grid(column=0, row=3, columnspan=2, pady=(0, 15))


app = W8b()
app.win.mainloop()
