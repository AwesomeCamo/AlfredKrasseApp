from tkinter import *

root = Tk()
root.title('Alfred Krasse App')
root.iconbitmap("./recources/images/HomeIcon.ico")
root.geometry("400x700")
root['background'] = '#FFFEF6'

def my_click():
    myLabel.grid_forget() #vergisst den grid, kann aber wieder neu aufgerufen werden durch "myLabel.grid()"
    myButton.grid_forget()
    myLabel2.grid(row=0, column=0)
    myButton2.grid(row=1,column=0)
    return

def my_clickback():
    myLabel2.grid_forget()
    myButton2.grid_forget()
    myLabel.grid(row=0,column=0)
    myButton.grid(row=3, column=0)
    return

myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="For Dennis <3")
myButton = Button(root, text="click me", command=my_click)
myButton2 = Button(root, text="Click me to go back", command=my_clickback)




myLabel.grid(row=0, column=0)
#myLabel2.grid(row = 1, column = 0)
myButton.grid(row=3, column=0)
#myButton2.grid(row=4, column=0)

root.mainloop()