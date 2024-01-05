import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.dialogs import Messagebox


def add_labels():
    list_size = len(labels)
    for i in range(20):
        labels.append(ttk.Label(label_container, text=f"Label {list_size + i + 1}"))
        labels[list_size + i].pack()


def remove_labels():
    for l in labels:
        l.destroy()
    labels.clear()
    # msg = Messagebox.ok(title="Remove Labels", message="All labels are removed from the container frame.")
    # msg = Messagebox.okcancel(title="Remove Labels", message="All labels are removed from the container frame.")
    msg = Messagebox.show_info(title="Remove Labels", message="All labels are removed from the container frame.")
    print(msg)


win = ttk.Window(themename="cosmo")
win.geometry("650x250+700+200")
win.title("SEN4017")

top_container = ttk.Frame(win)
top_container.pack(pady=10)

labels = []
btn1 = ttk.Button(top_container, text="Add Labels", command=add_labels)
btn1.grid(row=0, column=0, padx=(0, 10))
btn2 = ttk.Button(top_container, text="Remove Labels", command=remove_labels)
btn2.grid(row=0, column=1)

label_container = ScrolledFrame(win)
label_container.pack(fill="both", expand=True)

win.mainloop()
