from tkinter import *

master = Tk()

b = Label(master, text="Hello, world!")
b.pack()
w = Label(master, text="Rouge", fg="red")
w.pack()
w = Label(master, text="Helvetica", font=("Helvetica", 160))
w.pack()
w = Label(master, text="longtext", anchor=W, justify=RIGHT)
w.pack()

mainloop()
