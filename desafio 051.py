p = int(input("escolha o primeiro termo: "))
r = int(input("escolha a razão: "))
decimo = p + (11 - 1) * r # formula para designar o decimo
for c in range(p, decimo, r):
    print('{}'.format(c), end=' > ')
print("acabou")
