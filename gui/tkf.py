import tkinter
import turtle

def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
### 菜单   
root = tkinter.Tk()
menu = tkinter.Menu(root)
submenu=tkinter.Menu(root)
submenu.add_command(label="Open")
submenu.add_command(label="Save")
menu.add_cascade(label="File",menu=submenu)
root.config(menu=menu)
###
label = tkinter.Label(root,text="你好")
label.pack()
button1=tkinter.Button(root,text="五角星")
button1.pack()
button1.bind('<Button-1>',wjx)
root.mainloop()
