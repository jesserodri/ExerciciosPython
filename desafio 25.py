#crie um programa que leia o nome de uma pessoa  e diga  se ela tem silva no nome

n = input("digite o seu nome: ")

print("seu nome tem silva? {}".format('silva'in n.lower()))

#ou

ve= 'silva' in n.lower()
print(ve)
if ve == True:
    print("o seu nome tem silva")
else:
    print("o seu nome nao tem silva")

