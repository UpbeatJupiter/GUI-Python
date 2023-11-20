import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+100+100")

notebook1 = ttk.Notebook(win)
notebook1.pack(pady=30)

tab1 = ttk.Frame(notebook1, width=200, height=200)
tab2 = ttk.Frame(notebook1, width=200, height=200)

tab1.pack()
tab2.pack()

notebook1.add(tab1, text="Tab 1")
notebook1.add(tab2, text="Tab 2")

scrolled_text1 = ScrolledText(tab1, width=20, wrap="word")
scrolled_text1.pack(fill="both")

label_frame1 = ttk.LabelFrame(tab2, text="Checkbox")
label_frame1.pack(padx=10, pady=10, fill="both")

def click_handler():
    label_frame1.configure(text="Checkbox - " + selected_value.get())

selected_value = tk.StringVar()
checkbox1 = ttk.Checkbutton(label_frame1,
                            text="I agree to the terms and conditions.",
                            onvalue="Agree", offvalue="Disagree",
                            variable=selected_value,
                            command=click_handler)

checkbox1.pack(pady=10)

win.mainloop()
