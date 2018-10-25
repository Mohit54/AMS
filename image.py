import tkinter as tk
from PIL import Image, ImageTk


master=tk()

def cr(self):
        self.image = Image.open("nfl.jpg")

        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, image=self.photo,width=1500,height=900)
        self.label.image = self.photo # keep a reference!
        self.label.grid(row=0,column=1)




mainloop()
