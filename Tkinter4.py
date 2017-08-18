# Part 4: Basics with Tkinter GUI in Python
# Grid Layout

from tkinter import *

root = Tk()

l1 = Label(root,text='UserID')
l2 = Label(root,text='Password')
entry_1 = Entry(root)
entry_2 = Entry(root)

l1.grid(row=0,sticky=E) #Aligning to the right (East)
l2.grid(row=1,sticky=E)
entry_1.grid(column=1, row=0)
entry_2.grid(column=1, row=1)

cb = Checkbutton(root,text='Keep me logged in')
cb.grid(columnspan=2) #Merge and Center (2 columns)
root.mainloop()
