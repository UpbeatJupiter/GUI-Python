# GUI for listing database content (ScrolledText).

import tkinter as tk
from tkinter import scrolledtext
import sqlite3


class W8c:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Week 8")
        self.win.geometry("450x200+710+290")
        self.win.resizable(False, False)
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
        print(grades)
        grade_list = "ID\t\tName\t\tSurname\t\tGrade\n"
        for g in grades:
            grade_list += str(g[0]) + "\t\t"
            grade_list += g[1] + "\t\t"
            grade_list += g[2] + "\t\t"
            grade_list += str(g[3]) + "\n"
        conn.close()
        self.txt_content.insert("insert", grade_list)

    def create_widgets(self):
        self.txt_content = scrolledtext.ScrolledText(self.win)
        self.txt_content.pack()


app = W8c()
app.win.mainloop()
