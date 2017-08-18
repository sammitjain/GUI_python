### Mouse Click Events in Tkinter Python
##
##from tkinter import *
##
##root = Tk()
##
##h_lower = Scale(root,orient=HORIZONTAL,length=300,sliderlength=30,from_=0,to=255,tickinterval=50).pack()
##print(h_lower.get())
##
##root.mainloop()

from tkinter import *

def show_values():
    print (h_l.get(), h_u.get())

master = Tk()
h_l = Scale(master, from_=0, to=255, orient=HORIZONTAL)
h_l.pack()
h_u = Scale(master, from_=0, to=255, orient=HORIZONTAL)
h_u.pack()
#Button(master, text='Show', command=show_values).pack()
show_values()
mainloop()
