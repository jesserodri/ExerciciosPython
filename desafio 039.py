# informe a data de nascimento e mostre se ele tem que se apresentar ou nao e quanto tempo falta
from datetime import date

atual = date.today().year
nasc = int(input("Ano de nascimento"))
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18:
    print("voce tem que se alistar imediatamente!")
elif idade > 18:
    saldo = idade - 18
    print("se voce nao se alistou, ja devia ter se alistado a {} anos".format(saldo))
    ano = atual - saldo
    print("seu alistamento foi em{} ".format(ano))
else:
    saldo = 18 - idade
    print("voce ainda nao tem 18 anos e ainda faltam {} anos para o alistamento".format(saldo))
    ano = atual + saldo
    print("Seu alistamento sera em {}".format (ano))
