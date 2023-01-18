
#0

while True: 
    iq=int(input("Kui palju IQ teil on?"))














#4

from math import *
from random import *


while True:
    try:
        arv=int(input("Vali suvaline arv 1-10: "))
        if arv>10: break
        if arv<1: break
        print(int("1"))
        print(int("2"))
        print(int("3"))
        print(int("4"))
        print(int("5"))
        print(int("6"))
        print(int("7"))
        print(int("8"))
        print(int("9"))
        print(int("10"))
        print("")
        break
    except:
        print("Vale arv")
print("↓ Korrutustabel ↓")
a=1
while a<=10:
    b=1
    while b<=10:
        c=a*b
        print(c, end=" ")
        b+=1
    print(" ")
    a+=1


#2

n=0
print ("kolmnurga")
for e in range (11,0,-1):
    n = n + 1
    for f in range (1, n+1):
        print ("*", end = "")
    print()
print("")