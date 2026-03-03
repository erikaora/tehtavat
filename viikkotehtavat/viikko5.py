
luku=1

while luku <=1000:
    if luku %3 == 0:
        print(luku)
    luku +=1


while True:
    tuumat=float(input("Anna tuumamäärä (negatiivinen luku lopettaa):"))
    if tuumat < 0 :
        print("Ohjelma lopetetaan")
        break
    senttimetrit= tuumat*2.54
    print(f"{tuumat} tuumaa on{senttimetrit}senttimetriä")

luvut = []

while True:
    syote = input("Anna luku (Enter lopettaa):")
    if syote == "" :
        break

    luku=float(syote)
    luvut .append(luku)

if len(luvut) > 0 :
    print("Pienin:", min(luvut))
    print("Suurin", max(luvut))

else:
    print("Lukuja ei annettu.")

import random

salainen=random.randint(1,10)

while True:
    arvaus= int(input("Arvaa luku väliltä 1-10:"))
    if arvaus > salainen:
        print("Liian suuri arvaus")
    elif arvaus < salainen:
        print("Liian pieni arvaus")
    else:
        print("Oikein!")
        break


import random

N= int(input("Kuinka monta pistettä arvotaan?"))
ympyrassa=0

for i in range(N):
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)

    if x**2+ y**2<= 1:
        ympyrassa+=1

pii= 4* ympyrassa/N
print(f"Piin likiarvo on: {pii}")




