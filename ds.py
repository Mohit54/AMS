
# !/usr/bin/python3
from tkinter import *
from tkinter import ttk
import PhotoImage
from PIL import ImageTk, Image
import os




photo = PhotoImage(file="th.jpg")
lb=tkinter.Label(root,image = photo)
lb.grid(row=4, column=1)
