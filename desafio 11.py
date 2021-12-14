# programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessaria para pintar                Sabendo que cada litro de tinta pinta 2metros quadrados ou 2m2

comp = float(input("digite o comprimento da parede: "))
larg = float(input("digite a largura da parede: "))

area = comp * larg

if area > 1:
    print("Area da parede é o equivalente a {:.2f} metros quadrados".format(area))
    tinta = area / 2.00
    print(" serão usadas {:.1f} litros de tinta para pintar essa parede.".format(tinta))

elif area == 1:
    print("Area da parede é o equivalente a {:.2f} metros quadrados".format(area))
    print(" sera usada 1 litro de tinta para pintar essa parede.")
else:
    print("Area da parede é o equivalente a {:.2f} metros quadrados".format(area))
    print(" sera usada menos de 1 litro de tinta para pintar essa parede.")
