# Part 3: Basics with Tkinter GUI in Python
# Working with Labels and organizing them

from tkinter import *

root = Tk()

l1 = Label(root,text='L1',bg='red',fg='white')
l1.pack()
l2 = Label(root,text='L2',bg='green',fg='black')
l2.pack(fill=X)
l3 = Label(root,text='L3',bg='white',fg='blue')
l3.pack(side=LEFT,fill=Y)

root.mainloop()
