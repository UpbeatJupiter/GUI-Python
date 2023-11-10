import tkinter as tk
from tkinter import ttk

class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
       super().__init__()
       self.parent = parent
       self.title("SEN4017")
       self.geometry("300x300")
       self.iconbitmap("python.ico")
       self.lbl1 = None
       self.btn1 = None
       self.entry1 = None
       self.create_widgets()
       self.protocol("WM_DELETE_WINDOW", self.close_window)


    def create_widgets(self):
        self.lbl1 = ttk.Label(self, text="Second Window", font=("Calibri", 16))
        self.lbl1.pack(pady=(20,0))

        self.entry1 = ttk.Entry(self)
        self.entry1.pack(pady=(20,0))
        self.entry1.bind("<Return>", self.return_key)

        self.btn1 = ttk.Button(self, text="Close", command=self.close_window)
        self.btn1.pack(pady=(20,0))
    
    def return_key(self, event):
        self.parent.win.title(self.entry1.get())
        self.close_window()

    def close_window(self):
        print("Close Window")
        self.destroy()