from tkinter import *
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

seitenzähler = 0 #Seite wird gezählt und definiert
cluster = MongoClient("mongodb+srv://Dennis:MHhRui10mongodb@cluster0.aitqo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #Datenbankaufruf
db = cluster["Alfred-Krasse-App"] #Die Datenbank auslesen
collection1 = db["Lehrerkürzel"] #Einzelne Daten de Datenbank auslesen
collection2 = db["Unterricht"]#Einzelne Daten de Datenbank auslesen
collection3 = db["Ausfall"]#Einzelne Daten de Datenbank auslesen
root = Tk() #Fenster erstellen
root.title('Alfred Krasse App')                         #Name des Fensters
root.iconbitmap("./resources/images/HomeIcon.ico")      #Bild (icon oben links) laden
rootHeight = root.winfo_screenheight()                  #die Höhe des Fensters
rootWidth = root.winfo_screenwidth()                    #Die Breite des Fensters
root.geometry("%dx%d+0+0"%(rootWidth,rootHeight))        #Fenstergröße wird dem Display entsprechend angepasst
root['background'] = '#FFFEF6'                          #der Hintergrund

parent_navigation = Frame(root,width=rootWidth,height=rootHeight//4)    #Hauptframe erstellt für die 4 navigations Button (Hauptmenü,Schule,Persönliche Daten, Unterricht)
parent_navigation.grid()#Frame wird platziert

unterricht_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)#Frame für Unterricht Button erstellt
unterricht_frame_navigation.grid(row=0,column=0)#Frame wird platziert

schule_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)#Frame für Schule Button wurde erstellt
schule_frame_navigation.grid(row=0,column=1)#Frame wird platziert

persönliche_daten_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)#Frame für Persönliche Daten Button wurde erstellt
persönliche_daten_frame_navigation.grid(row=0,column=2)#Frame wird platziert

hauptmenü_frame_navigation = Frame(parent_navigation,width=rootWidth//4,height=rootHeight//4)#Frame für Hauptmenü Button wurde erstellt
hauptmenü_frame_navigation.grid(row=0,column=3)#Frame wird platziert

frame_parent_bottom = Frame(root,width=rootWidth,height=rootHeight//2+rootHeight//4)#Hauptframe für die Buttons unter der Navigation wurde erstellt
frame_parent_bottom.grid(row=1)#Frame wird platziert

frame_inhalt_event = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für Inhalt wurde erstellt
frame_inhalt_event.grid(row=1,column=1)#Frame wird platziert

frame_inhalt_ausfall = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für Inhalt Button erstellt
frame_inhalt_ausfall.grid(row=1,column=2)#Frame wird platziert

frame_inhalt_lehrerkürzel = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für Lehrerkürzel erstellt
frame_inhalt_lehrerkürzel.grid(row=1,column=1)#Frame wird platziert
frame_inhalt_lehrerkürzel.grid_forget()#Frame wird vergessen

frame_inhalt_lehrerkürzel_tabelle = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für die Tabelle in Lehrerkürzel erstellt
frame_inhalt_lehrerkürzel_tabelle.grid()#Frame wird platziert
frame_inhalt_lehrerkürzel_tabelle.grid_forget()#Frame wird vergessen

frame_inhalt_über_schule = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für über Schule Button wurde erstellt
frame_inhalt_über_schule.grid(row=1,column=2)#Frame wird platziert
frame_inhalt_über_schule.grid_forget()#Frame wird vergessen

frame_inhalt_über_schule_left = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für über Schule gespalten und links erstellt
frame_inhalt_über_schule_left.grid()#Frame wird platziert
frame_inhalt_über_schule_left.grid_forget()#Frame wird vergessen

frame_inhalt_über_schule_right = Frame(frame_parent_bottom,width=rootWidth//2,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame von über Schule rechts
frame_inhalt_über_schule_right.grid()#Frame wird platziert
frame_inhalt_über_schule_right.grid_forget()#Frame wird vergessen

frame_event_button = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für Event Button erstellt
frame_event_button.grid()#Frame wird platziert
frame_event_button.grid_forget()#Frame wird vergessen

frame_ausfall_button = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für Ausfall Button erstellt
frame_ausfall_button.grid()#Frame wird platziert
frame_ausfall_button.grid_forget()#Frame wird vergessen

frame_pers_daten = Frame(frame_parent_bottom,width=rootWidth,height=rootHeight//2+rootHeight//4,bg="#2d2d2d")#Frame für persönliche Daten erstellt
frame_pers_daten.grid()#Frame wird platziert
frame_pers_daten.grid_forget()#Frame wird vergessen

frame_grid = Frame(root)#Frame erstellt
frame_grid.grid()#Frame wird platziert
frame_grid.grid_forget()#Frame wird vergessen

class Information: #Klasse für Tabelle (über die Schule erstellt)
    def __init__(self,Name2,Position):
        self.Name2 = Name2
        self.Position = Position

def datenbank_ausgabe(anfang):#Datenbank ausgabe Funktion erstellt für Lehrerkürzel
    results = collection1.find({"$and":[{"_id":{"$lt":anfang+12}},{"_id":{"$gt":anfang-1}}]})#Das Auslesen pro Seite beträgt maximal 12 Namen
    i=1
    for result in results: #for Schleife um Tabelle zu erstellen
        label1 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Kürzel"], relief="solid", borderwidth="2", width=90, height=3, bg="#2d2d2d", fg="#e4bc1f")#spalte 1 in Tabelle
        label2 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Name"], relief="solid", borderwidth="2", width=90, height=3,bg="#2d2d2d", fg="#e4bc1f")#Spalte 2 in Tabelle
        label3 = Label(frame_inhalt_lehrerkürzel_tabelle, text=result["Email"], relief="solid", borderwidth="2", width=90, height=3,bg="#2d2d2d", fg="#e4bc1f")#Spalte 3 in Tabelle
        label1.grid(row=i, column=1, sticky=W)
        label2.grid(row=i, column=2, sticky=W)
        label3.grid(row=i, column=3, sticky=W)
        i+=1 # um die Reihe zu erweitern (tabelle zu erhalten)

def ausfall_vertretung(): #funktion per Buttondruck bei ausfall/vertretung
    forgetinhalt()#alles machen, was in forgetinhalt steht()
    frame_ausfall_button.grid()

    label_ausfall1 = Label(frame_ausfall_button,text=" Ausfallender Lehrer: ", relief="solid", borderwidth="2",  bg="#2d2d2d", fg="#e4bc1f")#Label erstellt mit Text
    label_ausfall1.config(font=("Monteserrat",18))#Schrift wurde verändert
    label_ausfall1.place(x=0,y=0,width=rootWidth//3,height=120)#platzierung von dem Label (Tabellen artig)

    label_ausfall_1 = Label(frame_ausfall_button, text=" Vertretung/Entfall: ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f") #der rest ist genau so wie oben beschrieben
    label_ausfall_1.config(font=("Monteserrat",18))
    label_ausfall_1.place(x=640, y=0, width=rootWidth // 3, height=120)

    label_ausfall__1 = Label(frame_ausfall_button, text=" Vertretender Lehrer: ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f")
    label_ausfall__1.config(font=("Monteserrat",18))
    label_ausfall__1.place(x=1280, y=0, width=rootWidth // 3, height=120)

    label_ausfall2 = Label(frame_ausfall_button, text=" Herr Vollstedt (MSS12) ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f")
    label_ausfall2.config(font=("Monteserrat", 16))
    label_ausfall2.place(x=0, y=120, width=rootWidth // 3, height=120)

    label_ausfall_2 = Label(frame_ausfall_button, text=" Entfällt ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f")
    label_ausfall_2.config(font=("Monteserrat", 16))
    label_ausfall_2.place(x=640, y=120, width=rootWidth // 3, height=120)

    label_ausfall__2 = Label(frame_ausfall_button, text=" / ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f")
    label_ausfall__2.config(font=("Monteserrat", 16))
    label_ausfall__2.place(x=1280, y=120, width=rootWidth // 3, height=120)

    label_ausfall3 = Label(frame_ausfall_button, text=" Herr Meißner (MSS12) ", relief="solid", borderwidth="2", bg="#2d2d2d",fg="#e4bc1f")
    label_ausfall3.config(font=("Monteserrat", 16))
    label_ausfall3.place(x=0, y=120*2, width=rootWidth // 3, height=120)

    label_ausfall_3 = Label(frame_ausfall_button, text=" Vertretung ", relief="solid", borderwidth="2", bg="#2d2d2d",fg="#e4bc1f")
    label_ausfall_3.config(font=("Monteserrat", 16))
    label_ausfall_3.place(x=640, y=120*2, width=rootWidth // 3, height=120)

    label_ausfall__3 = Label(frame_ausfall_button, text=" Herr Müller ", relief="solid", borderwidth="2", bg="#2d2d2d",fg="#e4bc1f")
    label_ausfall__3.config(font=("Monteserrat", 16))
    label_ausfall__3.place(x=1280, y=120*2, width=rootWidth // 3, height=120)

    label_ausfall3 = Label(frame_ausfall_button, text=" Frau Schäfer (MSS12) ", relief="solid", borderwidth="2",bg="#2d2d2d", fg="#e4bc1f")
    label_ausfall3.config(font=("Monteserrat", 16))
    label_ausfall3.place(x=0, y=120 * 3, width=rootWidth // 3, height=120)

    label_ausfall_3 = Label(frame_ausfall_button, text=" Entfällt ", relief="solid", borderwidth="2", bg="#2d2d2d",fg="#e4bc1f")
    label_ausfall_3.config(font=("Monteserrat", 16))
    label_ausfall_3.place(x=640, y=120 * 3, width=rootWidth // 3, height=120)

    label_ausfall__3 = Label(frame_ausfall_button, text=" / ", relief="solid", borderwidth="2", bg="#2d2d2d",fg="#e4bc1f")
    label_ausfall__3.config(font=("Monteserrat", 16))
    label_ausfall__3.place(x=1280, y=120 * 3, width=rootWidth // 3, height=120)

def event(): #Funktion (command) von Event erstellt
    forgetinhalt()
    frame_event_button.grid()

    label_Gurs = Label(frame_event_button, text=" Gurs 1940 - Ausstellung (KLI) ", relief="solid", borderwidth="2",  bg="#2d2d2d", fg="#e4bc1f") #das selbe gilt hier, wie bei def event():
    label_Gurs.config(font=("Monteserrat",16))
    label_Gurs.place(x=0,y=0,width=960,height=158)

    label_Gurs_datum = Label(frame_event_button, text=" 3.12.2021 - 20.1.2022 ", relief="solid", borderwidth="2",  bg="#2d2d2d", fg="#e4bc1f")
    label_Gurs_datum.config(font=("Monteserrat",16))
    label_Gurs_datum.place(x=960,y=0,width=960,height=158)

    label_Abitur = Label(frame_event_button, text=" MSS13 - Schriftliches - Abitur (SCE)  ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Abitur.config(font=("Monteserrat", 16))
    label_Abitur.place(x=0,y=158,width=960,height=158)

    label_Abitur_datum = Label(frame_event_button, text=" 5.1.2022 - 19.1.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Abitur_datum.config(font=("Monteserrat", 16))
    label_Abitur_datum.place(x=960,y=158,width=960,height=158)

    label_Berufsorientierung = Label(frame_event_button, text=" Berufsorientierung - Klassenstufe 9   ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Berufsorientierung.config(font=("Monteserrat", 16))
    label_Berufsorientierung.place(x=0,y=158*2,width=960,height=158)

    label_Berufsorientierung_datum = Label(frame_event_button, text=" 25.1.2022 - 26.1.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_Berufsorientierung_datum.config(font=("Monteserrat", 16))
    label_Berufsorientierung_datum.place(x=960,y=158*2,width=960,height=158)

    label_halbjahreszeugnis = Label(frame_event_button, text=" Ausgabe - Halbjahreszeugnis ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_halbjahreszeugnis.config(font=("Monteserrat", 16))
    label_halbjahreszeugnis.place(x=0,y=158*3,width=960,height=158)

    label_halbjahreszeugnis_datum = Label(frame_event_button, text=" 28.1.2022 ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_halbjahreszeugnis_datum.config(font=("Monteserrat", 16))
    label_halbjahreszeugnis_datum.place(x=960,y=158*3,width=960,height=158)

    label_winterferien = Label(frame_event_button, text=" Winterferien ", relief="solid",borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_winterferien.config(font=("Monteserrat", 16))
    label_winterferien.place(x=0,y=158*4,width=960,height=158)

    label_winterferien_datum = Label(frame_event_button, text=" 21.2.2022 - 25.2.2022 ", relief="solid", borderwidth="2", bg="#2d2d2d", fg="#e4bc1f")
    label_winterferien_datum.config(font=("Monteserrat", 16))
    label_winterferien_datum.place(x=960,y=158*4,width=960,height=158)

def add_seitenzähler(): #funktion zum Seiten zählen
    global seitenzähler #wurde globalisiert (überall aufrufbar)
    seitenzähler += 1 #Seite wird bei Knopfdruck +1


def sub_seitenzähler():
    global seitenzähler#wurde globalisiert(überall aufrufbar)
    if seitenzähler > 0:#wenn Seitenzahl größer als 0 ist,gilt das unten
        seitenzähler -= 1 #Seite wird bei Knopfdruck -1

def forget_for_lehrerkürzel():#Funktion nur für lehrerkürzel
    myEvent.place_forget() #Button wird vergessen
    myAusfall.place_forget()#Button wird vergessen
    frame_event_button.grid_forget()#Frame wird vergessen
    frame_ausfall_button.grid_forget()#Frame wird vergessen
    frame_event_button.grid_forget()#Frame wird vergessen
    myLehrerkürzel.place_forget()#Button wird vergessen
    frame_inhalt_über_schule_left.grid_forget()#Frame wird vergessen
    frame_inhalt_über_schule_right.grid_forget()#Frame wird vergessen
    myInformation.place_forget()#Button wird vergessen
    frame_grid.place_forget()#Button wird vergessen
    frame_inhalt_ausfall.grid_forget()#Frame wird vergessen
    frame_inhalt_event.grid_forget()#Frame wird vergessen
    frame_inhalt_über_schule.grid_forget()#Frame wird vergesen
    frame_inhalt_lehrerkürzel.grid_forget()#Frame wird vergessen
    buttonblack()#Funktion wird ausgeführt
    for child in frame_inhalt_lehrerkürzel.winfo_children():#in Lehrerkürzel werden alle Kinderframes vergessen und das solange, bis es keine mehr gibt
        child.place_forget()

    for child in frame_inhalt_über_schule.winfo_children():#in über_schule werden alle Kinderframes vergessen und das solange, bis es keine mehr gibt
        child.place_forget()

    for child in frame_inhalt_ausfall.winfo_children():#in ausfall  werden alle Kinderframes vergessen und das solange, bis es keine mehr gibt
        child.place_forget()

    for child in frame_inhalt_event.winfo_children():#in event  werden alle Kinderframes vergessen und das solange, bis es keine mehr gibt
        child.place_forget()

def forgetinhalt():#gilt das selbe wie bei forget_for_lehrerkürzel nur diesmal für alle Buttons/Funktionen außer Lehrerkürzel
    myEvent.place_forget()
    frame_event_button.grid_forget()
    frame_pers_daten.grid_forget()
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
    global seitenzähler #globalisiert (überall aufrufbar)
    seitenzähler = 0 #seite wird auf 0 gestellt

def buttonblack():#Funktin zum Knöpfe färben
    myButton1.config(bg="#2d2d2d")#Buttons werden gefärbt
    myButton2.config(bg="#2d2d2d")
    myButton3.config(bg="#2d2d2d")
    myButton4.config(bg="#2d2d2d")

def unterricht():                                       #Funktion erstellen für Button Unterricht
    forgetinhalt()
    myButton1.config(bg="#7f7f7f")           #Button wird grau,wenn aktiv

def hauptmenü():                #Funktion erstellt für Button Hauptmenü
    forgetinhalt()
    frame_inhalt_event.grid(row=1,column=1) #frame wird aufgerufen
    frame_inhalt_ausfall.grid(row=1,column=2)
    myEvent.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)#Button wird platziert
    myAusfall.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myButton4.config(bg="#7f7f7f") #Button wird grau

def schule():       #Funktion für Button Schule wird erstellt
    forgetinhalt()
    frame_inhalt_lehrerkürzel.grid(row=1,column=1)
    frame_inhalt_über_schule.grid(row=1,column=2)
    myLehrerkürzel.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myInformation.place(x=0,y=0,width=rootWidth//2,height=rootHeight//2+rootHeight//4)
    myButton2.config(bg="#7f7f7f")

def read_input_field1():
    global current_input1
    current_input1 = float(input_field1.get())

def read_input_field2():
    global current_input2
    current_input2 = float(input_field2.get())

def read_input_field3():
    global current_input3
    current_input3 = float(input_field3.get())

def read_input_field4():
    global current_input4
    current_input4 = float(input_field4.get())

def read_input_field5():
    global current_input5
    current_input5 = float(input_field5.get())

def graph_per_daten():
    read_input_field1()
    read_input_field2()
    read_input_field3()
    read_input_field4()
    read_input_field5()
    summe = sum([current_input1, current_input2, current_input3,current_input4,current_input5])
    anzahl = len([current_input1, current_input2, current_input3,current_input4,current_input5])
    wert = summe / anzahl
    x1 = 1
    y1 = wert
    x2 = [1,2,3,4,5]
    y2 = [current_input1, current_input2, current_input3,current_input4,current_input5]

    plt.bar(x2, y2, label="Noten Anzeige")
    plt.title("Noten Anzeige")
    plt.xlabel("Anzahl der Noten")
    plt.ylabel("Noten in MSS-Punkte")
    plt.tight_layout()
    plt.show()

    plt.bar(x1, y1, label="Noten Durchschnitt")
    plt.title("Noten Durchschnitt")
    plt.ylabel("Noten in MSS-Punkte (Durchschnitt)")
    plt.tight_layout()
    plt.show()



def persönliche_daten():
    forgetinhalt()
    myButton3.config(bg="#7f7f7f")
    frame_pers_daten.grid()
    input_field1.place(x=0, y=0, width=rootWidth // 2, height=140)
    input_field1.config(font=("Monteserrat", 16))
    input_field2.place(x=0, y=140, width=rootWidth // 2, height=140)
    input_field2.config(font=("Monteserrat", 16))
    input_field3.place(x=0, y=140 * 2, width=rootWidth // 2, height=140)
    input_field3.config(font=("Monteserrat", 16))
    input_field4.place(x=0, y=140 * 3, width=rootWidth // 2, height=140)
    input_field4.config(font=("Monteserrat", 16))
    input_field5.place(x=0, y=140 * 4, width=rootWidth // 2, height=140)
    input_field5.config(font=("Monteserrat", 16))
    graph_visualisieren.place(x=960, y=140*3)

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

input_field1 = Entry(frame_pers_daten,bg="#2d2d2d",fg="#e4bc1f")
input_field1.place(x=0,y=0,width=rootWidth//2,height=140)
input_field1.place_forget()

input_field2 = Entry(frame_pers_daten, bg="#2d2d2d", fg="#e4bc1f")
input_field2.place(x=0, y=140, width=rootWidth // 2, height=140)
input_field2.place_forget()

input_field3 = Entry(frame_pers_daten, bg="#2d2d2d", fg="#e4bc1f")
input_field3.place(x=0, y=140*2, width=rootWidth // 2, height=140)
input_field3.place_forget()

input_field4 = Entry(frame_pers_daten, bg="#2d2d2d", fg="#e4bc1f")
input_field4.place(x=0, y=140*3, width=rootWidth // 2, height=140)
input_field4.place_forget()

input_field5 = Entry(frame_pers_daten, bg="#2d2d2d", fg="#e4bc1f")
input_field5.place(x=0, y=140*4, width=rootWidth // 2, height=140)
input_field5.place_forget()

graph_visualisieren = Button(frame_pers_daten,bg="#2d2d2d", fg="#e4bc1f",text="Visualisiere deinen Graphen!",command=graph_per_daten,width=40,height=11)
graph_visualisieren.place(x=1000,y=140*3)
graph_visualisieren.config(font=("Monteserrat", 16))
graph_visualisieren.place_forget()

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
