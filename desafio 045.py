#programa que jogue jokenpo 1.0

import random
import os
import time

print("_-_"*7)
print("     1-papel")
print("     2-tesoura")
print("     3-pedra")
print("_-_"*7)

ec = random.randint(1,3)
#1- papel, 2- tesoura, 3-pedra
ep = int(input("Escolha: "))
#nov = True
#while nov == True:

print("\n\nJO!")
time.sleep(1)
print("KEN!")
time.sleep(1)
print("PO!\n")
time.sleep(1)

print("_-_"*10)
if ec == 1:
    print("o computador escolheu: PAPEL")
elif ec == 2:
    print("o computador escolheu: TESOURA")
elif ec == 3:
    print("o computador escolheu: PEDRA")
if ep == 1:
    print("voce escolheu: PAPEL")
elif ep == 2:
    print("voce escolheu: TESOURA")
elif ep == 3:
    print("voce escolheu: PEDRA")
print("_-_"*10)

print("")

if ec == 1 and ep == 2:

        print("Parabens player, Você ganhou!!")

elif ec == 2 and ep == 1:
   print("Não foi dessa vez, o Computador ganhou! ")
elif ec == 1  and ep == 3:
   print("Nã0 foi dessa vez, o Computador ganhou!")
elif ec == 3 and ep == 1:
   print("Parabens player, Você ganhou !")
elif ec == 2 and ep == 3:
   print("Parabens player, Você ganhou ! ")
elif ec == 3 and ep == 2:
   print("Não foi dessa vez, o Computador ganhou! ")
elif ec == 2 and ep == 2:
    print("Ninguem ganhou! os dois escolheram tesoura, jogue novamente ")
elif ec == 1 and ep == 1:
    print("Ninguem ganhou! os dois escolheram papel, jogue novamente ")
elif ec == 3 and ep == 3:
    print("Ninguem ganhou! os dois escolheram pedra, jogue novamente ")
else:
   print(" numero invalido ! Tente novamente!")
