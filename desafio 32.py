#ano bissexto

#update do ano atual Date

ano = int(input('digite algum ano para analisarmos se é bissexto: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("ano bissexto!")
else:
    print("Não é bissexto!")

