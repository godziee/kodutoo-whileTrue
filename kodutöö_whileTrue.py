

from math import *
from random import *


print("Arvuta peast! ...4*100-55")
o_vastus=4*100-55
vastus=int(input("Lahenda ülesanne..."))
k=1                                                 #k(katsed) - попытки
while True:
    if vastus!=o_vastus:
        print("Viga! Sisesta Õige vastus...", )
        vastus=int(input("Sisesta vastus..."))
        k+=1
    else:
        print("Õige vastus! Katsed oli ...",k )
        break
