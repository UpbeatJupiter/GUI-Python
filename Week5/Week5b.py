import tkinter as tk
from centerscreen import center_secreen_geometry

win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")


screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()


win.geometry(center_secreen_geometry(screen_width = win.winfo_screenwidth(),
                                     screen_height= win.winfo_screenheight(),
                                     window_width=300,
                                     window_height=300))

win.mainloop()