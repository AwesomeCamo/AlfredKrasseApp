from tkinter import *

root = Tk()
root.title('Alfred Krasse App')                         #titel name
root.iconbitmap("./resources/images/HomeIcon.ico")      #Bild (icon oben links)
root.geometry("1920x1080")                              #die größe der App
rootHeight = root.winfo_height()                        #die Höhe des Fensters
rootWidth = root.winfo_width()                          #die Breite des Fensters
root['background'] = '#FFFEF6' #der Hintergrund

navigation = Frame(root)
navigation.pack()

inhalt = Frame(root)
inhalt.pack()

frame_grid = Frame(inhalt)
frame_grid.pack()
frame_grid.pack_forget()

class person:
    def __init__(self,Kürzel,Name,EMail):
        self.Kürzel = Kürzel
        self.Name = Name
        self.EMail = EMail

def forgetinhalt():
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myLehrerkürzel.pack_forget()
    myInformation.pack_forget()
    frame_grid.pack_forget()

def unterricht():                                       #Funktion erstellen
    forgetinhalt()


def hauptmenü():
    forgetinhalt()
    myEvent.pack(side=LEFT)
    myAusfall.pack(side=LEFT)


def schule():
    forgetinhalt()
    myLehrerkürzel.pack(side=LEFT)
    myInformation.pack(side=LEFT)


def persönliche_daten():
    forgetinhalt()


def event():
    forgetinhalt()



def ausfall():
    forgetinhalt()



def lehrerkürzel():
    forgetinhalt()
    frame_grid.pack()
    i=0
    Headline = person("Kürzel","Name","E-Mail")
    Dennis = person("Frey","Dennis Frey","dede0ß3e21328^1@jfasgfiugasfs.com")
    Emely = person("LOOL","LECK MICH","emely.leckmich@gmail.com")
    data = [Headline,Dennis,Emely]
    for item in data:
        if i == 0:
            label1 = Label(frame_grid,text=item.Kürzel, relief="solid", borderwidth="2", width=30, anchor=CENTER)
            label2 = Label(frame_grid,text=item.Name, relief="solid", borderwidth="2", width=30, anchor=CENTER)
            label3 = Label(frame_grid,text=item.EMail, relief="solid", borderwidth="2", width=30, anchor=CENTER)
        else:
            label1 = Label(frame_grid,text=item.Kürzel,relief="solid",borderwidth="2",width=30,anchor=W)
            label2 = Label(frame_grid,text=item.Name,relief="solid",borderwidth="2",width=30,anchor=W)
            label3 =  Label(frame_grid,text=item.EMail,relief="solid",borderwidth="2",width=30,anchor=W)
        label1.grid(row=i, column=1,sticky=W,)
        label2.grid(row=i, column=2,sticky=W)
        label3.grid(row=i, column=3,sticky=W)
        i+=1

myButton1 = Button(navigation, text="Unterricht", command=unterricht, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton1.pack(side = LEFT) #die anordnung

myButton2 = Button(navigation, text="Schule",command=schule, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton2.pack(side = LEFT)

myButton3 = Button(navigation, text="Persönliche Daten",command=persönliche_daten, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton3.pack(side = LEFT)    #die Anordnung

myButton4 = Button(navigation, text="Hauptmenü", command=hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=70, height=10)         #Hauptmenü Button wurde erstellt
myButton4.pack(side=LEFT)

myLehrerkürzel = Button(inhalt, text="Lehrerkürzel", command=lehrerkürzel, bg="#2d2d2d", fg="#e4bc1f", width=140, height=rootHeight-10)
myLehrerkürzel.pack(side=LEFT)
myLehrerkürzel.pack_forget()

myInformation = Button(inhalt, text="Über die Schule", command="", bg="#2d2d2d", fg="#e4bc1f", width=140, height=rootHeight-10)
myInformation.pack(side=LEFT)
myInformation.pack_forget()

myEvent = Button(inhalt, text="Event",command=event, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)                             #Eventbutton wurde erstellt
myEvent.pack(side= LEFT)

myAusfall = Button(inhalt, text="Ausfall/Vertretung",command=ausfall, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)            #Ausfall/Vertretung Button wurde erstellt
myAusfall.pack(side= RIGHT)


root.mainloop()
