#programa que mostra o quanto a pessoa tem de dinheiro na carteira e quantos dolares ela pode comprar

car = float(input("Quantos reais voce tem na carteira? "))
dolar = 1 # era mais facil fazer dessa maneira:
real = 5.35     # dolar = real / 5.35 (que é a cotação do dolar)
buy = car / real # onde real é o equivalente a 1 dolar!

if car < 5.35:
    buy = dolar * real
    print("voce nao tem dinheiro o suficiente para comprar 1 dolar americano")
else:
    print("voce tem {} reais na carteira e pode comprar ate {:.2f} Dolares americanos".format(car, buy))