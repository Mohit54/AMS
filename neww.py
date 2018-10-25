#!/usr/bin/python
import sys
import os
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox
top=Tk()

def helloCallBack():
    os.system('lf.py')

B=Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()
