# Main window.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3
import dblib
import addnew
import gradelist


class MainWindow:
    def __init__(self):
        self.win = tk.Tk()
        self.window_title = "Week 9"
        self.win.geometry("250x210+710+290")
        self.win.title(self.window_title)
        self.win.iconbitmap("python.ico")
        self.win.resizable(False, False)
        self.db = dblib.GradeBookManager()
        self.create_widgets()

    def create_widgets(self):
        self.btn_create_database = ttk.Button(self.win, text="Create Database", width=30, command=self.create_db)
        self.btn_fill_database = ttk.Button(self.win, text="Fill Database", width=30, command=self.fill_db)
        self.btn_clear_database = ttk.Button(self.win, text="Clear Database", width=30, command=self.clear_db)
        self.btn_add_new = ttk.Button(self.win, text="Add New", width=30, command=self.show_add_new_window)
        self.btn_show_list = ttk.Button(self.win, text="Show List", width=30, command=self.show_grade_list_window)

        self.btn_create_database.pack(pady=(20, 0))
        self.btn_fill_database.pack(pady=(10, 0))
        self.btn_clear_database.pack(pady=(10, 0))
        self.btn_add_new.pack(pady=(10, 0))
        self.btn_show_list.pack(pady=(10, 0))

    def create_db(self):
        try:
            self.db.create_database()
            msg.showinfo(title=self.window_title, message="Database created.")
        except sqlite3.Error as err:
            msg.showerror(title=self.window_title, message="Failed to create the database.\n" + str(err))

    def fill_db(self):
        try:
            self.db.fill_database()
            msg.showinfo(title=self.window_title, message="Database populated.")
        except sqlite3.Error as err:
            msg.showerror(title=self.window_title, message="Failed to populate the database.\n" + str(err))

    def clear_db(self):
        try:
            self.db.clear_database()
            msg.showinfo(title=self.window_title, message="Database cleared.")
        except sqlite3.Error as err:
            msg.showerror(title=self.window_title, message="Failed to clear the database.\n" + str(err))

    def show_add_new_window(self):
        self.win.withdraw()
        self.add_new = addnew.AddNew(parent=self)
        self.add_new.grab_set()

    def show_grade_list_window(self):
        self.win.withdraw()
        self.grade_list = gradelist.GradeList(parent=self)
        self.grade_list.grab_set()


app = MainWindow()
app.win.mainloop()
