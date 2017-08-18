# Tkinter (Using Classes)

from tkinter import *


class MyButtons:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='Print',command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text='Quit',command=master.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Here's the message.")

root = Tk()
b = MyButtons(root)
root.mainloop()
