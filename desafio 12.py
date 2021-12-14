# programa que leia o preço do produto e mostre seu novo preço com 5% de desconto

prod = float(input("Insira o valor do produto atualmente: "))
des = prod * 0.05 # poderia fazer --- prod - (prod * 5 /100)
prodes = prod - des

print("Valor do produto ficou em {:.2f} reais com o desconto de 5%".format(prodes))

