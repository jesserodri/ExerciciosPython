cont = 0
s = 0
for c in range(1,7):
    n = int(input("digite um valor: "))
    if n % 2 == 0:
        cont += 1
        s = s + n
print("o valor da soma dos {} numeros pares contados é de {} ".format(cont,s))