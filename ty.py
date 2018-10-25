from tkinter import *
from PIL import ImageTk, Image
import os


img = ImageTk.PhotoImage(Image.open("AMS-Logo.jpg"))
bottom = Label(image = img,width=1100,height=440)



mainloop()
