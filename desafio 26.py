#faça um programa que leia uma frase e mostre quantas vezes aparece o 'a', qual posição aparee primeiro
# e em que posição aparece a ultima vez

n = str(input("digite uma frase qualquer: ")).strip().lower()

print('quantos a tem: {}'.format(n.count('a'))) # aqui usa o format ... se quiser
print('o primeiro a está na posição: ',n.find('a')+1) # ou n.lfind('a') \ o +1 depois do ('a') foi usado para que
#                                                      a posição inicial nao fosse 0
print('o ultimo a está na posição: ',n.rfind('a')+1)
