# calcular se 3 medidas pode formar um triangulo

r1 = float(input("primeira medida: "))
r2 = float(input("segunda medida: "))
r3 = float(input("terceira medida: "))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print("podem fazer um triangulo")
else:
    print("não pode fazer um triangulo")


'''
NÃO CONSEGUI FAZER
if m1 > m3 and m2 > m3:
    c = m1 + m2 > m3
    if  c :
        print("com essas medidas nao da para formar um triangulo")
    else:
        print("da para formar um triangulo")
    if m2 + m1 > m3:
        print("com essas medidas nao da para formar um triangulo")
    else:
        print(" da para formar um triangulo")
'''