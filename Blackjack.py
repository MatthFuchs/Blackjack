import random

class Karte():
    def __init__(self,Farbe,Wert):
        self.Farbe=Farbe
        self.Wert=Wert

def Spielerhirn():
    global Spielerziehen
    if Spielerziehen==True:
        if augenspieler>21:
            Spielerziehen=False
            print("------------------")
            print("BUST")
            Abschluss()

def Dealerhirn():
    global Dealerziehen
    if augendealer==21:
        Dealerziehen=False
    if augendealer>21:
        Dealerziehen=False
        print("------------------")
        print("Dealer BUST")
        Abschluss()
    if augendealer>augenspieler and augendealer>17:
        Dealerziehen=False



def nächsterzug():
    global Spielerziehen
    if Spielerziehen==True:
        zug=input("Noch eine Karte? Y/N: ")
        if zug == "Y" or zug == "y":
            Spielerziehen=True
            Ausgaben()
        if zug == "N" or "n":
            Spielerziehen=False
            Ausgaben()
        else:
            print("Falscher Eingabe...")
            nächsterzug()

def Dealerkarteeval():
    global Dealerwert
    Dealersuit=Dealerkarte.Wert

    if Dealerkarte.Wert =='Ass':
        Dealerwert = 11
    if Dealersuit =='Bube' or Dealersuit == 'Dame' or Dealersuit == 'König':
        Dealerwert = 10
    else:
        try:
            Dealerwert = int(Dealersuit)
        except:
            if augendealer <11:
                Dealerwert=11
            else:
                Dealerwert=1

    #print(Dealerwert)

def Spielerkarteeval():
    global Spielerwert
    Spielersuit=str(Spielerkarte.Wert)

    if Spielerkarte.Wert =='Ass':
        Spielerwert=11
    if Spielersuit =='Bube' or Spielersuit == 'Dame' or Spielersuit == 'König':
        Spielerwert=10
    else:
        try:
            Spielerwert=int(Spielersuit)
        except:
            if augenspieler <11:
                Spielerwert=11
            else:
                Spielerwert=1
    #print(Spielerwert)

def Dealerzug():
    global Dealerkarte
    Dealerkarte=random.choice(Kartendeck)
    Kartendeck.remove(Dealerkarte)

def Spielerzug():
    global Spielerkarte
    Spielerkarte=random.choice(Kartendeck)
    Kartendeck.remove(Spielerkarte)

def Ausgaben():
    global augenspieler,augendealer

    if Spielerziehen == True:
        Spielerzug()
        print("Deine Karte: "+Spielerkarte.Farbe+" "+Spielerkarte.Wert)
        Spielerkarteeval()
        try:
            spielerwertliste.append(Spielerwert)
            augenspieler=sum(spielerwertliste)

        except:
            print("konnte Spielerkarte nicht reintun")
        Spielerhirn()
    else:
        print("Spieler Skip")                                               #Spieler Skip

    if Dealerziehen == True:
        Dealerzug()
        print("Dealer Karte: "+Dealerkarte.Farbe+" "+Dealerkarte.Wert)
        Dealerkarteeval()
        try:
            dealerwertliste.append(Dealerwert)
            augendealer=sum(dealerwertliste)

        except:
            print("konnte dealerwert nicht hinzufügen")

        Dealerhirn()
    else:                                                           #Dealer Skip
        print("Dealer Skip")


    print("Gesamtwert deiner Karten:" + str(augenspieler))
    print("Gesamtwert der Dealerkarten: " + str(augendealer))

    checkaktiv()


def checkaktiv():
    if Spielerziehen==True or Dealerziehen==True:
        nächsterzug()
    else:
        Abschluss()

def Abschluss():
    global Geldbeutel
    print("-----ERGEBNIS-----")
    print("")
    if augenspieler>21 and augendealer<=21 or augendealer>augenspieler and augendealer<=21:
        print("Du hast "+str(einsatz)+" Euro Verloren :(")
    elif augenspieler<=21 and augenspieler > augendealer or augendealer>21 and augenspieler<=21:
        print("Du hast "+str(einsatz)+" Euro Gewonnen :)")
        Geldbeutel+=einsatz*2
    elif augenspieler == augendealer and augenspieler <=21:
        print("Unentschieden")
        Geldbeutel+=einsatz
    else:
        print("Error")
    print("")
    print("-------ENDE-------")
    ende()

def ende():

    nochmal=input("Nochmal Spielen? Y/N: ")
    if nochmal =="Y" or nochmal== "y":
        init()
    if nochmal == "N" or nochmal== "n":
        exit()

    print("Falsche Eingabe...")
    ende()


def Kartendeckmachen():
    global Kartendeck
    farben=["Pik","Herz","Karo","Kreuz"]
    werte=["Ass","2","3","4","5","6","7","8","9","10","Bube","Dame","König"]
    Kartendeck=[Karte(Farbe, Wert)for Farbe in farben for Wert in werte]

def Begrüßungdef():
    global Begrüßung,einsatz,Geldbeutel
    if Begrüßung ==1:
        print("Moin Meister, lass mal Zocken")
        Begrüßung =0


    try:
        print("Du hast " + str(Geldbeutel) + " Flocken in der Tasche")
        if Geldbeutel==0:
            print("Eigentlich bist du Pleite...aber Matze kümmert sich ja um dich, bekommst nen Tausi\nIch kanns mir ja leicht leisten mit meinem Bitcoin Reichtum")
            Geldbeutel=1000
        einsatz=int(input("Wieviel willst du denn einsetzen?: "))
        if einsatz <= Geldbeutel:
            Geldbeutel-=einsatz
        else:
            print("Da reicht die Kohle nicht...")
            Begrüßungdef()
    except:
        print("Falsche Eingabe...")
        Begrüßungdef()

    Kartendeckmachen()
    Ausgaben()


def init():
    global Spielerziehen,Dealerziehen
    Spielerziehen=True
    Dealerziehen=True
    global spielerwertliste,dealerwertliste
    spielerwertliste=[]
    dealerwertliste=[]
    global augenspieler,augendealer
    augenspieler=0
    augendealer=0
    Begrüßungdef()

def preinit():
    global Begrüßung,Geldbeutel
    Geldbeutel = 1000
    Begrüßung = 1
    init()


if __name__=="__main__":
    preinit()