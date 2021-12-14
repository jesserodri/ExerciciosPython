num = int(input("Digite um Numero:"))
tot = 0

for c in range(1, num + 1): #coloque +1 pois no for ele vai tirar o ultimo numero
    if num % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[34m',end=' ')
    print("{}".format(c), end=' ')
print('\033[m',end=' ')
print("\no Numero {} foi divisil {} vezes".format(num, tot), end=' ')

if tot == 2:
    print("E É um numero primo!".format(num))

else:
    print("E NÂO é um numero primo!")