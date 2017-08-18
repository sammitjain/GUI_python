# Mouse Click Events in Tkinter Python

from tkinter import *

root = Tk()

def leftclick(event):
    print("Event: Left Click")

def midclick(event):
    print("Event: Middle Click")
    
def rightclick(event):
    print("Event: Right Click")

frame = Frame(root,width=300,height=250)

frame.bind('<Button-1>',leftclick)
frame.bind('<Button-2>',midclick)
frame.bind('<Button-3>',rightclick)

frame.pack()

root.mainloop()
