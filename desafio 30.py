#criar um programa que informe se o numero é par ou impar !

n =  int(input("informe um numero inteiro: "))
r = n % 2
print('seu numero é impar!' if r == 1 else 'seu numero é par!')

#ou

#if r == 1:
 #   print("seu numero é impar !")
#else:
#    print("seu numero é par! ")
