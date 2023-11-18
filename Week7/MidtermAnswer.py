import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


def calc_avg():
    midterm_score = float(entry1.get())
    final_score = float(entry2.get())
    avg = (midterm_score * 0.4) + (final_score * 0.6)
    msg.showinfo(title="Result", message=f"The average is {avg} out of 100.")


def entry2_return(event):
    calc_avg()


win = tk.Tk()
win.title("Midterm")
win.geometry("300x145")

lbl1 = ttk.Label(text="Midterm Score:")
lbl2 = ttk.Label(text="Final Score:")
entry1 = ttk.Entry(win, width=25)
entry2 = ttk.Entry(win, width=25)
btn = ttk.Button(text="Calculate", command=calc_avg)

lbl1.grid(row=0, column=0, padx=20, pady=20)
lbl2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

btn.grid(row=2, column=0, pady=20, columnspan=2, sticky="e")

entry2.bind("<Return>", entry2_return)

win.mainloop()