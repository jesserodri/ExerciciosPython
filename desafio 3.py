#programa que faz a soma de dois numeros
n1 =int( input ('fale o primeiro numero')) #aqui eu coloquei int para formatar
n2 =int (input ('fale o segundo numero'))   # o input em tipo inteiro

#n1_int = int(n1 ) # modo de conversao extensa
#n2_int = int(n2 ) # modo de conversao extensa

soma = n1 + n2         ##n1_int + n2_int     #precisei fazer a conversao
                                     # pois o type do arquivo estava em STR 

print ('a soma entre {} e {} é {}'.format(n1,n2,soma))
# ou somente
print('ou')
print('a soma é',soma)
