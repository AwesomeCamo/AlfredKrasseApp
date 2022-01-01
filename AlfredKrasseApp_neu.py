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

parent_navigation = Frame(root,width=rootWidth,height=rootHeight//4)
parent_navigation.grid()

unterricht_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)
unterricht_frame_navigation.grid(row=0,column=0)

schule_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)
schule_frame_navigation.grid(row=0,column=1)

persönliche_daten_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)
persönliche_daten_frame_navigation.grid(row=0,column=2)

hauptmenü_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)
hauptmenü_frame_navigation.grid(row=0,column=3)

frame_parent_bottom = Frame(root,width=rootWidth,height=rootHeight//2+rootHeight//4)
frame_parent_bottom.grid(row=1)

frame_inhalt_event = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_event.grid(row=1,column=1)

frame_inhalt_ausfall = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_ausfall.grid(row=1,column=2)

frame_inhalt_lehrerkürzel = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_lehrerkürzel.grid(row=1,column=1)
frame_inhalt_lehrerkürzel.grid_forget()

frame_inhalt_lehrerkürzel_tabelle = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_lehrerkürzel_tabelle.grid()
frame_inhalt_lehrerkürzel_tabelle.grid_forget()

frame_inhalt_über_schule = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_über_schule.grid(row=1,column=2)
frame_inhalt_über_schule.grid_forget()

frame_inhalt_über_schule_left = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_über_schule_left.grid(row=1,column=1)
frame_inhalt_über_schule_left.grid_forget()

frame_inhalt_über_schule_right = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_über_schule_right.grid(row=1,column=1)
frame_inhalt_über_schule_right.grid_forget()

frame_event_button = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_event_button.grid()
frame_event_button.grid_forget()

frame_inhalt_event_left = Frame(frame_event_button,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_event_left.grid(row=0,column=0)
frame_inhalt_event_left.grid_forget()

frame_inhalt_event_right = Frame(frame_event_button,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_inhalt_event_right.grid(row=0,column=1)
frame_inhalt_event_right.grid_forget()

frame_ausfall_button = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")
frame_ausfall_button.grid()
frame_ausfall_button.grid_forget()

frame_grid = Frame(root)
frame_grid.grid()
frame_grid.grid_forget()

class Information:
    def __init__(self,Name2,Position):
        self.Name2 = Name2
        self.Position = Position

def datenbank_ausgabe(anfang):
    results = collection1.find({"$and":[{"_id":{"$lt":anfang+12}},{"_id":{"$gt":anfang-1}}]})
    i=1
    for result in results:
        label1 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Kürzel"], relief="solid", borderwidth="2", width=90, height=3, bg="#2d2d2d", fg="#e4bc1f")
        label2 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Name"], relief="solid", borderwidth="2", width=90, height=3,bg="#2d2d2d", fg="#e4bc1f")
        label3 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Email"], relief="solid", borderwidth="2", width=90, height=3,bg="#2d2d2d", fg="#e4bc1f")
        label1.grid(row=i, column=1, sticky=W)
        label2.grid(row=i, column=2, sticky=W)
        label3.grid(row=i, column=3, sticky=W)
        i+=1

def ausfall_vertretung():
    forgetinhalt()
    frame_ausfall_button.grid()

def event():
    forgetinhalt()
    frame_event_button.grid()
    frame_inhalt_event_right.grid(column=1)
    frame_inhalt_event_left.grid(column=0)

    label_Gurs = Label(frame_inhalt_event_left, text=" Gurs 1940 - Ausstellung (KLI) ", relief="solid", borderwidth="2",  bg="#2d2d2d", fg="#e4bc1f")
    label_Gurs.config(font=("Monteserrat",16))
    label_Gurs.place(x=0,y=0,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_Gurs_datum = Label(frame_inhalt_event_right, text=" 3.12.2021 - 20.1.2022 ", relief="solid", borderwidth="2",  bg="#2d2d2d", fg="#e4bc1f")
    label_Gurs_datum.config(font=("Monteserrat",16))
    label_Gurs_datum.place(x=0,y=54,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_Abitur = Label(frame_inhalt_event_left, text=" MSS13 - Schriftliches - Abitur (SCE)  ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Abitur.config(font=("Monteserrat", 16))
    label_Abitur.place(x=0,y=54*2,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_Abitur_datum = Label(frame_inhalt_event_right, text=" 5.1.2022 - 19.1.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Abitur_datum.config(font=("Monteserrat", 16))
    label_Abitur_datum.place(x=0,y=54*2,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_Berufsorientierung = Label(frame_inhalt_event_left, text=" Berufsorientierung - Klassenstufe 9   ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Berufsorientierung.config(font=("Monteserrat", 16))
    label_Berufsorientierung.place(x=0,y=54*3,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_Berufsorientierung_datum = Label(frame_inhalt_event_right, text=" 25.1.2022 - 26.1.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Berufsorientierung_datum.config(font=("Monteserrat", 16))
    label_Berufsorientierung_datum.place(x=0,y=54*3,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_halbjahreszeugnis = Label(frame_inhalt_event_left, text=" Ausgabe - Halbjahreszeugnis ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_halbjahreszeugnis.config(font=("Monteserrat", 16))
    label_halbjahreszeugnis.place(x=0,y=54*4,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_halbjahreszeugnis_datum = Label(frame_inhalt_event_right, text=" 28.1.2022 ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_halbjahreszeugnis_datum.config(font=("Monteserrat", 16))
    label_halbjahreszeugnis_datum.place(x=0,y=54*4,width=rootWidth//2,height=(rootHeight-rootHeight//4)//5)

    label_winterferien = Label(frame_inhalt_event_left, text=" Winterferien ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_winterferien.config(font=("Monteserrat", 16))
    label_winterferien.place(x=0,y=54*5,width=rootWidth//2,height=170)

    label_winterferien_datum = Label(frame_inhalt_event_right, text=" 21.2.2022 - 25.2.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_winterferien_datum.config(font=("Monteserrat", 16))
    label_winterferien_datum.place(x=0,y=54*5,width=rootWidth//2,height=170)

def add_seitenzähler():
    global seitenzähler
    seitenzähler += 1


def sub_seitenzähler():
    global seitenzähler
    if seitenzähler > 0:
        seitenzähler -= 1

def forget_for_lehrerkürzel():
    myEvent.place_forget()
    frame_inhalt_event_right.grid_forget()
    frame_inhalt_event_left.grid_forget()
    myAusfall.place_forget()
    frame_event_button.grid_forget()
    frame_ausfall_button.grid_forget()
    frame_event_button.grid_forget()
    myLehrerkürzel.place_forget()
    frame_inhalt_über_schule_left.grid_forget()
    frame_inhalt_über_schule_right.grid_forget()
    myInformation.place_forget()
    frame_grid.place_forget()
    frame_inhalt_ausfall.grid_forget()
    frame_inhalt_event.grid_forget()
    frame_inhalt_über_schule.grid_forget()
    frame_inhalt_lehrerkürzel.grid_forget()
    buttonblack()
    for child in frame_inhalt_lehrerkürzel.winfo_children():
        child.place_forget()

    for child in frame_inhalt_über_schule.winfo_children():
        child.place_forget()

    for child in frame_inhalt_ausfall.winfo_children():
        child.place_forget()

    for child in frame_inhalt_event.winfo_children():
        child.place_forget()

def forgetinhalt():
    myEvent.place_forget()
    frame_event_button.grid_forget()
    frame_inhalt_event_right.grid_forget()
    frame_inhalt_event_left.grid_forget()
    frame_ausfall_button.grid_forget()
    frame_event_button.grid_forget()
    frame_inhalt_lehrerkürzel_tabelle.grid_forget()
    frame_inhalt_über_schule_left.grid_forget()
    frame_inhalt_über_schule_right.grid_forget()
    myAusfall.place_forget()
    myLehrerkürzel.place_forget()
    myInformation.place_forget()
    frame_grid.place_forget()
    for child in frame_inhalt_lehrerkürzel.winfo_children():
        child.place_forget()

    for child in frame_inhalt_über_schule.winfo_children():
        child.place_forget()

    for child in frame_inhalt_ausfall.winfo_children():
        child.place_forget()

    for child in frame_inhalt_event.winfo_children():
        child.place_forget()

    frame_inhalt_ausfall.grid_forget()
    frame_inhalt_event.grid_forget()
    frame_inhalt_über_schule.grid_forget()
    frame_inhalt_lehrerkürzel.grid_forget()
    buttonblack()
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
    frame_inhalt_event.grid(row=1,column=1)
    frame_inhalt_ausfall.grid(row=1,column=2)
    myEvent.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myAusfall.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myButton4.config(bg="#7f7f7f")

def schule():
    forgetinhalt()
    frame_inhalt_lehrerkürzel.grid(row=1,column=1)
    frame_inhalt_über_schule.grid(row=1,column=2)
    myLehrerkürzel.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myInformation.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myButton2.config(bg="#7f7f7f")

def persönliche_daten():
    forgetinhalt()
    myButton3.config(bg="#7f7f7f")

def lehrerkürzel(seite):
    forget_for_lehrerkürzel()
    myButton2.config(bg="#7f7f7f")
    frame_inhalt_lehrerkürzel_tabelle
    frame_inhalt_lehrerkürzel_tabelle.grid()
    for child in frame_inhalt_lehrerkürzel_tabelle.winfo_children():
        child.destroy()
    i=0
    label1 = Label(frame_inhalt_lehrerkürzel_tabelle, text="Kürzel", relief="solid", borderwidth="2", width=90, height=3,anchor=CENTER, bg="#2d2d2d", fg="#e4bc1f")
    label2 = Label(frame_inhalt_lehrerkürzel_tabelle, text="Name", relief="solid", borderwidth="2", width=90, height=3, anchor=CENTER,bg="#2d2d2d", fg="#e4bc1f")
    label3 = Label(frame_inhalt_lehrerkürzel_tabelle, text="Email", relief="solid", borderwidth="2", width=90, height=3, anchor=CENTER,bg="#2d2d2d", fg="#e4bc1f")

    label1.grid(row=i, column=1, sticky=W)
    label2.grid(row=i, column=2, sticky=W)
    label3.grid(row=i, column=3, sticky=W)

    datenbank_ausgabe(seite)

    button_next = Button(frame_inhalt_lehrerkürzel_tabelle, text="Next", command=lambda: [add_seitenzähler(), lehrerkürzel(seitenzähler*16)],relief="solid",borderwidth=1, bg="#2d2d2d",fg="#e4bc1f",width=90,height=7,anchor=CENTER)
    button_next.grid(row=16, column=3,sticky=W)

    button_back = Button(frame_inhalt_lehrerkürzel_tabelle,text="Back",command=lambda:[sub_seitenzähler(),lehrerkürzel(seitenzähler*16)],relief="solid",borderwidth=1,bg="#2d2d2d",fg="#e4bc1f",width=90,height=7,anchor=CENTER)
    button_back.grid(row=16, column=1,sticky=W)

    seite_anzahl = Label(frame_inhalt_lehrerkürzel_tabelle, text="Seite: " + " " + str(seitenzähler+1), width=90, height=7,borderwidth=2,bg="#2d2d2d", fg="#e4bc1f",anchor=CENTER)
    seite_anzahl.grid(row=16, column=2,sticky=W)

def über_die_Schule():
    forgetinhalt()
    frame_inhalt_über_schule_right.grid(row=1,column=2)
    frame_inhalt_über_schule_left.grid(row=1,column=1)
    myButton2.config(bg="#7f7f7f")
    x=0
    Headline = Information("Name", "Position")
    Allmann = Information("Pete Allmann","Schulleiter")
    Schwamm = Information("Anne Schwamm", "Ständige Stellvertreterin",)
    Mohr = Information("Christoph Mohr","Zweiter Stellvertreter")
    Klein = Information("Frau Klein","Sekretärin")
    Spada = Information("Frau Spada","Sekretärin")
    adress = Information("Lessingstraße 24, 76887 Bad Bergzabern","06343-9344-0")
    daten = [Headline,Allmann,Schwamm,Mohr,Klein,Spada,adress]
    for name in daten:
        if x == 0:
            label1 = Label(frame_inhalt_über_schule_left,text=name.Name2, relief="solid", borderwidth="2", anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label1.config(font=("Monteserrat", 18,"bold italic"))
            label2 = Label(frame_inhalt_über_schule_right,text=name.Position, relief="solid", borderwidth="2",  anchor=CENTER, bg="#2d2d2d",fg="#e4bc1f")
            label2.config(font=("Monteserrat", 18,"bold italic"))
        else:
            label1 = Label(frame_inhalt_über_schule_left, text=name.Name2, relief="solid", borderwidth="2", anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label1.config(font=("Monteserrat", 18))
            label2 = Label(frame_inhalt_über_schule_right, text=name.Position, relief="solid", borderwidth="2", anchor=W, bg="#2d2d2d",fg="#e4bc1f")
            label2.config(font=("Monteserrat", 18))

        label1.place(y=x*(rootHeight-rootHeight//4)//8-1,height=(rootHeight-rootHeight//4)//7,width=rootWidth//2)
        label2.place(y=x*(rootHeight-rootHeight//4)//8-1,height=(rootHeight-rootHeight//4)//7,width=rootWidth//2)
        x+=1


button_back = Button(frame_grid,text="Back",command=lambda:[sub_seitenzähler(),lehrerkürzel(seitenzähler*16)],bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
button_back.grid(row=16, column=1,sticky=W)
button_back.grid_forget()

button_next = Button(frame_grid, text="Next", command=lambda: [add_seitenzähler(), lehrerkürzel(seitenzähler*16)], bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
button_next.grid(row=16, column=3,sticky=W)
button_next.grid_forget()

myButton1 = Button(unterricht_frame_navigation, text="Unterricht", command=unterricht, bg="#2d2d2d",fg="#e4bc1f")
myButton1.place(x=0,y=0,width=rootWidth//4,height=rootHeight//4) #die anordnung
myButton1.config(font=("Monteserrat",20))

myButton2 = Button(schule_frame_navigation, text="Schule",command=schule, bg="#2d2d2d",fg="#e4bc1f",width=70,height=10)
myButton2.place(x=0,y=0,width=rootWidth//4,height=rootHeight//4)
myButton2.config(font=("Monteserrat",20))

myButton3 = Button(persönliche_daten_frame_navigation, text="Persönliche Daten",command=persönliche_daten, bg="#2d2d2d",fg="#e4bc1f")
myButton3.place(x=0,y=0,width=rootWidth//4,height=rootHeight//4)    #die Anordnung
myButton3.config(font=("Monteserrat",20))

myButton4 = Button(hauptmenü_frame_navigation, text="Hauptmenü", command=hauptmenü, bg="#2d2d2d", fg="#e4bc1f")         #Hauptmenü Button wurde erstellt
myButton4.place(x=0,y=0,width=rootWidth//4,height=rootHeight//4)
myButton4.config(font=("Monteserrat",20))

myLehrerkürzel = Button(frame_inhalt_lehrerkürzel, text="Lehrerkürzel", command=lambda: lehrerkürzel(0) , bg="#2d2d2d", fg="#e4bc1f")
myLehrerkürzel.place(x=0,y=0,width=rootWidth//2,height=65)
myLehrerkürzel.config(font=("Monteserrat",20))
myLehrerkürzel.place_forget()

myInformation = Button(frame_inhalt_über_schule, text="Über die Schule", command=über_die_Schule, bg="#2d2d2d", fg="#e4bc1f")
myInformation.place(x=0,y=0,width=rootWidth//2,height=65)
myInformation.config(font=("Monteserrat",20))
myInformation.place_forget()

myEvent = Button(frame_inhalt_event, text="Event",command=event, bg="#2d2d2d",fg="#e4bc1f")                             #Eventbutton wurde erstellt
myEvent.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
myEvent.config(font=("Monteserrat",20))

myAusfall = Button(frame_inhalt_ausfall, text="Ausfall/Vertretung",command=ausfall_vertretung, bg="#2d2d2d",fg="#e4bc1f")            #Ausfall/Vertretung Button wurde erstellt
myAusfall.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
myAusfall.config(font=("Monteserrat",20))

root.mainloop()
