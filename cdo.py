from tkinter import *

gui= Tk()

text="Welcome to Attendance Managment System"



marquee = Text(gui, height=50, width=70)
marquee.pack()

i = 0

def command(x, i):
    marquee.insert("1.1", x)
    if i == len(text):
        i = 0
    else:
        i = i+1
    gui.after(100, lambda:command(text[i:i+1], i))

command(text[i:i+1], i)

gui.mainloop()

