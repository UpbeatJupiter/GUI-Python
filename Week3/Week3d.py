import tkinter as tk

win = tk.Tk()

win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")

win.columnconfigure(0, weight=2)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=2)
win.rowconfigure(2, weight=1)

label1 = tk.Label(win, text="Label 1", bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(win, text="Label 3", bg="green", fg="white")

label1.grid(row=0, column=0, sticky="nswe")
label2.grid(row=1, column=2, sticky="nswe")
label3.grid(row=2, column=1, sticky="nswe")

win.mainloop()
