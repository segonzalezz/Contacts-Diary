from tkinter import *

win = Tk()
window_width = 350
window_height = 560
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
position_top = int(screen_height / 4 - window_height / 4)
position_right = int(screen_width / 2 - window_width / 2)
win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

win.title('Create contact')
win.configure(background='#272A37')
win.resizable(False, False)

# Name
name_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
name_entry.place(x=40, y=80, width=256, height=50)
name_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
name_label = Label(win, text='• Name', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=40, y=30)

# Lastname
lastname_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
lastname_entry.place(x=40, y=160, width=256, height=50)
lastname_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
lastname_label = Label(win, text='• Lastname', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
lastname_label.place(x=40, y=110)

# Location
location_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
location_entry.place(x=40, y=240, width=256, height=50)
location_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
location_label = Label(win, text='• Location', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
location_label.place(x=40, y=190)

# Number
number_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
number_entry.place(x=40, y=320, width=256, height=50)
number_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
number_label = Label(win, text='• Number', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
number_label.place(x=40, y=270)

# Email
email_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
email_entry.place(x=40, y=400, width=256, height=50)
email_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
email_label = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=40, y=350)

# Update Password Button
update_pass = Button(win, fg='#f8f8f8', text='Create', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                     cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5")
update_pass.place(x=40, y=470, width=256, height=45)

win.mainloop()

