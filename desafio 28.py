#Jogo da adivinhação 1.0
import random
import time
print("-=-" * 20)
print("                 Jogo da adivinhação ")
np = random.randint(0,5)
n = int(input("..... Pensei em um numero entre 0 a 5. Tente acertar: "))
print("processando ...")
time.sleep(2) # coloca um tempo
if n == np:
    print("Parabens voce acertou !")
else:
    print("Errou... O numero que escolhi foi o {}  Achei que voce fosse conseguir !".format(np))

#ou
#print('parabens voce acertou'if n == np else 'voce errou') \ if simplificado