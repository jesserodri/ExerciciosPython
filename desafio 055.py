maior = 0
men = 0
for p in range(1, 6):
    peso = float(input("peso da {}ª pessoa: ".format(p)))
    if p == 1: # aqui como é a primeira pessoa então nao tem peso maior ou menor somente inicial
        maior = peso
        men = peso
    else:
        if peso > maior:
            maior = peso
        if peso < men:
            men = peso
print("o maior peso lido foi o {}KG".format(maior))
print(" o menor peso lido foi de {}KG".format(men))