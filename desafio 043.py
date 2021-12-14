# calculo de imc e classique as pessoas com o indice !

import time
import os

alt = float(input("informe sua altura: "))
peso = float(input("informe o seu peso atualmente: "))
imc =  peso/(alt ** 2)

print("calculando seu IMC ...")
time.sleep(1)

print("O resultado saiu..\nseu IMC é de {:.1f}".format(imc))
if imc < 18.5:
    print("Voce esta abaixo do peso")
elif 18.5 <= imc < 25:
    print(" Você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está na categoria sobrepeso")
elif 40 <= imc < 30:
    print("voce esta na categoria obesidade")
else: # elif >= 40:
    print("voce esta na categoria obesidade morbida")