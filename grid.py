from tkinter import *

colours = ['red','green','orange','white','yellow','blue']
L1=Label(text="b", relief=RIDGE,width=150,height=4).grid(row=1,column=0)
r = 1
for c in colours:
    Entry(bg=c, relief=SUNKEN,width=15).grid(row=r,column=4)
    r = r + 1

mainloop()
