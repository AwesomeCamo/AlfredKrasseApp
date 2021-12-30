
from tkinter import *
from pymongo import MongoClient

seitenzähler = 0
cluster = MongoClient("mongodb+srv://Dennis:MHhRui10mongodb@cluster0.aitqo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Alfred-Krasse-App"]
collection1 = db["Lehrerkürzel"]
collection2 = db["Unterricht"]
collection3 = db["Ausfall"]
root = Tk()
root.title('Alfred Krasse App')                         #titel name
root.iconbitmap("./resources/images/HomeIcon.ico")      #Bild (icon oben links)
rootHeight = root.winfo_screenheight()                        #die Höhe des Fensters
rootWidth = root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(rootWidth,rootHeight))
root['background'] = '#FFFEF6'                          #der Hintergrund
db = cluster["Alfred-Krasse-App"]
collection1 = db["Lehrerkürzel"]

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

class Information:
    def __init__(self,Name2,Position):
        self.Name2 = Name2
        self.Position = Position

def datenbank_ausgabe(anfang):
    results = collection1.find({"$and":[{"_id":{"$lt":anfang+14}},{"_id":{"$gt":anfang-1}}]})
    i=1
    for result in results:
        label1 = Label(frame_grid, text=result["Kürzel"], relief="solid", borderwidth="2", width=93, height=3, bg="#2d2d2d", fg="#e4bc1f")
        label2 = Label(frame_grid, text=result["Name"], relief="solid", borderwidth="2", width=93, height=3,bg="#2d2d2d", fg="#e4bc1f")
        label3 = Label(frame_grid, text=result["Email"], relief="solid", borderwidth="2", width=93, height=3,bg="#2d2d2d", fg="#e4bc1f")
        label1.grid(row=i, column=1, sticky=W)
        label2.grid(row=i, column=2, sticky=W)
        label3.grid(row=i, column=3, sticky=W)
        i+=1


def add_seitenzähler():
    global seitenzähler
    seitenzähler += 1


def sub_seitenzähler():
    global seitenzähler
    if seitenzähler > 0:
        seitenzähler -= 1

def forget_for_lehrerkürzel():
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myLehrerkürzel.pack_forget()
    myInformation.pack_forget()
    frame_grid.pack_forget()
    buttonblack()
    frame_info.pack_forget()
    frame_info2.pack_forget()

def forgetinhalt():
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myLehrerkürzel.pack_forget()
    myInformation.pack_forget()
    frame_grid.pack_forget()
    buttonblack()
    frame_info.pack_forget()
    frame_info2.pack_forget()
    global seitenzähler
    seitenzähler = 0

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

def lehrerkürzel(seite):
    forget_for_lehrerkürzel()
    myButton2.config(bg="#7f7f7f")
    frame_grid.pack()
    for child in frame_grid.winfo_children():
        child.destroy()
    i=0
    label1 = Label(frame_grid, text="Kürzel", relief="solid", borderwidth="2", width=93, height=3,
                   anchor=CENTER, bg="#2d2d2d", fg="#e4bc1f")
    label2 = Label(frame_grid, text="Name", relief="solid", borderwidth="2", width=93, height=3, anchor=CENTER,
                   bg="#2d2d2d", fg="#e4bc1f")
    label3 = Label(frame_grid, text="Email", relief="solid", borderwidth="2", width=93, height=3, anchor=CENTER,
                   bg="#2d2d2d", fg="#e4bc1f")
    label1.grid(row=i, column=1, sticky=W)
    label2.grid(row=i, column=2, sticky=W)
    label3.grid(row=i, column=3, sticky=W)

    datenbank_ausgabe(seite)

    button_next = Button(frame_grid, text="Next", command=lambda: [add_seitenzähler(), lehrerkürzel(seitenzähler*16)],relief="solid",borderwidth=1, bg="#2d2d2d",fg="#e4bc1f",width=93,height=7,anchor=CENTER)
    button_next.grid(row=16, column=3,sticky=W)

    button_back = Button(frame_grid,text="Back",command=lambda:[sub_seitenzähler(),lehrerkürzel(seitenzähler*16)],relief="solid",borderwidth=1,bg="#2d2d2d",fg="#e4bc1f",width=93,height=7,anchor=CENTER)
    button_back.grid(row=16, column=1,sticky=W)

    seite_anzahl = Label(frame_grid, text="Seite: " + " " + str(seitenzähler+1), width=93, height=7,borderwidth=2,bg="#2d2d2d", fg="#e4bc1f",anchor=CENTER)
    seite_anzahl.grid(row=16, column=2,sticky=W)

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

button_back = Button(frame_grid,text="Back",command=lambda:[sub_seitenzähler(),lehrerkürzel(seitenzähler*16)],bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
button_back.grid(row=16, column=1,sticky=W)
button_back.grid_forget()

button_next = Button(frame_grid, text="Next", command=lambda: [add_seitenzähler(), lehrerkürzel(seitenzähler*16)], bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
button_next.grid(row=16, column=3,sticky=W)
button_next.grid_forget()

myButton1 = Button(navigation, text="Unterricht", command=unterricht, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton1.pack(side = LEFT) #die anordnung

myButton2 = Button(navigation, text="Schule",command=schule, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton2.pack(side = LEFT)

myButton3 = Button(navigation, text="Persönliche Daten",command=persönliche_daten, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton3.pack(side = LEFT)    #die Anordnung

myButton4 = Button(navigation, text="Hauptmenü", command=hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=70, height=10)         #Hauptmenü Button wurde erstellt
myButton4.pack(side=LEFT)

myLehrerkürzel = Button(inhalt, text="Lehrerkürzel", command=lambda: lehrerkürzel(0) , bg="#2d2d2d", fg="#e4bc1f", width=140, height=rootHeight-10)
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
