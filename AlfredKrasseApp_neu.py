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

frame_info = Frame(inhalt)
frame_info.pack()
frame_info.pack_forget()

frame_info2 = Frame(inhalt)
frame_info2.pack()
frame_info2.pack_forget()

class Person:
    def __init__(self,Kürzel,Name,EMail):
        self.Kürzel = Kürzel
        self.Name = Name
        self.EMail = EMail

class Information:
    def __init__(self,Name2,Position):
        self.Name2 = Name2
        self.Position = Position

def forgetinhalt():
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myLehrerkürzel.pack_forget()
    myInformation.pack_forget()
    frame_grid.pack_forget()
    buttonblack()
    frame_info.pack_forget()
    frame_info2.pack_forget()

def buttonblack():
    myButton1.config(bg="#2d2d2d")
    myButton2.config(bg="#2d2d2d")
    myButton3.config(bg="#2d2d2d")
    myButton4.config(bg="#2d2d2d")

def unterricht():                                       #Funktion erstellen
    forgetinhalt()
    myButton1.config(bg="#7f7f7f")

def hauptmenü():
    forgetinhalt()
    myEvent.pack(side=LEFT)
    myAusfall.pack(side=LEFT)
    myButton4.config(bg="#7f7f7f")

def schule():
    forgetinhalt()
    myLehrerkürzel.pack(side=LEFT)
    myInformation.pack(side=LEFT)
    myButton2.config(bg="#7f7f7f")

def persönliche_daten():
    forgetinhalt()
    myButton3.config(bg="#7f7f7f")

def event():
    forgetinhalt()

def ausfall():
    forgetinhalt()

def lehrerkürzel():
    forgetinhalt()
    myButton2.config(bg="#7f7f7f")
    frame_grid.pack()
    i=0
    Headline = Person("Kürzel","Name","E-Mail")
    Dennis = Person("Frey","Dennis Frey","dede0ß3e21328^1@jfasgfiugasfs.com")
    Emely = Person("LOOL","LECK MICH","emely.leckmich@gmail.com")
    data = [Headline,Dennis,Emely]
    for item in data:
        if i == 0:
            label1 = Label(frame_grid,text=item.Kürzel, relief="solid", borderwidth="2", width=93,height=5, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label2 = Label(frame_grid,text=item.Name, relief="solid", borderwidth="2", width=93,height=5, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label3 = Label(frame_grid,text=item.EMail, relief="solid", borderwidth="2", width=93,height=5, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
        else:
            label1 = Label(frame_grid,text=item.Kürzel,relief="solid",borderwidth="2", width=93,height=5,anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label2 = Label(frame_grid,text=item.Name,relief="solid",borderwidth="2", width=93,height=5,anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label3 =  Label(frame_grid,text=item.EMail,relief="solid",borderwidth="2", width=93,height=5, bg="#2d2d2d",fg="#e4bc1f")
        label1.grid(row=i, column=1,sticky=W,)
        label2.grid(row=i, column=2,sticky=W)
        label3.grid(row=i, column=3,sticky=W)
        i+=1

def über_die_Schule():
    forgetinhalt()
    myButton2.config(bg="#7f7f7f")
    frame_info.pack()
    frame_info2.pack()
    x=0
    Headline = Information("Name", "Position")
    Allmann = Information("Pete Allmann","Schulleiter")
    Schwamm = Information("Anne Schwamm", "Ständige Stellvertreterin",)
    Mohr = Information("Christoph Mohr","Zweiter Stellvertreter")
    Klein = Information("Frau Klein","Sekretärin")
    Spada = Information("Frau Spada","Sekretärin")
    daten = [Headline,Allmann,Schwamm,Mohr,Klein,Spada]
    for name in daten:
        if x == 0:
            label1 = Label(frame_info,text=name.Name2, relief="solid", borderwidth="2", width=140,height=5, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label1.config(font=("Monteserrat", 9,"bold italic"))
            label2 = Label(frame_info,text=name.Position, relief="solid", borderwidth="2", width=140,height=5, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label2.config(font=("Monteserrat", 9,"bold italic"))
        else:
            label1 = Label(frame_info, text=name.Name2, relief="solid", borderwidth="2", width=140,height=5, anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label1.config(font=("Monteserrat", 9))
            label2 = Label(frame_info, text=name.Position, relief="solid", borderwidth="2", width=140,height=5, anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label2.config(font=("Monteserrat", 9))

        label1.grid(row=x, column=1, sticky=W)
        label2.grid(row=x, column=2, sticky=W)
        x+=1

    anschrift = Label(frame_info2,text="Lessingstraße 24, 76887 Bad Bergzabern", relief="solid", borderwidth="2",height=12, width=280, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
    anschrift.config(font=("Monteserrat", 9))
    telefon = Label(frame_info2,text="06343-9344-0", relief="solid", borderwidth="2", width=280,height=12, anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
    telefon.config(font=("Monteserrat", 9))

    anschrift.grid(row=x,column=1,sticky=W)
    telefon.grid(row=x+1,column=1,sticky=W)

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

myInformation = Button(inhalt, text="Über die Schule", command=über_die_Schule, bg="#2d2d2d", fg="#e4bc1f", width=140, height=rootHeight-10)
myInformation.pack(side=LEFT)
myInformation.pack_forget()

myEvent = Button(inhalt, text="Event",command=event, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)                             #Eventbutton wurde erstellt
myEvent.pack(side= LEFT)

myAusfall = Button(inhalt, text="Ausfall/Vertretung",command=ausfall, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)            #Ausfall/Vertretung Button wurde erstellt
myAusfall.pack(side= RIGHT)

root.mainloop()
