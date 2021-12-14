# leia o nome da pessoa e mostre o primeiro e ultimo some separadamente

n = str(input("digite o seu nome inteiro: ")).strip()
nome = n.split()
print("o primeiro: {}".format(nome[0]))
print("o ultimo: {} ".format(nome[len(nome)-1]))# como nao temos como saber quantos sobrenomes tem utilizamos.. -1
#                                                assim o codigo pega o ultimo