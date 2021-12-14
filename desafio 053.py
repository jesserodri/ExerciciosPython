frase= str(input("digite a frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]
''' da para fazer com um simples tratamento de texto ! e não com o for '''

'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print("A frase é um palindromo !")
    print("O inverso de {} é {}".format(junto, inverso))
else:
    print("A frase não é um palindromo !")