# programa que leia os km/s e se ultrapassar multa proporcional a velocidade
mul = 7
vperm = 80
vcar = int(input("Digite em km/s qual foi a velocidade do carro no momento do radar:  "))

if vcar > vperm:
    print("Você foi multado por passar do limite de velocidade!")
    print("sua multa ficou no valor de R${}".format((vcar - vperm) * 7))
else:
    print("você passou no radar dentro do limite permitido !")
# não precisa do else isso chamamos de condição simples! com else fica condição composta