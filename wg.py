import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="th.jpeg")

w1 = tk.Label(root, image=logo).pack(side="right")


root.mainloop()
