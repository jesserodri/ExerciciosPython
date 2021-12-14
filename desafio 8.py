#  programa que mostre o numero de metros para centimetros e milimetros att: dam, hm, km

met = float(input("Digite um valor em metros: "))
cen = met * 100
mili = met * 1000
dam = met * 0.1
hm = met * 0.01
km = met * 0.001
print("{} Metros é o mesmo que {} centimetros. \n {} milimetros".format(met, cen, mili))
print("{} decametro\n {}  hectômetro \n {} quilometro".format(dam,hm,km))