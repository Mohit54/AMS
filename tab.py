from tkinter import *
from PIL import ImageTk, Image
import os
gui= Tk()
gui.geometry("1000x500")


b=Label(gui,text="ID").place(x=10, y=10)

c=Label(gui,text="1").place(x=10, y=60)


c=Label(gui,text="2").place(x=10, y=150)


c=Label(gui,text="3").place(x=10, y=250)


c=Label(gui,text="4").place(x=10, y=350)


b=Label(gui,text="Name").place(x=40, y=10)

c=Label(gui,text="John").place(x=40, y=60)


c=Label(gui,text="Mohit").place(x=40, y=150)


c=Label(gui,text="Jenny").place(x=40, y=250)


c=Label(gui,text="Sam").place(x=40, y=350)


b=Label(gui,text="Age").place(x=90, y=10)

c=Label(gui,text="27").place(x=90, y=60)


c=Label(gui,text="22").place(x=90, y=150)

c=Label(gui,text="25").place(x=90, y=250)


c=Label(gui,text="24").place(x=90, y=350)

b=Label(gui,text="Post").place(x=150, y=10)

c=Label(gui,text="CEO").place(x=150, y=60)

c=Label(gui,text="Engineer").place(x=150, y=150)

c=Label(gui,text="Admin").place(x=150, y=250)

c=Label(gui,text="Designer").place(x=150, y=350)


b=Label(gui,text="Employee_ID").place(x=200, y=10)

c=Label(gui,text="EMP_001").place(x=210, y=60)

c=Label(gui,text="EMP_054").place(x=210, y=150)

c=Label(gui,text="EMP_023").place(x=210, y=250)

c=Label(gui,text="EMP_012").place(x=210, y=350)


b=Label(gui,text="Gender").place(x=275, y=10)

c=Label(gui,text="Male").place(x=275, y=60)

c=Label(gui,text="Male").place(x=275, y=150)

c=Label(gui,text="Female").place(x=275, y=250)

c=Label(gui,text="Male").place(x=275, y=350)

b=Label(gui,text="Picture").place(x=340, y=10)



img = ImageTk.PhotoImage(Image.open("c.jpg"))
L1= Label(gui, image = img,width=76,height=95).place(x=340, y=40)
img1 = ImageTk.PhotoImage(Image.open("m.jpg"))
L2= Label(gui, image = img1,width=76,height=95).place(x=340, y=140)
img2 = ImageTk.PhotoImage(Image.open("j.jpg"))
L2= Label(gui, image = img2,width=76,height=95).place(x=340, y=240)
img3 = ImageTk.PhotoImage(Image.open("s.jpg"))
L2= Label(gui, image = img3,width=76,height=95).place(x=340, y=340)
gui.mainloop()
