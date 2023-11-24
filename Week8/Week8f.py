# GUI for listing database content (Treeview including Delete event).

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3


class W8d:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Week 8")
        self.win.geometry("450x200+710+290")
        self.create_widgets()
        self.bind_widgets()
        self.list_grades()

    @staticmethod
    def get_connection():
        return sqlite3.connect("gradebook.db")

    def item_select(self, event):
        # print(self.tv.selection())
        for i in self.tv.selection():
            print(self.tv.item(i)["values"])

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

    def show_average(self, event):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("select count(*), avg(grade) from GradeBook")
        result = cur.fetchone()
        msg_content = (f"Number of recorded grades: {str(result[0])}\n\n"
                       f"The average: {str(round(result[1], 1))}")
        msg.showinfo(title="Week 8", message=msg_content)
        conn.close()

    def delete_grade(self, event):
        answer = msg.askyesno(title="Confirm Delete", message="Are you sure you want to delete the selected row?")
        if answer:
            for i in self.tv.selection():
                selected_row = self.tv.item(i)["values"]
                conn = self.get_connection()
                cur = conn.cursor()
                cur.execute("delete from GradeBook where gid=?", [selected_row[0]])
                conn.commit()
                self.tv.delete(i)

    def create_widgets(self):
        # Create a Treeview widget.
        # selectmode: extended(default), browse, none
        self.tv = ttk.Treeview(self.win, height=10, show="headings", selectmode="browse")
        self.tv["columns"] = ("id", "fname", "lname", "grade")
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

        # Add a vertical scrollbar to the Treeview.
        self.tv_scroll = ttk.Scrollbar(self.win, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscrollcommand=self.tv_scroll.set)
        self.tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

    def bind_widgets(self):
        self.win.bind("<F1>", self.show_average)  # Show the average when the user presses F1.
        self.tv.bind("<<TreeviewSelect>>", self.item_select)  # Find the selected Treeview item.
        self.tv.bind("<Delete>", self.delete_grade)  # Delete the selected Treeview item.


app = W8d()
app.win.mainloop()
