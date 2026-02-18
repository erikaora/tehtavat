import math

name = input("Anna nimesi:")


print("Hei " + name)
print("Hei", name)
print(f"Hei {name}!")

sade=float(input("Anna ympyrän säde:"))
pintaala=math.pi*sade**2

print(f"Ympyrän pintaala on {pintaala}")

kanta=float(input("Anna suorakulmion kanta:"))
korkeus=float(input("Anna suorakulmion korkeus:"))

piiri=2*(kanta+korkeus)
pintaala=kanta*korkeus

print(f"Suorakulmion piiri on {piiri}")
print(f"Suorakulmion pintaala on {pintaala}")

luku1=float(input("Anna 1 kokonaisluku:"))
luku2=float(input("Anna 2 kokonaisluku:"))
luku3=float(input("Anna 3 kokonaisluku:"))

summa=luku1+luku2+luku3
tulo=luku1*luku2*luku3
keskiarvo=summa/3

print(f"Summa: {summa}")
print(f"Tulo: {tulo}")
print(f"Keskiarvo: {keskiarvo}")

leiviskat=float(input("Anna leiviskat:"))
naulat=float(input("Anna naulat:"))
luodit=float(input("Anna luodit:"))

luodityhteensa=leiviskat*20*32+naulat*32+luodit
grammat=luodityhteensa*13.3

kilot=int(grammat//1000)
grammatjaljella=grammat-kilot*1000

print("Massa nykymittojen mukaan:")
print(f"{kilot}kilogrammaa ja {grammatjaljella:.2f}grammaa.")

import random

koodi1=""

for i in range(3) :
    koodi1 +=str(random.randint(0,9))

koodi2=""
for i in range(4):
    koodi2 +=str(random.randint(1,6))

print("Kolmenumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)

