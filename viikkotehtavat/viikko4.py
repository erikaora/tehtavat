
pituus=float(input("Anna kuhan pituus senttimetreinä: "))

alamitta= 37

if pituus < alamitta:
    puuttuu=alamitta - pituus
    print(f"Kuha on alamitainen, laske kuha takaisin järveen." )
    print(f"ALimmasta sallitusta mitasta puuttuu: {puuttuu: .1f} cm")

else:
    print("Kuha on sallitun kokoinen, saat pitää sen")



hytti= input("Anna hyttiluokka (LUX, A, B, C):"). upper()
if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")


sukupuoli=  input("Anna biologinen sukupuoli (nainen/mies):").lower()
hb=float(input("Anna hemoglobiiniarvo (g/l):"))

if sukupuoli == "nainen":
    if hb < 117 :
        print("Hemoglobiiniarvo on alhainen")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")


elif sukupuoli == "mies":
    if hb < 134 :
        print("Hemoglobiiniarvo on alhainen")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

else:
    print("Virheellinen sukupuoli")


vuosi=int(input("Anna vuosiluku:"))

if(vuosi % 4== 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")

k

