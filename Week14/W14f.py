# GUI freeze

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from time import sleep


def fill_text():
    for i in range(1, 11):
        sleep(1)
        st.insert(index="end", chars=f"Step {i}\n")


win = tk.Tk()
win.geometry("500x250+700+290")
win.title("Week 14")

st = scrolledtext.ScrolledText(win, width=20, height=10)
st.pack(expand=True, fill="both")

btn = ttk.Button(win, text="Fill text", command=fill_text)
btn.pack(pady=5)

win.mainloop()
