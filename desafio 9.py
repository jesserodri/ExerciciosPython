#programa que leia um numero e mostre sua tabuada

num = int(input("digite o numero que deseja: "))
tab = 0
resul= 0

while num >= 0:
    resul = tab * num
    print("{} x {} = {}".format(num,tab,resul))
    tab += 1
    if tab >=11:
        break
