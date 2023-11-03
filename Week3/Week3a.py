import tkinter as tk

win = tk.Tk()

win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(win, text="Label 3", bg="green", fg="white")

label1.place(x = 0, y = 0) 
label2.place(x = 200, y = 230) 
label3.place(x = 20, y = 120) 

win.mainloop()