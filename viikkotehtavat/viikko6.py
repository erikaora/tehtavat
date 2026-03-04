nimi= input("Kerro nimesi:")

if nimi !="Matti":
    annokset= int(input("Montako keittoannosta?"))
    hinta= annokset * 5.90
    print("Kokonaishinta on", hinta)

print("Seuraava, kiitos!")

tuntipalkka= float(input("Kerro tuntipalkkasi:"))

tunnit= float(input("Kerro tehdyt tuntisi:"))

viikonpaiva=input("Kerro viikonpäivä:")

if viikonpaiva.lower()=="sunnuntai":
    paivapalkka= tuntipalkka * 2 * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print ("Päiväpalkka:", paivapalkka, "euroa")

from math import sqrt

while True:
    luku= int(input("Anna  kokonaisluku:"))
    if luku==0:
        print("Exiting...")
        break
    elif luku<0:
        print("Virheellinen numero")
    else:
        print("Neliöjuuri on:", sqrt(luku))


tarina =""

while True:
    sana=input("Anna sana lisättäväksi tarinaan:")
    if sana == "loppu":
        print(tarina.strip())
        break
    else:
        tarina += sana + ""

while True:
    print("\nValitse toiminto:")
    print("1=yhteenlasku")
    print("2=Vähennyslasku")
    print("3=Kertolasku")
    print("4=Jakolasku")
    print("5=Lopeta")

    valinta=input("Valintasi:")
    if valinta == "0":
        print("Ohjelma lopetettu.")
        break

    luku1= float(input("Anna ensimmäinen luku:"))
    luku2=float(input("Anna toinen luku:"))

    if valinta == "1":
        print ("Tulos:", luku1+luku2)
    elif valinta == "2":
        print("Tulos:", luku1-luku2)
    elif valinta == "3":
        print("Tulos:", luku1*luku2)
    elif valinta == "4":
        if luku2 !=0:
            print("Tulos:", luku2/luku1)
        else:
            print("Nollalla ei voi jakaa.")
    else:
        print("Virheellinen valinta")
print("Ohjelma lopetettu.")

