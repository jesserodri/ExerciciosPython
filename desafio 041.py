#informe a idade do atleta e mostre sua categoria!

from datetime import date
atual = date.today().year ## data atual
print("-_-" * 15, "\n           categoria do atleta ")
idade_at = int(input("informe a idade do atleta:"))



if idade_at <= 9 :
    print("Categoria: Mirim")
elif idade_at > 9 and idade_at <= 14: #idade_at <=14
    print("Categoria: Infantil")
elif idade_at > 14 and idade_at <= 19:#idade_at <=19
    print("Categoria: Junior")
elif idade_at == 20: #idade_at <=20
    print("Categoria: Sênior")
else: # #idade_at > 25
    print("Categoria: Master")
