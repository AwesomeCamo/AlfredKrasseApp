from tkinter import *

root = Tk()
root.title('Alfred Krasse App')
root.iconbitmap("./resources/images/HomeIcon.ico")
root.geometry("1920x1080")
rootHeight = root.winfo_height()
rootWidth = root.winfo_width()
root['background'] = '#FFFEF6'

def my_click():
    #myButton.place_forget()          #vergisst den grid, kann aber wieder neu aufgerufen werden durch "myButton.grid()"
    #myButton2.place(relx=0.5,rely=0.5,anchor=CENTER)
    return

def my_clickback():
    #myButton2.place_forget()
    #myButton.place(relx=0.5,rely=0.5,anchor=CENTER)
    return

#myButton1 = Button(root, text="Unterricht",command=my_click, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10 )
#myButton2 = Button(root, text="Hauptmenü",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10)
#myButton3 = Button(root, text="Schule",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10)
#myButton4 = Button(root, text="Persönliche Daten",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10)
#myButton5 = Button(root, text="Einstellungen",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10)
#myButton6 = Button(root, text="Hauptmenü",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=30,height=10)

#myButton.place(relx=0.25,rely=0.25,anchor=CENTER)
#myButton2.place(relx=0.5,rely=0.5,anchor=CENTER)
#myButton3.place(relx=0.5,rely=0.5,anchor=CENTER)
#myButton4.place(relx=0.75,rely=0.75,anchor=CENTER)
#myButton5.place(relx=0.5,rely=0.5,anchor=CENTER)
#myButton6.(relx=0.5,rely=0.5,anchor=CENTER)
#myButton2.place_forget()
#myButton6.place_forget()

frame = Frame(root)
frame.pack()

Topframe = Frame(root)
Topframe.pack(side = TOP)

myButton1 = Button(frame, text="Unterricht",command=my_click, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton1.pack(side = LEFT)

myButton2 = Button(frame, text="Schule",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton2.pack(side = LEFT)

myButton3 = Button(frame, text="Persönliche Daten",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton3.pack(side = LEFT)

myButton4 = Button(frame, text="Einstellungen",command=my_clickback, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton4.pack(side = LEFT)

Bottomframe = Frame(root)
Bottomframe.pack(side = BOTTOM)

myEvent = Label(text="Event", bg="#2d2d2d",fg="#e4bc1f",width=rootWidth //2,height=65)
myEvent.pack(side= LEFT)

myAusfall = Label(text="Ausfall/Vertretung", bg="#2d2d2d",fg="#e4bc1f",width=rootWidth //2,height=65)
myAusfall.pack(side= RIGHT)

root.mainloop()

