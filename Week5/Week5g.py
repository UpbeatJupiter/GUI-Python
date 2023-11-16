import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_date_time():
    labels.append(ttk.Label(content,text=datetime.now().strftime("%d.%m.%Y - %H:%M:%S"),font=("Arial", 16)))
    labels[-1].pack(pady=(10,0))
    canvas.update()
    configure_canvas()
    
def clear():
    for label in labels:
        label.destroy()
    labels.clear()

def show_context_menu(event):
    context_menu.tk_popup(x=event.x_root, y=event.y_root)

def configure_canvas():
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfigure("content_window", width=canvas.winfo_width())

def configure_canvas_menu(event):
    configure_canvas()

win = tk.Tk()
win.title("SEN4017")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

labels = []

#Main container frame (canvas + scrollbar)
container = tk.Frame(win)
container.pack(fill="both", expand=True)

#Container with scrollbar support
canvas = tk.Canvas(container)
canvas.pack(fill="both",expand=True)

#Scrollbar
sb = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
sb.place(relx=1, rely=0, relheight=1, anchor="ne")

#Link our canvas to scrollbar
canvas.configure(yscrollcommand=sb.set)

#The actual container frame that keeps the widgets
content = tk.Frame(canvas)
content.pack(fill="both", expand=True)

#Place the content frame into canvas
canvas.create_window((0, 0), window=content, anchor="ne", tags="content_window")
canvas.bind("<Configure>", configure_canvas_menu)

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date_time)
context_menu.add_command(label="Clear", command=clear)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu)

win.mainloop()