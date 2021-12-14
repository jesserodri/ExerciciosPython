#informe um numero inteiro qualquer e qual conversão binario, octal ou hexadecimal
num = int(input("informe o numero inteiro para conversão: \n"))
print('''Escolha uma das bases para fazer a conversão:

[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal
''')
opcao = int(input(("opção: ")))

if opcao == 1:
    print("{}  convertido para o binario é igual a {}".format(num, bin(num)[2:]))# esse 2: é tratamento de texto

elif opcao == 2:
    print("{}  cnvertido para o octal é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{}  convertido para o hexadecimal é igual a {}".format(num, hex(num)[2:]))
else:
    print("tente novamente!")


# preciso ver como faz conversao para outros tipos numericos