#mesma proposta do 035 mas agora tem que classificar os tipos de tringulos que serão formados
r1 = float(input("primeira medida: "))
r2 = float(input("segunda medida: "))
r3 = float(input("terceira medida: "))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print("podem fazer um triangulo")
    if r1 != r2 != r3 != r1:
        print("esse triangulo é um ESCALENO")
    elif r1 == r2 == r3:
        print(" esse triangulo é um Equilátero")
    else:
        print("esse triangulo é um Isósceles")
else:
    print("não pode fazer um triangulo")