# GUI for listing database content (Treeview).

import tkinter as tk
from tkinter import ttk
import sqlite3


class W8d:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Week 8")
        self.win.geometry("450x200+710+290")
        self.create_widgets()
        self.list_grades()

    @staticmethod
    def get_connection():
        return sqlite3.connect("gradebook.db")

    def list_grades(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("select * from GradeBook")
        grades = cur.fetchall()
        for g in grades:
            # Populate the Treeview by adding values to the end of it.
            # self.tv.insert(parent="", index="end", values=(g[0], g[1], g[2], g[3]))
            self.tv.insert(parent="", index="end", values=g)
        conn.close()

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self.win, height=10, show="headings")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
        self.tv["selectmode"] = "browse"
        self.tv.pack(fill="both", expand=True)

        # Add headings for each column.
        self.tv.heading("id", text="ID", anchor="center")
        self.tv.heading("fname", text="First Name", anchor="center")
        self.tv.heading("lname", text="Last Name", anchor="center")
        self.tv.heading("grade", text="Grade", anchor="center")

        # Configure each column.
        self.tv.column("id", anchor="center", width=45, stretch="no")
        self.tv.column("fname", anchor="w", width=135)
        self.tv.column("lname", anchor="w", width=135)
        self.tv.column("grade", anchor="center", width=135)


app = W8d()
app.win.mainloop()
