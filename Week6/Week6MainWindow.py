import tkinter as tk
from tkinter import ttk
import Week6SecondWindow

class MainWindow:
    def __init__(self):
       self.win = tk.Tk()
       self.win.title("SEN4017")
       self.win.geometry("300x300")
       self.win.iconbitmap("python.ico")
       self.win2 = None
       self.lbl1 = None
       self.btn1 = None
       self.btn2 = None
       self.create_widgets()


    def create_widgets(self):
        self.lbl1 = ttk.Label(self.win, text="Main Window", font=("Calibri", 16))
        self.lbl1.pack(pady=(20,0))

        self.btn1 = ttk.Button(self.win, text="Open Second Window", command=self.open_new_window)
        self.btn1.pack(pady=(20,0))

        self.btn2 = ttk.Button(self.win, text="Close", command=self.win.destroy)
        self.btn2.pack(pady=(20,0))

    def open_new_window(self):
        self.win2 = Week6SecondWindow.SecondWindow()

app = MainWindow()
app.win.mainloop()