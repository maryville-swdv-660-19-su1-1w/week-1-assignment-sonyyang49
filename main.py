
# By Sony Yang

import random
import tkinter

window = tkinter.Tk()

# to rename the title of the window window.title("GUI")
window.title("Dice Roller")
window.geometry('400x150')

# pack is used to show the object in the window

title = tkinter.Label(window, text = "To start, please click the roll button.", font = ("Arial Bold", 15))
title.grid(column = 0, row = 0)

dice_num = tkinter.Label(window, text = "", font = ("Arial Bold", 30))
dice_num.grid(column = 0, row = 2)

def clicked():
    dice = random.randint(1,6)
    dice_num.configure(text = dice)

def exit():
    window.destroy()

rollbtn = tkinter.Button (window, text="Roll", bg="lightblue", fg="black", command = clicked)
rollbtn.grid(column = 0, row = 1)

exitbtn = tkinter.Button (window, text="Exit", bg="red", fg="white", command = exit)
exitbtn.grid(column = 0, row = 3)

window.mainloop()
