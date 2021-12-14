#informe dois numeros e mostre se algum é maior ou iguais

n1 = int(input("informe o primeiro numero: "))
n2 = int(input("informe o segundo numero: "))

if n1 > n2:
    print("o primeiro numero é maior que o segundo numero informado")
elif n1 < n2:
    print("o segundo numero é maior que o primeiro numero informado")
else:
    print("os numeros informados são iguais !")