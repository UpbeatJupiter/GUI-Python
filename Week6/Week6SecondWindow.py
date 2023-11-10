import tkinter as tk
from tkinter import ttk

class SecondWindow(tk.Toplevel):
    def __init__(self):
       super().__init__()
       self.title("SEN4017")
       self.geometry("300x300")
       self.iconbitmap("python.ico")
       self.lbl1 = None
       self.btn1 = None
       self.entry1 = None
       self.create_widgets()


    def create_widgets(self):
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Calibri", 16))
        self.lbl1.pack(pady=(20,0))

        self.entry1 = ttk.Entry(self)
        self.entry1.pack(pady=(20,0))

        self.btn1 = ttk.Button(self, text="Close", command=self.win.destroy)
        self.btn1.pack(pady=(20,0))
