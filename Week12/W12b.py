from PIL import Image
import ttkbootstrap as ttk

Image.CUBIC = Image.BICUBIC  # Fix for ttk.Meter

win = ttk.Window(themename="cosmo")
win.geometry("300x450+700+200")
win.title("SEN4017")

de1 = ttk.DateEntry(win, firstweekday=0, bootstyle="primary")
de1.pack(pady=(10, 0))

me1 = ttk.Meter(win,
                metersize=180,
                amountused=25,
                metertype="semi",
                subtext="% Completed",
                stripethickness=0,
                interactive=True)
me1.pack(pady=(10, 0))

nb1 = ttk.Notebook(win, bootstyle="light")
nb1.pack(padx=20, pady=20, fill="both", expand="True")

tab1 = ttk.Frame(nb1)
tab2 = ttk.Frame(nb1)

nb1.add(tab1, text="Group 1")
nb1.add(tab2, text="Group 2")

ttk.Label(tab1, text="This is Tab 1.", bootstyle="info").pack(pady=20)
ttk.Label(tab2, text="This is Tab 2.", bootstyle="info").pack(pady=20)

win.mainloop()
