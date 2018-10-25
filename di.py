from tkinter import *

import tkinter.messagebox as tm
import tkinter

top = tkinter.Tk()

def helloCallBack():
    tm.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
B.place(bordermode=OUTSIDE, anchor=SE,height=90, width=150)
top.mainloop()
