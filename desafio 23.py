#programa que leia um numero entre 0 a 9999 e mostre na tela cada digito separado

num = int((input("Digite um valor entre 0 a 9999: ")))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("unidade:{}  \ndezena:{} \ncentena:{} \nmilhar:{} ".format(u,d,c,m))
