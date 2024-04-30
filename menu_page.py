import tkinter as tk
from tkinter import ttk
import subprocess

def create_menu_page():
    root = tk.Tk()
    root.title("Menu")
    width = 1240
    height = 650
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.configure(bg="#525561")

    contacts_frame = tk.Frame(root, bg="#525561")
    contacts_frame.pack(pady=20)

    columns = ("Name", "LastName", "Location", "Number", "Email")
    contacts_table = ttk.Treeview(contacts_frame, columns=columns, show="headings")
    for col in columns:
        contacts_table.heading(col, text=col)
    contacts_table.pack()

    buttons_frame = tk.Frame(root, bg="#525561")
    buttons_frame.pack(pady=20)

    add_button = tk.Button(buttons_frame, text="Add", bg="#206DB4", fg="white", padx=10, pady=5, borderwidth=0, relief=tk.RIDGE, command= lambda : open_menu_page_create(root))
    add_button.grid(row=0, column=0, padx=10 )


    search_button =     tk.Button(buttons_frame, text="Search", bg="#206DB4", fg="white", padx=10, pady=5, borderwidth=0, relief=tk.RIDGE)
    search_button.grid(row=0, column=1, padx=10)

    update_button = tk.Button(buttons_frame, text="Update", bg="#206DB4", fg="white", padx=10, pady=5, borderwidth=0, relief=tk.RIDGE)
    update_button.grid(row=0, column=2, padx=10)

    delete_button = tk.Button(buttons_frame, text="Delete", bg="#206DB4", fg="white", padx=10, pady=5, borderwidth=0, relief=tk.RIDGE)
    delete_button.grid(row=0, column=3, padx=10)

    def open_menu_page_create():
        subprocess.run(["python", "menu_page_create.py"])


    root.mainloop()






