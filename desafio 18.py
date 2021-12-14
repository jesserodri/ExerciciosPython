#leia o valor do angulo e mostre o seno, cosseno e tangente
import math

ang = float(input("digite o valor do angulo: "))
sen= math.sin(math.radians(ang)) # para fazer o calculo corretamente precisa formatar para radianos
cos = math.cos(math.radians(ang))# se nao a conta nao sai corretamente
tan = math.tan(math.radians(ang))

print("angulo de {}º tem o Seno = {:.2f}, Cosseno = {:.2f}, Tangente = {:.2f}".format (ang,sen,cos,tan))