#pergunte o salario e efetue o aumento para salarios superiores a 1250 10 %,para inferior ou igual 15%
import time

salAnt = float(input("infome seu salario atualmente R$:"))

print("Aumento salarial para os colaboradores!")

if salAnt <= 1250:
    salNovo = salAnt * 15 / 100 + salAnt
    print (("Aumento de 15%, o seu Novo salario ficou em: R${:.2f}".format(salNovo)))
else:
    salNovo = salAnt * 10 / 100 + salAnt
    print("Aumento de 10%, o seu novo salario ficou em: R${:.2f}".format(salNovo))