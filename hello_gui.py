from tkinter import *

root = Tk()




# creating a label widget
msg = "My name is WDX"
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text=msg).grid(row=1, column=0)
e = Entry(root, width=50, borderwidth=5).grid(row=3, column=0)
def myClick():
    myLabel3 = Label(root, text=e.get()).grid(row=3, column=0)
myButton = Button(root, text='enter a string', state=ACTIVE, command=myClick, fg='blue').grid(row=2, column=0)




root.mainloop()
