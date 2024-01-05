import customtkinter as ctk


def sb_selection(value):
    textbox1.insert("end", f"{value} selected.\n")
    textbox1.see("end")


win = ctk.CTk()
win.geometry("300x450+700+200")
win.title("SEN4017")
frame1 = ctk.CTkFrame(win)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

textbox1 = ctk.CTkTextbox(frame1, wrap="none", width=240, height=80)
textbox1.pack(pady=(10, 0))

sb_value = ctk.StringVar(value="Option 3")
sb1 = ctk.CTkSegmentedButton(frame1,
                             values=["Option 1", "Option 2", "Option 3"],
                             variable=sb_value,
                             command=sb_selection)
sb1.pack(pady=(10, 0))

tv1 = ctk.CTkTabview(frame1, anchor="sw")
tv1.pack(padx=10, pady=10)

tab1 = tv1.add("Tab 1")
tab2 = tv1.add("Tab 2")
tv1.set("Tab 2")

lbl1 = ctk.CTkLabel(tab1, text="This is tab 1.")
lbl1.pack(pady=(30, 0))

lbl2 = ctk.CTkLabel(tab2, text="This is tab 2.")
lbl2.pack(pady=(30, 0))

btn1 = ctk.CTkButton(tab2, text="Exit", command=lambda: win.destroy())
btn1.pack(pady=(30, 0))

win.mainloop()
