print("soma dos multiplos de 3 entre 1 a 500!")
s=0
cont =0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont = cont + 1 # cont += 1
        s = s + c # s += c
print("a soma de todos os {} foi {}".format(cont,s))
