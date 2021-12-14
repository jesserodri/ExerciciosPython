# programa que mostra o dobro, triplo e raiz quadrado do numero digitado

num = int(input("digite o numero que deseja: "))

dob = num * 2
tri = num * 3
raiz = num ** 0.5 # ou (1/2)   # raiz = math.pow(num, 1/2)    >>precisa importar math

str(print("{} \n Dobro: {}\n Triplo: {}\n Raiz: {:.2f}".format(num, dob, tri, raiz))) #(num, (num*2), (num*3), (num**(1/2)

