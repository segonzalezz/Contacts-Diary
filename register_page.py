import subprocess
from tkinter import *



window = Tk()

height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets\\image_1.png")
bg_image = Label(
    window,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#272A37"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="Contacts Diary",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText1.place(x=110, y=45)

# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#FFFFFF",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#272A37"
)
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#FFFFFF",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#272A37"
)
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="Login",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#272A37",
    bd=0,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command = lambda : open_login(),
)
switchLogin.place(x=230, y=185, width=50, height=35)

# ================ First Name Section ====================
firstName_image = PhotoImage(file="assets\\input_img.png")
firstName_image_Label = Label(
    bg_image,
    image=firstName_image,
    bg="#272A37"
)
firstName_image_Label.place(x=80, y=242)

firstName_text = Label(
    firstName_image_Label,
    text="First name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
firstName_text.place(x=25, y=0)

firstName_icon = PhotoImage(file="assets\\name_icon.png")
firstName_icon_Label = Label(
    firstName_image_Label,
    image=firstName_icon,
    bg="#3D404B"
)
firstName_icon_Label.place(x=159, y=15)

firstName_entry = Entry(
    firstName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
firstName_entry.place(x=8, y=17, width=140, height=27)


# ================ Last Name Section ====================
lastName_image = PhotoImage(file="assets\\input_img.png")
lastName_image_Label = Label(
    bg_image,
    image=lastName_image,
    bg="#272A37"
)
lastName_image_Label.place(x=293, y=242)

lastName_text = Label(
    lastName_image_Label,
    text="Last name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
lastName_text.place(x=25, y=0)

lastName_icon = PhotoImage(file="assets\\name_icon.png")
lastName_icon_Label = Label(
    lastName_image_Label,
    image=lastName_icon,
    bg="#3D404B"
)
lastName_icon_Label.place(x=159, y=15)

lastName_entry = Entry(
    lastName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
lastName_entry.place(x=8, y=17, width=140, height=27)

# ================ Username Section ====================
username_image = PhotoImage(file="assets\\input_img.png")
username_image_Label = Label(
    bg_image,
    image=username_image,
    bg="#272A37"
)
username_image_Label.place(x=80, y=311)

username_text = Label(
    username_image_Label,
    text="Username",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
username_text.place(x=25, y=0)

username_icon = PhotoImage(file="assets\\username-icon.png")
username_icon_Label = Label(
    username_image_Label,
    image=username_icon,
    bg="#3D404B"
)
username_icon_Label.place(x=159, y=15)

username_entry = Entry(
    username_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
username_entry.place(x=8, y=17, width=150, height=27)

# ================ Location Section ====================
location_image = PhotoImage(file="assets\\input_img.png")
location_image_Label = Label(
    bg_image,
    image=location_image,
    bg="#272A37"
)
location_image_Label.place(x=80, y=450)

location_text = Label(
    location_image_Label,
    text="Location",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
location_text.place(x=25, y=0)

location_icon = PhotoImage(file="assets\\location-icon.png")
location_icon_Label = Label(
    location_image_Label,
    image=location_icon,
    bg="#3D404B"
)
location_icon_Label.place(x=159, y=15)

location_entry = Entry(
    location_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
location_entry.place(x=8, y=17, width=140, height=27)

# ================ Phone Section ====================
phone_image = PhotoImage(file="assets\\input_img.png")
phone_image_Label = Label(
    bg_image,
    image=phone_image,
    bg="#272A37"
)
phone_image_Label.place(x=293, y=450)

phone_text = Label(
    phone_image_Label,
    text="Phone",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
phone_text.place(x=25, y=0)

phone_icon = PhotoImage(file="assets\\phone-icon.png")
phone_icon_Label = Label(
    phone_image_Label,
    image=phone_icon,
    bg="#3D404B"
)
phone_icon_Label.place(x=159, y=15)

phone_entry = Entry(
    phone_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
phone_entry.place(x=8, y=17, width=140, height=27)

# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets\\input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#272A37"
)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets\\pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=0,
    bg="#3D404B",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
)
passwordName_entry.place(x=8, y=17, width=140, height=27)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(
    file="assets\\button_1.png")
submit_button = Button(
    bg_image,
    image=submit_buttonImage,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
    command= lambda : create_user()
)
submit_button .place(x=130, y=520, width=333, height=65)

# ================ Header Text Down ====================
headerText_image_down = PhotoImage(file="assets\\headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_down,
    bg="#272A37"
)
headerText_image_label3.place(x=650, y=530)

headerText3 = Label(
    bg_image,
    text="Powered by Sen Gideons",
    fg="#FFFFFF",
    font=("yu gothic ui bold", 20 * -1),
    bg="#272A37"
)
headerText3.place(x=700, y=530)

def open_login():
    window.destroy()
    subprocess.run(["python","login_page.py"])

def create_user():
    from Controller.user_Controller import user_Controller
    controller = user_Controller()
    name = firstName_entry.get()
    lastName = lastName_entry.get()
    location = location_entry.get()
    phone =  phone_entry.get()
    username = username_entry.get()
    password = passwordName_entry.get()
    controller.create_user(name, lastName, location, phone, username, password)


window.resizable(False, False)
window.mainloop()

