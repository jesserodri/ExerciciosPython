#leia os 4 nomes dos alunos e sortei um deles para apagar o quadro
import random

l1 = input("digite o nome do primeiro aluno: ")
l2 = input("digite o nome do segundo aluno: ")
l3 = input("digite o nome do terceiro aluno: ")
l4 = input("digite o nome do quarto aluno: ")

print(" 1. aluno = {} \n 2. aluno = {} \n 3. aluno = {} \n 4. aluno = {}\n\n".format(l1,l2,l3,l4))

num = random.randint(1,4)
if num == 1:
    print("o aluno escolhido foi o {}".format(l1))
if num == 2:
    print("o aluno escolhido foi o {}".format(l2))
elif num == 3:
    print("o aluno escolhido foi o {}".format(l3))
else:
    print("o aluno escolhido foi o {}".format(l4))

    # um jeito mais facil e SIMPLES de fazer :
lista = [l1,l2,l3,l4]

esc = random.choice(lista)

print("(jeito facilitado) o aluno escolhido foi {}".format(esc))