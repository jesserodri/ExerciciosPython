#leia o nome de uma cidade e mostre se o nome começa ou nao com santos

c = input("qual é o nome da sua cidade: ").strip() #remove os espaços do começo e inicio

print(c[:5].upper()=='SANTO')

#print('santo' in c.split()[0])