from tkinter import *

def change_color():
    current_color = text.cget("background")
    next_color = "green" if current_color == "red" else "red"
    text.config(background=next_color)
    root.after(1000, change_color)

root = Tk()
L1=Label(root, text = "Admin",bg="pink").grid(row=0,column = 0,padx=20, pady=20)
text = Text(root, background="green").grid(row=1,column = 0,padx=20, pady=20)

change_color()
root.mainloop()
