import customtkinter as ctk
import CTkMessagebox as msg


def add_labels():
    list_size = len(labels)
    for i in range(20):
        labels.append(ctk.CTkLabel(frame1, text=f"Label {list_size + i + 1}"))
        labels[list_size+i].pack(pady=(10, 0))

    frame1.configure(label_text=f"List of Labels ({len(labels)})")


def remove_labels():
    for l in labels:
        l.destroy()
    labels.clear()
    frame1.configure(label_text="List of Labels")
    msg.CTkMessagebox(win, title="Remove Labels",
                      message="All labels are removed from the container frame.",
                      option_1="OK")


win = ctk.CTk()
win.geometry("300x450+700+200")
win.title("SEN4017")
frame1 = ctk.CTkScrollableFrame(win, label_text="List of Labels")
frame1.pack(pady=20, padx=20, fill="both", expand=True)

labels = []
btn1 = ctk.CTkButton(frame1, text="Add labels", command=add_labels)
btn2 = ctk.CTkButton(frame1, text="Remove labels", command=remove_labels)
btn1.pack(pady=(10, 0))
btn2.pack(pady=(10, 0))

win.mainloop()
