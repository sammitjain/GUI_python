# Part 5: Binding functions to Layouts

##from tkinter import *
##
##root = Tk()
##
##def printName():
##    print("Sammit Jain")
##
##b1 = Button(root,text='Show',command=printName) #Give it the function you want to call
##b1.pack()
##root.mainloop()

#Alternative method using bind

from tkinter import *

root = Tk()

def printName(event):
    print("Sammit Jain")

b1 = Button(root,text='Show') #Give it the function you want to call
b1.bind('<Button-1>',printName)
b1.pack()
root.mainloop()
