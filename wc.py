from tkinter import *
root = Tk()
root.title("Xmas Message")

#command for the button
def test_com():
    #removing the button
    act_btn.grid_remove() 

#adding the textbox for the message
msg_box = Text(root, height = 1, width = 30)
msg_box.grid(row=0, column=0)

#adding the message
msg_box.insert(END, "Happy Xmas")

#changing the background to green
msg_box.config(background="green")


#changing the background to red
msg_box.config(background="red")

root.after(250, test_com)


#button for activating the command
act_btn = Button(root, text = "1", command = test_com)
act_btn.grid(row=0, column=0)
