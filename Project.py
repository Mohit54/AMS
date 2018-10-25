# !/usr/bin/python3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os

gui = Tk()






gui.geometry("1200x700")

gui.title("Attendance Management System for Office")
gui.configure(bg='white')







var=StringVar()
def show():
    print("Admin Login",E1.get())
    print("Employee Login",E2.get())
    var.set ("success")

img = ImageTk.PhotoImage(Image.open("th.jpg"))
L1= Label(gui, image = img,width=479,height=351).grid(row=90, column=90,padx=20, pady=20)
L1=Label(gui,text="WC")
L1=Label(gui, text = "Admin",bg="pink").grid(row=0,column = 0,padx=20, pady=20)

a=StringVar()

E1=Entry(gui,bd = 5,textvariable=a).grid(row=0,column = 1,padx=20, pady=20)
a.set("Username")

b=StringVar()
E2=Entry(gui,bd = 5,textvariable=b).grid(row=0,column = 2,padx=20, pady=20)
b.set("Password")
B=Button(gui,text="Login",bg="white",command=show).grid(row=0,column = 3,padx=20, pady=20)
L4=Label(gui,textvariable=var)

L5=Label(gui, text = "Welcome to AMS!",bg="black",fg="white" ,font=("Times New Roman", 25)).grid(row=0,column = 6,padx=10, pady=10)
L2=Label(gui, text="Employee",bg="light blue").grid(row=2,column=0,padx=20, pady=20)

c=StringVar()
E2=Entry(gui,bd = 5,textvariable=c).grid(row=2,column=1,padx=10, pady=10)
c.set("Employee Name")
B=Button(gui,text="Login",bg="white",command=show).grid(row=2,column=2,padx=1, pady=1)



L5=Label(gui, text = "New Users Can Register Here!",bg="white").grid(row=4,column = 1,padx=30, pady=30)
B1=Button(gui,text="Register",bg="white",command=show).grid(row=5,column=1,padx=1, pady=1)
img = ImageTk.PhotoImage(Image.open("nfl.jpg"))
L1= Label(gui, image = img,width=479,height=351).grid(row=6, column=6,padx=20, pady=20)

gui.mainloop()

