# conversor de temperatura - converter graus em fahrenheit
print(" 1 - ceulsis para fahrenheit")
print(" 2 - fahrenheit para ceulsis")
esc = int(input("escolha uma conversão: "))
if esc == 1:
    tempc = float(input("digite a temperatura em ceulsius para converter em fahrenheit: "))
    tempf = (tempc * 9/5) + 32
    print("a conversão de {}ºC fica {}ºF ".format(tempc, tempf))
elif esc ==2:
    tempf = float(input("digite a temperatura em fahrenheit para converter em ceulsius: "))
    tempc = (tempf - 32) * 5/9
    print("a conversao de {}ºF fica {:.1f}ºC".format(tempf, tempc))
else:
    print("Voce digitou um numero invalido!")