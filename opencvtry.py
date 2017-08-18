# Tkinter (Using Classes)

import cv2
import numpy as np
from tkinter import *


class MyButtons:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text='Print',command=self.showGrayscale)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text='Quit',command=master.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Here's the message.")
    def showGrayscale(self):
        testImg = cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
        cv2.imshow('Original',testImg)

root = Tk()
b = MyButtons(root)
##testImg = cv2.imread('messi.jpg')
##cv2.imshow('Original',testImg)
root.mainloop()
