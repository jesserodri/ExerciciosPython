cont = 1
from datetime import date

ma = 0
me = 0
for c in range(7) :
    p = int(input("Em que ano a {}ªpessoa nasceu: ".format(cont)))
    cont = cont + 1
    j = date.today().year - p
    if j >= 18:
        ma +=1
    elif j < 18:
        me += 1

print("\n\nExistem {} pessoas maiores de idade".format(ma))
print("Existem {} pessoas menores de idade".format(me))