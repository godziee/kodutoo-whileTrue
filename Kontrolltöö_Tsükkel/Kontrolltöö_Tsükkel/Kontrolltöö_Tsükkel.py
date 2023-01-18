

#variant 5

#1

from calendar import c
from math import *
from random import *

while True:
    try:
        n = int(input("Sisestage ekraanil kuvatavate majade arv. (0-9): "))
        m1 = "  \n   ~~~~~  "
        m2 = " \n  /_____\ "
        m3 = " \n  | []  | "
        m4 = "  \n   -----  "
    
        if n>0 and n<10:
            for x in range(n):
                print(m1,m2,m3,m4)
            break
        else:
            print("Tähelepanu! Valige arv, mis on suurem kui 0 ja väiksem kui 10.")
    except:
        print("Viga! Vajalik number.")

#2
#20 учеников по 2 класса

for o in range(1,3):
    info = 0
    for i in range(1,2): #20 учеников
        sum = 0
        for a in range(1,6):
            a = int(input("Sisestage hinne: "))
            sum = sum + a
        v = sum
        print(v)
        v = v/5
        print(v)
        print(i,"Keskmine hinne",v) #номер ученика и его средняя оценка
        print("----------------------")
info = info + v
print()
print(info,"Iga klassi keskmine hinne")
print("--------------------------")
print("Lõpp!")
print("")

#3

print(" ")
õpilased = random.randint(3, 10)
print("Kõik õpilased:", õpilased )
hindeid = []
for i in range(õpilased):
    hinne = random.randint(1, 100)
    hindeid.append(hinne)
min_hinne = hinne[0]
maks_hinne = hinne[0]
for hinne in hindeid:
    if hinne < min_hinne:
        min_hinne = hinne
    elif hinne > maks_hinne:
        maks_hinne = hinne
print(f"min. hinne:", min_hinne )
print(f"maks. hinne:", maks_hinne )
print()

#4

print(" ")
linnaosad = 12
linnaosade_teave = {}
for i in range(1, linnaosad + 1):
    linnaosade_teave[i] = {
        "elanikkonnast": random.randint(1, 200),
        "kogu_ala": random.randint(1, 100)
    }
for i in range(1, linnaosad + 1):
    print(f"Linnaosa {i} - elanikkonnast: {linnaosade_teave[i]['elanikkonnast']} tuhat inimest, ala: {linnaosade_teave[i]['kogu_ala']} km2")
kogu_elanikkond = sum([linnaosade_teave[i]['elanikkonnast'] for i in range(1, linnaosad + 1)])
kogu_ala = sum([linnaosade_teave[i]['kogu_ala'] for i in range(1, linnaosad + 1)])
keskmine_tihedus = kogu_elanikkond / kogu_ala
print(f"Piirkonna keskmine asustustihedus: {keskmine_tihedus} tuhat inimest/km2")
print()
print("Lõpp!")
print("Ilusat päeva!")




    


            

