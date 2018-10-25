#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
        
    def initUI(self):
      
        self.master.title("Lines")        
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self,bg="cyan")
        canvas.create_line(500, 2500, 500, 500)
       
        canvas.pack(side = BOTTOM)


def main():
  
    root = Tk()
    ex = Example()
    root.geometry("1000x500")
    root.mainloop()  


if __name__ == '__main__':
    main()  
