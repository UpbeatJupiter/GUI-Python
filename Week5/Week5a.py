import tkinter as tk

win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")

win_width = 600
win_height = 400

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = int((screen_width / 2) - (win_width / 2))

y = int((screen_height / 2) - (win_height / 2))

win.geometry(f"{win_width}x{win_height}+{x}+{y}")

win.mainloop()