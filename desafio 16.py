#leia um numero real e mostre o numero inteiro dele
import math


num = float(input('digite um numero real: '))

#conseguimos fazer mais de uma forma que são as seguintes:

print("a porção inteira de {} é o numero {:.0f}".format(num,num))

#ou \ esse aredonda para o primeiro numero inteiro

print(' a porção inteira de {} é o numero {}'.format(num, math.floor(num)))

#ou \ esse tira o restante dos numeros depois do primeiro numero

print(' a porção inteira de {} é o numero {}'.format(num, math.trunc(num)))