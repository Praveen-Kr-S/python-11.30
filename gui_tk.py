import tkinter as tk

main = tk.Tk()
#set the size
main.geometry("1920x1080")
main.config(background="gray")
#Frame - wegiths
container = tk.Frame(main,bg="#fed9b7")
#place(),pack()
container.place(x=0,y=0,width=1920,height=1080)

rg = tk.Frame(container,bg="#e7c6ff")
lg = tk.Frame(container,bg="#fca311")
dg = tk.Frame(container,bg="#adc178")

for page in (rg,lg,dg):
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

rg.tkraise()
main.mainloop()