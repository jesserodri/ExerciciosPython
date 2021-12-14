# leia o valor dos catetos e mostre a hipotenusa

import math
#from math import hypot
x = float(input("digite o cateto oposto X: "))
y = float(input("digite o cateto adjacente Y: "))

# hip = ( x ** 2 + y ** 2) ** (1/2) é o mesmo que :
hip = math.hypot(x,y)

print("resultados é {:.2f}".format(hip))