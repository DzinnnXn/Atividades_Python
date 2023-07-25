import os

s = 1
while s == 1:

    x = int(input("Informe um número: "))

    while x > -1:
        print(f"{x}")
        x -= 1

    print("Deseja sair")
    print("SIM - Y")
    print("NÃO - N")
    y = input("")

    y = y.upper()

    s = 0
    
