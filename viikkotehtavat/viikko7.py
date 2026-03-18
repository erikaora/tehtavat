import random

n = int(input("Kuinka monta arpakuutiota heitetään?"))

summa = 0

for i in range(n):
    heitto=random.randint(1,6)
    summa += heitto

print("Silmälukujen summa:", summa)


luvut = []

while True:
     syote = input("Anna luku(tyhjä lopettaa):")
     if syote == "":
         break

     luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta:")
for luku in luvut [:5]:
    print(luku)

luku= int(input("Anna kokonaisluku:"))

on_alkuluku= True

if luku < 2:
    on_alkuluku= False
else:
    for i in range(2,luku):
        if luku % i == 0:
            on_alkuluku= False
            break

if on_alkuluku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")


kaupungit = []

for i in range (5):
    nimi=input("Anna kaupungin nimi:")
    kaupungit.append(nimi)

print("Kaupungit:")

for k in kaupungit:
    print(k)

