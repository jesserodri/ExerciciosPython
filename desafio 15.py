# aluguel de carro...

dias_car = int(input('Quantos dias o carro ficou alugado ? '))
dias_car = dias_car * 60
km_rod = float(input('Quantos km rodados ? '))
km_rod = km_rod * 0.15
total = dias_car + km_rod
print("o total a pagar ficou em R${:.2f}".format(total))