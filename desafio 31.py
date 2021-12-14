#programa que calcule a distancia de uma viagem em km. sendo R$0.50 por km ate 200km .. passando
# de 200 fica R$0.45 por km


vk = float(input("informe a distancia da viagem que vai fazer: \nKm:"))
#via = vk * 0.50 if vk <= 200 else via = vk * 0.45
if vk <= 200:
    via = vk * 0.50
    print("o preço da sua viagem vai ficar em R${:.1f}".format(via))
else:
    via = vk * 0.45
    print("Passou de 200KM sua viagem então o preço vai ficar em R${:.1f}".format(via))