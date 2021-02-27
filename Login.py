from tkinter import *
from PIL import  Image,ImageTk
from tkinter import messagebox
import pymysql

root = Tk()
root.title("Login page")
root.geometry("1100x550+0+0")

img_login = ImageTk.PhotoImage(Image.open("Login_bg.jpg"))
login_bg_lbl = Label(root,image=img_login)
login_bg_lbl.place(x=-10,y=0)

Frame1 = Frame(root,bg='white',width=500,height=400)
Frame1.place(x=80,y=60)

Login_lbl = Label(Frame1,text="LOGIN FORM",fg='green',bg='white',font=('Times new roman',18,"bold"))
Login_lbl.place(x=10,y=10)

username_lbl = Label(Frame1,text='Username',fg='black',bg='white',font=('Times new roman',18,"bold"))
username_lbl.place(x=10,y=80)
username = StringVar()
username_entry = Entry(Frame1,fg='black',bg='white',font=('Times new roman',15),width=15,bd=3,textvariable=username)
username_entry.place(x=150,y=80)

password_lbl = Label(Frame1,text='Password',fg='black',bg='white',font=('Times new roman',18,"bold"))
password_lbl.place(x=10,y=150)
password = StringVar()
password_entry = Entry(Frame1,fg='black',bg='white',font=('Times new roman',15),width=15,bd=3,textvariable=password)
password_entry.place(x=150,y=150)

Login_button = Button(Frame1,text="Login",bg='white',fg='green',font=('Times new roman',15,"bold"),relief=FLAT)
Login_button.place(x=30,y=220)
Forget_button = Button(Frame1,text="Forgot Password?",bg='white',fg='green',font=('Times new roman',12),relief=FLAT)
Forget_button.place(x=180,y=220)
Register_button = Button(Frame1,text="No Account?Register Here.",bg='white',fg='green',font=('Times new roman',12),relief=FLAT)
Register_button.place(x=180,y=260)

root.mainloop()
