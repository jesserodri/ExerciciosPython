#programa para ler salario de um funcionario  e mostre seu novo salario, com 15% de aumento.

salAnte = float(input("qual seu salario atualmente: "))
aum = salAnte * 0.15 # poderia ter feito ---  salAnte + (salAnte * 15 /100) nao iria precisa da variavel aum
salAtual = salAnte + aum
print("o seu novo salario com aumento de 15% ficou equivalente a {:.2f}".format(salAtual))


