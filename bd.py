from tkinter import *

master = Tk()
master.geometry("1500x800")
Label(text="one").pack()

separator = Frame(width=200,height=300, bd=5)
Label(text="one").pack()
Label(text="one").pack()
L1=Label(master,text="two")
separator.pack(fill=X, padx=5, pady=5)

L1.pack()
mainloop()
