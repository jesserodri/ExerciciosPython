#programa que calcula o valor a ser pago por um produto considerando seu preço normal e cond/pagamento
import random
import time
prod = {"cadeira","telefone","carregador","fonte"}
#val = random.randint(30,50)
val = float(input("preço das compras: R$"))
print("O valor do seu produto é de {}".format(val))
time.sleep(2)
print("temos algumas formas de pagamento, são elas:")
time.sleep(0.5)
print("1- A vista/cheque\n2- A vista/cartão\n3- 2x no cartão\n4- 3x ou mais no cartão\n  "
      "         A vista/cheque 10% desconto e cartão 5% desconto a"
      "         No cartão parcelado, preço normal")
esc = int(input("qual a forma de pagamento que deseja: "))
if esc == 1:
      print("o produto saira com o preço de: R${}".format(val-(val * 10 / 100)))
elif esc == 2:
      print("o produto saira com o preço de R${}".format(val-(val* 5 / 100)))
elif esc == 3:
      print("o produto saira com o preço de: {} dividido em 2x de R${}".format(val, val/2))
elif esc == 4:
      es = int(input("Quantas parcelas: "))
      if es != 0:
            print("O preço do produto sera de R${}".format(val/es))

else:
      print("essa opção nao é valida !")