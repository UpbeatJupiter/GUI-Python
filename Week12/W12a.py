import ttkbootstrap as ttk
from ttkbootstrap import Style


def switch_theme():
    if var4.get() == 1:
        Style().theme_use("cosmo")
    else:
        Style().theme_use("superhero")


def set_value(value):
    pb1["value"] = value
    lbl1["text"] = int(float(value))


win = ttk.Window(themename="superhero")
win.geometry("300x450+700+200")
win.title("SEN4017")

lbl1 = ttk.Label(win, text="Label", bootstyle="primary")
lbl1.pack(pady=(10, 0))

entry1 = ttk.Entry(win, bootstyle="primary", width="22")
entry1.pack(pady=(10, 0))

combo1 = ttk.Combobox(win, values=["Item 1", "Item 2", "Item 3"], bootstyle="primary", width=20)
combo1.pack(pady=(10, 0))

btn1 = ttk.Button(win, text="Button", bootstyle="success-outline")
btn1.pack(pady=(10, 0))

var1 = ttk.IntVar()
cb1 = ttk.Checkbutton(win, text="Checkbutton 1", variable=var1, onvalue=1, offvalue=0, bootstyle="primary")
cb1.pack(pady=(10, 0))

var2 = ttk.IntVar()
cb2 = ttk.Checkbutton(win, text="Checkbutton 2", variable=var2, onvalue=1, offvalue=0, bootstyle="info-toolbutton")
cb2.pack(pady=(10, 0))

var3 = ttk.IntVar()
cb3 = ttk.Checkbutton(win, text="Checkbutton 3", variable=var3, onvalue=1, offvalue=0, bootstyle="success-round-toggle")
cb3.pack(pady=(10, 0))

var4 = ttk.IntVar()
cb4 = ttk.Checkbutton(win, text="Switch Theme", variable=var4, onvalue=1, offvalue=0, bootstyle="warning-square-toggle",
                      command=switch_theme)
cb4.pack(pady=(10, 0))

pb1 = ttk.Progressbar(win, maximum=100, value=0, length=250, style="success-striped")
pb1.pack(pady=(10, 0))

sc1 = ttk.Scale(win, from_=0, to=100, length=250, style="primary", command=set_value)
sc1.pack(pady=(10, 0))

lf1 = ttk.Labelframe(win, text="Radio Button Group")
lf1.pack(fill="x", expand=True, padx=20, pady=20)

var5 = ttk.StringVar()
rb1 = ttk.Radiobutton(lf1, text="Item 1", value="Item 1", variable=var5, bootstyle="primary")
rb1.pack(padx=5, pady=5)

rb2 = ttk.Radiobutton(lf1, text="Item 2", value="Item 2", variable=var5, bootstyle="danger")
rb2.pack(padx=5, pady=5)

win.mainloop()
