from tkinter import *
from PIL import ImageTk, Image
import os
m1 = PanedWindow()
m1.pack(expand=1)
img = ImageTk.PhotoImage(Image.open("AMS-Logo.jpg"))
bottom = Label(m1, image = img,width=1100,height=440)
m1.add(bottom)


mainloop()
