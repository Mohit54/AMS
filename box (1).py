# !/usr/bin/python3
from tkinter import *

top = Tk()
var=StringVar()
def show():
    print("username",E1.get())
    print("password",E2.get())
    var.set ("success")


CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()
L1=Label(top, text = "User Name")
L1.pack(side = LEFT)
E1=Entry(top, bd = 5)
E1.pack()

L2=Label(top, text="Password")
L2.pack(side = LEFT)
L2.pack()

E2=Entry(top,bd = 5)
E2.pack()

B=Button(top,text="insert",command=show)
L3=Label(top,textvariable=var)
B.pack()
L3.pack()
