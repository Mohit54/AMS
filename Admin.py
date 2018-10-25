#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
gui = Tk()






gui.geometry("1000x600")

gui.title("Admin")
gui.configure(bg='white')



var=StringVar()
def show():
    print("Admin Login",E1.get())
    print("Employee Login",E2.get())
    var.set ("success")


background_image = ImageTk.PhotoImage(Image.open("wk2.jpg"))
background_label = Label(gui, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
##img1 = ImageTk.PhotoImage(Image.open("th.jpg"))
##L1= Label(gui, image = img1,width=100,height=100).grid(row=2,column=15,padx=10, pady=10)
L1=Label(gui, text = "Admin Panel",bg="white",fg="red" ,font=("Times New Roman", 30)).grid(row=0,column = 15,padx=10, pady=10)
L1=Label(gui, text = "Options",bg="white",fg="black" ,font=("Times New Roman", 20)).grid(row=1,column = 15,padx=10, pady=10)








B=Button(gui, text="1.Employee Details ",bg="light blue").grid(row=2,column=15,padx=10, pady=10)




L2=Label(gui,text="2.Attendance ").grid(row=3,column=15,padx=10, pady=10)
B=Button(gui,text="i).Mark Attendance",bg="light blue",command=show).grid(row=4,column=15,padx=10, pady=10)
B=Button(gui,text="ii).Overall Attendance",bg="light blue",command=show).grid(row=5,column=15,padx=10, pady=10)


B1=Button(gui,text="3.Salary Details",bg="light blue",command=show).grid(row=6,column=15,padx=10, pady=10)

B1=Button(gui,text="4.Calaculate Payroll",bg="light blue",command=show).grid(row=7,column=15,padx=10, pady=10)


gui.mainloop()

