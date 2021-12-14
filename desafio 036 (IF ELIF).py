# consultar valor de emprestimo para financiamento de imovel
Valor_Casa = float(input("informe o valor da casa: "))
Sal_com =  float(input("informe o seu salario atualmente: "))
Anos_pg = float(input("informe em quantos anos deseja pagar o imovel: "))

x = Sal_com * 30 / 100
y = Valor_Casa / (Anos_pg * 12)
#print(x,y)


if x <= y:
    print(" \033[31mEmprestimo NEGADO!\033[m \n as parcelas estão acima dos 30% permitidos")
    print("valor parcela {}\n valor dos 30% do seu salario: {} ".format(y,x))
else:
    print("Parabens, voce pode obter o emprestimo")
    print("valor da parcela é {:.2f}\n valor dos 30% do seu salario: {:.2f} ".format(y, x))
