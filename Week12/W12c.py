import ttkbootstrap as ttk
import W12data

win = ttk.Window(themename="cosmo")
win.geometry("650x250+700+200")
win.title("SEN4017")

tv = ttk.Treeview(win, show="headings", bootstyle="primary", height=30)
tv["columns"] = ("id", "prod_name", "prod_price")
tv.pack(fill="both", expand=True, padx=(10, 20), pady=10)

tv.heading("id", text="Product Code", anchor="center")
tv.heading("prod_name", text="Name", anchor="center")
tv.heading("prod_price", text="Price", anchor="center")

tv_scroll = ttk.Scrollbar(win, orient="vertical", command=tv.yview)
tv.configure(yscrollcommand=tv_scroll.set)
tv_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

for product in W12data.products:
    tv.insert(parent="", index="end", values=product)

win.mainloop()
