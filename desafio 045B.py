# esse codigo foi o que o professor fez
import time
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')

computador = randint(0,2)
#print("o computador escolheu {}".format(itens[computador]))
print("     Jokenpo")
print("-="*10)
print('''Suas opções:

[0] PEDRA  
[1] PAPEL
[2] TESOURA
''')
print("-="*10)
jogador = int(input("Qual é a sua jogada: "))

print("\nJO!")
time.sleep(1)
print("KEN!")
time.sleep(1)
print("PO")
time.sleep(0.5)

print("-="*10)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou  {}".format(itens[jogador]))
print("-="*10)

if computador == 0:#pedra
    if jogador == 0:
        print("Empate")
    elif jogador ==1:
        print("Jogador venceu!")
    elif jogador ==2:
        print("Computador venceu!")
    else:
        print("invalido")
if computador == 1:#papel
    if jogador == 0:
        print("Computador venceu!")
    elif jogador ==1:
        print("Empate!")
    elif jogador ==2:
        print("Jogador venceu!")
    else:
       print("invalido")
if computador == 2:#tesoura
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador ==1:
        print("Computador venceu!")
    elif jogador ==2:
        print("Empate!")
    else:
        print("invalido")