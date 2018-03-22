from tkinter import *
import time
import datetime

def gettime():
    s=str(datetime.datetime.now()) + '\n'
    txt.insert(END,s)
    root.after(1000,gettime)

root =Tk()
root.geometry('320x240')
txt=Text(root)
txt.pack()
gettime()
root.mainloop()
