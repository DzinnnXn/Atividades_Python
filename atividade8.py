import os

x = int(input("Informe o ano: "))

y = x % 4
w = x % 100

if y == 0 and w == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
    
    os.system("pause")