# ler o numero maior e menor 

n1 = int(input("informe o primeiro numero: "))
n2 = int(input ("informe o segundo numero: "))
n3 = int(input("informe o terceiro numero: "))
#verificando o menor
menor = n1
if n1<n2 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# verificando o maior
maior = n1
if n2>n3 and n2>n1:
    maior= n2
if n3>n2 and n3>n1:
    maior = n3
print("o menor valor digitado foi {}".format(menor))
print("o maior valor digitado foi {}".format(maior))


'''
if (n1 > n2) and (n3 < n2):
    print("o primeiro numero informado {} é maior ".format(n1)) # 1
    print("o terceiro numero informado {} é o menor".format(n3)) # 3
if (n3 > n1 ) and (n1 < n2) and (n3 > n2) :
    print("o terceiro numero informado {} é maior".format(n3))  # 3
    print("o primeiro numero informado {} é menor".format(n1))  # 1
if (n2 > n1 ) and (n3 < n1):
    print("o segundo numero informado {} é maior".format(n2)) # 2
    print("o terceiro numero informado {} é menor".format(n3)) # 3
if (n3 > n2 ) and (n2 < n1) and (n3 > n1):
    print("o terceiro numero informado {} é o maior".format(n3)) # 3
    print("o segundo numero informado {} é o menor".format(n2)) # 2

if (n2 > n3 ) and (n1 < n3):
    print("o segundo numero informado {} é o maior ".format(n2))# 2
    print("o primeiro numero informado {} é o menor".format(n1))# 1

if (n1 > n2 ) and (n2 < n3) and (n1 > n3):
    print("o primeiro numero informado {} é o maior ".format(n1))# 1
    print("o segundo numero informado {} é o menor".format(n2))# 2
'''



