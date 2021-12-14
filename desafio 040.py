#calcule a nota e informe se ficou reprovado, recuperação ou aprovado

n1 = float(input("informe a primeira nota do aluno: "))
n2 = float(input("informe a segunda nota do aluno:"))
re = (n1 + n2 ) / 2

if re < 5 :
    print("Sua nota foi {:.2f}".format(re))
    print("Reprovado")
    print(type(re))
elif re == 5 and re <= 6.9: #ou  7 > re >= 5
    print("Sua nota foi {:.2f}".format(re))
    print("Recuperação")
    print(type(re))
else:
    print("Sua nota foi {:.1f}".format(re))
    print("Aprovado")