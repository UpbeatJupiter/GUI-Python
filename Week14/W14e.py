# Embedding a plot into a tkinter window

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def draw_plot():
    x1_values = [0, 2, 3, 4]
    y1_values = [0, 1, 2, 4]
    x2_values = [0, 1, 4, 6]
    y2_values = [0, 1, 2, 1]

    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.grid(visible=True)
    ax.plot(x1_values, y1_values, linestyle="--", color="red")
    ax.plot(x2_values, y2_values, color="green")
    canvas.draw()


def clear_plot():
    ax.clear()
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.grid(visible=True)
    canvas.draw()


win = tk.Tk()
win.geometry("500x550+500+150")
win.title("Week 14")

fig = Figure(figsize=(5, 5))
ax = fig.add_subplot()
canvas = FigureCanvasTkAgg(master=win, figure=fig)
canvas.get_tk_widget().pack()

ttk.Button(win, text="Draw", command=draw_plot).pack(pady=10, side="right", expand=True)
ttk.Button(win, text="Clear", command=clear_plot).pack(pady=10, side="left", expand=True)

win.mainloop()
