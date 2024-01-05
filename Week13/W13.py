import tkinter as tk
from tkinter import ttk


def add_new(event):
    pass


def import_data():
    pass


def export_data():
    pass


win = tk.Tk()
win.geometry("420x200+700+200")
win.title("SEN4017 - Week 13")
win.resizable(False, False)

top_container = tk.Frame(win)
bottom_container = tk.Frame(win)
top_container.pack(fill="both", expand=True)
bottom_container.pack(fill="both", expand=True)

tv = ttk.Treeview(top_container, show="headings", height=5)
tv["columns"] = ("fname", "lname", "grade")
tv.pack(fill="both", expand=True, padx=(10, 25), pady=15)

tv.heading("fname", text="First Name", anchor="center")
tv.heading("lname", text="Last Name", anchor="center")
tv.heading("grade", text="Grade", anchor="center")

tv.column("fname", anchor="center", width=150)
tv.column("lname", anchor="center", width=150)
tv.column("grade", anchor="center", width=70)

tv_scroll = ttk.Scrollbar(top_container, orient="vertical", command=tv.yview)
tv.configure(yscrollcommand=tv_scroll.set)
tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

txt_fname = ttk.Entry(bottom_container, width=24)
txt_lname = ttk.Entry(bottom_container, width=24)
txt_grade = ttk.Entry(bottom_container, width=10)

txt_fname.grid(row=0, column=0, padx=10)
txt_lname.grid(row=0, column=1)
txt_grade.grid(row=0, column=2, padx=10)

txt_grade.bind("<Return>", add_new)

menubar = tk.Menu(win)
win.configure(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Import Data...", command=import_data)
file_menu.add_command(label="Export Data", command=export_data)
menubar.add_cascade(label="File", menu=file_menu)

win.mainloop()
