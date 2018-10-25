
# !/usr/bin/python3
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(1000,900)
root.geometry("1500x900")
img = ImageTk.PhotoImage(Image.open("AMS-Logo.jpg"))

L1= Label(root, image = img,width=1100,height=440)
L1.pack()


root.mainloop()
