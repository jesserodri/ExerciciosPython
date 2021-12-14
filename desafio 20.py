#leia o nome dos 4 alunos e apresente a ordem que devem apresentar o trabalho
import random
#from random import shuffle   maneira de importar somente o que precisa

l1 = input('primeiro aluno: ')
l2 = input('segundo aluno: ')
l3 = input('terceiro aluno: ')
l4 = input('quarto aluno: ')
alunos = [l1,l2,l3,l4]# isso aqui é um lista

random.shuffle(alunos) # embaralha a lista  /  se importar somente o shuffle nao precisa colocar o random.

print("a ordem de apresentação será")
print(alunos)