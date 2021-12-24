from tkinter import *

root = Tk()
root.title('Alfred Krasse App')                         #titel name
root.iconbitmap("./resources/images/HomeIcon.ico")      #Bild (icon oben links)
root.geometry("1920x1080")                              #die größe der App
rootHeight = root.winfo_height()                        #die Höhe des Fensters
rootWidth = root.winfo_width()                          #die Breite des Fensters
root['background'] = '#FFFEF6'                          #der Hintergrund

def unterricht():                                       #Funktion erstellen
    myButton1.pack_forget()                             #vergisst den grid, kann aber wieder neu aufgerufen werden durch "myButton.pack()"
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)                           #button wird angezeigt
    return

def hauptmenü():
    myButton4.pack_forget()
    myHauptmenü4_2.pack_forget()
    myLehrerkürzel.pack_forget()
    myInformation.pack_forget()
    myButton1.pack(side=LEFT)
    myButton2.pack(side=LEFT)
    myButton3.pack(side=LEFT)
    myEvent.pack(side=LEFT)
    myAusfall.pack(side=LEFT)
    return

def schule():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myHauptmenü4_2.pack(side=LEFT)
    myLehrerkürzel.pack(side=LEFT)
    myInformation.pack(side=LEFT)
    return

def persönliche_daten():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def event():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def ausfall():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def lehrerkürzel():
    nestedList = [["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|", "AND","","","",":","","","","","","Mark Andauer","","","",":", "and@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","TR","","","","",":","","","","", "Werner Traube","","","",":", "tr@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","STF","","","",":", "Wolfgang Streitfurth",":", "stf@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","LOL","","","",":","","","", "Leon Lollipop","","","","",":", "lol@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","WND","","","",":","","","","" "Hubert Wandler","","","",":", "wnd@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","WA","","","","",":", "","","","" "Werner Aufmund","","","",":", "wa@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","HM","","","","",":","","","","","", "Happy Meal","","","","","",":", "hm@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","KK","","","","",":","","", "Kirsten Kaufland","","",":", "kk@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-""|"],
                  ["|","AKK","","","",":","","","","","","", "Anne Kern","","","","","",":", "akk@schulebza.com"],
                  ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","",":"],
                  ["|","Kürzel", ":","","","","","","","","","Name","","","","","","","","",":","E-Mail"]]

    myInformation.pack_forget()
    myLehrerkürzel.pack_forget()
    myHauptmenü4_2.pack_forget()
    myButton4.pack(side=LEFT)
    lehrerkürzelText = Text(root, height=30,font=('times', 25, 'bold', 'italic'))
    lehrerkürzelText.pack()
    for item in nestedList:
        lehrerkürzelText.insert('1.0', ' '.join(map(str, item)))
        lehrerkürzelText.insert('1.0', "\n")

frame = Frame(root)
frame.pack()

topframe = Frame(root)
topframe.pack(side = TOP)

myButton1 = Button(frame, text="Unterricht",command=unterricht, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton1.pack(side = LEFT) #die anordnung

myButton2 = Button(frame, text="Schule",command=schule, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton2.pack(side = LEFT)

myButton3 = Button(frame, text="Persönliche Daten",command=persönliche_daten, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton3.pack(side = LEFT)

bottomframe = Frame(root)                                                                                               #Bottomframe, damit der Event und Ausfall Button unten steht
bottomframe.pack(side = BOTTOM)                                                                                         #die Anordnung

myEvent = Button(text="Event",command=event, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)                             #Eventbutton wurde erstellt
myEvent.pack(side= LEFT)

myAusfall = Button(text="Ausfall/Vertretung",command=ausfall, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)            #Ausfall/Vertretung Button wurde erstellt
myAusfall.pack(side= RIGHT)

myButton4 = Button(frame, text="Hauptmenü", command=hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=93, height=10)         #Hauptmenü Button wurde erstellt
myButton4.pack(side=LEFT)
myButton4.pack_forget()

myHauptmenü4_2 = Button(frame, text="Hauptmenü", command=hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myHauptmenü4_2.pack(side=LEFT)
myHauptmenü4_2.pack_forget()

myLehrerkürzel = Button(frame, text="Lehrerkürzel", command=lehrerkürzel, bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myLehrerkürzel.pack(side=LEFT)
myLehrerkürzel.pack_forget()

myInformation = Button(frame, text="Über die Schule", command="", bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myInformation.pack(side=LEFT)
myInformation.pack_forget()


root.mainloop()
