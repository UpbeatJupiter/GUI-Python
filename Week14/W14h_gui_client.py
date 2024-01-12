import tkinter as tk
from tkinter import ttk
from threading import Thread
import socket


def send_message():
    btn.configure(state="disabled")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 4017))
    msg = client.recv(1024).decode("utf-8")
    print(msg)
    client.send(bytes(entry.get(), "utf-8"))
    msg = client.recv(1024).decode("utf-8")
    response_label.configure(text=msg)
    client.close()
    btn.configure(state="normal")


def send_message_using_thread(event=None):
    message_sender_thread = Thread(target=send_message)
    message_sender_thread.start()


win = tk.Tk()
win.geometry("300x130+700+290")
win.resizable(False, False)
win.title("Simple GUI Client")

entry_label = ttk.Label(win, text="Enter the message to send:")
entry_label.pack(padx=5, pady=5)

entry = ttk.Entry(win, width=30)
entry.pack(padx=5, pady=5)
entry.bind("<Return>", send_message_using_thread)
entry.focus_set()

btn = ttk.Button(win, text="Send", command=send_message_using_thread)
btn.pack(padx=5, pady=5)

response_label = ttk.Label(win, text="")
response_label.pack(padx=5, pady=5)

win.mainloop()
