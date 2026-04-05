import tkinter as tk
from webbrowser import register
from tkinter import messagebox,ttk
from PIL import Image,ImageTk

import pymysql as sql

def rg_remove():
    rg_name.delete(0,"end")
    rg_phone.delete(0,"end")
    rg_email.delete(0,"end")
    rg_pass.delete(0,"end")

def lg_remove():
    lg_email.delete(0,"end")
    lg_pass.delete(0,"end")

def sp(pg):
    pg.tkraise()

def register():
    name,phone,email,password = rg_name.get(),rg_phone.get(),rg_email.get(),rg_pass.get()
    # print(name,email,phone,password)
    if not all([name,phone,email,password]):
        messagebox.showerror("Error","Please fill all fields")
        return None
    db = sql.connect(user="root",host="localhost",port=3306,db="praveen_tech",password="root")
    cur=db.cursor()
    cur.execute(""" insert into users(name,email,phone,password) values(%s,%s,%s,%s) """,(name,email,phone,password))
    db.commit()
    db.close()
    messagebox.showinfo("Register Successful","Register Successful")
    rg_remove()


def login():
    email, password = lg_email.get(), lg_pass.get()
    if not all([email,password]):
        messagebox.showerror("Error","Please fill all fields")
        return None
    db = sql.connect(user="root", host="localhost", port=3306, db="praveen_tech", password="root")
    cur = db.cursor()
    cur.execute(""" select * from users where email=%s and password=%s """,(email,password))
    # print(cur.fetchone())
    if cur.fetchone():
        lg_remove()
        messagebox.showinfo("Login Successful","Login Successful")
        dg.tkraise()
    else:
        messagebox.showerror("Error","Invaild User")
    db.commit()
    db.close()


main = tk.Tk()
#set the size
main.geometry("1920x1080")
main.config(background="gray")
#Frame - wegiths
container = tk.Frame(main,bg="#fed9b7")
#place(),pack()
container.place(x=0,y=0,width=1920,height=1080)

rg = tk.Frame(container,bg="#e7c6ff")
lg = tk.Frame(container,bg="#e7c6ff")
dg = tk.Frame(container,bg="#e7c6ff")
s25 = tk.Frame(container,bg="#e7c6ff")

for page in (rg,lg,dg,s25):
    page.place(x=0,y=0,width=1920,height=1080)

#Register Page
title = tk.Label(rg,text="Register Form",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",30))
title.place(x=600,y=100)
#user name
tk.Label(rg,text="User Name :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=200)
rg_name = tk.Entry(rg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20))
rg_name.place(x=680,y=200)
#user phone
tk.Label(rg,text="User Phone :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=260)
rg_phone = tk.Entry(rg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20))
rg_phone.place(x=680,y=260)

#user email
tk.Label(rg,text="User Email :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=320)
rg_email = tk.Entry(rg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20))
rg_email.place(x=680,y=320)

#user Password
tk.Label(rg,text="Password :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=380)
rg_pass = tk.Entry(rg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20),show="*")
rg_pass.place(x=680,y=380)

tk.Button(rg,text="Login Form",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),command=lambda:sp(lg)).place(x=550,y=450)
tk.Button(rg,text="Register",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),command=register).place(x=750,y=450)

#Login Page
title = tk.Label(lg,text="Login Form",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",30))
title.place(x=600,y=100)

#user email
tk.Label(lg,text="User Email :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=220)
lg_email = tk.Entry(lg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20))
lg_email.place(x=680,y=220)

#user Password
tk.Label(lg,text="Password :",bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20)).place(x=500,y=280)
lg_pass = tk.Entry(lg,bg="#e7c6ff",fg="#3e5c76",font=("Arial Bold",20),show="*")
lg_pass.place(x=680,y=280)

tk.Button(lg,text="Register Form",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),command=lambda:sp(rg)).place(x=550,y=350)
tk.Button(lg,text="Login",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),command=login).place(x=800,y=350)

#dasboard page

title = tk.Label(dg,text="Welcome to E-Kart",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",30))
title.place(x=600,y=100)

img = Image.open(r"C:\Users\prave\OneDrive\Pictures\sm25.jpg")
img = img.resize((200,200))
pic = ImageTk.PhotoImage(img)
tk.Label(dg,image=pic).place(x=200,y=200)
tk.Button(dg,image=pic,command=lambda:sp(s25)).place(x=500,y=200)
tk.Button(dg,text="Logout",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),command=lambda:sp(lg)).place(x=1350,y=50)

#text area
tk.Text(dg,bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",20),width=20,height=5).place(x=200,y=500)

#Combobox box
l=["India","China","Japan","France"]
ttk.Combobox(dg,values=l).place(x=600,y=500)

#Check box
ttk.Checkbutton(dg,text="Yes").place(x=800,y=500)
ttk.Checkbutton(dg,text="No").place(x=850,y=500)

#Radio Button
ttk.Radiobutton(dg,text="Yes").place(x=1000,y=500)
ttk.Radiobutton(dg,text="No").place(x=1050,y=500)

#s25 page
title = tk.Label(s25,text="Welcome to Samsung Mobiles",bg="#e7c6ff",fg="#219ebc",font=("Arial Bold",30))
title.place(x=600,y=100)

rg.tkraise()
main.mainloop()
