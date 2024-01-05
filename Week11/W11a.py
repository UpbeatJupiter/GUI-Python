import customtkinter as ctk


def set_text(event):
    lbl1.configure(text=entry1.get())


def button_click():
    lbl1.configure(text=f"Checkbox is {cb1.get()}.")


def get_slider_value(value):
    pb1.set(value)


def set_appearance():
    if sw1.get() == 1:
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


ctk.set_appearance_mode("light")  # system, light, dark
# ctk.set_default_color_theme("green")  # blue, dark-blue, green

win = ctk.CTk()
win.geometry("300x450+700+200")
win.title("SEN4017")
frame1 = ctk.CTkFrame(win)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

lbl1 = ctk.CTkLabel(frame1, text="Label")
lbl1.pack(pady=(10, 0))

entry1 = ctk.CTkEntry(frame1, placeholder_text="You can type here.")
entry1.pack(pady=(10, 0))
entry1.bind("<KeyRelease>", set_text)

combo1 = ctk.CTkComboBox(frame1, values=["Item 1", "Item 2", "Item 3"])
combo1.pack(pady=(10, 0))

opt_menu1 = ctk.CTkOptionMenu(frame1, values=["Item 1", "Item 2", "Item 3"])
opt_menu1.pack(pady=(10, 0))

cb1 = ctk.CTkCheckBox(frame1, text="Checkbox", onvalue="checked", offvalue="unchecked")
cb1.pack(pady=(10, 0))

btn1 = ctk.CTkButton(frame1, text="Button", command=button_click)
btn1.pack(pady=(10, 0))

rb_value = ctk.IntVar(value=1)
rb1 = ctk.CTkRadioButton(frame1, text="Item 1", variable=rb_value, value=1)
rb2 = ctk.CTkRadioButton(frame1, text="Item 2", variable=rb_value, value=2)

rb1.pack(pady=(10, 0))
rb2.pack(pady=(10, 0))

pb1 = ctk.CTkProgressBar(frame1)
pb1.set(0.8)
pb1.pack(pady=(10, 0))

sldr1 = ctk.CTkSlider(frame1, from_=0, to=1, command=get_slider_value)
sldr1.set(0.8)
sldr1.pack(pady=(10, 0))

sw1_value = ctk.IntVar(value=1)
sw1 = ctk.CTkSwitch(frame1, variable=sw1_value, onvalue=1, offvalue=0,
                    text="Light mode", command=set_appearance)
sw1.pack(pady=(10, 0))

win.mainloop()
