# GUI freeze (fixed, threaded version)

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from time import sleep
from threading import Thread


def fill_text_using_thread():
    filler_thread = Thread(target=fill_text)
    filler_thread.start()


def fill_text():
    btn.configure(state="disabled")

    for i in range(1, 11):
        sleep(1)
        st.insert(index="end", chars=f"Step {i}\n")

    btn.configure(state="normal")


win = tk.Tk()
win.geometry("500x250+700+290")
win.title("Week 14")

st = scrolledtext.ScrolledText(win, width=20, height=10)
st.pack(expand=True, fill="both")

btn = ttk.Button(win, text="Fill text", command=fill_text_using_thread)
btn.pack(pady=5)

win.mainloop()
