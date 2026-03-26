
numero = int(input("Anna numero:"))

for i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")

lista = []
while True:
    arvo = int(input("Uusi arvo:"))

    if arvo ==0 :
        print("Hei Hei!")
        break

    lista.append(arvo)

    print("Lista nyt:", lista)
    print("Lista järjestyksessä:", sorted(lista))


sanat= ["juoma", "kana", "koira", "nocco", "kakka", "puhelin"]

maara=0
for sana in sanat:
    if len(sana)>5:
        maara+=1

print("Yli 5 kirjaimen sanoja:", maara)


def kuusi(koko):
    print("Tämä on kuusi!")

    leveys=2*koko-1 #kuusen alin leveys

    #Kuusen oksat
    for i in range(1, koko+1):
        tahtia=2*i-1
        print(("*"*tahtia).center(leveys))

    # Rungon tähti
    print("*".center(leveys))

kuusi(5)


def suurin_arvo(a,b,c):
    return max(a,b,c)

l1=int(input("Anna ensimmäinen luku:"))
l2=int(input("Anna toinen luku:"))
l3=int(input("Anna kolmas luku:"))

print("Suurin arvo on:", suurin_arvo(l1,l2,l3))
