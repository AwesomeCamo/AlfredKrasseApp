from tkinter import *

root = Tk()
root.title('Alfred Krasse App')                         #titel name
root.iconbitmap("./resources/images/HomeIcon.ico")      #Bild (icon oben links)
root.geometry("1920x1080")                              #die größe der App
rootHeight = root.winfo_height()                        #die Höhe des Fensters
rootWidth = root.winfo_width()                          #die Breite des Fensters
root['background'] = '#FFFEF6'                          #der Hintergrund

def Unterricht():                                       #Funktion erstellen
    myButton1.pack_forget()                             #vergisst den grid, kann aber wieder neu aufgerufen werden durch "myButton.pack()"
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)                           #button wird angezeigt
    return

def Hauptmenü():
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

def Schule():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myHauptmenü4_2.pack(side=LEFT)
    myLehrerkürzel.pack(side=LEFT)
    myInformation.pack(side=LEFT)

    return

def Persönliche_Daten():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def Event():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def Ausfall():
    myButton1.pack_forget()
    myButton2.pack_forget()
    myButton3.pack_forget()
    myEvent.pack_forget()
    myAusfall.pack_forget()
    myButton4.pack(side=LEFT)
    return

def Lehrerkürzel():
    nestedList = [["AND", "Mark Andauer", "and@schulebza.com"],
                  ["TR", "Werner Traube", "tr@schulebza.com"],
                  ["STF", "Wolfgang Streitfurth", "stf@schulebza.com"],
                  ["LOL","Leon Lollipop","lol@schulebza.com"],
                  ["WND","Hubert Wandler","wnd@schulebza.com"],
                  ["WA","Werner Aufmund","wa@schulebza.com"],
                  ["HM","Happy Meal","hm@schulebza.com"],
                  ["KK","Kirsten Kaufland","kk@schulebza.com"],
                  ["AKK","Anne Kern","akk@schulebza.com"]]

    print(": Kürzel " " " " : Name "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" : EMail "" "" "" "" "" "" "" "" "" "" "" ""  :")
    for item in nestedList:
        print(":", item[0]," "*(7-len(item[0])),":",item[1]," "*(20-len(item[1])),":",item[2]," "*(17-len(item[2])),":")

    myInformation.pack_forget()
    myLehrerkürzel.pack_forget()
    myHauptmenü4_2.pack_forget()
    myButton4.pack(side=LEFT)

frame = Frame(root)
frame.pack()

Topframe = Frame(root)
Topframe.pack(side = TOP)

myButton1 = Button(frame, text="Unterricht",command=Unterricht, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton1.pack(side = LEFT) #die anordnung

myButton2 = Button(frame, text="Schule",command=Schule, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton2.pack(side = LEFT)

myButton3 = Button(frame, text="Persönliche Daten",command=Persönliche_Daten, bg="#2d2d2d",fg="#e4bc1f",width=93,height=10)
myButton3.pack(side = LEFT)

Bottomframe = Frame(root)                                                                                               #Bottomframe, damit der Event und Ausfall Button unten steht
Bottomframe.pack(side = BOTTOM)                                                                                         #die Anordnung

myEvent = Button(text="Event",command=Event, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)                             #Eventbutton wurde erstellt
myEvent.pack(side= LEFT)

myAusfall = Button(text="Ausfall/Vertretung",command=Ausfall, bg="#2d2d2d",fg="#e4bc1f",width=140,height=65)            #Ausfall/Vertretung Button wurde erstellt
myAusfall.pack(side= RIGHT)

myButton4 = Button(frame, text="Hauptmenü", command=Hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=93, height=10)         #Hauptmenü Button wurde erstellt
myButton4.pack(side=LEFT)
myButton4.pack_forget()

myHauptmenü4_2 = Button(frame, text="Hauptmenü", command=Hauptmenü, bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myHauptmenü4_2.pack(side=LEFT)
myHauptmenü4_2.pack_forget()

myLehrerkürzel = Button(frame, text="Lehrerkürzel", command=Lehrerkürzel, bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myLehrerkürzel.pack(side=LEFT)
myLehrerkürzel.pack_forget()

myInformation = Button(frame, text="Über die Schule", command="", bg="#2d2d2d", fg="#e4bc1f", width=93, height=rootHeight)
myInformation.pack(side=LEFT)
myInformation.pack_forget()


root.mainloop()
