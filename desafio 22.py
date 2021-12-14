# leia o nome da pessoa e mostre algumas funcionalidades da manipulação de textos

nome = input("Digite o seu nome completo: ").strip() #ja vai eliminar os espaços antes e depois na frase

print(nome.upper())# palavras todas em maiusculas
print(nome.lower())#palavras todas em minusculas
print(nome.title()) # maiusculas em todas as palavras
print(nome.capitalize()) #maiuscula na primeira palavra
print("nome inteiro com espaço",len(nome.strip())) # conta espaço somente no meio da frase
print("nome inteiro sem espaço",len(nome.replace(" ", ""))) # sem espaço  .replace usado nesse contexto substitui espaço em
                               #len(nome)-nome.count('')))             # branco por string vazia

print("primeiro nome tem {} letras".format(len(nome.split()[0]))) # tranforma em lista o nome colocado e mostra a quantidade de numeros do
                                         #(nome.find(' '))))                      # primeiro nome
                                    # o