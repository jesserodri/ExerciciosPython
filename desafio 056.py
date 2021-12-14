# --------------------------Declarando variaveis iniciais-----------------------
mediaIdade = 0
somaidade = 0
maisVelho = 0
maisJovem = 0
contM = 0
contF = 0
nomeVelho = ''
totmulher20 = 0
# ---------------------------------------------------------------------------------
                                #inicio
for p in range(1, 5):
    print("Dados da {}ª pessoa: ".format(p))
    nome = str(input(("\ninforme o seu nome: "))).strip().upper()
    sexo = str(input("informe o sexo M ou F: ")).strip().upper()
    idade = int(input("informe sua idade: "))
    somaidade += idade

# verificação da idade e nome
    if p == 1 and sexo in 'Mm':  # inves de sexo == 'm' colocasse IN para ambos os m's
        maisVelho = idade
        nomeVelho = nome
        maisJovem = idade
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    else:
        if idade < maisJovem:
            maisJovem = idade

    # Contagem dos sexos
    if sexo == 'M':
        contM += 1
    if sexo == 'F':
        contF += 1

mediaIdade = somaidade / p

# ---------------------------Exibição dos resultados-----------------------
print("A media de idade do grupo é {}".format(mediaIdade))
print("Tem ao todo {} mulheres com menos de 20 anos de idade".format(totmulher20))
print("o mais velho do grupo tem {} de idade e seu nome é {}\n".format(maisVelho, nomeVelho))

print(("informações adicionais:"))
print(" o mais Jovem do grupo tem {} de idade".format(maisJovem))
print(" Tem {} Pessoas que são do sexo Masculino".format(contM))
print(" Tem {} Pessoas que são do sexo feminino".format(contF))
