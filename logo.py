# !/usr/bin/python3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os


master = Tk()






canvas = Canvas(master, width=1500,height=900)
img = ImageTk.PhotoImage(Image.open("nfl.jpg"))
canvas.create_image(900,360, anchor=CENTER, image=img)
canvas.pack()
mainloop()
